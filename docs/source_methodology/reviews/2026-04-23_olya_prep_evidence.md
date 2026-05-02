# Olya Prep — Evidence Pack

```yaml
document: OLYA_PREP_EVIDENCE_2026_04_23
version: 1.0
date: 2026-04-23
status: READ-ONLY evidence enumeration
owner: Opus RepoPrompt (Phase 4b prep parallel track; 4a in-flight on M4 Max)
brief: PHASE_4B.PREP.OLYA_PACK_EVIDENCE_GATHERING
scope: enumeration only — CTO drafts prep pack + counter-examples + options
source_head: phase_3_5-exit + post-oracle (inheriting from
             2026-04-26 verification pass docs + current HEAD CLAUDE.md v0.15)
mutation_scope: NONE — docs/reviews/ addition only; en1gma/ untouched
authority_cross_refs:
  CLAUDE.md: §6 invariants + §15 SW27 / SW28 / SW31 full framings + §4 strategy model
  FORWARD_PLAN.md: v2.3 §P3 Post-Phase-3 scope, Olya queue line 681
  POST_PHASE_3_ORACLE.md: §4.6 Map init + §4.7 cascade + §4.8 day_state
                         + §6 hot files
  COO_INPUTS_POST_PHASE_3.md: §3.2 P3 + P5 + C3 Olya bottleneck
  2026-04-26_phase_4a_verification_pass.md: T5 F2.1 + T6 F2.2 lineage
purpose: |
  Enumerate ground-truth repository evidence for Phase 4b Olya session
  prep pack. Six tasks per brief: T1 P3 fallback inventory, T2 P5
  day_state causal linkage code capture, T3 SW27 queued framing, T4
  SW31 queued framing, T5 F2.2 Shape 2 cross-path event overlap, T6
  ground-truth trade index.
rule: |
  Enumeration only. No methodology options, no counter-example
  assignment, no SW ID assignment. Evidence is pinned to file:line
  references; staleness discipline per POST_PHASE_3_ORACLE.
```

---

## T1 — P3 Map Init Fallback Inventory

```yaml
target: en1gma/console/map/map_engine.py — every fallback branch that could
        mask invalid Map state with a permissive default
audit_method:
  - grep try/except across map_engine.py
  - grep `.get(..., default)` for semantic-default patterns
  - grep `if ... is None` + `if ... .empty` for conditional fallbacks
  - cross-check against POST_PHASE_3_ORACLE §4.6 known sites
authority_surface_adjacency:
  all_sites_inside_module: en1gma/console/map/map_engine.py
  consumers_reading_resulting_state:
    - en1gma/console/map/dealing_range.py (DealingRangeTracker — reads
      DR origin/extreme produced here)
    - en1gma/console/map/gate.py (reads map_state.active_pdas
      downstream — SW47 direction clause + SW47 F1 scaffold land here)
    - en1gma/console/chain/canon/map_canon/session.py::_run_map_session
      (consumes MapEngine instance returned by _init_map_for_date)

fallbacks:

  - site: en1gma/console/map/map_engine.py:305-311
    name: FB01_fallback_full_range_no_displacement
    current_shape: |
      if not disp_events:
          if not daily_bars.empty:
              self._dealing_range.create_range(
                  origin_wick=daily_bars["high"].max(),
                  extreme_wick=daily_bars["low"].min(),
                  source_leg="fallback_full_range",
              )
          return
    trigger_condition: |
      Zero displacement events emitted by detect.py at 1D timeframe
      across the entire 45-day HTF lookback. Map is being asked to
      initialize a dealing range with no structural basis for
      direction or extents.
    docstring_intent: |
      Function docstring (:294): "Derive dealing range from
      displacement events on daily bars." No documented fallback
      semantic. The "fallback_full_range" source_leg label is the
      only in-code marker.
    silent_vs_explicit: |
      EXPLICIT branch (named source_leg) but SILENT semantically —
      no log, no raise, no MapState construction_mode flag. Consumer
      (gate.py SW47 F1 scaffold) cannot distinguish this DR from a
      detector-derived one.
    methodology_adjacency: HIGH
    notes: |
      Directly affects Map truth (DR origin + extreme). Under this
      fallback, DR ≈ full-range box of daily_bars window; discount
      + premium are half-splits of the full window rather than
      methodology-calibrated zones.

  - site: en1gma/console/map/map_engine.py:327-337
    name: FB02_regime_time_timestamp_compare_swallow
    current_shape: |
      try:
          d_end = d.properties.get("time_end", d.time)
          d_ts = pd.Timestamp(d_end)
          r_ts = pd.Timestamp(regime_time)
          if d_ts.tz is None and r_ts.tz is not None:
              d_ts = d_ts.tz_localize(r_ts.tz)
          if d_ts < r_ts:
              continue
      except Exception:
          pass
    trigger_condition: |
      Any exception during timestamp comparison between a candidate
      displacement's time_end property and the regime's
      established_at timestamp. Tz mismatch, malformed property
      dict, naive timestamp combined with unexpected input, etc.
    docstring_intent: |
      No docstring on the branch itself. Enclosing function
      docstring (:294 `_initialize_dealing_range_from_detections`)
      does not mention tz-failure handling. INV-DETECTION-TIME-TZ-
      AWARE (SW24) guarantees incoming Detection.time is tz-aware
      at source; the try/except is defensive-only.
    silent_vs_explicit: |
      SILENT — bare `except Exception: pass`. On exception the
      displacement is NOT filtered by regime_time — it enters the
      same-direction regime-disp pool as though the time check
      passed.
    methodology_adjacency: HIGH
    notes: |
      Affects which displacement becomes regime_disp (fed to
      origin/extreme derivation). Consequence on exception:
      displacement preceding the regime establishment may be chosen
      as the regime-leg displacement — INV-PDA-DIRECTION-FIDELITY
      upstream semantic analog.

  - site: en1gma/console/map/map_engine.py:340-341
    name: FB03_regime_disp_last_displacement_fallback
    current_shape: |
      if regime_disp is None:
          regime_disp = disp_events[-1]
    trigger_condition: |
      No displacement in disp_events passed both the same-direction
      filter (:323 `if d_dir != dir_str: continue`) and the regime-
      time filter (after FB02). Meaning: no displacement is both
      regime-direction-aligned AND post-regime-establishment.
    docstring_intent: |
      No docstring on the branch. Semantic: "if no regime-aligned
      displacement exists, fall back to the last displacement in
      the series regardless of direction."
    silent_vs_explicit: |
      SILENT — no log, no flag. The fallback regime_disp feeds
      `_find_origin_before_displacement` + `_find_displacement_
      extreme` as though it were regime-aligned.
    methodology_adjacency: HIGH
    notes: |
      Counter-direction displacement driving DR derivation. Olya
      ruling required: is this acceptable cold-start bootstrap, or
      should Map init halt with explicit "no regime-aligned
      displacement in window" error?

  - site: en1gma/console/map/map_engine.py:402-403
    name: FB04_pullback_bars_tail5_fallback
    current_shape: |
      if pullback_bars.empty:
          pullback_bars = daily_bars[before_mask].tail(5)
    trigger_condition: |
      Anchor-based pullback window (between prior same-direction
      displacement and current displacement) yields zero bars, OR
      anchor_ts is None and before_mask yields a window that the
      anchor_ts filter did not populate.
    docstring_intent: |
      Function docstring (:367 `_find_origin_before_displacement`):
      "Scoped to the pullback window, NOT the full pre-displacement
      range." The tail(5) fallback contradicts that scoping intent.
    silent_vs_explicit: |
      SILENT — no log. Last-5-bars substitute for a methodology-
      calibrated pullback window.
    methodology_adjacency: HIGH
    notes: |
      Affects Map origin (DR origin_price). Olya calibrated Q3/Q4
      against "pullback peak before displacement" — the tail(5)
      substitute has no methodology grounding.

  - site: en1gma/console/map/map_engine.py:404-405
    name: FB05_pullback_bars_head_half_fallback
    current_shape: |
      if pullback_bars.empty:
          pullback_bars = daily_bars.head(max(1, len(daily_bars) // 2))
    trigger_condition: |
      FB04's tail(5) substitute also yields empty (rare — requires
      before_mask window shorter than 5 bars). E.g., trade date
      near start of available data.
    docstring_intent: |
      No docstring — inherits same function context as FB04.
    silent_vs_explicit: SILENT — no log, no flag.
    methodology_adjacency: HIGH
    notes: |
      Nested fallback-of-fallback. Uses first half of daily_bars
      regardless of regime or anchor. Extreme cold-start path.

  - site: en1gma/console/map/map_engine.py:438-451
    name: FB06_extreme_candle_zero_wick_fallback
    current_shape: |
      ext_candle = disp_event.properties.get("extreme_candle", {})
      if direction == "bearish":
          extreme = float(ext_candle.get("wick_low", 0.0))
      else:
          extreme = float(ext_candle.get("wick_high", 0.0))

      if extreme == 0.0:
          col = daily_bars["timestamp_ny"]
          disp_ts = self._align_ts(disp_event.time, col)
          post = daily_bars[col >= disp_ts]
          if post.empty:
              post = daily_bars.tail(1)
          return float(post["low"].min()) if direction == "bearish" \
                 else float(post["high"].max())
    trigger_condition: |
      detect.py displacement event omits `extreme_candle` or its
      wick_high/wick_low sub-keys. When present, value is 0.0.
      Production ra_engine always emits these keys (per
      displacement.py emission); gap arises if a detector variant,
      legacy trace, or corrupted properties dict is consumed.
    docstring_intent: |
      Function docstring (:423 `_find_displacement_extreme`):
      "Starts from the displacement event's own extreme candle
      wick." No documented fallback semantic. The `extreme == 0.0`
      branch is undocumented.
    silent_vs_explicit: |
      SILENT — no log on either the missing-key path or the
      extreme==0.0 branch. Fallback substitutes a post-disp
      wick-min/max (or last-bar min/max via `post.empty`).
    methodology_adjacency: HIGH
    notes: |
      Affects DR extreme_price. A legitimate zero-price wick is
      impossible in EUR/USD (prices are O(1.0)), so extreme==0.0
      uniquely signals missing-property. SW32 sibling (silent-
      upgrade-via-dict.get pattern class). Also note the hardcoded
      PIP-free comparison (`== 0.0`) works only because no real
      wick price is zero.

  - site: en1gma/console/map/map_engine.py:448
    name: FB07_post_empty_tail1_fallback
    current_shape: |
      if post.empty:
          post = daily_bars.tail(1)
    trigger_condition: |
      Nested fallback under FB06. Disp_ts is after the final bar in
      daily_bars, so no bars are "post-disp."
    docstring_intent: No docstring on the branch.
    silent_vs_explicit: SILENT.
    methodology_adjacency: HIGH
    notes: |
      Last-bar wick substitute for extreme. Combined with FB06, the
      chain of fallbacks can take DR extreme from a tail(1) wick
      under worst-case compound conditions.

  - site: en1gma/console/map/map_engine.py:457-458
    name: FB08_after_cluster_empty_early_return
    current_shape: |
      if after_cluster.empty:
          return extreme
    trigger_condition: |
      No bars exist after `end_time` (displacement cluster end) in
      daily_bars. Trade date = the most recent available daily bar.
    docstring_intent: |
      Implicit: "no forward bars to scan for extension, return the
      cluster-derived extreme as-is." Not explicitly documented.
    silent_vs_explicit: |
      EXPLICIT early return with methodology-plausible semantic
      (cluster extreme IS a valid endpoint for a same-session
      leg). But SILENT in the observability sense — no log.
    methodology_adjacency: MEDIUM
    notes: |
      Unlike FB04-07 this one returns a methodology-defensible
      value (the displacement cluster's own extreme). Olya ruling
      may accept this as cold-start. Flagged for completeness.

  - site: en1gma/console/map/map_engine.py:460
    name: FB09_atr_value_default_50pips_silent_upgrade
    current_shape: |
      atr_value = disp_event.properties.get("atr_value", 50.0) * PIP
    trigger_condition: |
      displacement event omits `atr_value` property. Production
      ra_engine emits it on every STRONG/VALID/WEAK-graded
      displacement; gap arises via legacy traces or variant
      detectors.
    docstring_intent: |
      No docstring marker on this line. Used in
      `pullback_threshold = max(5.0 * PIP, 0.25 * atr_value)`
      within _find_displacement_extreme.
    silent_vs_explicit: |
      SILENT — a semantic-grade default. 50 pips is a large ATR
      (EURUSD daily typical ATR 30-60 pips); pullback_threshold
      becomes max(5, 12.5) = 12.5 pips regardless of actual
      volatility. This IS the SW32 silent-upgrade-via-dict.get
      anti-pattern class, inside map_engine.py scope (Block 2
      audit report flagged this specific line as AMBIGUOUS; §11
      silent_upgrade_discipline applies).
    methodology_adjacency: MEDIUM
    notes: |
      Affects whether forward-scanning for extreme terminates on
      pullback (0.25 * atr_value pullback threshold). Sibling of
      SW32 confirmed instances in mss.py + chain_evaluator.py.

  - site: en1gma/console/map/map_engine.py:505-513
    name: FB10_h4_regime_time_timestamp_compare_swallow
    current_shape: |
      try:
          d_end = d.properties.get("time_end", d.time)
          d_ts = pd.Timestamp(d_end)
          r_ts = pd.Timestamp(regime_time)
          if d_ts.tz is None and r_ts.tz is not None:
              d_ts = d_ts.tz_localize(r_ts.tz)
          if d_ts < r_ts:
              continue
      except Exception:
          pass
    trigger_condition: Same as FB02 but inside _compute_h4_dealing_range.
    docstring_intent: No docstring on the branch.
    silent_vs_explicit: SILENT — identical pattern to FB02.
    methodology_adjacency: HIGH
    notes: |
      H4 variant of FB02. INV-HTF-INCLUDES-CASCADE-PAIR guarantees
      4H is always present; cascade activation (daily invalid →
      H4) threads through this path. Failure mode parallels FB02.

  - site: en1gma/console/map/map_engine.py:517-522
    name: FB11_h4_regime_disp_same_dir_fallback
    current_shape: |
      if same_dir_post_regime:
          regime_disp = same_dir_post_regime[-1]
      else:
          same_dir = [d for d in disp_events if d.direction == dir_str]
          if same_dir:
              regime_disp = same_dir[-1]
          else:
              return None
    trigger_condition: |
      No same-direction displacement post regime_time in H4 data.
      Falls back to last same-direction displacement (any time).
      If none, returns None → caller (initialize) skips H4 cascade
      and stamps authority_tf = "DAILY".
    docstring_intent: No docstring on the branch.
    silent_vs_explicit: |
      HYBRID — the `return None` leaf is methodology-defensible
      (no H4-grade leg found, defer to daily). The
      `same_dir[-1]` branch is SILENT (ignores regime_time).
    methodology_adjacency: HIGH
    notes: |
      H4 analog of FB03 but with explicit None terminal. Olya
      ruling may separate the two branches: (a) last same-dir
      (accept / fail-closed / log) vs (b) return None (accept).

  - site: en1gma/console/map/map_engine.py:565-566
    name: FB12_pda_init_dr_none_early_return
    current_shape: |
      if self._dealing_range.current is None:
          return
    trigger_condition: |
      `_initialize_pdas_from_detections` called with no DR
      established (e.g., FB01-FB11 chain bottomed out or
      `_initialize_dealing_range_from_detections` returned without
      creating DR).
    docstring_intent: |
      Function docstring (:549) mentions SW04 direction + zone
      fidelity invariants; does NOT document "no DR → skip PDA
      creation" semantic.
    silent_vs_explicit: |
      SILENT — no PDAs created, caller has no signal. MapState
      emerges with regime + DR but zero active_pdas; gate
      evaluates DISARMED (NO_ACTIVE_PDA) on every bar.
    methodology_adjacency: MEDIUM
    notes: |
      Downstream effect is observable (DISARMED reason is logged)
      but upstream cause (no DR) is not surfaced. SW47 F1
      construction_mode scaffold would fire here if FB01-FB11
      produced FALLBACK mode.

  - site: en1gma/console/map/map_engine.py:572-573
    name: FB13_fvg_results_missing_per_tf_skip
    current_shape: |
      fvg_dr = results.get("fvg", {}).get(tf_key)
      if not fvg_dr:
          continue
    trigger_condition: |
      detect.py results dict has no "fvg" key, or no entry for a
      given TF (e.g., "1D" or "4H"). Production pipeline always
      populates these; gap surfaces with non-standard detection
      input or missing aggregated bars for that TF.
    docstring_intent: Implicit: "no FVGs emitted on this TF, skip."
    silent_vs_explicit: |
      SILENT skip — but this is arguably the RIGHT policy (no data
      → no PDAs for that TF). Less suspect than other fallbacks.
    methodology_adjacency: MEDIUM
    notes: |
      Flagged for completeness. Compound with FB12 — both paths
      end with "zero PDAs created" under different triggers.

  - site: en1gma/console/map/map_engine.py:576-582
    name: FB14_pda_init_malformed_fvg_debug_skip
    current_shape: |
      try:
          fields = _pda_fields_from_detection(fvg)
      except ValueError as exc:
          log.debug(
              "SW04 skip malformed FVG detection tf=%s id=%s: %s",
              tf_key, getattr(fvg, "id", "?"), exc,
          )
          continue
    trigger_condition: |
      A detected FVG has malformed properties: missing top/bottom,
      non-numeric gap_pips, zone_top <= zone_bottom, unknown
      direction string. Caught at SW04 validation layer.
    docstring_intent: |
      Function docstring (:549): "Malformed detections are logged
      at DEBUG and skipped (D5 hybrid policy)". EXPLICITLY
      documented.
    silent_vs_explicit: |
      EXPLICIT — named D5 hybrid policy (fail-fast in test via
      pure-helper call; log+skip in production). log.debug not
      log.warning means operators usually don't see these.
    methodology_adjacency: MEDIUM
    notes: |
      Intentional post-SW04 design. Question for Olya: is a rash
      of D5-skips a map-validity concern (if N FVGs get dropped,
      how many remaining PDAs is "enough"?) or is count-
      independent arming the intended semantic?

  - site: en1gma/console/map/map_engine.py:621-630
    name: FB15_replay_price_forward_timestamp_compare_swallow
    current_shape: |
      try:
          pda_ts = pd.Timestamp(pda.created_at)
          bar_ts = pd.Timestamp(bar_time)
          if pda_ts.tz is not None and bar_ts.tz is None:
              bar_ts = bar_ts.tz_localize(pda_ts.tz)
          elif pda_ts.tz is None and bar_ts.tz is not None:
              pda_ts = pda_ts.tz_localize(bar_ts.tz)
          if bar_ts <= pda_ts:
              continue
      except Exception:
          pass
    trigger_condition: |
      Any exception comparing PDA.created_at to bar.timestamp_ny
      in _replay_price_forward's per-bar, per-PDA loop.
    docstring_intent: |
      Function docstring (:593 _replay_price_forward): "Only
      processes bars AFTER each PDA's creation time." Does not
      document exception semantic.
    silent_vs_explicit: |
      SILENT — `except Exception: pass`. On exception, the bar
      IS processed (creation-time guard is silently dropped) —
      PDA can be retroactively mitigated by bars preceding its
      creation.
    methodology_adjacency: HIGH
    notes: |
      INV-PDA-CREATED-AT-CONFIRMATION protection bypass on
      exception. Sibling of FB02 + FB10 (same try/except pattern).
      INV-DETECTION-TIME-TZ-AWARE (SW24) source-side guarantee
      makes this defensive-only in production.

count_summary:
  total_enumerated: 15
  methodology_adjacency_HIGH: 10  # FB01, FB02, FB03, FB04, FB05, FB06, FB07, FB10, FB11, FB15
  methodology_adjacency_MEDIUM: 4  # FB08, FB09, FB12, FB13, FB14
  methodology_adjacency_LOW: 0
  silent_vs_explicit_SILENT: 11   # FB01(labelled-but-silent), FB02, FB03, FB04, FB05, FB06, FB07, FB09, FB12, FB13, FB15
  silent_vs_explicit_EXPLICIT: 3  # FB01(label), FB08, FB14
  silent_vs_explicit_HYBRID: 1    # FB11

clustering_hints_for_cto:
  A_zero_input_bootstrap:
    members: [FB01, FB12, FB13]
    semantic: "no structural input → use permissive default"
    olya_question_shape: "is this acceptable cold-start, or halt?"
  B_tz_timestamp_swallow:
    members: [FB02, FB10, FB15]
    semantic: "except Exception: pass on tz/timestamp compare"
    olya_question_shape: "INV-DETECTION-TIME-TZ-AWARE (SW24)
                         upstream guarantee — is defensive
                         swallow still needed?"
    candidate_resolution: "replace with specific TypeError /
                         ValueError narrow catch + log.warning"
  C_regime_direction_fallback:
    members: [FB03, FB11]
    semantic: "no regime-aligned displacement → last displacement
              (FB03) or return None (FB11 terminal)"
    olya_question_shape: "is counter-direction displacement an
                         acceptable DR-leg source?"
  D_pullback_substitute:
    members: [FB04, FB05]
    semantic: "tail(5) or head(half) pullback substitute when
              anchor window empty"
    olya_question_shape: "methodology-calibrated substitute vs
                         halt?"
  E_missing_property_default:
    members: [FB06, FB07, FB09]
    semantic: "properties.get with semantic-grade default (0.0
              wick, 50-pip ATR)"
    olya_question_shape: "SW32 sibling — silent_upgrade_discipline
                         (CLAUDE.md §11) anti-pattern application?"
  F_defensible_early_return:
    members: [FB08, FB11.terminal, FB14]
    semantic: "explicitly-documented or semantically-defensible
              short-circuit"
    olya_question_shape: "keep as-is with invariant declaration?"
```

---

## T2 — P5 Day State Causal Linkage

```yaml
target: en1gma/console/map/day_state.py::_check_expansion_delivered
        + _find_aligned_event

current_code:
  file: en1gma/console/map/day_state.py
  function: _check_expansion_delivered
  line_range: 182-218
  excerpt: |
    def _check_expansion_delivered(
        self,
        htf_detections: dict[str, dict[str, Any]],
    ) -> DayStateTransition | None:
        """Look for aligned displacement + MSS at or above authority TF."""
        transition_tf = self._resolve_transition_tf()
        tf_key = _TF_KEY_MAP.get(transition_tf)
        if tf_key is None:
            return None

        dir_str = _DIRECTION_MAP.get(self._regime_direction)
        if dir_str is None:
            return None

        eligible_tf_keys = self._eligible_tf_keys(transition_tf)

        disp_id = self._find_aligned_event(
            htf_detections, "displacement", dir_str, eligible_tf_keys,
        )
        if disp_id is None:
            return None

        mss_id = self._find_aligned_event(
            htf_detections, "mss", dir_str, eligible_tf_keys,
        )
        if mss_id is None:
            return None

        return DayStateTransition(
            from_state=DayState.PRE_EXPANSION,
            to_state=DayState.POST_EXPANSION,
            trigger_displacement_id=disp_id,
            trigger_mss_id=mss_id,
            authority_tf=transition_tf.value,
            regime_direction=self._regime_direction.value,
        )

adjacent_helpers:
  file: en1gma/console/map/day_state.py
  function: _find_aligned_event
  line_range: 235-251
  excerpt: |
    @staticmethod
    def _find_aligned_event(
        detections: dict[str, dict[str, Any]],
        primitive: str,
        direction: str,
        eligible_tf_keys: list[str],
    ) -> str | None:
        """Find first detection of a primitive aligned with direction at eligible TFs."""
        prim_results = detections.get(primitive, {})
        for tf_key in eligible_tf_keys:
            result = prim_results.get(tf_key)
            if result is None:
                continue
            dets = getattr(result, "detections", [])
            for det in dets:
                if getattr(det, "direction", None) == direction:
                    return getattr(det, "id", "unknown")
        return None

current_shape_description: |
  Displacement + MSS are matched INDEPENDENTLY. Each _find_aligned_
  event call scans its primitive over eligible TF keys (authority TF
  and above) and returns the FIRST detection whose direction matches
  the regime direction, ignoring:
    - temporal order (displacement before MSS? no check)
    - same TF (displacement on 4H + MSS on 1D both count as "aligned")
    - time-window constraint (displacement from 10 days ago + MSS
      today both count)
    - bar-distance constraint (no "MSS within N bars of displacement")
    - causal linkage (no check that MSS consumed the displacement's
      structural swing break)
  Any two direction-aligned events at or above authority TF trigger
  the transition — potentially from unrelated structural episodes.

adjacent_semantics:
  allowed_tfs:
    logic: |
      _eligible_tf_keys(min_tf) returns all TFs at or ABOVE min_tf
      via _TF_RANK {H1:0, H4:1, DAILY:2}. authority_tf=H4 →
      eligible={H4, DAILY}. authority_tf=DAILY → eligible={DAILY}.
    site: day_state.py:228-234 (_eligible_tf_keys)
    invariant_protection: |
      INV-DAY-STATE-MARKET-DRIVEN satisfied (only detected-event
      triggers). INV-DAY-STATE-MAP-COHERENT (v1.0.1) constrains
      derivation pipeline — same detection pipeline as regime + DR
      — also satisfied (same `htf_detections` source).
  direction_matching_logic:
    direction_map: day_state.py:52-55 (_DIRECTION_MAP)
      MarketDirection.BULLISH → "bullish"
      MarketDirection.BEARISH → "bearish"
    comparison: `getattr(det, "direction", None) == direction` (:249)
    neutral_regime_behavior: |
      `dir_str is None` branch returns None early (:195), so NEUTRAL
      regime never transitions day_state.
  time_window_bar_distance_semantics:
    NONE — no time filtering anywhere in _check_expansion_delivered
      or _find_aligned_event. htf_detections is session-window-
      filtered upstream by caller (orchestrator feeds
      `session_detections = _filter_detections_in_time_window(...)`
      at session.py:515 — filters to [forex_day_start_ny, bar.ny]
      window). So matching is bounded to "detections emitted today
      by the time of the current bar" but NOT narrowed within that
      window.

ground_truth_references:
  test_fixture_files:
    - path: en1gma/tests/console/map/test_day_state.py
      scope: DayStateEngine unit behavior
      hits: |
        :99  test_transition_on_aligned_displacement_mss (positive case)
        :106 test_no_transition_on_counter_displacement
        :114 test_no_transition_on_displacement_without_mss
        :120 test_no_transition_on_mss_without_displacement
        :128 test_transition_idempotent
        :89  test_init_with_prior_expansion
      fixture_helper: _make_htf_detections(disp_dir, mss_dir,
                     disp_tf, mss_tf, include_disp, include_mss,
                     disp_id="disp_1D_001", mss_id="mss_1D_001")
      description: |
        Synthetic detection dicts constructed in-test. Each test
        primitive is a single-element detections list with
        hardcoded ID. No time field on synthetic detections, so
        existing tests do NOT exercise temporal ordering (they
        couldn't reveal the causal-linkage gap).
    - path: en1gma/tests/integration/test_day_state_wiring.py
      scope: end-to-end wiring — process_detections called per bar
      hits: |
        :5   G1_SW03_WIRED contract docstring
        :92  day_state_engine.process_detections(session_detections)
        :167 G1: process_detections called per bar (unit reproduction)
        :175-193 monkey-patched DayStateEngine.process_detections spy
        :307-331 G1 integration — run_map_replay invocation path spy
      description: |
        Asserts process_detections is invoked at the right cadence.
        Does NOT assert semantic properties of a "valid" transition
        beyond "fires when helper returns transition object."

  shipped_ground_truth_trade_files_exercising_day_state:
    - traces/ground_truth/trade_001/decision_trace.jsonl
      (Oct 1 2025 — daily BEARISH, EXPANSION phase)
    - traces/ground_truth/trade_003/decision_trace.jsonl
      (Dec 12 2025 — daily BULLISH, EXPANSION phase)
    - traces/ground_truth/trade_005/decision_trace.jsonl
      (Dec 12 2025 — BULLISH)
    - traces/ground_truth/trade_006/decision_trace.jsonl
      (Dec 15 2025 — BULLISH EXPANSION)
    - traces/ground_truth/trade_007/decision_trace.jsonl
      (Sep 16 2025 — BULLISH CONTINUATION)
    - traces/ground_truth/trade_013/decision_trace.jsonl
      (Mar 12 2026 — BEARISH EXPANSION)
    note: |
      All 6 shipped ground-truth trades are EXPANSION or
      CONTINUATION under daily authority. None exercise RETRACE
      or RANGE semantics. Counter-example trade hunt (CTO P5
      next step) would target: (a) a trade date where
      displacement and MSS align in direction but are from
      unrelated structural episodes, (b) a trade date where
      correctly causally-linked displacement+MSS pair is
      distinct from the first-seen pair returned today.
```

---

## T3 — SW27 FVG Initial Guard

```yaml
sw_id: SW27
registered: 2026-04-21 (formal registration per §11 finding_id_discipline
            after placeholder-reference collision resolution)
block: audit-hold
severity: MEDIUM
status_today: HELD pending Olya ruling (per 2026-04-20 audit-hold posture;
              CTO + G + Opus concurrence)

queued_framing_verbatim: |
  (CLAUDE.md §15 block_2_status SW27 entry, 2026-04-21)

  "FVG initial guard — temporal evaluation semantic. Methodology
  question surfaced via the 2026-04-17 sweep analysis: should the
  first FVG observed after a sweep/MSS be treated as a valid
  chain step, or does the methodology require a guard window
  (N bars, or confirmation of displacement quality) before the
  first FVG is eligible? Today's chain evaluator treats any FVG
  matching the primitives as eligible — no guard.

  Severity: MEDIUM (methodology-universal — affects every Map-
  gated cartridge using OTE/FVG).
  Block: audit-hold (HELD pending fresh-eyes architectural audit
  per 2026-04-20 ruling).
  Correctness impact today: NONE demonstrable on 6/6 ground truth
  (those trades do not stress the guard window). Future risk:
  pattern-matching across a larger ground-truth set may surface
  trades where the first FVG was Olya-invalid but chain-valid.
  Classification: scope console, effect methodology.
  Authority: Olya ruling required on guard semantic before Phase 4
  drift work lands."

affected_code_sites:
  primary:
    - path: en1gma/console/chain/chain_evaluator.py
      function: _match_fvg
      line_range: 382-435
      current_semantic: |
        Step 3 of the fixed SWEEP→MSS→FVG→OTE sequence. Scans
        fvg detections at LTF (15m + 5m per cartridge), accepts
        any detection satisfying:
          (1) det.direction == trade_dir
          (2) det.time >= mss.time (temporal monotonicity only)
          (3) det.time <= current_bar_time (no future leak)
          (4) det.type == "fvg"
          (5) det.properties["gap_pips"] >= cfg.fvg_min_size_pips
        Among all candidates, selects BEST by largest gap_pips
        (:422 `if gap_pips > best_gap: best_gap = gap_pips`).
        NO guard window: an FVG detected 1 bar after MSS is as
        eligible as one detected 10 bars later.
    - path: en1gma/console/chain/chain_config.py
      class: ChainConfig
      field: fvg_min_size_pips  # per-cartridge size threshold only
      absence: |
        No `fvg_initial_guard_bars` field. No
        `fvg_require_displacement_confirmed` flag. No guard
        mechanism exists in the config surface today.
  adjacent:
    - path: en1gma/console/detection/ra_engine/detectors/fvg.py
      note: |
        FVG detector emits candidates based on 3-candle wick-pattern
        algorithm. Each emitted FVG is a "candidate" from
        detection's view; chain_evaluator is the consumer that
        decides "eligible to arm."

current_behavior_without_guard:
  6_of_6_ground_truth_behavior: |
    CLAUDE.md: "Correctness impact today: NONE demonstrable on
    6/6 ground truth." The trace files (traces/ground_truth/
    trade_*/chain_trace.jsonl) show chain_complete=0 on all 6
    today (gate arms but chain fails at OTE step, not FVG). Olya
    verification posture was that with correct Map authority
    (post-phase_3_4) the 6/6 would chain-complete; today the
    bottleneck is OTE reach, not FVG guard.
  dispatch_flow_on_first_fvg: |
    chain_evaluator.evaluate (:108-288) runs the 4 steps
    sequentially. On MSS match (step 2), the next bar's re-entry
    to evaluate calls _match_fvg (step 3). If an FVG exists with
    time > mss.time matching direction and gap > min size, it
    becomes the best candidate. OTE check follows immediately.
  failure_mode_if_guard_needed: |
    Scenario — an immediate-post-MSS FVG that is methodology-
    invalid (e.g., same-bar wick artifact, not a structurally
    confirmed imbalance) arms the chain. Today's runtime enters
    OTE check on this FVG; if OTE zone is also reached, trade
    is placed. Olya's concern (per SW27 framing): "the first FVG
    observed" may not be the "methodology-valid first FVG" —
    some initial print-activity is noise pre-displacement-
    confirmation.

relationship_to_siblings:
  SW31_displacement_quality:
    note: |
      SW27 (temporal guard) and SW31 (grade filter) are
      methodology-fidelity siblings. Both land via
      `_match_fvg` / upstream MSS quality gate. If Olya rules
      "SW31 minimum VALID grade → MSS must be VALID-backed",
      that partially narrows the SW27 surface (the MSS-pre-
      requisite becomes tighter). CTO may choose to frame
      both as one cluster.
  SW32_silent_upgrade_class:
    note: |
      SW32 identified the engineering anti-pattern class
      (dict.get with semantic-grade default). Its instances
      at mss.py:284/364 + chain_evaluator.py:356 affect how
      grade data flows into FVG match. Not itself an Olya
      ruling item (engineering discipline), but the fix path
      couples with SW31 if the chosen grade-filter semantic
      relies on quality_grade presence.

authority_for_ruling: Olya (methodology)
  cited_in_CLAUDE.md: §15 SW27 "Authority: Olya ruling required"
```

---

## T4 — SW31 Displacement Quality Threshold

```yaml
sw_id: SW31
registered: 2026-04-21 via Phase 2.5 Brief 2 §B2 audit
            (docs/findings/PHASE_2_5_AUDIT_REPORT.md §B2.2-§B2.3)
block: 2  # methodology-held pending Olya ruling
severity: MEDIUM
status_today: REGISTERED — methodology ruling required

queued_framing_verbatim: |
  (CLAUDE.md §15 block_2_status SW31 entry, registered 2026-04-21)

  "Displacement quality methodology-fidelity gap. Surfaced
  2026-04-21 evening via Phase 2.5 Brief 2 §B2 audit
  (docs/findings/PHASE_2_5_AUDIT_REPORT.md §B2.2 + §B2.3).

  Context: Olya methodology ruling 2026-04-21 included the edge
  case 'If expansion lacks real displacement, Olya does NOT
  mentally upgrade to POST_EXPANSION. day_state depends on VALID
  expansion, not just any MSS print.' INV-DAY-STATE-MAP-COHERENT
  registered in parallel.

  B2 audit finding on the coherence axis: OUTCOME NULL — Map
  (regime.update_on_mss + dealing_range.is_daily_range_valid) and
  day_state (DayStateEngine._find_aligned_event) BOTH consume the
  same detection results from run_detection() and BOTH filter
  purely by direction match. Identical upstream source, identical
  filter logic, no per-consumer quality threshold. They move in
  lock-step. INV-DAY-STATE-MAP-COHERENT confirmed as forward-
  looking protection (no violation today).

  B2 adjacent finding (separate from the coherence question):
  the displacement detector emits grade-tagged candidates
  (STRONG >=2.0x ATR / VALID >=1.5x / WEAK >=1.25x / None <1.25x)
  and passes any candidate through the loosest OR gate (atr>=1.0
  OR body_ratio>=0.55). Downstream consumers (Map + day_state)
  apply NO additional quality filter. Therefore a WEAK-graded or
  None-graded displacement can drive both day_state to
  POST_EXPANSION and Map's dealing-range invalidation, even
  though Olya's methodology uses 'VALID expansion' language.
  This is a consumer-shared gap, not a Map-vs-day_state
  divergence.

  Severity: MEDIUM. Class: methodology-fidelity.
  Correctness impact today: UNKNOWN — depends on Olya's ruling
  on whether 'VALID expansion' is a strict >=VALID grade filter
  or a looser conceptual description. 6/6 ground truth trades
  unaffected today (all STRONG-graded events).
  Block: 2 (methodology-held pending Olya ruling). Parallels
  SW27 (FVG initial guard) as a methodology-fidelity question.
  Classification: scope console, effect methodology.
  Authority: Olya ruling required. If VALID-minimum confirmed,
  fix is console-level: add grade filter to both consumers
  simultaneously (preserves INV-DAY-STATE-MAP-COHERENT). If
  current behavior ruled acceptable, document the semantic
  explicitly in MAP_SPATIAL_PRIMER and close SW31."

affected_code_sites:
  detector_grade_emission:
    - path: en1gma/console/detection/ra_engine/detectors/displacement.py
      function: _quality_grade
      line_range: 79-93
      excerpt: |
        def _quality_grade(atr_ratio: float) -> Optional[str]:
            """Assign quality grade based on ATR ratio.
            STRONG: >= 2.0x
            VALID:  >= 1.5x
            WEAK:   >= 1.25x
            None:   < 1.25x
            """
            if atr_ratio >= 2.0:
                return "STRONG"
            if atr_ratio >= 1.5:
                return "VALID"
            if atr_ratio >= 1.25:
                return "WEAK"
            return None
    - path: en1gma/console/detection/ra_engine/detectors/displacement.py
      line: 333 (grade = _quality_grade(used_atr))
      line: 424 (emission: "quality_grade": grade)
      semantic: |
        Displacement detector emits the grade tag on the detection.
        A None grade emits the key absent or explicit None
        depending on path.
    - path: en1gma/console/detection/ra_engine/detectors/displacement.py
      line: 503 (consumer-side read: `g = d["quality_grade"]`)
      context: downstream filter call site

  broader_or_gate_emission:
    note: |
      Per §B2.3 audit framing: displacement's final acceptance is
      the loosest of ATR>=1.0 OR body_ratio>=0.55. grade TAG is
      carried on ALL accepted candidates regardless of whether
      they would qualify as STRONG/VALID/WEAK/None.
    site: displacement.py (detector acceptance gate — precedes
          grade assignment)

  day_state_consumer_with_no_grade_filter:
    - path: en1gma/console/map/day_state.py
      function: _find_aligned_event
      line_range: 235-251
      context: |
        Scans `getattr(det, "direction", None) == direction` only.
        No access to det.properties["quality_grade"]. Accepts any
        detection that passed detector emission.

  map_consumer_with_no_grade_filter:
    - path: en1gma/console/map/map_engine.py
      function: _initialize_regime_from_detections
      line_range: 253-285
      context: |
        Similarly scans displacement events by direction only.
        For regime-derivation fallback (:279-285) picks the
        `max(disp_events, key=lambda d: d.properties.get(
        "range_pips", 0))` — sorts by size, NOT grade.

  dealing_range_daily_validity:
    - path: en1gma/console/map/dealing_range.py
      function: is_daily_range_valid
      context: |
        Downstream check consumed by MapEngine.initialize (:224)
        to decide whether daily DR is expanding (cascade to H4)
        or valid. Does not consult grade either.

  mss_silent_upgrade_sw32_sibling:
    - path: en1gma/console/detection/ra_engine/detectors/mss.py:284
      line: quality_grade → "VALID"  (bullish emission default)
    - path: en1gma/console/detection/ra_engine/detectors/mss.py:364
      line: quality_grade → "VALID"  (bearish emission default)
    - path: en1gma/console/chain/chain_evaluator.py:356
      line: quality_grade → "VALID"  (consumer nested fallback)
      semantic: |
        If grade key absent on an emitted detection, the
        consumer-side .get default upgrades to "VALID" silently.
        SW32 pattern class registered as engineering sibling of
        SW31 methodology question.

current_behavior_without_threshold:
  sequencing: |
    displacement detector emits (direction, atr_value,
    quality_grade, range_pips, ...) → Map + day_state filter by
    direction only → consumers apply no grade threshold → any
    accepted displacement (even WEAK or None) can drive both:
      (a) Map regime-derivation fallback (:279 max range_pips)
      (b) Map is_daily_range_valid check (dealing_range.py)
      (c) day_state PRE_EXPANSION → POST_EXPANSION transition
          (day_state.py:_check_expansion_delivered)
  6_of_6_ground_truth_behavior: |
    CLAUDE.md: "6/6 ground truth trades unaffected today (all
    STRONG-graded events)." Current production pattern does not
    exercise the gap — all 6 annotated EXPANSION trades have
    STRONG-graded displacement upstream.
  future_risk: |
    CLAUDE.md: "if a WEAK-graded or None-graded displacement
    enters production detection, it drives day_state transition
    + Map regime-fallback unchecked."
  coherence_property_today: |
    INV-DAY-STATE-MAP-COHERENT (v1.0.1) is NOT violated — both
    consumers behave the same way (both filter on direction
    only). The invariant protects against Map + day_state
    drifting from each other; it does not ensure either one is
    methodology-correct.

relationship_to_siblings:
  SW27_fvg_guard:
    overlap: |
      Both are methodology-fidelity asks on chain/day_state inputs.
      If Olya rules SW31 requires >=VALID grade filter, SW27 asks
      what happens after the grade-qualified MSS. Cluster-able
      but logically independent rulings.
  SW32_engineering_sibling:
    note: |
      SW32 registered 2026-04-21 as the pattern class (silent-
      upgrade-via-dict.get). Its 5 confirmed instances all occur
      at grade-flow sites. If SW31 ruling makes grade load-bearing,
      SW32 remediation (replace silent defaults with explicit
      weak-bucket / presence check) becomes prerequisite.

authority_for_ruling: Olya (methodology — "VALID expansion" semantic)
  cited_in_CLAUDE.md: §15 SW31 "Authority: Olya ruling required"
```

---

## T5 — F2.2 Shape 2: Cross-Path Event Overlap

```yaml
target: event types observed by both ARS canon runner + Map canon runner
method:
  - enumerate ARS canon's detection consumption sites + emitted trace events
  - enumerate Map canon's detection consumption sites + emitted trace events
  - partition observed events into
      DECISION fields (cross-path byte-identity REQUIRED per
        INV-DAEMON-REAL-TIME-SCOPE applied across paths)
      OBSERVATIONAL metadata (divergence permitted w/ invariant rationale)
      AMBIGUOUS (methodology ruling required)

scope_framing:
  related_invariants:
    INV-DAEMON-REAL-TIME-SCOPE:
      established: SW38 2026-04-22
      scope: within-ARS three-path (batch / advance / daemon)
      cross_path_applicability_today: NOT EXTENDED —
        "does NOT extend to cross-cartridge path comparison"
        per 2026-04-26 phase_4a_verification_pass T6
    DEC-ARS-BYPASSES-MAP:
      established: phase_3_2 D1
      scope: |
        ARS deliberately produces different decision surface than
        Map on the same date. Cross-path decision-field byte-
        identity is NOT expected today.
    INV-DETECTION-AUTHORITY-SINGLETON:
      established: pre-Phase-3
      scope: |
        detect.py is sole detection emitter. Does NOT today
        promise "output invariant regardless of caller" — only
        "no other module generates detections." Proposed
        tightening to INV-DETECTION-CALLER-INVARIANT is T6
        Shape 1 from 2026-04-26 verification pass.
  2026_04_26_verification_pass_T6_ruling:
    shape_1_caller_invariant_detection:
      disposition: RECOMMENDED
      scope: detection output byte-identity across callers
      invariant_to_register: INV-DETECTION-CALLER-INVARIANT
    shape_2_trade_decision_nucleus:
      disposition: OUT_OF_SCOPE_without_methodology_ruling
      rationale: DEC-ARS-BYPASSES-MAP precludes byte-identity on
                  same-date decision nuclei
  this_task_scope_per_brief: |
    BRIEF T5 asks "event types observed by both ARS canon runner +
    Map canon runner" and "field classification". Enumeration
    only — no invariant declaration, no Olya-ruling-dependent
    shape assignment. CTO synthesizes options from the evidence.

ars_observed_event_types:
  emission_source: en1gma/console/chain/canon/ars/tracer.py
  emitted_record_types (from en1gma/console/chain/canon/ars/trace_schema.py):
    - SweepEvent (time_ny, direction, extension_pips, valid)
    - FvgScan (time_ny, direction, gap_pips, untouched_pips,
              candle_b_overlap, candle_c_inside, reacceptance,
              valid, rejection_reason)
    - TraceTradeRecord (direction, entry, sl, tp, rr, fvg_time_ny,
                        sweep_extreme, sweep_extension_pips)
    - TraceOutcome (result, r_value, exit_price, duration_minutes,
                    time_resolved)
    - ARSSessionRecord (umbrella — aggregates all above)
  raw_detection_consumption:
    5m_fvg:
      site: ars_canon.detect_fvg_on_5m
      note: |
        ARS uses a specialized FVG-matching routine (not detect.py's
        run_detection with primitive="fvg" at tf="5m"). Canonical
        ARS FVG-filter criteria (candle_b_overlap / candle_c_inside
        / reacceptance) are ARS-canon-specific beyond run_detection
        emission.
    asia_sweep_extension:
      site: ars_canon (asia-specific sweep tracking)
      note: |
        ARS tracks sweep extensions via its own asia-range logic,
        NOT via detect.py's liquidity_sweep primitive on 5m.
        Confirmed via 2026-04-26_phase_4a_verification_pass T6
        "ARS uses asia-sweep extension tracker, not detect.py's
        liquidity_sweep primitive on 5m."
    consumed_timeframes:
      - 1m (fixture backbone)
      - 5m (fvg watch)

map_observed_event_types:
  emission_source: |
    en1gma/console/chain/canon/map_canon/session.py::_run_map_session
    emits typed records via MapDecisionRecord.to_dict() +
    GateEvaluation.to_dict() + ChainEvaluation.to_dict() into
    decision_trace.jsonl + chain_trace.jsonl + map_timeline.jsonl.
  emitted_record_types (from en1gma/console/chain/canon/map_canon/trace_schema.py):
    - GateEvaluation (time, state, reason, direction, pda_ref, kz,
                     disarm_reasons)
    - ChainEvaluation (time, status, summary, steps, first_unsatisfied,
                       rejection_reason)
    - MapDecisionRecord (heterogeneous discriminated union —
        MAP_INIT_SKIPPED, MAP_INIT_FAILED, DAY_STATE_BLOCKED,
        DAY_STATE_TRANSITION, GATE_DISARMED, CHAIN_INCOMPLETE,
        GOVERNANCE_REJECTED, TRADE_APPROVED)
  emitted_map_timeline_events (from en1gma/observe/map_timeline.py):
    - REGIME_SET, REGIME_CHANGED
    - DEALING_RANGE_SET, DEALING_RANGE_SUPERSEDED
    - PDA_CREATED, PDA_TOUCHED, PDA_REJECTED, PDA_MITIGATED,
      PDA_INVALIDATED
    - GATE_ARMED, GATE_DISARMED
  raw_detection_consumption:
    htf_1D_4H:
      site: _init_map_for_date (session.py:305-356)
      primitives: fvg, mss, displacement (on 1D); fvg, mss,
                  displacement (on 4H — cascade-active)
    ltf_15m_5m:
      site: _run_map_session LTF window (session.py:614-636)
      primitives: sweep, mss, fvg, ote (via chain_evaluator)
    consumed_timeframes:
      - 1D (regime + DR + PDA init)
      - 4H (DR cascade + PDA init when INV-HTF-INCLUDES-CASCADE-PAIR)
      - 15m (chain evaluator)
      - 5m (chain evaluator)
      - 1m (LTF aggregation backbone)

overlap_set:
  detection_primitive_x_tf_intersection:
    - fvg_5m:
        ARS: detect_fvg_on_5m (ARS-canon-specialized)
        Map: chain_evaluator _match_fvg over ltf_tfs ["15m","5m"]
             consuming run_detection output
        overlap_kind: PARTIAL — both consume 5m FVG DATA (same
                      1m bars → same 5m aggregation → same FVG
                      events from detect.py), but ARS applies
                      canon-specialized filters (candle_b_overlap
                      / candle_c_inside / reacceptance) absent
                      from Map's chain_evaluator path
        note: |
          True raw-detection overlap at the run_detection(fvg, 5m)
          boundary IS the F2.2 Shape 1 "caller-invariant detection"
          question. Post-filter ARS vs Map outputs are NOT
          byte-equivalent even if the input detection set is.
  trade_decision_output_nucleus:
    shared_field_names: [direction, entry, sl, tp, rr]
    semantic_alignment: |
      ARS produces TraceTradeRecord(direction, entry, sl, tp, rr).
      Map produces CanonIntent → TradeIntent with (direction,
      entry_price, sl_price, tp_price, rr_ratio) via
      entry_spec_to_canon_intent + build_intent.
    byte_identity_expectation_on_same_date:
      NOT EXPECTED per DEC-ARS-BYPASSES-MAP — the two cartridges
      produce different strategies on the same input; same-date
      identity is an architectural contradiction, not a target.
  session_lifecycle_events:
    ARS_only:
      - session_start (ARSSessionRecord.session_id)
      - asia_range (asia_high/asia_low/asia_range_pips/asia_range_valid)
      - sweep_events (SweepEvent entries through sweep window)
      - fvg_scans (FvgScan entries through sweep window)
      - setup_found / rejection_reason
      - trade + outcome
    Map_only:
      - MAP_INIT_SKIPPED / MAP_INIT_FAILED (per-date map init)
      - DAY_STATE_BLOCKED / DAY_STATE_TRANSITION
      - GATE_DISARMED (per-bar, in kill zone)
      - CHAIN_INCOMPLETE
      - GOVERNANCE_REJECTED
      - TRADE_APPROVED + trade payload
      - PDA lifecycle (PDA_CREATED → TOUCHED/MITIGATED/REJECTED
        /INVALIDATED) via map_timeline.py
  governance_events:
    common_substrate: |
      Both paths call check_governance(mode, halt, lease,
      risk_state, risk_limits) per SW08 INV-GOVERNANCE-SINGLE-
      CHECK-SITE. Both emit governance rejection rationale.
    ARS_emission: TraceOutcome + halt_status/lease_status fields
    Map_emission: MapDecisionRecord(governance="REJECTED",
                  reason=..., blocker=...)
    field_name_overlap: halt_status, rejection_reason, blocker

decision_field_vs_observational_field_partition:
  decision_field_nucleus_across_paths (if cross-path parity were a goal):
    (direction, entry, sl, tp, rr): AMBIGUOUS
      rationale: |
        DEC-ARS-BYPASSES-MAP says cross-path byte-identity NOT
        expected on same date by design. Only a methodology
        ruling could carve a SUBSET of dates where parity is
        expected (e.g., "dates where ARS setup coincides with
        Map identifying same PDA as valid"). Shape 2 of F2.2
        remains ruling-gated per 2026-04-26 T6 verdict.
    governance_rejection_reason + blocker + halt_status:
      CROSS_PATH_INVARIANT: |
        SW08 single-check-site contract guarantees governance
        decisions are IDENTICAL under identical (mode, halt,
        lease, risk_state, risk_limits) input. If both paths
        see the same governance state, rejection nucleus MUST
        be byte-identical. This is a FACT of SW08, not a
        ruling-dependent claim. No cross-path test today
        enforces this — it is assert-able without Olya input.
  observational_metadata (path-specific, never expected identical):
    ARS_specific:
      - asia_high/asia_low/asia_range_pips/asia_range_valid
      - sweep_events list (ARS-specific session tracking)
      - fvg_scans list (ARS-canon FVG filter outcomes)
      - duration_minutes (SW36 fix — bar.ny-derived)
      - max_{high,low}_extension_pips (SW37-residual + SW38
        INV-DAEMON-REAL-TIME-SCOPE scope)
    Map_specific:
      - regime_direction
      - dealing_range_origin / dealing_range_extreme
      - pdas_active count
      - gate_evaluations / gate_armed_count
      - chain_evaluations / chain_complete_count
      - pda_ref, kz, disarm_reasons
      - authority_tf (DAILY vs H4 cascade)
  ambiguous_or_methodology_gated:
    run_detection(fvg, 5m) byte-identity across callers:
      disposition: F2.2 Shape 1 (RECOMMENDED in 2026-04-26
                   verification pass; new invariant
                   INV-DETECTION-CALLER-INVARIANT registerable
                   without methodology ruling)
    trade-decision nucleus byte-identity on overlapping dates:
      disposition: F2.2 Shape 2 (Olya-ruling-gated per
                   2026-04-26 T6)

current_parity_assertion_coverage:
  within_ARS:
    test_three_path_equivalence (en1gma/tests/cartridges/ars/):
      partitions TradeResult/SessionRecord fields:
        _TRADE_DECISION_FIELDS: 18 byte-identical REQUIRED
        _OBSERVATIONAL_METADATA_FIELDS: 3 xfail under
          INV-DAEMON-REAL-TIME-SCOPE
      scope: batch / advance / daemon within ARS — NOT cross-cartridge
    test_ars_parity: 151/151 session parity vs source repo
    test_ars_advance_canon_parity: 306 parametrized advance() cases
  within_Map:
    test_map_canon_runner_parity: run_map_replay ↔ direct
      MapCanonRunner.run(ctx) sha256 byte-identity on trade_001.
      Within-Map determinism only (not cross-ARS).
    test_daily_expansion_6_trade_parity: 6/6 ground truth replay
      byte-identity (scope: Map path vs committed reference traces;
      same-path determinism).
  cross_ARS_Map:
    explicit_search_via_2026_04_26_T6: |
      "grep for 'ARS.*Map|ars.*map|cross.path' across tests/:
      no cross-path harness"
    verdict: NONE — zero tests assert any cross-ARS-Map identity
             (neither on detection outputs nor trade-decision
             nuclei)

summary_for_cto_synthesis:
  deliverables_for_olya_prep:
    1: detection-level overlap (run_detection on same bars /
       same TF) — candidate for INV-DETECTION-CALLER-INVARIANT
       registration, NOT methodology-ruling-gated (Shape 1,
       CTO could formalize without Olya touch)
    2: trade-decision nucleus overlap — methodology-ruling-gated
       (Shape 2). Olya question: "should there be a subset of
       dates where we expect ARS and Map to agree on direction/
       entry/sl/tp?"
    3: governance rejection nucleus — ALREADY INVARIANT via SW08
       single-check-site; no ruling needed, test gap only
  what_is_NOT_this_task: |
    Assignment of either Shape 1 or Shape 2 as a Phase 4b scope
    item. This enumeration provides the evidence surface; CTO
    drafts the decision-table for Olya.
```

---

## T6 — Ground-Truth Trade Index

```yaml
target: methodology-relevant attribute indexing across ground-truth trade sets
purpose: |
  Enable CTO to counter-example-hunt against each decision option
  in the Olya prep pack. Enumeration only — no counter-example
  assignment.

source_sets:
  DAILY_EXPANSION_14_trades:
    path: en1gma/ground_truth/annotated_trades.yaml
    count: 14 (IDs trade_001 through trade_014)
    authority: Olya's hand-annotated methodology-assertive set
    scope: 2025-09-16 through 2026-03-17; mix of EXPANSION /
           RETRACE / INDEPENDENT / RANGE
    coverage_in_shipped_6_replay: trade_001 + 003 + 005 + 006 +
                                   007 + 013 have trace outputs
                                   under traces/ground_truth/*/
  ARS_151_trades:
    path: en1gma/tests/cartridges/ars/_canon_trade_dates.py
    count: 151 (CANON_TRADE_DATES tuple list)
    authority: ars_canon.process_session reproduction — parity
               contract vs source repo
    scope: 2021-04-07 through 2026-03-20 (5-year coverage;
           +54.02R walk-forward)
    coverage_in_replay: full 151/151 ARS session parity via
                        test_ars_parity + test_ars_advance_canon_parity
  shipped_replay_fixtures:
    path: en1gma/tests/integration/test_daily_expansion_6_trade_parity.py
    mapping (trade_id -> (start_date, end_date, min_gate_armed)):
      trade_001: (2025-09-15, 2025-10-05, 1930)
      trade_003: (2025-11-01, 2025-12-15, 714)
      trade_005: (2025-11-01, 2025-12-15, 714)
      trade_006: (2025-11-01, 2025-12-18, 714)
      trade_007: (2025-08-01, 2025-09-20, 245)
      trade_013: (2026-01-15, 2026-03-15, 927)
    replay_result_corpus: traces/ground_truth/all_6_results.json

DAILY_EXPANSION_trade_index:

  - id: trade_001
    date: 2025-10-01
    execution_time_ny: "03:30"
    direction: SHORT
    kill_zone: LOKZ
    htf_phase: EXPANSION
    day_state: PRE_EXPANSION  # transitions expected DURING this trade per SW03 wiring
    daily_direction: BEARISH
    authority_tf: Daily
    strategy_type: state_gated
    setup_type: REVERSAL
    entry_tf: 15m
    replay_shipped: true
    replay_summary_from_all_6_results: |
      regime=BEARISH origin=1.18199 extreme=1.16454 eq=1.17327
      pdas=19 gate_armed=1930 chain_complete=0 trades=0
      deepest: 3/4 steps at 2025-09-15T02:15:00 LOKZ (pre-trade-date
      gate arming on earlier date; OTE not reached)
    fallbacks_exercised_estimate: UNKNOWN (no instrumentation to trace
                                   which T1 FB* fires per replay)
    mixed_direction_PDA_in_zone: UNKNOWN (SW47 hazard relevance
                                 per COO_INPUTS §3.1 P1 — fixtures
                                 do not exercise the hazard)
    notes: |
      Only DAILY_EXPANSION trade where daily direction ≠ shipped-
      replay regime is 0 — BEARISH expansion, BEARISH regime.
      Kill-zone-realignment case (1H had bullish MSS 00:00; 15m
      bearish MSS 03:30 restores EXPANSION). Classic SW27 / SW31
      stress candidate if CTO wants to probe guard/grade around
      regime-realignment edges.

  - id: trade_002
    date: 2025-09-29
    execution_time_ny: "07:45"
    direction: LONG
    kill_zone: NYOKZ
    htf_phase: RETRACE
    day_state: N/A  # RETRACE is Phase-2+ cartridge (RETRACE_COUNTER) — PARKED
    daily_direction: BEARISH
    authority_tf: Daily
    strategy_type: state_gated
    setup_type: REVERSAL
    entry_tf: 15m
    replay_shipped: false  # not in the 6 replayed; RETRACE cartridge not shipped
    notes: |
      Uses SMT (DXY divergence) as sweep substitute — "Not in
      locked L1 — tolerated as known miss." Known methodology-
      scope-out case.

  - id: trade_003
    date: 2025-12-12
    execution_time_ny: "08:00"
    direction: LONG
    kill_zone: NYOKZ
    htf_phase: EXPANSION
    day_state: PRE_EXPANSION
    daily_direction: BULLISH
    authority_tf: Daily
    strategy_type: state_gated
    setup_type: REVERSAL
    entry_tf: 15m
    replay_shipped: true
    replay_summary_from_all_6_results: |
      regime=BULLISH origin=1.16152 extreme=1.17485 eq=1.16818
      pdas=11 gate_armed=714 chain_complete=0 trades=0
      deepest: 3/4 at 2025-11-19T04:10:00 LOKZ (OTE not reached)
    notes: |
      CORRECTED 2026-03-19: Olya confirmed daily BULLISH (was
      originally RANGE). Daily bullish MSS from Dec 4 + 4H bullish
      MSS Dec 10 with strong displacement. Classic "ATR warmup
      limitation" flag in Olya note — relevant for SW31 grade
      filter if daily MSS grade tag is absent due to ATR stage.

  - id: trade_004
    date: 2025-10-28
    execution_time_ny: "00:20"
    direction: SHORT
    kill_zone: N/A
    htf_phase: INDEPENDENT
    day_state: N/A
    daily_direction: NEUTRAL
    authority_tf: N/A
    strategy_type: asia_range_scalp
    setup_type: CONTINUATION
    entry_tf: 5m
    replay_shipped: false
    notes: |
      Asia Range Scalp — bypasses HTF phase entirely (ARS-sibling
      cartridge by design). Not Map-relevant for Olya methodology
      questions.

  - id: trade_005
    date: 2025-12-12  # SAME DATE AS trade_003 (different intraday setup)
    execution_time_ny: "09:00"
    direction: LONG
    kill_zone: NYOKZ
    htf_phase: EXPANSION
    day_state: PRE_EXPANSION (or POST_EXPANSION post trade_003 if same-day)
    daily_direction: BULLISH
    authority_tf: Daily
    strategy_type: state_gated
    setup_type: REVERSAL
    entry_tf: 15m
    replay_shipped: true
    replay_summary_from_all_6_results: |
      IDENTICAL to trade_003 replay output (same regime, origin,
      extreme, eq, PDAs, funnel). This is expected — same HTF
      lookback window produces same Map init, test harness
      replays the same date range; the TWO trades on Dec 12 are
      NOT differentiated in today's Map-canon replay.
    notes: |
      Same date as trade_003. max_trades_per_day = 1 per
      daily_expansion.yaml → at most one of the two is
      reachable per Map-canon session body. Relevant for
      SW27 question — does "first FVG" semantic preclude
      capturing trade_005 if trade_003 arms first?

  - id: trade_006
    date: 2025-12-15
    execution_time_ny: "03:45"
    direction: LONG
    kill_zone: LOKZ
    htf_phase: EXPANSION
    day_state: PRE_EXPANSION
    daily_direction: BULLISH
    authority_tf: Daily
    strategy_type: state_gated
    setup_type: REVERSAL
    entry_tf: 15m
    replay_shipped: true
    replay_summary_from_all_6_results: |
      regime=BULLISH origin=1.16152 extreme=1.17485 eq=1.16818
      pdas=11 gate_armed=714 chain_complete=0 trades=0
      deepest: 3/4 at 2025-11-19T04:10:00 LOKZ (OTE not reached)
      (Note: identical deepest date as trade_003/005 — same
       "previous day 8am NYOKZ FVG" storyline per Olya.)
    notes: |
      "4hr bullish expansion targeting H 1.17628 still not reached
      from previous day" — continuation of trade_005 momentum.

  - id: trade_007
    date: 2025-09-16
    execution_time_ny: "09:45"
    direction: LONG
    kill_zone: NYOKZ
    htf_phase: EXPANSION
    day_state: POST_EXPANSION (per "continuation" semantic)
    daily_direction: BULLISH
    authority_tf: Daily
    strategy_type: state_gated
    setup_type: CONTINUATION  # the ONLY CONTINUATION in the 6 shipped
    entry_tf: 5m
    replay_shipped: true
    replay_summary_from_all_6_results: |
      regime=BULLISH origin=1.16461 extreme=1.17654 eq=1.17057
      pdas=8 gate_armed=245 chain_complete=0 trades=0
      deepest: 3/4 at 2025-08-01T08:30:00 NYOKZ
    notes: |
      5m continuation trade — DAILY_CONTINUATION cartridge semantic
      (parked — not shipped as cartridge YAML). Demonstrates
      POST_EXPANSION day_state eligibility case if
      DAILY_CONTINUATION cartridge were active.

  - id: trade_008
    date: 2025-10-15
    execution_time_ny: "10:00"
    direction: LONG
    kill_zone: NYOKZ
    htf_phase: RETRACE
    day_state: N/A
    daily_direction: BEARISH
    authority_tf: Daily
    strategy_type: state_gated
    setup_type: REVERSAL
    entry_tf: 15m
    replay_shipped: false
    notes: |
      RETRACE cartridge not shipped. Flagged in ARS canon date
      list: (2025, 10, 15) SELL LOSS -1.00R — ARS traded this day
      SHORT and lost. COUNTER-EXAMPLE candidate for cross-path
      disagreement on same date (SHORT ARS vs LONG DAILY_EXPANSION
      if cartridge existed; neither cartridge is shipped for
      bearish RETRACE today). Relevant to F2.2 Shape 2.

  - id: trade_009
    date: 2025-11-14
    execution_time_ny: "01:00"
    direction: SHORT
    kill_zone: N/A
    htf_phase: INDEPENDENT
    day_state: N/A
    daily_direction: NEUTRAL
    authority_tf: N/A
    strategy_type: asia_range_scalp
    setup_type: CONTINUATION
    entry_tf: 5m
    replay_shipped: false
    notes: |
      Asia Range Scalp. Flagged in ARS canon date list: (2025, 11,
      14) SELL WIN +1.70R — ARS traded SHORT this day and won.
      Direction-aligned with trade_009 setup; potential F2.2
      Shape 2 counter-example candidate if ARS scalp and Map-
      gated scalp are the same-direction.

  - id: trade_010
    date: 2025-11-12
    execution_time_ny: "09:30"
    direction: LONG
    kill_zone: NYOKZ
    htf_phase: RETRACE
    day_state: N/A
    daily_direction: BEARISH
    authority_tf: Daily
    strategy_type: state_gated
    setup_type: REVERSAL
    entry_tf: 15m
    replay_shipped: false
    notes: RETRACE — not shipped.

  - id: trade_011
    date: 2025-11-28
    execution_time_ny: "09:15"
    direction: LONG
    kill_zone: NYOKZ
    htf_phase: RANGE
    day_state: N/A
    daily_direction: NEUTRAL
    authority_tf: 4H  # CASCADE — daily is NEUTRAL
    strategy_type: state_gated
    setup_type: CONTINUATION
    entry_tf: 15m
    replay_shipped: false
    notes: |
      RANGE cartridge not shipped. Interesting for SW43
      (AuthorityTF binary mapping) because authority_tf=4H is
      declared but cartridge doesn't exist. Also flagged: "NO
      SWEEP" — chain step 1 would fail; relevant to SW27 guard
      discussion ("sweep-optional chain" deferred per
      calibration Q20-25).

  - id: trade_012
    date: 2026-03-17
    execution_time_ny: "08:25"
    direction: LONG
    kill_zone: NYOKZ
    htf_phase: RETRACE
    day_state: N/A
    daily_direction: BEARISH
    authority_tf: Daily
    strategy_type: state_gated
    setup_type: REVERSAL
    entry_tf: 5m
    replay_shipped: false
    notes: |
      OUT OF DATA RANGE per YAML note ("2026-W12 is OUTSIDE
      current data range ends at 2026-W08"). Not replayable
      today.

  - id: trade_013
    date: 2026-03-12
    execution_time_ny: "09:00"
    direction: SHORT
    kill_zone: NYOKZ
    htf_phase: EXPANSION
    day_state: PRE_EXPANSION
    daily_direction: BEARISH
    authority_tf: Daily
    strategy_type: state_gated
    setup_type: REVERSAL
    entry_tf: 15m
    replay_shipped: true
    replay_summary_from_all_6_results: |
      regime=BEARISH origin=1.18348 extreme=1.15303 eq=1.16825
      pdas=6 gate_armed=927 chain_complete=0 trades=0
      deepest: 3/4 at 2026-02-10T07:30:00 NYOKZ (OTE not reached)
    notes: |
      Was listed OUT OF DATA RANGE per YAML header ("2026-W11 is
      OUTSIDE"). Contradiction with test_daily_expansion_6_trade
      _parity being green — fixture must actually have data through
      Mar 15 2026. Worth CTO verification if Olya prep relies on
      trade_013 freshness.

  - id: trade_014
    date: 2026-02-04
    execution_time_ny: "07:00"
    direction: SHORT
    kill_zone: NYOKZ
    htf_phase: RETRACE
    day_state: N/A
    daily_direction: BULLISH
    authority_tf: Daily
    strategy_type: state_gated
    setup_type: REVERSAL
    entry_tf: 15m
    replay_shipped: false
    notes: RETRACE cartridge not shipped.

ARS_151_trade_distribution:
  emission_policy: |
    ARS emits up to one trade per qualifying session date. Direction
    inferred post-entry from asia-sweep extension + MSS
    characteristics.
  reading_annotation_from_canon_trade_dates_py:
    total: 151
    breakdown_by_direction_and_outcome:
      # Counts extracted from _canon_trade_dates.py inline
      # comments (format: "# DIR OUTCOME ±R.RR")
      # (Totals approximate — annotation inline only; exact counts
      # per CTO verification if high precision needed)
    mixed_direction_PDA_in_zone_relevance: |
      ARS does NOT consume Map PDAs by design (DEC-ARS-BYPASSES-
      MAP). Therefore "mixed_direction_PDA_in_zone" attribute is
      N/A for ARS trades — ARS has no PDA awareness. Included here
      so CTO can NOT mistake the ARS set for SW47 counter-example
      hunting (which targets Map-gated path specifically).
  overlap_with_DAILY_EXPANSION_trade_dates:
    same_date_cases_confirmed:
      trade_008 (Oct 15, 2025) ↔ ARS (2025, 10, 15): SELL LOSS -1.00R
        # DAILY_EXPANSION direction LONG; ARS direction SHORT.
        # Directional DISAGREEMENT on same date.
      trade_009 (Nov 14, 2025) ↔ ARS (2025, 11, 14): SELL WIN +1.70R
        # DAILY_EXPANSION direction SHORT; ARS direction SHORT.
        # Directional AGREEMENT.
    relevance_to_F2.2_Shape_2: |
      Two confirmed same-date cases; one disagreement + one
      agreement. CTO counter-example hunt (if Shape 2 methodology
      ruling directs) has minimum-viable evidence seed here.

fallbacks_exercised_attribute_limitation:
  today_not_traceable: |
    No instrumentation in production replay emits which FB* branch
    fires per session. SW47 F1 Map-fallback scaffold (shipped 4a
    dispatch 4) adds MapConstructionMode enum on MapState but no
    construction site sets FALLBACK yet (scaffold armed but
    unfired). Per-fallback observability would need to be added
    as an Olya-session prep step or as P3/SW49 implementation
    scope.
  implication_for_counter_example_hunt: |
    CTO cannot today assign "replay trade_007 to test FB01 under
    no-displacement cold start" — the correlation would require
    either replay instrumentation or handcrafted synthetic
    fixtures that trigger each FB site in isolation. Scope note
    for Olya prep pack.

summary_attribute_table:
  fields_populated_per_trade:
    - id, date, execution_time_ny, direction, kill_zone, htf_phase
    - day_state (methodology-declared or N/A for non-state-gated)
    - daily_direction, authority_tf, strategy_type, setup_type
    - entry_tf, replay_shipped, notes
  fields_left_UNKNOWN_with_rationale:
    - fallbacks_exercised (no replay instrumentation)
    - mixed_direction_PDA_in_zone (no fixture probe; flagged as
      SW47 hazard-relevance scope note per COO_INPUTS §3.1 P1)
  fields_partially_populated:
    - replay_summary_from_all_6_results (only 6/14 have trace output)
```

---

## Exit Gates

```yaml
G1_T1_fallback_inventory_landed:
  status: GREEN
  enumerated: 15 fallback sites (FB01-FB15)
  required_fields_per_site: site, name, current_shape, trigger_condition,
                            docstring_intent, silent_vs_explicit,
                            methodology_adjacency, notes
  coverage: all fields populated for all 15 sites

G2_T2_day_state_captured:
  status: GREEN
  current_code_excerpt: _check_expansion_delivered (day_state.py:182-218) +
                        _find_aligned_event (day_state.py:235-251)
  semantic_summary: displacement + MSS matched independently; no causal
                    linkage check; no temporal ordering; no same-TF
                    constraint; no bar-distance check
  test_fixture_list:
    - test_day_state.py (6 named tests on transition semantic)
    - test_day_state_wiring.py (4 wiring tests)
    - 6 ground-truth decision_trace.jsonl files

G3_T3_T4_framings_retrieved:
  status: GREEN
  SW27_verbatim: captured from CLAUDE.md §15 block_2_status
                  (registered 2026-04-21, authority Olya)
  SW27_site_list: chain_evaluator._match_fvg (382-435) +
                  chain_config (field absence) +
                  detectors/fvg.py (adjacent)
  SW31_verbatim: captured from CLAUDE.md §15 block_2_status
                  (registered 2026-04-21, authority Olya)
  SW31_site_list: displacement.py _quality_grade (79-93) + emission
                  (333, 424) + consumer (503); day_state.py
                  _find_aligned_event (235-251); map_engine.py
                  _initialize_regime_from_detections (253-285);
                  dealing_range.is_daily_range_valid; mss.py:
                  284/364 + chain_evaluator.py:356 (SW32 siblings)

G4_T5_event_overlap_partitioned:
  status: GREEN
  ars_observed_types: SweepEvent, FvgScan, TraceTradeRecord,
                      TraceOutcome, ARSSessionRecord (plus custom
                      asia-sweep extension + detect_fvg_on_5m)
  map_observed_types: GateEvaluation, ChainEvaluation,
                      MapDecisionRecord, MapTimeline events (11
                      event types across PDA/regime/DR/gate)
  overlap_set: 5m FVG data (raw-detection level — Shape 1 scope);
               governance rejection nucleus (SW08 single-check-
               site invariant)
  field_classification: partitioned into decision-nucleus (SW08
                         governance AMBIGUOUS-on-trade-fields),
                         observational (path-specific lists),
                         ambiguous/methodology-gated (Shape 2)
  existing_test_coverage: ZERO cross-ARS-Map tests; within-path
                          determinism only

G5_T6_trade_index_built:
  status: GREEN
  DAILY_EXPANSION: 14 trades fully indexed with 13-attribute schema
  ARS_151: overlap + relevance note + two confirmed same-date
           cases (Oct 15 disagree, Nov 14 agree)
  fallbacks_exercised_attribute: marked UNKNOWN with rationale
                                 (no instrumentation available)
  mixed_direction_PDA: marked UNKNOWN with SW47 relevance note

G6_read_only_preserved:
  status: GREEN
  git_diff_scope_will_be: docs/reviews/2026-04-23_olya_prep_evidence.md only
  en1gma_touched: NONE
  cartridges_touched: NONE
  scripts_touched: NONE
  tests_touched: NONE
  no_sw_ids_assigned: correct per §11 finding_id_discipline
                      (no formal trigger event in this read-only pass)

G7_DENSE_format_maintained:
  status: GREEN
  format: YAML blocks throughout, binary verdicts where applicable,
          file:line refs, no prose bloat

pass_condition: MET
fail_condition_not_triggered: no T1-T6 surfaced UNKNOWN_HAZARDS or
                              code-that-doesn't-match-canonical-docs
```

---

## Handoff Notes

```yaml
what_is_in_scope_for_cto_next:
  - Draft Olya prep pack in decision-table format per GPT F7 discipline
  - Per-fallback disposition option drafting (T1 FB01-FB15): {accept
    as cold-start / fail-closed with specific error / log-and-flag
    via MapConstructionMode.FALLBACK}
  - Option drafting for P5 causal linkage (T2): 2 shapes per
    COO_INPUTS §3.2 P5 disposition shape
  - Counter-example trade assignment per decision option using the
    T6 index (e.g., "if Olya rules FB11 fail-closed, replay trade_011
    to probe RANGE-cartridge authority_tf=4H interaction")
  - F2.2 Shape 1 vs Shape 2 split (T5): Shape 1 is
    engineer-closable without Olya; Shape 2 needs methodology ruling
  - SW ID assignment at moment of finalized brief per §11

what_is_NOT_in_scope_for_this_artifact:
  - SW ID registration for T1 fallback clusters (no formal finding
    trigger — enumeration only)
  - Methodology option drafting
  - Counter-example assignment
  - Priority ordering (evidence only)
  - Scope expansion beyond T1-T6

residual_verification_requests:
  trade_013_data_range_note: |
    annotated_trades.yaml header claims "2026-W11 is OUTSIDE
    current data range (ends at 2026-W08)" yet
    test_daily_expansion_6_trade_parity.py includes trade_013
    end_date=2026-03-15 and the test is reportedly green
    (853+4 baseline). Either the YAML header is stale or the
    fixture extends beyond 2026-W08. Worth CTO verification
    before Olya-prep materials cite trade_013 freshness.
  trade_003_vs_trade_005_same_date_replay: |
    Both share (2025, 12, 12) and produce IDENTICAL replay output
    per all_6_results.json. max_trades_per_day=1 means at most one
    is captured. Relevant for SW27 ("does first FVG semantic
    preclude capturing the second?") and for day_state semantics
    if POST_EXPANSION day_state after trade_003 should gate
    trade_005 in DAILY_CONTINUATION (not shipped).
```

---

*End of evidence pack. Handoff: G / CTO to synthesize prep pack from
this file; Opus RepoPrompt remains HOT for follow-up depth requests.*
*Read-only pass completed at phase_3_5-exit HEAD + post-oracle +
2026-04-26 verification pass reference. No en1gma/ mutations.*
