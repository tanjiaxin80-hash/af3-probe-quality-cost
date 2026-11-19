from csv import DictReader
from math import comb, isclose, sqrt
from pathlib import Path
from statistics import mean, stdev
import json

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "figure_data"


def load(path):
    with (DATA / path).open(encoding="utf-8-sig", newline="") as stream:
        return list(DictReader(stream))


def binomial_upper_limit(events, count, alpha=0.05):
    lower, upper = 0.0, 1.0
    for _ in range(70):
        p = (lower + upper) / 2
        tail = sum(comb(count, k) * p**k * (1 - p)**(count - k)
                   for k in range(events + 1))
        if tail > alpha:
            lower = p
        else:
            upper = p
    return (lower + upper) / 2


def summarize():
    costs = {row["method"]: row for row in load("main/figure3.csv")}
    fixed = costs["DEVELOPMENT_SELECTED_BEST_FIXED"]
    feedback = costs["FULL_FEEDBACK"]
    probe = float(feedback["probe_seconds"])
    wall_difference = float(feedback["cached_wall_seconds"]) - float(fixed["cached_wall_seconds"])
    allowance = probe - wall_difference
    pairs = [row for row in load("main/figure4_actual.csv") if row["method"] == "FULL_FEEDBACK"]
    assert len(pairs) == len({row["target_id"] for row in pairs}) == 10
    assert isclose(sum(float(r["probe_budget_at_break_even_seconds"]) for r in pairs), allowance)
    zero_probe_excess = sum(float(row["probe_budget_at_break_even_seconds"]) < 0 for row in pairs)

    methods = {r["method"]: r for r in load("all12_frozen_method_context.csv")}
    held_out = methods["FULL_FEEDBACK"]
    records = load("supplement/decision_classification_all75.csv")
    deltas = [float(row["final_TM_difference"]) for row in records]
    count = len(deltas)
    assert count == len({row["group"] for row in records}) == int(held_out["P3_evaluable"]) == 75
    events = sum(row["final_within_tolerance"].lower() == "false" for row in records)
    assert events == int(held_out["events"])
    # Two-sided 95% Student t quantile at the prespecified 74 degrees of freedom.
    half_width = 1.992543495 * stdev(deltas) / sqrt(count)
    center = mean(deltas)

    return {
        "measured_probe_seconds": round(probe, 3),
        "break_even_probe_seconds": round(allowance, 3),
        "required_probe_reduction_percent": round(100 * wall_difference / probe, 2),
        "paths_costlier_than_fixed_P3_with_zero_probe_time": zero_probe_excess,
        "audited_paths": len(pairs),
        "cached_wall_time_increase_percent": round(100 * wall_difference / float(fixed["cached_wall_seconds"]), 2),
        "audit_composite_cost_increase_percent": round(100 * wall_difference / float(fixed["composite_seconds"]), 2),
        "held_out_groups": int(held_out["targets"]),
        "held_out_valid_returns": int(held_out["valid_returns"]),
        "held_out_evaluable_groups": count,
        "TM_score_loss_events": events,
        "observed_loss_percent": round(100 * events / count, 2),
        "one_sided_95_percent_upper_limit_assuming_independent_binomial_outcomes": round(100 * binomial_upper_limit(events, count), 2),
        "mean_paired_TM_score_difference": round(center, 6),
        "paired_TM_score_difference_95_percent_t_interval": [round(center - half_width, 6), round(center + half_width, 6)],
    }


if __name__ == "__main__":
    print(json.dumps(summarize(), indent=2))
