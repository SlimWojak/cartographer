# Phase 5 C2 — Map v2 Producer Design Scoping

```yaml
artifact_id: PHASE_5_C2_MAP_V2_PRODUCER_DESIGN_SCOPING_2026_05_01
classification: DESIGN_SCOPING | NO_CODE | NO_SCHEMA_CHANGE | NO_PRODUCER | NO_RUNTIME | NO_FIXTURE
status: DRAFT_FOR_G_CHAIR_GPT_REVIEW
owner: Fresh_Droid_CTO_GPT55
date: 2026-05-01
authorized_by:
  G_ratified_digest: 7ad7833948f1656bcaa75b4a3dcb83c65e3c5b85
implementation_authorized: false
schema_change_authorized: false
producer_authorized: false
runtime_authorized: false
fixture_authorized: false
certification_effect: NONE
```

---

## purpose_and_source_order

```yaml
purpose: |
  Answer Olya's engineering questions at architectural/design level only:
  where delivery_quality, level_state, execution_permission, and Daily
  candle-quality / strong-close-through primitives should live, and what future
  work would be required before implementation.

source_order:
  1: docs/raw/OLYA_VERBATIM_PHASE_5_C2.md
  2: docs/reviews/PHASE_5_C2_OLYA_BUNDLED_TOUCHPOINT_DIGEST_2026_05_01.md
  3: docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md
  4: docs/reviews/PHASE_5_STAGE_1A_BALANCE_MARKET_STATE_CONTRACT_AMENDMENT_BRIEF_DRAFT_2026_04_29.md
  5: docs/canonical/CARTRIDGE_CONTRACT.md
  6: CLAUDE.md
  7: docs/canonical/FORWARD_PLAN.md
  8: docs/canonical/CERTIFICATION_STATE.md
```

---

## executive_design_recommendations

```yaml
recommendations:
  delivery_quality:
    recommended_design_position: separate_field_alongside_market_state
    rationale: |
      Olya's source separates context/location from behaviour. Keeping
      market_state as the five-state context enum and adding delivery_quality as
      an adjacent descriptive dimension avoids adding consolidation as a sixth
      state and avoids overloading market_state.
    future_schema_implication: "Likely additive producer/read-model/trace field if separately approved later; no schema change now."
    no_implementation_now: true

  level_state:
    recommended_design_position: HTF_level_or_PDA_read_model_surface
    rationale: |
      Olya replaced acceptance language with observable level states. The owner
      surface should be the console Map's HTF level/PDA representation, not a
      strategy/cartridge declaration, because it describes interaction with
      Daily/Weekly levels before strategy-specific decisions.
    future_schema_implication: "Owner-surface decision and contract amendment likely needed later; no schema change now."
    no_implementation_now: true

  execution_permission:
    recommended_design_position: separate_from_HTF_direction
    rationale: |
      Direction is persistent Daily bias context. Execution permission is a
      later eligibility/permission surface. Olya's trade_011 language supports
      htf_direction=bullish while execution_permission=wait until a trigger.
    no_implementation_now: true

  strong_close_through:
    recommended_design_position: Daily_only_map_evidence_rule
    rationale: |
      Olya defined strong close-through as Daily candle evidence only, with no
      lower-timeframe dependency. It belongs in Map evidence/level-state logic
      if later implemented, but the primitive gap must be reviewed first.
    primitive_gap_handling: future_repo_inspection_required_before_any_machine_rule
    no_implementation_now: true
```

---

## Q1_delivery_quality_field

```yaml
question: |
  Is representing consolidation as delivery_quality rather than a sixth
  market_state clean enough for the engine?

answer:
  recommended_design_position: YES_DESIGN_SCOPE_ONLY
  rationale:
    - "Preserves Olya's five-state market_state enum."
    - "Keeps consolidation as behaviour inside pullback, balance, approaching_target, reassessment, or stalled expansion."
    - "Avoids state conflicts where consolidation could compete with market_state."
  future_schema_implication:
    dimensions_to_surface_in_WP1_contract_delta_brief:
      - market_state_5_value_enum_from_source
      - delivery_quality_3_value_enum_from_source
    affected_surfaces_to_review:
      - Map_v2_read_model
      - trace_output
      - snapshot_fixtures
      - producer_output_contract
    concrete_field_shape: deferred_to_WP1_contract_delta
    status: deferred_no_schema_change_now
  no_implementation_now: true
```

---

## Q2_trade_011_sequence_codability

```yaml
question: |
  Is trade_011 sequence design-scopable as pullback + consolidating ->
  4H MSS/displacement back bullish -> expansion?

answer:
  design_scopable: true
  caveat: provisional_only
  proposed_design_sequence_from_source:
    before_trigger:
      htf_direction: bullish
      market_state: pullback
      delivery_quality: consolidating
      execution_permission: wait
    trigger:
      event: 4H_MSS_displacement_back_bullish
      transition: pullback_to_expansion
    after_trigger:
      market_state: expansion
      execution_permission: allowed_if_strategy_conditions_met
  required_caveats:
    - trade_011_remains_provisional
    - no_fixture_or_canonical_repair_authorized
    - H4_role_must_remain_strategy_specific_not_core_Map_authority
    - future_design_must_distinguish_HTF_direction_from_execution_permission
```

---

## Q3_execution_permission_separation

```yaml
question: "Should execution_permission remain separate from HTF direction?"

answer:
  recommended_design_position: YES_SEPARATE
  relation_to_actionability_state: |
    Map v2 design input (v0.14; methodology and design input only, with no
    current runtime effect) proposes separation of HTF direction from
    actionability_state. This design recommendation aligns with that
    separation: direction remains persistent Daily context, while
    actionability/execution eligibility must not collapse into direction.
  relation_to_strategy_cartridge_permission: |
    Strategy/cartridge permission remains downstream. A cartridge may require
    additional confirmation such as strategy-specific H4 evidence, but core Map
    direction remains Daily-only.
  console_vs_cartridge_boundary:
    console_map_owns:
      - HTF direction context
      - market_state
      - actionability_state
      - evidence_refs
      - future_delivery_quality_if_separately_approved
      - future_level_state_if_separately_approved
    cartridge_or_strategy_gate_owns:
      - strategy_specific_entry_permission
      - H4_confirmation_requirement_if_ratified_for_strategy
      - trend_or_scalp_behavior_under_BALANCE
    forbidden_collapse:
      - "Do not encode Olya's pre-trigger neutral feeling as neutral HTF direction when Daily direction remains known."
      - "Do not make H4 a core Map direction authority."
```

---

## Q4_delivery_quality_placement

```yaml
question: "Should delivery_quality be a separate field alongside market_state?"

answer:
  recommended_design_position: YES_DESIGN_SCOPE_ONLY
  read_model_surface:
    placement: alongside_market_state
    owner: console_map_read_model
    semantics: behaviour_quality_inside_current_market_state
  trace_snapshot_implication:
    trace: delivery_quality_reason_or_evidence_ref_would_be_needed_later
    snapshot: inert_snapshots_would_need_optional_or_required_delivery_quality_once_contract_changes
  producer_output_implication:
    dimensions_to_surface_in_WP1_contract_delta_brief:
      - delivery_quality
      - delivery_quality_reason_or_evidence_linkage
    concrete_field_shape: deferred_to_WP1_contract_delta
    status: deferred_no_producer_or_schema_change_now
  schema_impact: deferred_no_schema_change_now
```

---

## Q5_level_state_and_strong_close_through

```yaml
question: |
  Where should level_state and Daily-only strong_close_through / possible
  daily_momentum_candle primitive fit?

answer:
  level_state_owner_surface:
    recommended_design_position: HTF_level_or_PDA_lifecycle_read_model
    owner: console_map
    reason: |
      level_state describes observable interaction with Daily/Weekly levels or
      zones. It is context/evidence for Map, not strategy-specific permission.
  strong_close_through_as_method_rule:
    recommended_design_position: Daily_only_map_evidence_rule
    source_locked_points:
      - Daily_candle_itself
      - no_lower_timeframe_dependency
      - strong_Daily_candle_quality_required
      - close_through_event_is_not_automatically_invalidation
  primitive_gap_classification:
    status: engineering_gap_to_investigate_later
    candidate_names_from_source:
      - daily_momentum_candle
      - daily_decisive_candle
    not_decided_here: true
  repo_inspection_needed_or_not:
    answer: needed_before_future_implementation
    reason: |
      A future mission must inspect current displacement/MSS and Daily candle
      evidence surfaces to decide whether existing primitives can express the
      rule or whether a new Daily-only candle-quality primitive is required.
  future_mission_boundary:
    - primitive_gap_analysis
    - contract_delta_if_needed
    - fixture_examples_if_G_authorizes
    - implementation_only_after_separate_G_authorization
```

---

## open_questions

```yaml
open_questions:
  - exact_field_names_for_delivery_quality_and_level_state
  - whether_delivery_quality_is_required_or_optional_in_early_Map_v2_outputs
  - whether_level_state_attaches_to_each_HTF_level_ref_or_only_active_levels
  - whether actionability_state needs an extension or whether strategy permission remains entirely downstream
  - whether existing Daily displacement primitives can satisfy strong Daily candle-quality evidence
  - what chart examples are required before any producer rule is written
```

---

## source_fidelity_to_ratified_digest

```yaml
ratified_digest: docs/reviews/PHASE_5_C2_OLYA_BUNDLED_TOUCHPOINT_DIGEST_2026_05_01.md @ 7ad7833
preserved_source_points:
  delivery_quality_values: "clean | consolidating | failed_delivery"
  level_state_values:
    - not_touched
    - touched
    - inside
    - above
    - below
    - closed_through
    - rejected
    - invalidated
  strong_daily_candle_quality_signs:
    - large_body_relative_to_recent_daily_candles
    - clear_movement_through_the_level_or_zone
    - close_is_not_barely_beyond_the_level_or_zone
    - no_dominant_rejection_wick_against_the_close
  follow_through_required: false
  transition_note: "valid MSS/displacement is the transition trigger; no separate follow-through activation gate"
```

---

## future_work_packages

```yaml
future_work_packages_if_separately_authorized:
  WP1_contract_delta_brief:
    scope: delivery_quality_and_level_state_contract_shape
    output: no_code_contract_delta
    frozen_contract_gate:
      rule: >
        HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF is frozen. Adding
        delivery_quality or level_state to producer/read-model output requires
        explicit G-ratified contract amendment, parallel to the Stage 1A
        BALANCE amendment path.
      status: future_gate_not_authorized_here
  WP2_primitive_gap_inspection:
    scope: current_MSS_displacement_Daily_candle_quality_surfaces
    output: gap_report_only
  WP3_trace_snapshot_design:
    scope: trace_and_snapshot_fields_for_delivery_quality_level_state
    output: fixture_contract_plan_only
  WP4_trade_011_ratification_lane:
    scope: provisional_trade_011_sequence_review
    output: G_and_Olya_ratified_classification_before_any_fixture
  WP5_producer_mission:
    scope: implementation_only_after_contract_and_gap_reviews
    output: separate_G_authorized_mission_required
```

---

## migration_risk_notes

```yaml
risks:
  market_state_overload:
    risk: "Encoding consolidation as market_state would violate Olya's five-state model."
    mitigation: "Use delivery_quality as separate dimension if later approved."
  actionability_direction_collapse:
    risk: "Treating wait/no-entry as unknown direction would recreate stale neutral/fallback ambiguity."
    mitigation: "Keep direction, actionability_state, and strategy permission separate."
  h4_authority_resurrection:
    risk: "trade_011 sequence could accidentally promote H4 into core Map authority."
    mitigation: "Keep H4 strategy-specific confirmation only."
  primitive_overreach:
    risk: "Daily momentum candle could be invented without source examples or code-surface review."
    mitigation: "Primitive gap analysis before any implementation brief."
  certification_drift:
    risk: "Design scoping could be mistaken as V2 evidence."
    mitigation: "Certification effect is NONE until future implementation/replay/review."
```

---

## certification_non_effect

```yaml
certification:
  current_level: TRACE_CERTIFIED_DAILY_AUTHORITY_V1
  v1_unchanged: true
  map_v2_certified: false
  digest_and_design_scoping_are_evidence_for_v2_certification: false
  future_v2_requires:
    - separate_G_authorized_implementation
    - deterministic_replay
    - chart_truth_review
    - walk_forward_evidence
    - explicit_G_ratification
```

---

## forbidden_implementation_boundary

```yaml
not_authorized:
  - no_code_changes
  - no_schema_changes
  - no_producer_implementation
  - no_runtime_read_path
  - no_fixture_work
  - no_trade_011_canonicalization_or_repair
  - no_v2_certification_claim
  - no_paper_trading_claim
  - no_daily_momentum_primitive_implementation
  - no_Q4_Q5_Q6_operationalization
  - no_strategy_migration
  - no_cartridge_change
```

---

## validation_expectations

```yaml
validation:
  - docs_only_scope
  - no_code_or_schema_change_authorization
  - no_producer_or_runtime_authorization
  - no_fixture_authorization
  - no_trade_011_canonicalization_claim
  - no_v2_certification_claim
  - no_paper_trading_claim
  - no_primitive_implementation_claim
  - no_strategy_or_cartridge_migration_claim
  - source_fidelity_to_ratified_digest
```

---

*PHASE_5_C2_MAP_V2_PRODUCER_DESIGN_SCOPING_2026_05_01 — design scoping only. It answers engineering placement questions at architecture level and authorizes no code, schema, producer, runtime, fixture, strategy, cartridge, certification, paper-trading, primitive implementation, or trade_011 canonicalization work.*
