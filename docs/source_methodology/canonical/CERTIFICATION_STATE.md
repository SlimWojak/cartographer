# CERTIFICATION STATE

```yaml
document: CERTIFICATION_STATE
version: 1.4
date: 2026-05-01
status: CANONICAL — LIVING DOCUMENT
version_note: "Stage 2D two inert fixtures, C2 design scoping, WP1, and WP2 gap report ratified; V1 certification unchanged; Map v2 remains not certified"
purpose: |
  Tracks the system's epistemic certification status. What has been
  validated, what gaps are known, what must be true before confidence
  upgrades. Orientates new agents on what walk-forward proved and
  what it did not prove.
owner: CTO (maintained), G (approved)
update_cadence: "After regime engine changes, walk-forward re-runs, diagnostic-ratification missions, or methodology seed resolutions"
rule: |
  This doc answers one question: "What has been validated and what hasn't?"
  Does not duplicate FORWARD_PLAN (what to build) or PHASE_4_RATIFICATION
  (why we build it). Tracks the EVIDENCE STATE.
```

---

## 1. Current status

```yaml
certification_level: TRACE_CERTIFIED_DAILY_AUTHORITY_V1
certification_scope: "DAILY authority only; known NEUTRAL/H4 doctrine gap remains open"
date_established: 2026-04-28
basis: |
  Walk-forward re-validation (5yr 3mo), Phase 4b lane-close
  (11/12 chart-truth), and POST_4B.H1 diagnostic hardening ratification.
chart_truth: "11/12 GREEN; trade_011 BLOCKED_BY_METHODOLOGY_SEED"
ratification: docs/reviews/POST_4B_H1_DIAG_UNKNOWN_CHAIN_REASON_RATIFICATION_2026_04_28.md

stage_2D_inert_fixture_notes:
  status: TWO_INERT_FIXTURES_LANDED
  first_fixture:
    status: LANDED_AND_RATIFIED_AT_8d67740
    path: tests/fixtures/map_v2/stage_2D/eurusd_daily_2024_08_15_2024_09_12_balance_snapshot.yaml
    classification_surface: Olya_asserted_BALANCE_example_snapshot
    source_window: EURUSD_Daily_2024-08-15_to_2024-09-12
  second_fixture:
    status: LANDED_AND_RATIFIED_AT_6d4e5d6
    path: tests/fixtures/map_v2/stage_2D/eurusd_daily_2026_02_04_trade_014_retrace_not_balance_snapshot.yaml
    classification_surface: Olya_asserted_NOT_BALANCE_RETRACE_example_snapshot
    source_window: EURUSD_Daily_2026-02-04
    source_bridge: docs/reviews/PHASE_5_C2_OLYA_VERBAL_NOT_BALANCE_CONFIRMATION_2026_05_01.md @ ea1011d
  scope: "inert metadata only"
  certification_effect: NONE
  producer_effect: NONE
  runtime_effect: NONE
  consumer_effect: NONE
  design_scoping:
    status: RATIFIED_AT_3d09e8b
    path: docs/reviews/PHASE_5_C2_MAP_V2_PRODUCER_DESIGN_SCOPING_2026_05_01.md
    source_digest: docs/reviews/PHASE_5_C2_OLYA_BUNDLED_TOUCHPOINT_DIGEST_2026_05_01.md @ 7ad7833
    accepted_design_recommendations:
      - delivery_quality_separate_design_dimension_alongside_market_state_if_later_contract_amended
      - level_state_future_HTF_level_or_PDA_read_model_surface_decision
      - execution_permission_separate_from_HTF_direction
      - strong_Daily_close_through_Daily_only_map_evidence_with_future_primitive_gap_inspection
    certification_effect: NONE
    implementation_effect: NONE
    schema_effect: NONE
    producer_effect: NONE
    runtime_effect: NONE
  wp1_contract_delta_preflight:
    status: RATIFIED_AT_6002d6f
    path: docs/reviews/PHASE_5_C2_WP1_DELIVERY_QUALITY_LEVEL_STATE_CONTRACT_DELTA_PREFLIGHT_2026_05_01.md
    certification_effect: NONE
    schema_effect: NONE
    producer_effect: NONE
    runtime_effect: NONE
  wp2_primitive_gap_report:
    status: RATIFIED_AT_ef185f8
    path: docs/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md
    final_recommendation: existing_surface_extension_needed
    new_primitive_decision: not_made
    methodology_examples_needed_for_tie_break: true
    certification_effect: NONE
    implementation_effect: NONE
    schema_effect: NONE
    producer_effect: NONE
    runtime_effect: NONE
  trade_011_status: provisional_not_canonicalized

one_line: |
  The Daily-authority path initializes correctly, refuses FALLBACK honestly,
  produces stable trade distribution across 5+ years, and now has deterministic
  near-miss diagnostics with FALLBACK placeholder direction partitioned from
  valid OK regime analytics. The regime engine still has no NEUTRAL state once
  any Daily MSS exists; this is a known doctrine gap, not a failure of the
  scoped Daily-authority certification.
```

---

## 2. Walk-forward evidence

```yaml
walk_forward:
  date_run: 2026-04-28
  window: 2021-01-01 → 2026-03-20 (1,633 trading days)
  warmup: 90 days (SW58b1 HTF warmup policy)
  script: en1gma/scripts/run_walk_forward.py
  command: "python -m en1gma.scripts.run_walk_forward --start 2021-01-01 --end 2026-03-20 --workers 4 --output reports/walk_forward_2021_2026.yaml"
  branch: main
  base_head_sha: fa29051
  output: reports/walk_forward_2021_2026.yaml
  diagnostics:
    summary: reports/diagnostics/unknown_near_misses_summary_2021_2026.yaml
    detail: reports/diagnostics/unknown_near_misses_2021_2026.yaml
  wall_time: "7,224s (120.4 min, 4 workers)"
  reproducible: true

  headline_numbers:
    total_days: 1633
    construction_mode:
      OK: "1,564 (95.8%)"
      FALLBACK: "69 (4.2%)"
      FAILED: "0 (0%)"
    init_failed: 0
    all_regime_direction:
      BEARISH: "904 (55.4%)"
      BULLISH: "729 (44.6%)"
      NEUTRAL: "0 (0%)"
    valid_regime_direction_OK_only:
      BEARISH: 867
      BULLISH: 697
    fallback_placeholder_direction:
      BEARISH: 37
      BULLISH: 32
    authority_tf:
      DAILY: "1,633 (100%)"
      H4: "0 (0%)"
    regime_phase:
      EXPANSION: "869 (53.2%)"
      RETRACE: "764 (46.8%)"
    gate_armed_days: "706 (43.2%)"
    chain_complete_days: "88 (5.4%)"
    trades: "88 (W:48 L:40, 54.5% WR, +56.0R)"
    near_misses_true_kz_local: 1003
    bookkeeping_artifacts: 114
    raw_unknown_near_misses: 0
    diagnostic_incomplete: 0
    max_consecutive_losses: 3
```

---

## 2A. Inert non-certification surfaces

```yaml
Map_v2_inert_fixture_surfaces:
  status: INERT_METADATA_AND_DESIGN_ONLY_NOT_CERTIFICATION_EVIDENCE
  latest: "Stage 2D two inert fixtures landed: BALANCE at 8d67740 and trade_014 NOT_BALANCE/RETRACE at 6d4e5d6; C2 Olya bundled digest ratified at 7ad7833, design scoping at 3d09e8b, WP1 at 6002d6f, WP2 brief at c9ff53e, and WP2 gap report at ef185f8."
  fixtures:
    first_balance: tests/fixtures/map_v2/stage_2D/eurusd_daily_2024_08_15_2024_09_12_balance_snapshot.yaml
    second_trade_014_not_balance_retrace: tests/fixtures/map_v2/stage_2D/eurusd_daily_2026_02_04_trade_014_retrace_not_balance_snapshot.yaml
  source_bridge: docs/reviews/PHASE_5_C2_OLYA_VERBAL_NOT_BALANCE_CONFIRMATION_2026_05_01.md @ ea1011d
  design_scoping_bridge: docs/reviews/PHASE_5_C2_MAP_V2_PRODUCER_DESIGN_SCOPING_2026_05_01.md @ 3d09e8b
  wp1_preflight_bridge: docs/reviews/PHASE_5_C2_WP1_DELIVERY_QUALITY_LEVEL_STATE_CONTRACT_DELTA_PREFLIGHT_2026_05_01.md @ 6002d6f
  wp2_gap_report_bridge: docs/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md @ ef185f8
  caveat: |
    These fixtures are accepted inert example snapshots for future
    design/validation scaffolding only. They do not validate Map v2 runtime
    behavior, do not implement a producer or consumer path, do not create runtime
    consumption, do not change schema/cartridge surfaces, and do not certify V2.
    delivery_quality, level_state, execution_permission separation, and strong
    Daily close-through remain design-scoped/preflight-scoped only. WP2 reports
    existing_surface_extension_needed, new_primitive_decision=not_made, and
    methodology_examples_needed_for_tie_break=true. Any producer/read-model output
    change requires future explicit G-ratified contract amendment, and any strong
    Daily close-through machine rule requires future methodology examples and/or
    contract/primitive design before implementation.
```

---

## 3. Validated surfaces

These have evidence from the walk-forward that they work correctly across 5+ years of structurally diverse market conditions.

```yaml

FALLBACK_refusal:
  status: VALIDATED
  evidence: |
    69 FALLBACK days across 1,633 trading days (4.2%). Zero trades on
    FALLBACK dates. SW58a gate refusal fires correctly every time.
    FALLBACK placeholder direction is now reported separately from valid
    OK-mode regime direction.
  invariants_exercised:
    - INV-GATE-REFUSES-FALLBACK-MAP
    - INV-MAP-CONSTRUCTION-MODE-EXPLICIT
    - INV-REGIME-FROM-METHODOLOGY-NOT-FALLBACK

Map_initialization:
  status: VALIDATED
  evidence: |
    Zero INIT_FAILED across 1,633 days. MapEngine.initialize succeeds
    on every trading day in the 5-year window. No data-quality or
    aggregation failures.

gate_funnel_determinism:
  status: VALIDATED
  evidence: |
    POST_4B.H1 corrected the near-miss accounting unit to KZ-local ARMED
    chain evaluations and separated cross-KZ bookkeeping artifacts. Raw
    unknown near-misses are now zero.
      no_sweep: 491
      sweep_no_mss: 249
      causal_fvg_absent: 105
      fvg_no_ote: 85
      location_filter_rejected: 63
      multiple_location_valid_causal_fvgs: 5
      price_not_in_fvg: 4
      eq_side_violation: 1
      raw_unknown: 0
    True KZ-local near-misses: 1,003. Bookkeeping artifacts preserved
    separately: 114.
  reconciliation_note: |
    The v1.0 narrative listed a 1,122-row near-miss breakdown. The actual
    pre-H1 artifact reconciled to 1,117 rows. POST_4B.H1 reconciles exactly:
    1,003 true KZ-local near-misses + 114 bookkeeping artifacts = 1,117.
    The apparent 5-row delta was prior narrative aggregation drift, not
    runtime semantic loss.

trade_distribution_stability:
  status: VALIDATED_AS_SANITY_SIGNAL
  evidence: |
    11-22 trades/year across 5 full years. No negative years. Max 3
    consecutive losses. Both kill zones active (LOKZ: 46, NYOKZ: 42).
    Both directions fire (SHORT: 48, LONG: 40).
  caveat: |
    This is an operational sanity signal, NOT strategy-quality proof.
    Do not interpret +56R as certified edge. Walk-forward P&L is
    secondary to epistemic surface validation.

regime_phase_alternation:
  status: VALIDATED
  evidence: |
    EXPANSION: 53.2%, RETRACE: 46.8%. Healthy alternation without
    pathological aggregate skew in either phase.
```

---

## 4. Known doctrine gaps

These are surfaces where the system is not fully epistemically certified. They are known, documented, and explicitly not implemented.

```yaml
NEUTRAL_regime_absence:
  severity: HIGH — known and accepted
  finding: |
    Zero NEUTRAL regime days across 1,633 trading days. The regime
    engine has only two output paths:
      (a) Daily MSS found → BULLISH or BEARISH (OK)
      (b) No Daily MSS → displacement fallback (FALLBACK, refused)
    There is no third path for "MSS exists but is no longer governing."
  implication: |
    Confirms the methodology seed (docs/methodology_seeds/
    MSS_NOT_EQUAL_ACTIVE_CONTROL.md) applies broadly, not just to
    trade_011, which remains provisional and not canonicalized. An unknown fraction of the 1,564 OK days may have
    stale regime assignments that happen to be harmless because gate
    or chain filters them before they become trades.
  resolution_path: |
    Methodology seed validation cycle: collect 2-3 additional fixtures,
    return to Olya with multi-fixture evidence, mechanize only after
    Olya ratifies a deterministic rule. Do NOT implement from walk-forward
    statistical inference or MSS-age telemetry.
  references:
    - docs/methodology_seeds/MSS_NOT_EQUAL_ACTIVE_CONTROL.md
    - docs/reviews/PHASE_4B_LANE_CLOSE_RATIFICATION_2026_04_27.md §5

H4_cascade_authority:
  severity: MEDIUM — known and accepted
  finding: |
    Zero H4 authority days across 1,633 days. authority_tf is 100%
    DAILY. No code path exists to promote H4 to regime authority.
  implication: |
    All walk-forward results are Daily-authority-only. The validation
    does not cover any future H4/Momentum logic. trade_011 (which
    requires H4 authority) remains outside this certification scope.
  resolution_path: |
    Gated behind NEUTRAL_regime_absence resolution. H4 cascade is
    downstream of Daily-control-check. See VAULT entry
    momentum_continuation_h4_neutral_daily.

long_side_weakness:
  severity: LOW — observation only
  finding: |
    Long WR: 48% (19W/21L). Short WR: 60% (29W/19L). The long side
    is approximately breakeven while the short side carries the edge.
  implication: |
    May be market-cycle bias (EUR/USD trending bearish for much of the
    window), noise from small sample, or signal that some BULLISH regime
    assignments are stale. Not actionable yet.
  resolution_path: |
    Park for future Olya walk-forward review. Do not optimize or
    threshold-tune. If NEUTRAL regime is implemented later, re-check
    whether long-side weakness reduces.
```

---

## 5. Hygiene status

```yaml
unknown_near_miss_taxonomy:
  status: CLOSED
  closed_by: POST_4B.H1.SW-DIAG-UNKNOWN-CHAIN-REASON
  ratification: docs/reviews/POST_4B_H1_DIAG_UNKNOWN_CHAIN_REASON_RATIFICATION_2026_04_28.md
  result: "raw_unknown 0; diagnostic_incomplete 0; 114 bookkeeping artifacts partitioned"

fallback_direction_reporting:
  status: CLOSED
  closed_by: POST_4B.H1.SW-DIAG-UNKNOWN-CHAIN-REASON
  result: |
    valid_regime_direction excludes construction_mode != OK. FALLBACK
    placeholder direction remains visible in fallback_placeholder_direction.

walk_forward_rerun_after_cleanup:
  status: CLOSED
  result: "headline numbers preserved; 88 trades; W:48 L:40; zero FALLBACK trades"
```

---

## 6. Certification upgrade conditions

```yaml
upgrade_to_TRACE_CERTIFIED_DAILY_AUTHORITY_V1:
  status: SATISFIED_AND_RATIFIED
  date: 2026-04-28
  ratification: docs/reviews/POST_4B_H1_DIAG_UNKNOWN_CHAIN_REASON_RATIFICATION_2026_04_28.md
  all_required:
    unknown_near_miss_count_reduced_to_zero: PASS
    walk_forward_rerun_preserves_headline_numbers: PASS
    fallback_direction_reporting_distinguished_from_valid_regime_direction: PASS
  scope_limits:
    - "Daily-authority-only certification"
    - "NEUTRAL regime implementation not included"
    - "H4 cascade authority not included"
    - "Long-side weakness remains observation only"
    - "P&L optimization not included"

upgrade_to_FULLY_EPISTEMICALLY_CERTIFIED:
  status: FUTURE_PHASE_5_PLUS
  requires_additionally:
    - "Methodology seed resolved: MSS_NOT_EQUAL_ACTIVE_CONTROL mechanized from multi-fixture evidence"
    - "NEUTRAL regime state implemented and walk-forward re-run"
    - "H4 cascade authority implemented (if methodology supports it)"
    - "14/14 chart-truth including trade_011"
    - "Olya extreme confidence checkpoint passed"
  note: |
    FULLY_EPISTEMICALLY_CERTIFIED is not a current Phase 4 deliverable.
    TRACE_CERTIFIED_DAILY_AUTHORITY_V1 is scoped and does not mechanize
    stale Daily MSS control.
```

---

## 7. Walk-forward provenance

```yaml
run_record:
  date: 2026-04-28
  script: en1gma/scripts/run_walk_forward.py
  command: "python -m en1gma.scripts.run_walk_forward --start 2021-01-01 --end 2026-03-20 --workers 4 --output reports/walk_forward_2021_2026.yaml"
  branch: main
  base_head_sha: fa29051
  river_data: ~/phoenix-river/EURUSD (Dukascopy 1m bars, 2020-11-23 → 2026-03-20)
  warmup_policy: 90 days (SW58b1)
  workers: 4 (multiprocessing.Pool, ~408 days/chunk)
  output_artifact: reports/walk_forward_2021_2026.yaml
  diagnostic_artifacts:
    - reports/diagnostics/unknown_near_misses_summary_2021_2026.yaml
    - reports/diagnostics/unknown_near_misses_2021_2026.yaml
  wall_time: "7,224s (120.4 min)"

  chunk_details:
    - "chunk 0: 2021-01-01 → 2022-04-21 (408 days, 6876s)"
    - "chunk 1: 2022-04-22 → 2023-08-10 (408 days, 7224s)"
    - "chunk 2: 2023-08-11 → 2024-11-28 (408 days, 6971s)"
    - "chunk 3: 2024-11-29 → 2026-03-20 (409 days, 6991s)"

rerun_triggers:
  - "Any change to map_engine.py regime initialization"
  - "Any change to gate.py evaluation logic"
  - "Any change to chain_evaluator.py"
  - "Any change to run_discovery_scan.py diagnostic accounting"
  - "Any change to run_walk_forward.py merge/reporting logic"
  - "Any future implementation of delivery_quality, level_state, execution_permission separation, or Daily strong-close-through primitive/extension logic"
  - "HTF warmup window change"
  - "Detection engine change"
  - "New cartridge affecting DAILY_EXPANSION"
  - "Any future change that makes Stage 2D inert fixtures runtime-consumed or producer-generated"
```

---

## 8. Observations for future methodology work

Parked findings from the walk-forward that are not actionable now but should inform future sprints.

```yaml
stale_MSS_authority_frequency:
  observation: |
    With a 90-day lookback, the regime engine always finds either a Daily
    MSS or falls back to displacement. POST_4B.H1 added output-only MSS-age
    telemetry for evidence indexing. It must not be treated as a filter,
    confidence decay, neutral heuristic, or active-control doctrine.
  priority: FUTURE (methodology seed validation cycle)

eq_side_violation_singleton:
  observation: |
    Cleaned funnel retains one eq_side_violation near-miss. This is a
    singleton diagnostic residual, not an implementation target.
  priority: PARKED (review only if it recurs or Olya requests funnel review)

clean_funnel_shape:
  observation: |
    New true KZ-local near-miss funnel is deterministic: no_sweep 491,
    sweep_no_mss 249, causal_fvg_absent 105, fvg_no_ote 85,
    location_filter_rejected 63, small residual deterministic classes 10.
  priority: "FUTURE sanity check at next Olya walk-forward touchpoint; do not optimize thresholds from this distribution."

FALLBACK_period_market_structure:
  observation: |
    FALLBACK clusters correlate with ranging/transitional markets. These
    are periods where DAILY_EXPANSION should produce NO_TRADE, and it does.
    They may inform future RANGE or RETRACE cartridge discussions.
  priority: FUTURE (post-Phase 4, new cartridge work)

short_side_edge_concentration:
  observation: |
    60% short WR vs 48% long WR. EUR/USD was trending bearish for
    significant portions of 2021-2024. The short-side edge may be
    market-cycle alpha rather than structural strategy alpha.
  priority: FUTURE (walk-forward subset analysis, Olya review)
```

---

*CERTIFICATION_STATE v1.4 — TRACE_CERTIFIED_DAILY_AUTHORITY_V1 unchanged. Stage 2D fixtures, C2 design scoping, WP1, and WP2 are not V2 certification evidence; known NEUTRAL/H4 doctrine gap remains parked behind MSS_NOT_EQUAL_ACTIVE_CONTROL validation, and trade_011 remains provisional/not canonicalized.*
