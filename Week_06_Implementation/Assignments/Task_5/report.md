# Task 5 report

## Agent design

[`solve_tasks.py`](./solve_tasks.py) combines the earlier tasks. It loads the
task list, builds a query for each missing method, imports `retrieve` from Task
4, and gets the five highest-ranked chunks from Task 3's embedding index.

The chunks are included in a prompt for `gpt-6-luna`, which is asked to return
only the requested method. Before writing changes, the script parses the
response with Python's AST and checks the method name. It then replaces only
that method in the target file.

The target repository is `Week_06_Implementation/AI4SE_Playground`. The
standard task list and embedding index are used by default; `--tasks` and
`--index` select different input files.

## Dry-run mode

With `--dry-run`, the script loads all tasks, retrieves context, calls the LLM,
validates each generated method, and reports the files it would update without
changing the repository:

```bash
python Task_5/solve_tasks.py --dry-run
```

The normal run is:

```bash
python Task_5/solve_tasks.py
```
