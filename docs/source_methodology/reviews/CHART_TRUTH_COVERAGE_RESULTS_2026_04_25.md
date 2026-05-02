```yaml
mission: PHASE_4B.M3.CHART_TRUTH_COVERAGE
status: DIAGNOSTIC_COMPLETE
base_head: 92cb9ab
test_file: en1gma/tests/integration/test_daily_expansion_chart_truth.py
asserted_fields: [daily_direction, authority_tf, htf_phase]
summary:
  total_fixtures: 12
  pass_count: 6
  fail_count: 6
  fail_breakdown:
    daily_direction_mismatch: 2
    authority_tf_mismatch: 1
    htf_phase_mismatch: 6
    multiple_field_mismatch: 2
  no_interpretation_clause: >
    Document reports current chart-truth assertion outcomes only. It does not
    propose fixes, classify gaps as methodology vs implementation, or assign
    additional SW IDs beyond the coverage-expansion closeout ID.
per_fixture_table:
  - trade_id: trade_001
    date: "2025-10-01"
    strategy_type: state_gated
    evaluation_timestamp: "2025-10-01T03:30:00-04:00"
    status: PASS
    expected_state: {'daily_direction': 'BEARISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    actual_state_at_evaluation: {'daily_direction': 'BEARISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    failure_class: none
    mismatches: {}
    htf_window: "2025-08-17→2025-10-01T03:30:00-04:00"
  - trade_id: trade_002
    date: "2025-09-29"
    strategy_type: state_gated
    evaluation_timestamp: "2025-09-29T07:45:00-04:00"
    status: FAIL
    expected_state: {'daily_direction': 'BEARISH', 'authority_tf': 'DAILY', 'htf_phase': 'RETRACE'}
    actual_state_at_evaluation: {'daily_direction': 'BEARISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    failure_class: htf_phase
    mismatches: {'htf_phase': {'expected': 'RETRACE', 'actual': 'EXPANSION'}}
    htf_window: "2025-08-15→2025-09-29T07:45:00-04:00"
  - trade_id: trade_003
    date: "2025-12-12"
    strategy_type: state_gated
    evaluation_timestamp: "2025-12-12T08:00:00-05:00"
    status: PASS
    expected_state: {'daily_direction': 'BULLISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    actual_state_at_evaluation: {'daily_direction': 'BULLISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    failure_class: none
    mismatches: {}
    htf_window: "2025-10-28→2025-12-12T08:00:00-05:00"
  - trade_id: trade_005
    date: "2025-12-12"
    strategy_type: state_gated
    evaluation_timestamp: "2025-12-12T09:00:00-05:00"
    status: PASS
    expected_state: {'daily_direction': 'BULLISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    actual_state_at_evaluation: {'daily_direction': 'BULLISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    failure_class: none
    mismatches: {}
    htf_window: "2025-10-28→2025-12-12T09:00:00-05:00"
  - trade_id: trade_006
    date: "2025-12-15"
    strategy_type: state_gated
    evaluation_timestamp: "2025-12-15T03:45:00-05:00"
    status: PASS
    expected_state: {'daily_direction': 'BULLISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    actual_state_at_evaluation: {'daily_direction': 'BULLISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    failure_class: none
    mismatches: {}
    htf_window: "2025-10-31→2025-12-15T03:45:00-05:00"
  - trade_id: trade_007
    date: "2025-09-16"
    strategy_type: state_gated
    evaluation_timestamp: "2025-09-16T09:45:00-04:00"
    status: PASS
    expected_state: {'daily_direction': 'BULLISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    actual_state_at_evaluation: {'daily_direction': 'BULLISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    failure_class: none
    mismatches: {}
    htf_window: "2025-08-02→2025-09-16T09:45:00-04:00"
  - trade_id: trade_008
    date: "2025-10-15"
    strategy_type: state_gated
    evaluation_timestamp: "2025-10-15T10:00:00-04:00"
    status: FAIL
    expected_state: {'daily_direction': 'BEARISH', 'authority_tf': 'DAILY', 'htf_phase': 'RETRACE'}
    actual_state_at_evaluation: {'daily_direction': 'BEARISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    failure_class: htf_phase
    mismatches: {'htf_phase': {'expected': 'RETRACE', 'actual': 'EXPANSION'}}
    htf_window: "2025-08-31→2025-10-15T10:00:00-04:00"
  - trade_id: trade_010
    date: "2025-11-12"
    strategy_type: state_gated
    evaluation_timestamp: "2025-11-12T09:30:00-05:00"
    status: FAIL
    expected_state: {'daily_direction': 'BEARISH', 'authority_tf': 'DAILY', 'htf_phase': 'RETRACE'}
    actual_state_at_evaluation: {'daily_direction': 'BULLISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    failure_class: daily_direction+htf_phase
    mismatches: {'daily_direction': {'expected': 'BEARISH', 'actual': 'BULLISH'}, 'htf_phase': {'expected': 'RETRACE', 'actual': 'EXPANSION'}}
    htf_window: "2025-09-28→2025-11-12T09:30:00-05:00"
  - trade_id: trade_011
    date: "2025-11-28"
    strategy_type: state_gated
    evaluation_timestamp: "2025-11-28T09:15:00-05:00"
    status: FAIL
    expected_state: {'daily_direction': 'NEUTRAL', 'authority_tf': 'H4', 'htf_phase': 'RANGE'}
    actual_state_at_evaluation: {'daily_direction': 'BEARISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    failure_class: daily_direction+authority_tf+htf_phase
    mismatches: {'daily_direction': {'expected': 'NEUTRAL', 'actual': 'BEARISH'}, 'authority_tf': {'expected': 'H4', 'actual': 'DAILY'}, 'htf_phase': {'expected': 'RANGE', 'actual': 'EXPANSION'}}
    htf_window: "2025-10-14→2025-11-28T09:15:00-05:00"
  - trade_id: trade_012
    date: "2026-03-17"
    strategy_type: state_gated
    evaluation_timestamp: "2026-03-17T08:25:00-04:00"
    status: FAIL
    expected_state: {'daily_direction': 'BEARISH', 'authority_tf': 'DAILY', 'htf_phase': 'RETRACE'}
    actual_state_at_evaluation: {'daily_direction': 'BEARISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    failure_class: htf_phase
    mismatches: {'htf_phase': {'expected': 'RETRACE', 'actual': 'EXPANSION'}}
    htf_window: "2026-01-31→2026-03-17T08:25:00-04:00"
  - trade_id: trade_013
    date: "2026-03-12"
    strategy_type: state_gated
    evaluation_timestamp: "2026-03-12T09:00:00-04:00"
    status: PASS
    expected_state: {'daily_direction': 'BEARISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    actual_state_at_evaluation: {'daily_direction': 'BEARISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    failure_class: none
    mismatches: {}
    htf_window: "2026-01-26→2026-03-12T09:00:00-04:00"
  - trade_id: trade_014
    date: "2026-02-04"
    strategy_type: state_gated
    evaluation_timestamp: "2026-02-04T07:00:00-05:00"
    status: FAIL
    expected_state: {'daily_direction': 'BULLISH', 'authority_tf': 'DAILY', 'htf_phase': 'RETRACE'}
    actual_state_at_evaluation: {'daily_direction': 'BULLISH', 'authority_tf': 'DAILY', 'htf_phase': 'EXPANSION'}
    failure_class: htf_phase
    mismatches: {'htf_phase': {'expected': 'RETRACE', 'actual': 'EXPANSION'}}
    htf_window: "2025-12-21→2026-02-04T07:00:00-05:00"
```
