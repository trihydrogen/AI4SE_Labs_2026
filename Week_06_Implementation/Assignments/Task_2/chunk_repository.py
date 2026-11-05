from __future__ import annotations

import json
from pathlib import Path


CHUNK_SIZE = 120
OVERLAP = 20

SOURCE_ROOT = Path(__file__).parents[2] / "AI4SE_Playground"
OUTPUT_FILE = Path(__file__).with_name("repository_chunks.json")

EXCLUDED_PARTS = {".git", "__pycache__", ".venv", ".pytest_cache"}


def should_include(path: Path) -> bool:
    """Return whether the file should be included in the repository index."""
    return path.suffix == ".py" and not any(
        part in EXCLUDED_PARTS for part in path.parts
    )


def chunk_file(path: Path) -> list[dict[str, object]]:
    """Split one source file into overlapping line-based chunks."""
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    relative_path = path.relative_to(SOURCE_ROOT).as_posix()
    chunks: list[dict[str, object]] = []
    step = CHUNK_SIZE - OVERLAP

    for start in range(0, len(lines), step):
        end = min(start + CHUNK_SIZE, len(lines))
        chunks.append(
            {
                "id": f"{relative_path}:{start + 1}-{end}",
                "file": relative_path,
                "start_line": start + 1,
                "end_line": end,
                "content": "".join(lines[start:end]),
            }
        )
        if end == len(lines):
            break

    return chunks


def build_chunks() -> list[dict[str, object]]:
    """Build chunks for all included Python files."""
    chunks: list[dict[str, object]] = []
    for path in sorted(SOURCE_ROOT.rglob("*.py")):
        if should_include(path):
            chunks.extend(chunk_file(path))
    return chunks


def main() -> None:
    chunks = build_chunks()
    OUTPUT_FILE.write_text(
        json.dumps(chunks, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(chunks)} chunks to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
