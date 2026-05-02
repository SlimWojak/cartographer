This brief does not authorize implementation.

# PHASE_5.STAGE_1A — BALANCE Market State Contract Amendment

```yaml
brief_id: PHASE_5_STAGE_1A_BALANCE_MARKET_STATE_CONTRACT_AMENDMENT_BRIEF_DRAFT_2026_04_29
mission_id: PHASE_5.STAGE_1A.BALANCE_MARKET_STATE_CONTRACT_AMENDMENT
classification: NO_CODE | CONTRACT_AMENDMENT | NOT_IMPLEMENTATION
status: G_RATIFIED_CONTRACT_AMENDMENT
behavior_change_authorized: false
runtime_changes_authorized: false
schema_changes_authorized: false
cartridge_changes_authorized: false
implementation_authorized: false
certification_authorized: false
contract_amendment_ratification:
  decision: G_RATIFIES_STAGE_1A_BALANCE_CONTRACT_AMENDMENT
  ratification_date: 2026-04-29
  status: G_RATIFIED_CONTRACT_AMENDMENT
  implementation_authorized: false
  text: |
    G ratifies HTF Map v0.15 BALANCE as an additive Map v2 contract
    amendment. BALANCE is added as a market_state value. It preserves known
    Daily direction, remains actionability_state=actionable, is not neutral,
    not reassessment, not paused, and not cannot_determine.

    Map outputs market_state=balance as context only. Strategies decide trade
    permission and trend/scalp behavior. Deterministic BALANCE detection logic
    is not formalized in v0.15 and must not be invented. BALANCE requirements
    are conceptual contract predicates, not direct detector gates. Future
    producer work requiring BALANCE detection must route to Olya for chart
    examples and example-based calibration.
owner: CTO
reviewers:
  - Chief_Architect_GPT
  - Claude_Chair
  - G
date: 2026-04-29
methodology_source:
  primary: docs/reviews/OLYA_NEX_HTF_MAP_v0_15_BALANCE_PATCH.md
  source_status: Olya_methodology_input
  source_version: "0.15"
  includes:
    - initial_v0_15_balance_patch
    - balance_detection_refinement_followup
  source_payload_parse_check:
    status: PASS
    parsed_as: well_formed_yaml_mapping
    required_keys_present:
      - actionability_state.enum
      - market_state.enum
      - balance.definition
      - balance.requirements
      - balance.behavior
      - balance.strategy_relationship
      - balance.assignment
      - state_definitions
      - map_vs_strategy
      - balance_detection_refinement
amends_frozen_contract:
  path: docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md
  frozen_commit_sha: f2ffc34405e82b573e6ced5058977d8f564936f9
  amendment_type: additive_market_state_contract_delta
stage_2A_pointer:
  path: docs/reviews/PHASE_5_STAGE_2A_MAP_V2_READ_MODEL_TRACE_SHELL_BRIEF_DRAFT_2026_04_29.md
  pushed_commit_sha: 335a8f15d137271e67d032d594b1be46c49776dc
stage_2B_pointer:
  path: docs/reviews/PHASE_5_STAGE_2B_MAP_V2_CONSTRUCTION_REPLAY_HARNESS_BRIEF_DRAFT_2026_04_29.md
  pushed_commit_sha: 95e321bb11e55ebf981af3f90a48de337d312f2f
phase_decision: docs/reviews/PHASE_4_CLOSE_PHASE_5_OPEN_DECISION_BRIEF_2026_04_29.md
architecture_boundary: docs/canonical/CARTRIDGE_CONTRACT.md
```

---

## 1. Non-authorization header

```yaml
non_authorization:
  exact_line: "This brief does not authorize implementation."
  meaning: |
    This document is a no-code contract amendment brief for review. It may be
    used for Chair / Chief Architect / G review and possible ratification, but
    it does not authorize code, schema, cartridge, producer, replay, artifact,
    migration, certification, strategy, or runtime work.

not_authorized:
  - code_changes
  - schema_changes
  - cartridge_changes
  - runtime_changes
  - MapV2Engine_producer
  - deterministic_BALANCE_detection_algorithm
  - market_data_inference
  - candle_count_thresholds
  - attempt_count_thresholds
  - invented_failure_patterns
  - strategy_permission_logic_in_Map
  - DMB_TRM_MEM_implementation
  - DAILY_EXPANSION_v1_migration
  - DAILY_EXPANSION_v2_read_path
  - H4_authority
  - target_ranking
  - v2_certification_claim
  - trade_011_repair
```

---

## 2. Methodology source summary

```yaml
source_methodology_summary:
  source_file: docs/reviews/OLYA_NEX_HTF_MAP_v0_15_BALANCE_PATCH.md
  source_version: "0.15"
  source_payload_parse_check:
    status: PASS
    parsed_as: well_formed_yaml_mapping
    required_keys_present:
      - actionability_state.enum
      - market_state.enum
      - balance.definition
      - balance.requirements
      - balance.behavior
      - balance.strategy_relationship
      - balance.assignment
      - state_definitions
      - map_vs_strategy
      - balance_detection_refinement

  version_label_note: |
    Olya/NEX described this as a patch to the prior HTF Map spec, not a
    rewrite. Repository convention records the patched methodology input as
    v0.15 superseding/amending v0.14.

  summary: |
    Olya/NEX adds BALANCE as a Map v2 market_state. BALANCE describes a
    non-directional execution environment inside known directional context:
    Daily direction is known and persists, price is between opposing HTF
    levels, progression is not clean expansion or pullback, and liquidity may
    exist on both sides before the next expansion.

  source_enum_delta:
    actionability_state_unchanged:
      - actionable
      - paused_reassessment
      - cannot_determine
    market_state_add:
      - balance

  source_behavior:
    direction: persists
    actionability_state: actionable
    not_neutral: true
    not_reassessment: true
    not_paused: true
    can_be_assigned_directly: true
    does_not_require_prior_expansion_or_pullback: true

  source_detection_refinement:
    failure_definition_status: NOT_FORMALIZED
    failure_manifestations_non_exhaustive:
      - rejection
      - stalling
      - LTF_shifts
      - range_formation
    producer_phase_requirement: "derive later from chart examples and validated behavior"

  ratification_artifact_audit_chain:
    on_ratification: "commit SHA must be captured"
    downstream_anchoring: |
      Future BALANCE-related briefs, including Stage 2C and C2 producer
      preflight/implementation briefs, must cite this Stage 1A amendment
      commit SHA in addition to f2ffc34405e82b573e6ced5058977d8f564936f9.
```

---

## 3. Six-question resolution summary

```yaml
six_question_resolution_summary:
  Q1_should_Map_v2_add_BALANCE:
    answer: YES
    contract_effect: "Add balance to market_state enum."

  Q2_does_BALANCE_change_Daily_direction:
    answer: NO
    contract_effect: "Daily direction remains known and persists."

  Q3_does_BALANCE_pause_or_block_actionability:
    answer: NO
    contract_effect: "actionability_state remains actionable; BALANCE is not reassessment, not paused, and not cannot_determine."

  Q4_can_BALANCE_be_assigned_directly:
    answer: YES
    contract_effect: "BALANCE does not require prior expansion or pullback state."

  Q5_who_decides_strategy_behavior_under_BALANCE:
    answer: STRATEGY
    contract_effect: "Map outputs market_state=balance only; trend/scalp permissions are strategy-owned."

  Q6_is_deterministic_BALANCE_detection_formalized_now:
    answer: NO
    contract_effect: |
      Producer detection logic is deferred to future Olya example-based
      calibration. Includes followup confirmation: do not invent fixed
      patterns, candle counts, or attempt counts; producer semantics require
      examples.
```

---

## 4. BALANCE contract delta

```yaml
balance_contract_delta:
  enum_delta:
    market_state_before:
      - expansion
      - pullback
      - approaching_target
      - reassessment
    market_state_after:
      - expansion
      - pullback
      - approaching_target
      - reassessment
      - balance

  definition: |
    BALANCE is a non-directional execution environment inside known
    directional context: Daily direction is known and persists, but price is
    between opposing HTF levels, not progressing cleanly as expansion or
    pullback, and liquidity may be present on both sides before the next
    expansion.

  requirements:
    - direction_known
    - price_between_opposing_htf_levels
    - no_clean_expansion_or_pullback_progression
    - liquidity_present_on_both_sides

  behavior:
    direction: persists
    actionability_state: actionable
    not_neutral: true
    not_reassessment: true
    not_paused: true
    can_be_assigned_directly: true
    does_not_require_prior_expansion_or_pullback: true

  requirement_interpretation_rule: |
    BALANCE requirements are conceptual contract predicates in Stage 1A. They
    are not sufficient detector gates and must not be implemented as direct
    boolean code without Olya example-based calibration.

  market_state_definitions_v0_15:
    expansion: movement_from_pd_context_toward_external_liquidity
    pullback: movement_from_range_extreme_back_toward_midpoint_or_pd_context
    approaching_target: price_inside_near_target_zone
    reassessment: after_target_touch_direction_persists_but_actionability_pauses
    balance: non_directional_execution_environment_inside_known_directional_context
    rule: |
      These are Olya/NEX v0.15 methodology definitions. Stage 1A records them
      as contract language; it does not implement deterministic producer
      detection.

  explicit_non_meanings:
    - "BALANCE is not NEUTRAL."
    - "BALANCE is not actionability_state=paused_reassessment."
    - "BALANCE is not actionability_state=cannot_determine."
    - "BALANCE is not H4 conflict or H4 alignment."
    - "BALANCE is not a strategy permission field."
    - "BALANCE is not an execution instruction."
```

---

## 5. Market state / actionability coupling amendment

```yaml
market_state_vs_actionability_state_coupling_amendment:
  market_state:
    type: descriptive_market_context
    may_equal:
      - expansion
      - pullback
      - approaching_target
      - reassessment
      - balance

  actionability_state:
    type: permission_context_for_strategy_consumption
    may_equal:
      - actionable
      - paused_reassessment
      - cannot_determine

  coupling:
    - "market_state=balance requires direction.status=known."
    - "market_state=balance requires actionability_state=actionable."
    - "market_state=balance is forbidden when actionability_state=paused_reassessment."
    - "market_state=balance is forbidden when actionability_state=cannot_determine."
    - "market_state=balance does not reset, neutralize, or flip Daily direction."
    - "market_state=balance does not by itself authorize or block execution; strategy owns behavior."
    - "actionability_state remains the only strategy-consumption permission field."
```

---

## 6. Strategy boundary invariant

```yaml
strategy_boundary_invariant:
  invariant: |
    Map outputs market_state=balance only. Strategy behavior under BALANCE is
    strategy-owned. Trend/scalp permissions must not be encoded in core Map
    output, core Map lifecycle, or Map v2 producer logic.

  map_vs_strategy_v0_15:
    map_role:
      - identify_context
      - output_market_state
      - preserve_direction
    strategy_role:
      - decide_trade_permission
      - decide_if_balance_allows_entries
      - decide_trend_vs_scalp_behavior
    invariant: |
      Map emits context and preserves direction. Strategies decide permission
      and behavior. BALANCE strategy examples are not core Map outputs.

  examples_allowed_as_non_contractual_guidance:
    trend_strategies: restricted_or_low_confidence
    scalp_strategies: allowed_if_declared

  implementation_rule: |
    DMB/TRM/MEM behavior under BALANCE belongs in separate strategy briefs.
    No Stage 1A text authorizes strategy implementation, strategy promotion,
    cartridge changes, or console branches shaped by one cartridge's BALANCE
    behavior.

  forbidden_core_map_outputs:
    - balance_trend_permission
    - balance_scalp_permission
    - balance_strategy_rank
    - balance_trade_direction
    - balance_entry_filter
    - balance_exit_filter
```

---

## 7. Producer detection deferral and halt gate

```yaml
producer_detection_deferral:
  status: NOT_FORMALIZED
  required_clause: |
    BALANCE detection is not formalized in v0.15. Failure to progress beyond a
    level may manifest as rejection, stalling, LTF shifts, or range formation.
    Stage 1A must not reduce these to a fixed deterministic pattern, candle
    count, attempt count, or threshold.

  do_not_formalize_now:
    - no_clean_progression_thresholds
    - between_htf_levels_failure_patterns
    - fixed_rejection_pattern
    - fixed_stalling_pattern
    - fixed_LTF_shift_pattern
    - fixed_range_formation_pattern
    - candle_count_thresholds
    - attempt_count_thresholds

  balance_failure_manifestation_plurality:
    canon: |
      BALANCE failure-to-progress may manifest through rejection, stalling, LTF
      shifts, or range formation. These are plural candidate signals by
      Olya/NEX v0.15 refinement.
    constraint: |
      Future producer detection must not collapse BALANCE to a single
      deterministic pattern. Any formalization must support the plurality of
      manifestations or route to Olya for example-based calibration.

  future_producer_rule: |
    Any future producer implementation requiring deterministic BALANCE
    detection logic must halt and route to Olya for chart examples and
    example-based calibration.

  methodology_halt_gate:
    route: G_to_Olya
    halt_if_future_work_needs:
      - deterministic_BALANCE_detection_algorithm
      - wick_close_body_balance_trigger
      - level_failure_pattern_selection
      - candle_count_or_attempt_count_threshold
      - LTF_shift_definition_for_BALANCE
      - range_formation_definition_for_BALANCE
      - clean_progression_threshold
```

---

## 8. Stage 1 / 2A / 2B / C2 impact assessment

```yaml
impact_assessment:
  stage_1_contract:
    impact: "market_state enum extension + coupling/invariant additions"
    no_rewrite: true
    amendment_mode: additive

  stage_2A:
    impact: "small future enum/type/test extension likely required"
    no_immediate_code: true
    note: "Stage 2A landed enum/types remain unmodified by this no-code brief."

  stage_2B:
    impact: "optional future construction fixture extension likely useful"
    no_immediate_artifact_update: true
    note: "Stage 2B pushed construction artifacts remain valid cold-start artifacts."

  C2_producer:
    impact: "producer brief must include BALANCE and halt-gate detection semantics"
    status: "blocked until Stage 1A ratified and Stage 2C enum/fixture extension considered"
    producer_detection_status: BLOCKED_FROM_FORMALIZING_BALANCE_DETECTION

  stage_2C_naming_convention: |
    Stage 2C refers to the future implementation slice that extends Stage 2A
    enum/types/tests and optionally Stage 2B fixture corpus to cover BALANCE.
    It requires a separate brief and ratification.

  v1_runtime:
    impact: none
    v1_certification_impact: none
    trade_011_impact: none

  certification:
    impact: "no v2 certification claim; future V2 certification must include BALANCE coverage"
    no_chart_truth_rebaseline_now: true
    no_walk_forward_claim_now: true
```

---

## 9. Forbidden scope

```yaml
forbidden_scope:
  - code_changes
  - schema_changes
  - cartridge_changes
  - runtime_changes
  - MapV2Engine_producer
  - deterministic_BALANCE_detection_algorithm
  - market_data_inference
  - candle_count_thresholds
  - attempt_count_thresholds
  - invented_failure_patterns
  - strategy_permission_logic_in_Map
  - DMB_TRM_MEM_implementation
  - DAILY_EXPANSION_v1_migration
  - DAILY_EXPANSION_v2_read_path
  - H4_authority
  - target_ranking
  - v2_certification_claim
  - chart_truth_rebaseline
  - walk_forward_claim
  - trade_011_repair
```

---

## 10. Ratification text for G

```yaml
recommended_ratification_text:
  text: |
    G ratifies HTF Map v0.15 BALANCE as a Map v2 contract amendment.
    BALANCE is added as a market_state value. It preserves known Daily
    direction, remains actionable, is not neutral, not reassessment, and not
    paused. Map outputs BALANCE as context only; strategies decide behavior.
    Deterministic BALANCE detection logic is not formalized in v0.15 and must
    not be invented. Future producer work requiring BALANCE detection must
    route to Olya for chart examples and calibration.

  if_ratified_status_target: G_RATIFIED_CONTRACT_AMENDMENT
  implementation_authorized_by_ratification: false
  methodology_touchpoint_required_now: false
```

---

## 11. Stage 1A exit criteria

```yaml
stage_1A_authoring_exit_criteria:
  deliverable:
    owner: CTO
    condition: "Balance contract amendment brief complete with v0.15 source pointer and additive contract delta."

  boundary_review:
    owners:
      - Claude_Chair
      - Chief_Architect_GPT
    condition: "No algorithm invention, strategy permission leakage, H4 leakage, certification overclaim, or implementation authorization."

  methodology_consistency:
    owner: G
    condition: "Olya/NEX v0.15 content preserved; producer detection deferral explicitly retained."

  ratification:
    owner: G
    condition: "G authorizes or rejects Stage 1A contract amendment."

  gate_to_next:
    rule: |
      If Stage 1A is ratified, next expected engineering step is a small Stage
      2C enum/fixture extension brief. Do not begin C2 producer work before
      Balance-state review and any necessary Stage 2C bridge are complete.
```

---

## 12. No-code close statement

```yaml
brief_authoring_only: true
implementation_authorized: false
runtime_behavior_changed: false
console_files_modified_by_this_brief: false
schema_files_modified_by_this_brief: false
cartridge_files_modified_by_this_brief: false
MapV2Engine_producer_implemented: false
deterministic_BALANCE_detection_algorithm_created: false
DMB_TRM_MEM_implemented: false
DAILY_EXPANSION_v1_migrated: false
DAILY_EXPANSION_v2_read_path_created: false
H4_authority_resurrected: false
target_ranking_added: false
v2_certification_claimed: false
chart_truth_rebaseline_done: false
walk_forward_claim_made: false
trade_011_repaired: false
```
