"""Eval metrics.

Reported per the README:

- Qualification recall and precision (stratified by tier and crop)
- Tier classification accuracy (confusion matrix)
- Score correlation (Spearman ρ) between agent and founder
- Outreach quality (mean rating)
- Cost per qualified lead, latency p50/p95
- "Missed customer" coverage gap closed

All functions take in-memory data structures only. The runner is responsible
for I/O.
"""

from __future__ import annotations

from collections.abc import Sequence


def precision_recall(
    predicted_qualified: set[str],
    actually_qualified: set[str],
) -> dict[str, float]:
    """Standard P/R. `predicted_qualified` is the set of lead_ids the agent
    marked Tier 1/2/3. `actually_qualified` is the founder's ground truth.
    """
    true_positives = predicted_qualified & actually_qualified
    p = len(true_positives) / len(predicted_qualified) if predicted_qualified else 0.0
    r = len(true_positives) / len(actually_qualified) if actually_qualified else 0.0
    f1 = (2 * p * r / (p + r)) if (p + r) else 0.0
    return {"precision": p, "recall": r, "f1": f1, "n_pred": len(predicted_qualified),
            "n_true": len(actually_qualified)}


def confusion_matrix(
    predicted_tiers: Sequence[str],
    actual_tiers: Sequence[str],
    labels: Sequence[str] = ("tier_1", "tier_2", "tier_3", "unfit"),
) -> dict[str, dict[str, int]]:
    """Counts of predicted-vs-actual tier pairs."""
    if len(predicted_tiers) != len(actual_tiers):
        raise ValueError("Predicted and actual tier sequences must have equal length.")
    out: dict[str, dict[str, int]] = {a: {p: 0 for p in labels} for a in labels}
    for actual, pred in zip(actual_tiers, predicted_tiers, strict=True):
        if actual in out and pred in out[actual]:
            out[actual][pred] += 1
    return out


def spearman_rho(predicted_scores: Sequence[float], actual_scores: Sequence[float]) -> float:
    """Spearman rank correlation. Implemented inline to avoid scipy as a dep
    just for one number; swap for scipy.stats.spearmanr if we ever want p-values.
    """
    if len(predicted_scores) != len(actual_scores):
        raise ValueError("Score sequences must have equal length.")
    n = len(predicted_scores)
    if n < 2:
        return 0.0

    def _rank(values: Sequence[float]) -> list[float]:
        indexed = sorted(range(n), key=lambda i: values[i])
        ranks = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and values[indexed[j + 1]] == values[indexed[i]]:
                j += 1
            avg_rank = (i + j) / 2 + 1
            for k in range(i, j + 1):
                ranks[indexed[k]] = avg_rank
            i = j + 1
        return ranks

    pr, ar = _rank(predicted_scores), _rank(actual_scores)
    d2 = sum((a - b) ** 2 for a, b in zip(pr, ar, strict=True))
    return 1 - (6 * d2) / (n * (n**2 - 1))
