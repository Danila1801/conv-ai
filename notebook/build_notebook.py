"""Turn a .py file with '# %%' cell marks into a Jupyter notebook.

Why: several of us work on the project at the same time. A .ipynb is one big JSON file and
merges badly in git. Plain .py files merge fine. So we write cells in .py files and build
the notebook from them.

Usage:
    python notebook/build_notebook.py pilot/pilot.py pilot/pilot.ipynb
    python notebook/build_notebook.py part1.py part2.py final.ipynb     (several inputs, joined in order)

Cell marks:
    # %%              starts a code cell
    # %% [markdown]   starts a text cell; every line of it starts with "# "
"""
import json
import sys


def split_cells(source):
    """Return a list of (kind, lines) with kind 'code' or 'markdown'."""
    cells, kind, lines = [], None, []
    for line in source.splitlines():
        if line.startswith("# %%"):
            if kind is not None:
                cells.append((kind, lines))
            kind = "markdown" if "[markdown]" in line else "code"
            lines = []
        elif kind is not None:
            lines.append(line)
        elif line.strip():
            # text before the first cell mark becomes a code cell
            kind, lines = "code", [line]
    if kind is not None:
        cells.append((kind, lines))
    return cells


def to_notebook_cell(kind, lines):
    # drop empty lines at the start and the end of a cell
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    if kind == "markdown":
        # "# text" -> "text", "#" -> ""
        lines = [line[2:] if line.startswith("# ") else line.lstrip("#") for line in lines]
    text = [line + "\n" for line in lines[:-1]] + lines[-1:]
    if kind == "markdown":
        return {"cell_type": "markdown", "metadata": {}, "source": text}
    return {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": text}


def build(py_paths, ipynb_path):
    cells = []
    for path in py_paths:
        with open(path, encoding="utf-8") as f:
            for kind, lines in split_cells(f.read()):
                if any(line.strip() for line in lines):
                    cells.append(to_notebook_cell(kind, lines))
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }
    with open(ipynb_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=1)
        f.write("\n")
    return len(cells)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    n = build(sys.argv[1:-1], sys.argv[-1])
    print(f"{sys.argv[-1]}: {n} cells")
