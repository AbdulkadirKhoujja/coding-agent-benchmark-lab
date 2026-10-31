# Versioned multi-tenant event reconciliation task

Implement `reconcile(events)` in candidate.py. Each event is a dict with nonempty string `tenant` and `key`, nonnegative integer `version` (not bool), and `value`. Return a mapping from `tenant/key` to the value of the greatest version. Out-of-order input is allowed. Identical replays are safe; conflicting values at the same version raise ValueError. Invalid or missing fields raise ValueError. Never merge tenant namespaces or mutate input.

This is a **synthetic benchmark task**; no real coding agent was evaluated.
