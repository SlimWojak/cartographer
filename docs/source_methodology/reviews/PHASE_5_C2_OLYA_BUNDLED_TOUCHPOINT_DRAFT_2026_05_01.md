# Phase 5 C2 — Olya Bundled Methodology Touchpoint Draft

```yaml
artifact_id: PHASE_5_C2_OLYA_BUNDLED_TOUCHPOINT_DRAFT_2026_05_01
classification: OLYA_QUESTION_PACKET_DRAFT | NO_CODE | NO_FIXTURE | NO_IMPLEMENTATION
status: LOCAL_DRAFT_FOR_G_CHAIR_GPT_REVIEW
owner: Fresh_Droid_CTO_GPT55
date: 2026-05-01
preferred_mode: written_async
fallback_mode: verbal_phone_plus_G_attested_record
max_questions: 5
runtime_effect: NONE
fixture_effect: NONE
implementation_effect: NONE
certification_effect: NONE
```

---

## context

```yaml
current_state:
  final_handover: docs/handovers/PHASE_5_DAY_2026_05_01_FINAL_EOD_HANDOVER.md
  final_handover_sha: b2106c6b44be8af3b06a9d6cf9974797cec00e09
  canon_operational_anchor: 16a93db2dca90b18034242a5ce3dc0c911077665
  map_v2_status: inert_surfaces_only_no_producer_no_runtime_no_certification
  trade_011: pending_Olya_laptop_review
  trade_013: held_for_separate_decision

fixtures_landed:
  BALANCE_positive_2024_08_15_to_2024_09_12:
    path: tests/fixtures/map_v2/stage_2D/eurusd_daily_2024_08_15_2024_09_12_balance_snapshot.yaml
    classification_surface: Olya_asserted_BALANCE_example_snapshot
  NOT_BALANCE_RETRACE_trade_014_2026_02_04:
    path: tests/fixtures/map_v2/stage_2D/eurusd_daily_2026_02_04_trade_014_retrace_not_balance_snapshot.yaml
    classification_surface: Olya_asserted_NOT_BALANCE_RETRACE_example_snapshot
```

---

## purpose

```yaml
summary: |
  Ask Olya a compact bundled set of methodology questions that can unlock the
  next Stage 2D / C2 decisions without inventing detector logic or implementation
  rules.

packet_style:
  tone: concise
  primary_delivery: written_async
  fallback_delivery: verbal_phone_plus_G_attested_record
```

---

## tier_1_must_answer

```yaml
questions:
  1_annotated_trade_taxonomy_bridge:
    balance_definition_anchor: >
      Using your current BALANCE definition — known Daily direction but
      unclear near-term delivery path — please confirm how to bridge the
      older annotated trade labels into the current Map v2 vocabulary.
    ask: |
      Should prior annotated trades labeled EXPANSION be treated as
      NOT_BALANCE unless you explicitly say otherwise?
      Should prior annotated trades labeled RETRACE be treated as
      NOT_BALANCE unless you explicitly say otherwise?
      Or do EXPANSION and RETRACE need different handling under the
      current BALANCE vocabulary?
    desired_answer: yes_no_caveat_by_label_class

  2_trade_011_review:
    ask: |
      Please review trade_011. Is it NOT_BALANCE, cannot_determine / Daily
      neutral, RANGE, or something else under current Map v2 vocabulary?
      If you need your chart/laptop for trade_011, please mark this deferred.
      Pending laptop review is acceptable.
    desired_answer: label_plus_short_reason

  3_balance_resolution_signal:
    ask: |
      When BALANCE resolves back into expansion, what signal do you require?
      For example, is it a valid Daily MSS/displacement back in direction,
      or something else?
    desired_answer: principle_plus_one_example_if_possible
```

---

## tier_2_if_bandwidth

```yaml
opening_note: |
  Skip Tier 2 if bandwidth is tight; Tier 1 alone is sufficient for current
  decisions. We will not invent an acceptance or strong-close-through proxy
  from a partial answer.

questions:
  4_acceptance_definition:
    ask: |
      When you say price accepts beyond a level, what minimum chart evidence
      do you mean?
    desired_answer: short_definition_or_defer

  5_strong_close_through:
    ask: |
      Is "strong close-through" a specific rule-like candle/sequence, or just
      emphasis for decisive displacement?
    desired_answer: short_definition_or_defer
```

---

## desired_answer_format

```yaml
format:
  - question_id
  - direct_answer
  - short_reason
  - optional_example_if_easy
  - defer_allowed_if_not_ready

preferred_reply_shape: |
  Compact bullets are enough. If a question needs chart/laptop review, mark it
  deferred rather than estimating.
```

---

## explicit_non_authorizations

```yaml
not_authorized:
  - no_detector_algorithm
  - no_thresholds
  - no_runtime_or_producer_work
  - no_schema_or_cartridge_change
  - no_fixture_authorization
  - no_trade_011_repair
  - no_v2_certification_or_paper_trading_claim
  - no_Q4_Q5_Q6_operationalization
  - no_acceptance_or_strong_close_through_proxy_invention
```

---

## validation_expectations

```yaml
validation:
  - docs_only_scope
  - no_runtime_claim
  - no_v2_certification_claim
  - no_fixture_or_implementation_authorization
  - no_detector_or_threshold_language
  - no_trade_011_resolution_claim
  - no_acceptance_or_strong_close_through_definition_claim
```

---

*PHASE_5_C2_OLYA_BUNDLED_TOUCHPOINT_DRAFT_2026_05_01 — Olya question packet draft only. No code, fixture, implementation, detector, threshold, runtime, producer, schema, cartridge, strategy, certification, paper-trading, trade_011 repair, Q4/Q5/Q6, acceptance proxy, or strong-close-through proxy is authorized.*
