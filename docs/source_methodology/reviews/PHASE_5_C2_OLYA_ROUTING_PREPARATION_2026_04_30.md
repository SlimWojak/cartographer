This document prepares methodology routing only. It does not contact Olya or authorize producer work.

# PHASE_5.C2 — Olya Routing Preparation

```yaml
artifact_id: PHASE_5_C2_OLYA_ROUTING_PREPARATION_2026_04_30
classification: METHODOLOGY_ROUTING_PREP | NO_CODE | NO_OLYA_CONTACT
status: DRAFT_FOR_G_CHAIR_GPT_REVIEW
owner: Droid_CTO_GPT55
date: 2026-04-30
input_anchor:
  origin_main_sha: d56f141689e5f25efe247397afd73c0316d1471f
  source_artifact: docs/reviews/PHASE_5_C2_PRODUCER_PREFLIGHT_2026_04_30.md
authorizations:
  methodology_answers_authorized: false
  producer_brief_authorized: false
  producer_code_authorized: false
  runtime_changes_authorized: false
  schema_changes_authorized: false
  cartridge_changes_authorized: false
  strategy_migration_authorized: false
  certification_claim_authorized: false
  paper_trading_claim_authorized: false
```

---

## executive_verdict

```yaml
verdict: GREEN_FOR_NO_CODE_ROUTING_PREPARATION_ONLY
purpose: |
  Convert the ratified C2 preflight Q1-Q7 methodology unknowns into concise,
  chart-example-oriented prompts for G, Chair, and GPT review before any later
  Olya-facing packet is separately authorized.

core_thesis: |
  Olya should receive chart-language questions with requested example classes,
  not producer architecture language. This note strips architecture noise and
  identifies which methodology questions are essential before the first C2
  producer design slice.

recommended_next_gate: |
  G reviews this note with Chair and GPT. If accepted, G may separately
  authorize a final Olya-facing methodology packet.
```

---

## source_boundary

```yaml
source_of_questions:
  artifact: docs/reviews/PHASE_5_C2_PRODUCER_PREFLIGHT_2026_04_30.md
  source_section: Olya_methodology_question_candidates
  source_questions: [Q1, Q2, Q3, Q4, Q5, Q6, Q7]

canon_state_preserved:
  current_certification: TRACE_CERTIFIED_DAILY_AUTHORITY_V1
  phase_5_state: DESIGN_LANE_LIVE_NO_PRODUCER
  map_v2_status: inert_surfaces_only
  producer_status: none
  strategy_consumer_status: none

scope_limit: |
  This artifact rewrites questions for review. It does not add methodology,
  change the Map v2 output contract, select a producer slice, or define a
  detector.
```

---

## non_authorization_statement

```yaml
non_authorization: |
  This is not an Olya-facing packet, not methodology truth, not a producer
  implementation brief, and not authorization to build. It prepares questions
  for G review only.

not_authorized:
  - contact_Olya
  - final_Olya_facing_packet
  - methodology_answers_by_Droid
  - BALANCE_detector_thresholds
  - fixed_pattern_reduction
  - producer_implementation_brief
  - producer_code
  - runtime_schema_or_cartridge_change
  - strategy_migration
  - v2_certification_claim
  - paper_trading_claim
  - trade_011_repair
```

---

## Olya_routing_principle

```yaml
principle: |
  Olya should be asked concrete methodology questions using chart examples, not
  abstract system-design language. Each question should ask for positive
  examples, near-miss controls, and the exact chart features that distinguish
  the accepted label from rejected alternatives.

question_style:
  use:
    - chart_examples
    - marked_bars_or_zones
    - accepted_label
    - rejected_alternative_labels
    - Olya_own_label_or_terminology
    - Olya_phrasing_for_trigger_or_distinguishing_feature
    - marked_features_distinguishing_accepted_from_rejected
  avoid:
    - class_names_from_code
    - producer_algorithm_terms
    - fixed_numbers_not_supplied_by_Olya
    - architecture_decisions
    - implementation_file_surfaces
```

---

## question_grouping_by_chart_primitive

```yaml
groups:
  BALANCE_environment_and_detection:
    includes: [Q1, Q2, Q3]
    chart_primitive: "known Daily direction, price between opposing HTF levels, unclear progression, liquidity on both sides"
    first_slice_relevance: essential

  range_transition_and_new_leg_confirmation:
    includes: [Q4, Q5]
    chart_primitive: "meaningful pullback from the current move or extreme, Daily displacement, follow-through, meaningful extreme/reference point"
    first_slice_relevance: deferrable_if_excluded_from_initial_producer_slice

  state_transition_and_insufficient_evidence:
    includes: [Q6, Q7]
    chart_primitive: "post-target reassessment exit and early-sequence Daily charts before direction can be confidently called"
    first_slice_relevance:
      Q6: deferrable_if_paused_reassessment_excluded_from_initial_slice
      Q7: essential
```

---

## Q1_Q7_rewritten_for_chart_review

```yaml
Q1_BALANCE_detection_examples:
  group: BALANCE_environment_and_detection
  chart_review_prompt: |
    Show chart examples you would label BALANCE because price fails to progress
    cleanly. For each, describe in your own words what kind of failure it is.
    Include variety where possible. Mark the bars or zones that make it BALANCE
    rather than normal expansion, pullback, approaching target, or reassessment.
  evidence_needed:
    - positive_BALANCE_examples_with_Olya_described_variety
    - near_miss_examples_not_BALANCE
    - marked_feature_that_separates_BALANCE_from_other_market_states

Q2_HTF_level_context:
  group: BALANCE_environment_and_detection
  chart_review_prompt: |
    On BALANCE examples, mark the HTF levels that define the BALANCE context.
    If multiple level pairs could plausibly apply, mark the selected pair and
    rejected pairs.
  evidence_needed:
    - selected_HTF_level_pair
    - rejected_candidate_level_pairs
    - reason_the_selected_pair_is_the_active_context

Q3_liquidity_both_sides:
  group: BALANCE_environment_and_detection
  chart_review_prompt: |
    Show examples where liquidity is clearly present on both sides, plus
    control examples where one side is not sufficient yet. Mark the chart
    evidence without turning it into fixed candle-count, attempt-count, or
    numeric rules.
  evidence_needed:
    - both_sides_liquidity_positive_examples
    - insufficient_liquidity_control_examples
    - marked_evidence_that_makes_both_sides_liquidity_present

Q4_pullback_state_change_trigger:
  group: range_transition_and_new_leg_confirmation
  chart_review_prompt: |
    Show examples of meaningful pullbacks from the current move or extreme that
    you would treat as a state change. Mark the bar or zone that triggers the
    change and describe the trigger in your own terms: wick, close, body, or
    other.
  evidence_needed:
    - pullback_state_change_positive_examples
    - failed_or_insufficient_pullback_controls
    - marked_trigger_condition

Q5_follow_through:
  group: range_transition_and_new_leg_confirmation
  chart_review_prompt: |
    Show Daily displacement examples that do and do not qualify as
    follow-through for confirming a new expansion leg. Mark the chart point, if
    any, after which you would treat the move as having established a new
    meaningful extreme. If not, explain why the prior extreme remains the
    relevant reference.
  evidence_needed:
    - follow_through_positive_examples
    - displacement_without_follow_through_controls
    - marked_meaningful_extreme_or_reference_point

Q6_paused_reassessment_exit:
  group: state_transition_and_insufficient_evidence
  chart_review_prompt: |
    After a target touch where direction persists, show examples that exit
    paused reassessment and examples that remain paused. Mark the chart event
    that causes the exit.
  evidence_needed:
    - reassessment_exit_positive_examples
    - remains_paused_control_examples
    - marked_exit_event

Q7_bootstrap_unknown:
  group: state_transition_and_insufficient_evidence
  chart_review_prompt: |
    Show early-sequence Daily charts where direction cannot be confidently
    called. Mark the boundary between unknown and known direction. Use your own
    language for the unknown state.
  evidence_needed:
    - insufficient_Daily_evidence_examples
    - examples_where_direction_becomes_known
    - marked_boundary_between_unknown_and_known_direction
```

---

## required_chart_examples

```yaml
essential_before_first_C2_producer_design:
  BALANCE_detection_packet:
    questions: [Q1, Q2, Q3]
    examples_needed:
      - BALANCE_positive_examples_with_Olya_named_failure_variety
      - near_miss_not_BALANCE
      - HTF_level_context_selection_with_competing_anchors
      - both_sides_liquidity_clear_vs_unclear

  bootstrap_unknown_direction_packet:
    questions: [Q7]
    examples_needed:
      - insufficient_Daily_evidence_requires_unknown_direction
      - first_valid_Daily_evidence_makes_direction_known
      - ambiguous_case_that_must_not_receive_provisional_direction

deferrable_or_appendix_if_first_slice_excludes_the_feature:
  range_transition_packet:
    questions: [Q4, Q5]
    examples_needed:
      - pullback_state_change_positive_and_control
      - follow_through_positive_and_control

  reassessment_exit_packet:
    questions: [Q6]
    examples_needed:
      - post_target_touch_exits_paused_reassessment
      - post_target_touch_remains_paused

per_example_annotation_fields:
  - chart_date_or_window
  - timeframe_context
  - accepted_label
  - rejected_alternative_labels
  - marked_trigger_bar_or_zone
  - Olya_own_label_or_terminology
  - Olya_phrasing_for_trigger_or_distinguishing_feature
  - marked_features_distinguishing_accepted_from_rejected
  - whether_example_is_positive_or_control
```

---

## defer_or_include_matrix

```yaml
include_in_initial_Olya_routing_if_G_approves:
  Q1:
    reason: "Core BALANCE calibration; producer cannot safely infer it."
  Q2:
    reason: "BALANCE requires opposing HTF levels; level selection must not be invented."
  Q3:
    reason: "Liquidity on both sides is part of BALANCE; thresholds are explicitly not formalized."
  Q7:
    reason: "Bootstrap unknown direction prevents fallback or provisional state invention."

defer_unless_first_producer_slice_requires_feature:
  Q4:
    reason: "Can be excluded if initial producer slice does not implement pullback-driven state-change range lifecycle."
  Q5:
    reason: "Can be excluded if initial producer slice does not create new expansion legs from follow-through."
  Q6:
    reason: "Can be excluded if initial producer slice does not implement paused reassessment exit."

G_decision_needed: |
  Decide whether the first Olya-facing packet should contain only Q1-Q3 and Q7,
  or include Q4-Q6 as clearly marked appendix items.
```

---

## architecture_noise_removed

```yaml
removed_from_Olya_routing_surface:
  - target_status_enum
  - trace_transition_policy
  - implementation_brief_shape
  - validation_command_design
  - evidence_home_design
  - file_allowlist_or_forbidden_file_list
  - v1_v2_parallel_trace_mechanics
  - strategy_migration_decisions
  - certification_evidence_table_design

kept_as_boundary_reminders_only:
  - V1_runtime_remains_current_authority
  - Map_v2_producer_runtime_remains_absent
  - Olya_questions_are_chart_methodology_questions
  - G_decides_whether_to_route_any_packet
  - Droid_does_not_answer_methodology
```

---

## recommended_G_decision

```yaml
recommendation: RECOMMEND_REVIEW_AND_PATCH_BEFORE_ANY_OLYA_FACING_PACKET
suggested_scope_if_G_continues:
  primary_packet:
    include: [Q1, Q2, Q3, Q7]
    purpose: "Resolve first-slice-essential BALANCE and bootstrap methodology."
  optional_appendix:
    include: [Q4, Q5, Q6]
    purpose: "Prepare range lifecycle and reassessment questions only if G wants broader routing."

non_authorization: |
  This recommendation does not authorize Olya contact, producer design,
  implementation, migration, certification claims, or paper-trading claims.

next_gate: |
  G, Chair, and GPT review this preparation note. If accepted, G may separately
  authorize a final Olya-facing packet.
```

---

## forbidden_scope_restatement

```yaml
forbidden:
  - Olya_contact
  - final_Olya_facing_packet
  - methodology_answers_by_Droid
  - BALANCE_detector_algorithm
  - fixed_BALANCE_patterns_or_thresholds
  - producer_implementation_brief
  - producer_code
  - runtime_code
  - schema_changes
  - cartridge_changes
  - strategy_migration
  - H4_core_Map_authority
  - target_ranking
  - v2_certification_claim
  - paper_trading_claim
  - trade_011_repair
  - new_C2_substage_canon_labels
```

---

*PHASE_5_C2_OLYA_ROUTING_PREPARATION_2026_04_30 — no-code methodology routing preparation only. It converts C2 preflight unknowns into chart-review prompts for G review while preserving the no-producer boundary.*
