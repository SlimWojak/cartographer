# Phase 5 C2 — Olya Methodology Reply Verbatim

```yaml
artifact_id: PHASE_5_OLYA_METHOD_REPLY_VERBATIM
classification: OLYA_METHOD_REPLY | VERBATIM_LOGIC | FORMATTING_CLEANUP_ONLY
status: RECEIVED_FROM_OLYA_CLEANED_FOR_ADVISOR_REVIEW
date: 2026-04-30
source_packet: docs/reviews/PHASE_5_C2_OLYA_FACING_METHOD_PACKET_DRAFT_2026_04_30.md
cleanup_scope: |
  Telegram paste normalized for markdown framing, YAML indentation, blank lines,
  and non-breaking spaces. Olya's methodology content and answer logic are not
  intentionally changed.
```

---

## Olya Reply

```yaml
htf_map_c2_olya_answers:
  version: "0.1"
  status: methodology_locked_by_olya
  scope: phase_5_c2_questions
  output_type: human_methodology_ruling
  note: >
    This answers the office questions semantically. It is not yet detector
    implementation logic or forensic fixture annotation.

  q1_balance_detection_examples:
    locked: true
    definition: >
      BALANCE means Daily direction is known, but price is not delivering
      cleanly. Price is stuck between Daily/Weekly HTF levels or PD arrays,
      with valid interest on both sides, so the next delivery path is unclear.
    not_definition:
      - not_unknown_direction
      - not_direction_flip
      - not_target_completed_reassessment
      - not_clean_pullback
      - not_clean_expansion
    core_principle: >
      BALANCE = known directional context + unclear near-term delivery path.
    positive_examples:
      - instrument: EURUSD
        timeframe: Daily
        window: "2026-04-06_to_2026-04-29"
        label: balance
        direction: bullish
        explanation: >
          Price had a bullish Daily leg. It pulled back into or near the
          midpoint area of that bullish leg and rejected with a bullish
          engulfing candle. After that, price did not continue cleanly into
          external buy-side liquidity above the 17 April high. Instead, it
          started ranging between the bullish leg midpoint below and a Daily
          bearish OB / opposing HTF PDA above.
        balance_zone: "around_2026-04-27_to_2026-04-28"
        why_balance: >
          Daily direction was still bullish, but delivery was no longer clean.
          Price was stuck between opposing HTF levels, with liquidity above
          the 17 April high and a Daily bullish FVG deeper in discount below
          around the 8 April candle.
        uncertainty_type: next_delivery_path_not_daily_direction

      - instrument: EURUSD
        timeframe: Daily
        window: "2024-08-15_to_2024-09-12"
        label: balance
        direction: bullish
        explanation: >
          Price had a Daily bullish leg and left a weak high above. It then
          pulled back into Daily discount and into a Daily bullish FVG. After
          rejecting from that discount area, price did not immediately continue
          cleanly toward the weak high. Instead, it became trapped between the
          discount bullish FVG below and the Daily bearish FVG / opposing PDA
          formed around 28 August above.
        why_balance: >
          Daily direction was still bullish, but price was no longer delivering
          cleanly. The market was stuck between opposing HTF PD arrays, with
          upside liquidity still available above the weak high and downside
          liquidity / discount rebalancing still available below.
        uncertainty_type: next_delivery_path_not_daily_direction

    near_miss_examples:
      clean_pullback:
        label: not_balance
        classification: pullback
        explanation: >
          If Daily direction is bullish and price moves cleanly away from the
          current high toward midpoint, discount, or a bullish PDA, this is
          PULLBACK, not BALANCE. Price is progressing cleanly back toward
          PD context.

      clean_expansion:
        label: not_balance
        classification: expansion
        explanation: >
          If Daily direction is bullish and price is delivering clearly from
          discount toward external buy-side liquidity, this is EXPANSION,
          not BALANCE.

      target_completed_pause:
        label: not_balance
        classification: reassessment
        explanation: >
          If price has already touched the active target, the map pauses for
          reassessment. This is REASSESSMENT, not BALANCE, because the active
          draw has completed.

  q2_balance_defining_levels:
    locked: true
    rule: >
      BALANCE should be defined between Daily and Weekly HTF map levels only.
    valid_balance_boundaries:
      daily:
        - daily_dealing_range_high
        - daily_dealing_range_low
        - daily_midpoint_or_eq
        - daily_quadrants_if_useful
        - daily_fvg
        - daily_ob
        - daily_opposing_pda
        - pdh
        - pdl
        - nearest_unswept_daily_swing_high
        - nearest_unswept_daily_swing_low

      weekly:
        - weekly_high
        - weekly_low
        - pwh
        - pwl
        - nearest_unswept_weekly_swing_high
        - nearest_unswept_weekly_swing_low
        - weekly_target_or_draw_area

    invalid_as_primary_balance_boundaries:
      - session_highs_lows
      - asia_range
      - pre_lokz_range
      - pre_ny_range
      - intraday_equal_highs_lows
      - arbitrary_visible_intraday_levels
    internal_liquidity_note: >
      Session levels and intraday liquidity can exist inside the balance area,
      but they do not define the HTF balance boundaries.
    core_principle: >
      BALANCE boundaries = Daily/Weekly HTF map levels only.

  q3_two_sided_liquidity_or_interest:
    locked: true
    rule: >
      BALANCE requires two-sided Daily/Weekly interest, not necessarily
      external liquidity on both sides.
    definition: >
      Price is between Daily/Weekly levels where there is a plausible draw,
      liquidity reason, or rebalancing reason both above and below current
      price.
    not_required:
      - perfect_equal_highs_and_lows_on_both_sides
      - external_liquidity_on_both_sides
      - symmetrical_liquidity
    valid_upside_interest:
      - pdh
      - pwh
      - unswept_daily_swing_high
      - unswept_weekly_swing_high
      - weak_high
      - daily_bearish_pda_above
      - unfinished_upside_draw_or_target
    valid_downside_interest:
      - pdl
      - pwl
      - unswept_daily_swing_low
      - unswept_weekly_swing_low
      - weak_low
      - daily_bullish_pda_below
      - discount_fvg
      - discount_ob
      - midpoint_or_eq_area_below
    example_rule: >
      In bullish Daily direction, upside may have weak high / buy-side liquidity
      while downside may have a Daily bullish FVG in discount. If price is stuck
      between them, this can be BALANCE.
    core_principle: >
      BALANCE requires two-sided Daily/Weekly interest, not necessarily
      two-sided external liquidity.

  q4_meaningful_pullback:
    locked: true
    definition: >
      A meaningful pullback is not just any candle against the active Daily leg.
      It requires both distance and context.
    requirements:
      distance:
        rule: >
          Price must move materially away from the current Daily extreme.
        mechanical_proxy: one_quadrant_transition_away_from_current_extreme
        excludes:
          - shallow_pause_near_extreme
          - minor_candle_against_leg
          - sideways_noise_without_location_change

      context:
        rule: >
          Price must trade into a meaningful Daily/Weekly reference area.
        valid_references:
          - midpoint_or_eq
          - quadrant_boundary
          - daily_fvg
          - daily_ob
          - daily_or_weekly_pda
          - daily_or_weekly_liquidity_level
          - relevant_discount_or_premium_area

    midpoint_requirement:
      required: false
      note: >
        Midpoint is not mandatory, but the pullback must be into something
        meaningful. It cannot be just movement into empty space.
    bullish_example: >
      In a bullish Daily regime, price pulls back materially away from the
      current high and trades into Daily/Weekly context such as midpoint,
      discount, bullish FVG, OB, quadrant boundary, or relevant liquidity.
    bearish_example: >
      In a bearish Daily regime, price pulls back materially away from the
      current low and trades into Daily/Weekly context such as midpoint,
      premium, bearish FVG, OB, quadrant boundary, or relevant liquidity.
    core_principle: >
      Meaningful pullback = distance + Daily/Weekly context.

  q5_new_expansion_leg:
    locked: true
    definition: >
      A new expansion leg is not always a brand-new Daily directional regime.
      It can be a new same-direction shift after a temporary counter-direction
      pullback inside the existing Daily regime.
    regime_vs_orderflow:
      daily_directional_regime:
        definition: >
          The bigger Daily map direction established by valid Daily
          MSS/displacement.
        persistence: >
          Persists until opposing Daily MSS/displacement flips the regime.

      temporary_daily_orderflow:
        definition: >
          The counter-direction order flow that can form during a meaningful
          pullback inside the existing Daily regime.
        note: >
          Temporary counter-direction order flow does not automatically flip
          the whole map direction.

    requirements:
      - existing_daily_directional_regime_remains_valid
      - meaningful_pullback_into_daily_or_weekly_context
      - temporary_counter_direction_daily_orderflow_is_broken
      - valid_same_direction_daily_mss_displacement_event
      - follow_through
    bullish_example: >
      Daily regime is bullish. Price makes a meaningful pullback into
      Daily/Weekly context and creates temporary bearish Daily order flow.
      A new bullish expansion leg begins when price breaks that temporary
      bearish pullback order flow with bullish Daily MSS/displacement and
      follow-through.
    bearish_example: >
      Daily regime is bearish. Price makes a meaningful pullback into
      Daily/Weekly context and creates temporary bullish Daily order flow.
      A new bearish expansion leg begins when price breaks that temporary
      bullish pullback order flow with bearish Daily MSS/displacement and
      follow-through.
    implementation_note: >
      If the system codes MSS together with displacement, the same existing
      MSS/displacement primitive can be used. The important distinction is
      whether the event is flipping the whole Daily regime or restarting
      expansion inside an already-valid regime.
    core_principle: >
      Regime does not need to reset. Pullback order flow does need to be
      overcome.

  q6_reengagement_after_target_touch:
    locked: true
    definition: >
      After the active target is touched, Daily direction persists but
      actionability pauses into reassessment.
    target_touch_effects:
      - active_draw_completed
      - direction_persists
      - actionability_pauses
      - reassessment_state_active
      - no_automatic_jump_to_next_target
    weekly_role:
      allowed: true
      role: next_objective_context
      rule: >
        Weekly can help identify whether another larger HTF objective remains
        open, but Weekly does not create actionability by itself.
      principle: >
        Weekly = next objective context. Daily = re-engagement evidence.
    valid_reengagement_paths:
      continuation_path:
        requirements:
          - target_touched
          - no_opposing_daily_regime_flip
          - fresh_same_direction_daily_mss_displacement
          - follow_through
        explanation: >
          Price touches the active target, pauses, then gives fresh
          same-direction Daily MSS/displacement with follow-through.

      pullback_path:
        requirements:
          - target_touched
          - meaningful_pullback_into_daily_or_weekly_context
          - temporary_counter_direction_daily_orderflow_forms
          - same_direction_daily_mss_displacement_breaks_pullback_orderflow
          - follow_through
        explanation: >
          Price touches the active target, pulls back meaningfully, then
          re-engages when same-direction Daily MSS/displacement breaks the
          temporary pullback order flow with follow-through.

    consolidation_after_target_touch:
      rule: >
        Consolidation after target touch does not re-engage actionability
        by itself. It remains reassessment until resolved.
      cases:
        target_touch_then_consolidation:
          classification: reassessment
        target_touch_then_consolidation_then_same_direction_displacement:
          classification: reengagement
          requires: follow_through
        target_touch_then_consolidation_then_opposing_daily_mss_displacement:
          classification: possible_regime_flip
    core_principle: >
      After target touch, direction persists but actionability pauses.
      Re-engagement requires fresh Daily evidence: same-direction Daily
      MSS/displacement with follow-through, either directly or after a
      meaningful pullback. Weekly may identify the next larger objective,
      but it does not create actionability by itself.

  q7_unknown_vs_known_daily_direction:
    locked: true
    cannot_determine_definition: >
      Cannot_determine does not mean no context. It means Daily/Weekly context
      is unresolved, with competing directional scenarios, and no valid Daily
      MSS/displacement has confirmed one side yet.
    known_direction_definition: >
      Daily direction becomes known when a valid Daily MSS/displacement confirms
      a directional regime.
    unknown_context_sources:
      - price_inside_old_daily_or_weekly_range
      - price_reacting_from_daily_or_weekly_pda_without_confirmation
      - price_swept_liquidity_without_structure_shift
      - previous_target_or_draw_exhausted_without_fresh_daily_regime
      - price_between_major_htf_levels_without_confirmed_daily_mss_displacement
    not_enough_for_known_direction:
      - pda_reaction_alone
      - liquidity_sweep_alone
      - strong_candle_alone
      - lower_timeframe_shift_alone
      - price_moving_away_from_level_without_daily_mss_displacement
    balance_vs_cannot_determine:
      cannot_determine:
        meaning: directional_regime_not_confirmed_yet
        condition: before_valid_daily_mss_displacement_confirms_one_side
      balance:
        meaning: directional_regime_known_but_delivery_path_unclear
        condition: after_daily_direction_is_known
    core_principle: >
      Unknown direction is not random. It comes from unresolved Daily/Weekly
      context. The map can describe scenarios, but it should not output bullish
      or bearish direction until valid Daily MSS/displacement confirms one side.

  consolidated_principles:
    - balance_known_direction_unclear_delivery_path
    - balance_boundaries_daily_weekly_only
    - balance_requires_two_sided_daily_weekly_interest
    - meaningful_pullback_requires_distance_and_context
    - new_expansion_leg_breaks_temporary_pullback_orderflow_inside_existing_regime
    - target_touch_pauses_actionability_until_fresh_daily_evidence
    - weekly_can_contextualize_next_objective_but_not_create_actionability
    - cannot_determine_is_unresolved_context_before_confirmed_daily_regime
```
---

## Follow-Up Questions Sent To Olya

Olya/NEX — this is very helpful and resolves the semantic layer. I have four short precision follow-ups so we can avoid mis-encoding your answer later:

1. BALANCE activation timing
   In Q1, when does a clean pullback become BALANCE? Is it after price rejects a meaningful area and then fails to continue, after it shows interaction with both sides, after it starts ranging, or some other chart cue?

2. Selecting BALANCE boundaries
   In Q2, if several Daily/Weekly levels could define the BALANCE area, how do you choose the active upper/lower pair? Is it nearest meaningful opposing levels, strongest PD arrays, current active draw context, most recent interaction, or a discretionary hierarchy?

3. Meaningful pullback distance trigger
   In Q4, you mention one quadrant transition away from the current extreme as a mechanical proxy. Is that a hard minimum, or a useful approximation? Also, does the transition require wick, close, body, or is that context-dependent?

4. Follow-through
   In Q5/Q6, re-engagement and a new expansion leg require Daily MSS/displacement plus follow-through. What counts as follow-through in your chart language? Is it a Daily close, next candle continuation, displacement body, break-and-hold, failure to immediately reject, or something else?

---

## Olya Follow-Up Response Verbatim

```yaml
olya_followup_response_verbatim:
  distance:
    default_machine_proxy: one_quadrant_transition_away_from_current_daily_extreme
    hard_law: false
    note: >
      One quadrant transition is a default machine proxy, not a sacred
      hard methodology law. A pullback may still qualify if it interacts
      with a meaningful Daily/Weekly area close to that threshold.

  context_required: true

  valid_context_references:
    - midpoint_or_eq
    - quadrant_boundary
    - daily_fvg
    - daily_ob
    - daily_or_weekly_pda
    - daily_or_weekly_liquidity_level
    - relevant_discount_or_premium_area

  interaction:
    wick_counts_as_interaction: true
    body_counts_as_interaction: true
    close_required_for_interaction: false
    explanation: >
      Strong bullish or bearish markets may only tap a meaningful area by
      wick before continuing. Therefore, wick or body touch counts as valid
      interaction with the Daily/Weekly area.

  invalidation:
    wick_alone_invalidates_level: false
    close_through_required: true
    additional_requirement: follow_through_or_acceptance_beyond_level
    explanation: >
      Close/body is mainly used for acceptance or invalidation, not for
      basic interaction. A Daily/Weekly level should only be considered
      invalidated after strong close-through with follow-through or
      acceptance beyond the level.

  clean_sentence: >
    Meaningful pullback requires distance plus Daily/Weekly context.
    One quadrant transition is the default machine proxy, but interaction
    with the relevant Daily/Weekly area can be by wick or body. Wick touch
    counts as interaction. Close/body is mainly used for acceptance or
    invalidation, and a level should only be considered invalidated after
    strong close-through with follow-through or acceptance beyond it.

  followup_q4_followthrough_correction:
    locked: true
    correction: >
      Remove follow-through as a required condition for new expansion leg
      activation or re-engagement.
    previous_incorrect_requirement:
      - daily_mss_displacement_plus_follow_through
    corrected_activation_event: >
      Valid Daily MSS/displacement back in the original Daily direction.
    applies_to:
      - new_expansion_leg
      - reengagement_after_target_touch
    new_expansion_leg_rule: >
      A new expansion leg activates when the existing Daily directional regime
      remains valid, price has pulled back or paused, and price gives valid
      Daily MSS/displacement back in the original Daily direction.
    reengagement_rule: >
      After target touch and reassessment, re-engagement activates when price
      gives fresh valid Daily MSS/displacement back in the original Daily
      direction.
    followthrough_role:
      required_gate: false
      allowed_as_quality_evidence: true
      allowed_as_management_evidence: true
      explanation: >
        Follow-through may be tracked later as quality, continuation, or
        management evidence, but it should not be required as an additional
        activation gate.
    clean_sentence: >
      I want to correct the earlier wording. I do not want separate
      follow-through to be required after Daily MSS/displacement. The valid
      Daily MSS/displacement back in the original direction is the activation
      event for new expansion / re-engagement. Follow-through can be tracked
      later as quality or management evidence, but it should not be required
      as an additional activation condition.

  consolidated_followup_principles:
    - balance_activates_on_known_direction_before_target_completion_with_messy_acceptance_between_daily_weekly_interests
    - reassessment_overrides_balance_after_active_target_touch
    - balance_boundaries_are_selected_inside_current_active_daily_dealing_range_or_leg
    - active_balance_box_uses_nearest_valid_daily_weekly_interest_above_and_below_price
    - meaningful_pullback_requires_distance_plus_daily_weekly_context
    - one_quadrant_transition_is_default_proxy_not_sacred_hard_law
    - wick_or_body_touch_counts_as_interaction
    - strong_close_through_plus_acceptance_required_for_level_invalidation
    - remove_followthrough_as_activation_gate
    - daily_mss_displacement_back_in_original_direction_is_activation_event
```
