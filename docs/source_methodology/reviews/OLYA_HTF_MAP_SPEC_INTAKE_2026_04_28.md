## Olya HTF Map Spec v0.14 as authoritative spec
## Provenance: Olya/NEX updated as v0.14
## Supersedes: v0.13/v0.12/v0.11

htf_map_spec:
  version: "0.14"
  supersedes:
    - "0.13"
    - "0.12"
    - "0.11"
  status: Olya-methodology-input
  scope: console

  direction:
    authority: Daily
    rule:
      - daily_mss_required
      - daily_displacement_required
    persistence:
      - remains_until_opposing_daily_mss
    output:
      - bullish
      - bearish

  actionability_state:
    enum:
      - actionable
      - paused_reassessment
      - cannot_determine

  htf_layers:
    weekly:
      role:
        - draw_and_targets
      not_used_for_direction: true

    daily:
      role:
        - primary_direction
        - dealing_range
        - pd_zones
        - state
        - target_completion

    h4:
      role: strategy_specific_only
      not_map_authority: true
      not_global_alignment_filter: true
      not_used_to_create_conflict_state: true

    h1:
      role:
        - narrative_confirmation
        - internal_liquidity
      not_trade_gating: true

  dealing_range:
    definition:
      start: origin_swing_extreme_of_mss_displacement_leg
      end: displacement_extreme
    measurement: wick_to_wick

    origin_swing_definition:
      bullish: lowest_swing_low_before_displacement_that_caused_structure_break
      bearish: highest_swing_high_before_displacement_that_caused_structure_break
      ignore_minor_candles_unless_they_define_true_extreme: true

    current_extreme:
      definition: latest_extreme_of_active_daily_leg
      updates_on: continuous_extension
      resets_on: new_expansion_leg

    lifecycle:
      bias_reset:
        trigger: opposing_daily_mss

      continuous_extension:
        rule: same_direction_continuation_without_meaningful_pullback
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

      strategy_execution_note:
        rule: >
          Strategy may act on displacement before new extreme is confirmed.
          Map range update waits for structural follow-through.

      no_time_based_reset: true

  pd_zones:
    midpoint:
      formula: "(high + low) / 2"

    quadrants:
      formula: "(high - low) / 4"
      zones:
        lower_discount: range_low_to_Q1
        upper_discount: Q1_to_midpoint
        lower_premium: midpoint_to_Q3
        upper_premium: Q3_to_range_high

    usage:
      - location_label_only
      - trade_permission_owned_by_strategy

  liquidity:
    external_liquidity:
      includes:
        - PDH
        - PDL
        - PWH
        - PWL
        - nearest_unswept_daily_swing_high_low_per_side
        - nearest_unswept_weekly_swing_high_low_per_side

    internal_liquidity:
      includes:
        - H1_equal_highs_lows
        - session_highs_lows
        - pre_lokz_range
        - pre_ny_range

    rules:
      - only_external_liquidity_can_be_primary_draw
      - internal_liquidity_cannot_be_dominant_draw

  old_high_low_definition:
    rule:
      - derived_from_existing_swing_primitives
      - daily_and_weekly_only
      - must_be_unswept
      - keep_nearest_unswept_per_side_per_timeframe
    excludes:
      - intraday_swings
      - arbitrary_visible_levels
      - last_N_without_structure

  draw_on_liquidity:
    map_outputs:
      - dominant_draw
      - available_htf_targets

    dominant_draw:
      count: one
      selection_rule: highest_timeframe_relevant_objective
      priority:
        - weekly
        - daily
      notes:
        - distance_does_not_override_timeframe
        - dominant_draw_is_narrative_not_execution_target

    available_htf_targets:
      type: bounded_list
      includes:
        - PDH
        - PDL
        - PWH
        - PWL
        - nearest_unswept_daily_swings
        - nearest_unswept_weekly_swings
      excludes:
        - monthly_levels_v1
        - h4_targets
        - h1_targets
        - session_targets

    strategy_relationship:
      - map_suggests_dominant_draw
      - strategy_selects_execution_target

  target_completion:
    rule:
      - wick_touch_equals_target_achieved

    effects:
      - active_draw_completed
      - stop_trading_into_completed_level
      - direction_persists
      - actionability_state_becomes_paused_reassessment

  proximity:
    definition:
      near_target_zone: 75_to_100_percent_of_dealing_range
    usage:
      - context_flag_only
      - strategy_decides_behavior

  state:
    output_type: interpreted

    types:
      - expansion
      - pullback
      - approaching_target
      - reassessment

    definitions:
      expansion: movement_from_pd_context_toward_external_liquidity
      pullback: movement_from_range_extreme_back_toward_midpoint_or_pd_context
      approaching_target: price_inside_near_target_zone
      reassessment: after_target_touch_direction_persists_but_actionability_pauses

    reassessment_exit:
      valid_events:
        - continuation_displacement_with_follow_through
        - meaningful_pullback_followed_by_displacement_with_follow_through
      displacement_source: existing_daily_displacement_primitive
      requires_new_mss: false
      forbidden:
        - immediate_next_target_assumption
        - automatic_direction_flip

    rules:
      - state_determined_by_daily_range_position_and_expansion_behavior
      - not_lower_timeframe_structure

  pd_gating:
    rule: strategy_dependent
    map_role: provide_location_labels_only
    examples:
      DMB: requires_longs_discount_shorts_premium
      TRM: no_htf_pd_gating_required

  map_output:
    type: interpreted
    includes:
      - direction
      - actionability_state
      - dealing_range_high_low
      - current_extreme
      - midpoint
      - quadrant_location
      - dominant_draw
      - available_htf_targets
      - target_completion_status
      - proximity_to_target
      - market_state

  exclusions_v1:
    - ipda_20_day_range
    - monthly_levels
    - minor_swing_detection
    - ob_ifvg_logic
    - automatic_target_ranking
    - h4_global_direction_filter
    - session_liquidity_as_dominant_draw
