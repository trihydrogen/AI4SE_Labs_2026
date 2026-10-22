"""LangGraph network for refining heterogeneous software requirements."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Literal, TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel, Field


Priority = Literal["MUST", "SHOULD", "COULD", "WONT"]


class CandidateRequirement(BaseModel):
    name: str
    statement: str
    explanation: str
    priority: Priority
    source_documents: list[str]
    source_quotes: list[str] = Field(default_factory=list)


class RequirementSet(BaseModel):
    requirements: list[CandidateRequirement]


class FinalRequirement(BaseModel):
    requirement_id: str
    name: str
    explanation: str
    priority: Priority
    source_documents: list[str]
    source_quotes: list[str] = Field(default_factory=list)


class DiscardedRequirement(BaseModel):
    original_statement: str
    reason: str
    source_documents: list[str]


class NormalizationResult(BaseModel):
    requirements: list[FinalRequirement]
    discarded: list[DiscardedRequirement]


class ValidationResult(BaseModel):
    valid: bool
    problems: list[str] = Field(default_factory=list)
    missing_topics: list[str] = Field(default_factory=list)
    contradictory_requirements: list[str] = Field(default_factory=list)


class GraphState(TypedDict, total=False):
    input_directory: str
    documents: list[dict[str, str]]
    candidates: list[CandidateRequirement]
    normalized: list[FinalRequirement]
    discarded: list[DiscardedRequirement]
    validation: ValidationResult
    retry_count: int
    output_path: str


def _models() -> tuple[ChatOpenAI, ChatOpenAI, ChatOpenAI]:
    """Construct the three intentionally different LLM clients."""
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is not configured. Put it in a local .env file."
        )

    return (
        ChatOpenAI(model="gpt-5.6-luna", temperature=0),
        ChatOpenAI(model="gpt-5.4-nano", temperature=0),
        ChatOpenAI(model="gpt-4o-mini", temperature=0),
    )


def load_documents(state: GraphState) -> GraphState:
    """Load every supported source file below the supplied directory."""
    input_directory = Path(state["input_directory"]).resolve()
    if not input_directory.is_dir():
        raise NotADirectoryError(f"Input directory does not exist: {input_directory}")

    documents: list[dict[str, str]] = []
    for path in sorted(input_directory.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".txt", ".eml"}:
            content = path.read_text(encoding="utf-8", errors="replace").strip()
            if content:
                documents.append(
                    {
                        "document_id": path.relative_to(input_directory).as_posix(),
                        "content": content,
                    }
                )

    if not documents:
        raise ValueError(f"No non-empty .txt or .eml files found in {input_directory}")

    return {**state, "documents": documents, "retry_count": 0}


def _documents_text(documents: list[dict[str, str]]) -> str:
    return "\n\n".join(
        f"DOCUMENT: {document['document_id']}\n{document['content']}"
        for document in documents
    )


def extract_requirements(state: GraphState) -> GraphState:
    extractor, _, _ = _models()
    prompt = f"""
You are a software requirements analyst. Extract every candidate software
requirement from the source documents below.

Rules:
- Do not ignore requirements from emails, interviews, meetings, or drafts.
- Ignore greetings, jokes, personal stories, and unrelated discussion.
- Do not merge candidates yet.
- Do not invent details unsupported by the documents.
- Preserve source document IDs and provide supporting quotes.
- Include functional and non-functional requirements.
- Use this priority scale: MUST (essential or explicitly critical), SHOULD
  (important), COULD (useful optional capability), WONT (explicitly excluded
  or deferred).

Return only structured data matching the requested schema.

SOURCE DOCUMENTS:
{_documents_text(state["documents"])}
"""
    result = extractor.with_structured_output(RequirementSet).invoke(prompt)
    return {**state, "candidates": result.requirements}


def _candidate_text(candidates: list[CandidateRequirement]) -> str:
    return "\n\n".join(
        candidate.model_dump_json(indent=2) for candidate in candidates
    )


def _normalize(state: GraphState, prompt_prefix: str = "") -> GraphState:
    _, normalizer, _ = _models()
    prompt = f"""
You are a senior requirements engineer. Normalize the candidate requirements
below into a complete, consistent requirements set.

Tasks:
- Merge semantically duplicate requirements.
- Preserve every source document contributing to a merged requirement.
- Use consistent terminology and clear paragraph-long explanations.
- Assign sequential IDs in the format REQ-001, REQ-002, and so on.
- Preserve the priority scale: MUST, SHOULD, COULD, WONT.
- Detect contradictions and resolve them conservatively.
- Put unsupported, nonsensical, or irreconcilably conflicting candidates in
  the discarded list, with a specific reason and source documents.
- Never silently delete a candidate and never invent functionality.

{prompt_prefix}

CANDIDATES:
{_candidate_text(state["candidates"])}
"""
    result = normalizer.with_structured_output(NormalizationResult).invoke(prompt)
    return {
        **state,
        "normalized": result.requirements,
        "discarded": result.discarded,
    }


def normalize_requirements(state: GraphState) -> GraphState:
    return _normalize(state)


def validate_requirements(state: GraphState) -> GraphState:
    _, _, validator = _models()
    requirements = "\n\n".join(
        requirement.model_dump_json(indent=2)
        for requirement in state["normalized"]
    )
    document_ids = [document["document_id"] for document in state["documents"]]
    prompt = f"""
Review this requirements specification against the original document IDs.
Return valid=true only when all checks pass.

Check:
1. Every requirement has a unique ID, name, paragraph explanation, priority,
   and at least one source document.
2. Semantic duplicates are merged.
3. Requirements are mutually consistent and terminology is consistent.
4. Important requirements from the source corpus are not missing.
5. Discarded candidates have reasons and source documents.

ORIGINAL DOCUMENT IDS:
{document_ids}

NORMALIZED REQUIREMENTS:
{requirements}
"""
    result = validator.with_structured_output(ValidationResult).invoke(prompt)
    return {**state, "validation": result}


def validation_router(state: GraphState) -> str:
    validation = state["validation"]
    if validation.valid or state.get("retry_count", 0) >= 2:
        return "render"
    return "revise"


def revise_requirements(state: GraphState) -> GraphState:
    validation = state["validation"]
    feedback = "\n".join(
        [
            *validation.problems,
            *[f"Missing topic: {topic}" for topic in validation.missing_topics],
            *[
                f"Contradiction: {item}"
                for item in validation.contradictory_requirements
            ],
        ]
    )
    revised = _normalize(
        state,
        "Revise the complete set using this validator feedback. Preserve all "
        f"source tracing and do not silently remove requirements:\n{feedback}",
    )
    return {**revised, "retry_count": state.get("retry_count", 0) + 1}


def render_document(state: GraphState) -> GraphState:
    output_path = Path(state["output_path"]).resolve()
    lines = [
        "# Software Requirements Specification",
        "",
        "## Priority Scale",
        "",
        "- **MUST**: Required for the system to be acceptable.",
        "- **SHOULD**: Important, but the system may operate without it.",
        "- **COULD**: Desirable optional functionality.",
        "- **WONT**: Explicitly excluded or deferred.",
        "",
        "## Requirements",
        "",
    ]
    for requirement in state["normalized"]:
        lines.extend(
            [
                f"### {requirement.requirement_id}: {requirement.name}",
                "",
                requirement.explanation,
                "",
                f"**Priority:** {requirement.priority}",
                "",
                "**Traceability:**",
                *[f"- `{source}`" for source in requirement.source_documents],
            ]
        )
        if requirement.source_quotes:
            lines.extend(["", "**Evidence:**", *[
                f"> {quote}" for quote in requirement.source_quotes
            ]])
        lines.append("")

    lines.extend(["## Discarded Requirements", ""])
    for discarded in state["discarded"]:
        lines.extend(
            [
                "### Discarded candidate",
                "",
                f"**Original statement:** {discarded.original_statement}",
                "",
                f"**Reason:** {discarded.reason}",
                "",
                "**Sources:**",
                *[f"- `{source}`" for source in discarded.source_documents],
                "",
            ]
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return {**state, "output_path": str(output_path)}


def build_graph():
    graph = StateGraph(GraphState)
    graph.add_node("load_documents", load_documents)
    graph.add_node("extract_requirements", extract_requirements)
    graph.add_node("normalize_requirements", normalize_requirements)
    graph.add_node("validate_requirements", validate_requirements)
    graph.add_node("revise_requirements", revise_requirements)
    graph.add_node("render_document", render_document)
    graph.add_edge(START, "load_documents")
    graph.add_edge("load_documents", "extract_requirements")
    graph.add_edge("extract_requirements", "normalize_requirements")
    graph.add_edge("normalize_requirements", "validate_requirements")
    graph.add_conditional_edges(
        "validate_requirements",
        validation_router,
        {"revise": "revise_requirements", "render": "render_document"},
    )
    graph.add_edge("revise_requirements", "validate_requirements")
    graph.add_edge("render_document", END)
    return graph.compile()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a traceable requirements document from a corpus."
    )
    parser.add_argument("input_directory", help="Directory containing .txt and .eml files")
    parser.add_argument(
        "--output",
        default="requirements_document.md",
        help="Output Markdown path (default: requirements_document.md)",
    )
    args = parser.parse_args()

    load_dotenv()
    result = build_graph().invoke(
        {
            "input_directory": args.input_directory,
            "output_path": args.output,
        }
    )
    print(f"Generated: {result['output_path']}")
    print(f"Requirements: {len(result['normalized'])}")
    print(f"Discarded: {len(result['discarded'])}")
    print(f"Validation passed: {result['validation'].valid}")


if __name__ == "__main__":
    main()
