This brief does not authorize implementation until G ratifies it.

# PHASE_5.STAGE_2B — Map v2 Construction Replay Harness

```yaml
brief_id: PHASE_5_STAGE_2B_MAP_V2_CONSTRUCTION_REPLAY_HARNESS_BRIEF_DRAFT_2026_04_29
mission_id: PHASE_5.STAGE_2B.MAP_V2_CONSTRUCTION_REPLAY_HARNESS
classification: IMPLEMENTATION_BRIEF_DRAFT | NOT_AUTHORIZED_TO_EXECUTE
recommended_slice: PARALLEL_REPLAY_FOUNDATION
status: G_RATIFIED_FOR_EXECUTION
behavior_change_authorized: false
runtime_changes_authorized: false
schema_changes_authorized: false
cartridge_changes_authorized: false
implementation_authorized: false
implementation_authorized_scope: STRICT_STAGE_2B_ONLY
certification_authorized: false
execution_ratification:
  decision: G_RATIFIES_STAGE_2B_EXECUTION
  ratification_date: 2026-04-29
  status: APPROVED_FOR_EXECUTION
  scope: "strictly under the patched Stage 2B brief"
  text: |
    G ratifies PHASE_5.STAGE_2B.MAP_V2_CONSTRUCTION_REPLAY_HARNESS for
    execution strictly under the patched Stage 2B brief.

    Authorization is limited to a parallel deterministic construction/replay
    harness for inert Map v2 read-model instances, using explicit controlled
    inputs or fixtures only. Authorization includes deterministic fixture
    artifacts, canonical serialization/hash stability, EvidenceRef ordering
    checks, target inventory canonicalization checks, v1 baseline/final smoke
    artifacts, and Stage 2A regression preservation.

    This ratification does not authorize a MapV2Engine producer, market-data
    inference, methodology interpretation, MapEngine/Gate/Chain/Orchestrator
    changes, cartridge/schema changes, DAILY_EXPANSION migration, H4 authority,
    target ranking, v2 certification claims, walk-forward claims, chart-truth
    rebaseline, or trade_011 repair.
pre_execution_sequence:
  P0_first: "commit and push this ratified brief before implementation begins"
  P2_second: "capture v1_smoke_baseline.yaml only after P0 is anchored"
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
stage_2A_pointer:
  path: docs/reviews/PHASE_5_STAGE_2A_MAP_V2_READ_MODEL_TRACE_SHELL_BRIEF_DRAFT_2026_04_29.md
  pushed_commit_sha: 335a8f15d137271e67d032d594b1be46c49776dc
  exact_status: EXECUTED_AND_PUSHED
phase_decision: docs/reviews/PHASE_4_CLOSE_PHASE_5_OPEN_DECISION_BRIEF_2026_04_29.md
architecture_boundary: docs/canonical/CARTRIDGE_CONTRACT.md
```

---

## 1. Non-authorization header

```yaml
non_authorization:
  exact_line: "This brief does not authorize implementation until G ratifies it."
  meaning: |
    This document is a Stage 2B mission brief draft for review. It may be used
    for Chair / Chief Architect / G review, but no code, artifact generation,
    replay harness implementation, schema, cartridge, migration, or runtime
    execution may begin from it until G separately ratifies Stage 2B execution.

not_authorized:
  - implementation
  - code_changes
  - artifact_generation
  - schema_changes
  - cartridge_changes
  - MapV2Engine_producer
  - MapEngine_behavior_changes
  - Gate_Chain_Orchestrator_changes
  - DAILY_EXPANSION_v1_migration
  - DAILY_EXPANSION_v2_read_path
  - DMB_MEM_TRM_implementation_or_promotion
  - H4_core_authority
  - target_ranking
  - v1_trace_retirement
  - v2_certification_claim
  - trade_011_repair_attempt
  - methodology_seed_interpretation
```

---

## 2. Mission thesis

```yaml
thesis: |
  Build a parallel deterministic construction/replay harness for Map v2
  read-model instances using the inert Stage 2A shell. The harness must remain
  isolated from v1 runtime and must not become the Map v2 producer.

primary_goal: |
  Turn hand-constructed v2 objects into deterministic construction artifacts:
  legal snapshot/trace payloads, canonical serialization, and stable hashes
  from explicit controlled inputs.

non_negotiable: |
  Stage 2B is construction-only. If it infers Olya methodology from market data,
  becomes a producer, affects a v1 replay result, or creates a strategy-consumed
  read path, it is too broad.
```

---

## 3. Inheritance from Stage 1 and Stage 2A

```yaml
stage_1_inheritance:
  frozen_contract_source: docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md
  required_inheritance:
    - "Map v2 is a Daily-authority interpreted read model, not an execution instruction."
    - "construction_mode values remain OK | CANNOT_DETERMINE; FALLBACK is forbidden."
    - "direction.status/value and actionability_state remain separate epistemic surfaces."
    - "Core Map direction remains Daily-only."
    - "H4 remains strategy-specific only and never core Map authority."
    - "PD/quadrant output remains label-only; strategy owns permission."
    - "dominant_draw is narrative context only, non-executable."
    - "available_htf_targets remains unordered and unranked."
    - "evidence_refs remain typed, stable, and replay-deterministic."
    - "V1 and v2 traces remain parallel until explicit retirement decision."

stage_2A_inheritance:
  executed_surface: en1gma/console/map_v2/
  required_inheritance:
    - "Use the inert immutable Stage 2A shells as the only v2 construction target."
    - "No v1 runtime surface imports, calls, dispatches to, or consumes map_v2."
    - "No pyproject/import-linter config touch unless separately justified and isolated."
    - "Preserve Stage 2A inertness tests and extend them only if needed."
    - "Preserve canonical tuple ordering for evidence_refs and target inventory."
    - "Preserve cold_start_instance as legal CANNOT_DETERMINE shape, not runtime inference."

deferred_residuals_preserved:
  target_status_enum: "Do not expand beyond inert UNSWEPT/COMPLETED shell behavior."
  v1_trace_retirement_detail: "Do not retire or replace v1 trace evidence."
  bootstrap_behavior: "Do not invent runtime bootstrap methodology."
  halt_scope_nuance: "Engineering packaging is allowed; methodology interpretation halts."
```

---

## 4. Stage 2B scope

```yaml
in_scope_for_stage_2B_if_ratified:
  - parallel_v2_construction_harness_for_explicit_inputs
  - deterministic_fixture_or_sample_generation
  - serialization_hash_stability_for_v2_snapshots
  - serialization_hash_stability_for_v2_traces
  - evidence_ref_ordering_and_replay_stability_assertions
  - target_inventory_canonical_order_assertions
  - cold_start_CANNOT_DETERMINE_construction_path
  - construction_only_replay_artifacts_for_v2_shell
  - v2_only_artifact_output_under_tests_fixtures_map_v2_stage_2B
  - before_after_v1_smoke_preservation
  - trade_011_canonical_visible_boundary_preservation

out_of_scope_for_stage_2B:
  - actual_MapV2Engine_producer
  - market_data_detection_or_methodology_inference
  - daily_methodology_interpretation
  - MapEngine_behavior_changes
  - Gate_Chain_Orchestrator_changes
  - governance_execution_or_broker_changes
  - DAILY_EXPANSION_v1_migration
  - DAILY_EXPANSION_v2_read_path
  - cartridge_schema_or_yaml_changes
  - H4_authority_or_strategy_overlay
  - target_ranking_or_next_target_logic
  - target_completion_runtime_behavior
  - v2_certification_claim
  - trade_011_repair_attempt
```

---

## 5. Expected files and forbidden surfaces

Final file list must be repo-audited before execution. Stage 2B should prefer new v2-specific modules and tests over edits to any v1 authority surface.

```yaml
preferred_new_files_if_ratified:
  - en1gma/console/map_v2/construct.py
  - en1gma/console/map_v2/replay.py
  - en1gma/tests/console/map_v2/test_v2_construction_determinism.py
  - en1gma/tests/console/map_v2/test_v2_replay_harness.py

artifact_output_location:
  primary_path: tests/fixtures/map_v2/stage_2B/
  rationale: |
    Stage 2B artifacts are deterministic construction fixtures, not runtime
    reports or certification outputs. Keeping them under the test fixture tree
    makes non-runtime status structurally visible.
  allowed_files:
    - tests/fixtures/map_v2/stage_2B/construction_replay_sample.yaml
    - tests/fixtures/map_v2/stage_2B/replay_hashes.yaml
    - tests/fixtures/map_v2/stage_2B/v1_smoke_baseline.yaml
    - tests/fixtures/map_v2/stage_2B/v1_smoke_final.yaml
  reports_path_allowed: false
  reports_path_exception: "Requires separate G/CTO decision; not Stage 2B."

possible_config_touch_requires_review:
  - pyproject.toml
  note: |
    Only if import-linter needs explicit map_v2 replay-harness awareness.
    Any config touch must be isolated as its own atomic commit and cannot be
    hidden inside construction/hashing slices.

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
  - en1gma/observe/replay.py
  - en1gma/observe/decision_trace.py
  - en1gma/console/governance/
  - en1gma/console/execution/

artifact_path_forbidden_collisions:
  - traces/map_*
  - chain_trace.jsonl
  - decision_trace.jsonl
  - map_timeline.jsonl
  - map_state.json
  - session_summary.yaml
```

---

## 6. Construction harness design boundary

```yaml
construction_harness_boundary:
  allowed_input_source: "explicit controlled construction cases or fixtures"
  forbidden_input_sources:
    - River_market_data
    - detect_py_live_or_replay_detection
    - MapEngine_state
    - Gate_or_Chain_state
    - Orchestrator_runtime_outputs
    - cartridge_strategy_config

allowed_output_shapes:
  - MapV2Output
  - MapV2Snapshot
  - MapV2TraceMinimum
  - EvidenceRef_payloads
  - deterministic_hash_records
  - construction_replay_sample_artifact

producer_boundary:
  not_a_producer: true
  must_not:
    - infer_direction_from_bars
    - detect_MSS_or_displacement
    - select_origin_swing_from_price_action
    - select_dominant_draw_from_market_data
    - advance_range_lifecycle
    - decide_target_completion_runtime_behavior
    - emit_strategy_permission
    - feed_DAILY_EXPANSION_v1_or_v2

methodology_safety_rule: |
  The harness may construct legal v2 objects from explicit values. It may not
  decide what those values should be from market evidence unless that decision
  is already frozen as a pure packaging rule in Stage 1/2A.
```

---

## 7. Deterministic serialization and hashing contract

```yaml
hashing_contract:
  hash_algorithm: sha256
  canonical_payload_source:
    snapshot: MapV2Snapshot.to_payload()
    trace: MapV2TraceMinimum.to_payload()
    evidence_ref: EvidenceRef.to_payload()
  canonical_serialization:
    format: json
    requirements:
      - sort_keys_true
      - compact_separators
      - utf8
      - no_current_time
      - no_random_uuid
      - no_unordered_dict_iteration_semantics
      - no_platform_specific_path_values_in_hash_input

stable_ordering_requirements:
  evidence_refs: "sort by ref_id, source_time, ref_type"
  target_inventory: "sort by target_id, price, source_ref"
  direction_evidence_refs: "stable sorted tuple"
  strategy_consumer_read_surface: "stable sorted tuple"
  available_htf_targets: "stable tuple canonicalization before serialization"

required_hash_records:
  - construction_case_id
  - map_contract_version
  - snapshot_hash
  - trace_hash
  - evidence_refs_hash_or_inline_refs
  - source_commit_sha
  - generated_at_commit_sha
  - generated_by_stage
  - explicit_non_certification_flag

hash_record_commit_precision:
  source_commit_sha: "commit containing construction fixture input"
  generated_at_commit_sha: "commit at which artifact was generated"
  rule: "If source and generation commit are identical, record both with the same value."

construction_case_id_contract:
  scope: globally_unique_within_stage_2B_artifact_corpus
  generation_rule: |
    Derived from stable SHA256 hash of canonical input_payload, prefixed with
    case purpose, e.g. cold_start_<hash12>. Must not be random, sequential,
    timestamp-derived, or manually reused across different payloads.
  collision_rule: "Duplicate construction_case_id with different input_payload aborts Stage 2B."
  stability_rule: "Same canonical input_payload must produce same construction_case_id across re-runs."
```

---

## 8. V2 construction replay artifacts

```yaml
artifact_policy:
  stage: PHASE_5_STAGE_2B
  type: construction_only
  output_location: tests/fixtures/map_v2/stage_2B/
  reports_path_allowed: false
  may_be_committed_if:
    - deterministic
    - small
    - v2_only
    - generated_from_explicit_fixture_or_sample
    - carries_no_secret_or_runtime_state
    - cannot_be_confused_with_certified_v1_replay_output
  must_not:
    - overwrite_v1_replay_outputs
    - use_existing_v1_trace_filenames
    - write_to_reports_path_without_separate_G_CTO_decision
    - include_broker_or_account_data
    - imply_walk_forward_or_chart_truth_certification
    - hide_trade_011_failure

yaml_carrier_not_hash_input:
  rule: |
    YAML artifact files are readability carriers only. Hashes must be computed
    from canonical JSON payloads per Section 7, never from YAML emitter output.

initial_corpus_bound:
  max_committed_construction_cases: 10
  expansion_requires: separate_brief_or_explicit_CTO_G_approval

sample_artifact_minimum_fields:
  - stage
  - construction_case_id
  - map_contract_version
  - input_payload
  - snapshot_payload
  - trace_payload
  - snapshot_hash
  - trace_hash
  - validation_notes
  - explicit_non_claims

explicit_non_claims_minimum_set:
  - stage_2B_does_not_certify_v2
  - artifact_is_construction_only_not_runtime_replay
  - artifact_does_not_imply_chart_truth_status
  - artifact_does_not_imply_walk_forward_status
  - artifact_does_not_migrate_DAILY_EXPANSION_v1
  - artifact_does_not_feed_runtime_or_strategy
  - trade_011_remains_v1_doctrine_seed_boundary
```

---

## 9. Inertness proof

Stage 2B inertness must be proven by structure and tests, not by prose.

```yaml
structural_module_separation:
  required_package: en1gma.console.map_v2
  forbidden_runtime_import_direction: "v1 runtime surfaces must not import map_v2"

inertness_assertions:
  import_graph_assertion:
    rule: |
      No module in en1gma/console/map/, en1gma/console/chain/,
      en1gma/orchestrator/, en1gma/scripts/, en1gma/cartridges/,
      en1gma/console/governance/, or en1gma/console/execution/ imports
      en1gma.console.map_v2.

  call_graph_assertion:
    rule: "No v1 runtime entrypoint resolves to a v2 construction or replay symbol."

  consumer_set_assertion:
    rule: "Only map_v2 modules, map_v2 tests, and v2-only artifact generation code import the Stage 2B harness."

  no_runtime_consumption_assertion:
    rule: "No gate, chain, MapEngine, orchestrator, governance, execution, cartridge, or DAILY_EXPANSION_v1 path reads v2 fields or Stage 2B artifacts."

  artifact_inertness_assertion:
    rule: "Stage 2B artifacts are fixture outputs only and are not read by v1 runtime."
```

---

## 10. V1 replay continuity gate

```yaml
v1_replay_continuity_gate:
  mandatory: true
  before_after_required: true
  required_sequence:
    - v1_smoke_BEFORE_stage_2B_changes
    - apply_stage_2B_changes_if_ratified
    - quick_v1_smoke_after_each_atomic_commit
    - full_v1_smoke_AFTER_final_stage_2B_commit
    - compare_result_shape_and_hashes_where_available
  rule: "Any v1 replay, trace, chart-truth, or smoke drift aborts Stage 2B."

baseline_gate_amendment_source:
  commit_sha: 66073831da853bbb9ed73c40fd55e95dd5b75400
  rule: "Stage 2B inherits the canonical 11/12 chart-truth gate from this amendment."

v1_baseline_artifact_capture:
  required_before_commit_1: true
  artifact_path: tests/fixtures/map_v2/stage_2B/v1_smoke_baseline.yaml
  post_artifact_path: tests/fixtures/map_v2/stage_2B/v1_smoke_final.yaml
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
  comparison_rule: |
    Final artifact must match baseline on test counts, pass/fail shape, sole
    red identity, trade_011 boundary classification, and chart-truth/fixture
    file hashes. Byte/hash equivalence of raw command output is preferred if
    stable, but structured content equivalence is mandatory.

v1_chart_truth_baseline_exception:
  accepted_known_boundary: trade_011
  expected_state: "BLOCKED_BY_METHODOLOGY_SEED / known v1 doctrine-seed boundary"
  accepted_baseline: "11/12 chart-truth with trade_011 as sole red/blocked fixture"
  not_an_abort_condition: true
  required_visibility:
    - "Run full 12-fixture chart-truth suite."
    - "Do not use -k not trade_011."
    - "Do not skip, repair, reclassify, or hide trade_011."
    - "If feasible, add an explicit named visibility assertion only in a later harness-hardening pass, not by expanding Stage 2B."
  abort_conditions:
    - any_additional_chart_truth_failure
    - trade_011_status_changes_unexpectedly
    - trade_011_is_repaired_hidden_skipped_without_log_or_reclassified
    - any_non_chart_truth_smoke_fails

v1_file_hash_guard:
  required_for_final_report:
    - en1gma/tests/integration/test_daily_expansion_chart_truth.py
    - en1gma/ground_truth/annotated_trades.yaml
  rule: "Confirm chart-truth test and fixture surfaces were not modified by Stage 2B unless separately ratified."
```

---

## 11. Methodology ambiguity halt gate

```yaml
methodology_halt_gate:
  rule: |
    Any ambiguity that changes, interprets, extends, narrows, or operationalizes
    Olya methodology halts Stage 2B and routes the exact question G -> Olya.
    CTO, Chair, Chief Architect, and agents may frame the question but must not
    answer it.

halt_if_harness_needs:
  - wick_vs_close_vs_body_quadrant_semantics
  - follow_through_semantics
  - real_dominant_draw_selection_beyond_frozen_non_executable_precedence
  - target_lifecycle_behavior_beyond_UNSWEPT_COMPLETED_shell
  - origin_swing_selection_from_market_data
  - daily_mss_or_displacement_detection_from_bars
  - reassessment_exit_semantics
  - producer_like_state_transition_behavior

route: "G -> Olya"
note: |
  If any of the above occurs, Stage 2B is too broad or has crossed into C2
  producer work.
```

---

## 12. Tests required before green

```yaml
new_stage_2B_tests_if_ratified:
  - same_input_same_snapshot_hash
  - same_input_same_trace_hash
  - evidence_refs_canonical_order_stable
  - target_inventory_canonical_order_stable
  - cold_start_replay_constructs_CANNOT_DETERMINE_legally
  - construction_does_not_import_or_call_v1_runtime
  - artifact_output_is_v2_only_and_not_runtime_consumed

expected_test_count_minimum:
  stage_2A_regression_tests: 14
  new_stage_2B_tests: 7
  total_minimum: 21

stage_2A_tests_must_remain_green:
  - type_shape_roundtrip
  - immutable_type_property
  - cold_start_instance_contract_legal
  - evidence_ref_uniqueness
  - evidence_ref_deterministic_construction_stability
  - direction_unknown_requires_null_and_cannot_determine
  - construction_mode_forbids_FALLBACK
  - target_inventory_forbids_ordering_fields
  - trace_minimum_serializes_round_trips_and_canonicalizes_refs
  - trace_minimum_enforces_direction_shape_and_contract_version
  - snapshot_serializes_round_trips_freezes_and_sorts_target_inventory
  - v1_runtime_surfaces_do_not_import_map_v2_package
  - importing_v1_map_package_does_not_load_map_v2_modules
  - importing_map_v2_package_does_not_load_v1_runtime_surfaces

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
```

---

## 13. Validation commands

```yaml
validation_minimum:
  - git diff --check
  - pytest en1gma/tests/console/map_v2/
  - mypy en1gma/console/map_v2
  - lint-imports --config pyproject.toml
  - pytest en1gma/tests/integration/test_map_canon_runner_parity.py
  - pytest en1gma/tests/integration/test_replay_no_future_leak.py
  - pytest en1gma/tests/integration/test_daily_expansion_chart_truth.py
  - pytest en1gma/tests/integration/test_sw49_construction_mode.py
  - pytest en1gma/tests/integration/test_decision_trace_construction_enrichment.py

commit_cadence:
  before_commit_1: "full v1 smoke baseline; chart-truth 11/12 trade_011 visible"
  after_each_atomic_commit: "pytest en1gma/tests/console/map_v2/ + quick v1 smoke subset"
  before_push: "full validation_minimum"
```

---

## 14. Atomic commit discipline

```yaml
atomic_commit_discipline:
  rule: "One logical change per commit; each commit independently passes scoped type/lint/test gates."
  no_partial_pass_merges: true
  commit_message_must_cite:
    - Stage_2B_scope
    - frozen_artifact_sha_f2ffc34405e82b573e6ced5058977d8f564936f9
  suggested_commit_slices_if_ratified:
    1_replay_harness_shell: "construct/replay module + no-runtime import tests"
    2_deterministic_hashing: "snapshot/trace hash outputs + stability tests"
    3_fixture_artifact_generation: "sample construction replay report/artifact"
    4_final_inertness_and_v1_equivalence: "final tests/report only"
```

---

## 15. Abort criteria

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
  - Stage_2B_harness_becomes_producer
  - MapV2Engine_or_equivalent_real_producer_added
  - harness_reads_market_data_to_infer_methodology
  - artifact_output_overwrites_or_mimics_v1_certified_outputs
  - duplicate_construction_case_id_with_different_input_payload
  - v1_baseline_artifact_capture_skipped
  - artifact_written_to_reports_path_without_separate_G_CTO_decision
  - corpus_exceeded_initial_bound
  - evidence_refs_are_free_form_strings_without_stable_replay_semantics
  - construction_mode_permits_FALLBACK
  - direction_unknown_can_carry_stale_bullish_or_bearish
  - target_inventory_has_ordering_or_ranking_fields
  - pyproject_or_import_linter_config_touch_hidden_inside_other_slice
  - v2_certification_claim_made
  - trade_011_repair_attempted
```

---

## 16. Certification delta link

```yaml
certification_delta:
  stage_2B_certifies_v2: false
  stage_2B_creates: "deterministic construction replay evidence for inert v2 shells"
  future_target: TRACE_CERTIFIED_DAILY_AUTHORITY_V2_PENDING
  v1_certification_transfer: false
  v1_runtime_certification_impact: none_expected_and_must_be_proven_by_smoke
  chart_truth_rebaseline_done: false
  walk_forward_done: false
  trade_011_resolved: false
```

---

## 17. Subagent validation posture

```yaml
subagent_validation_posture:
  primary: subagent_validation
  fallback: direct_CTO_validation_with_explicit_log_entry
  transient_failure_threshold: 3
  threshold_scope: "Counter resets at the start of each Stage execution gate."
  threshold_rule: "Three transient subagent failures in one session triggers halt-and-report rather than continuing by direct fallback."
```

---

## 18. Stage 2B authoring exit criteria

```yaml
stage_2B_authoring_exit_criteria:
  deliverable:
    owner: CTO
    condition: "Stage 2B brief draft complete with Stage 1/2A pointers and construction-only boundaries."

  boundary_review:
    owners:
      - Claude_Chair
      - Chief_Architect_GPT
    condition: "No producer leakage, v1/v2 isolation breach, H4 leakage, target ranking, strategy contamination, certification overclaim, or artifact collision."

  methodology_consistency:
    owner: G
    condition: "Any open methodology ambiguity is routed to Olya or explicitly marked blocking."

  ratification:
    owner: G
    condition: "G authorizes or rejects Stage 2B execution."

  gate_to_implementation:
    rule: "All four criteria required. This brief alone authorizes no implementation."
```

---

## 19. Green condition if executed later

```yaml
green_condition_if_executed_later: |
  Stage 2B is green only if v2 construction replay is deterministic,
  artifacted, and hash-stable; Stage 2A inertness remains intact; v1 behavior
  and v1 smoke result shape are unchanged; no methodology is interpreted; no
  producer is added; no v2 certification is claimed.

explicit_non_green:
  - "Harness reads market data and infers v2 state."
  - "Harness output is consumed by DAILY_EXPANSION_v1 or any runtime path."
  - "Evidence refs or target inventory have insertion-order replay semantics."
  - "Artifacts overwrite or masquerade as certified v1 replay outputs."
  - "trade_011 is hidden, skipped, repaired, or reclassified."
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
replay_harness_implemented: false
MapV2Engine_producer_implemented: false
DAILY_EXPANSION_v1_migrated: false
DAILY_EXPANSION_v2_read_path_created: false
DMB_MEM_TRM_implemented: false
H4_authority_resurrected: false
target_ranking_added: false
v2_certification_claimed: false
trade_011_repaired: false
```
