# Coding Agent Benchmark Lab

Original **synthetic** coding-agent benchmark demonstration for pre-contract portfolio use. No client data or actual AI-agent evaluation is claimed.

## Contents
- `TASK.md`: explicit requirements and grading contract
- `candidate.py`: intentionally flawed illustrative candidate
- `reference.py`: deterministic reference implementation
- `tests/test_reconcile.py`: 10 tests covering valid and invalid inputs
- `evaluate.py`: four transparent public examples
- `Dockerfile`: Python version-tag and pytest version pinned

## Run
```bash
python -m pip install -r requirements.txt
python -m pytest -q
python evaluate.py reference
python evaluate.py candidate # expected nonzero exit
docker build -t benchmark-demo . && docker run --rm benchmark-demo
```

## Integrity limitations
The tests exercise the reference implementation, not arbitrary candidate submissions. The public evaluator is illustrative, **not** tamper-resistant or hidden. The Docker base is a pinned version tag rather than an immutable digest. No independent adjudication of difficulty or measured real-agent success rate is claimed. A production benchmark needs candidate isolation, time/resource limits, immutable image digests, private test separation and independent review.
