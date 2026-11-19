# CSV inventory

Numeric time fields ending in `_seconds` use seconds. A blank cell is missing or inapplicable as defined by the manuscript. Boolean values and category strings are retained verbatim. Quality-score scales follow the manuscript. The inventory describes the files without imputing values.

## `figure_data/all12_frozen_method_context.csv`

Records: 12.

Columns: `method`, `targets`, `valid_returns`, `P3_evaluable`, `events`, `composite_ratio_75`, `status`.

## `figure_data/main/figure1.csv`

Records: 4.

Columns: `profile`, `n_paired`, `all_targets`, `valid_returns`, `mean_TM_difference`, `TM_CI_low`, `TM_CI_high`, `mean_lDDT_difference`, `lDDT_CI_low`, `lDDT_CI_high`, `inference_ratio`, `composite_ratio`, `interval`, `risk_events`.

## `figure_data/main/figure2.csv`

Records: 2.

Columns: `diagnostic`, `P3_evaluable_targets`, `P3_unevaluable_retained`, `mean_TM_difference`, `mean_lDDT_difference`, `risk_events_by_construction_not_validation`, `inference_seconds`, `P3_inference_seconds`, `inference_ratio`, `composite_replay_seconds`, `P3_composite_replay_seconds`, `composite_ratio`, `same_direct_decision_probe_surcharge_seconds`, `selected_P0`, `selected_P1`, `selected_P3`, `selected_P4`, `requires_posthoc_truth_and_runtime`, `post_hoc_exploratory`.

## `figure_data/main/figure3.csv`

Records: 3.

Columns: `method`, `targets`, `attempts`, `retrieval_seconds`, `probe_seconds`, `upgrade_or_fixed_seconds`, `decision_seconds`, `wrapper_other_seconds`, `cached_wall_seconds`, `composite_seconds`, `reference_composite_seconds`, `native_success_seconds`, `native_failure_seconds`, `UM_seconds`, `lambda_star_unclipped`, `needed_probe_reduction_fraction`, `current_excess_seconds`, `zero_probe_composite_seconds`.

## `figure_data/main/figure4_actual.csv`

Records: 20.

Columns: `target_id`, `method`, `probe_seconds`, `upgrade_seconds`, `decision_seconds`, `wrapper_other_seconds`, `shared_retrieval_seconds`, `reference_composite_seconds`, `reference_inference_seconds`, `current_composite_seconds`, `probe_budget_at_break_even_seconds`, `lambda_star_unclipped`, `inference_only_lambda_star`, `needed_probe_reduction_fraction_if_0_to_1`, `status`, `cost_scope`, `post_hoc_fixed_decisions`.

## `figure_data/main/figure4_curves.csv`

Records: 303.

Columns: `scope`, `method`, `lambda_fraction`, `cost_excess_seconds`.

## `figure_data/main/figure4_replay.csv`

Records: 1.

Columns: `n`, `probe_seconds`, `upgrade_seconds`, `reference_inference_seconds`, `lambda_star_actions_only`, `online_overhead_unknown`.

## `figure_data/supplement/decision_classification_all75.csv`

Records: 75.

Columns: `target_id`, `group`, `classification`, `executed_budgets`, `returned_budget`, `upgrade`, `upgrade_failed_returned_P0`, `P0_TM`, `final_TM`, `P3_TM`, `P0_TM_difference`, `final_TM_difference`, `P0_within_tolerance`, `final_within_tolerance`, `inference_replay_seconds`, `retrieval_shared_once_seconds`, `composite_replay_seconds`, `anomaly`, `post_hoc_exploratory`.

## `figure_data/supplement/decision_classification_summary.csv`

Records: 5.

Columns: `classification`, `targets`, `mean_P0_TM_difference`, `mean_final_TM_difference`, `minimum_final_TM_difference`, `maximum_final_TM_difference`, `inference_replay_seconds`, `composite_replay_seconds`, `mean_composite_replay_seconds`, `post_hoc_exploratory`.

## `figure_data/supplement/selection_space_aggregate.csv`

Records: 8.

Columns: `scope`, `route`, `targets`, `constraint_violations`, `inference_replay_seconds`, `inference_ratio_P3`, `composite_replay_seconds`, `composite_ratio_P3`, `post_hoc_exploratory`.

## `figure_data/supplement/timing_paired_ratios36.csv`

Records: 36.

Columns: `target_id`, `group`, `length`, `round`, `contrast`, `both_completed`, `charged_route_ratio`, `charged_route_difference_seconds`, `technical_repeats`.

## `figure_data/supplement/timing_variability18.csv`

Records: 18.

Columns: `target_id`, `group`, `length`, `stratum`, `profile`, `planned_replicates`, `completed_replicates`, `dispatched_replicates`, `all_charged_seconds`, `completed_route_mean_seconds`, `completed_route_median_seconds`, `completed_route_min_seconds`, `completed_route_max_seconds`, `completed_route_sample_SD_seconds`, `completed_route_CV`, `OOM_recoveries`, `cost_scope`.
