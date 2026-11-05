"""Solve the missing-code tasks with the local retrieval index and an LLM."""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys
from pathlib import Path
from textwrap import dedent
from typing import Any


ASSIGNMENTS_DIR = Path(__file__).parents[1]
WEEK_ROOT = ASSIGNMENTS_DIR.parent
TARGET_ROOT = WEEK_ROOT / "AI4SE_Playground"
DEFAULT_TASKS = ASSIGNMENTS_DIR / "missing_code.json"
DEFAULT_INDEX = ASSIGNMENTS_DIR / "Task_3" / "chunk_embeddings.json"
DEFAULT_MODEL = "gpt-6-luna"
ALLOWED_MODELS = {
    "gpt-6-luna",
    "gpt-5.6-luna",
    "gpt-5.4-nano",
    "gpt-5-nano",
    "gpt-5-mini",
    "gpt-4.1-nano",
    "gpt-4o-mini",
}


def load_tasks(path: Path) -> list[dict[str, str]]:
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError(f"Expected a JSON list in {path}")
    return tasks


def build_query(task: dict[str, str]) -> str:
    return (
        f"Implement {task['class']}.{task['method']} in {task['file']}.\n"
        f"Required behavior:\n{task['docstring']}"
    )


def build_prompt(
    task: dict[str, str],
    matches: list[dict[str, Any]],
) -> str:
    context = "\n\n".join(
        f"--- {match['id']} (similarity {match['score']:.4f}) ---\n"
        f"{match['content']}"
        for match in matches
    )
    return dedent(
        f"""\
        You are implementing one missing method in an existing Python repository.

        Target file: {task['file']}
        Target class: {task['class']}
        Target method: {task['method']}

        Required behavior:
        {task['docstring']}

        Return only the complete Python method definition. Do not use Markdown
        fences. Do not modify or include any other method or class.
        Preserve the existing public interface and repository coding style.

        Relevant repository context:
        {context}
        """
    )


def generate_method(prompt: str, model_name: str) -> str:
    """Generate a method using the established LangChain OpenAI integration."""
    try:
        from dotenv import load_dotenv
    except ImportError as error:
        raise RuntimeError(
            "python-dotenv is required for non-dry-run execution."
        ) from error
    load_dotenv(Path(__file__).with_name(".env"))
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is not configured; use --dry-run to test retrieval."
        )
    try:
        from langchain_openai import ChatOpenAI
    except ImportError as error:
        raise RuntimeError(
            "langchain-openai is required for non-dry-run execution."
        ) from error

    response = ChatOpenAI(model=model_name).invoke(prompt)
    content = response.content
    if not isinstance(content, str):
        raise ValueError("The LLM returned non-text content.")
    return content.strip()


def clean_generated_method(source: str, expected_name: str | None = None) -> str:
    """Extract and normalize a method from the model's response."""
    cleaned = source.strip()
    fenced = re.fullmatch(r"```(?:python)?\s*(.*?)```", cleaned, re.DOTALL)
    cleaned = fenced.group(1).strip() if fenced else cleaned
    if expected_name:
        method_line = re.search(
            rf"(?m)^[ \t]*(?:async[ \t]+)?def[ \t]+{re.escape(expected_name)}\b",
            cleaned,
        )
        if method_line:
            cleaned = cleaned[method_line.start():]
    return dedent(cleaned)


def validate_method(source: str, expected_name: str) -> ast.FunctionDef | ast.AsyncFunctionDef:
    cleaned = clean_generated_method(source, expected_name)
    try:
        tree = ast.parse(cleaned)
    except SyntaxError as error:
        raise ValueError(f"Generated method is not valid Python: {error}") from error

    definitions = [
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    if len(definitions) != 1 or definitions[0].name != expected_name:
        raise ValueError(
            f"Expected exactly one method named {expected_name!r} in the response."
        )
    return definitions[0]


def replace_method(
    file_path: Path,
    class_name: str,
    method_name: str,
    generated_source: str,
) -> None:
    original = file_path.read_text(encoding="utf-8")
    tree = ast.parse(original)
    target_class = next(
        (
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef) and node.name == class_name
        ),
        None,
    )
    if target_class is None:
        raise ValueError(f"Class {class_name!r} was not found in {file_path}")

    target_method = next(
        (
            node
            for node in target_class.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name == method_name
        ),
        None,
    )
    if target_method is None:
        raise ValueError(
            f"Method {class_name}.{method_name} was not found in {file_path}"
        )

    generated = clean_generated_method(generated_source, method_name)
    validate_method(generated, method_name)
    original_lines = original.splitlines(keepends=True)
    start = target_method.lineno - 1
    end = target_method.end_lineno
    indentation = re.match(r"[ \t]*", original_lines[start]).group(0)
    replacement = dedent(generated)
    replacement = "\n".join(
        indentation + line if line.strip() else line
        for line in replacement.splitlines()
    )
    if not replacement.endswith("\n"):
        replacement += "\n"
    file_path.write_text(
        "".join(original_lines[:start]) + replacement + "".join(original_lines[end:]),
        encoding="utf-8",
    )


def import_retriever() -> Any:
    """Import Task 4 without duplicating its retrieval implementation."""
    assignments_text = str(ASSIGNMENTS_DIR)
    if assignments_text not in sys.path:
        sys.path.insert(0, assignments_text)
    from Task_4.retrieve_chunks import retrieve

    return retrieve


def run(tasks_path: Path, index_path: Path, model: str, dry_run: bool) -> int:
    retrieve = import_retriever()
    tasks = load_tasks(tasks_path)
    for number, task in enumerate(tasks, start=1):
        identifier = f"{task['class']}.{task['method']}"
        query = build_query(task)
        matches = retrieve(query, index_path=index_path, top_k=5)
        prompt = build_prompt(task, matches)
        print(f"[{number}/{len(tasks)}] {identifier}")
        print(f"  Retrieved {len(matches)} chunks")
        generated = generate_method(prompt, model)
        validate_method(generated, task["method"])
        target_path = TARGET_ROOT / task["file"]
        if dry_run:
            print(f"  Generated and validated; would update {target_path}")
        else:
            replace_method(target_path, task["class"], task["method"], generated)
            print(f"  Updated {target_path}")
    return len(tasks)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tasks", type=Path, default=DEFAULT_TASKS)
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--model", default=DEFAULT_MODEL, choices=sorted(ALLOWED_MODELS))
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="run retrieval and generation without editing source files",
    )
    args = parser.parse_args()
    run(args.tasks, args.index, args.model, args.dry_run)


if __name__ == "__main__":
    main()
