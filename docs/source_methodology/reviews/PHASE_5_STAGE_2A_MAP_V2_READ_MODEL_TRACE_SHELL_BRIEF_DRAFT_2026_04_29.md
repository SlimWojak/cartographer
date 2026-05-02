This brief does not authorize implementation until G ratifies it.

# PHASE_5.STAGE_2A — Map v2 Inert Read-Model + Trace Shell

```yaml
brief_id: PHASE_5_STAGE_2A_MAP_V2_READ_MODEL_TRACE_SHELL_BRIEF_DRAFT_2026_04_29
mission_id: PHASE_5.STAGE_2A.MAP_V2_READ_MODEL_TRACE_SHELL
classification: IMPLEMENTATION_BRIEF_DRAFT | NOT_AUTHORIZED_TO_EXECUTE
recommended_slice: NARROW_FOUNDATION
status: G_RATIFIED_FOR_EXECUTION
behavior_change_authorized: false
runtime_changes_authorized: false
schema_changes_authorized: false
cartridge_changes_authorized: false
implementation_authorized: false
certification_authorized: false
execution_ratification:
  decision: G_RATIFIES_STAGE_2A_EXECUTION
  ratification_date: 2026-04-29
  status: APPROVED_FOR_EXECUTION
  scope: "strictly under the patched brief"
  text: |
    G ratifies PHASE_5.STAGE_2A.MAP_V2_READ_MODEL_TRACE_SHELL for execution,
    strictly under the patched brief. Authorization is limited to the inert
    Map v2 read-model, evidence/trace/snapshot shell, serialization surface,
    inertness assertions, and required tests.

    This ratification does not authorize MapEngine behavior changes, v1 runtime
    mutation, cartridge/schema changes, DAILY_EXPANSION_v1 migration,
    DMB/MEM/TRM work, H4 authority, target ranking, v2 certification claims,
    P&L analysis, or trade_011 repair.
owner: CTO
reviewers:
  - Chief_Architect_GPT
  - Claude_Chair
  - G
date: 2026-04-29
frozen_contract_pointer:
  path: docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md
  frozen_commit_sha: f2ffc34405e82b573e6ced5058977d8f564936f9
  exact_status: FROZEN_BY_G_APPROVAL
phase_decision: docs/reviews/PHASE_4_CLOSE_PHASE_5_OPEN_DECISION_BRIEF_2026_04_29.md
architecture_boundary: docs/canonical/CARTRIDGE_CONTRACT.md
forward_plan: docs/canonical/FORWARD_PLAN.md
```

---

## 1. Non-authorization header

```yaml
non_authorization:
  exact_line: "This brief does not authorize implementation until G ratifies it."
  meaning: |
    This document is a mission brief draft for review. It may be used for
    Chair / Chief Architect / G review, but no code, schema, cartridge,
    migration, replay, or implementation execution may begin from it until G
    separately ratifies Stage 2A execution.

not_authorized:
  - implementation
  - code_changes
  - schema_changes
  - cartridge_changes
  - DAILY_EXPANSION_v1_migration
  - DMB_MEM_TRM_implementation_or_promotion
  - H4_core_authority
  - target_ranking
  - v1_trace_retirement
  - v2_certification_claim
  - strategy_performance_claim
  - PnL_optimization
  - trade_011_repair_attempt
  - methodology_seed_interpretation

schema_language_precision:
  rule: |
    schema_changes_authorized=false means no cartridge loader schema, runtime
    persistence schema, or v1 trace schema change. Internal inert Python type
    definitions inside map_v2 are allowed only if G ratifies Stage 2A execution.
```

---

## 2. Mission thesis

```yaml
thesis: |
  First executable Stage 2 slice should build the inert Map v2 read-model,
  trace/evidence shell, and serialization/test surface only. It must be unable
  to affect v1 runtime, v1 replay, DAILY_EXPANSION_v1, cartridges, strategy
  behavior, gate behavior, chain behavior, governance, execution, or broker
  outcomes.

primary_goal: |
  Make the frozen v2 contract physically representable and testable without
  connecting it to live decision flow.

non_negotiable: |
  Stage 2A must be inert. If it can change a trade, gate, regime, chain,
  cartridge, replay result, v1 trace, governance decision, or execution intent,
  it is too broad.
```

---

## 3. Implementation slice boundary

```yaml
in_scope_for_stage_2A_if_ratified:
  - inert_read_model_shell_only
  - separate_map_v2_package
  - immutable_v2_type_shapes
  - contract_version_field_resolution
  - construction_mode_shape
  - direction_status_value_shape
  - actionability_state_shape
  - evidence_ref_typed_model
  - current_extreme_pending_candidate_shape
  - unordered_target_inventory_shape
  - minimal_target_status_enum_shape
  - cold_start_instance_contract_shape
  - v2_snapshot_shape
  - v2_trace_minimum_shape
  - serialization_roundtrip_tests
  - deterministic_construction_tests_for_evidence_refs
  - structural_inertness_tests
  - mandatory_v1_replay_smoke_before_after

out_of_scope_for_stage_2A:
  - MapEngine_behavior_changes
  - existing_v1_map_mutation
  - DAILY_EXPANSION_consumption_of_v2_fields
  - cartridge_schema_changes
  - strategy_migration
  - target_selection_logic
  - target_completion_runtime_behavior
  - H4_strategy_overlay_implementation
  - DMB_MEM_TRM_work
  - performance_or_PnL_evaluation
  - v2_certification_claims
```

---

## 4. Chair addendum A1-A12 crosswalk

```yaml
chair_addendum_crosswalk:
  A1_structural_module_separation:
    disposition: included
    sections: [5, 8]
    summary: "Brief prefers separate en1gma/console/map_v2 package."

  A2_inertness_proof_concrete_definition:
    disposition: included
    sections: [8]
    summary: "Import graph, call graph, consumer set, and no-runtime-consumption assertions are explicit."

  A3_v1_replay_smoke_as_gate_not_optional:
    disposition: included
    sections: [9, 12]
    summary: "V1 replay smoke before/after with byte/hash equivalence is mandatory."

  A4_replay_test_surface_for_v2:
    disposition: included
    sections: [9]
    summary: "Stage 2A chooses construction_only v2 replay disposition; true v2 harness deferred."

  A5_immutability_by_construction:
    disposition: included
    sections: [6, 12]
    summary: "Frozen dataclasses, tuple collections, read-only mapping shape, immutability tests."

  A6_atomic_commit_discipline:
    disposition: included
    sections: [15]
    summary: "One logical change per commit; each commit independently green; commit messages cite Stage 2A and frozen artifact SHA."

  A7_estimate_realism_F6_check:
    disposition: included
    sections: [16]
    summary: "1-2 working sessions with named breakpoints."

  A8_stage_2A_authoring_exit_criteria:
    disposition: included
    sections: [18]
    summary: "Deliverable, boundary review, methodology consistency, ratification, gate to implementation."

  A9_subagent_infra_posture:
    disposition: included
    sections: [17]
    summary: "Subagent primary, direct CTO fallback with log, 3 transient failure halt threshold."

  A10_naming_single_source_of_truth:
    disposition: included
    sections: [6, 7, 9]
    summary: "contract_version for inner model; map_contract_version for outer snapshot/trace envelope."

  A11_bootstrap_representation_explicit:
    disposition: included
    sections: [6, 11, 12]
    summary: "cold_start_instance shape is explicit and tested."

  A12_trade_011_explicit_out_of_scope:
    disposition: included
    sections: [1, 13, 20]
    summary: "No trade_011 repair attempt or methodology seed interpretation."
```

---

## 5. Expected files to touch

Final file list must be repo-audited before execution. Stage 2A should prefer new v2-specific modules over edits to v1 authority surfaces.

```yaml
preferred_new_package:
  path: en1gma/console/map_v2/
  rationale: |
    Separate package makes inertness visible by structure. Shape boundaries
    are stronger than policy boundaries.

likely_new_files:
  - en1gma/console/map_v2/__init__.py
  - en1gma/console/map_v2/types.py
  - en1gma/console/map_v2/evidence.py
  - en1gma/console/map_v2/trace.py
  - en1gma/console/map_v2/snapshot.py
  - en1gma/tests/console/map_v2/test_v2_contract_types.py
  - en1gma/tests/console/map_v2/test_v2_trace_contract.py
  - en1gma/tests/console/map_v2/test_v2_inertness.py

possible_config_touch_requires_review:
  - pyproject.toml
  note: |
    Only if import-linter needs explicit awareness of en1gma.console.map_v2.
    This is still not runtime/schema/cartridge work, but must be isolated as
    its own atomic commit if required.

forbidden_files_or_surfaces:
  - en1gma/cartridges/*.yaml
  - en1gma/cartridges/loader.py
  - en1gma/console/map/map_engine.py
  - en1gma/console/map/context_types.py
  - en1gma/console/map/map_persistence.py
  - en1gma/console/chain/gate.py
  - en1gma/console/chain/chain_evaluator.py
  - en1gma/console/chain/canon/map_canon/session.py
  - en1gma/orchestrator/map_orchestrator.py
  - en1gma/scripts/run_map_session.py
  - en1gma/console/governance/
  - en1gma/console/execution/
```

---

## 6. Data model requirements

```yaml
stage_2A_type_policy:
  immutability_by_construction:
    dataclasses: frozen_true
    collections:
      unordered_sets: tuple_based
      mappings: mappingproxy_or_equivalent_read_only_shape
    rule: "Consumers cannot mutate v2 read-model state by construction."

naming_single_source_of_truth:
  inner_read_model_field: contract_version
  outer_snapshot_envelope_field: map_contract_version
  rule: |
    contract_version is the v2 read-model on-wire field. map_contract_version
    is permitted only as the outer snapshot envelope key. Implementation must
    not introduce additional aliases.

required_shapes:
  contract_version: "map_v2"

  construction_mode:
    values: [OK, CANNOT_DETERMINE]
    forbidden_values: [FALLBACK]

  direction:
    status: [known, unknown]
    value: [bullish, bearish, null]
    rule:
      - "unknown requires value=null"
      - "unknown requires actionability_state=cannot_determine"
      - "known requires value in [bullish, bearish]"
      - "fallback_direction forbidden"

  actionability_state:
    values: [actionable, paused_reassessment, cannot_determine]

  evidence_ref:
    fields:
      - ref_id
      - ref_type
      - source_tf
      - source_time
      - source_bar_index
      - source_detection_id
      - price
      - contract_version
    replay_rule: "ref_id unique within snapshot and stable across deterministic construction re-runs."
    ref_type_rule: |
      evidence_ref.ref_type inherits the frozen Stage 1 enum exactly. No new
      ref_type values may be introduced in Stage 2A unless separately reviewed
      as contract drift.

  current_extreme:
    canonical_value_rule: "canonical current_extreme remains last confirmed extreme during pending state"
    pending_candidate:
      fields:
        - candidate_extreme_price
        - candidate_extreme_time
        - candidate_displacement_ref
        - required_follow_through_condition

  target_inventory:
    type: unordered_bounded_set
    forbidden_fields:
      - priority_index
      - executable_rank
      - next_target
      - sort_order

  target_status_enum:
    values: [UNSWEPT, COMPLETED]
    scope: inert_data_shape_only
    note: "This closes the Stage 1 residual for shell typing only; it does not implement target-completion runtime behavior."

cold_start_instance:
  required: true
  shape:
    construction_mode: CANNOT_DETERMINE
    direction.status: unknown
    direction.value: null
    actionability_state: cannot_determine
    evidence_refs: empty_tuple
    cannot_determine_reason: required
  rule: "Cold start is a legal inert shape, not a runtime inference rule."

unenumerated_shape_inheritance_rule:
  rule: |
    Any v2 snapshot/trace field listed in Section 7 but not locally enumerated
    in Section 6 inherits its shape directly from the frozen Stage 1 contract.
    Stage 2A may physically represent those fields but must not add fields,
    remove fields, narrow fields, rename semantics, or interpret methodology
    beyond the frozen contract.
  inherited_fields:
    - dealing_range
    - quadrant_location
    - external_liquidity
    - internal_liquidity
    - dominant_draw
    - available_htf_targets
    - target_completion_status
    - proximity_to_target
    - market_state
  frozen_contract_source:
    path: docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md
    commit_sha: f2ffc34405e82b573e6ced5058977d8f564936f9

tuple_canonical_ordering:
  evidence_refs:
    rule: "sort by ref_id ascending, then source_time ascending, then ref_type ascending"
  target_inventory:
    rule: "sort by target_id ascending, then price ascending, then source_ref ascending"
  internal_liquidity:
    rule: "sort by source_ref ascending, then price ascending, then kind ascending"
  general_rule: |
    Any tuple used to represent an unordered frozen-contract set must be
    canonically sorted before serialization. Insertion order is forbidden as
    replay semantics.
```

---

## 7. Frozen snapshot and trace carry-through

Stage 2A must make the frozen Stage 1 snapshot and trace contracts physically representable. It must not narrow the frozen contract.

```yaml
v2_snapshot_minimum_from_frozen_contract:
  outer_envelope_version_field: map_contract_version
  inner_read_model_version_field: contract_version
  fields:
    - map_contract_version
    - construction_mode
    - direction_status
    - direction_value
    - direction_evidence_refs
    - actionability_state
    - actionability_reason
    - cannot_determine_reason
    - dealing_range
    - current_extreme
    - pending_candidate
    - quadrant_location
    - external_liquidity
    - internal_liquidity
    - dominant_draw
    - available_htf_targets
    - target_completion_status
    - proximity_to_target
    - market_state
    - evidence_refs

v2_trace_minimum_from_frozen_contract:
  envelope_version_field: map_contract_version
  fields:
    - map_contract_version
    - construction_mode
    - direction_status
    - direction_value
    - direction_evidence_refs
    - actionability_state
    - actionability_reason
    - cannot_determine_reason
    - paused_reassessment_reason
    - range_lifecycle_reason
    - origin_swing_ref
    - current_extreme_update_mode
    - follow_through_ref
    - target_completion_reason
    - dominant_draw_reason
    - h4_not_authority_assertion
    - pd_label_only_assertion
    - strategy_consumer_read_surface
    - evidence_refs
    - target_inventory_unordered_assertion
    - no_consumer_map_mutation_assertion
    - evidence_ref_replay_assertion

trace_assertions_from_frozen_contract:
  h4_not_authority_assertion: required
  pd_label_only_assertion: required
  target_inventory_unordered_assertion: required
  no_consumer_map_mutation_assertion: required
  evidence_ref_replay_assertion: required
```

---

## 8. Inertness proof

Stage 2A inertness must be proven by structure and tests, not by prose.

```yaml
structural_module_separation:
  required_package: en1gma.console.map_v2
  forbidden_runtime_import_direction: "v1 runtime surfaces must not import map_v2"

inertness_assertions:
  import_graph_assertion:
    primary: import-linter contract in pyproject.toml if required
    mirror: procedural assertion in test_v2_inertness.py
    config_touch_rule: "Config touch must be isolated as its own atomic commit."
    rule: |
      No module in en1gma/console/map/, en1gma/console/chain/,
      en1gma/orchestrator/, en1gma/scripts/, en1gma/cartridges/,
      en1gma/console/governance/, or en1gma/console/execution/ imports
      en1gma/console/map_v2/*.
    allowed_importers:
      - en1gma/console/map_v2/*
      - en1gma/tests/console/map_v2/*

  call_graph_assertion:
    rule: "No v1 runtime entrypoint resolves to a v2 symbol through dispatch, registry, loader, or orchestrator wiring."

  consumer_set_assertion:
    rule: "Only Stage 2A internal modules and Stage 2A tests import map_v2."

  no_runtime_consumption_assertion:
    rule: "No gate, chain, MapEngine, orchestrator, governance, execution, cartridge, or DAILY_EXPANSION_v1 path reads v2 fields."
```

---

## 9. Replay and trace plan

```yaml
v1_replay_continuity_gate:
  mandatory: true
  before_after_required: true
  required_sequence:
    - v1_replay_smoke_BEFORE_stage_2A_changes
    - apply_stage_2A_changes
    - v1_replay_smoke_AFTER_stage_2A_changes
    - byte_or_hash_equivalence_required
  rule: "Any v1 replay drift aborts Stage 2A."
  commit_cadence:
    - "run full v1 replay smoke before commit 1 as baseline"
    - "run quick parity subset after each atomic commit"
    - "run full v1 replay smoke after final commit before merge"
    - "byte/hash equivalence required between baseline and final smoke"

v1_chart_truth_baseline_exception:
  accepted_known_boundary: trade_011
  expected_state: "BLOCKED_BY_METHODOLOGY_SEED / known v1 doctrine-seed boundary"
  accepted_baseline: "11/12 chart-truth with trade_011 as sole red/blocked fixture"
  not_an_abort_condition: true
  abort_conditions:
    - any_additional_chart_truth_failure
    - trade_011_status_changes_unexpectedly
    - trade_011_is_repaired_hidden_skipped_without_log_or_reclassified
    - any_non_chart_truth_smoke_fails
  final_equivalence_rule: |
    Final post-Stage-2A v1 smoke must match the pre-code baseline:
    same 11/12 chart-truth shape, same trade_011 boundary, no new drift.

v2_replay_harness_disposition:
  stage_2A_disposition: construction_only
  rationale: |
    Stage 2A is inert and not consumed by runtime. True v2 replay requires a
    later parallel harness. Stage 2A therefore proves deterministic
    construction, serialization, and evidence_ref stability, while preserving
    v1 replay byte/hash equivalence.
  deferred_true_v2_replay_harness: Stage_2B_or_later

v2_trace_shell:
  required: true
  minimum_fields:
    - map_contract_version
    - construction_mode
    - direction_status
    - direction_value
    - direction_evidence_refs
    - actionability_state
    - actionability_reason
    - cannot_determine_reason
    - paused_reassessment_reason
    - range_lifecycle_reason
    - origin_swing_ref
    - current_extreme_update_mode
    - follow_through_ref
    - target_completion_reason
    - dominant_draw_reason
    - evidence_refs
    - h4_not_authority_assertion
    - pd_label_only_assertion
    - strategy_consumer_read_surface
    - target_inventory_unordered_assertion
    - no_consumer_map_mutation_assertion
    - evidence_ref_replay_assertion
```

---

## 10. DAILY_EXPANSION v1 non-migration guard

```yaml
DAILY_EXPANSION_v1_guard:
  status: remains_v1_certified_until_explicit_migration
  reads: map_v1_trace_surface
  cannot_read_v2_fields_until:
    - separate_G_ratified_migration_mission
    - v2_implementation_complete
    - v2_replay_green
    - chart_truth_rebaseline
    - no_regression_v1_or_explicit_v1_retirement_decision

DAILY_EXPANSION_v2_candidate:
  status: future_candidate_only
  reads: map_v2_contract_surface_after_implementation
  certification_required: TRACE_CERTIFIED_DAILY_AUTHORITY_V2_PENDING
```

---

## 11. Methodology ambiguity halt gate

```yaml
methodology_halt_gate:
  rule: |
    Any ambiguity that changes, interprets, extends, narrows, or operationalizes
    Olya methodology halts Stage 2A and routes the exact question G -> Olya.
    CTO, Chair, Chief Architect, and agents may frame the question but must not
    answer it.

especially_watch:
  - wick_vs_close_vs_body_for_quadrant_transition
  - follow_through_definition
  - bootstrap_before_daily_evidence
  - target_status_enum_if_methodology_significant
  - current_extreme_pending_confirmation
  - reassessment_exit_semantics
```

---

## 12. Tests required before green

```yaml
new_stage_2A_tests:
  - type_shape_roundtrip
  - immutable_type_property
  - cold_start_instance_contract_legal:
      asserts:
        - instantiable
        - serializable
        - construction_mode=CANNOT_DETERMINE
        - direction.status=unknown
        - direction.value=null
        - actionability_state=cannot_determine
        - evidence_refs=empty_tuple
        - cannot_determine_reason_non_empty
  - evidence_ref_uniqueness
  - evidence_ref_deterministic_construction_stability
  - direction_unknown_requires_null_and_cannot_determine
  - construction_mode_forbids_FALLBACK
  - target_inventory_forbids_ordering_fields
  - no_consumer_map_mutation_contract_test
  - import_graph_inertness_assertion
  - call_graph_inertness_assertion
  - consumer_set_inertness_assertion

mandatory_v1_smokes_before_and_after:
  - pytest en1gma/tests/integration/test_map_canon_runner_parity.py
  - pytest en1gma/tests/integration/test_replay_no_future_leak.py
  - pytest en1gma/tests/integration/test_daily_expansion_chart_truth.py
  - pytest en1gma/tests/integration/test_sw49_construction_mode.py
  - pytest en1gma/tests/integration/test_decision_trace_construction_enrichment.py
  chart_truth_interpretation: |
    test_daily_expansion_chart_truth.py is acceptable only as canonical 11/12:
    trade_011 must remain the sole red/blocked fixture and must remain visible
    in the baseline/final report. Do not use an unlogged -k not trade_011
    workaround.

validation_commands:
  - git diff --check
  - lint-imports --config pyproject.toml
  - mypy en1gma
  - pytest en1gma/tests/console/map_v2/
  - pytest en1gma/tests/integration/test_map_canon_runner_parity.py
  - pytest en1gma/tests/integration/test_replay_no_future_leak.py
  - pytest en1gma/tests/integration/test_daily_expansion_chart_truth.py
  - pytest en1gma/tests/integration/test_sw49_construction_mode.py
  - pytest en1gma/tests/integration/test_decision_trace_construction_enrichment.py
```

---

## 13. Abort criteria

```yaml
abort_if:
  - any_v1_runtime_behavior_change
  - any_v1_replay_drift
  - any_v1_trace_drift
  - any_non_chart_truth_v1_baseline_smoke_failure
  - any_chart_truth_failure_other_than_trade_011
  - trade_011_status_changes_unexpectedly
  - trade_011_hidden_skipped_without_log_reclassified_or_repaired
  - any_cartridge_schema_touch
  - any_cartridge_yaml_touch
  - any_DAILY_EXPANSION_v1_consumption_of_v2_fields
  - any_H4_authority_path_introduced
  - any_target_ranking_representation_introduced
  - any_methodology_interpretation_not_in_frozen_contract
  - inability_to_prove_inertness
  - evidence_refs_are_free_form_strings_without_stable_replay_semantics
  - construction_mode_permits_FALLBACK
  - direction_unknown_can_carry_stale_bullish_or_bearish
  - target_inventory_has_ordering_or_ranking_fields
  - v2_certification_claim_made
  - trade_011_repair_attempted
```

---

## 14. Certification delta link

```yaml
certification_delta:
  stage_2A_certifies_v2: false
  stage_2A_creates: "testable inert primitives for future certification"
  future_target: TRACE_CERTIFIED_DAILY_AUTHORITY_V2_PENDING
  v1_certification_transfer: false
  v1_runtime_certification_impact: none_expected_and_must_be_proven_by_smoke
```

---

## 15. Atomic commit discipline

```yaml
atomic_commit_discipline:
  rule: "One logical change per commit; each commit independently passes type/lint/test gates."
  no_partial_pass_merges: true
  commit_message_must_cite:
    - Stage_2A_scope
    - frozen_artifact_sha_f2ffc34405e82b573e6ced5058977d8f564936f9
  suggested_commit_slices_if_ratified:
    1_map_v2_immutable_types: "new en1gma/console/map_v2 package + type tests only"
    2_v2_trace_snapshot_shell: "trace/snapshot shell + serialization tests only"
    3_inertness_assertions: "import/call/consumer graph tests only"
    4_optional_import_linter_update: "only if required to police map_v2 boundary"
```

---

## 16. Estimate and breakpoints

```yaml
estimate_realism:
  expected_working_sessions: "1-2"
  reason: |
    Inert shell still requires immutable dataclasses, evidence_ref schema,
    target inventory shape, serialization, graph tests, and v1 replay smokes.

breakpoints:
  stop_after_brief_review: "No execution until G ratifies Stage 2A."
  stop_after_type_shell: "Verify no runtime imports before trace/snapshot shell."
  stop_after_trace_shell: "Run v2 serialization tests and v1 smoke subset."
  stop_before_merge: "Run full Stage 2A validation command list."
```

---

## 17. Subagent validation posture

```yaml
subagent_validation_posture:
  primary: subagent_validation
  fallback: direct_CTO_validation_with_explicit_log_entry
  transient_failure_threshold: 3
  threshold_rule: "Three transient subagent failures in one session triggers halt-and-report rather than continuing by direct fallback."
  prior_context: "Stage 1 logged F_SUBAGENT_RECHECK_DOUBLE_ERROR as transient_infra_non_blocking."
```

---

## 18. Stage 2A authoring exit criteria

```yaml
stage_2A_authoring_exit_criteria:
  deliverable:
    owner: CTO
    condition: "Stage 2A brief draft complete with frozen contract pointer and all required boundaries."

  boundary_review:
    owners:
      - Claude_Chair
      - Chief_Architect_GPT
    condition: "No H4 leakage, target ranking, strategy contamination, certification overclaim, or v1/v2 isolation breach."

  methodology_consistency:
    owner: G
    condition: "Any open methodology ambiguity is routed to Olya or explicitly marked blocking."

  ratification:
    owner: G
    condition: "G authorizes or rejects Stage 2A execution."

  gate_to_implementation:
    rule: "All four criteria required. This brief alone authorizes no implementation."
```

---

## 19. Green condition

```yaml
green_condition_if_executed_later: |
  V2 contract shell exists as inert, immutable, typed, serializable, traceable
  structure; tests prove core invariants; v1 runtime and replay surfaces are
  unchanged; no strategy consumes v2; no Map v2 certification claim is made.

explicit_non_green:
  - "Types exist but can be consumed by DAILY_EXPANSION_v1."
  - "Evidence refs are free-form strings without stable replay semantics."
  - "Target inventory has ordering/ranking fields."
  - "construction_mode permits FALLBACK."
  - "direction unknown can carry stale bullish/bearish."
  - "Any implementation infers methodology not frozen in Stage 1."
```

---

## 20. No-code close statement

```yaml
brief_authoring_only: true
implementation_authorized: false
runtime_behavior_changed: false
console_files_modified_by_this_brief: false
schema_files_modified_by_this_brief: false
cartridge_files_modified_by_this_brief: false
DAILY_EXPANSION_v1_migrated: false
DMB_MEM_TRM_implemented: false
H4_authority_resurrected: false
target_ranking_added: false
v2_certification_claimed: false
trade_011_repaired: false
```
