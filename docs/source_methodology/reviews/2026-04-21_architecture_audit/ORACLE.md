# ORACLE.md — Current-State Codebase Orientation
# For CTO, Olya's Advisors, and fresh agents planning the cartridge refactor
# Author: Claude Opus 4.7 (full codebase read, 2026-04-21)
# Companion to: CARTRIDGE_CONTRACT.md, CARTRIDGE_IMPLEMENTATION_DRAFT.md, DESIGN.md, COMPARISON.md

```yaml
purpose: |
  Dense factual snapshot of en1gma's codebase AS IT EXISTS TODAY.
  Not aspirational. Not historical. Current reality on main branch.
  Read this to understand what you're working with before planning sprints.
format: DENSE_M2M
read_time: "~10 minutes"
```

---

## 1. WHAT EN1GMA IS (30-second version)

A constitutional trading kernel for EUR/USD that encodes one trader's (Olya's) ICT
methodology into a deterministic, governable runtime. Two execution paths:

- **Path A (ARS):** Self-contained Asia Range Scalp. Live on M3 in shadow/paper mode.
  Bypasses the HTF Map entirely. 151/151 parity proven. Walk-forward validated (+54R, 5yr).

- **Path B (Map-gated):** HTF spatial context → LTF execution chain. 6/6 ground truth
  trades produce paper fills. Operational in replay mode. Not yet live.

722 tests. Zero flakes (Monday). Two humans govern: G (capital), Olya (methodology).

---

## 2. REPOSITORY SHAPE

```
en1gma/                          # Python package root
├── __init__.py                  # v0.1.0
│
├── data/                        # L1: DATA INGESTION
│   ├── bar_types.py             #   Bar1m, Bar5m dataclasses + PIP constant + session hour constants
│   ├── river.py                 #   Parquet reader (load_date_range, load_1m_bars) + LiveRiverReader
│   └── tf_aggregator.py         #   1m → 5m aggregation (used by ARS)
│
├── detection/                   # L2: DETECTION (singleton oracle)
│   ├── detect.py                #   SOLE ENTRY POINT: run_detection(bars_by_tf) → detections
│   ├── detection_types.py       #   Re-exports from ra_engine
│   ├── locked_baseline.yaml     #   Locked detector config
│   └── ra_engine/               #   39 vendored files from Research Accelerator
│       ├── engine/              #     Detection base type, cascade runner, registry
│       │   └── base.py          #     Detection dataclass (__post_init__ enforces tz-aware)
│       ├── detectors/           #     One file per primitive (13 total)
│       │   ├── _common.py       #     to_ny_aware() — tz source-of-truth
│       │   ├── fvg.py, mss.py, sweep.py, displacement.py, swing_points.py,
│       │   │   order_block.py, ote.py, asia_range.py, equal_hl.py,
│       │   │   htf_liquidity.py, luxalgo_mss.py, luxalgo_ob.py,
│       │   │   reference_levels.py, session_liquidity.py
│       ├── config/              #     YAML config loader + schema
│       ├── data/                #     CSV loader, River adapter, session tagger, TF aggregator
│       └── evaluation/          #     Walk-forward, fitness, comparison (research tooling)
│
├── context/                     # L3: HTF MAP (persistent spatial context)
│   ├── context_types.py         #   ALL shared types: Regime, DealingRange, PDA, MapState,
│   │                            #   GateResult, MapConfig + 12 enums (MarketDirection,
│   │                            #   PDAStatus, LocationClass, AuthorityTF, etc.)
│   ├── map_engine.py            #   MapEngine class — THE central spatial engine
│   │                            #   initialize() from HTF bars, process_daily_bar(),
│   │                            #   process_h4_bar(), get_state(), get_active_pdas()
│   ├── regime.py                #   RegimeTracker — direction + phase + authority TF
│   ├── dealing_range.py         #   DealingRangeTracker + is_daily_range_valid() (DR cascade)
│   ├── pda_store.py             #   PDAStore — add_fvg(), update_on_price(), update_on_bar_close()
│   │                            #   PDA lifecycle: OPEN → TOUCHED → REJECTED|MITIGATED|INVALIDATED
│   ├── map_persistence.py       #   JSON serialize/deserialize MapState for cross-session persistence
│   └── liquidity.py             #   STUB v2 — detect_resting_liquidity() returns []
│
├── gating/                      # L4a: EXECUTION GATE (single file, standalone package)
│   └── execution_gate.py        #   evaluate_gate(map_state, price, time) → ARMED|DISARMED
│                                #   4 conditions: regime + PDA in zone + direction perm + kill zone
│
├── chain/                       # L4b: LTF EXECUTION CHAIN
│   ├── chain_evaluator.py       #   ChainEvaluator.evaluate() — sweep → MSS → FVG → OTE → entry
│   │                            #   normalize_detection_times() — thin aware→UTC adapter (post-SW24)
│   ├── chain_types.py           #   SweepMatch, MSSMatch, FVGMatch, ChainResult, EntrySpec
│   │                            #   Each match type has __post_init__ UTC enforcement
│   ├── chain_config.py          #   ChainConfig dataclass (12 fields) + EntryMethod/TPMethod/SLPlacement enums
│   └── ars/                     #   ⚠ ARS CANON ALGORITHM (strategy-specific code in console infra)
│       ├── ars_canon.py         #     measure_asia_range(), track_sweep_extensions(),
│       │                        #     detect_fvg_on_5m(), simulate_outcome(), process_session()
│       │                        #     ARSCandidate + TradeResult dataclasses. ~400 lines.
│       ├── session_state.py     #     SessionState dataclass + Phase enum + advance() method
│       │                        #     302 parametrized parity assertions. Production-hardened.
│       ├── checkpoint.py        #     Append-only JSONL checkpoint + torn-line-tolerant reader
│       └── recovery.py          #     FAST_PATH/SLOW_PATH/FRESH_START/OUT_OF_WINDOW recovery
│
├── execution/                   # L5a: TRADE EXECUTION
│   ├── intent_builder.py        #   build_intent_from_ars() + build_intent_from_chain()
│   │                            #   ⚠ imports ARSCandidate directly (strategy-specific coupling)
│   ├── broker_adapter.py        #   PaperBroker — open_position(), close_position(), halt_all()
│   └── position.py              #   Position state machine (PENDING→OPEN→CLOSED|HALTED)
│
├── control/                     # L5b + WIRING: governance + orchestration + day_state
│   ├── governance.py            #   OperatingMode enum, validate_config(), check_governance()
│   │                            #   Single authorization site (INV-GOVERNANCE-SINGLE-CHECK-SITE)
│   ├── halt.py                  #   HaltSignal (<50ms), check_halt_signal(swarm_path)
│   ├── lease.py                 #   LeaseStateMachine (DRAFT→ACTIVE→EXPIRED|REVOKED|HALTED)
│   ├── risk.py                  #   RiskState + RiskLimits — can_trade() check
│   ├── day_state.py             #   DayStateEngine — PRE_EXPANSION/POST_EXPANSION FSM
│   │                            #   Market-structure-driven (INV-DAY-STATE-MARKET-DRIVEN)
│   ├── orchestrator.py          #   run_ars_session() — Path A wiring (~100 lines)
│   └── map_orchestrator.py      #   run_map_replay() — Path B wiring (~600 lines, largest file)
│                                #   Date iteration, bar loading, detection, map processing,
│                                #   gate eval, chain eval, governance, broker, tracing
│
├── observe/                     # OBSERVABILITY (cross-cutting)
│   ├── decision_trace.py        #   DecisionTracer + SessionRecord — per-session JSONL trace
│   ├── map_timeline.py          #   MapTimeline — JSONL structural event log (regime, DR, PDA, gate)
│   ├── replay.py                #   replay_session() — deterministic replay from trace
│   └── state_snapshot.py        #   SystemSnapshot capture (bar, asia, sweep, gate, position)
│
├── strategies/                  # STRATEGY DECLARATIONS (YAML + loader)
│   ├── loader.py                #   StrategyParams + GovernanceConfig dataclasses
│   │                            #   load_strategy(), load_governance(), build_governance_deps()
│   │                            #   ⚠ Two separate dataclasses, not a unified CartridgeSpec
│   ├── daily_expansion.yaml     #   Map-gated strategy (map_required: true)
│   └── ars_v1_3.yaml            #   Self-contained strategy (map_required: false)
│                                #   ⚠ Fundamentally different YAML shape from daily_expansion
│
├── methodology/                 # LOCKED REFERENCE (read-only, Olya-ratified)
│   ├── SYNTHETIC_OLYA_METHOD_vLOCK.yaml   # 13 locked primitives
│   ├── calibration_results.yaml            # 27 Olya answers
│   ├── STATE_DETECTION_LOGIC_v2.yaml       # State detection rules
│   ├── ARS_CANON_v1_3.md                   # ARS methodology document
│   ├── HTF_MAP_SPEC_v0_1.yaml              # Map spec (v0.1 — 1178 lines, comprehensive)
│   ├── DAILY_MOMENTUM_BREAKOUT_CANON.md    # SUPERSEDED by daily_expansion.yaml
│   └── METHODOLOGY_INDEX.md                # Index of all methodology docs
│
├── tests/                       # 722 TESTS (3 tiers)
│   ├── unit/           (24 files)  # Module correctness
│   ├── contract/       (5 files)   # Extraction parity (kernel == source repo)
│   └── scenario/       (9 files)   # Full trade sequences + wiring integration
│
├── ground_truth/                # ANNOTATED TRADE DATA
│   └── annotated_trades.yaml    # 14 Olya-annotated trades (6 used for ground truth)
│
├── scripts/                     # OPERATIONAL + CALIBRATION SCRIPTS
│   ├── run_ars_session.py       #   ARS daemon entry point (launchd on M3)
│   ├── run_map_session.py       #   Map-gated session entry point
│   ├── run_discovery_scan.py    #   Walk-forward discovery tool
│   ├── sentinel.py              #   Gemma 4 system monitor (5 health checks + Telegram relay)
│   ├── henry_analyst.py         #   GLM 5.1 forensic analyst
│   ├── health_check.py          #   System diagnostics
│   └── calibration/             #   7 calibration scripts (DR, FVG, gate, persistence, etc.)
│
└── docs/
    └── HTF_MAP_SPEC_v0_1.yaml   #   Duplicate of methodology/ copy (historical)
```

---

## 3. DATA FLOW — PATH A (ARS)

```
┌──────────────────────────────────────────────────────┐
│ scripts/run_ars_session.py                           │
│   --mode shadow  --date 2026-04-21                   │
│                                                      │
│   1. load_strategy("ars_v1_3")                       │
│   2. build_governance_deps(governance_config)        │
│   3. validate_config(mode, halt, lease, risk)  ← T1  │
│   4. control/orchestrator.run_ars_session(            │
│        mode, date, halt, lease, risk, risk_limits)   │
│                                                      │
│   Inside run_ars_session():                          │
│     a. river.load_date_range(walk_back_window)       │
│     b. ars_canon.measure_asia_range(bars, date)      │
│     c. ars_canon.track_sweep_extensions(bars, ...)   │
│     d. ars_canon.detect_fvg_on_5m(bars, ...)         │
│     e. IF candidate found:                           │
│        → check_governance(mode, halt, lease, risk)   │  ← T2
│        → build_intent_from_ars(candidate)            │
│        → broker.open_position(intent)                │
│     f. ars_canon.simulate_outcome(bars, candidate)   │
│     g. trace.end_session()                           │
└──────────────────────────────────────────────────────┘

Live daemon variant (run_live_session in run_ars_session.py):
  Uses SessionState + checkpoint + recovery.
  LiveRiverReader.next_bar() per-bar loop.
  SessionState.advance(bar) per bar.
  Checkpoint written on every state mutation.
  Recovery on restart: FAST_PATH (checkpoint + gap backfill)
  or SLOW_PATH (fresh + session replay).
```

---

## 4. DATA FLOW — PATH B (Map-Gated)

```
┌──────────────────────────────────────────────────────────┐
│ control/map_orchestrator.run_map_replay(                 │
│   mode, start_date, end_date, strategy="DAILY_EXPANSION")│
│                                                          │
│   1. validate_config(mode, halt, lease, risk)      ← T1  │
│   2. FOR each trading_date in [start..end]:              │
│      a. _init_map_for_date(bars, td, lookback=45d)       │
│         → MapEngine().initialize(daily_bars, h4_bars)    │
│         → RegimeTracker.update_on_mss(daily MSS)         │
│         → DealingRangeTracker.create_range(origin, ext)  │
│         → PDAStore.add_fvg(...) for each daily FVG       │
│         → MapEngine._replay_price_forward(daily_bars)    │
│         → run_detection(bars_by_tf) → HTF detections     │
│                                                          │
│      b. DayStateEngine.process_detections(htf_dets)      │
│                                                          │
│      c. FOR each kill_zone [LOKZ, NYOKZ]:                │
│         FOR each 1m bar in kz_window:                    │
│           i.  run_detection(ltf_bars) → LTF detections   │
│           ii. evaluate_gate(map_state, price, time)      │
│               → regime dir ✓ + PDA in zone ✓             │
│               + direction perm ✓ + kill zone ✓           │
│               → ARMED or DISARMED                        │
│                                                          │
│           iii. IF ARMED:                                 │
│                ChainEvaluator.evaluate(                  │
│                  gate_result, ltf_detections,            │
│                  current_bar, armed_pda, dealing_range)  │
│                → sweep match? → MSS match?               │
│                → FVG match? → OTE in zone?               │
│                → ChainResult (COMPLETE or INCOMPLETE)    │
│                                                          │
│           iv.  IF chain COMPLETE:                        │
│                build_intent_from_chain(entry_spec)       │
│                check_governance(mode, halt, lease, risk)│  ← T2
│                broker.open_position(intent)              │
│                pda_store.reject_pda(armed_pda)           │
│                                                          │
│      d. Write decision_trace, chain_trace, map_timeline  │
│      e. Write session_summary.yaml                       │
└──────────────────────────────────────────────────────────┘
```

---

## 5. KEY TYPES AND THEIR RELATIONSHIPS

```
Bar1m ──────→ run_detection() ──→ Detection ──→ MapEngine ──→ MapState
  │                                   │              │           │
  │                                   │              │     ┌─────┴──────┐
  │                                   ▼              │     │            │
  │                            DetectionResult       │   Regime    DealingRange
  │                            {tf → {primitive →    │     │            │
  │                             [Detection]}}        │     │        equilibrium
  │                                                  │     │            │
  │                                                  ▼     ▼            ▼
  │                                            PDAStore ──→ PDA[]
  │                                                │
  │                                                ▼
  │                                         evaluate_gate()
  │                                                │
  │                                          GateResult
  │                                          (ARMED/DISARMED)
  │                                                │
  └────────────→ ChainEvaluator.evaluate() ←───────┘
                        │
                  ChainResult
                  (COMPLETE/INCOMPLETE)
                        │
                  EntrySpec (entry, SL, TP, RR)
                        │
                  TradeIntent
                        │
                  check_governance()
                        │
                  GovernanceResult (approved/blocked)
                        │
                  PaperBroker.open_position()
                        │
                  Position (PENDING→OPEN→CLOSED)
```

---

## 6. KEY MODULE SIZES (lines, approximate)

```
map_orchestrator.py     ~650   ← largest file, full Path B wiring
map_engine.py           ~700   ← second largest, spatial engine + initialization
ars_canon.py            ~410   ← ARS algorithm (stateless batch version)
session_state.py        ~340   ← ARS daemon state machine
chain_evaluator.py      ~570   ← 4-step chain evaluation
context_types.py        ~220   ← all shared types (12 enums + 7 dataclasses)
loader.py               ~310   ← strategy YAML → StrategyParams
decision_trace.py       ~200   ← ARS-specific trace format
governance.py           ~190   ← mode + validate + check_governance
pda_store.py            ~190   ← PDA lifecycle management
```

---

## 7. WHAT WORKS AND WHAT DOESN'T

### ✅ Working and battle-tested

| Component | Evidence |
|-----------|----------|
| ARS canon algorithm | 151/151 parity, 302 advance() assertions, P1 verified in production |
| Detection singleton | 5/5 contract parity, tz-aware at source (SW24) |
| Map engine | 6/6 ground truth, 27/27 Olya calibration, direction-faithful PDAs (SW04) |
| Chain evaluator | 6/6 ground truth, UTC-canonical (SW07), tz source-of-truth at detector (SW24) |
| Governance | Single check site, both paths wired, PAPER/LIVE parity enforced (SW08) |
| Session recovery | FAST/SLOW/FRESH/OUT_OF_WINDOW, checkpoint tolerant of torn writes (SW09) |
| Replay determinism | Per-date Map re-init, no future leak (SW02), byte-identical on replay |
| PDA mitigation | Retrace-fill semantic correct for FVG (SW01), Olya-ratified |
| DR cascade | Daily → H4 when daily still expanding, 15 tests |
| Day state | PRE/POST_EXPANSION FSM, market-driven, wired per bar |

### ⚠ Known issues (registered findings, not yet fixed)

| ID | Severity | Issue | Block |
|----|----------|-------|-------|
| SW06 | MEDIUM | Terminal PDAs lost on persistence save (map_persistence) | 2 |
| SW10 | MEDIUM | pda_timeframes loaded but never enforced in gate | 1 (Olya) |
| SW11 | MEDIUM | 7/12 ChainConfig fields use hardcoded defaults, not YAML | 2 |
| SW12 | MEDIUM | map_persistence write is non-atomic (crash = corrupt) | 2 |
| SW13 | LOW | max_chain_bars=24 declared but never enforced | 2 |
| SW14 | MEDIUM | River heartbeat gaps not detected (substance check) | 2 |
| SW18 | MEDIUM | Sentinel ignores config paths for river_heartbeat | 2 |
| SW19 | LOW | Sunday 18:00+ false weekend detection in Sentinel | 3 |
| SW22 | MEDIUM | OTE body vs wick source unverified (Olya F2) | 2 |
| SW23 | LOW | UTC/NY parquet calendar-date boundary (latent) | 2 |
| SW25 | LOW | map_timeline.jsonl non-deterministic hash | 3 |
| SW26 | MEDIUM | Sentinel heartbeat boolean-vs-substance false positives | 2 |

### ⚠ Structural concerns (from audit, cartridge boundary)

| # | Concern | Detail |
|---|---------|--------|
| 1 | ARS canon code in console | `chain/ars/` is strategy-specific code inside infrastructure |
| 2 | Non-uniform YAML schemas | `ars_v1_3.yaml` and `daily_expansion.yaml` have different shapes |
| 3 | intent_builder couples to ARS | `build_intent_from_ars()` imports `ARSCandidate` directly |
| 4 | `control/` conflates 3 concerns | governance + orchestration + day_state in one package |
| 5 | `gating/` is a single-file package | execution_gate.py alone in its own directory |
| 6 | No import boundary enforcement | Nothing prevents console from importing cartridge names |
| 7 | Duplicate mitigation logic | pda_store + map_engine both implement FVG retrace-fill check |
| 8 | `context/` name is generic | Doesn't teach the two-clock model; `map/` would be clearer |

---

## 8. INVARIANT REGISTER (25 active)

Grouped by the concern they protect:

```yaml
SOVEREIGNTY:
  - INV-SOVEREIGN-1: "Human sovereignty over capital is absolute"
  - INV-SOVEREIGN-2: "Live execution requires human T2 approval"

SAFETY:
  - INV-HALT-1: "halt_local < 50ms"
  - INV-HALT-2: "halt_cascade < 500ms"
  - INV-HALT-OVERRIDES-ALL: "Halt wins over any other system state"

DETECTION:
  - INV-DETECTION-AUTHORITY-SINGLETON: "detect.py is the sole detection oracle"
  - INV-OLYA-ABSOLUTE: "Olya's NO on any detection is final"
  - INV-DETECTION-TIME-TZ-AWARE: "Every Detection.time tz-aware at construction"
  - INV-VLOCK: "13 L1 primitives locked"

ARCHITECTURE:
  - INV-ORCHESTRATOR-DUMB: "Orchestrator sequences and wires. Never decides."
  - INV-MAP-SCOPE-V1.1: "Daily regime + daily FVG + DR cascades daily→H4"
  - INV-NO-REIMPLEMENTATION: "Extracted modules pass source repo tests unchanged"
  - INV-REPLAY-DETERMINISM: "Same stored inputs → same outputs. Always."
  - INV-DAY-STATE-MARKET-DRIVEN: "Day state transitions on market structure only"
  - INV-SESSION-STATE-PROGRESSION: "ARS daemon state is serializable + recoverable"

METHODOLOGY:
  - INV-CANON-FIDELITY: "Strategy canon algorithms identical to proven simulators"
  - INV-PDA-CREATED-AT-CONFIRMATION: "PDA created_at = Candle C close"
  - INV-PDA-DIRECTION-FIDELITY: "PDA direction = detector direction, not regime"
  - INV-PDA-ZONE-FROM-DETECTOR: "PDA zone bounds verbatim from detector"
  - INV-PDA-MITIGATION-IS-RETRACE-FILL: "FVG mitigated when retrace fills zone"

GOVERNANCE:
  - INV-NO-UNGOVERNED-TRADES: "Every trade passes through governance (CLOSED)"
  - INV-LIVE-REQUIRES-T2: "LIVE raises NotImplementedError until graduation"
  - INV-GOVERNANCE-SINGLE-CHECK-SITE: "check_governance() sole authorization"
  - INV-MODE-EXPLICIT-PER-INVOCATION: "OperatingMode required, no defaults"
  - INV-PAPER-GOVERNANCE-PARITY-WITH-LIVE: "PAPER and LIVE identical deps"
  - INV-GOVERNANCE-SEPARATION: "Governance rejection doesn't mutate Map state"
```

**Not yet registered** (proposed by CARTRIDGE_CONTRACT.md):
INV-CARTRIDGE-PURE-DECLARATION, INV-CONSOLE-STRATEGY-BLIND,
INV-NEW-CARTRIDGE-NO-CONSOLE-CHANGE, INV-CARTRIDGE-SCHEMA-UNIFIED,
INV-BOUNDARY-CLASSIFIABLE, INV-AUTHORITY-BOUNDARY-EXPLICIT, INV-RULING-SCOPE-EXPLICIT

---

## 9. TEST DISTRIBUTION

```yaml
unit:      24 files
  key_suites:
    test_ars_canon.py              # ARS batch algorithm correctness
    test_ars_session_state.py      # SessionState.advance() correctness
    test_ars_checkpoint.py         # Checkpoint read/write + torn-line tolerance
    test_ars_recovery.py           # Recovery path selection + gap backfill
    test_map_engine.py             # Map initialization + PDA creation + price updates
    test_map_engine_pda_fidelity.py  # SW04: direction + zone from detector
    test_chain_evaluator.py        # 4-step chain evaluation scenarios
    test_chain_timezone.py         # SW07: UTC enforcement on chain types
    test_day_state.py              # FSM transitions + regime awareness
    test_governance_enforcement.py # SW08: mode enforcement + dep requirements
    test_dr_cascade.py             # Daily → H4 cascade validation
    test_ra_engine_tz_contract.py  # SW24: Detection.__post_init__ tz enforcement
    test_sentinel.py               # Health check logic (SW19 Sunday flake)

contract:  5 files
  test_ars_parity.py               # 151 trade parity (kernel == source repo)
  test_ars_advance_canon_parity.py # 302 parametrized advance() parity
  test_detection_parity.py         # 5 detection parity checks
  test_map_trade001.py             # Ground truth trade 001 full-path validation

scenario:  9 files
  test_map_wiring.py               # End-to-end Map-gated path integration
  test_governance_wiring.py        # SW08 governance on both paths
  test_replay_no_future_leak.py    # SW02 per-date Map re-init
  test_day_state_wiring.py         # SW03 day state per-bar processing
  test_chain_determinism_tz.py     # SW07 chain tz across full replay
  test_ars_restart_recovery.py     # SW09 daemon restart scenarios
  test_sw04_pda_fidelity.py        # SW04 direction + zone integration
  test_sw24_real_river_tz.py       # SW24 real River parquet tz preservation
  test_smoke_live.py               # LiveRiverReader smoke test
```

---

## 10. STRATEGY YAML COMPARISON (the schema gap)

### daily_expansion.yaml (62 lines)
```yaml
# Top-level fields consumed by loader → StrategyParams:
strategy: DAILY_EXPANSION          # string
family: DAILY_MOMENTUM
version: "1.0"
map_required: true
day_state_requirement: PRE_EXPANSION
regime: { required_phase, direction_permission }
pda: { types, timeframes }
execution_windows: { timezone, windows, LOKZ{}, NYOKZ{} }
detection: { ltf_timeframes, htf_timeframes }
chain: { sequence, entry_method, ote_fib, tp_method, sl_method, sl_buffer_pips }
governance: { max_trades_per_day, lease{}, risk{} }
```

### ars_v1_3.yaml (61 lines)
```yaml
# Top-level fields — DIFFERENT SHAPE:
strategy: { name, version, pair, map_required, description }  # nested dict!
risk: { per_trade_pct, min_rr, max_trades_per_session }
governance: { lease{}, risk{} }
asia_range: { start_hour_ny, end_hour_ny, range_cap_pips, classifications{} }
sweep: { window_start_hour_ny, window_end_hour_ny, min/max_extension_pips }
fvg: { timeframe, min_untouched_pips, entry_cap_hour, require_* booleans }
exit: { sl_buffer_pips, tp_buffer_pips, mode, timeout }
provenance: { canon_doc, validated_trades, total_r, validation_period }
```

**Key observation:** `daily_expansion.yaml` is consumed by `loader.py` → `StrategyParams`.
`ars_v1_3.yaml` is partially consumed by `loader.py` (governance block only) but its
algorithm-specific sections (`asia_range`, `sweep`, `fvg`, `exit`) are NOT consumed by
any loader — they're documentation/reference. The actual ARS parameters are hardcoded
constants in `ars_canon.py` (`RANGE_CAP_PIPS = 30.0`, `SWEEP_MIN_PIPS = 2.0`, etc.).

This is the core cartridge contract gap: ARS's parameters live in Python constants,
not in the YAML declaration. The YAML describes what the constants are, but the runtime
doesn't read them.

---

## 11. IMPORT DEPENDENCY MAP (simplified)

```
data ←── detection ←── context ←── gating ←── chain
  │          │            │           │          │
  │          │            │           │          ├── ars (⚠ strategy-specific)
  │          │            │           │          │
  └──────────┴────────────┴───────────┴──────────┴──→ control/
                                                       ├── governance (imports halt, lease, risk)
                                                       ├── orchestrator (imports ars_canon, river, trace)
                                                       └── map_orchestrator (imports EVERYTHING)

execution ←── control (broker needs halt; intent needs ars_canon ⚠ + chain_types)
observe ←── chain/ars (replay imports ars_canon directly ⚠)
strategies/loader ←── chain/chain_config + control/day_state + control/halt + control/lease + control/risk
```

**⚠ marks** = strategy-specific coupling that the cartridge refactor would remove.

---

## 12. GROUND TRUTH TRACES

Six trades validated end-to-end (all BEARISH, LOKZ/NYOKZ, EUR/USD):

```
traces/ground_truth/
├── trade_001/   Oct 1 2025, SHORT, LOKZ   ← primary calibration trade
├── trade_003/   Oct 3 2025, SHORT, NYOKZ
├── trade_005/   Oct 8 2025, SHORT, LOKZ
├── trade_006/   Oct 8 2025, SHORT, NYOKZ
├── trade_007/   Oct 9 2025, SHORT, LOKZ
└── trade_013/   Nov 4 2025, SHORT, LOKZ

Per trade: decision_trace.jsonl, chain_trace.jsonl, map_timeline.jsonl, session_summary.yaml
```

Bullish ground truth trades technically unblocked post-SW01 but not yet run (held pending audit).

---

## 13. WHAT CTO + ADVISORS NEED TO KNOW FOR SPRINT PLANNING

### The refactor target
Move from current flat 9-package layout to `console/` + `cartridges/` + `orchestrator/`
per CARTRIDGE_CONTRACT.md + CARTRIDGE_IMPLEMENTATION_DRAFT.md.

### What's mechanically easy
- Directory restructure (move files, update imports, run tests) — ~1 week
- Import lint enforcement — 1 day
- Gate merged into chain — 1 hour

### What's architecturally non-trivial
1. **Unified CartridgeSpec schema** — ARS and DAILY_EXPANSION need to conform to the same
   dataclass. The ARS YAML shape is fundamentally different. ARS algorithm params need to
   move from Python constants to `canon_algorithm.params` in YAML.

2. **Canon runner** — ARS canon isn't a simple function. It has:
   - Multi-phase progression (Asia → sweep → FVG → outcome)
   - SessionState with advance() per bar
   - Checkpoint/recovery with 4 recovery paths
   - Notification idempotency via seen_notification_ids
   
   The canon runner interface must support all of this. A simple
   `canon(bars) → trade` interface is insufficient.

3. **Duplicate mitigation consolidation** — pda_store.update_on_bar_close() and
   map_engine._replay_price_forward() both implement FVG retrace-fill. Should be
   consolidated to a single site before moving both into `console/map/`.

### What blocks what
```
CARTRIDGE_CONTRACT v1.0 canonicalized
  └→ Directory restructure (Phase 2)
       └→ Schema unification + canon runner (Phase 3)
            └→ Block 4 drift fixes (normal sprints on clean base)
                 └→ RETRACE/RANGE cartridges (Olya creative work)
```

### Current operational state
- ARS live on M3 (shadow/paper), launchd automated, Sentinel monitoring
- Path B operational in replay mode, not live
- Fresh-eyes architectural audit was scheduled this week — the audit has now happened
  (DESIGN.md + COMPARISON.md). Its output feeds directly into the cartridge refactor plan.

---

*"The kernel works. The architecture is correct. The build is now about making the
structure match the documentation — so the next 50 sprints build on a foundation
where the filesystem teaches what the docs describe."*
