This document is a no-code preflight only. It does not authorize producer implementation.

# PHASE_5.C2 — Map v2 Producer Preflight

```yaml
artifact_id: PHASE_5_C2_PRODUCER_PREFLIGHT_2026_04_30
mission_id: PHASE_5.C2.PRODUCER_PREFLIGHT
classification: PLANNING | PRODUCER_DESIGN_PREFLIGHT | NO_CODE
status: DRAFT_FOR_G_CHAIR_GPT_REVIEW
owner: Droid_CTO_GPT55
date: 2026-04-30
behavior_change_authorized: false
producer_code_authorized: false
runtime_changes_authorized: false
schema_changes_authorized: false
cartridge_changes_authorized: false
strategy_migration_authorized: false
certification_claim_authorized: false
paper_trading_claim_authorized: false

purpose: |
  Identify the unresolved producer-design questions, methodology dependencies,
  evidence requirements, halt gates, and next authorization boundary for a
  later Map v2 producer lane. This artifact advances planning only.

canonical_inputs:
  - CLAUDE.md
  - docs/canonical/FORWARD_PLAN.md
  - docs/canonical/PHASE_5_KICKOFF_CLOSE_2026_04_29.md
  - docs/canonical/CERTIFICATION_STATE.md
  - docs/canonical/CARTRIDGE_CONTRACT.md
  - docs/reviews/PHASE_4_CLOSE_PHASE_5_OPEN_DECISION_BRIEF_2026_04_29.md
  - docs/reviews/HTF_MAP_v0_14_DESIGN_BRIEF_DRAFT_2026_04_29.md
  - docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md
  - docs/reviews/PHASE_5_STAGE_1A_BALANCE_MARKET_STATE_CONTRACT_AMENDMENT_BRIEF_DRAFT_2026_04_29.md
  - docs/reviews/PHASE_5_STAGE_2A_MAP_V2_READ_MODEL_TRACE_SHELL_BRIEF_DRAFT_2026_04_29.md
  - docs/reviews/PHASE_5_STAGE_2B_MAP_V2_CONSTRUCTION_REPLAY_HARNESS_BRIEF_DRAFT_2026_04_29.md
  - docs/reviews/PHASE_5_STAGE_2C_BALANCE_ENUM_AND_FIXTURE_EXTENSION_BRIEF_DRAFT_2026_04_29.md
  - docs/reviews/OLYA_NEX_HTF_MAP_v0_15_BALANCE_PATCH.md

sha_caveat:
  c4_valid_as_of_origin_main_sha: 67f6647373f72a0919916ead88d4bfab0d40a37f
  c4_pushed_commit_sha: b7ada658094850a3a4cf6effc9e45053aab44cea
  current_origin_main_sha_at_drafting: 38e7366c7cb28be395b46c71cbb8c355331265f6
  interpretation: |
    Not a contradiction. C4 was anchored to the prior origin/main SHA before
    its own push. Do not halt solely on this perceived mismatch.
    The current origin/main SHA at drafting reflects CI hygiene only; it has no
    production, runtime, schema, or cartridge effect.
```

---

## executive_verdict

```yaml
verdict: GREEN_FOR_NO_CODE_PREFLIGHT_ONLY
c2_as_understood: |
  C2 is the next Map v2 producer-design lane after Stage 2C. Current canon
  authorizes this preflight artifact only; it does not authorize producer code,
  runtime consumption, schema or cartridge edits, migration, certification, or
  trade_011 repair.

main_risk: |
  The safe producer boundary is blocked by methodology-operationalization
  questions, especially deterministic BALANCE detection and several Daily range
  lifecycle edge cases. These must be routed through G -> Olya when they become
  concrete, not answered by CTO or implementation agents.

recommended_next_gate: |
  G reviews this preflight with Chair and GPT, then authorizes a separate
  Olya-routing preparation artifact if desired. Do not jump directly from this
  preflight into a producer implementation brief.
```

---

## current_canon_boundary

```yaml
live_runtime:
  status: TRACE_CERTIFIED_DAILY_AUTHORITY_V1
  scope: current_runtime_Daily_authority_path_only
  evidence: docs/canonical/CERTIFICATION_STATE.md
  chart_truth: "11/12 GREEN; trade_011 remains visible as BLOCKED_BY_METHODOLOGY_SEED"

map_v2_current_state:
  stage_1_contract: frozen
  stage_1A_BALANCE_amendment: ratified_and_pushed
  stage_2A_shell: inert_read_model_trace_snapshot_shell_pushed
  stage_2B_harness: construction_only_replay_harness_pushed
  stage_2C_BALANCE_bridge: inert_enum_type_test_fixture_extension_pushed
  producer: none
  runtime_consumer: none
  strategy_consumer: none
  v2_certification: none

non_transfer_rule: |
  V1 certification proves the current runtime only. It does not transfer to
  Map v2 because v2 changes output contract, direction/actionability split,
  market_state, range lifecycle, target inventory, trace shape, and evidence
  requirements.
```

---

## C2_definition_as_understood

```yaml
c2_working_definition: |
  C2 is the future producer lane that would convert market data and detection
  evidence into the frozen Map v2 read-model outputs. In the present artifact,
  C2 means producer-design preflight only: define boundaries, unknowns,
  evidence surfaces, and gates before any implementation brief exists.

inputs_available_now:
  - frozen_Map_v2_output_contract
  - Stage_1A_BALANCE_contract_amendment
  - inert_Stage_2A_read_model_trace_snapshot_shell
  - Stage_2B_construction_only_harness_and_fixture_policy
  - Stage_2C_BALANCE_inert_representation

not_part_of_c2_preflight:
  - producer_algorithm
  - MapV2Engine_code
  - runtime_read_path
  - DAILY_EXPANSION_migration
  - schema_or_cartridge_changes
  - strategy_behavior
  - final_Olya_question_pack
  - v2_evidence_claim
```

---

## producer_design_unknowns

```yaml
OLYA_METHODOLOGY_REQUIRED:
  BALANCE_detection:
    status: NOT_FORMALIZED
    unknowns:
      - deterministic_BALANCE_detection_algorithm
      - HTF_level_selection_semantics_for_opposing_levels
      - liquidity_present_on_both_sides_logic
      - no_clean_progression_threshold
      - rejection_vs_stalling_vs_LTF_shift_vs_range_formation_selection
      - candle_count_or_attempt_count_thresholds
    canon_basis: |
      v0.15 says BALANCE failure-to-progress may manifest as rejection,
      stalling, LTF shifts, or range formation, and must not be reduced to a
      fixed pattern without example-based calibration.

  range_lifecycle_edges:
    unknowns:
      - wick_vs_close_vs_body_semantics_for_quadrant_transition
      - follow_through_definition_for_new_expansion_leg
      - origin_swing_selection_in_edge_cases
      - dominant_draw_selection_when_interpretations_compete
      - paused_reassessment_exit_semantics
      - bootstrap_behavior_before_enough_Daily_evidence

G_ARCHITECTURE_DECISION_REQUIRED:
  open_producer_lane:
    decision: whether_to_authorize_any_C2_producer_implementation_mission
    current_state: not_authorized
  v1_v2_parallelism:
    decision: preserve_parallel_v1_v2_surfaces_until_explicit_migration_gate
    current_state: parallel_preservation_only
  v1_trace_retirement:
    decision: whether_or_when_to_retire_or_transition_v1_trace_surfaces
    current_state: not_decided
  strategy_migration:
    decision: whether_DAILY_EXPANSION_or_other_strategies_may_read_v2
    current_state: separate_future_migration_mission_required

CHAIR_GOVERNANCE_DECISION_REQUIRED:
  fresh_session_review:
    requirement: Chair_and_GPT_review_before_any_producer_implementation_brief
  target_status_enum:
    requirement: close_before_any_target_completion_runtime_behavior
  implementation_brief_shape:
    requirement: ensure_future_brief_has_atomic_scope_and_halt_gates
  certification_claim_discipline:
    requirement: prevent evidence_language_from_becoming_certification_language

DROID_IMPLEMENTATION_DETAIL_LATER:
  allowed_later_if_non_semantic:
    - pure_field_naming_consistent_with_frozen_contract
    - trace_packaging_without_semantic_change
    - snapshot_versioning_mechanics_without_semantic_change
    - deterministic_fixture_id_generation
    - immutable_read_model_construction_mechanics
    - test_file_organization
  constraint: |
    These remain implementation details only while they do not interpret,
    extend, narrow, or operationalize methodology.

CERTIFICATION_EVIDENCE_REQUIRED:
  future_evidence_unknowns:
    - deterministic_replay_for_v2_fields
    - chart_truth_rebaseline_plan
    - walk_forward_no_regression_plan
    - cannot_determine_accounting
    - paused_reassessment_accounting
    - h4_not_core_authority_assertions
    - pd_label_only_strategy_owned_gating_assertions
    - v1_trace_continuity_or_transition_plan
    - target_inventory_unordered_shape_assertions
    - no_consumer_map_mutation_assertions
    - follow_through_gated_range_update_assertions
    - evidence_ref_replay_stability_assertions
    - current_extreme_pending_candidate_assertions
    - DAILY_EXPANSION_v1_v2_migration_gate_assertions
```

---

## Olya_methodology_question_candidates

These are candidates only. They are not the final Olya-facing question pack.

```yaml
candidate_questions:
  Q1_BALANCE_detection_examples:
    owner_classification: OLYA_METHODOLOGY_REQUIRED
    candidate: |
      Which chart examples should calibrate BALANCE detection, especially
      cases where failure-to-progress appears as rejection, stalling, LTF
      shifts, or range formation?

  Q2_opposing_HTF_levels:
    owner_classification: OLYA_METHODOLOGY_REQUIRED
    candidate: |
      For BALANCE, what qualifies as the opposing HTF levels that bound the
      environment, and which Daily evidence should select them?

  Q3_liquidity_both_sides:
    owner_classification: OLYA_METHODOLOGY_REQUIRED
    candidate: |
      What evidence is sufficient to say liquidity is present on both sides
      without inventing fixed candle counts, attempt counts, or thresholds?

  Q4_quadrant_transition_trigger:
    owner_classification: OLYA_METHODOLOGY_REQUIRED
    candidate: |
      Does a meaningful pullback quadrant transition trigger on wick, close,
      body, or another explicit chart condition?

  Q5_follow_through:
    owner_classification: OLYA_METHODOLOGY_REQUIRED
    candidate: |
      What confirms follow-through after a Daily displacement so that Map v2
      may update current_extreme and create the new active range?

  Q6_paused_reassessment_exit:
    owner_classification: OLYA_METHODOLOGY_REQUIRED
    candidate: |
      What event exits paused_reassessment after a target touch while direction
      persists?

  Q7_bootstrap_unknown:
    owner_classification: OLYA_METHODOLOGY_REQUIRED
    candidate: |
      Before enough Daily evidence exists, which conditions require
      cannot_determine rather than any provisional directional state?
```

---

## architecture_decisions_required

```yaml
decisions_before_any_implementation_brief:
  - id: A1_open_C2_producer_mission
    owner: G
    decision_needed: authorize_or_decline_a_separate_producer_implementation_mission

  - id: A2_parallel_v1_v2_strategy_boundary
    owner: G_CTO_Chair
    decision_needed: affirm_v1_runtime_remains_authority_until_explicit_v2_migration

  - id: A3_target_status_enum
    owner: CTO_Chair_GPT
    decision_needed: close_target_status_enum_before_target_completion_runtime_behavior

  - id: A4_trace_transition_policy
    owner: CTO_G
    decision_needed: preserve_parallel_trace_or_define_transition_before_any_v1_trace_retirement

  - id: A5_implementation_slice_size
    owner: CTO_Chair
    decision_needed: choose_first_producer_slice_after_methodology_gates_are_answered

  - id: A6_evidence_home
    owner: CTO_Chair
    decision_needed: define_future_v2_evidence_locations_without_confusing_them_with_v1_certification
```

---

## implementation_brief_prerequisites

```yaml
must_be_true_before_authoring_C2_implementation_brief:
  governance:
    - separate_G_authorization_for_producer_implementation_mission
    - Chair_and_GPT_fresh_review_complete
    - explicit_scope_small_enough_for_atomic_validation

  methodology:
    - BALANCE_detection_route_decided
    - follow_through_semantics_decided_or_excluded_from_first_slice
    - quadrant_transition_trigger_decided_or_excluded_from_first_slice
    - bootstrap_cannot_determine_behavior_decided
    - paused_reassessment_exit_decided_or_excluded_from_first_slice

  architecture:
    - target_status_enum_residual_closed_or_excluded_from_first_slice
    - v1_v2_parallel_preservation_restated
    - no_strategy_consumer_migration_in_first_producer_slice_unless_separately_authorized
    - future_evidence_surface_names_do_not_overlap_v1_certification_outputs

  validation_design:
    - deterministic_fixture_policy_for_producer_inputs_outputs
    - v1_drift_guard_named
    - inertness_or_runtime_boundary_tests_named
    - no_consumer_mutation_test_named
```

```yaml
implementation_brief_shape_note: |
  This block defines the shape of a future brief, not its content. It does not
  authorize drafting an implementation brief.

expected_later_implementation_brief_shape:
  classification: IMPLEMENTATION_BRIEF_DRAFT
  opening_line: "This brief does not authorize implementation until G ratifies it."
  required_blocks:
    - scope_and_non_authorizations
    - owner_doc_pointers
    - methodology_questions_previously_answered
    - explicit_exclusions
    - files_allowed_and_forbidden
    - task_slices_with_exit_gates
    - validation_commands
    - v1_drift_guard
    - evidence_non_claims
  forbidden_in_later_brief_without_separate_authorization:
    - strategy_migration
    - cartridge_schema_change
    - runtime_consumption_by_DAILY_EXPANSION
    - target_ranking
    - H4_core_authority
    - certification_claim
```

---

## evidence_and_certification_surfaces

```yaml
current_evidence_surfaces:
  v1_authority:
    owner: docs/canonical/CERTIFICATION_STATE.md
    status: current_runtime_only
    walk_forward_window: "2021-01-01 -> 2026-03-20"
    chart_truth: "11/12 GREEN; trade_011 visible boundary"

  stage_2A:
    surface: inert_read_model_trace_snapshot_shell
    claim_limit: representation_shape_only

  stage_2B:
    surface: tests/fixtures/map_v2/stage_2B/
    claim_limit: construction_only_not_runtime_replay

  stage_2C:
    surface: tests/fixtures/map_v2/stage_2C/
    claim_limit: BALANCE_inert_representation_and_v1_equivalence_smoke

future_v2_evidence_surfaces_to_design:
  - producer_input_fixture_corpus
  - producer_output_snapshot_corpus
  - v2_trace_event_corpus
  - deterministic_replay_hash_manifest
  - chart_truth_rebaseline_table
  - walk_forward_v2_comparison_report
  - cannot_determine_accounting_report
  - paused_reassessment_accounting_report
  - v1_v2_transition_or_parallel_trace_manifest

language_guard:
  allowed: "future evidence requirement"
  forbidden:
    - claim_that_v2_is_certified
    - claim_that_paper_trading_is_cleared
    - claim_that_trade_011_is_repaired
    - claim_that_12_of_12_is_achieved
```

---

## sequencing_impact_on_SW01_SW10_ARS_walkforward_DAILY_CONTINUATION

```yaml
SW01:
  impact: |
    SW01 retrace-fill/PDA mitigation semantics remain v1 doctrine and structural
    history. C2 must not reopen v1 mitigation logic or use producer preflight to
    patch trade_011.
  boundary: no_v1_runtime_patch

SW10:
  impact: |
    Any legacy H4 cascade tension is not a reason to resurrect H4 as core Map
    authority. Map v2 core direction remains Daily-only; H4 is strategy-specific
    context only if later declared by a strategy brief.
  boundary: no_H4_core_authority

ARS_v1_4:
  impact: |
    ARS is Map-independent and should not be sequenced behind C2. C2 evidence
    may reuse general governance/trace discipline, but it must not assert
    cross-ARS/Map trade parity.
  boundary: ARS_bypasses_Map

walk_forward_revalidation:
  impact: |
    V2 walk-forward revalidation is a future evidence requirement after producer
    implementation and replay design. The current V1 walk-forward remains the
    only live runtime evidence state.
  boundary: no_v2_walk_forward_claim

DAILY_CONTINUATION:
  impact: |
    DAILY_CONTINUATION remains parked until Olya provides a chain/entry spec.
    C2 must not infer continuation consumer behavior from Map v2 context fields.
  boundary: no_strategy_behavior_from_Map_context

Map_v2_output_contract:
  impact: |
    The frozen output contract is the upstream owner for C2. C2 consumes it and
    identifies producer questions; it does not renegotiate the contract.
  boundary: contract_consumer_not_contract_rewrite
```

---

## hard_halt_conditions

```yaml
halt_if:
  - C2_definition_conflicts_with_owner_docs
  - producer_preflight_requires_methodology_answer_not_already_in_canon
  - BALANCE_predicates_are_converted_into_detector_gates
  - fixed_BALANCE_patterns_or_thresholds_are_invented
  - H4_is_used_as_core_Map_authority
  - target_ranking_is_introduced
  - strategy_permission_logic_is_encoded_in_Map
  - runtime_or_schema_or_cartridge_changes_become_necessary_to_continue_planning
  - DAILY_EXPANSION_migration_is_assumed
  - trade_011_repair_is_attempted
  - v2_evidence_language_becomes_certification_language
  - paper_trading_status_is_claimed
  - doctrine_or_CI_hygiene_is_mixed_into_C2_commit

route:
  methodology: G_to_Olya
  architecture: G_CTO_Chair_GPT
  governance: G_Chair
```

---

## forbidden_scope_restatement

```yaml
forbidden_by_this_artifact:
  - producer_code
  - runtime_code
  - schema_changes
  - cartridge_changes
  - strategy_migration
  - implementation_brief
  - v2_certification_claim
  - paper_trading_claim
  - trade_011_repair
  - final_Olya_question_pack
  - doctrine_folder_cleanup
  - CI_workflow_refactor
```

---

## recommended_next_authorization

```yaml
recommendation: RECOMMEND_OLYA_ROUTING_PREPARATION_AFTER_REVIEW
non_authorization: |
  This is a recommendation, not an authorization. The next gate requires
  separate G ratification.
scope: |
  If G accepts this preflight, the next bounded artifact should be a reviewed
  Olya-routing preparation note that turns the candidate methodology unknowns
  into a minimal, chart-example-oriented package for G to decide whether and
  how to bring to Olya.

not_recommended_next:
  - producer_implementation_brief
  - MapV2Engine_code
  - runtime_migration
  - strategy_consumer_work
  - v2_certification_plan_claim

exit_state_after_this_artifact:
  - C2_boundary_is_explicit
  - methodology_unknowns_are_classified
  - evidence_delta_is_visible
  - next_gate_is_G_review_then_possible_Olya_routing_preparation
```

---

*PHASE_5_C2_PRODUCER_PREFLIGHT_2026_04_30 — no-code producer-design preflight. It preserves V1 authority, Map v2 inertness, and the G -> Olya methodology route.*
