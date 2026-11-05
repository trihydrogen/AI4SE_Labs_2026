# Task 2 Report

## Chunking design

The chunking script recursively scans the repository and includes only `.py`
files. Git metadata, virtual environments, caches, and compiled Python files
are excluded because they are not useful context for solving coding tasks.

Each file is split into chunks of at most 120 lines. Consecutive chunks overlap
by 20 lines. The overlap preserves context when a class, method, import block,
or conditional statement crosses a chunk boundary.

Line-based chunking was chosen because it is simple and easy to implement.
Each chunk stores the relative file path, start line, end line, and source
content. This metadata will later allow a retrieval component to identify
where a relevant piece of context came from.

The chunks are stored in `repository_chunks.json` as a JSON list, as it is
easy to dump and load in Python.
