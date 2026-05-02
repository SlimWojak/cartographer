This packet is approved by G for Olya review. No Olya/NEX use has occurred at commit time.

# Phase 5 C2 WP2 — Olya Strong Close-Through Example Routing Packet

```yaml
artifact_id: PHASE_5_C2_WP2_OLYA_STRONG_CLOSE_THROUGH_EXAMPLE_ROUTING_PACKET_2026_05_01
classification: OLYA_EXAMPLE_ROUTING_PACKET | DOCS_ONLY | NO_CODE | NO_SCHEMA | NO_PRODUCER | NO_RUNTIME | NO_FIXTURE
status: G_APPROVED_FOR_OLYA_REVIEW
owner: Fresh_Droid_CTO_GPT55
date: 2026-05-01
input_anchor:
  origin_main_sha: 5027da89cabad16ffde4164befbccd227da1663a
  source_artifacts:
    - docs/handovers/PHASE_5_DAY_2026_05_01_FINAL_EVENING_HANDOVER.md
    - docs/raw/OLYA_VERBATIM_PHASE_5_C2.md
    - docs/reviews/PHASE_5_C2_OLYA_BUNDLED_TOUCHPOINT_DIGEST_2026_05_01.md
    - docs/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_INSPECTION_BRIEF_2026_05_01.md
    - docs/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md
authorized_by:
  G_live_session_choice: "Proceed with Option A: Olya examples for Daily strong close-through"
  G_dispatch_shape_choice: "Use Essentials plus Optional Appendix; review both with Olya as appropriate"
authorizations:
  Olya_contact_authorized: true
  NEX_contact_authorized: false
  methodology_answers_by_Droid_authorized: false
  code_authorized: false
  primitive_design_authorized: false
  primitive_implementation_authorized: false
  schema_change_authorized: false
  producer_authorized: false
  runtime_authorized: false
  fixture_authorized: false
  certification_claim_authorized: false
  paper_trading_claim_authorized: false
```

---

## packet_header_for_G_review

```yaml
purpose: |
  Provide a targeted chart-example request that G may review with Olya.

target_decision_supported: |
  Resolve the WP2 tie-break: whether existing Daily candle-quality and level
  evidence can be composed into a future strong close-through surface, or
  whether Olya examples imply a separate Daily-only candle-quality primitive may
  be needed later.

wp2_disposition_preserved:
  final_recommendation: existing_surface_extension_needed
  new_primitive_decision: not_made
  methodology_examples_needed_for_tie_break: true

usage_rule: |
  Start with Essential Questions. Use the Optional Appendix if Olya has time or
  if the essential answers need decomposition around level/zone movement quality
  or wick controls.

dispatch_mode_note: |
  This packet is structured for G's in-person walkthrough with Olya. If NEX is
  included, G should explicitly confirm that separately.
```

---

## source_locked_methodology

```yaml
strong_close_through:
  source: docs/raw/OLYA_VERBATIM_PHASE_5_C2.md
  definition: "Daily candle closes beyond the level/zone with strong Daily candle quality"
  scope: Daily_only
  no_lower_timeframe_dependency: true
  daily_candle_quality_signs:
    - large_body_relative_to_recent_daily_candles
    - clear_movement_through_the_level_or_zone
    - close_is_not_barely_beyond_the_level_or_zone
    - no_dominant_rejection_wick_against_the_close

level_state_distinctions:
  closed_through: "Candle closed beyond the level/zone; event only"
  invalidated: "Level/zone no longer treated as valid support, resistance, PDA, or context; conclusion"
  key_rule: "Closed_through and invalidated are not automatically the same."

wp2_quality_sign_matrix:
  sign_1_large_body_relative_to_recent_daily_candles:
    coverage: partial_likely_addressable
    examples_needed_for: relative_window_and_sufficiency
  sign_2_clear_movement_through_the_level_or_zone:
    coverage: absent_as_general_level_relative_event
    examples_needed_for: level_or_zone_close_through_composition
  sign_3_close_is_not_barely_beyond_the_level_or_zone:
    coverage: absent_as_general_level_relative_strength_event
    examples_needed_for: non_numeric_barely_beyond_controls
  sign_4_no_dominant_rejection_wick_against_the_close:
    coverage: partial_methodology_uncertain
    examples_needed_for: rejection_wick_positive_and_control_cases
```

---

## short_message_to_Olya

Message for G review with Olya:

> Olya — we need targeted Daily chart examples for strong close-through through a Daily/Weekly level or zone.
>
> Please answer from charts and your own trading language.
>
> The specific question is not code design. We need examples that show when a Daily close beyond a level/zone is merely `closed_through`, and when it is strong enough that it may lead to `invalidated`.
>
> Please use Daily chart windows where possible, mark the relevant level/zone and Daily candle, include positive examples and near-miss controls, and describe the chart features that make the difference.

---

## answer_format_request

For each answered item, please provide:

```yaml
preferred_answer_shape:
  - chart_window_or_date
  - timeframe_context
  - level_or_zone_being_tested
  - positive_or_near_miss
  - Olya_label_or_plain_language_description
  - marked_daily_candle_or_sequence
  - marked_close_relative_to_level_or_zone
  - wick_body_or_range_features_that_matter
  - why_this_is_only_closed_through_or_may_lead_to_invalidated
  - what_similar_case_should_be_rejected
```

Plain language is preferred. If a question is not answerable without more chart examples, please say what examples are needed.

Example volume guide: 3-5 strong positive examples and 2-4 near-miss controls are enough unless the feature genuinely needs more variety.

---

## essential_questions

```yaml
Q1_strong_daily_close_through_positive_examples:
  ask: |
    Please show Daily examples where price closes beyond a Daily/Weekly level
    or zone and you would treat the close as strong or decisive, not merely a
    basic close-through. Mark the candle, the level/zone, and the body/wick
    features that matter.
  requested_examples:
    - strong_positive_examples_across_different_level_or_zone_types_if_available
    - Olya_words_for_what_makes_the_Daily_candle_strong
    - whether_formal_Daily_MSS_is_present_or_not_present_if_relevant
  tie_break_value: |
    Tests whether Daily candle quality can be recognized from chart examples
    without forcing a formal MSS/displacement requirement.

Q2_basic_closed_through_near_miss_controls:
  ask: |
    Please show examples where a Daily candle closes beyond a level/zone, but
    you would treat it as only a basic closed-through event rather than a strong
    close-through. Mark what makes it insufficient.
  requested_examples:
    - tiny_or_barely_beyond_close_examples
    - weak_body_or_unclear_movement_examples
    - examples_where_the_level_or_zone_should_not_be_called_invalidated_yet
  tie_break_value: |
    Separates closed_through as an event from invalidated as a conclusion
    without inventing numeric thresholds.

Q5_no_formal_mss_but_strong_daily_candle:
  ask: |
    Please show examples, if they exist, where no formal Daily MSS is present
    yet, but a Daily candle closing through a level/zone is still strong enough
    to matter for the HTF map. Also show controls where no formal MSS means the
    candle should not be enough.
  requested_examples:
    - strong_without_formal_Daily_MSS_examples_if_any
    - not_enough_without_formal_Daily_MSS_controls
    - Olya_words_for_why_the_candle_itself_is_or_is_not_enough
  tie_break_value: |
    Directly tests the WP2 primitive-gap question without asking Olya to design
    a code primitive or prefer a primitive name.

Q6_invalidated_conclusion_boundary:
  ask: |
    Please show examples where strong Daily close-through may lead to the
    level/zone being invalidated, and examples where it should remain only
    closed_through. Mark what additional chart behavior, if any, makes
    invalidated a valid conclusion in your methodology.
  requested_examples:
    - strong_close_through_that_may_lead_to_invalidated
    - closed_through_but_not_invalidated_controls
    - Olya_words_for_the_boundary_between_event_and_conclusion
  tie_break_value: |
    Preserves closed_through_event_vs_invalidated_conclusion separation.
```

---

## optional_appendix_questions

Use these if Olya has time or if the essential answers need more precision. They
are not prerequisites to begin the conversation.

```yaml
Q3_level_or_zone_movement_quality:
  ask: |
    Please show examples where the Daily candle clearly moves through the
    level/zone, and examples where it does not. Mark whether the relevant
    distinction is close position, body travel, wick behavior, where the candle
    opens/closes relative to the zone, or something else in your language.
  requested_examples:
    - clear_movement_through_level_or_zone_examples
    - unclear_or_barely_beyond_controls
    - Olya_words_for_the_distinguishing_chart_feature
  tie_break_value: |
    Targets WP2 quality signs 2 and 3 while avoiding threshold invention.

Q4_rejection_wick_controls:
  ask: |
    Please show examples where a Daily close beyond the level/zone is weakened
    or rejected because of the wick structure, plus examples where wick
    structure does not weaken the strong close-through. Mark the wick/body
    relationship that matters.
  requested_examples:
    - dominant_rejection_wick_against_the_close_controls
    - no_dominant_rejection_wick_positive_examples
    - Olya_words_for_when_wick_structure_changes_the_read
  tie_break_value: |
    Tests whether existing candle-quality examples are enough to represent
    Olya's no-dominant-rejection-wick sign.
```

---

## example_annotation_template

```yaml
example_template:
  question_id: Q__
  chart_window_or_date: ""
  timeframe_context: "Daily"
  level_or_zone: ""
  positive_or_near_miss: ""
  Olya_description: ""
  formal_Daily_MSS_present_if_relevant: ""
  marked_candle_or_sequence: ""
  close_relative_to_level_or_zone: ""
  body_wick_or_range_features: ""
  closed_through_or_may_lead_to_invalidated: ""
  why_this_example_is_valid_or_rejected: ""
```

---

## what_not_to_ask_or_answer

```yaml
not_needed_from_Olya_or_NEX:
  - code_or_file_design
  - primitive_names_or_class_design
  - detector_thresholds_first
  - lower_timeframe_confirmation
  - schema_or_output_contract_design
  - producer_runtime_or_storage_design
  - execution_or_broker_design
  - performance_or_certification_claims
  - translation_into_internal_labels_without_Olya_confirmation

packet_must_not_imply:
  - existing_surface_is_sufficient
  - new_primitive_is_required
  - daily_momentum_candle_is_preferred
  - daily_decisive_candle_is_preferred
  - strong_close_through_requires_LTF_confirmation
  - basic_closed_through_equals_invalidated
```

---

## G_review_notes

```yaml
review_focus:
  - "Is this narrow enough to decide the WP2 tie-break?"
  - "Are the questions chart-language first?"
  - "Does it avoid asking for thresholds before examples?"
  - "Does it avoid suggesting a primitive preference?"
  - "Does it preserve no-LTF dependency?"
  - "Does it preserve closed_through as event and invalidated as conclusion?"
  - "Does it avoid broad reopening of Map v2 methodology?"

open_G_choice_after_review:
  selected: essentials_plus_optional_appendix
  essential_questions: [Q1_strong_daily_close_through_positive_examples, Q2_basic_closed_through_near_miss_controls, Q5_no_formal_mss_but_strong_daily_candle, Q6_invalidated_conclusion_boundary]
  optional_appendix_questions: [Q3_level_or_zone_movement_quality, Q4_rejection_wick_controls]
  effect: G may review the essentials and optional appendix with Olya.
```

---

## non_authorization_statement

```yaml
non_authorization: |
  This file authorizes G to review this packet with Olya. It does not authorize
  NEX contact unless G separately chooses that, Droid-authored methodology
  answers, code, extending or implementing any primitive, changing
  runtime/schema/cartridge surfaces, creating fixtures, migrating strategies,
  making certification claims, making paper-trading claims, or
  repairing/canonicalizing trade_011.

explicitly_forbidden:
  - NEX_contact_without_G_approval
  - methodology_answers_by_Droid
  - producer_brief
  - producer_code
  - primitive_design_or_implementation
  - runtime_schema_cartridge_changes
  - fixture_creation
  - third_fixture
  - strategy_migration
  - v2_certification_claim
  - paper_trading_claim
  - trade_011_repair_or_canonicalization
  - threshold_invention
  - lower_timeframe_confirmation_logic
  - existing_surface_sufficient_claim
  - new_primitive_required_claim
```

---

## validation_expectations

```yaml
validation:
  - docs_only_scope
  - G_authorized_Olya_review_only
  - no_code_change
  - no_runtime_claim
  - no_schema_change_authorization
  - no_producer_runtime_authorization
  - no_fixture_or_third_fixture_authorization
  - no_v2_certification_claim
  - no_paper_trading_claim
  - no_trade_011_canonicalization_claim
  - no_primitive_implementation_claim
  - no_threshold_invention_claim
  - no_LTF_dependency_claim
  - preserves_closed_through_event_vs_invalidated_conclusion
  - preserves_WP2_new_primitive_decision_not_made
```

---

*PHASE_5_C2_WP2_OLYA_STRONG_CLOSE_THROUGH_EXAMPLE_ROUTING_PACKET_2026_05_01 — G-approved Olya example-routing packet. It asks for Daily chart examples to resolve the WP2 strong-close-through tie-break and authorizes no Droid-authored methodology answer, code, primitive design or implementation, schema, producer, runtime, fixture, certification, paper-trading, threshold, LTF confirmation, strategy migration, cartridge work, NEX contact without separate G approval, or trade_011 lane.*
