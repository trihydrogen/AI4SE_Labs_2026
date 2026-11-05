"""Retrieve the most relevant repository chunks from a JSON embedding index."""

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
DEFAULT_INDEX = (
    Path(__file__).parents[1] / "Task_3" / "chunk_embeddings.json"
)


def tokens(text: str) -> list[str]:
    return [match.group(0).lower() for match in TOKEN_PATTERN.finditer(text)]


def bucket(token: str) -> int:
    digest = hashlib.sha256(token.encode("utf-8")).digest()
    return int.from_bytes(digest[:4], "big") % DIMENSIONS


def query_vector(query: str, idf: list[float]) -> list[float]:
    counts = Counter(tokens(query))
    vector = [0.0] * DIMENSIONS
    for token, count in counts.items():
        vector[bucket(token)] += (1.0 + math.log(count)) * idf[bucket(token)]
    norm = math.sqrt(sum(value * value for value in vector))
    return [value / norm for value in vector] if norm else vector


def retrieve(
    query: str,
    index_path: Path = DEFAULT_INDEX,
    top_k: int = 5,
) -> list[dict[str, Any]]:
    """Return up to ``top_k`` chunks ordered by cosine similarity."""
    index = json.loads(index_path.read_text(encoding="utf-8"))
    if index.get("format") != "hashed-tfidf-v1":
        raise ValueError(f"Unsupported embedding format in {index_path}")
    idf = index["idf"]
    query_embedding = query_vector(query, idf)

    matches = []
    for chunk in index["chunks"]:
        score = sum(
            query_value * chunk_value
            for query_value, chunk_value in zip(query_embedding, chunk["embedding"])
        )
        matches.append({**chunk, "score": score})
    return sorted(matches, key=lambda match: match["score"], reverse=True)[:top_k]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("-k", "--top-k", type=int, default=5)
    args = parser.parse_args()
    if args.top_k < 1:
        parser.error("--top-k must be positive")

    for match in retrieve(args.query, args.index, args.top_k):
        print(
            f"{match['score']:.4f} {match['id']}\n"
            f"{match['content']}\n"
            f"{'-' * 60}"
        )


if __name__ == "__main__":
    main()
