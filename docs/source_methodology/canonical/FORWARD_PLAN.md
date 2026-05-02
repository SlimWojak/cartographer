# FORWARD PLAN

```yaml
document: FORWARD_PLAN
version: 3.5 (Phase 5 Day 2026-05-01 evening WP2 gap report ratified; no producer)
date: 2026-05-01
status: CANONICAL
owner: CTO (maintained), G (approval/ratification)
audience: CTO, Opus, COO, advisors, future agents
purpose: |
  Directs what happens next. Evidence state lives in CERTIFICATION_STATE;
  closed mission proof lives in ratification/review docs; parked ideas live
  in VAULT. This document must distinguish inert Map v2 surfaces from absent
  producer/runtime/certification. It now also records ratified C2 WP1/WP2
  artifacts without authorizing implementation.
```

---

## 1. Current State

```yaml
phase: PHASE_5_ACTIVE_DESIGN_LANE_LIVE_NO_PRODUCER
certification_level: TRACE_CERTIFIED_DAILY_AUTHORITY_V1
evidence_owner: docs/canonical/CERTIFICATION_STATE.md
phase_5_close_anchor: docs/handovers/PHASE_5_DAY_2026_05_01_FINAL_EVENING_HANDOVER.md
valid_as_of_origin_main_before_anchor_semantics_patch: 470c44c0e70b1cc5da41195c3a397b2c4c41f8ba
canon_content_refresh_sha: 20f06735fe5f3e8372940cd82e547c9a4ed121d5
canon_anchor_patch_sha: 470c44c0e70b1cc5da41195c3a397b2c4c41f8ba
olya_bundled_digest_ratified_sha: 7ad7833948f1656bcaa75b4a3dcb83c65e3c5b85
design_scoping_ratified_sha: 3d09e8b7ef2d6436bc2b47d9f5541105b6a6e5d3
wp1_contract_delta_preflight_ratified_sha: 6002d6f2576dde6e56521119dba381e2601f3701
wp2_primitive_gap_brief_ratified_sha: c9ff53eaa617ba900a61162e9d97017dd674bac1
wp2_gap_report_ratified_sha: ef185f8410f27460face0c3f9b45889bc786eadb
current_origin_main_rule: "Use git rev-parse origin/main; this plan does not self-anchor its own final patch SHA."

phase_4_certification_hygiene:
  status: CLOSED_BY_G_RATIFICATION
  trace_certification: TRACE_CERTIFIED_DAILY_AUTHORITY_V1
  evidence_ratification: docs/reviews/POST_4B_H1_DIAG_UNKNOWN_CHAIN_REASON_RATIFICATION_2026_04_28.md
  phase_close_decision: docs/reviews/PHASE_4_CLOSE_PHASE_5_OPEN_DECISION_BRIEF_2026_04_29.md
  phase_close_decision_status: G_RATIFIED_APPROVED_WITH_BOUNDARIES
  headline: "1,633 trading days; 88 trades; zero FALLBACK trades; raw unknown near-misses 0; known v1 MSS/actionability doctrine gap remains visible; Map v2 design addresses it but is not live runtime"

phase_5_candidate:
  thesis: HTF_MAP_V2
  methodology_input: docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md
  methodology_version: "0.14 + v0.15 BALANCE amendment"
  design_brief: docs/reviews/HTF_MAP_v0_14_DESIGN_BRIEF_DRAFT_2026_04_29.md
  decision_brief: docs/reviews/PHASE_4_CLOSE_PHASE_5_OPEN_DECISION_BRIEF_2026_04_29.md
  decision_status: G_RATIFIED_APPROVED_WITH_BOUNDARIES
  stage_1_brief: docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md
  stage_1_status: FROZEN_BY_G_APPROVAL
  stage_2A_status: INERT_READ_MODEL_TRACE_SNAPSHOT_SHELL_PUSHED
  stage_2B_status: CONSTRUCTION_REPLAY_HARNESS_PUSHED
  stage_1A_balance_status: BALANCE_MARKET_STATE_CONTRACT_AMENDMENT_RATIFIED_AND_PUSHED
  stage_2C_status: BALANCE_ENUM_TYPE_TEST_AND_FIXTURE_EXTENSION_PUSHED
  c2_preflight_status: PRODUCER_DESIGN_PREFLIGHT_PUSHED
  c2_methodology_status: OLYA_VERBATIM_ARCHIVED_AND_DIGEST_PUSHED
  c2_olya_bundled_digest_status: OLYA_BUNDLED_DIGEST_RATIFIED_AT_7ad7833
  c2_design_scoping_status: MAP_V2_PRODUCER_DESIGN_SCOPING_RATIFIED_AT_3d09e8b
  c2_wp1_contract_delta_preflight_status: RATIFIED_AT_6002d6f
  c2_wp2_primitive_gap_brief_status: RATIFIED_AT_c9ff53e
  c2_wp2_gap_report_status: RATIFIED_AT_ef185f8
  c2_brief_authorization_status: FIRST_PRODUCER_SLICE_BRIEF_BOUNDARY_RATIFIED_AND_PUSHED
  c2_execution_authorization_status: FIRST_SLICE_EXECUTION_BOUNDARY_RATIFIED_AND_PUSHED
  stage_2D_status: TWO_INERT_FIXTURES_LANDED_NO_PRODUCER
  stage_2D_first_fixture_status: FIRST_INERT_BALANCE_FIXTURE_LANDED_AT_8d67740
  stage_2D_second_fixture_status: SECOND_INERT_NOT_BALANCE_RETRACE_FIXTURE_LANDED_AT_6d4e5d6
  olya_verbal_confirmation_record: docs/reviews/PHASE_5_C2_OLYA_VERBAL_NOT_BALANCE_CONFIRMATION_2026_05_01.md @ ea1011d
  implementation_status: INERT_AND_DESIGN_ONLY__NO_PRODUCER_RUNTIME_OR_CONSUMER
  wp2_gap_report_disposition: existing_surface_extension_needed
  wp2_new_primitive_decision: not_made
  wp2_methodology_examples_needed_for_tie_break: true
  certification_status: NOT_CERTIFIED

certification_boundary:
  v1_transfers_to_map_v2: false
  note: |
    V1 certification proves the current runtime scope only. Map v2 changes the
    output contract, authority boundary, range lifecycle, target inventory,
    actionability state, and trace/certification requirements.

cartridge_lifecycle:
  protocol: docs/canonical/CARTRIDGE_LIFECYCLE_PROTOCOL.md
  status: "v0.2 remains in force."
  phase_5_note: |
    Phase 5 may surface Layer-B cartridge template/schema work later as Map v2
    consumer surfaces mature, but no protocol changes are made in this canon sync.

historical_detail_pointer_rule: |
  Closed mission details must leave a ratification doc pointer, review doc
  pointer, archive pointer, or finding ID pointer. No orphan deletion.
```

---

## 2. Immediate Next Actions

```yaml
priority_order:
  1_day_2026_05_01_final_evening_handover:
    action: "Use the 2026-05-01 final evening handover as the fresh-session bootstrap index, then follow owner docs."
    handover: docs/handovers/PHASE_5_DAY_2026_05_01_FINAL_EVENING_HANDOVER.md
    classification: DOCS_ONLY | STATE_ANCHOR
    status: CURRENT_HANDOFF_ANCHOR

  2_completed_inert_surfaces:
    action: "Preserve Stage 2A/2B/Stage 1A/Stage 2C and both Stage 2D fixtures as inert, non-runtime Map v2 surfaces."
    decision_brief: docs/reviews/PHASE_4_CLOSE_PHASE_5_OPEN_DECISION_BRIEF_2026_04_29.md
    stage_1_brief: docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md
    balance_amendment: docs/reviews/PHASE_5_STAGE_1A_BALANCE_MARKET_STATE_CONTRACT_AMENDMENT_BRIEF_DRAFT_2026_04_29.md
    balance_bridge: docs/reviews/PHASE_5_STAGE_2C_BALANCE_ENUM_AND_FIXTURE_EXTENSION_BRIEF_DRAFT_2026_04_29.md
    first_stage_2D_fixture: tests/fixtures/map_v2/stage_2D/eurusd_daily_2024_08_15_2024_09_12_balance_snapshot.yaml
    second_stage_2D_fixture: tests/fixtures/map_v2/stage_2D/eurusd_daily_2026_02_04_trade_014_retrace_not_balance_snapshot.yaml
    classification: INERT_REPRESENTATION_ONLY
    status: PUSHED_THROUGH_STAGE_2D_TWO_INERT_FIXTURES
    rule: "Inert surfaces do not authorize producer, runtime read path, runtime consumption, consumer mutation, schema migration, cartridge migration, strategy promotion, H4 authority, target ranking, v2 certification, paper-trading, or v1 trace retirement."

  3_c2_methodology_design_scoping_wp1_wp2_and_two_fixtures_landed:
    action: "Treat C2 methodology/design scope as locked for current source-capture, design-scoping, WP1 preflight, and WP2 gap-report scope via Olya sources, ratified bundled digest, ratified design scoping, ratified WP1/WP2 artifacts, and G-attested Olya NOT_BALANCE confirmation; preserve both Stage 2D fixtures as metadata-only."
    preflight: docs/reviews/PHASE_5_C2_PRODUCER_PREFLIGHT_2026_04_30.md
    verbatim: docs/reviews/PHASE_5_OLYA_METHOD_REPLY_VERBATIM.md
    digest: docs/reviews/PHASE_5_C2_OLYA_METHODOLOGY_DIGEST_2026_04_30.md
    not_balance_confirmation: docs/reviews/PHASE_5_C2_OLYA_VERBAL_NOT_BALANCE_CONFIRMATION_2026_05_01.md
    olya_bundled_digest: docs/reviews/PHASE_5_C2_OLYA_BUNDLED_TOUCHPOINT_DIGEST_2026_05_01.md @ 7ad7833
    design_scoping: docs/reviews/PHASE_5_C2_MAP_V2_PRODUCER_DESIGN_SCOPING_2026_05_01.md @ 3d09e8b
    wp1_contract_delta_preflight: docs/reviews/PHASE_5_C2_WP1_DELIVERY_QUALITY_LEVEL_STATE_CONTRACT_DELTA_PREFLIGHT_2026_05_01.md @ 6002d6f
    wp2_primitive_gap_brief: docs/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_INSPECTION_BRIEF_2026_05_01.md @ c9ff53e
    wp2_gap_report: docs/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md @ ef185f8
    authorization: docs/reviews/PHASE_5_C2_FIRST_PRODUCER_SLICE_BRIEF_AUTHORIZATION_2026_04_30.md
    execution_authorization: docs/reviews/PHASE_5_C2_FIRST_PRODUCER_SLICE_EXECUTION_AUTHORIZATION_2026_04_30.md
    stage_2D_packet: docs/reviews/PHASE_5_C2_STAGE_2D_SINGLE_FIXTURE_DROID_PACKET_DRAFT_2026_05_01.md
    trade_014_packet: docs/reviews/PHASE_5_C2_STAGE_2D_TRADE_014_NOT_BALANCE_FIXTURE_DROID_PACKET_DRAFT_2026_05_01.md
    stage_2D_first_fixture: tests/fixtures/map_v2/stage_2D/eurusd_daily_2024_08_15_2024_09_12_balance_snapshot.yaml
    stage_2D_second_fixture: tests/fixtures/map_v2/stage_2D/eurusd_daily_2026_02_04_trade_014_retrace_not_balance_snapshot.yaml
    status: METHODOLOGY_DIGEST_DESIGN_SCOPING_WP1_WP2_AND_TWO_INERT_FIXTURES_RATIFIED
    must_preserve:
      - "V1 certification does not transfer to Map v2."
      - "Map v2 producer/runtime/consumer remains not implemented and not certified."
      - "Stage 2D fixtures are inert metadata only and not runtime-consumed."
      - "delivery_quality and level_state are preflight-scoped only; future producer/read-model output change requires explicit G-ratified contract amendment parallel to Stage 1A BALANCE."
      - "execution_permission separation is design-scoped only; no implementation is authorized."
      - "Strong Daily close-through remains Daily-only map evidence; WP2 gap report disposition is existing_surface_extension_needed, new_primitive_decision=not_made, and methodology_examples_needed_for_tie_break=true."
      - "No existing_surface_sufficient claim, new_primitive_required claim, primitive implementation/extension, threshold invention, or lower-timeframe confirmation logic is authorized."
      - "trade_011 remains provisional and is not canonicalized."
      - "Q4/Q5/Q6 operationalization remains deferred unless separately authorized."
      - "No acceptance proxy, strong-close-through proxy, followthrough activation gate, or automatic target ranking is authorized."
      - "Future target is TRACE_CERTIFIED_DAILY_AUTHORITY_V2_PENDING only after producer/runtime implementation and replay if G opens that lane."

  4_next_gate:
    action: "Next natural decision is Olya example routing for Daily strong close-through or WP1 contract-amendment scoping; implementation remains unauthorized. trade_013 is held for separate decision; third fixture remains unauthorized."
    rule: "Do not start a third fixture, producer, runtime, schema, cartridge, strategy, certification, paper-trading, or trade_011 lane without separate G authorization."
    not_authorized:
      - MapV2Engine_producer
      - runtime_migration
      - schema_changes
      - cartridge_changes
      - strategy_migration
      - v2_certification_or_paper_trading_claims
      - trade_011_canonicalization
      - daily_momentum_or_daily_decisive_primitive_implementation_or_extension
      - threshold_invention
      - lower_timeframe_confirmation_logic
      - Q4_Q5_Q6_operationalization
```

---

## 3. Deferred / Blocked Work

```yaml
strategy_family_builds:
  DMB:
    status: DEFERRED
    reason: "Needs Map v2 design lane and strategy-specific H4/PD-gating boundary before implementation."
  MEM:
    status: WAITING_FOR_OLYA_DRAFT_v2
    reason: "Olya is reshaping MEM against v0.14 HTF Map spec; original MEM concept was superseded before delivery."
  TRM:
    status: SEPARATE_CANON_OR_SESSION_LANE_IF_PRIORITIZED
    reason: "Map-independent draft; not a driver for core HTF Map v2."

runtime_work:
  map_v2_inert_surfaces:
    status: LIVE_THROUGH_STAGE_2D_TWO_INERT_FIXTURES
    scope: "type shell, trace/snapshot shell, construction harness, BALANCE representation, first inert Olya-asserted BALANCE example snapshot, and trade_014 inert NOT_BALANCE/RETRACE adjacent-state snapshot"
  map_v2_producer_runtime:
    status: NOT_AUTHORIZED
    next_natural_step: "Olya example routing for Daily strong close-through or WP1 contract-amendment scoping if G chooses; no implementation/design gate or next Stage 2D candidate is authorized; trade_013 is held for separate decision"
  schema_changes:
    status: NOT_AUTHORIZED
  cartridge_changes:
    status: NOT_AUTHORIZED
  doctrine_folder_changes:
    status: SEPARATE_LANE_UNTOUCHED
    items:
      - docs/doctrine deletions
      - untracked docs/findings/doctrine/

legacy_deferred_design:
  SW52_semantic_detection_parity:
    status: DEFERRED
    reason: "reference and production surfaces are not plug-compatible"
  SW38_SW43_schema_v2_cluster:
    status: DESIGN_SESSION_GATED
    note: "May be revisited as part of Phase 5 contract/schema work after governance."
  SW44_typing_and_utility_debt:
    status: PARKED_OR_OPEN_IF_PRIORITIZED
```

---

## 4. Certification Gates

```yaml
TRACE_CERTIFIED_DAILY_AUTHORITY_V1:
  owner: docs/canonical/CERTIFICATION_STATE.md
  status: SATISFIED_AND_RATIFIED_FOR_CURRENT_RUNTIME_ONLY
  ratification: docs/reviews/POST_4B_H1_DIAG_UNKNOWN_CHAIN_REASON_RATIFICATION_2026_04_28.md
  not_in_scope:
    - "Map v2 output contract"
    - "v0.14 actionability state"
    - "v0.14 target inventory / dominant draw / target completion"
    - "H4 strategy-specific overlays"
    - "DMB/MEM/TRM implementation or promotion"

TRACE_CERTIFIED_DAILY_AUTHORITY_V2_PENDING:
  status: FUTURE_TARGET_AFTER_MAP_V2_IMPLEMENTATION
  requires:
    - "G ratifies Phase 5 implementation lane"
    - "Map v2 output contract frozen"
    - "implementation completed under contract"
    - "deterministic replay for v2 fields"
    - "chart-truth rebaseline"
    - "walk-forward no-regression and new-field evidence"
    - "explicit cannot_determine / paused_reassessment accounting"
    - "assertions that H4 is not core Map authority"
    - "assertions that PD/quadrants are Map labels and strategy owns gating"

FULLY_EPISTEMICALLY_CERTIFIED:
  owner: docs/canonical/CERTIFICATION_STATE.md
  phase: "Phase 5+ or later; not current state"
  requires:
    - "Map v2 runtime completed and V2-certified if G opens that lane"
    - "strategy-specific H4 overlays only if separately ratified by methodology/strategy briefs"
    - "expanded chart-truth beyond current 11/12 scope"
    - "Olya extreme confidence checkpoint"
```

---

## 5. Decision Discipline

```yaml
scope_effect_rule:
  owner: docs/canonical/CARTRIDGE_CONTRACT.md §7
  requirement: "Every brief, ruling, and change declares scope + effect."

phase_4_scope_rule:
  current_scope_status: "Closed by G ratification on 2026-04-29."
  decision: docs/reviews/PHASE_4_CLOSE_PHASE_5_OPEN_DECISION_BRIEF_2026_04_29.md
  closure_boundary: "TRACE_CERTIFIED_DAILY_AUTHORITY_V1 only; 11/12 chart-truth; trade_011 remains a v1 doctrine-seed boundary."

phase_5_guardrail:
  opened: "G-ratified no-code Map v2 design lane."
  current_stage: "Stage 2D two inert fixtures landed plus C2 design scoping, WP1 preflight, WP2 brief, and WP2 gap report ratified: BALANCE at 8d67740, trade_014 NOT_BALANCE/RETRACE at 6d4e5d6, Olya bundled digest at 7ad7833, design scoping at 3d09e8b, WP1 at 6002d6f, WP2 brief at c9ff53e, WP2 gap report at ef185f8; no producer."
  next_natural_step: "Olya example routing for Daily strong close-through or WP1 contract-amendment scoping if G chooses; trade_013 is held for separate decision and trade_011 remains provisional/not canonicalized."
  producer_requires: "separate G-ratified producer mission after future review."
  deny_until_then:
    - MapV2Engine_producer
    - runtime_read_path
    - schema_changes
    - cartridge_changes
    - DMB_MEM_TRM_implementation
    - H4_authority_resurrection
    - automatic_target_ranking
    - strategy_performance_judgment
    - doctrine_folder_cleanup
    - third_fixture_without_G_authorization
    - trade_011_canonicalization
    - daily_momentum_or_daily_decisive_primitive_implementation_or_extension
    - threshold_invention
    - lower_timeframe_confirmation_logic
    - Q4_Q5_Q6_operationalization

doc_hygiene_rule:
  subtract_point_stop: true
  no_new_mega_doc: true
  removed_closed_detail_must_leave_pointer:
    - "ratification doc pointer"
    - "review doc pointer"
    - "archive pointer"
    - "finding ID pointer"
```

---

## 6. Pointers

```yaml
evidence_state:
  - docs/canonical/CERTIFICATION_STATE.md

phase_5_close_anchor:
  - docs/handovers/PHASE_5_DAY_2026_05_01_FINAL_EVENING_HANDOVER.md
  - docs/canonical/PHASE_5_KICKOFF_CLOSE_2026_04_29.md

phase_decision:
  - docs/reviews/PHASE_4_CLOSE_PHASE_5_OPEN_DECISION_BRIEF_2026_04_29.md

stage_1_contract_freeze:
  - docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md

stage_2_inert_surfaces:
  - docs/reviews/PHASE_5_STAGE_2A_MAP_V2_READ_MODEL_TRACE_SHELL_BRIEF_DRAFT_2026_04_29.md
  - docs/reviews/PHASE_5_STAGE_2B_MAP_V2_CONSTRUCTION_REPLAY_HARNESS_BRIEF_DRAFT_2026_04_29.md
  - docs/reviews/PHASE_5_STAGE_1A_BALANCE_MARKET_STATE_CONTRACT_AMENDMENT_BRIEF_DRAFT_2026_04_29.md
  - docs/reviews/PHASE_5_STAGE_2C_BALANCE_ENUM_AND_FIXTURE_EXTENSION_BRIEF_DRAFT_2026_04_29.md
  - tests/fixtures/map_v2/stage_2D/eurusd_daily_2024_08_15_2024_09_12_balance_snapshot.yaml
  - tests/fixtures/map_v2/stage_2D/eurusd_daily_2026_02_04_trade_014_retrace_not_balance_snapshot.yaml

map_v2_design_inputs:
  - docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md
  - docs/reviews/HTF_MAP_v0_14_DESIGN_BRIEF_DRAFT_2026_04_29.md
  - docs/reviews/HTF_MAP_v0_11_RESIDUAL_CLARIFICATIONS_2026_04_28.md

c2_day_2026_04_30_chain:
  - docs/reviews/PHASE_5_C2_PRODUCER_PREFLIGHT_2026_04_30.md
  - docs/reviews/PHASE_5_C2_OLYA_ROUTING_PREPARATION_2026_04_30.md
  - docs/reviews/PHASE_5_C2_OLYA_FACING_METHOD_PACKET_DRAFT_2026_04_30.md
  - docs/reviews/PHASE_5_OLYA_METHOD_REPLY_VERBATIM.md
  - docs/reviews/PHASE_5_C2_OLYA_METHODOLOGY_DIGEST_2026_04_30.md
  - docs/reviews/PHASE_5_C2_FIRST_PRODUCER_SLICE_BRIEF_AUTHORIZATION_2026_04_30.md
  - docs/reviews/PHASE_5_C2_FIRST_PRODUCER_SLICE_BRIEF_DRAFT_2026_04_30.md
  - docs/reviews/PHASE_5_C2_FIRST_PRODUCER_SLICE_EXECUTION_AUTHORIZATION_2026_04_30.md

c2_day_2026_05_01_chain:
  - docs/reviews/PHASE_5_C2_STAGE_2D_SINGLE_FIXTURE_DROID_PACKET_DRAFT_2026_05_01.md
  - docs/raw/OLYA_VERBATIM_PHASE_5_C2.md
  - docs/reviews/PHASE_5_C2_OLYA_BUNDLED_TOUCHPOINT_DIGEST_2026_05_01.md
  - docs/reviews/PHASE_5_C2_MAP_V2_PRODUCER_DESIGN_SCOPING_2026_05_01.md
  - docs/reviews/PHASE_5_C2_WP1_DELIVERY_QUALITY_LEVEL_STATE_CONTRACT_DELTA_PREFLIGHT_2026_05_01.md
  - docs/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_INSPECTION_BRIEF_2026_05_01.md
  - docs/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md

closed_hardening_proof:
  - docs/reviews/POST_4B_H1_DIAG_UNKNOWN_CHAIN_REASON_RATIFICATION_2026_04_28.md

closed_lane_proof:
  - docs/reviews/PHASE_4B_LANE_CLOSE_RATIFICATION_2026_04_27.md

architecture_boundary:
  - docs/canonical/CARTRIDGE_CONTRACT.md
  - docs/canonical/CARTRIDGE_LIFECYCLE_PROTOCOL.md

parked_future:
  - docs/canonical/VAULT.md

snapshot_reference:
  - docs/archive/POST_PHASE_3_ORACLE.md
```

---

*FORWARD_PLAN v3.5 - live roadmap only. Evidence lives in CERTIFICATION_STATE. Closed details live in ratification/review docs. Parked ideas live in VAULT. Stage 2D fixtures, C2 design scoping, WP1, and WP2 are docs-only/inert; no producer/runtime/certification is live.*
