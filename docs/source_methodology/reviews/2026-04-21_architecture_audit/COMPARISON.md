# COMPARISON.md — Phase 3: First-Principles Design vs en1gma Reality
# Author: Claude Opus 4.7 (fresh instance)
# Date: 2026-04-21

## METHOD

For each element of the Phase 2 design, I compare against en1gma's actual
implementation after reading: NORTH_STAR.md, MAP_SPATIAL_PRIMER_v1.md,
HTF_MAP_SPEC_v0_1.yaml, CLAUDE.md, strategy YAMLs, code structure of all
key modules (detect.py, map_engine.py, chain_evaluator.py, execution_gate.py,
governance.py, orchestrator.py, map_orchestrator.py, loader.py, context_types.py,
pda_store.py, regime.py, dealing_range.py).

---

## 1. TOP-LEVEL STRUCTURE

### My Design
```
kernel/
├── console/          # Strategy-blind ICT machinery
│   ├── primitives/   # L1: Detection singleton
│   ├── map/          # L2: HTF spatial context
│   ├── chain/        # L3: LTF execution chain
│   ├── governance/   # L4: Capital safety
│   ├── execution/    # L5: Intent → broker → position
│   └── data/         # L0: Bar types, river, aggregation
├── cartridges/       # Pure YAML strategy declarations + schema + loader
├── orchestrator/     # Wiring layer (sequences console components)
├── observe/          # Tracing, replay, timeline
├── methodology/      # Locked Olya reference (read-only)
├── tests/
├── ground_truth/
└── scripts/
```

### en1gma Reality
```
en1gma/
├── data/             # L1: Bar types, river, aggregation
├── detection/        # L2: detect.py facade + ra_engine/
├── context/          # L3: map_engine, regime, dealing_range, pda_store
├── gating/           # L4 (partial): execution_gate
├── chain/            # L4: chain_evaluator + ARS canon + session state
├── execution/        # L5: intent_builder, broker_adapter, position
├── control/          # L5 + wiring: governance, halt, lease, risk, orchestrator, day_state
├── observe/          # Tracing, replay, timeline
├── strategies/       # YAML configs + loader.py
├── methodology/      # Locked reference
├── tests/
├── ground_truth/
└── scripts/
```

### Verdict: DIVERGENT — structure matters

**The critical difference:** en1gma does NOT have a `console/` vs `cartridges/` directory
split. The console concept is distributed across 6+ top-level packages. The cartridge
concept lives in `strategies/` but shares the same structural level as console packages.

**Why this matters:**

1. **Constraint #8 (fresh agent orientation from structure alone):** A fresh agent landing
   in en1gma sees `data/`, `detection/`, `context/`, `gating/`, `chain/`, `execution/`,
   `control/`, `observe/`, `strategies/` — nine peer directories. The console/cartridge
   boundary is invisible from directory structure. You must read CLAUDE.md to discover it.

2. **Constraint #6 (classifiable as console or cartridge work):** When `strategies/loader.py`
   contains Python code that constructs `StrategyParams` and `GovernanceConfig`, is that
   console work or cartridge work? The loader is *infrastructure* that serves cartridges,
   but it lives in the cartridge directory. My design puts `schema.py` + `loader.py` in
   `cartridges/` too, but the `console/` parent makes the boundary visible.

3. **Constraint #5 (new cartridges require no console changes):** Both designs satisfy
   this — new YAML files in `strategies/` or `cartridges/` don't touch console code.
   But en1gma's flat structure makes it harder to *verify* this constraint at a glance.

**Assessment:** My `console/` grouping is structurally cleaner for orientation (constraint
#8) and boundary visibility (constraint #6). The refactor would be a directory restructure
with zero logic changes — low risk, high orientation value.

**However:** en1gma's flat structure has a pragmatic benefit: fewer nested directories,
shorter import paths. The 5-layer model is well-documented in CLAUDE.md even though it
isn't *embodied* in directory structure. This is a legitimate trade-off.

---

## 2. DETECTION SINGLETON

### My Design
`console/primitives/detect.py` — single facade, one file per primitive, stateless functions.

### en1gma Reality
`detection/detect.py` — single facade wrapping `ra_engine/` (39 vendored files from
the Research Accelerator). Each detector in `ra_engine/detectors/` is one file per primitive.
`run_detection(bars_by_tf, timeframes, config_path)` is the sole entry point.

### Verdict: CONVERGENT

The singleton pattern is identical. en1gma's `ra_engine/` sub-package is more complex than
my design anticipated (it includes evaluation, config, data adapters) but this is the
reality of a vendored extraction from a research tool. The facade pattern (`detect.py` →
`ra_engine/`) cleanly isolates the complexity. The `_common.to_ny_aware()` pattern for
tz-awareness at the source is exactly right.

---

## 3. MAP (HTF SPATIAL CONTEXT)

### My Design
`console/map/` with: engine.py, regime.py, dealing_range.py, pda.py, persistence.py,
types.py, day_state.py

### en1gma Reality
`context/` with: map_engine.py, regime.py, dealing_range.py, pda_store.py,
map_persistence.py, context_types.py, liquidity.py (stub)
`control/day_state.py` (separate from context/)

### Verdict: CONVERGENT with minor divergences

**Convergent elements:**
- MapEngine is the central class (my `engine.py` ≈ their `map_engine.py`)
- RegimeTracker, DealingRangeTracker, PDAStore — identical decomposition
- Persistence as a separate module
- Rich type system (Regime, DealingRange, PDA, MapState, GateResult)

**Minor divergences:**
1. en1gma calls it `context/`, I called it `map/`. The `context/` name is arguably worse
   because "context" is generic — `map/` is specific and teaches the two-clock model.
   **My design is marginally better for orientation.**

2. `day_state.py` lives in `control/` in en1gma, not with the Map. This is a reasonable
   choice (day_state is a control-flow concern, not a spatial concern), but my design
   groups it with the Map because it answers a spatial question ("what phase is the
   market in?"). **Toss-up — both placements are defensible.**

3. en1gma has `context_types.py` as a mega-types file (~200+ lines of enums + dataclasses)
   serving the Map, gate, PDA, dealing range, regime, and liquidity. My design distributes
   types closer to their modules. **en1gma's approach is simpler but creates coupling —
   every module imports from the same types file. Pragmatically fine.**

---

## 4. EXECUTION CHAIN

### My Design
`console/chain/` with: evaluator.py, gate.py, types.py, config.py

### en1gma Reality
`chain/` with: chain_evaluator.py, chain_types.py, chain_config.py
`gating/execution_gate.py` (separate package)

### Verdict: CONVERGENT with one structural divergence

The chain evaluation logic is identical in decomposition: evaluator + types + config.

**Divergence: Gate placement.** en1gma puts the execution gate in its own `gating/`
top-level package. My design puts it in `console/chain/gate.py`. en1gma's choice creates
a 9th peer directory for a single file (`execution_gate.py`). My design keeps gate and
chain together since the gate exists solely to arm the chain.

**Assessment:** My placement is cleaner. A single-file package is a structural smell.
The gate should live next to the chain it arms.

---

## 5. GOVERNANCE

### My Design
`console/governance/` with: governance.py, halt.py, lease.py, risk.py, mode.py, types.py

### en1gma Reality
`control/` with: governance.py, halt.py, lease.py, risk.py — PLUS orchestrator.py,
map_orchestrator.py, day_state.py all in the same package.

### Verdict: DIVERGENT — `control/` conflates governance and orchestration

en1gma's `control/` package contains two fundamentally different concerns:
1. **Governance** (halt, lease, risk, governance.py) — capital safety, the L5 layer
2. **Orchestration** (orchestrator.py, map_orchestrator.py) — wiring, the sequencing layer
3. **Day state** (day_state.py) — a Map/market-structure concern

These are not the same kind of thing. Governance is a constraint layer. Orchestration
is a wiring layer. Day state is a spatial state engine.

My design separates these:
- Governance in `console/governance/`
- Orchestration in `orchestrator/` (top-level)
- Day state in `console/map/`

**Assessment:** en1gma's `control/` package violates constraint #8 (structure teaches
architecture) because a fresh agent looking at `control/` sees 7 files spanning 3
different concerns. Separating governance from orchestration would make the architecture
self-documenting.

---

## 6. THE CARTRIDGE CONTRACT

### My Design
Formal `CartridgeSpec` dataclass in `cartridges/schema.py`. Single unified schema.
All cartridges conform to the same interface. Validation rejects unknown fields.

### en1gma Reality
`StrategyParams` + `GovernanceConfig` in `strategies/loader.py`. Two separate dataclasses.
YAML schemas are NOT uniform — `ars_v1_3.yaml` uses `strategy.name` (nested), while
`daily_expansion.yaml` uses `strategy:` as a top-level string. The ARS YAML has a
completely different shape (asia_range, sweep, fvg, exit sections) that doesn't map
to StrategyParams at all.

### Verdict: DIVERGENT — the cartridge contract is the biggest gap

**This is the most important finding.** The console/cartridge metaphor is articulated
beautifully in en1gma's documentation (NORTH_STAR.md, MAP_SPATIAL_PRIMER_v1.md), but
the code does not fully enforce it:

1. **No unified cartridge schema.** ARS and DAILY_EXPANSION have fundamentally different
   YAML shapes. ARS declares `asia_range`, `sweep`, `fvg`, `exit` sections that are
   strategy-specific implementation parameters. DAILY_EXPANSION declares `pda`, `chain`,
   `execution_windows` that map to console configuration. These are not the same contract.

2. **ARS canon algorithm lives in `chain/ars/`** — a strategy-specific algorithm lives
   inside console infrastructure. This contradicts constraint #5 (new cartridge = no
   console change). If someone wanted to add another self-contained algorithm (like a
   Silver Bullet canon), they'd need to add code to `chain/`.

3. **The loader constructs governance deps.** `build_governance_deps()` in `loader.py`
   instantiates `LeaseStateMachine` and `RiskState` — this is runtime construction logic,
   not cartridge loading. It conflates cartridge parsing with console initialization.

4. **`StrategyParams` has fields that only apply to map-gated paths** (`day_state_requirement`,
   `pda_types`, `pda_timeframes`, `regime_required_phase`). ARS ignores all of these.
   This means StrategyParams is not actually a universal cartridge contract — it's a
   union type with an implicit `if map_required` branch.

**What my design does differently:**
- Single `CartridgeSpec` with explicit `map.required` field
- Map-specific config nested under `map:` (only validated when `map.required: true`)
- Canon algorithm declaration is a field, not a code directory
- ARS's algorithm-specific params would live in the YAML under a `canon_params:` section
  consumed by a generic canon runner, not by strategy-specific Python in `chain/ars/`

**Assessment:** en1gma articulates the cartridge concept in docs but has not yet
fully implemented it in code. The ARS path is a "cartridge" in name but a bespoke
code path in reality. This is the gap most worth closing. The fix: formalize the
cartridge contract, move ARS canon to a registered-algorithm pattern, and unify
the YAML schema.

---

## 7. ORCHESTRATION

### My Design
`orchestrator/` top-level with: runtime.py, map_session.py, direct_session.py

### en1gma Reality
`control/orchestrator.py` (ARS path) and `control/map_orchestrator.py` (Map path)

### Verdict: CONVERGENT on decomposition, DIVERGENT on placement

Both designs have two orchestrators — one for map-gated, one for direct/ARS. en1gma's
`run_ars_session()` and `run_map_replay()` are functionally equivalent to my
`direct_session.py` and `map_session.py`.

The divergence is placement: en1gma buries orchestrators in `control/` alongside
governance. My design gives orchestration its own top-level directory, which makes
the wiring layer visible from structure.

`map_orchestrator.py` is also the largest file in the system (600+ lines) and handles
date iteration, bar filtering, detection, map processing, chain evaluation, governance,
broker execution, tracing, and result collection — all in one function. This is
appropriate for a wiring layer (INV-ORCHESTRATOR-DUMB), but the size suggests it
could benefit from decomposition into smaller wiring functions.

---

## 8. OBSERVABILITY

### My Design
`observe/` with: trace.py, replay.py, timeline.py, snapshot.py

### en1gma Reality
`observe/` with: decision_trace.py, replay.py, map_timeline.py, state_snapshot.py

### Verdict: CONVERGENT

Near-identical. Same decomposition, same placement. File naming differs trivially.

---

## 9. INVARIANTS

### My Design
17 invariants organized by concern (detection, two-clocks, governance, determinism,
cartridge boundary, methodology, orientation).

### en1gma Reality
25+ invariants in CLAUDE.md, organized by concern (sovereignty, safety, detection,
architecture, methodology, governance).

### Verdict: CONVERGENT with additions

en1gma has MORE invariants than my design, including:
- INV-REPLAY-DETERMINISM (I had this)
- INV-SESSION-STATE-PROGRESSION (I didn't have this — ARS daemon restart safety)
- INV-PDA-DIRECTION-FIDELITY (I didn't have this — direction from detector, not regime)
- INV-PDA-ZONE-FROM-DETECTOR (I didn't have this — zone bounds from detector properties)
- INV-PDA-MITIGATION-IS-RETRACE-FILL (I didn't have this — FVG mitigation semantic)
- INV-PDA-CREATED-AT-CONFIRMATION (I didn't have this — created_at = Candle C close)

These are battle-tested invariants discovered through implementation. My design
couldn't have anticipated them without building the system. This is expected and healthy.

**Notable:** en1gma does NOT have explicit invariants for the cartridge boundary
(my INV-CARTRIDGE-PURE-DECLARATION, INV-CONSOLE-STRATEGY-BLIND, INV-NEW-CARTRIDGE-NO-CONSOLE-CHANGE).
This absence correlates with the cartridge contract gap identified in §6.

---

## 10. TWO-CLOCK SEPARATION

### My Design
INV-MAP-NEVER-TRADES, INV-CHAIN-NEVER-DIRECTS, INV-TWO-CLOCK-SEPARATION

### en1gma Reality
Extensively documented in NORTH_STAR.md, MAP_SPATIAL_PRIMER_v1.md, CLAUDE.md.
"The Map never fires a trade. The Execution never decides direction."

### Verdict: CONVERGENT

The two-clock model is the foundational insight of both designs. en1gma articulates
it more richly (the MAP_SPATIAL_PRIMER is an exceptional document — the spatial-vs-checklist
distinction is a genuinely novel way to communicate the architecture to agents). My design
converges completely on the principle; en1gma's documentation of it is superior.

---

## 11. ELEMENTS MISSING IN EN1GMA (present in my design)

### 11a. Explicit console/cartridge directory boundary
**What:** A `console/` parent directory grouping all strategy-blind machinery.
**Why it matters:** Constraint #8 — structure teaches architecture. Today the
boundary exists in documentation but not in directory layout.

### 11b. Formal cartridge contract invariants
**What:** INV-CARTRIDGE-PURE-DECLARATION, INV-CONSOLE-STRATEGY-BLIND,
INV-NEW-CARTRIDGE-NO-CONSOLE-CHANGE
**Why it matters:** Without these invariants, the cartridge boundary can drift
(and HAS drifted — ARS canon code lives in `chain/ars/`).

### 11c. Unified cartridge YAML schema
**What:** A single CartridgeSpec that both ARS and DAILY_EXPANSION conform to.
**Why it matters:** Constraint #7 — Olya's bounded creative surface. If different
cartridges have different YAML shapes, the "fill in a declared interface" promise
breaks down.

### 11d. Gate lives with chain
**What:** Gate in the same package as chain evaluator.
**Why it matters:** Reduces package count, keeps related concerns together.

---

## 12. ELEMENTS MISSING IN MY DESIGN (present in en1gma)

### 12a. ARS session state + checkpoint + recovery
**What:** `chain/ars/session_state.py`, `checkpoint.py`, `recovery.py` — daemon
restart safety for the live ARS trading session. Append-only JSONL checkpoint,
four recovery paths (FAST/SLOW/FRESH/OUT_OF_WINDOW).
**Should my design include it?** YES. I under-specified the operational resilience
layer. A production trading daemon MUST handle process restarts gracefully. This
is essential infrastructure I overlooked.

### 12b. DR authority cascade (daily → H4)
**What:** `is_daily_range_valid()` in `dealing_range.py` — when daily DR is still
expanding, cascade to H4 for zone classification.
**Should my design include it?** YES, as console logic. I mentioned it in Tension 2
but didn't fully resolve it. en1gma correctly puts this in the dealing range module
as methodology logic, not cartridge configuration.

### 12c. Ground truth traces as test fixtures
**What:** `traces/ground_truth/trade_001/` through `trade_013/` with full
decision_trace, chain_trace, map_timeline, and session_summary per trade.
**Should my design include it?** YES. This is how determinism (constraint #4) is
verified in practice. My design mentioned ground_truth but didn't specify the
per-trade trace artifact structure.

### 12d. Sentinel + Henry (operational monitoring agents)
**What:** Gemma-based always-on monitor + GLM forensic analyst.
**Should my design include it?** Not in the kernel itself, but the `ops/` directory
in my design is the right home. en1gma puts these in `scripts/`, which is adequate
but doesn't distinguish operational tooling from development scripts.

### 12e. MAP_SPATIAL_PRIMER — the "how to think" document
**What:** A document that teaches agents to reason about the Map as a spatial model,
not a filter chain, with anti-patterns and self-check questions.
**Should my design include it?** YES. This is a remarkable orientation artifact that
directly serves constraint #8. My design's ARCHITECTURE.md doesn't include this
cognitive guidance. en1gma's documentation is significantly richer than what I proposed.

### 12f. Extensive calibration infrastructure
**What:** `calibration_results.yaml` (27 Olya answers), calibration scripts,
ground truth annotations. The methodology/ directory serves as a locked,
Olya-ratified reference — not just documentation, but a conformance surface.
**Should my design include it?** YES, I had `methodology/` but under-specified its
role as a CONFORMANCE surface, not just documentation.

---

## 13. OVERALL VERDICT

### PARTIAL CONVERGENCE

The core architectural decisions converge strongly:
- Two-clock model (Map + Chain with strict separation) ✅
- Detection singleton ✅
- Governance as constraint layer with single check site ✅
- Observability via decision trace + replay ✅
- Strategy as configuration (YAML) not code ✅
- Invariant-driven development ✅
- Three test tiers (unit, contract, scenario) ✅

The meaningful divergences are:

| # | Element | Severity | Assessment |
|---|---------|----------|------------|
| 1 | **Cartridge contract formalization** | HIGH | en1gma articulates the metaphor beautifully but the code has gaps: non-uniform YAML schemas, ARS canon code in console, no cartridge boundary invariants. This is the gap most worth closing. |
| 2 | **Directory structure as architecture** | MEDIUM | en1gma's flat structure (9 peer packages) doesn't embody the console/cartridge boundary. A `console/` grouping would make the architecture self-documenting per constraint #8. Trade-off: deeper nesting vs. orientation clarity. |
| 3 | **control/ conflation** | MEDIUM | Governance + orchestration + day_state in one package obscures three distinct concerns. Separating them would improve fresh-agent orientation. |
| 4 | **Gate placement** | LOW | Single-file `gating/` package is minor structural noise. |

Elements where en1gma is STRONGER than my first-principles design:

| # | Element | Note |
|---|---------|------|
| 1 | **Battle-tested invariants** | 25+ invariants discovered through implementation — PDA direction fidelity, zone-from-detector, mitigation semantics. Can't be derived from first principles. |
| 2 | **MAP_SPATIAL_PRIMER** | Exceptional cognitive orientation document. My design has nothing equivalent. |
| 3 | **Session state + checkpoint + recovery** | Production resilience I overlooked entirely. |
| 4 | **DR authority cascade** | Methodology-correct dealing range fallback I noted as a tension but didn't resolve. |
| 5 | **Documentation depth** | CLAUDE.md, NORTH_STAR.md, calibration results, handover docs, brief pattern — en1gma's documentation surface is significantly richer. |

### Final Assessment

en1gma arrived at near-optimal architecture through iteration. The core design
decisions are correct and battle-proven. The primary improvement opportunity is
**formalizing the cartridge boundary** — making the console/cartridge split visible
in code structure, enforcing a unified cartridge contract, and moving ARS-specific
code out of console infrastructure. This would close the gap between en1gma's
excellent documentation (which clearly articulates the console/cartridge metaphor)
and its code (which doesn't yet fully embody it).

The system is not divergent from optimal — it is 80-85% converged, with the
remaining 15-20% being structural formalization of an already-understood concept.

---

*"The kernel is lean. The kernel is canonical. The documentation knows what the
code should become. The code is catching up."*
