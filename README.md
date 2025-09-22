# How to Run

Quick setup and run:

1. Create and activate a virtual environment and install dependencies:

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

2. Start Jupyter and open the demo notebook:

```bash
jupyter notebook demo.ipynb
```

Open and run `demo.ipynb` to see timing comparisons and plots.

Files

- `analysis.py` — Graph building and timing helpers (functions to create the weighted adjacency matrix and run timing experiments).
- `astar.py` — A* search implementation.
- `greedy_search.py` — Greedy Best-First Search implementation.
- `bfs.py` — Breadth-First Search implementation.
- `dfs.py` — Depth-First Search implementation.
- `heuristics.py` — Heuristic functions and straight-line distances.
- `demo.ipynb` — Jupyter notebook that runs the searches, collects timings, and plots results.
- `requirements.txt` — Python dependencies for the notebook and examples.

