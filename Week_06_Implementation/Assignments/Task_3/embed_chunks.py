"""Create a local JSON embedding index for the repository chunks.

The embedding is a deterministic 256-dimensional hashed TF-IDF vector.  It
uses only the Python standard library, so no embedding API or model download
is required.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any


DIMENSIONS = 256
TOKEN_PATTERN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|[0-9]+")
DEFAULT_CHUNKS = Path(__file__).parents[1] / "Task_2" / "repository_chunks.json"
DEFAULT_OUTPUT = Path(__file__).with_name("chunk_embeddings.json")


def tokens(text: str) -> list[str]:
    """Return source-code and natural-language tokens from ``text``."""
    return [match.group(0).lower() for match in TOKEN_PATTERN.finditer(text)]


def bucket(token: str) -> int:
    """Map a token deterministically to one embedding dimension."""
    digest = hashlib.sha256(token.encode("utf-8")).digest()
    return int.from_bytes(digest[:4], "big") % DIMENSIONS


def vectorize(text: str, idf: list[float]) -> list[float]:
    """Create a length-normalized hashed TF-IDF vector."""
    counts = Counter(tokens(text))
    vector = [0.0] * DIMENSIONS
    for token, count in counts.items():
        vector[bucket(token)] += (1.0 + math.log(count)) * idf[bucket(token)]

    norm = math.sqrt(sum(value * value for value in vector))
    return [value / norm for value in vector] if norm else vector


def embedding_text(chunk: dict[str, Any]) -> str:
    """Include location metadata so identifiers remain searchable."""
    return f"File: {chunk['file']}\nSource:\n{chunk['content']}"


def build_index(chunks_path: Path, output_path: Path) -> None:
    chunks = json.loads(chunks_path.read_text(encoding="utf-8"))
    if not isinstance(chunks, list):
        raise ValueError(f"Expected a JSON list of chunks in {chunks_path}")

    document_frequencies = [0] * DIMENSIONS
    for chunk in chunks:
        seen = {bucket(token) for token in set(tokens(embedding_text(chunk)))}
        for index in seen:
            document_frequencies[index] += 1

    document_count = len(chunks)
    idf = [
        math.log((document_count + 1) / (frequency + 1)) + 1
        for frequency in document_frequencies
    ]
    embeddings = [
        {
            "id": chunk["id"],
            "file": chunk["file"],
            "start_line": chunk["start_line"],
            "end_line": chunk["end_line"],
            "content": chunk["content"],
            "embedding": vectorize(embedding_text(chunk), idf),
        }
        for chunk in chunks
    ]

    output = {
        "format": "hashed-tfidf-v1",
        "dimensions": DIMENSIONS,
        "idf": idf,
        "chunks": embeddings,
    }
    output_path.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(embeddings)} chunk embeddings to {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chunks", type=Path, default=DEFAULT_CHUNKS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    build_index(args.chunks, args.output)


if __name__ == "__main__":
    main()
