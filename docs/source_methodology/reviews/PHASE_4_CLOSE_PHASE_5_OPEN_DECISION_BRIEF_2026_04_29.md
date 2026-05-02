# Phase 4 Close / Phase 5 Open Decision Brief

```yaml
brief_id: PHASE_4_CLOSE_PHASE_5_OPEN_DECISION_BRIEF_2026_04_29
classification: DOCS_ONLY | GOVERNANCE_PREP
status: G_RATIFIED_APPROVED_WITH_BOUNDARIES
behavior_change: none
runtime_changes: NONE
schema_changes: NONE
cartridge_changes: NONE
review_date: 2026-04-29
baseline_commit: fcd2221
next_decision_owner: G
ratified_by: G
ratification_date: 2026-04-29
ratified_decision: APPROVED_WITH_BOUNDARIES
phase_4_status: CLOSED_BY_G_RATIFICATION
phase_5_status: OPEN_NO_CODE_DESIGN_LANE
phase_5_candidate_thesis: HTF_Map_v2
methodology_input: docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md
methodology_version: "0.14"
design_brief: docs/reviews/HTF_MAP_v0_14_DESIGN_BRIEF_DRAFT_2026_04_29.md
stage_1_brief: docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md
hard_guardrail: "No implementation before separate G-ratified implementation mission under the frozen Map v2 contract."
forbidden:
  - console_code_changes
  - schema_changes
  - cartridge_changes
  - DMB_MEM_TRM_implementation
  - H4_authority_resurrection
  - automatic_target_ranking
  - strategy_performance_judgment
  - PnL_optimization
  - doctrine_folder_cleanup
  - retroactive_trade_011_repair
```

---

## 1. Ratified decision

G ratified Phase 4 closure and Phase 5 opening on 2026-04-29 with boundaries.

```yaml
ratification:
  decision: APPROVED_WITH_BOUNDARIES
  text: |
    G ratifies closure of Phase 4 at TRACE_CERTIFIED_DAILY_AUTHORITY_V1,
    scoped strictly to the current Daily-authority runtime. Phase 4 close
    acknowledges 11/12 chart-truth, with trade_011 named as a known v1
    doctrine-seed boundary deferred to Map v2 as design input, not
    retroactively repaired.

    G opens Phase 5 as a governed HTF Map v2 design lane using Olya/NEX
    HTF Map v0.14 as methodology input. Stage 1 is Map_v2_output_contract_freeze,
    classified as NO_CODE_DESIGN | CONTRACT_FREEZE.

    This ratification does not authorize console implementation, schema
    migration, cartridge changes, DMB/MEM/TRM promotion, H4 authority
    resurrection, target-ranking logic, strategy-performance claims, or
    unrelated doctrine-folder cleanup.
```

---

## 2. Phase 4 close basis

```yaml
phase_4_close_basis:
  trace_certification:
    level: TRACE_CERTIFIED_DAILY_AUTHORITY_V1
    evidence: docs/canonical/CERTIFICATION_STATE.md
    summary: |
      Daily-authority path is trace-certified for the current runtime scope:
      FALLBACK maps are refused, raw unknown near-misses are zero, and the
      five-plus-year walk-forward has deterministic diagnostics.

  runtime_reentry:
    status: COMPLETED
    evidence: reports/dry_run/post_4b_runtime_reentry_bf02197/
    summary: "Deterministic replay and dry-run evidence captured for reentry windows."

  governance_hygiene:
    completed:
      - cartridge_lifecycle_protocol_v0_2
      - DMB_TRM_draft_intake
      - DMB_expressibility_review
      - HTF_Map_v0_11_gap_analysis
      - HTF_Map_v0_13_no_code_design_brief
      - HTF_Map_v0_14_methodology_capture
      - HTF_Map_v0_14_no_code_design_brief

  methodology_residual_closure:
    status: COMPLETED
    evidence:
      - docs/reviews/HTF_MAP_v0_11_RESIDUAL_CLARIFICATIONS_2026_04_28.md
      - docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md
    summary: |
      All methodology residuals from the v0.11/v0.13 gap-analysis lane
      are closed in v0.14: direction vs actionability, continuation
      displacement after pullback, reassessment exit, origin swing identity
      for range start, available HTF target membership, H4 boundary, and
      PD-zone label-vs-permission ownership. Stage 1 contract design is
      unblocked from the methodology side.

  residual_known_gaps:
    - NEUTRAL_regime_absence remains a known doctrine gap in v1 scope.
    - H4 authority is not certified by v1 and must not be resurrected as core Map authority.
    - Map v2 is not implemented and is not certified.

  chart_truth_boundary:
    status: "11/12 GREEN; trade_011 BLOCKED_BY_METHODOLOGY_SEED"
    rule: |
      Phase 4 close does not claim 12/12 or 14/14 chart-truth. trade_011
      remains outside v1 certification pending Map v2 implementation, replay,
      and Olya/G review.
```

Phase 4 can close because the current system state is explicit: what is certified is named, what is not certified is named, and the next capability thesis is design-ready but not implemented.

---

## 3. Phase 5 methodology input

```yaml
phase_5_methodology_input:
  source: docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md
  version: "0.14"
  provenance: Olya/NEX_verified
  supersedes:
    - htf_map_spec_v0_13
    - htf_map_spec_v0_12
    - htf_map_spec_v0_11
  design_brief: docs/reviews/HTF_MAP_v0_14_DESIGN_BRIEF_DRAFT_2026_04_29.md
```

v0.14 is the recommended design input because it resolves the major methodology iteration points. The v0.14 resolutions fall into three groups: authority/actionability semantics, range/state lifecycle mechanics, and strategy-consumer boundaries.

- Authority/actionability:
  - Daily authority is explicit.
  - Direction persists until opposing Daily MSS.
  - Actionability is separate from direction.
  - H4 is strategy-specific only: not Map authority, not global alignment, not conflict state.
- Range/state lifecycle:
  - Range start is the origin swing extreme of the MSS/displacement leg with bullish/bearish definitions.
  - New Map range update waits for follow-through; strategy may act earlier if strategy rules allow.
  - Reassessment exit requires follow-through.
- Consumer boundaries:
  - PD gating is strategy-dependent while Map remains labels-only.
  - Dominant draw is narrative, not execution target.
  - Strategy selects execution target.

---

## 4. Certification boundary

```yaml
v1_certification:
  level: TRACE_CERTIFIED_DAILY_AUTHORITY_V1
  transfers_to_map_v2: false
  reason: |
    V1 certification validates the current Daily-authority runtime and its
    current trace surfaces. Map v2 changes the Map output contract, authority
    boundary, range lifecycle, target inventory, actionability state, and
    certification trace requirements.

map_v2_certification_status:
  status: NOT_CERTIFIED
  future_class: TRACE_CERTIFIED_DAILY_AUTHORITY_V2_PENDING
  requires:
    - output_contract_freeze
    - deterministic_replay_for_v2_fields
    - chart_truth_rebaseline
    - walk_forward_no_regression
    - explicit_cannot_determine_and_paused_reassessment_accounting
    - H4_not_core_map_authority_assertions
    - PD_labels_only_with_strategy_owned_gating_assertions
```

No Phase 4 evidence should be restated as proof of Map v2 behavior. Phase 4 evidence only supports the current runtime and the decision to proceed into design/governance for new capability work.

---

## 5. Map v2 is new capability work

```yaml
map_v2_work_classification:
  type: NEW_CAPABILITY_WORK
  not_a_refactor: true
  not_a_schema_only_patch: true
  not_a_cartridge_only_change: true
  behavior_change_expected_when_implemented: true

why_new_capability:
  - new_output_contract_direction_actionability_market_state_targets
  - Daily_only_authority_split_from_H4_strategy_overlays
  - origin_swing_range_start_and_current_extreme_lifecycle
  - follow_through_gated_range_update_and_reassessment_exit
  - bounded_external_internal_liquidity_inventory
  - dominant_draw_and_target_completion_lifecycle
```

Opening Phase 5 does not authorize implementation by itself. It authorizes controlled design progression starting with a contract freeze. Implementation requires a later, separate G-ratified mission under the frozen Stage 1 contract.

---

## 6. Recommended Phase 5 Stage 1

```yaml
stage_1:
  name: Map_v2_output_contract_freeze
  classification: NO_CODE_DESIGN | CONTRACT_FREEZE
  objective: |
    Freeze the Map v2 output contract, persistence surface, trace vocabulary,
    and consumer boundaries before runtime implementation begins.
  inputs:
    - docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md
    - docs/reviews/HTF_MAP_v0_14_DESIGN_BRIEF_DRAFT_2026_04_29.md
    - docs/reviews/HTF_MAP_v0_11_RESIDUAL_CLARIFICATIONS_2026_04_28.md
  input_note: |
    The residual clarifications artifact is a closed-question audit trail,
    not an open residual source.
  outputs_expected:
    - Map_v2_output_contract_spec
    - trace_field_contract
    - persistence_snapshot_contract
    - strategy_consumer_boundary_note
    - certification_plan_delta
  hard_gates:
    - no_code_contract_freeze_only
    - separate_G_ratification_required_before_implementation
    - Olya_methodology_authority_preserved
    - no_H4_core_map_authority
    - no_automatic_target_ranking
    - no_strategy_performance_claims
```

---

## 7. Guardrails for next Droid / CTO context

```yaml
hard_guardrails:
  no_implementation_before_contract_freeze_and_separate_G_mission: true
  no_console_code: true
  no_schema_changes: true
  no_cartridge_changes: true
  no_DMB_MEM_TRM_implementation: true
  no_H4_authority_resurrection: true
  no_automatic_target_ranking: true
  no_strategy_performance_judgment: true
  no_doctrine_folder_cleanup: true
  no_retroactive_trade_011_repair: true

recommended_next_artifacts:
  - docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md
  - Phase_5_certification_plan_delta_after_contract_freeze
```

---

## 8. Ratified recommendation

```yaml
recommendation: APPROVED_WITH_BOUNDARIES
rationale: |
  Phase 4 has reached a clean epistemic checkpoint. The current runtime is
  trace-certified within its stated Daily-authority v1 scope, methodology gaps
  are explicit, and v0.14 gives a sufficiently concrete Map v2 methodology input
  for no-code contract design. Phase 5 should open only as a governed design lane
  until G ratifies implementation. Methodology is now ahead of implementation:
  Olya's HTF Map v0.14 defines the platform contract more precisely than the
  current runtime can express, which is exactly the right condition for opening
  a governed Phase 5 design lane.
```

---

## 9. No-code close statement

```yaml
runtime_behavior_changed: false
console_files_modified: false
schema_files_modified: false
cartridge_files_modified: false
DMB_MEM_TRM_implemented: false
H4_authority_resurrected: false
automatic_target_ranking_added: false
strategy_performance_judgment: false
PnL_optimization_done: false
doctrine_folder_cleanup_done: false
trade_011_retroactively_repaired: false
```
