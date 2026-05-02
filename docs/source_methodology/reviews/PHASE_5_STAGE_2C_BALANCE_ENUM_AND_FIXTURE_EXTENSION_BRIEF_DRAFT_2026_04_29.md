This brief does not authorize implementation until G ratifies it.

# PHASE_5.STAGE_2C — BALANCE Enum / Type / Test + Fixture Extension

```yaml
brief_id: PHASE_5_STAGE_2C_BALANCE_ENUM_AND_FIXTURE_EXTENSION_BRIEF_DRAFT_2026_04_29
mission_id: PHASE_5.STAGE_2C.BALANCE_ENUM_AND_FIXTURE_EXTENSION
classification: IMPLEMENTATION_BRIEF_DRAFT | NOT_AUTHORIZED_TO_EXECUTE
recommended_slice: SMALL_INERT_BALANCE_BRIDGE
status: G_RATIFIED_FOR_EXECUTION
behavior_change_authorized: false
runtime_changes_authorized: false
schema_changes_authorized: false
cartridge_changes_authorized: false
implementation_authorized: false
implementation_authorized_scope: STRICT_STAGE_2C_ONLY
certification_authorized: false
execution_ratification:
  decision: G_RATIFIES_STAGE_2C_EXECUTION
  ratification_date: 2026-04-29
  status: APPROVED_FOR_EXECUTION
  scope: "strictly under the Stage 2C brief"
  text: |
    G ratifies PHASE_5.STAGE_2C.BALANCE_ENUM_AND_FIXTURE_EXTENSION for
    execution strictly under the Stage 2C brief.

    Authorization is limited to inert representation of BALANCE in the Map v2
    enum/type/test surface, snapshot roundtrip coverage, and an optional
    deterministic BALANCE construction fixture under the existing Stage 2B
    corpus rules.

    This does not authorize BALANCE detection, MapV2Engine producer work,
    market-data inference, HTF level selection logic, liquidity-both-sides
    logic, no-clean-progression thresholds, strategy behavior, schema or
    cartridge changes, DAILY_EXPANSION migration, trace widening,
    certification claims, or trade_011 repair.
pre_execution_sequence:
  P0_first: "commit and push this ratified brief before implementation begins"
  P1_second: "capture tests/fixtures/map_v2/stage_2C/v1_smoke_baseline.yaml before commit 1"
owner: CTO
reviewers:
  - Chief_Architect_GPT
  - Claude_Chair
  - G
date: 2026-04-29
audit_chain:
  frozen_stage_1_contract:
    path: docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md
    commit_sha: f2ffc34405e82b573e6ced5058977d8f564936f9
  baseline_gate_amendment:
    commit_sha: 66073831da853bbb9ed73c40fd55e95dd5b75400
  stage_2A:
    path: docs/reviews/PHASE_5_STAGE_2A_MAP_V2_READ_MODEL_TRACE_SHELL_BRIEF_DRAFT_2026_04_29.md
    commit_sha: 335a8f15d137271e67d032d594b1be46c49776dc
  stage_2B:
    path: docs/reviews/PHASE_5_STAGE_2B_MAP_V2_CONSTRUCTION_REPLAY_HARNESS_BRIEF_DRAFT_2026_04_29.md
    commit_sha: 95e321bb11e55ebf981af3f90a48de337d312f2f
  stage_1A_balance:
    path: docs/reviews/PHASE_5_STAGE_1A_BALANCE_MARKET_STATE_CONTRACT_AMENDMENT_BRIEF_DRAFT_2026_04_29.md
    commit_sha: 59985ce6db71acd4c8b0ff587a4b5cc4bbb375c6
  rule: |
    Stage 2C anchors to both the original frozen Map v2 contract and the
    BALANCE amendment. Future agents must be able to see why BALANCE appears
    in code after Stage 2A/2B.
architecture_boundary: docs/canonical/CARTRIDGE_CONTRACT.md
```

---

## 1. Non-authorization header

```yaml
non_authorization:
  exact_line: "This brief does not authorize implementation until G ratifies it."
  meaning: |
    This document is a Stage 2C implementation brief draft for review. It may
    be used for Chair / Chief Architect / G review, but no code, schema,
    cartridge, producer, replay, artifact, migration, certification, strategy,
    or runtime work may begin from it until G separately ratifies Stage 2C
    execution.

not_authorized:
  - implementation
  - code_changes
  - artifact_generation
  - replay_execution
  - schema_changes
  - cartridge_changes
  - BALANCE_detection_algorithm
  - MapV2Engine_producer
  - market_data_inference
  - HTF_level_selection_logic
  - liquidity_present_on_both_sides_algorithm
  - no_clean_progression_threshold
  - candle_count_or_attempt_count_threshold
  - strategy_permission_logic
  - DMB_TRM_MEM_behavior
  - DAILY_EXPANSION_migration
  - runtime_consumption
  - v2_certification_claim
  - trade_011_repair
```

---

## 2. Mission purpose

```yaml
purpose: |
  Extend the inert Map v2 code and fixture surfaces to represent the
  G-ratified BALANCE market_state amendment. This is a small bridge slice only.
  It must not implement BALANCE detection, producer behavior, strategy
  behavior, or runtime consumption.

primary_goal_if_ratified: |
  Make BALANCE representable in the existing inert Map v2 shell and optional
  deterministic construction fixture corpus while preserving Stage 2A/2B
  inertness and v1 replay continuity.

non_negotiable: |
  Stage 2C is representation and fixture extension only. If implementation
  needs to decide whether real price action is in BALANCE, it has crossed into
  producer methodology and must halt.
```

---

## 3. Scope

```yaml
in_scope_if_ratified:
  - "Extend Stage 2A inert market_state enum/type shell to include BALANCE."
  - "Add explicit BALANCE coupling tests from Stage 1A section 5."
  - "Extend snapshot serialization roundtrip tests to include BALANCE."
  - "Keep trace contract unchanged; market_state is a snapshot field, not a trace field."
  - "Add one deterministic BALANCE construction case to the Stage 2B fixture corpus if clean."
  - "Update deterministic replay hashes/artifacts if BALANCE fixture is added."
  - "Capture fresh Stage 2C v1 baseline/final smoke artifacts."
  - "Preserve Stage 2A inertness and Stage 2B artifact inertness."
  - "Preserve v1 baseline/final smoke equivalence and trade_011 visibility."

out_of_scope:
  - "Any logic deciding whether real price action is in BALANCE."
  - "Any River, detect.py, MapEngine, Gate, Chain, Orchestrator, cartridge config, broker/execution, or governance input."
  - "Any strategy decision about trend/scalp behavior under BALANCE."
  - "Any MapV2Engine producer or equivalent producer behavior."
  - "Any BALANCE detection algorithm."
  - "Any HTF level selection semantics."
  - "Any liquidity-present-on-both-sides algorithm."
  - "Any clean-progression threshold."
  - "Any candle count or attempt count threshold."
  - "Any schema or cartridge change."
  - "Any DAILY_EXPANSION migration."
  - "Any v2 certification claim."
  - "Any trade_011 repair."
```

---

## 4. BALANCE representation contract

```yaml
balance_representation_contract:
  source: docs/reviews/PHASE_5_STAGE_1A_BALANCE_MARKET_STATE_CONTRACT_AMENDMENT_BRIEF_DRAFT_2026_04_29.md
  source_commit_sha: 59985ce6db71acd4c8b0ff587a4b5cc4bbb375c6

  market_state_enum_delta:
    add:
      - balance

  state_definition:
    balance: non_directional_execution_environment_inside_known_directional_context

  coupling_rules_to_encode_as_tests:
    - "market_state=balance requires direction.status=known."
    - "market_state=balance requires actionability_state=actionable."
    - "market_state=balance is forbidden when actionability_state=paused_reassessment."
    - "market_state=balance is forbidden when actionability_state=cannot_determine."
    - "market_state=balance does not reset, neutralize, or flip Daily direction."

  representational_only: true
  not_detector_gate: true
  no_market_data_inference: true
```

---

## 5. Snapshot-only typing and trace non-widening

```yaml
snapshot_trace_boundary:
  market_state_surface: MapV2Snapshot
  trace_surface_change_authorized: false
  rule: |
    Frozen Stage 1 and Stage 2A carry market_state on the snapshot surface.
    Stage 2C may type and validate snapshot market_state but must not add
    market_state to MapV2TraceMinimum or otherwise widen the trace contract.

code_documentation_alignment:
  if_market_state_enum_documented_in_code:
    requirement: "Docstring/comment must match Olya/NEX v0.15 state_definitions verbatim."
  if_no_documentation_added:
    requirement: "No inferred or invented definitions in code."
```

---

## 6. Required BALANCE coupling tests

```yaml
required_balance_coupling_tests:
  source: "Stage 1A section 5 coupling amendment"
  tests:
    - test_balance_requires_direction_status_known
    - test_balance_requires_actionability_state_actionable
    - test_balance_forbidden_with_paused_reassessment
    - test_balance_forbidden_with_cannot_determine
    - test_balance_does_not_flip_daily_direction
  rule: |
    Tests prove representational legality only. They must not implement BALANCE
    detection from market data or encode trend/scalp strategy permissions.
```

---

## 7. Mandatory F1 v1 baseline gate

```yaml
mandatory_F1_v1_baseline_gate:
  selected_option: option_A_recapture
  rationale: |
    Stage 2C is small. Fresh baseline capture is cleaner and avoids reasoning
    about inter-stage drift.

  option_A_recapture:
    required: true
    before_commit_1: tests/fixtures/map_v2/stage_2C/v1_smoke_baseline.yaml
    after_final_commit: tests/fixtures/map_v2/stage_2C/v1_smoke_final.yaml
    comparison_rule: |
      Structured content equivalence on test counts, pass/fail shape, sole red
      identity, trade_011 boundary classification, chart-truth test hash, and
      annotated_trades hash.

  option_B_inherit_stage_2B_baseline:
    selected: false
    reason: "Stage 2C requires fresh baseline/final artifacts."

  minimum_fields:
    - command
    - exit_code
    - pass_fail_counts
    - chart_truth_shape
    - trade_011_status
    - test_file_sha256
    - annotated_trades_sha256
    - captured_at
    - commit_sha
```

---

## 8. A1 chart-truth baseline exception

```yaml
baseline_gate_amendment_source:
  commit_sha: 66073831da853bbb9ed73c40fd55e95dd5b75400
  rule: "Stage 2C inherits the canonical 11/12 chart-truth gate from this amendment."

v1_chart_truth_baseline_exception:
  accepted_known_boundary: trade_011
  expected_state: "BLOCKED_BY_METHODOLOGY_SEED / known v1 doctrine-seed boundary"
  accepted_baseline: "11/12 chart-truth with trade_011 as sole red/blocked fixture"
  not_an_abort_condition: true
  required_visibility:
    - run_full_12_fixture_chart_truth_suite
    - do_not_use_k_not_trade_011
    - do_not_skip_repair_reclassify_or_hide_trade_011
  abort_conditions:
    - any_additional_chart_truth_failure
    - trade_011_status_changes_unexpectedly
    - trade_011_is_repaired_hidden_skipped_without_log_or_reclassified
    - any_non_chart_truth_smoke_fails
```

---

## 9. BALANCE fixture extension policy

```yaml
balance_fixture_requirements:
  optional_but_recommended: true
  fixture_policy_if_added: |
    Extend the existing Stage 2B construction fixture corpus by adding one
    explicit controlled BALANCE case and updating the existing Stage 2B
    construction_replay_sample.yaml and replay_hashes.yaml artifacts. Stage 2C
    v1 smoke baseline/final artifacts live under tests/fixtures/map_v2/stage_2C/.

  construction_case_id:
    shape: balance_<hash12>
    derivation: stable_SHA256_of_canonical_input_payload
    forbidden:
      - random
      - sequential
      - timestamp_derived
    collision_rule: "Inherit Stage 2B section 7 collision rule."

  corpus_state:
    before: "1 construction case: cold_start_d268dc4344a1"
    after_expected_if_fixture_added: "2 construction cases: cold_start_<hash12>, balance_<hash12>"
    bound: 10
    rule: "Remain under Stage 2B corpus bound."

  balance_fixture_stage_attribution:
    required: true
    rule: |
      Any BALANCE construction case added to the existing Stage 2B fixture
      corpus must set generated_by_stage=PHASE_5_STAGE_2C in replay_hashes.yaml
      and any construction replay sample entry.

  artifact_paths_if_fixture_added:
    update_existing:
      - tests/fixtures/map_v2/stage_2B/construction_replay_sample.yaml
      - tests/fixtures/map_v2/stage_2B/replay_hashes.yaml
    create_new:
      - tests/fixtures/map_v2/stage_2C/v1_smoke_baseline.yaml
      - tests/fixtures/map_v2/stage_2C/v1_smoke_final.yaml
    forbidden:
      - reports/map_v2
      - traces/map_*
      - chain_trace.jsonl
      - decision_trace.jsonl
      - map_timeline.jsonl
      - map_state.json
      - session_summary.yaml
```

---

## 10. Inertness continuity

```yaml
inertness_continuity_required:
  must_still_hold_after_2C:
    - import_graph_assertion
    - call_graph_assertion
    - consumer_set_assertion
    - no_runtime_consumption_assertion
    - artifact_inertness_assertion
  rule: |
    New BALANCE enum, tests, and fixture must remain inside map_v2/test/fixture
    surfaces. No v1 runtime path may import, call, read, or consume them.

forbidden_runtime_surfaces:
  - en1gma/console/map/map_engine.py
  - en1gma/console/chain/gate.py
  - en1gma/console/chain/chain_evaluator.py
  - en1gma/orchestrator/*
  - en1gma/cartridges/*
  - en1gma/console/governance/*
  - en1gma/console/execution/*
  - any_v1_runtime_surface
```

---

## 11. Expected files to touch

Final file list must be repo-audited before execution.

```yaml
likely_files_if_ratified:
  - en1gma/console/map_v2/types.py
  - en1gma/console/map_v2/snapshot.py
  - en1gma/console/map_v2/construct.py
  - en1gma/console/map_v2/replay.py
  - en1gma/tests/console/map_v2/test_map_v2_type_shells.py
  - en1gma/tests/console/map_v2/test_v2_trace_snapshot_shell.py
  - en1gma/tests/console/map_v2/test_v2_construction_determinism.py
  - tests/fixtures/map_v2/stage_2B/construction_replay_sample.yaml
  - tests/fixtures/map_v2/stage_2B/replay_hashes.yaml
  - tests/fixtures/map_v2/stage_2C/v1_smoke_baseline.yaml
  - tests/fixtures/map_v2/stage_2C/v1_smoke_final.yaml

trace_py_touch_rule:
  path: en1gma/console/map_v2/trace.py
  allowed: false
  rationale: "market_state is snapshot-only; Stage 2C must not widen the trace contract."

forbidden_files:
  - en1gma/console/map/map_engine.py
  - en1gma/console/chain/gate.py
  - en1gma/console/chain/chain_evaluator.py
  - en1gma/orchestrator/*
  - en1gma/cartridges/*
  - en1gma/console/governance/*
  - en1gma/console/execution/*
```

---

## 12. Slice dependency rule

```yaml
slice_dependency_rule:
  sequence:
    1_balance_enum_type_extension: "enum/type/coupling tests only"
    2_balance_snapshot_roundtrip: "snapshot serialization/hash roundtrip only; trace remains unchanged"
    3_balance_fixture_extension: "one deterministic construction fixture + replay hash update"
    4_final_v1_equivalence: "full validation/report only"
  rule: |
    Slice 1 must land before slice 2; slice 2 before slice 3; slice 3 before
    final equivalence. Each slice independently green. No cross-slice rollback.

atomic_commit_discipline:
  rule: "One logical change per commit; each commit independently passes scoped gates."
  commit_message_must_cite:
    - Stage_2C_scope
    - frozen_stage_1_sha_f2ffc34405e82b573e6ced5058977d8f564936f9
    - stage_1A_balance_sha_59985ce6db71acd4c8b0ff587a4b5cc4bbb375c6
```

---

## 13. Validation minimum

```yaml
brief_authoring_validation:
  - git_diff_check
  - brief_sanity_check
  - stale_authorization_language_check
  - sensitive_text_check
  - subagent_review

if_later_executed_after_G_ratification:
  - git_diff_check
  - pytest en1gma/tests/console/map_v2/
  - mypy en1gma/console/map_v2
  - lint-imports --config pyproject.toml
  - full_v1_smoke_suite
  - chart_truth_canonical_11_12_with_trade_011_visible
  - v1_baseline_final_artifact_comparison
```

---

## 14. Halt gates

```yaml
halt_if:
  - implementation_needs_BALANCE_detection_algorithm
  - implementation_needs_HTF_level_selection_semantics
  - implementation_needs_liquidity_present_on_both_sides_logic
  - implementation_needs_no_clean_progression_threshold
  - implementation_needs_candle_count_or_attempt_count_threshold
  - implementation_starts_encoding_strategy_behavior
  - implementation_touches_producer_or_v1_runtime
  - implementation_touches_schema_or_cartridge_surfaces
  - implementation_attempts_to_resolve_trade_011
  - implementation_requires_market_data_inference
  - implementation_widens_trace_with_market_state
  - implementation_rebaselines_chart_truth_or_claims_v2_certification

methodology_route: G_to_Olya
```

---

## 15. Subagent validation posture

```yaml
subagent_validation_posture:
  counter_resets_at_stage_start: true
  threshold: "3 transient failures in Stage 2C execution"
  on_threshold_hit: halt_and_report
```

---

## 16. Green condition if executed later

```yaml
green_condition_if_executed_later: |
  BALANCE is representable in the inert v2 shell and deterministic fixture
  corpus without producer logic, strategy logic, v1 drift, trade_011 drift, or
  certification claim. Stage 2A/2B inertness remains intact.

explicit_non_green:
  - "BALANCE represented through detector/producer logic."
  - "BALANCE encoded as strategy permission."
  - "market_state added to trace surface."
  - "Any v1 runtime path imports or consumes BALANCE fields."
  - "trade_011 hidden, skipped, repaired, or reclassified."
  - "Any v2 certification, chart-truth rebaseline, walk-forward, or performance claim."
```

---

## 17. Final report requirements if executed later

```yaml
final_report_if_executed_later:
  must_include:
    - stage_2C_ratified_brief_commit_sha
    - implementation_commit_list
    - files_touched
    - BALANCE_tests_added
    - construction_case_id_if_fixture_added
    - generated_by_stage_value_if_fixture_added
    - corpus_count_before_after
    - baseline_final_v1_artifact_comparison
    - chart_truth_status
    - trade_011_boundary_status
    - explicit_non_claims
    - unrelated_doctrine_folder_status
```

---

## 18. No-code close statement

```yaml
brief_authoring_only: true
implementation_authorized: false
runtime_behavior_changed: false
console_files_modified_by_this_brief: false
schema_files_modified_by_this_brief: false
cartridge_files_modified_by_this_brief: false
BALANCE_enum_type_extension_implemented: false
BALANCE_fixture_created: false
BALANCE_detection_algorithm_created: false
MapV2Engine_producer_implemented: false
strategy_permission_logic_added: false
DAILY_EXPANSION_migrated: false
H4_authority_resurrected: false
target_ranking_added: false
v2_certification_claimed: false
trade_011_repaired: false
```
