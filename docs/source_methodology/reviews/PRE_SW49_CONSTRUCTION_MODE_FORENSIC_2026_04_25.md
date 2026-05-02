```yaml
mission: PHASE_4B.M2.FORENSIC.PRE_SW49
status: GREEN
authored: 2026-04-25
base_main_head_verified: fdde343
classification: READ_ONLY_FORENSIC
instrumentation_branch: forensic/pre-sw49-construction-mode
instrumentation_commit: 6b70395
instrumented_run:
  command: PRE_SW49_FORENSIC_LOG=/tmp/pre_sw49_forensic.jsonl python3 -m pytest -q en1gma/tests/integration/test_daily_expansion_chart_truth.py
  result: "6 passed"
  log_path: /tmp/pre_sw49_forensic.jsonl
  log_records: 339

pre_task_verification:
  origin_main_head:
    expected: fdde343
    observed_head: fdde343
    observed_origin_main: fdde343
    result: PASS

  mapstate_construction_mode_field:
    field_exists: true
    field_path: en1gma/console/map/context_types.py:223
    enum_path: en1gma/console/map/context_types.py:97
    enum_values: [NORMAL, FALLBACK]
    default_value: MapConstructionMode.NORMAL
    explicit_production_setters: []
    current_meaning:
      NORMAL: "current non-fallback / OK-equivalent scaffold value"
      FALLBACK: "gate-refused value; only test fixture sets explicitly at fdde343"
    instrumentation_strategy: BRANCH_A_PLUS_PATH_IDENTITY
    rationale: |
      construction_mode exists, but production MapState constructors omit it and
      therefore default to NORMAL. Forensic run logged both current field value
      and path identity at regime/DR/PDA construction surfaces.

  chart_truth_gate_baseline:
    command: python3 -m pytest -q en1gma/tests/integration/test_daily_expansion_chart_truth.py
    result: "6 passed"

  chart_truth_fixture_set:
    - {trade_id: trade_001, evaluation_timestamp: "2025-10-01T03:30:00-04:00"}
    - {trade_id: trade_003, evaluation_timestamp: "2025-12-12T08:00:00-05:00"}
    - {trade_id: trade_005, evaluation_timestamp: "2025-12-12T09:00:00-05:00"}
    - {trade_id: trade_006, evaluation_timestamp: "2025-12-15T03:45:00-05:00"}
    - {trade_id: trade_007, evaluation_timestamp: "2025-09-16T09:45:00-04:00"}
    - {trade_id: trade_013, evaluation_timestamp: "2026-03-12T09:00:00-04:00"}

  chart_truth_call_chain:
    entry: en1gma/tests/integration/test_daily_expansion_chart_truth.py:test_daily_expansion_chart_truth_expected_state
    snapshot: en1gma/tests/integration/test_daily_expansion_chart_truth.py:_semantic_snapshot
    production_init: en1gma/console/chain/canon/map_canon/session.py:_init_map_for_date
    map_entry: en1gma/console/map/map_engine.py:MapEngine.initialize
    key_steps:
      - load_date_range(DEFAULT_RIVER, trade_date - 45d, trade_date)
      - point_in_time_bars = bars where bar.ny <= evaluation_timestamp
      - _init_map_for_date(point_in_time_bars, trade_date, htf_timeframes=["1D","4H"])
      - MapEngine.initialize(...) -> get_state()
      - assert map_state.regime direction / authority_tf / phase

per_fixture:
  - trade_id: trade_001
    evaluation_timestamp: "2025-10-01T03:30:00-04:00"
    construction_mode: OK
    observed_current_field: NORMAL
    construction_source_path: "en1gma/console/map/map_engine.py:264-271 _initialize_regime_from_detections daily MSS detector branch (ME-01)"
    primary_source_event: mss_1D_2025-09-24T00:00:00_bear
    source_event_timestamp: "2025-09-24T00:00:00-04:00"
    emitted_regime: {direction: BEARISH, authority_tf: DAILY, phase: EXPANSION}
    dealing_range_source_leg: displacement_1D_2025-09-23T00:00:00_bear
    fallback_sites_fired: []
    chart_truth_result_at_fdde343: PASS
    supporting_log_excerpt:
      - {event: regime_update, site_id: ME-01, path_classification: DETECTOR_SOURCED, bar_datetime: "2025-09-24T00:00:00-04:00", source_mss_id: mss_1D_2025-09-24T00:00:00_bear, emitted_regime_direction: BEARISH, emitted_authority_tf: DAILY, changed: true}
      - {event: map_state_emit, site_id: ME-14, construction_mode: NORMAL, bar_datetime: "2025-10-01T03:30:00-04:00", source_mss_id: mss_1D_2025-09-24T00:00:00_bear, emitted_regime_direction: BEARISH, emitted_authority_tf: DAILY, emitted_regime_phase: EXPANSION, dealing_range_source_leg: displacement_1D_2025-09-23T00:00:00_bear}

  - trade_id: trade_003
    evaluation_timestamp: "2025-12-12T08:00:00-05:00"
    construction_mode: OK
    observed_current_field: NORMAL
    construction_source_path: "en1gma/console/map/map_engine.py:264-271 _initialize_regime_from_detections daily MSS detector branch (ME-01)"
    primary_source_event: mss_1D_2025-12-10T00:00:00_bull
    source_event_timestamp: "2025-12-10T00:00:00-05:00"
    emitted_regime: {direction: BULLISH, authority_tf: DAILY, phase: EXPANSION}
    dealing_range_source_leg: displacement_4H_2025-12-11T08:00:00_bull
    fallback_sites_fired: []
    chart_truth_result_at_fdde343: PASS
    supporting_log_excerpt:
      - {event: regime_update, site_id: ME-01, path_classification: DETECTOR_SOURCED, bar_datetime: "2025-12-10T00:00:00-05:00", source_mss_id: mss_1D_2025-12-10T00:00:00_bull, emitted_regime_direction: BULLISH, emitted_authority_tf: DAILY, changed: true}
      - {event: map_state_emit, site_id: ME-14, construction_mode: NORMAL, bar_datetime: "2025-12-12T08:00:00-05:00", source_mss_id: mss_1D_2025-12-10T00:00:00_bull, emitted_regime_direction: BULLISH, emitted_authority_tf: DAILY, emitted_regime_phase: EXPANSION, dealing_range_source_leg: displacement_4H_2025-12-11T08:00:00_bull}

  - trade_id: trade_005
    evaluation_timestamp: "2025-12-12T09:00:00-05:00"
    construction_mode: OK
    observed_current_field: NORMAL
    construction_source_path: "en1gma/console/map/map_engine.py:264-271 _initialize_regime_from_detections daily MSS detector branch (ME-01)"
    primary_source_event: mss_1D_2025-12-10T00:00:00_bull
    source_event_timestamp: "2025-12-10T00:00:00-05:00"
    emitted_regime: {direction: BULLISH, authority_tf: DAILY, phase: EXPANSION}
    dealing_range_source_leg: displacement_4H_2025-12-11T08:00:00_bull
    fallback_sites_fired: []
    chart_truth_result_at_fdde343: PASS
    supporting_log_excerpt:
      - {event: regime_update, site_id: ME-01, path_classification: DETECTOR_SOURCED, bar_datetime: "2025-12-10T00:00:00-05:00", source_mss_id: mss_1D_2025-12-10T00:00:00_bull, emitted_regime_direction: BULLISH, emitted_authority_tf: DAILY, changed: true}
      - {event: map_state_emit, site_id: ME-14, construction_mode: NORMAL, bar_datetime: "2025-12-12T09:00:00-05:00", source_mss_id: mss_1D_2025-12-10T00:00:00_bull, emitted_regime_direction: BULLISH, emitted_authority_tf: DAILY, emitted_regime_phase: EXPANSION, dealing_range_source_leg: displacement_4H_2025-12-11T08:00:00_bull}

  - trade_id: trade_006
    evaluation_timestamp: "2025-12-15T03:45:00-05:00"
    construction_mode: OK
    observed_current_field: NORMAL
    construction_source_path: "en1gma/console/map/map_engine.py:264-271 _initialize_regime_from_detections daily MSS detector branch (ME-01)"
    primary_source_event: mss_1D_2025-12-10T00:00:00_bull
    source_event_timestamp: "2025-12-10T00:00:00-05:00"
    emitted_regime: {direction: BULLISH, authority_tf: DAILY, phase: EXPANSION}
    dealing_range_source_leg: displacement_4H_2025-12-12T08:00:00_bull
    fallback_sites_fired: []
    chart_truth_result_at_fdde343: PASS
    supporting_log_excerpt:
      - {event: regime_update, site_id: ME-01, path_classification: DETECTOR_SOURCED, bar_datetime: "2025-12-10T00:00:00-05:00", source_mss_id: mss_1D_2025-12-10T00:00:00_bull, emitted_regime_direction: BULLISH, emitted_authority_tf: DAILY, changed: true}
      - {event: map_state_emit, site_id: ME-14, construction_mode: NORMAL, bar_datetime: "2025-12-15T03:45:00-05:00", source_mss_id: mss_1D_2025-12-10T00:00:00_bull, emitted_regime_direction: BULLISH, emitted_authority_tf: DAILY, emitted_regime_phase: EXPANSION, dealing_range_source_leg: displacement_4H_2025-12-12T08:00:00_bull}

  - trade_id: trade_007
    evaluation_timestamp: "2025-09-16T09:45:00-04:00"
    construction_mode: OK
    observed_current_field: NORMAL
    construction_source_path: "en1gma/console/map/map_engine.py:264-271 _initialize_regime_from_detections daily MSS detector branch (ME-01)"
    primary_source_event: mss_1D_2025-09-07T00:00:00_bull
    source_event_timestamp: "2025-09-07T00:00:00-04:00"
    emitted_regime: {direction: BULLISH, authority_tf: DAILY, phase: EXPANSION}
    dealing_range_source_leg: displacement_4H_2025-09-16T08:00:00_bull
    fallback_sites_fired: []
    chart_truth_result_at_fdde343: PASS
    supporting_log_excerpt:
      - {event: regime_update, site_id: ME-01, path_classification: DETECTOR_SOURCED, bar_datetime: "2025-09-07T00:00:00-04:00", source_mss_id: mss_1D_2025-09-07T00:00:00_bull, emitted_regime_direction: BULLISH, emitted_authority_tf: DAILY, changed: true}
      - {event: map_state_emit, site_id: ME-14, construction_mode: NORMAL, bar_datetime: "2025-09-16T09:45:00-04:00", source_mss_id: mss_1D_2025-09-07T00:00:00_bull, emitted_regime_direction: BULLISH, emitted_authority_tf: DAILY, emitted_regime_phase: EXPANSION, dealing_range_source_leg: displacement_4H_2025-09-16T08:00:00_bull}

  - trade_id: trade_013
    evaluation_timestamp: "2026-03-12T09:00:00-04:00"
    construction_mode: OK
    observed_current_field: NORMAL
    construction_source_path: "en1gma/console/map/map_engine.py:264-271 _initialize_regime_from_detections daily MSS detector branch (ME-01)"
    primary_source_event: mss_1D_2026-03-01T00:00:00_bear
    source_event_timestamp: "2026-03-01T00:00:00-05:00"
    emitted_regime: {direction: BEARISH, authority_tf: DAILY, phase: EXPANSION}
    dealing_range_source_leg: displacement_1D_2026-03-01T00:00:00_bear
    fallback_sites_fired: []
    chart_truth_result_at_fdde343: PASS
    supporting_log_excerpt:
      - {event: regime_update, site_id: ME-01, path_classification: DETECTOR_SOURCED, bar_datetime: "2026-03-01T00:00:00-05:00", source_mss_id: mss_1D_2026-03-01T00:00:00_bear, emitted_regime_direction: BEARISH, emitted_authority_tf: DAILY, changed: true}
      - {event: map_state_emit, site_id: ME-14, construction_mode: NORMAL, bar_datetime: "2026-03-12T09:00:00-04:00", source_mss_id: mss_1D_2026-03-01T00:00:00_bear, emitted_regime_direction: BEARISH, emitted_authority_tf: DAILY, emitted_regime_phase: EXPANSION, dealing_range_source_leg: displacement_1D_2026-03-01T00:00:00_bear}

summary:
  non_OK_count: 0
  non_OK_fixture_ids: []
  primary_source_distribution: {ME-01: 6}
  fallback_site_distribution: {}
  all_logged_site_distribution: {ME-01: 9, DR-01: 6, ME-10: 318, ME-14: 6}
  expected_decision_per_g_ruling: PROCEED_SW49_NARROW_HARD_REFUSAL
  no_interpretation_clause: "This report measures path identity and applies only G's binary decision tree; it proposes no implementation fix."

inventory_appendix:
  fallback_sites_confirmed:
    - site_id: ME-03
      ref: en1gma/console/map/map_engine.py:305-312
      function: _initialize_dealing_range_from_detections
      branch_condition: "if not disp_events and daily_bars non-empty"
      classification: FALLBACK
      fired_in_six_fixture_run: false
    - site_id: ME-06a
      ref: en1gma/console/map/map_engine.py:402-403
      function: _find_origin_before_displacement
      branch_condition: "pullback_bars.empty -> daily_bars[before_mask].tail(5)"
      classification: FALLBACK
      fired_in_six_fixture_run: false
    - site_id: ME-06b
      ref: en1gma/console/map/map_engine.py:404-405
      function: _find_origin_before_displacement
      branch_condition: "tail(5) still empty -> daily_bars.head(first half)"
      classification: FALLBACK
      fired_in_six_fixture_run: false
    - site_id: ME-04
      ref: en1gma/console/map/map_engine.py:327-336
      function: _initialize_dealing_range_from_detections
      branch_condition: "timestamp comparison raises -> except Exception: pass"
      classification: FALLBACK
      fired_in_six_fixture_run: false
    - site_id: ME-10
      ref: en1gma/console/map/map_engine.py:547-587
      function: _initialize_pdas_from_detections
      branch_condition: "valid FVG detections create PDAs; malformed FVG skipped at debug"
      classification: DETECTOR_SOURCED
      fired_in_six_fixture_run: true

  all_construction_sites:
    - {site_id: CT-01, ref: en1gma/console/map/context_types.py:97, function: MapConstructionMode, classification: UNKNOWN_NEEDS_TRACE, note: "enum scaffold NORMAL/FALLBACK"}
    - {site_id: CT-02, ref: en1gma/console/map/context_types.py:209-223, function: MapState, classification: UNKNOWN_NEEDS_TRACE, note: "construction_mode default NORMAL"}
    - {site_id: R-01, ref: en1gma/console/map/regime.py:25-29, function: RegimeTracker.__init__, classification: UNKNOWN_NEEDS_TRACE, note: "initial NEUTRAL/RANGE/DAILY"}
    - {site_id: R-02, ref: en1gma/console/map/regime.py:48-54, function: RegimeTracker.update_on_mss, classification: DETECTOR_SOURCED, note: "neutral -> detector direction"}
    - {site_id: R-03, ref: en1gma/console/map/regime.py:61-67, function: RegimeTracker.update_on_mss, classification: DETECTOR_SOURCED, note: "opposing same/higher TF flips direction"}
    - {site_id: ME-01, ref: en1gma/console/map/map_engine.py:262-272, function: _initialize_regime_from_detections, classification: DETECTOR_SOURCED, note: "daily MSS detector branch"}
    - {site_id: ME-02, ref: en1gma/console/map/map_engine.py:280-292, function: _initialize_regime_from_detections, classification: DETECTOR_SOURCED, note: "daily displacement-derived regime branch when no MSS"}
    - {site_id: ME-03, ref: en1gma/console/map/map_engine.py:305-312, function: _initialize_dealing_range_from_detections, classification: FALLBACK, note: "fallback_full_range"}
    - {site_id: ME-04, ref: en1gma/console/map/map_engine.py:327-336, function: _initialize_dealing_range_from_detections, classification: FALLBACK, note: "timestamp compare except/pass"}
    - {site_id: ME-05, ref: en1gma/console/map/map_engine.py:340-341, function: _initialize_dealing_range_from_detections, classification: FALLBACK, note: "regime_disp = disp_events[-1]"}
    - {site_id: ME-06, ref: en1gma/console/map/map_engine.py:402-405, function: _find_origin_before_displacement, classification: FALLBACK, note: "pullback_bars fallback tail(5)/first-half"}
    - {site_id: ME-07, ref: en1gma/console/map/map_engine.py:444-450, function: _find_displacement_extreme, classification: FALLBACK, note: "missing extreme_candle -> scan bars"}
    - {site_id: ME-08, ref: en1gma/console/map/map_engine.py:517-522, function: _compute_h4_dealing_range, classification: DETECTOR_SOURCED_OR_FALLBACK, note: "post-regime H4 displacement or same_dir[-1] fallback"}
    - {site_id: ME-09, ref: en1gma/console/map/map_engine.py:537-545, function: _compute_h4_dealing_range, classification: DETECTOR_SOURCED_OR_FALLBACK, note: "H4 DealingRange construction depends on selected displacement branch"}
    - {site_id: ME-10, ref: en1gma/console/map/map_engine.py:565-587, function: _initialize_pdas_from_detections, classification: DETECTOR_SOURCED, note: "PDA fields from detector FVG"}
    - {site_id: ME-11, ref: en1gma/console/map/map_engine.py:621-631, function: _replay_price_forward, classification: UNKNOWN_NEEDS_TRACE, note: "PDA lifecycle timestamp compare except/pass"}
    - {site_id: ME-12, ref: en1gma/console/map/map_engine.py:637-654, function: process_daily_bar, classification: UNKNOWN_NEEDS_TRACE, note: "returns get_state()"}
    - {site_id: ME-13, ref: en1gma/console/map/map_engine.py:656-669, function: process_h4_bar, classification: UNKNOWN_NEEDS_TRACE, note: "returns get_state()"}
    - {site_id: ME-14, ref: en1gma/console/map/map_engine.py:675-686, function: get_state, classification: UNKNOWN_NEEDS_TRACE, note: "MapState constructor omits construction_mode -> default NORMAL"}
    - {site_id: DR-01, ref: en1gma/console/map/dealing_range.py:56-64, function: DealingRangeTracker.create_range, classification: DETECTOR_SOURCED_OR_FALLBACK, note: "classification depends on caller source_leg"}
    - {site_id: PDA-01, ref: en1gma/console/map/pda_store.py:60-75, function: PDAStore.add_fvg, classification: DETECTOR_SOURCED, note: "production caller is _initialize_pdas_from_detections"}
    - {site_id: MP-01, ref: en1gma/console/map/map_persistence.py:106-114, function: deserialize_map_state, classification: UNKNOWN_NEEDS_TRACE, note: "Regime from JSON"}
    - {site_id: MP-02, ref: en1gma/console/map/map_persistence.py:118-125, function: deserialize_map_state, classification: UNKNOWN_NEEDS_TRACE, note: "DealingRange from JSON"}
    - {site_id: MP-03, ref: en1gma/console/map/map_persistence.py:129-134, function: deserialize_map_state, classification: UNKNOWN_NEEDS_TRACE, note: "MapState constructor omits construction_mode -> default NORMAL"}
    - {site_id: DS-01, ref: en1gma/console/map/day_state.py:77-84, function: DayStateEngine.__init__, classification: UNKNOWN_NEEDS_TRACE, note: "initial PRE_EXPANSION from regime direction/TF"}
    - {site_id: DS-02, ref: en1gma/console/map/day_state.py:151-163, function: process_detections, classification: DETECTOR_SOURCED, note: "transition via _check_expansion_delivered"}
    - {site_id: DS-03, ref: en1gma/console/map/day_state.py:210-217, function: _check_expansion_delivered, classification: DETECTOR_SOURCED, note: "aligned displacement + MSS"}
    - {site_id: DS-04, ref: en1gma/console/map/day_state.py:219-223, function: _resolve_transition_tf, classification: FALLBACK, note: "unsupported TF fallback to DAILY"}

  absent_paths_checked:
    - en1gma/console/session.py
    - en1gma/console/day_state.py
```
