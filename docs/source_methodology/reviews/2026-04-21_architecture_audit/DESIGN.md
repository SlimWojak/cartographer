# DESIGN.md — First-Principles Architecture for an ICT Trading Kernel
# Phase 2 of Outcome-Design Audit
# Author: Claude Opus 4.7 (fresh instance, no prior en1gma exposure)
# Date: 2026-04-21

## 1. GOVERNING PRINCIPLE

The system is a **console + cartridge** runtime. The console encodes ICT methodology
as universal, strategy-blind machinery. Cartridges are pure declarations that configure
which console capabilities to activate. The boundary between them is the primary
architectural invariant.

---

## 2. TOP-LEVEL REPOSITORY STRUCTURE

```
kernel/
├── README.md                    # 1-paragraph orientation + pointer to ARCHITECTURE.md
├── ARCHITECTURE.md              # This design — the canonical structural reference
├── CLAUDE.md                    # Agent orientation (operational state, session artifacts)
│
├── console/                     # ── THE CONSOLE (strategy-blind ICT machinery) ──
│   ├── primitives/              # L1: ICT detection primitives (singleton implementations)
│   │   ├── __init__.py          #     Re-exports the detection facade
│   │   ├── detect.py            #     Single entry point — detect(bars, timeframe, primitive_type)
│   │   ├── types.py             #     Detection, Primitive enum, shared types
│   │   ├── fvg.py               #     Fair Value Gap detector
│   │   ├── mss.py               #     Market Structure Shift detector
│   │   ├── sweep.py             #     Liquidity sweep detector
│   │   ├── displacement.py      #     Displacement detector
│   │   ├── swing_points.py      #     Swing point detector
│   │   ├── order_block.py       #     Order block detector
│   │   ├── ote.py               #     Optimal Trade Entry detector
│   │   ├── dealing_range.py     #     Dealing range measurement
│   │   ├── asia_range.py        #     Asia session range detector
│   │   └── ...                  #     One file per primitive (13 vLOCK primitives)
│   │
│   ├── map/                     # L2: HTF Spatial Context Engine (persistent, cross-session)
│   │   ├── __init__.py
│   │   ├── engine.py            #     MapEngine — the persistent worldview
│   │   ├── regime.py            #     Regime tracking (direction + authority TF)
│   │   ├── dealing_range.py     #     Dealing range lifecycle + cascade logic
│   │   ├── pda.py               #     PDA store — lifecycle (OPEN→TOUCHED→terminal)
│   │   ├── persistence.py       #     Cross-session JSON state save/restore
│   │   ├── types.py             #     MapState, Regime, DealingRange, PDA, PDAStatus
│   │   └── day_state.py         #     Intraday market-structure FSM (PRE/POST expansion)
│   │
│   ├── chain/                   # L3: LTF Execution Chain (intraday, resets each session)
│   │   ├── __init__.py
│   │   ├── evaluator.py         #     Chain evaluation: sweep → MSS → FVG → OTE → entry
│   │   ├── gate.py              #     Execution gate — boolean "should chain scan now?"
│   │   ├── types.py             #     ChainResult, SweepMatch, MSSMatch, FVGMatch, OTEMatch
│   │   └── config.py            #     ChainConfig (populated from cartridge YAML)
│   │
│   ├── governance/              # L4: Capital Safety (halt, lease, risk — human sovereignty)
│   │   ├── __init__.py
│   │   ├── governance.py        #     check_governance() — THE single authorization site
│   │   ├── halt.py              #     Halt state machine (<50ms response)
│   │   ├── lease.py             #     Lease state machine (bounded autonomy windows)
│   │   ├── risk.py              #     Risk limits + position sizing
│   │   ├── mode.py              #     OperatingMode enum {TEST, SHADOW, PAPER, LIVE}
│   │   └── types.py             #     Blocker enum, GovernanceResult
│   │
│   ├── execution/               # L5: Trade Execution (intent → broker → position)
│   │   ├── __init__.py
│   │   ├── intent.py            #     IntentBuilder — chain result → trade intent
│   │   ├── broker.py            #     BrokerAdapter (paper + live implementations)
│   │   └── position.py          #     Position tracking + state
│   │
│   └── data/                    # L0: Data Ingestion (bar types, river, TF aggregation)
│       ├── __init__.py
│       ├── bar.py               #     Bar/Candle types — the universal data unit
│       ├── river.py             #     Live bar stream (River)
│       └── aggregator.py        #     Timeframe aggregation (M5 → H1 → H4 → D1)
│
├── cartridges/                  # ── CARTRIDGE DECLARATIONS ──
│   ├── __init__.py
│   ├── schema.py                #     CartridgeSpec dataclass — the cartridge contract
│   ├── loader.py                #     YAML → CartridgeSpec parser + validator
│   ├── ars_v1_3.yaml            #     ARS cartridge (map_required: false)
│   ├── daily_expansion.yaml     #     Daily Expansion cartridge (map_required: true)
│   └── ...                      #     Future cartridges added here as YAML files only
│
├── orchestrator/                # ── WIRING LAYER (sequences console components) ──
│   ├── __init__.py
│   ├── runtime.py               #     Main orchestrator — cartridge + console → session
│   ├── map_session.py           #     Map-gated path: River → Map → Gate → Chain → Intent
│   └── direct_session.py        #     Map-independent path: River → Canon Algo → Intent
│
├── observe/                     # ── OBSERVABILITY (trace, replay, timeline) ──
│   ├── __init__.py
│   ├── trace.py                 #     Decision trace (every decision logged)
│   ├── replay.py                #     Deterministic replay engine
│   ├── timeline.py              #     Map timeline (structural event log)
│   └── snapshot.py              #     State snapshots for debugging
│
├── methodology/                 # ── LOCKED METHODOLOGY REFERENCE (read-only) ──
│   ├── vlock.yaml               #     13 locked primitives — Olya-ratified
│   ├── calibration.yaml         #     27+ Olya calibration answers
│   ├── state_detection.yaml     #     State detection logic
│   └── INDEX.md                 #     Methodology index
│
├── tests/                       # ── TEST TIERS ──
│   ├── unit/                    #     Module correctness
│   ├── contract/                #     Extraction parity + invariant enforcement
│   └── scenario/                #     Full trade sequences against ground truth
│
├── ground_truth/                # ── ANNOTATED TRADE DATA ──
│   ├── annotated_trades.yaml
│   └── traces/                  #     Per-trade trace artifacts
│       ├── trade_001/
│       └── ...
│
├── scripts/                     # ── OPERATIONAL SCRIPTS ──
│   ├── run_session.py           #     Main entry point (loads cartridge, runs session)
│   ├── run_replay.py            #     Replay a stored trace
│   ├── health_check.py          #     System health diagnostics
│   └── ...
│
└── ops/                         # ── DEPLOYMENT + MONITORING ──
    ├── sentinel/                #     Always-on system monitor
    ├── launch/                  #     launchd/cron scripts
    └── config/                  #     Runtime configuration (paths, hosts, etc.)
```

---

## 3. LAYER RESPONSIBILITIES

### L0: Data (`console/data/`)
- **Owns:** Bar types, river streaming, timeframe aggregation
- **Contract:** Produces typed `Bar` objects with tz-aware timestamps
- **Rule:** No detection logic. No strategy awareness. Pure data plumbing.

### L1: Primitives (`console/primitives/`)
- **Owns:** Every ICT detection primitive (FVG, MSS, sweep, displacement, OB, OTE, etc.)
- **Contract:** `detect(bars, timeframe, primitive) → List[Detection]`
- **Invariant:** SINGLETON — each primitive has exactly one implementation. `detect.py` is the sole entry point. No module outside `primitives/` may implement detection logic.
- **Rule:** Primitives are stateless functions. They receive bars, they return detections. They do not know about the Map, the Chain, strategies, or governance.

### L2: Map (`console/map/`)
- **Owns:** Persistent spatial context — regime, dealing range, PDA lifecycle
- **Contract:** Consumes HTF detections → maintains `MapState` (regime + active dealing range + PDA store)
- **Two-clock boundary:** The Map answers WHERE and WHICH DIRECTION. It never fires a trade.
- **Persistence:** JSON-serializable state, survives process restarts
- **Day state:** Intraday FSM (PRE_EXPANSION / POST_EXPANSION) driven by market structure, never by system events
- **Rule:** Map mutations are event-driven (structural detection events), not per-bar. Map state reflects observed market structure only — governance concerns are orthogonal.

### L3: Chain (`console/chain/`)
- **Owns:** LTF execution evaluation — sweep → MSS → FVG → OTE → entry signal
- **Contract:** Given LTF bars + gate=ARMED → evaluates chain → produces `ChainResult` or None
- **Gate:** Boolean function: regime direction + permission + active PDA in zone + kill zone time → ARMED/DISARMED
- **Two-clock boundary:** The Chain answers HOW TO ENTER. It never decides direction.
- **Rule:** Chain resets each session. Config comes from the loaded cartridge. Chain is infrastructure — it doesn't change between cartridges; only its *configuration* changes.

### L4: Governance (`console/governance/`)
- **Owns:** Capital safety — halt, lease, risk checks
- **Contract:** `check_governance(mode, halt, lease, risk, limits) → GovernanceResult`
- **Invariant:** SINGLE CHECK SITE — `check_governance()` is the sole authorization function. Direct halt/lease/risk queries are observability-only.
- **Invariant:** LIVE requires human T2 token
- **Invariant:** PAPER and LIVE have identical governance dependencies (parity)
- **Rule:** Governance never mutates Map/PDA/structural state. Market observation and authorization to act are orthogonal.

### L5: Execution (`console/execution/`)
- **Owns:** Trade intent construction, broker interaction, position tracking
- **Contract:** ChainResult → Intent → (governance check) → Broker → Position
- **Rule:** No execution without prior governance authorization.

---

## 4. THE CARTRIDGE CONTRACT

This is the critical interface. A cartridge is a YAML file that conforms to `CartridgeSpec`:

```yaml
# cartridge schema
name: string                    # unique identifier
family: string                  # strategy family (e.g., DAILY_MOMENTUM, ASIA_SCALP)
version: string                 # semantic version

# Console configuration — what to activate
map:
  required: bool                # does this cartridge use the HTF Map?
  regime_direction: bool        # does the gate check regime?
  pda_types: [FVG, OB, ...]    # which PDA types to track (v1: FVG only)
  pda_timeframes: [DAILY, H4]  # which TFs to create PDAs from
  dealing_range:
    primary_tf: DAILY           # primary dealing range timeframe
    cascade_tf: H4              # fallback if primary is still expanding
  day_state:
    required_state: PRE_EXPANSION | POST_EXPANSION | ANY

# Chain configuration — how to evaluate entries
chain:
  sweep_lookback_hours: float
  mss_max_bars: int
  fvg_contact: WICK | BODY
  ote_zone: [float, float]      # e.g., [0.62, 0.79] for standard OTE
  ote_contact: WICK | BODY
  max_chain_bars: int

# Risk parameters
risk:
  max_risk_per_trade: float
  max_daily_loss: float
  max_open_positions: int

# Governance
governance:
  lease:
    duration_minutes: int
    auto_renew: bool
  risk:
    # risk limit overrides specific to this cartridge

# Kill zones — when to scan
kill_zones:
  - name: LONDON
    start: "08:00"
    end: "12:00"
    tz: Europe/London
  - name: NEW_YORK
    start: "09:30"
    end: "16:00"
    tz: America/New_York

# Canon algorithm (optional — for self-contained strategies like ARS)
canon_algorithm: ars | null     # if set, bypasses Map+Chain entirely
```

### What a cartridge DECLARES:
- Which console capabilities to activate (Map yes/no, which PDAs, which TFs)
- Parameter values for chain evaluation
- Risk and governance parameters
- Time windows for operation

### What a cartridge does NOT declare:
- Detection logic (owned by primitives)
- How the Map works (owned by console/map)
- How the chain evaluates (owned by console/chain)
- Governance mechanics (owned by console/governance)
- Any executable code whatsoever

### Cartridge validation:
- `loader.py` validates every cartridge on load against `CartridgeSpec`
- Unknown fields are rejected (no silent drift)
- Every field maps to a known console capability
- If a cartridge requests a capability the console doesn't have, load fails with a clear error

---

## 5. KEY ARCHITECTURAL INVARIANTS

```yaml
# Detection
INV-DETECTION-SINGLETON: "Each primitive has exactly one implementation in primitives/"
INV-DETECTION-STATELESS: "Detectors are pure functions: bars in → detections out"
INV-DETECTION-TZ-AWARE: "Every Detection.time is timezone-aware at construction"

# Two Clocks
INV-MAP-NEVER-TRADES: "The Map never fires a trade. It answers WHERE."
INV-CHAIN-NEVER-DIRECTS: "The Chain never decides direction. It answers HOW."
INV-TWO-CLOCK-SEPARATION: "No module may both update Map state and evaluate Chain"

# Governance
INV-SOVEREIGN-ABSOLUTE: "Human sovereignty over capital is absolute"
INV-GOVERNANCE-SINGLE-SITE: "check_governance() is the sole authorization function"
INV-LIVE-REQUIRES-HUMAN: "LIVE mode requires explicit human T2 approval"
INV-NO-UNGOVERNED-TRADE: "Every broker interaction preceded by check_governance()"
INV-GOVERNANCE-NO-STATE-MUTATION: "Governance never mutates Map/PDA/structural state"
INV-PAPER-LIVE-PARITY: "PAPER and LIVE have identical governance deps"

# Determinism
INV-REPLAY-DETERMINISM: "Same stored inputs → byte-identical outputs"
INV-NO-IMPLICIT-STATE: "All state that affects output is explicitly captured in trace"

# Cartridge Boundary
INV-CARTRIDGE-PURE-DECLARATION: "Cartridges contain zero executable code"
INV-CONSOLE-STRATEGY-BLIND: "No console module references a specific cartridge"
INV-NEW-CARTRIDGE-NO-CONSOLE-CHANGE: "Adding a cartridge never modifies console/"
INV-BOUNDARY-CLASSIFIABLE: "Every change is classifiable as console or cartridge work"

# Methodology
INV-OLYA-ABSOLUTE: "Olya's NO on any detection/methodology question is final"
INV-VLOCK: "13 primitives locked. Changes require Olya recalibration."
INV-PDA-LIFECYCLE: "OPEN → TOUCHED → REJECTED|MITIGATED|INVALIDATED"

# Orientation
INV-STRUCTURE-TEACHES: "Directory structure alone teaches the architecture"
```

---

## 6. INTERFACE CONTRACTS

### Detection → Map
```python
# Map consumes HTF detections
map_engine.process_detections(detections: List[Detection], bar: Bar) → MapState
```

### Map → Gate
```python
# Gate reads Map state (read-only) + cartridge config
gate.evaluate(map_state: MapState, cartridge: CartridgeSpec, current_time: datetime) → ARMED | DISARMED
```

### Gate → Chain
```python
# Chain only runs when gate is ARMED
chain.evaluate(ltf_bars: List[Bar], config: ChainConfig) → Optional[ChainResult]
```

### Chain → Intent
```python
# Intent built from chain result + cartridge risk params
intent.build(chain_result: ChainResult, cartridge: CartridgeSpec, map_state: MapState) → TradeIntent
```

### Intent → Governance → Broker
```python
# Governance check before any broker interaction
result = governance.check(mode, halt, lease, risk, limits)
if result.allowed:
    broker.execute(intent)
```

### Orchestrator wiring (not a contract — just sequencing)
```
River.next_bar()
  → aggregator.process(bar)
  → primitives.detect(htf_bars)
  → map.process_detections(htf_detections)
  → day_state.process(htf_detections)
  → primitives.detect(ltf_bars)
  → gate.evaluate(map_state, cartridge)
  → if ARMED: chain.evaluate(ltf_bars, chain_config)
  → if chain_result: intent.build(chain_result)
  → governance.check(intent)
  → if allowed: broker.execute(intent)
  → trace.log(decision)
```

---

## 7. ORIENTATION SIGNALS

A fresh agent landing in this repo should understand the architecture within minutes:

1. **Directory names are the architecture.** `console/` vs `cartridges/` is the primary split. Inside `console/`, the numbered layers (primitives → map → chain → governance → execution) tell the data flow story.

2. **README.md** contains a single paragraph + the directory tree + a pointer to ARCHITECTURE.md. Nothing else.

3. **ARCHITECTURE.md** (this document) is the canonical structural reference. It fits in one file.

4. **Cartridges are YAML files in `cartridges/`.** A new agent can read any cartridge and understand what the strategy does without reading any Python.

5. **Tests mirror the source structure.** `tests/unit/` parallels `console/`, `tests/contract/` tests extraction parity and invariants, `tests/scenario/` runs full trade sequences.

6. **methodology/** is read-only reference. It's not code. It's Olya's locked rulings.

7. **The orchestrator is dumb.** It sequences and wires. It never decides. Reading `orchestrator/runtime.py` shows the full data flow in one file.

---

## 8. TENSIONS AND OPEN QUESTIONS

### Tension 1: Canon algorithms vs. chain universality
ARS has its own self-contained algorithm that bypasses the Map entirely. This means
the console must support two paths: map-gated (Chain) and direct (canon algorithm).
The `canon_algorithm` field in CartridgeSpec handles this, but it creates a bifurcation
in the orchestrator. This is acceptable if canon algorithms are rare (ARS is the only
one currently); it would be problematic if many cartridges needed custom algorithms.

### Tension 2: Dealing range cascade is methodology, not configuration
The daily → H4 cascade when daily DR is still expanding is a methodology rule, not a
cartridge parameter. It should live in `console/map/dealing_range.py`, not be configurable
per cartridge. But the cartridge declares `cascade_tf: H4` — is this configuration or
methodology? My design puts the cascade logic in the console and the TF selection in the
cartridge, which may create ambiguity.

### Tension 3: PDA mitigation semantics vary by PDA type
FVG mitigation (retrace-fill) is different from OB mitigation (which isn't defined yet).
This means `pda.py` needs type-dispatched mitigation logic. The cartridge declares which
PDA types to track, but the mitigation rules are console logic. This is clean today (v1:
FVG only) but will need careful design when OB/iFVG are added.

### Tension 4: Observability placement
Tracing and replay are cross-cutting concerns. They don't fit cleanly into a single layer.
I've placed them in `observe/` at the top level (not inside `console/`) because they
observe the console rather than being part of it. But they need to instrument every layer,
which creates coupling.

---

## 9. WHAT I WOULD BUILD FIRST

1. `console/primitives/` — detection singleton with one primitive (FVG) proven
2. `console/data/` — bar types + aggregator
3. `console/map/` — regime + dealing range + PDA store
4. `console/chain/` — evaluator + gate
5. `console/governance/` — halt + lease + risk + check_governance()
6. `cartridges/schema.py` + `loader.py` — the cartridge contract
7. `cartridges/daily_expansion.yaml` — first real cartridge
8. `orchestrator/` — wire it all together
9. `observe/` — trace + replay
10. `cartridges/ars_v1_3.yaml` + `orchestrator/direct_session.py` — second path

This ordering ensures the console is proven before any cartridge loads, and the
cartridge contract is validated before the second strategy is added.
