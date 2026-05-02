This is a draft packet for G/Chair/GPT review only. No Olya/NEX use has occurred.

# Phase 5 C2 — Olya-Facing Methodology Packet Draft

```yaml
artifact_id: PHASE_5_C2_OLYA_FACING_METHOD_PACKET_DRAFT_2026_04_30
classification: OLYA_FACING_PACKET_DRAFT | NO_CONTACT | NO_CODE
status: DRAFT_FOR_G_CHAIR_GPT_REVIEW
owner: Droid_CTO_GPT55
date: 2026-04-30
input_anchor:
  origin_main_sha: a59ee2e43c280be22a00c876d7ac4039bd75db0d
  source_artifacts:
    - docs/reviews/PHASE_5_C2_PRODUCER_PREFLIGHT_2026_04_30.md
    - docs/reviews/PHASE_5_C2_OLYA_ROUTING_PREPARATION_2026_04_30.md
audience_if_later_approved_by_G:
  - Olya
  - NEX
authorizations:
  Olya_contact_authorized: false
  methodology_answers_by_Droid_authorized: false
  code_authorized: false
  runtime_changes_authorized: false
  migration_authorized: false
  certification_claim_authorized: false
  paper_trading_claim_authorized: false
```

---

## packet_header_for_G_review

```yaml
purpose: |
  Draft a chart-language methodology packet that G may review with Chair and
  GPT before deciding whether to bring it to Olya/NEX.

priority_structure:
  priority_1_core_required:
    - Q1_BALANCE_detection_examples
    - Q2_HTF_levels_defining_BALANCE_context
    - Q3_liquidity_on_both_sides
    - Q7_unknown_vs_known_Daily_direction
  priority_2_appendix_helpful:
    - Q4_meaningful_pullback_recognition
    - Q5_new_expansion_leg_confirmation
    - Q6_re_engagement_after_target_touch

review_rule: |
  The question wording below should be reviewed for chart-language clarity and
  absence of internal system phrasing before any later use.

dispatch_mode_note: |
  This packet is structured for either face-to-face walkthrough or async reply.
  G chooses dispatch mode.
```

---

## short_message_to_Olya

Draft message for G review:

> Olya/NEX — we need chart-calibration help for a Daily context read. Please answer from charts and your own trading language. NEX may help organize the reply, but please do not translate the answers into our internal labels unless Olya confirms the phrasing.
>
> Where possible, please use chart windows, mark the relevant bars/zones/levels, show positive examples, and include near-miss examples that should be rejected. The goal is to capture how Olya sees the chart, what she would call it, and which features make the call valid.

---

## answer_format_request

For each answered item, please provide:

```yaml
preferred_answer_shape:
  - chart_window_or_date
  - timeframe_context
  - accepted_label_in_Olya_words
  - rejected_alternative_labels_if_relevant
  - marked_bars_zones_or_levels
  - Olya_phrasing_for_trigger_or_distinguishing_feature
  - what_makes_the_positive_example_valid
  - what_makes_the_near_miss_or_rejected_example_invalid
```

Plain language is preferred. If a question is not answerable without more chart examples, please say what examples are needed.

Example volume guide: per question, 2-4 positive examples and 1-2 near-miss controls is usually sufficient unless a feature genuinely needs more variety.

---

## priority_1_core_questions

These are the core questions needed before the first C2 design slice can be safely framed.

```yaml
priority_1_core:
  Q1_BALANCE_detection_examples:
    ask: |
      Please show chart examples you would label BALANCE because price fails to
      progress cleanly. For each, describe in your own words what kind of
      failure it is. Include variety where possible. Mark the bars or zones
      that make it BALANCE rather than other chart behaviours you would recognise.
    requested_examples:
      - positive_BALANCE_examples
      - near_miss_examples_that_are_not_BALANCE
      - Olya_words_for_the_failure_type

  Q2_HTF_levels_defining_BALANCE_context:
    ask: |
      On BALANCE examples, please mark the higher-timeframe levels that define
      the BALANCE context. If more than one level pair could apply, please mark
      the selected pair and the rejected alternatives.
    requested_examples:
      - selected_higher_timeframe_level_pair
      - rejected_alternative_level_pairs
      - explanation_in_Olya_words_for_why_the_selected_pair_controls_the_context

  Q3_liquidity_on_both_sides:
    ask: |
      Please show examples where liquidity is clearly present on both sides,
      plus control examples where one side is not sufficient yet. Please mark
      the chart features that make the difference without turning them into
      fixed candle-count, attempt-count, or numeric rules.
    requested_examples:
      - clear_both_sides_liquidity_examples
      - one_side_not_sufficient_examples
      - Olya_words_for_the_distinguishing_features

  Q7_unknown_vs_known_Daily_direction:
    ask: |
      Please show early Daily-chart sequences where direction is not yet
      confidently knowable, and mark the point where it becomes knowable. Use
      your own language for the unknown state and the chart features that end it.
    requested_examples:
      - direction_not_yet_confident_examples
      - direction_becomes_confident_examples
      - Olya_words_for_the_boundary_between_unknown_and_known_direction
```

---

## priority_2_appendix_questions

These are helpful second-priority questions for smoother range-lifecycle design. G may choose whether to include them with the core packet or hold them for later.

```yaml
priority_2_appendix:
  Q4_meaningful_pullback_recognition:
    ask: |
      Please show examples of meaningful pullbacks from the current move that
      you would recognise as a shift in what is happening. Mark the bar or zone
      that signals the shift and describe the trigger in your own terms: wick,
      close, body, or other.
    requested_examples:
      - meaningful_pullback_recognition_examples
      - pullback_examples_that_are_not_enough
      - Olya_words_for_the_trigger

  Q5_new_expansion_leg_confirmation:
    ask: |
      Please show Daily displacement examples that do and do not qualify as
      follow-through for a new expansion leg, and mark the chart point after
      which the new leg is confirmed. If not confirmed, explain why the prior
      extreme remains the relevant reference.
    requested_examples:
      - confirmed_new_expansion_leg_examples
      - displacement_without_confirmation_examples
      - Olya_words_for_the_confirming_feature

  Q6_re_engagement_after_target_touch:
    ask: |
      After price touches a target while the underlying direction is still
      valid, please show examples where you would re-engage and examples where
      you would stand aside. Mark the chart event that causes the difference.
      Use your own language for the waiting state.
    requested_examples:
      - re_engagement_after_target_touch_examples
      - stand_aside_after_target_touch_examples
      - Olya_words_for_the_waiting_or_re_engagement_trigger
```

---

## example_annotation_template

```yaml
example_template:
  question_id: Q__
  chart_window_or_date: ""
  timeframe_context: ""
  positive_or_near_miss: ""
  Olya_label: ""
  rejected_label_if_any: ""
  marked_bars_zones_or_levels: ""
  Olya_words_for_trigger_or_feature: ""
  why_this_example_is_valid_or_rejected: ""
```

---

## what_not_to_answer

```yaml
not_needed_from_Olya_or_NEX:
  - code_or_file_design
  - platform_or_storage_design
  - execution_or_broker_design
  - performance_claims
  - numeric_rules_unless_Olya_already_uses_them
  - translation_into_internal_labels_without_Olya_confirmation
```

---

## G_review_notes

```yaml
review_focus:
  - "Is the packet genuinely usable by Olya/NEX?"
  - "Are Q1-Q3 and Q7 clearly core?"
  - "Are Q4-Q6 clearly appendix/helpful?"
  - "Is every question phrased as chart review, not system design?"
  - "Does the packet avoid implying Olya/NEX has already received it?"
  - "Does the packet avoid broader internal vocabulary, not only the original forbidden-term list?"

open_G_choice:
  option_A_minimal:
    include: [Q1, Q2, Q3, Q7]
    reason: "Smallest core packet for first-slice methodology calibration."
  option_B_core_plus_appendix:
    include: [Q1, Q2, Q3, Q7, Q4, Q5, Q6]
    reason: "Broader packet that may reduce later range-lifecycle round trips."
```

---

## non_authorization_statement

```yaml
non_authorization: |
  This file is a draft for G/Chair/GPT review only. It does not authorize
  contacting Olya or NEX, creating methodology answers, writing any code,
  changing runtime/schema/cartridge surfaces, migrating strategies, making
  certification claims, making paper-trading claims, or repairing trade_011.

explicitly_forbidden:
  - Olya_contact
  - packet_use_without_G_approval
  - methodology_answers_by_Droid
  - producer_brief
  - producer_code
  - runtime_schema_cartridge_changes
  - strategy_migration
  - v2_certification_claim
  - paper_trading_claim
  - trade_011_repair
  - new_C2_substage_canon_labels
```

---

*PHASE_5_C2_OLYA_FACING_METHOD_PACKET_DRAFT_2026_04_30 — draft methodology packet for review only; no Olya/NEX contact and no implementation authorization.*
