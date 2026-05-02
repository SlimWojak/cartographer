# Phase 4a Verification Pass — Dispatch 3 Report

```yaml
document: PHASE_4A_D3_VERIFICATION_PASS
version: 1.0
date: 2026-04-26
status: DRAFT — READ-ONLY verdicts; gates dispatch-4 (P1 SW47)
owner: Opus (Cursor, HOT context continues into dispatch 4 after G ratification)
brief: PHASE_4A.D3.VERIFICATION_PASS (CTO bundle dispatch 3+4, conditional approval)
phase: 4a_step_1_of_bundled_execution
source_head: e2ecbde (phase_3_5-exit + post-oracle)
mutation_scope: NONE — git diff shows docs/ addition only; en1gma/ untouched
authority_cross_refs:
  COO_INPUTS_POST_PHASE_3.md: §3 priority table + §4 C4-C7 origin + §5 verification gaps
  POST_PHASE_3_ORACLE.md: §4 authority surfaces + §8 known drift
  ADVISOR_REVIEW_2026_04_26.md (b3f5e11): Lean/Bloat 1-4 + High 3 source lines
  CARTRIDGE_CONTRACT.md v1.0.3: §5 on_failure fail-closed discipline (D4 REMOVE precedent)
  CLAUDE.md v0.15: §6 invariants + §15 findings register (next SW = SW47)
purpose: |
  Narrow Phase 4a scope BEFORE P1 mutation + P2 dispatch. Resolve the
  four COO-flagged verification gaps (C4-C7) and survey the parity
  harness for tuple-equality (F2.1) and cross-path determinism
  (F2.2) coverage. Output in commit body is the authoritative record
  — G consumes to ratify P1 proceed and size Phase 4a continuation.
pass_condition_met: |
  - 4 verification verdicts landed (T1-T4)
  - 2 parity-harness gap reports landed (T5-T6)
  - each verdict paired with fix class (WIRE | REMOVE | ACCEPT) + size estimate
  - git diff shows only docs/ addition; no en1gma/ touched
  - zero UNKNOWN_HAZARD surfaced — bundle proceeds to dispatch 4 on G ratification
```

---

## T1 — C4: MapConfig usage verification

```yaml
target: en1gma/console/map/context_types.py::MapConfig (definition at line 212-268)
audit_method:
  - grep MapConfig + every site importing the class
  - grep self._config on MapEngine (the sole consumer candidate)
  - grep cfg.<field_name> for each of the 18 declared fields across en1gma/

instantiation_sites:
  production:
    en1gma/console/map/map_engine.py:160-161:
      context: MapEngine.__init__(config: MapConfig | None = None)
      action: self._config = config or MapConfig()
  tests_only:
    en1gma/tests/integration/test_map_trade001.py:42,61,76: MapEngine(MapConfig())
    en1gma/tests/console/map/test_map_engine.py:467: cfg = MapConfig() (defaults-only assertion)
    en1gma/tests/console/map/test_context_types.py:21: import-only

consumption_sites:
  self_config_reads_in_production:
    en1gma/console/map/map_engine.py: ZERO reads (grep `self._config\.` in map_engine → only the assignment at :161)
  cfg_field_reads_anywhere_in_en1gma:
    ZERO for all 18 declared fields.
    Fields searched: origin_source, extreme_source, extension_mode,
                     multi_leg_rule, pda_type_priority, zone_requirement,
                     straddle_valid, touch_trigger, cross_tf_touch,
                     mitigation_trigger, touch_permanent, proximity_mode,
                     proximity_buffer_pips, gate_persist_after_touch,
                     multi_pda_rule, allow_multi_arm, max_lookback_days,
                     max_pda_age_days.

field_level_table:
  origin_source:              dead (Olya Q1 default; MapEngine uses wick implicitly via DR cascade; field not read)
  extreme_source:             dead (Olya Q2; same pattern)
  extension_mode:              dead (Olya Q3 "rolling"; DR cascade hardcoded)
  multi_leg_rule:              dead (Olya Q4; DR composition hardcoded)
  pda_type_priority:           dead (Olya Q5/Q6 "FVG only"; PDA init loads FVG only, not driven by field)
  zone_requirement:            dead (Olya Q7 "midpoint"; gate.py zone check uses LocationClass, not this)
  straddle_valid:              dead (Olya Q8; chain_evaluator._eq_side_valid hardcodes behavior)
  touch_trigger:               dead (Olya Q12 "any_price_entry"; pda_store.py hardcodes)
  cross_tf_touch:              dead (Olya Q13; hardcoded true)
  mitigation_trigger:          dead (Olya Q14 "close_through"; pda_store.apply_bar_close:97-150 hardcodes this semantic)
  touch_permanent:             dead (Olya Q15; PDAStatus state machine hardcodes)
  proximity_mode:              dead (Olya Q18 "edge_touch"; gate.py touch check hardcoded)
  proximity_buffer_pips:       dead (Olya Q18; default 0.0 never sourced from config)
  gate_persist_after_touch:    dead (Olya Q19; gate re-arm semantic hardcoded)
  multi_pda_rule:              dead (Olya Q22 "first_reached"; gate candidate-pick hardcoded)
  allow_multi_arm:             dead (Olya Q23; no multi-arm machinery exists)
  max_lookback_days:           dead (Olya Q26 unlimited; no age filter)
  max_pda_age_days:            dead (Olya Q27 unlimited; no age filter)
  tally: 0/18 fields READ; 18/18 fields PARSED-ONLY

verdict: UNUSED
removal_candidate: YES
fix_class: D4_REMOVE
  shape: |
    (a) Delete class MapConfig from context_types.py
    (b) Delete config parameter + self._config from MapEngine.__init__ (or
        leave parameter absent per swiss-watch-reduce-surfaces posture)
    (c) Delete test_mapconfig_calibrated_defaults + all MapConfig()
        instantiations in tests (replace with MapEngine() bare
        construction; semantics identical since nothing reads the config)
    (d) Register INV-MAP-BEHAVIOR-FROM-METHODOLOGY-NOT-CONFIG — Olya's
        locked answers are implemented as HARDCODED spatial semantics,
        not runtime-configurable parameters. If future re-tuning is
        required, reopen per-field with ratified spec evolution; NOT
        via a dead-knob reinstation.
    (e) Strict-mode rejection: none needed — MapConfig is not cartridge-
        facing; no YAML schema surface to reject.
  size_estimate:
    production: ~60 LOC deletion (definition + consumer plumbing)
    tests: ~25 LOC deletion
    total: ~85 LOC removal (pure shrink)
  risk: LOW — removing dead storage; no behavior change
  parity_impact_prediction: 151/151 ARS + 6/6 DAILY_EXPANSION preserved

implications_for_phase_4a:
  - swiss-watch "smaller in authority surfaces" criterion: closes one dead surface
  - D4 posture ("if a field is not live, enforce / reject / delete") → DELETE
  - discoverable + standalone; does NOT block P1 SW47 — implementable after P1 lands
  - handoff note: combine with C5/C6 cleanup as a single "dead config surfaces" sprint

cross_refs:
  COO_INPUTS §4 C4_MapConfig_largely_unused (observation + 30-min verification task)
  POST_PHASE_3_ORACLE §8 C4 (cleanup candidate)
  ADVISOR_REVIEW Lean/Bloat 3 ("MapConfig as a largely unused runtime config surface")
```

---

## T2 — C5: chain.sequence runtime dispatch

```yaml
target: cartridge chain.sequence YAML field → loader → ChainConfig → chain_evaluator.evaluate() step ordering

load_path:
  cartridge_yaml:
    en1gma/cartridges/daily_expansion.yaml:44: "sequence: [SWEEP, MSS, FVG, OTE]"
    en1gma/cartridges/ars_v1_3.yaml: (ARS cartridge — not map_required; chain schema not
                                     applicable; ARS canon bypasses chain_evaluator)
  loader_enforcement:
    en1gma/cartridges/loader.py:58: _REQUIRED_CHAIN = {"sequence", "entry_method", ...}
    en1gma/cartridges/loader.py:59: _VALID_CHAIN_STEPS = {"SWEEP", "MSS", "FVG", "OTE"}
    en1gma/cartridges/loader.py:285: _validate_chain_steps(chain_raw.get("sequence", []))
    en1gma/cartridges/loader.py:439-442: _validate_chain_steps — checks step ∈ _VALID set
  loader_build:
    en1gma/cartridges/loader.py:394-410 _build_chain_config(chain: dict) -> ChainConfig:
      fields populated: entry_at, tp_method, sl_placement, sl_buffer_pips, ote_zone
      sequence: NOT PASSED to ChainConfig (ChainConfig has no sequence field)

chain_config_surface:
  en1gma/console/chain/chain_config.py:33-48:
    @dataclass(frozen=True) class ChainConfig
    Declared fields: sweep_required, sweep_proximity_buffer_pips, sweep_lookback_hours,
                     mss_min_quality, fvg_min_size_pips, ote_zone, entry_at,
                     sl_placement, sl_buffer_pips, tp_method, min_rr, max_chain_bars
    sequence_field_present: NO
  module_docstring: "The chain SEQUENCE is fixed (sweep → MSS → FVG → OTE).
                    What varies per strategy is thresholds and matching criteria."

runtime_dispatch:
  en1gma/console/chain/chain_evaluator.py:108-288 ChainEvaluator.evaluate(...):
    structure: sequential if/return blocks, literal-ordered:
      1. _match_sweep (:159)          — literal "Step 1"
      2. _match_mss (:169)            — literal "Step 2"
      3. _match_fvg (:180)            — literal "Step 3"
      4. _check_ote (:192)            — literal "Step 4"
    consumes_ChainConfig.sequence: NO (field does not exist to consume)
    consumes_cartridge.sequence_indirectly: NO (not threaded through)
  evaluator_comment:
    en1gma/console/chain/chain_evaluator.py:5 docstring:
      "It evaluates a 4-step confirmation sequence on 15m/5m detections"
    intent: sequence is architecturally fixed, not per-cartridge configurable

gap_characterization:
  validation_scope: loader checks step VOCABULARY (members of _VALID_CHAIN_STEPS)
  validation_gap_1: NO ORDERING CHECK — cartridge could declare
    [FVG, MSS, SWEEP, OTE] and pass _validate_chain_steps
  validation_gap_2: NO MEMBERSHIP CHECK — cartridge could declare
    [SWEEP, SWEEP, SWEEP, SWEEP] or [OTE] and pass
  runtime_behavior: regardless of YAML declaration, runtime executes
    SWEEP → MSS → FVG → OTE

verdict: DIVERGENT (trust-debt — same class as max_trades_per_window pre-D4)
trust_debt_flag: YES
  symptom: cartridge declares a sequence; runtime ignores the declaration
  failure_mode_if_author_trusts_declaration:
    - reorder attempts silently no-op (author assumes their ordering takes effect)
    - omit a step silently no-op (author assumes skipping sweep disarms the sweep gate)
    - doctrine drift: declarative contract broken at the declaration surface

fix_class: D4_REMOVE (preferred) OR D4_WIRE (not recommended — see rationale)
fix_shape_REMOVE:
  rationale: |
    chain_evaluator explicitly documents "sequence is fixed" (INV intent).
    Per-cartridge sequence reordering is not a methodology-calibrated
    capability — it would be a cartridge-author footgun if wired.
    Swiss-watch posture: fewer authority surfaces, stricter truth.
  shape: |
    (a) Delete "sequence" from _REQUIRED_CHAIN set (loader.py:58)
    (b) Delete _validate_chain_steps invocation (loader.py:285) + helper (:439-442)
    (c) Delete _VALID_CHAIN_STEPS constant (loader.py:59)
    (d) Strict-mode rejection: add explicit raise in load_strategy if
        chain.sequence key present — mirror max_trades_per_window / 
        day_state_requirement pattern (loader.py:304-312, 341-349):
          if "sequence" in chain_raw:
              raise StrategyLoadError(
                  "chain.sequence has been removed from the cartridge schema
                   (phase_4a D4 ratification). The field had no runtime
                   consumer — chain_evaluator executes SWEEP→MSS→FVG→OTE as
                   an architectural invariant (see chain_evaluator.py
                   module docstring). Migration: remove the line from the
                   cartridge YAML chain: block. Invariant:
                   INV-CHAIN-SEQUENCE-FIXED (§6 post-Phase-4a)."
              )
    (e) Delete chain.sequence line from daily_expansion.yaml
    (f) Register INV-CHAIN-SEQUENCE-FIXED at CLAUDE.md §6 as named
        constitutional constraint (architectural, not per-cartridge)
  size_estimate: ~20 LOC loader + ~3 LOC cartridge + §6 INV entry
  risk: LOW — deletes dead knob + tightens schema
  parity_impact_prediction: 6/6 DAILY_EXPANSION preserved (runtime behavior unchanged)

fix_shape_WIRE_not_recommended:
  rationale_against: |
    Would require runtime dynamic dispatch over sequence steps; larger
    LOC + introduces per-cartridge capability with no calibrated
    methodology demand. Expansion posture violates FORWARD_PLAN §P3
    "freeze expansion until P1-P6 close."

implications_for_phase_4a:
  - standalone; does NOT block P1 SW47
  - swiss-watch "stricter in config truth" criterion direct hit
  - pairs naturally with C6 (governance_precedence REMOVE) + C7 sl_method
    cleanup as a "cartridge schema D4 REMOVE batch" sprint
  - register under CHAIR SPLIT-HAZARD registration discipline at moment
    of commit → SW53 candidate (per CTO ratification note 2 above — F4
    atomic scope SW53 is reserved; this may or may not be the same
    finding; CTO to assign)

cross_refs:
  COO_INPUTS §4 C5_chain_sequence_runtime_dispatch_unverified
  POST_PHASE_3_ORACLE §8 C5
  ADVISOR_REVIEW Lean/Bloat 1
```

---

## T3 — C6: governance_precedence consumption

```yaml
target: GovernanceConfig.governance_precedence field (mapping through StrategyParams)

load_path:
  loader_dataclass:
    en1gma/cartridges/loader.py:99: governance_precedence: str
                                     (field on StrategyParams dataclass)
  loader_assignment:
    en1gma/cartridges/loader.py:381:
      governance_precedence=governance.get("precedence", "max_trades_per_day_overrides")
    note: YAML key is "precedence" under governance:, default string literal
          populated when absent. Field is NOT in _REQUIRED_TOP_LEVEL nor
          _REQUIRED_GOVERNANCE — optional with default.

consumption_sites:
  production_reads_of_governance_precedence: ZERO
    searched across: en1gma/console/, en1gma/orchestrator/, en1gma/scripts/,
                     en1gma/observe/, en1gma/methodology/, en1gma/cartridges/
  test_reads:
    en1gma/tests/cartridges/test_strategy_loader.py:75:
      assert params.governance_precedence == "max_trades_per_day_overrides"
    scope: default-value assertion ONLY; does not exercise behavior driven
           by non-default value
  runtime_governance_decisions:
    en1gma/console/governance/governance.py::check_governance (§4.5 authority surface)
      Blocker enum: {NONE, HALT, LEASE, RISK}
      precedence_logic: halt > lease > risk (hardcoded in check order)
      consumes_governance_precedence_field: NO
    en1gma/console/governance/risk.py RiskLimits / RiskState
      no reference to governance_precedence

verdict: UNUSED
removal_candidate: YES
fix_class: D4_REMOVE
  shape: |
    (a) Delete governance_precedence field from StrategyParams dataclass
        (loader.py:99)
    (b) Delete the .get("precedence", ...) line (loader.py:381)
    (c) Delete test_strategy_loader assertion (test_strategy_loader.py:75)
    (d) Strict-mode rejection: raise StrategyLoadError if governance.precedence
        is present in YAML — migration pattern mirrors max_trades_per_window
        (loader.py:341-349):
          if "precedence" in governance:
              raise StrategyLoadError(
                  "governance.precedence has been removed from the cartridge
                   schema (phase_4a D4 ratification). The field had no
                   runtime consumer — governance precedence is hardcoded
                   halt > lease > risk in check_governance (governance.py:147).
                   Strategy '…' still declares it; remove the line."
              )
    (e) Currently-shipping cartridges do NOT declare precedence — neither
        ars_v1_3.yaml nor daily_expansion.yaml set it. Strict-mode rejection
        is prospective protection, not a migration requirement.
  size_estimate: ~12 LOC removal + strict-mode rejection block
  risk: LOW — no cartridge uses it; no runtime consumer
  parity_impact_prediction: 151/151 + 6/6 preserved (no behavior change)

implications_for_phase_4a:
  - swiss-watch "stricter in config truth" + "smaller in authority surfaces"
  - bundles with C5 chain.sequence REMOVE + T4 sl_method REMOVE as one sprint
  - standalone; does NOT block P1 SW47

cross_refs:
  COO_INPUTS §4 C6_governance_precedence_unverified
  POST_PHASE_3_ORACLE §8 C6
  ADVISOR_REVIEW High 3 ("governance_precedence appears unused in runtime")
```

---

## T4 — C7: sl_method runtime consumption

```yaml
target: cartridge sl_method YAML key → loader _build_chain_config → ChainConfig
        sl_placement + sl_buffer_pips → chain_evaluator._compute_sl

load_path_sl_method:
  cartridge_yaml:
    en1gma/cartridges/daily_expansion.yaml:48: "sl_method: SWEEP_EXTREME"
    en1gma/cartridges/ars_v1_3.yaml: no sl_method (ARS bypasses chain)
  loader_enforcement:
    en1gma/cartridges/loader.py:58: _REQUIRED_CHAIN includes "sl_method"
  loader_build:
    en1gma/cartridges/loader.py:394-410 _build_chain_config(chain):
      line 398: sl_buffer = chain.get("sl_buffer_pips", 0.5)
      line 399: sl_placement = SLPlacement.SWEEP_EXTREME_BUFFERED if sl_buffer > 0
                                                                  else SLPlacement.SWEEP_EXTREME_RAW
      line 407-408: ChainConfig(sl_placement=..., sl_buffer_pips=..., ...)
    chain["sl_method"] KEY_READ: NO — _build_chain_config NEVER reads the
    sl_method value from the chain dict. Required for presence only;
    content is discarded.
  enum_declaration:
    en1gma/console/chain/chain_config.py:28-31 class SLPlacement:
      SWEEP_EXTREME_BUFFERED = "SWEEP_EXTREME_BUFFERED"
      SWEEP_EXTREME_RAW = "SWEEP_EXTREME_RAW"
    note: enum values are DERIVED shapes; raw cartridge-facing name
          "SWEEP_EXTREME" is neither member — mapping is implicit via
          the sl_buffer>0 branch.

load_path_sl_buffer_pips:
  cartridge_yaml: daily_expansion.yaml:49 + ars_v1_3.yaml:61
  loader: explicit .get("sl_buffer_pips", 0.5) — value READ + stored
  runtime_consumption:
    en1gma/console/chain/chain_evaluator.py:509: buffer = cfg.sl_buffer_pips * PIP
    en1gma/console/chain/chain_evaluator.py:510: if cfg.sl_placement == SLPlacement.SWEEP_EXTREME_RAW
    en1gma/console/chain/chain_evaluator.py:512-514: direction-sensitive buffer apply

derivation_firing:
  SWEEP_EXTREME → SWEEP_EXTREME_BUFFERED: YES — triggers when sl_buffer_pips > 0
    (cartridge default = 0.5 → BUFFERED). Verified at loader.py:399.
  SWEEP_EXTREME → SWEEP_EXTREME_RAW: triggers when sl_buffer_pips == 0 (not in
    any shipping cartridge today).

partial_wiring_summary:
  wired_half: sl_buffer_pips
    cartridge → loader → ChainConfig.sl_buffer_pips → chain_evaluator._compute_sl
    cartridge → loader (sl_buffer>0 branch) → ChainConfig.sl_placement → chain_evaluator._compute_sl
  not_wired_half: sl_method VALUE
    cartridge key REQUIRED by loader but CONTENT NEVER READ
    sl_method: "SWEEP_EXTREME" vs "FOOBAR" vs "" → all pass load (presence
    required, not value validated)

verdict: PARTIALLY_WIRED
  qualifier: functional sl computation IS correct today (SWEEP_EXTREME
  BUFFERED fires; _compute_sl honors direction + buffer). The wiring gap
  is on the sl_method FIELD itself — it's a trust-debt decoration, not a
  functional defect. Same class-of-hazard as chain.sequence (T2) but
  scope-narrower because the paired field sl_buffer_pips IS wired.

evidence_chain_wired_path:
  daily_expansion.yaml:49 (sl_buffer_pips: 0.5)
    → loader.py:398 (sl_buffer read)
    → loader.py:399 (sl_placement derived)
    → loader.py:407-408 (ChainConfig populated)
    → chain_evaluator.py:509-514 (_compute_sl consumes both fields)

evidence_chain_dangling_sl_method:
  daily_expansion.yaml:48 (sl_method: SWEEP_EXTREME)
    → loader.py:58 _REQUIRED_CHAIN (presence check only)
    → loader.py:284 _validate_required(chain_raw, _REQUIRED_CHAIN, "chain")
    → (no value read anywhere; string content discarded)

fix_class: D4_REMOVE (sl_method field only; sl_buffer_pips preserved)
  rationale: |
    sl_method value is presence-required-but-content-ignored. Author
    can declare any string without effect. Cleaner: drop the field from
    the schema; rely on sl_buffer_pips > 0 as the single configuration
    surface for BUFFERED vs RAW (or introduce an explicit sl_placement
    YAML key in a future v2 schema if RAW-without-buffer needs
    declaring without zeroing the buffer).
  shape: |
    (a) Remove "sl_method" from _REQUIRED_CHAIN (loader.py:58)
    (b) Delete sl_method line from daily_expansion.yaml:48
    (c) Strict-mode rejection: if "sl_method" in chain_raw: raise
        StrategyLoadError with migration guidance (mirror
        max_trades_per_window / chain.sequence patterns).
    (d) Expand test_strategy_loader.py fixtures already present at
        :130, :149, :177, :299, :426 to remove sl_method lines +
        verify explicit-presence rejection test.
    (e) Document in CARTRIDGE_CONTRACT §3: sl is configured via
        sl_buffer_pips alone (0 = RAW extreme; >0 = BUFFERED extreme
        by N pips).
  size_estimate: ~20 LOC loader + cartridge + contract doc
  risk: LOW — removes redundant presence-check; runtime unchanged
  parity_impact_prediction: 6/6 DAILY_EXPANSION preserved

fix_class_alternative_WIRE:
  if_preferred: map sl_method enum values explicitly to SLPlacement,
    remove sl_buffer>0 as the BUFFERED trigger.
  not_recommended: expands surface; sl_buffer_pips already acts as the
    single-source-of-truth; WIRE creates two redundant knobs.

implications_for_phase_4a:
  - swiss-watch "stricter in config truth" direct hit
  - bundle-batch with C5 + C6 + C4 as dead-config-surfaces sprint
  - standalone; does NOT block P1 SW47

cross_refs:
  COO_INPUTS §4 C7_sl_method_runtime_consumption_unverified
  POST_PHASE_3_ORACLE §8 C7
  ADVISOR_REVIEW High 3 (sl_method line)
```

---

## T5 — F2.1: detection identity parity harness expansion survey

```yaml
target: existing parity harness — what dimensions does it compare TODAY?

harnesses_examined:
  1_en1gma/tests/integration/test_detection_parity.py:
     comparison_source: kernel detect.py (run_detection) vs RA detect.py (runner.run_locked)
     comparison_unit: dict[f"{primitive}/{tf}" -> len(dr.detections)]  (line 45)
     assertion:       count-equality per primitive/tf key  (lines 109-114)
     evidence: test_detection_parity.py:102-118 reduces both sides to
               int counts before comparing — no tuple, no id, no properties
  2_en1gma/tests/cartridges/ars/test_ars_parity.py:
     scope: ARS session fixtures (151 dates) trade-level parity vs source repo
     NOT detection-level parity — operates on TradeResult surface
  3_en1gma/tests/cartridges/ars/test_ars_advance_canon_parity.py:
     scope: 306 parametrized advance() assertions — SessionState progression
     NOT detection-identity
  4_en1gma/tests/integration/test_map_canon_runner_parity.py:
     scope: run_map_replay ↔ direct MapCanonRunner.run(ctx) on trade_001 date
     comparison: sha256 of chain_trace.jsonl + decision_trace.jsonl  (lines 79-87, 149-153)
     byte-identity at the TRACE-OUTPUT level, but only FOR THAT PATH
     (not kernel-vs-RA detection parity; a downstream determinism guard)
  5_en1gma/tests/cartridges/ars/test_three_path_equivalence.py:
     scope: ARS batch ↔ ARS advance() ↔ ARS daemon (three PATHS within ARS)
     _TRADE_DECISION_FIELDS (18): byte-identical REQUIRED — but these
     are TradeResult / SessionRecord fields (asia_*, sweep_*, outcome,
     r_achieved, etc.), not detection events
     _OBSERVATIONAL_METADATA_FIELDS (3): per-path xfail under
     INV-DAEMON-REAL-TIME-SCOPE
     relevance_to_F2.1: NONE — this is path-equivalence within ARS,
     not detection-tuple identity

verdict: COUNT_ONLY
  scope: the singleton detection parity harness compares bucket counts;
  a detection set with identical COUNT but different CONTENT (different
  ids / timestamps / prices / directions / types / properties) passes.

gap_list (dimensions currently NOT asserted):
  1. Detection.id:               (source_repo=engine/base.py Detection dataclass)
     kernel path: detection objects carry stable id via _common.mkid
  2. Detection.time:             tz-aware datetime (post-SW24 INV-DETECTION-TIME-TZ-AWARE)
     gap: timestamp equality not compared
  3. Detection.direction:        str (bullish/bearish/neutral)
  4. Detection.price:            float
  5. Detection.type:             str (fvg, sweep, mss, etc.)
  6. Detection.properties:       dict (qualification_path, quality_grade,
                                 displacement_type, atr_value, range_pips,
                                 time_end, gap_pips, zone_top, zone_bottom,
                                 broken_swing, extreme_price, etc.)

proposed_harness_shape:
  dimension_1_tuple_equality:
    comparison_key_per_detection:
      (tf, time_iso, type, direction, round(price, 5), id)
    assertion: set-equality of tuples between kernel and RA per (primitive, tf)
    mismatch_output: symmetric_difference listing + first-divergent-tuple per bucket
  dimension_2_properties_deep_equality:
    scope: core decision-impacting property keys per primitive
      fvg:     {gap_pips, zone_top, zone_bottom, candle_a_low, candle_c_high}
      mss:     {displacement.quality_grade, displacement.extreme_price,
                broken_swing.price, break_type}
      sweep:   {proximity_pips, extension_pips, extreme_price}
      ote:     (derived — covered by mss consumption)
    assertion: dict-equal at overlapping keys (strict); tolerate divergent
      keys on non-decision-path metadata with explicit allow-list
  xfail_policy: none today (no known drift; surface existence of any
    divergence as test FAIL, matching SW38 INV-DAEMON-REAL-TIME-SCOPE
    discipline that explained drift needs named-invariant citation)

implementation_size_estimate:
  code:
    test_detection_parity.py extension: +40-60 LOC (replace count dict
      with tuple set + properties dict per-key; add diff renderer)
    no new fixture file needed
  tests: same 5 annotated-trade weeks already parametrized; reuses
    _river_available + _ra_available skipif guards
  blast_radius_on_existing_surface: zero — test-only extension
  risk: LOW-MEDIUM — if current count-parity is a ceiling on actual
    content-parity, tuple-equality may FAIL on current code and surface
    a latent detection-drift finding. If so: CHAIR SPLIT-HAZARD
    protocol applies (flag + register new SW + halt, per dispatch 3
    brief FAIL_CONDITION).

caveats:
  timestamp_normalization: RA may stamp NY-aware vs kernel UTC-aware
    internally; both must normalize to a canonical representation
    before tuple comparison. Reuse chain_evaluator._to_utc pattern
    (SW07 precedent).
  id_determinism: if RA's Detection.id generator is non-deterministic
    across runs but kernel's is deterministic (or vice versa), id-in-
    tuple will fail. Mitigation: exclude id from tuple key (compare on
    natural content tuple only) OR normalize ids deterministically
    pre-compare.

implications_for_phase_4a:
  - P6 (COO priority P6 / SW52 candidate): this IS the "semantic
    detection parity" proof gate in COO_INPUTS §3.2 and §7 Swiss-watch
    criterion "more provable in replay_persistence"
  - implementation scheduled as standalone sprint per COO_INPUTS §6
    phase_4_opener_candidates ordering_11 (post-P1/P2/P3/P4)
  - verdict here CONFIRMS the gap and SIZES implementation; does NOT
    claim scope bleeds into P1

cross_refs:
  COO_INPUTS §3.2 P6_semantic_detection_parity (SW52 candidate)
  COO_INPUTS §7 non_negotiable_phase_4_exit_gates[6]
  POST_PHASE_3_ORACLE §5 INV-DETECTION-AUTHORITY-SINGLETON (count-parity TODAY; SEMANTIC = SW52/P6)
  ADVISOR_REVIEW Medium 7 (count-parity gap half)
```

---

## T6 — F2.2: cross-path determinism assertion survey

```yaml
target: where ARS canon runner + Map canon runner observe overlapping event
        types, is cross-path identity asserted?

path_scope_inventory:
  path_A_ars:
    entry: scripts/run_ars_session.py (--mode REQUIRED; map_required=false)
    canon: console/chain/canon/ars/ars_canon.py (self-contained; DEC-ARS-BYPASSES-MAP)
    detect_consumption: detect_fvg_on_5m + custom ARS asia-session semantics
    TFs_consumed: 1m (fixture backbone), 5m (fvg watch)
    output_surface: TradeResult + SessionRecord (ARS-shaped schema)
  path_B_map:
    entry: scripts/run_map_session.py (--mode REQUIRED; map_required=true)
    canon: console/chain/canon/map_canon/runner.py + session._run_map_session
    detect_consumption: full detect.py on HTF + LTF
    TFs_consumed: 1D, 4H, 15m, 5m (and 1H via ChainEvaluator indirectly)
    output_surface: chain_trace + decision_trace + map_timeline (Map-shaped)

overlap_analysis:
  bar_level:
    ARS fixtures (CANON_TRADE_DATES, 151 dates spanning 2024-2026) run on
    1m + 5m bars within asia window + NY session
    Map fixtures (6 DAILY_EXPANSION ground-truth dates, 2025-2026) run on
    1D + 4H HTF bars (45-day lookback) + 15m + 5m LTF bars on the trade date
    date_intersection_in_ground_truth: NON-ZERO possible but not
    systematically exercised — no test asserts overlap today
  event_type_overlap_when_bars_overlap:
    detect.py primitives available to both paths:
      sweep / liquidity_sweep, fvg, mss, displacement, ob (on any TF)
    ARS actually consumes: fvg/5m + sweep/1m (via ars_canon.detect_fvg_on_5m
      and asia-sweep extension tracker)
    Map actually consumes: fvg/1D + fvg/4H (PDA init), sweep/15m + mss/15m +
      fvg/15m + sweep/5m + mss/5m + fvg/5m (chain evaluator)
    minimum_true_overlap: fvg/5m detections on a shared trade-date
  trade_decision_output_surface_overlap:
    ARS TradeResult fields vs Map CanonIntent fields:
      both have: direction, entry, sl, tp (semantically; field names differ)
      ARS-only: asia_high/low, asia_range_pips, sweep_extreme, fvg_time_ny,
                range_class, outcome (simulated)
      Map-only: pda_ref, chain_evidence (sweep + mss + fvg + ote_level)
    common_decision_nucleus: {direction, entry, sl, tp, rr}
    caveat: semantically same fields but produced by different methodology
      (ARS = asia-setup; Map = HTF-PDA + chain) → byte-identity is NOT
      expected on same date even at the nucleus; this is intentional per
      cartridge separation

existing_cross_path_assertion_search:
  test_files_searched:
    en1gma/tests/cartridges/ars/: no imports from console.chain.canon.map_canon
                                 nor orchestrator.map_orchestrator
    en1gma/tests/integration/test_smoke_live.py: ARS-only
    en1gma/tests/integration/test_map_canon_runner_parity.py: within-Map-path
                                                              determinism
    en1gma/tests/cartridges/ars/test_three_path_equivalence.py: within-ARS
                                                                three-path
                                                                equivalence
    grep for "ARS.*Map|ars.*map|cross.path" across tests/: no cross-path harness
  verdict: no test asserts any cross-ARS-Map identity (neither on
    detection outputs nor trade-decision nuclei)

scope_boundary_declarations_relevant:
  INV-DAEMON-REAL-TIME-SCOPE (SW38, 2026-04-22):
    framed within ARS three-path observation (batch/advance/daemon)
    declares what batch vs daemon observation scopes may legitimately
    diverge on (Class B observational metadata)
    does NOT extend to cross-cartridge path comparison
  DEC-ARS-BYPASSES-MAP (phase_3_2):
    deliberate architectural property — ARS paths do not consume Map
    state; by design the two paths produce different decision surfaces
    on the same date
  INV-DETECTION-AUTHORITY-SINGLETON:
    says detect.py is the sole source of detection truth; does NOT
    (today) promise "output invariant regardless of caller" — only
    "no other module generates detections"

verdict: NOT_ASSERTED  (primary)
         SCOPE_AMBIGUOUS  (secondary — cross-path semantic identity
                           requires methodology ratification first)

overlap_inventory:
  event_types_BOTH_paths_observe_via_detect.py:
    fvg/5m:                 ARS (detect_fvg_on_5m) + Map (chain fvg match)
    sweep/15m, sweep/5m:    Map only in production flow
                            (ARS uses asia-sweep extension tracker, not
                             detect.py's liquidity_sweep primitive on 5m
                             — verification note: confirm via ars_canon
                             internals if F2.2 harness lands)
    mss/15m, mss/5m:        Map only
    fvg/15m:                Map only
  minimum_nontrivial_overlap: fvg/5m on dates where both paths run

proposed_assertion_shape:
  shape_1_caller_invariant_detection_output (RECOMMENDED):
    claim: for any (bars_subset, tf_subset) passed to detect.py, the
      DetectionResult is byte-identical regardless of which cartridge
      path invoked it.
    assertion_unit:   tuple-equality per detection event (folds into
                      F2.1 harness; same comparison surface)
    test_construction:
      - load bars for date D on a fixed TF (e.g. 5m for 2025-10-01)
      - invoke detect.py twice: once via ARSRunner wrapper, once via
        MapCanonRunner wrapper (or once directly, once via each)
      - compare DetectionResult tuple sets
    scope_coverage: reinforces INV-DETECTION-AUTHORITY-SINGLETON with a
      "caller-invariant" corollary — tightens the invariant from
      "singleton emitter" to "singleton AND output-stable across call sites"
    invariant_to_register: INV-DETECTION-CALLER-INVARIANT (§6 extension)
  shape_2_trade_decision_nucleus_parity (NOT RECOMMENDED without Olya):
    claim: on dates where both ARS and Map generate intents, the
      {direction, entry, sl, tp} fields are byte-identical
    issue: contradicts DEC-ARS-BYPASSES-MAP — the two paths are
      DESIGNED to produce different decisions on the same date. Only
      a methodology ruling could declare a subset of dates where
      parity IS expected (e.g. "on ARS setups that Map also sees as
      valid PDAs in its DR"). Scope-ambiguous; do not pursue in
      dispatch 3/4.

implementation_size_estimate:
  shape_1_caller_invariant:
    code: ~30-50 LOC test extension (either new test_detection_parity_caller_
          invariant.py file or extend test_detection_parity.py)
    fixtures: reuse existing annotated trade weeks; pick 1-2 dates
              where both ARS trade-date and Map lookback-window touch
    tests: 2-3 parametrized cases
    blast_radius: test-only
    risk: LOW-MEDIUM — if caller context inadvertently mutates
      detect.py output (unlikely given pure-function contract), test
      fails and surfaces latent coupling. CHAIR SPLIT-HAZARD applies.
  shape_2_trade_decision_nucleus: OUT_OF_SCOPE without methodology ruling

caveats:
  scope_ambiguous_rationale: |
    The dispatch-3 brief asks to "acknowledge INV-DAEMON-REAL-TIME-SCOPE
    scope boundary (decision fields yes; observational metadata
    exempt)." But INV-DAEMON-REAL-TIME-SCOPE applies to within-ARS
    three-path; cross-ARS-Map scope is not yet ruled. Shape 1
    (caller-invariant detection) is safely within INV-DETECTION-
    AUTHORITY-SINGLETON semantic — it does not require cross-path
    decision-field parity, only detection-output parity which IS a
    shared contract today (just under-asserted).

implications_for_phase_4a:
  - Shape 1 pairs naturally with F2.1 (T5 expansion) — same test file,
    same comparison machinery, stronger invariant (SINGLETON-AND-
    CALLER-INVARIANT)
  - Shape 2 is Phase 4b-or-later and methodology-ruling-dependent —
    add as queued item, do NOT execute in this dispatch bundle
  - neither shape blocks P1 SW47; both are exit-gate candidates for
    swiss-watch certification (COO_INPUTS §7 "more provable in replay_
    persistence")

cross_refs:
  COO_INPUTS §7 swiss_watch "more_provable_in_replay_persistence"
  POST_PHASE_3_ORACLE §5 INV-DETECTION-AUTHORITY-SINGLETON
  POST_PHASE_3_ORACLE §8 SW38 INV-DAEMON-REAL-TIME-SCOPE (scope-boundary precedent)
  ADVISOR_REVIEW Medium 7 (semantic parity framing)
```

---

## Exit Gates — Dispatch 3 Pass Condition

```yaml
G1_six_verdicts_landed:
  T1_C4_MapConfig:              UNUSED → D4_REMOVE (~85 LOC, LOW risk)
  T2_C5_chain_sequence:         DIVERGENT → D4_REMOVE (~20 LOC + INV-CHAIN-SEQUENCE-FIXED)
  T3_C6_governance_precedence:  UNUSED → D4_REMOVE (~12 LOC)
  T4_C7_sl_method:              PARTIALLY_WIRED → D4_REMOVE on sl_method field
                                only (~20 LOC; sl_buffer_pips wiring preserved)
  T5_F2.1_detection_identity:   COUNT_ONLY → FULL_TUPLE proposed (~40-60 LOC)
  T6_F2.2_cross_path:           NOT_ASSERTED (+ SCOPE_AMBIGUOUS on decision-
                                field shape) → caller-invariant detection
                                shape recommended (~30-50 LOC)
  status: ALL SIX LANDED

G2_scope_implications_clear:
  T1-T4 fix_class: all D4_REMOVE (strict-mode rejection pattern per
    CARTRIDGE_CONTRACT §5); batch-bundleable as a single "dead config
    surfaces" sprint (~137 LOC deletion + 4 strict-mode rejection blocks
    + 2 new invariants: INV-MAP-BEHAVIOR-FROM-METHODOLOGY-NOT-CONFIG
    and INV-CHAIN-SEQUENCE-FIXED)
  T5-T6 fix_class: ACCEPT for today (harness expansion as P6/SW52
    sprint); T6 Shape 1 folds into T5 extension → single atomic commit
    covers both
  phase_4a_ordering_implication: verification clears P1 SW47 to proceed
    without scope dependency; C4-C7 cleanup + P6/F2.1/F2.2 harness
    expansion are Phase 4a/4b sequencing decisions for CTO
  status: CLEAR

G3_no_mutation:
  git_diff_scope: docs/reviews/2026-04-26_phase_4a_verification_pass.md (new file)
  pre_existing_whitespace_drift_in_tree: docs/canonical/POST_PHASE_3_ORACLE.md
    + docs/reviews/COO_INPUTS_POST_PHASE_3.md (whitespace-only, pre-session;
    NOT staged in this commit — left in working tree for cleanup elsewhere)
  en1gma_touched: NONE
  cartridges_touched: NONE
  scripts_touched: NONE
  tests_touched: NONE
  status: CLEAN — read-only pass respected

G4_handoff_ready:
  report_dense_yaml:                   YES (this file)
  each_verdict_has_fix_class:          YES (WIRE | REMOVE | ACCEPT assigned)
  each_verdict_has_size_estimate:      YES (LOC + risk + parity impact)
  P1_SW47_proceed_signal:              CLEAR — no verdict touches gate.py or
                                       conflicts with P1 scope; no
                                       UNKNOWN_HAZARD surfaced
  phase_4a_continuation_sizing:        feasible as separate sprint (C4-C7
                                       REMOVE batch + P6 harness expansion)
  status: READY

pass_condition: MET
fail_condition_not_triggered: no T1-T6 surfaced UNKNOWN_HAZARD; all six are
  characterized within D4 discipline (WIRE/REMOVE/ACCEPT + strict-mode
  rejection pattern) or swiss-watch harness expansion pattern

unknown_hazards_surfaced: NONE
chair_split_hazards_registered: NONE (no finding ID assignment triggered in
  this read-only pass; SW IDs assigned at mutation moment per §11
  finding_id_discipline)
```

---

## Handoff to Dispatch 4 (P1 SW47) + CTO Review Hooks

```yaml
dispatch_4_proceed_signal:
  conditions_met:
    - verification exit gates G1-G4 all green
    - zero UNKNOWN_HAZARDS
    - no verdict conflicts with P1 SW47 scope (gate.py:114-118 direction clause)
    - no verdict requires re-scoping before mutation phase
  awaiting: G ratification of this report before dispatch 4 begins

scope_carry_forward_for_dispatch_4:
  no_change_to_P1_brief:
    - gate.py:114-118 direction clause fix as specified in CTO brief
    - F1 Map-fallback assertion scaffold per brief T2
    - 2 tests (mixed-direction parity + fallback-scaffold)
    - SW47 §15 registration at commit moment
    - H1 frequency delta block in commit body
  confirmed_adjacent_invariants_today:
    - INV-PDA-DIRECTION-FIDELITY (SW04 shipped): direction_context field
      on PDA is detector-faithful; P1 exploits this
    - INV-GATE-DIRECTION-CONSISTENT-WITH-REGIME (proposed §6 addition
      per CTO brief T4 invariant_update): CTO discretion to defer to
      Phase 4b when gate migrates to Map-assembly layer per GPT F3

scope_not_carried_forward (Phase 4a+ or 4b continuation, NOT bundled into dispatch 4):
  dead_config_surfaces_batch:
    items: T1 MapConfig REMOVE + T2 chain.sequence REMOVE + T3
           governance_precedence REMOVE + T4 sl_method REMOVE
    sizing: ~137 LOC deletion + 4 strict-mode rejection blocks + 2
            new invariants
    owner_proposal: Opus or COO Claude, standalone sprint
    priority: MEDIUM (aligns with Swiss-watch "stricter config truth"
             and "smaller authority surfaces" criteria but not on the
             critical path for correctness)
  semantic_parity_expansion:
    items: T5 F2.1 FULL_TUPLE harness + T6 F2.2 Shape 1 caller-invariant
           detection harness (fold together into one commit)
    sizing: ~70-110 LOC test extension
    owner_proposal: Opus, standalone sprint; SW52 candidate registration
    priority: MEDIUM-HIGH (COO_INPUTS §7 exit_gate #6 — non-negotiable
             for Swiss-watch cert)
  out_of_scope_without_methodology_ruling:
    items: T6 Shape 2 cross-ARS-Map trade-decision parity
    disposition: queue for Olya session if relevant; DEC-ARS-BYPASSES-MAP
                 currently precludes byte-identity expectation

CTO_review_hooks:
  1. Ratify: do T1-T4 REMOVE shapes move forward as one batch sprint,
     or sequenced individually? (COO recommends: one atomic batch,
     reuses strict-mode rejection pattern already precedent-set)
  2. Invariant registration timing: INV-MAP-BEHAVIOR-FROM-METHODOLOGY-
     NOT-CONFIG + INV-CHAIN-SEQUENCE-FIXED — register at §6 at moment
     of MapConfig / chain.sequence REMOVE commit per §11 discipline
  3. Approve Shape 1 (caller-invariant detection) as the F2.2 resolution
     and fold into F2.1 expansion as single SW52 sprint? Or split into
     two commits (F2.1 primary tuple-equality + F2.2 caller-invariant
     secondary)?
  4. Greenlight dispatch 4 (P1 SW47): G to ratify this report → Opus
     resumes HOT context and executes dispatch 4 per brief specification
```

---

*End of Dispatch 3 verification report. Read-only pass completed at e2ecbde + this docs commit. Handoff to G for ratification, then Opus resumes with dispatch 4 (P1 SW47) per bundle contract.*
