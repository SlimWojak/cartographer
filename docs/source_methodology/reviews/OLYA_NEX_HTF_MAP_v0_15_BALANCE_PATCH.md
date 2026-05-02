## This document captures Olya feedback requirted to add BALANCE as methodology on HTYF map per GPT brief, to create v0.15

htf_map_spec:
  version: "0.15"
  status: Olya-methodology-input
  scope: console

  actionability_state:
    enum:
      - actionable
      - paused_reassessment
      - cannot_determine

  market_state:
    enum:
      - expansion
      - pullback
      - approaching_target
      - reassessment
      - balance

  balance:
    definition: >
      Direction is known, but price is between opposing HTF levels,
      not progressing cleanly, and may seek liquidity on either side
      before the next expansion.

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

    strategy_relationship:
      map_outputs_balance_only: true
      strategy_decides_behavior: true
      examples:
        trend_strategies: restricted_or_low_confidence
        scalp_strategies: allowed_if_declared

    assignment:
      can_be_assigned_directly: true
      does_not_require_prior_expansion_or_pullback: true
      condition: >
        Daily direction is known, but current price is stuck between opposing
        HTF levels with no clean directional progression.

  state_definitions:
    expansion: movement_from_pd_context_toward_external_liquidity
    pullback: movement_from_range_extreme_back_toward_midpoint_or_pd_context
    approaching_target: price_inside_near_target_zone
    reassessment: after_target_touch_direction_persists_but_actionability_pauses
    balance: non_directional_execution_environment_inside_known_directional_context

  map_vs_strategy:
    map_role:
      - identify_context
      - output_market_state
      - preserve_direction
    strategy_role:
      - decide_trade_permission
      - decide_if_balance_allows_entries
      - decide_trend_vs_scalp_behavior

## Balance Detection Refinement

balance_detection_refinement:

  level_interaction:
    description: >
      BALANCE is often observed around HTF levels where price fails to
      progress cleanly, but failure patterns are not fixed at this stage.

  failure_definition:
    status: NOT_FORMALIZED

    rule: >
      Failure to progress beyond a level can manifest in multiple ways
      (rejection, stalling, LTF shifts, range formation). These are not
      reduced to a single deterministic pattern in v0.15.

  implementation_guidance:
    - do_not_invent_fixed_patterns
    - do_not_bind_to_candle_counts
    - do_not_bind_to_attempt_counts

  producer_phase:
    requirement: >
      Detection logic should be derived later from chart examples and
      validated behavior. If required, halt and return to Olya for
      example-based calibration.