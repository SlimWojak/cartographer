# HTF Map v0.11 Residual Clarifications

```yaml
review_id: HTF_MAP_v0_11_RESIDUAL_CLARIFICATIONS_2026_04_28
mission_id: POST_4B.H6.HTF_MAP_SPEC_v0_11_GAP_ANALYSIS
classification: READ_ONLY_METHODOLOGY_INTAKE | RESIDUAL_CLARIFICATION_NOTE
scope: console_map_methodology
behavior_change: none
baseline_commit: 063cb6a
review_date: 2026-04-28
authoritative_source: docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md
runtime_changes: NONE
schema_changes: NONE
cartridge_changes: NONE
```

---

## 1. Clarification priority summary

```yaml
blocking_before_implementation:
  - direction_persists_vs_reassessment_no_trade_bias_distinction
  - machine_definition_for_continuation_displacement_after_pullback
  - definition_of_new_structure_or_expansion_after_reassessment
  - exact_identity_of_swing_that_created_daily_mss
  - available_targets_membership_and_unswept_rules
  - h4_cascade_retirement_vs_strategy_sidecar_confirmation

non_blocking_for_gap_analysis: true
```

This note is not a request to implement. It packages residual methodology questions that should be resolved before v0.11 Map work begins.

---

## 2. Required residual: direction persists vs reassessment no-trade-bias

### Problem

v0.11 says direction persists until opposing Daily MSS, but target completion triggers reassessment with no immediate trade bias until new structure or expansion forms. That creates two separate concepts that the current implementation does not separate:

- **Directional context**: `bullish | bearish`, persistent after Daily MSS.
- **Actionability / trade bias**: whether strategies should treat the direction as eligible for new entries.

Current code couples direction, phase, premium/discount permission, and gate behavior more tightly than v0.11 implies.

### Clarification needed

```yaml
question_id: H6_C1_direction_vs_reassessment
question: |
  After the active draw is completed and Map enters reassessment, should Map continue
  outputting the prior Daily direction while also emitting market_state=reassessment,
  with strategies treating reassessment as no-trade-bias until a reset condition occurs?

candidate_machine_contract_to_confirm:
  direction:
    persists_until: opposing_daily_mss
    value_during_reassessment: previous_direction
  market_state:
    set_to: reassessment
    trigger: wick_touch_of_active_dominant_draw_target
  strategy_behavior:
    default: no_new_directional_trades_during_reassessment
    override_allowed: strategy_specific_only_if_explicitly_ratified

why_it_matters: |
  If reassessment erases direction, the system needs a neutral/unknown-state design.
  If reassessment preserves direction but blocks trade bias, Map needs separate fields
  for direction and actionability/market_state. v0.11 appears to support the second
  model, but machine behavior should be confirmed.
```

### Recommended wording for Olya/NEX

> When the dominant draw has been wick-touched, do we keep the prior Daily direction visible as context while `market_state=reassessment` blocks new directional trades, or does the direction itself become absent/neutral until new structure forms?

---

## 3. Required residual: machine definition for `continuation_displacement_after_pullback`

### Problem

v0.11 says the dealing range updates on `continuation_displacement_after_pullback`, but the spec does not yet define a machine-detectable trigger. Current code can supersede a dealing range, but live daily/H4 bar processors do not rebuild DR on a fresh continuation displacement after pullback.

### Clarification needed

```yaml
question_id: H6_C2_continuation_displacement_after_pullback
question: |
  What exact machine conditions qualify as continuation_displacement_after_pullback
  for range_update?

candidate_fields_to_define:
  authority_timeframe: Daily_only
  required_prior_state:
    - existing_daily_direction_active
    - active_dealing_range_exists
    - price_has_pulled_back_from_displacement_extreme
  pullback_definition_options:
    - touch_or_cross_midpoint
    - enter_correct_pd_zone
    - form_daily_pullback_swing
    - minimum_counter_move_percent_of_range
  continuation_displacement_definition_options:
    - detector_displacement_same_direction_after_pullback
    - close_beyond_previous_displacement_extreme
    - wick_beyond_previous_displacement_extreme
    - body_percent_or_atr_quality_threshold
  new_range_start_options:
    - pullback_swing_that_preceded_continuation_displacement
    - swing_that_created_continuation_mss
  new_range_end_options:
    - continuation_displacement_extreme
    - expansion_leg_extreme_until_meaningful_pullback

why_it_matters: |
  Without this definition, any implementation would choose an arbitrary pullback
  threshold or continuation trigger and risk inventing methodology. It also determines
  whether existing DealingRangeTracker supersession semantics are valid or need rewrite.
```

### Recommended wording for Olya/NEX

> For a same-direction Daily continuation after pullback, what exact pullback evidence must occur first, and what exact displacement evidence updates the dealing range? Should the new range start at the pullback swing, the MSS-creating swing, or another structural point?

---

## 4. Required residual: definition of new structure or expansion after reassessment

### Problem

v0.11 says reassessment ends only when new structure or expansion forms. Current Map has no target-completion or reassessment state, and therefore no exit rule.

### Clarification needed

```yaml
question_id: H6_C3_reassessment_exit
question: |
  What exact events exit market_state=reassessment after target completion?

candidate_exit_events_to_confirm:
  opposing_daily_mss:
    effect: reset_bias_and_new_direction
    likely_required: true
  same_direction_daily_mss_or_continuation_structure:
    effect: resume_prior_direction_with_new_range
    needs_definition: true
  same_direction_daily_displacement_after_pullback:
    effect: range_update_and_resume_expansion
    overlaps_with: H6_C2_continuation_displacement_after_pullback
  mere_intraday_h4_or_h1_structure:
    effect: should_not_exit_core_map_reassessment_under_v0_11
    rationale: h4_strategy_specific_only_and_h1_narrative_not_gating
  price_rejects_target_without_daily_structure:
    effect: unknown
    needs_olya_ruling: true

why_it_matters: |
  This determines whether Map can resume actionability without opposing MSS, and
  whether reassessment is a context flag only or a hard no-trade state for Map-gated
  strategies. It also prevents H4/H1 structure from silently becoming core Map authority.
```

### Recommended wording for Olya/NEX

> After target completion puts Map into reassessment, which Daily events end reassessment: opposing MSS only, same-direction continuation displacement after pullback, same-direction Daily MSS, or any new Daily expansion? Should H4/H1 structure ever exit reassessment in core Map?

---

## 5. Additional residuals surfaced by the gap analysis

| Residual | Why it matters | Suggested ask |
|---|---|---|
| Exact identity of `swing_that_created_daily_mss` | Current DR start is pullback-origin before displacement, not explicit MSS swing identity. | Is this the protected swing, broken swing, swing before displacement, or the swing whose break confirmed MSS? |
| `available_targets` membership | v0.11 lists PDH/PDL/PWH/PWL and unswept daily/weekly swings; external liquidity also mentions monthly levels if present. | For v1, should Map include monthly levels and HTF EQH/EQL, or only the explicit `map_outputs` list? |
| Structural old high/low qualification | Spec excludes intraday/arbitrary recent levels but does not give swing-strength thresholds. | What detector threshold or structural proof qualifies daily/weekly old highs/lows? |
| Active draw completion with intermediate targets | v0.11 allows lower-timeframe targets as intermediate but only external liquidity can be primary draw. | Does touching an intermediate target trigger reassessment, or only the dominant draw target? |
| H4 cascade retirement | Current certified Map relies on Daily→H4 cascade. v0.11 says H4 not used in Map. | Should existing H4 cascade be retired entirely from core Map, or preserved only as a separate strategy-specific confirmation surface? |
| PD zone label vs permission behavior | Current gate uses premium/discount as permission. v0.11 says label-only. | Should current Daily Expansion parity behavior be preserved in a strategy-specific gate while core Map becomes label-only? |

---

## 6. Proposed clarification packet

```yaml
packet_for_olya_nex:
  C1_direction_reassessment: |
    When target completion triggers reassessment, does Daily direction remain visible
    while strategy bias is suspended, or does direction become neutral/absent?

  C2_continuation_displacement_after_pullback: |
    What exact Daily pullback evidence and same-direction displacement evidence update
    the dealing range? What are the new range start and end anchors?

  C3_reassessment_exit: |
    What exact Daily event exits reassessment: opposing MSS, same-direction MSS,
    continuation displacement after pullback, or another structure/expansion event?

  C4_swing_that_created_daily_mss: |
    Which swing is the DR start: protected swing, broken swing, swing before displacement,
    or another MSS-related structural point?

  C5_available_targets: |
    For v0.11 v1, are available_targets limited to PDH/PDL/PWH/PWL plus unswept
    daily/weekly swings, or do monthly levels and HTF EQH/EQL participate?

  C6_h4_boundary: |
    Should the current Daily→H4 core Map cascade be retired from core Map and replaced
    only by strategy-specific H4 confirmation, with no H4 authority inside Map?
```

---

## 7. Read-only scope statement

```yaml
runtime_behavior_changed: false
console_files_modified: false
schema_files_modified: false
cartridge_files_modified: false
performance_or_profitability_claims: false
```
