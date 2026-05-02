# HTF Map v0.14 Design Brief Draft

```yaml
brief_id: HTF_MAP_v0_14_DESIGN_BRIEF_DRAFT_2026_04_29
classification: NO_CODE_DESIGN | PHASE_5_DESIGN_BRIEF_DRAFT
scope: console_map_design
status: DRAFT_PENDING_G_RATIFICATION
behavior_change: none
runtime_changes: NONE
schema_changes: NONE
cartridge_changes: NONE
implementation_status: NOT_YET
review_date: 2026-04-29
baseline_commit: 84504e5
methodology_source: docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md
methodology_version: "0.14"
methodology_authority: Olya/NEX
supersedes_design_input: docs/reviews/HTF_MAP_v0_13_DESIGN_BRIEF_DRAFT_2026_04_28.md
supersedes_inputs:
  - htf_map_spec_v0_13
  - htf_map_spec_v0_12
  - htf_map_spec_v0_11
forbidden:
  - console_code_changes
  - schema_changes
  - cartridge_changes
  - DMB_MEM_TRM_implementation
  - H4_authority_resurrection
  - automatic_target_ranking
  - strategy_performance_judgment
```

---

## 1. Purpose

Translate Olya/NEX HTF Map v0.14 into a no-code Phase 5 design brief. This brief updates the v0.13 design draft for v0.14 methodology and remains design-only: no console code, no schema patch, no cartridge patch, and no strategy-performance judgment.

```yaml
design_readiness:
  conceptual_spec: READY
  machine_spec: READY_ENOUGH
  implementation: NOT_YET

main_architectural_implication: |
  HTF Map v2 should be a Daily-authority interpreted read model:
  direction + actionability + dealing range + current extreme + quadrant
  + HTF target inventory + dominant draw + target completion + proximity
  + market state.

v0_14_delta_summary:
  - "Range start is origin_swing_extreme_of_mss_displacement_leg."
  - "Bullish origin is the lowest swing low before displacement that caused structure break."
  - "Bearish origin is the highest swing high before displacement that caused structure break."
  - "New expansion leg waits for follow-through before Map range update."
  - "Strategy may act on displacement before Map confirms new extreme."
  - "PD gating is strategy-dependent; Map provides labels only."
  - "DMB preserves PD gating strategy-side; TRM does not require HTF PD gating."
  - "Reassessment exit requires follow-through."
```

---

## 2. Output contract

Map v2 emits an interpreted Daily-authority read model. The contract is context, not execution instruction.

```yaml
map_output_contract_v2:
  direction:
    values: [bullish, bearish]
    authority: Daily
    evidence_required:
      - daily_mss
      - daily_displacement
    persistence: remains_until_opposing_daily_mss

  actionability_state:
    values:
      - actionable
      - paused_reassessment
      - cannot_determine
    independent_from_direction: true

  dealing_range_high_low:
    measurement: wick_to_wick
    start: origin_swing_extreme_of_mss_displacement_leg
    end: displacement_extreme
    origin_swing_definition:
      bullish: lowest_swing_low_before_displacement_that_caused_structure_break
      bearish: highest_swing_high_before_displacement_that_caused_structure_break
      ignore_minor_candles_unless_they_define_true_extreme: true

  current_extreme:
    definition: latest_extreme_of_active_daily_leg
    updates_on: continuous_extension
    resets_on: new_expansion_leg_after_follow_through

  midpoint:
    formula: "(high + low) / 2"

  quadrant_location:
    labels:
      - lower_discount
      - upper_discount
      - lower_premium
      - upper_premium
    usage:
      - location_label_only
      - trade_permission_owned_by_strategy

  liquidity_and_targets:
    dominant_draw: one_narrative_objective
    available_htf_targets: bounded_external_target_list
    target_completion_status: wick_touch_based
    proximity_to_target: context_flag_only

  market_state:
    values:
      - expansion
      - pullback
      - approaching_target
      - reassessment
    source: daily_range_position_and_expansion_behavior
    reassessment_exit_requires_follow_through: true
    not_lower_timeframe_structure: true
```

---

## 3. Data model fields

These are design-level fields only. They are not a schema patch in this mission.

| Field group | Design fields | Required semantics |
|---|---|---|
| Direction evidence | `direction`, `direction_authority`, `daily_mss_ref`, `daily_displacement_ref`, `direction_established_at`, `opposing_daily_mss_ref` | Direction is Daily-only and cannot be established by H4/H1. |
| Actionability | `actionability_state`, `actionability_reason`, `actionability_updated_at` | Trade eligibility context is separate from directional context. |
| Dealing range | `range_high`, `range_low`, `range_start_ref`, `range_end_ref`, `origin_swing_ref`, `origin_swing_price`, `midpoint`, `range_status`, `range_created_at` | Start is the true origin swing extreme of the MSS/displacement leg, not arbitrary recent high/low. |
| Origin swing | `origin_swing_side`, `origin_swing_time`, `origin_swing_source_ref`, `ignore_minor_candle_flag` | Bullish uses lowest qualifying swing low; bearish uses highest qualifying swing high. |
| Current extreme | `current_extreme_price`, `current_extreme_time`, `current_extreme_source_ref`, `current_extreme_update_mode`, `follow_through_ref` | Continuous extension updates current extreme; new range update waits for follow-through. |
| Quadrants | `q1`, `midpoint`, `q3`, `current_quadrant`, optional `object_quadrant` | Labels only. Strategy owns any permission rule. |
| External liquidity | `external_liquidity[]` with `target_id`, `kind`, `timeframe`, `side`, `price`, `status`, `source_ref` | Only Daily/Weekly old highs/lows and PDH/PDL/PWH/PWL participate in primary draw. |
| Internal liquidity | `internal_liquidity[]` with `kind`, `timeframe`, `side`, `price`, `source_ref` | Context/sweep fuel only; never dominant draw. |
| Draw and targets | `dominant_draw`, `available_htf_targets[]`, `dominant_draw_completed` | Dominant draw is narrative. Strategy selects execution target. |
| Completion/proximity | `target_completion_status`, `completed_target_refs[]`, `proximity_to_target`, `range_progress_to_target` | Wick touch completes target; proximity is 75-100% of dealing range. |
| Market state | `market_state`, `market_state_reason`, `last_state_transition_ref`, `reassessment_exit_ref` | Reassessment exits only after follow-through-valid Daily events. |
| Construction integrity | `construction_mode`, `cannot_determine_reason`, `evidence_refs[]` | Unknown/cannot-determine remains explicit and must not become no-setup. |

---

## 4. Direction vs actionability split

```yaml
direction:
  meaning: persistent_daily_bias_context
  source: Daily_MSS_plus_Daily_displacement
  persists_until: opposing_Daily_MSS
  does_not_pause_on_target_completion: true

actionability_state:
  meaning: whether Map context is actionable for strategy consumption
  may_pause_while_direction_persists: true
  paused_reassessment_trigger: wick_touch_completion_of_active_draw
  cannot_determine_trigger: insufficient_required_daily_evidence

consumer_rule: |
  Strategies consume both fields. Direction answers "which way is the Daily map
  pointing?" Actionability answers "is it currently valid to act on that map?"
```

`paused_reassessment` must not be represented as `NEUTRAL`, an opposing direction, or a silent no-trade. It is a distinct actionability state with the prior Daily direction still visible.

---

## 5. Daily-only authority model

```yaml
authority_model:
  direction_authority: Daily
  required_evidence:
    - daily_mss_required
    - daily_displacement_required
  reset_event: opposing_daily_mss
  weekly_role: draw_and_targets_only
  h4_role: strategy_specific_only
  h1_role: narrative_confirmation_and_internal_liquidity_only

forbidden_authority_sources:
  - h4_global_direction_filter
  - h4_map_authority
  - h4_conflict_state
  - h1_trade_gating
  - session_liquidity_as_dominant_draw
```

Current Map v1/v1.1 behavior uses a Daily→H4 cascade and H4 structural ingestion. Phase 5 design must split those concerns before implementing v0.14 semantics.

---

## 6. H4 strategy-specific boundary

H4 can exist only as a strategy-specific confirmation or selection surface. It must not be part of core Map authority.

```yaml
h4_boundary:
  allowed:
    - strategy_specific_confirmation_if_declared_by_strategy
    - strategy_specific_pda_selection_if_declared_by_strategy
    - strategy_trace_context_for_that_strategy
  forbidden:
    - core_map_direction
    - global_alignment_filter
    - map_conflict_state
    - fallback_authority_when_daily_unclear
    - dominant_draw_or_available_htf_target_source
```

DMB/MEM H4 needs, if ratified later, belong in strategy-specific surfaces after Map v2 emits Daily context. H4 is not a reason to keep or resurrect core Map H4 authority.

---

## 7. Dealing range lifecycle

```yaml
dealing_range_lifecycle:
  initial_creation:
    trigger: Daily_MSS_plus_Daily_displacement
    start: origin_swing_extreme_of_mss_displacement_leg
    origin_swing_definition:
      bullish: lowest_swing_low_before_displacement_that_caused_structure_break
      bearish: highest_swing_high_before_displacement_that_caused_structure_break
      ignore_minor_candles_unless_they_define_true_extreme: true
    end: displacement_extreme
    measurement: wick_to_wick

  continuous_extension:
    trigger: same_direction_continuation_without_meaningful_pullback
    action: update_current_extreme_only
    creates_new_range: false

  meaningful_pullback:
    definition: at_least_one_quadrant_transition_from_current_extreme

  new_expansion_leg:
    map_level_rule:
      - meaningful_pullback
      - daily_displacement
      - follow_through_updates_current_extreme
    displacement_source: existing_daily_displacement_primitive
    requires_new_mss: false
    action: create_new_active_range_only_after_follow_through

  strategy_execution_note: |
    Strategy may act on displacement before new extreme is confirmed.
    Map range update waits for structural follow-through.

  bias_reset:
    trigger: opposing_Daily_MSS
    action: reset_direction_and_range_context

  no_time_based_reset: true
```

The implementation design must preserve evidence references for every lifecycle transition. Fallback full-range or H4-derived ranges must not masquerade as Daily v0.14 ranges.

---

## 8. Current extreme semantics

`current_extreme` is distinct from the range endpoint and from strategy entry permission.

| Condition | Range high/low | Current extreme | Strategy actionability note |
|---|---|---|---|
| Initial Daily expansion leg | Created from origin swing extreme to displacement extreme | Set to displacement extreme | Strategies consume the established Daily map. |
| Same-direction continuation without meaningful pullback | Unchanged | Updates to latest active-leg extreme | No new range. |
| Meaningful pullback then Daily displacement, before follow-through | Unchanged | Pending / not confirmed as new range extreme | Strategy may act before Map confirms new extreme if its strategy rules allow. |
| Follow-through updates current extreme | New range can be created | Resets to follow-through-confirmed extreme | Map updates range only after structural follow-through. |
| Opposing Daily MSS | Reset under new direction | Reset under new direction | Direction and range context reset. |

---

## 9. Quadrant location labels and PD gating

```yaml
quadrants:
  lower_discount: range_low_to_Q1
  upper_discount: Q1_to_midpoint
  lower_premium: midpoint_to_Q3
  upper_premium: Q3_to_range_high
map_role:
  - provide_location_labels_only
  - do_not_make_core_trade_permission_decisions
pd_gating:
  rule: strategy_dependent
  examples:
    DMB: requires_longs_discount_shorts_premium
    TRM: no_htf_pd_gating_required
```

Migration risk: current gate behavior treats premium/discount as a permission filter. v0.14 keeps Map labels-only but clarifies that trade permission can exist strategy-side. Therefore DMB can preserve PD gating in its strategy contract while TRM remains ungated by HTF PD zones.

---

## 10. External/internal liquidity model

```yaml
external_liquidity:
  purpose: primary_htf_liquidity_and_draw_candidates
  eligible_sources:
    - PDH
    - PDL
    - PWH
    - PWL
    - nearest_unswept_daily_swing_high_low_per_side
    - nearest_unswept_weekly_swing_high_low_per_side
  exclusions:
    - monthly_levels_v1
    - h4_targets
    - h1_targets
    - session_targets
    - arbitrary_visible_levels

internal_liquidity:
  purpose: intermediate_liquidity_sweep_fuel_context
  eligible_sources:
    - H1_equal_highs_lows
    - session_highs_lows
    - pre_lokz_range
    - pre_ny_range
  can_be_dominant_draw: false
```

External target inventory must be bounded. No automatic ranking beyond the v0.14 dominant-draw priority is allowed.

---

## 11. Dominant draw vs strategy execution target

```yaml
dominant_draw:
  count: one
  role: narrative_context
  selection_rule: highest_timeframe_relevant_objective
  priority:
    - weekly
    - daily
  distance_does_not_override_timeframe: true
  not_execution_target: true

strategy_execution_target:
  selected_by: strategy
  source: available_htf_targets
  map_does_not_force_selection: true
  map_does_not_auto_rank_targets: true
```

Map suggests a dominant draw; strategy chooses the execution target. This prevents Map from becoming a strategy-specific target selector.

---

## 12. Target completion lifecycle

```yaml
target_completion:
  achievement_rule: wick_touch_equals_target_achieved
  effects:
    - mark_target_completed
    - mark_active_draw_completed_if_target_is_active_draw
    - stop_trading_into_completed_level
    - keep_direction_persistent
    - set_actionability_state_to_paused_reassessment

completion_status_values_design:
  - resting
  - completed
  - completed_active_draw
```

Completed levels must remain visible as completed context. They must not be silently removed if their completion affects reassessment or future no-trade reasoning.

---

## 13. Reassessment entry and exit

```yaml
reassessment_entry:
  trigger: wick_touch_completion_of_active_draw
  direction_behavior: direction_persists
  actionability_behavior: paused_reassessment
  forbidden:
    - immediate_direction_flip
    - immediate_next_target_assumption

reassessment_exit:
  valid_events:
    - continuation_displacement_with_follow_through
    - meaningful_pullback_followed_by_displacement_with_follow_through
  displacement_source: existing_daily_displacement_primitive
  requires_new_mss: false
  forbidden:
    - h4_exit_from_core_map_reassessment
    - h1_exit_from_core_map_reassessment
    - automatic_direction_flip
```

Reassessment is not a neutral regime and not a fallback. It is an interpreted state in which direction remains known but actionability is paused until Daily expansion evidence refreshes context with follow-through.

---

## 14. Certification impact

```yaml
certification_impact:
  current_certification: TRACE_CERTIFIED_DAILY_AUTHORITY_V1
  v0_14_status: design_only_not_certified
  expected_future_certification_class: TRACE_CERTIFIED_DAILY_AUTHORITY_V2_PENDING
  behavior_change_now: none

future_certification_requirements:
  - deterministic_replay_for_v0_14_map_outputs
  - chart_truth_rebaseline_for_map_v2_fields
  - walk_forward_regression_against_no_fallback_trade_invariant
  - trace_rows_for_direction_actionability_market_state_target_completion
  - explicit_cannot_determine_and_paused_reassessment_accounting
  - H4_not_core_map_authority_assertions
  - PD_quadrant_label_only_assertions
  - follow_through_gated_range_update_assertions
```

Existing v1 certification remains evidence for the current runtime only. It must not be reworded to imply v0.14 / Map v2 behavior before implementation and replay evidence exist.

---

## 15. Migration risks

| Risk | Current surface | v0.14 conflict | Design handling |
|---|---|---|---|
| H4 cascade embedded in core Map | Loader requires `1D` + `4H`; Map computes H4 DR fallback and ingests H4 structural events. | v0.14 says H4 is strategy-specific only. | Split core Daily Map from strategy H4 overlays before claiming v0.14. |
| PD zone gates trades in core gate | Gate maps direction permission to premium/discount required location. | v0.14 says Map labels only, while strategy owns PD gating. | Move location permission into strategy-specific consumers; DMB may preserve PD gating, TRM does not. |
| Range origin ambiguity | Current design used `swing_that_created_daily_mss`. | v0.14 requires origin swing extreme of MSS/displacement leg with side-specific definitions. | Design origin-swing evidence refs before implementation. |
| Range update too early | v0.13 design allowed new expansion on meaningful pullback + displacement. | v0.14 requires follow-through before Map range update. | Add pending state/evidence for displacement-before-follow-through; strategy may act before Map confirms. |
| Narrow MapState output | Current state exposes regime, DR, active PDAs, resting-liquidity stub, construction mode. | v0.14 requires actionability, current_extreme, targets, completion, proximity, market_state. | Freeze output contract and persistence/replay changes before behavior work. |
| Liquidity wiring is detector-side, not Map-side | HTF/reference/session primitives exist; Map liquidity module is stubbed. | v0.14 needs bounded external/internal inventory. | Build target inventory from existing primitives only after output contract is fixed. |
| Day-state and market-state are distinct | Current DayState is PRE/POST expansion eligibility. | v0.14 market_state is interpreted Daily range behavior. | Do not overload DayState; design a separate Map state output. |
| Certification/report consumers assume v1 fields | Current chart-truth and discovery surfaces assert authority/construction fields. | v0.14 adds new state and removes H4 authority from core. | Plan rebaseline and new trace assertions. |

---

## 16. Staged implementation proposal — design level only

```yaml
stage_0_governance_decision:
  purpose: "Ratify Phase 4 -> Phase 5 transition and accept v0.14 as Map v2 design input."
  output: phase_5_design_authorization
  must_decide:
    - Map_v2_new_capability_work_authorized_or_not
    - no_implementation_before_G_ratification

stage_1_contract_design:
  purpose: "Freeze Map v2 output contract, persistence shape, and trace vocabulary."
  no_runtime_behavior_until_contract_reviewed: true

stage_2_authority_boundary_design:
  purpose: "Separate Daily-only core Map authority from strategy-specific H4/H1 overlays."
  required_decision: retire_or_sidecar_existing_h4_cascade

stage_3_dealing_range_and_state_design:
  purpose: "Specify origin swing, current_extreme, continuous extension, follow-through-gated new range, and reassessment transitions."
  source: htf_map_spec_v0_14

stage_4_liquidity_target_design:
  purpose: "Design bounded external/internal liquidity inventory, dominant draw, target completion, and proximity outputs."
  anti_goal: automatic_target_ranking

stage_5_migration_and_certification_plan:
  purpose: "Define parity guards, chart-truth rebaseline, deterministic replay checks, and no-regression gates."
  must_preserve:
    - no_fallback_trades
    - construction_mode_truthfulness
    - explicit_cannot_determine
    - no_strategy_performance_claims
```

---

## 17. No-code close statement

```yaml
runtime_behavior_changed: false
console_files_modified: false
schema_files_modified: false
cartridge_files_modified: false
DMB_MEM_TRM_implemented: false
H4_authority_resurrected: false
automatic_target_ranking_added: false
strategy_performance_judgment: false
```
