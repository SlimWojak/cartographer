# NORTH STAR
# en1gma — Why We Exist and Where We're Going

```yaml
document: NORTH_STAR
version: 1.0
date: 2026-03-30
status: CANONICAL
owner: G (Sovereign Operator)
audience: G, CTO, advisors, future humans
purpose: Strategic vision. Not implementation detail.
rule: "If it doesn't answer WHY or WHERE, it doesn't belong here."
```

---

## 1. IDENTITY

en1gma is a constitutional algorithmic trading system that reads
market structure, holds persistent spatial context, and executes
entries when structure and context align — under sovereign human
governance.

```yaml
core_loop:
  human_frames: "G and Olya define what to look for"
  machine_computes: "en1gma detects, contextualises, and gates"
  human_promotes: "Olya validates. G approves capital."
  machine_refines: "Dream Cycle mines failures into sharper detection"

one_sentence: |
  en1gma systematises Olya's discretionary trading expertise
  into a deterministic, governable, self-improving system —
  where human sovereignty over capital is absolute.
```

---

## 2. CORE PRINCIPLES

```yaml
sovereignty: |
  Human sovereignty over capital is absolute and non-negotiable.
  No trade executes without governance approval. No algorithm
  overrides the operator. Halt wins over everything, always.

measure_twice: |
  Quality over speed. Permanent final form over expedient hacks.
  If full implementation takes 3 days but is correct — do it.
  If a shortcut takes 3 hours but creates debt — don't.

methodology_authority: |
  Olya is the sole authority on trading methodology.
  Her NO on any detection or strategy decision is final.
  Code changes to match methodology, not the reverse.
  INV-OLYA-ABSOLUTE.

detection_fidelity: |
  The system's job is detection fidelity — presenting the market
  structure honestly. The edge comes from Olya's calibrated
  filters on top of faithful detection. Raw detection ≠ edge.
  Calibrated detection + discipline = edge.

strategy_as_configuration: |
  A "strategy" is not a codebase. It is a configuration of the Map —
  which regime to require, which PDAs to track, which zone to demand.
  The execution chain is infrastructure. It doesn't change.
  New strategy ideas become: "what does the Map look like for this?"

console_cartridge_boundary: |
  en1gma is a CONSOLE + CARTRIDGE system. The console is the universal
  ICT machinery (detection, Map, chain, canon runtime, governance,
  observability) — strategy-blind, shared by all cartridges.
  A cartridge is a YAML declaration that configures which console
  capabilities to activate. ARS and DAILY_EXPANSION are cartridges.
  Every brief, ruling, and change classifies as console work or
  cartridge work, with a declared effect dimension (methodology /
  evaluation / configuration / structure / workflow).
  See docs/canonical/CARTRIDGE_CONTRACT.md for the full contract.
```

---

## 3. THE TWO-CLOCK MODEL

This is the core architectural insight. Everything else follows.

```yaml
slow_clock:
  name: "The Map"
  what: "Persistent spatial model of the market"
  holds: "regime, dealing range, active PDAs, resting liquidity"
  updates: "on structural events only (daily MSS, FVG mitigated, regime change)"
  persistence: "cross-session — objects live for days or weeks"
  character: |
    quiet most of the time. A day with no events means zero updates.
    Most days produce zero Map updates. This is correct — the Map
    holds until structural events force a change. A builder who
    updates the Map more frequently is adding noise, not value.
  answers: "WHERE should we be watching, and in WHICH direction?"

fast_clock:
  name: "The Execution"
  what: "LTF chain evaluation within kill zone windows"
  runs: "sweep → MSS → FVG → OTE → entry"
  updates: "per-bar within kill zone"
  persistence: "intraday — resets each session"
  character: "activates ONLY when Map says 'price is at a live PDA in correct zone'"
  answers: "HOW do we enter, right now, at this location?"

separation: |
  The Map never fires a trade. The Execution never decides direction.
  Direction PERMISSION comes from the Map.
  Execution TRIGGER comes from LTF confirmation inside a map-approved location.
  These responsibilities never cross.
```

---

## 4. THE 5-LAYER SPINE

The spine lives inside the CONSOLE. Cartridges declare which layers to
activate; the console runs them. See `CARTRIDGE_CONTRACT` §2 (what the
console owns) and §3 (what a cartridge declares).

```
CONSOLE (strategy-blind ICT machinery)
  L1 DATA        River → raw bars → canonicalisation → TF aggregation
  L2 DETECTION   detect.py → 13 vLOCK primitives → structural events
  L3 MAP         Regime + dealing range + PDAs (persistent, event-driven)
  L4 CHAIN       Gate (boolean) → LTF chain (sweep→MSS→FVG→OTE→entry)
                 + CANON RUNTIME (registered algorithms — ARS today)
  L5a GOVERNANCE Halt → Lease → Risk → check_governance()  ┐
  L5b EXECUTION  Intent → Broker → Position → Audit        ┘ peers
                                                             both consumed by
                                                             orchestrator

CARTRIDGES (declarations — YAML only, no code)
  identity + map_configuration + chain_parameters + time_windows
  + risk_parameters + (optional) canon_algorithm

ORCHESTRATOR (wiring layer — reads CartridgeSpec, dispatches)
  Path A: canon_algorithm present → canon runner
  Path B: map_required true       → detect → Map → Gate → Chain
```

Governance and execution are **peers** consumed by the orchestrator, not
sequential layers. The import lint rules in CARTRIDGE_IMPLEMENTATION_DRAFT
§4.2 formalize this.

Two execution paths converge at governance:

```yaml
path_a: "ARS: Canon Runner → check_governance() → Broker"
  note: "Self-contained. Bypasses Map. State-independent. Dispatch via
         CANON_RUNNERS registry (console work to register, cartridge
         work to select)."

path_b: "Map-gated: detect.py → Map → Gate → Chain → check_governance() → Broker"
  note: "HTF context required. Map IS the strategy."
```

---

## 5. GOVERNANCE PHILOSOPHY

```yaml
bounded_autonomy: |
  The system operates within explicit bounds (the Lease).
  Within those bounds, it detects and executes autonomously.
  Beyond those bounds, it halts and waits for human instruction.
  Bounds are set by G. Methodology is set by Olya.

constitutional_safety:
  halt: "< 50ms local, < 500ms cascade. Overrides everything."
  lease: "DRAFT → ACTIVE → EXPIRED. Ceremony to renew."
  shadow: "Shadow mode until G signs graduation. No capital at risk."
  live: "Requires explicit T2 human approval. No automated escalation."

graduation_path:
  shadow: "system runs, decisions traced, no trades placed"
  paper: "trades placed on paper broker, P&L tracked, Olya reviews"
  live: "real capital, requires ceremony + T2 + Olya confirmation"
  
  principle: "each step requires demonstrated competence at the prior level"
```

---

## 6. THE PARKED VISION

These ideas are proven or designed but not on the critical path.
They return when their preconditions are met. They are not lost.

```yaml
bead_field:
  what: "Cryptographically anchored knowledge substrate — bi-temporal, provenance-linked, rejection-rich"
  key_principle: "Every fact, claim, and rejection is a signed, immutable bead with full lineage"
  status: "564K beads, 66GB on M3 — built and proven"
  returns_when: "Dream Cycle needs training data from production trading"
  value: "audit trail, forensic replay, training substrate"

dream_cycle:
  what: "The system's learning engine — mines rejected trades, simulates counterfactuals, distils skills"
  key_principle: "DEC-ENERGY-NOT-STORED — energy is COMPUTED over the field, never stored on the substrate"
  key_concept: "Shadow Field — the negative space of what was rejected. Structurally rich failures."
  returns_when: "6+ months of production Map-gated trading data accumulated"
  value: "transforms failures into sharper detection and new strategy configurations"

ceremony_engine:
  what: "Weekly governance attestation — schedule, check, attest, advance"
  returns_when: "paper trading stable, G wants formal review cadence"

bridge:
  what: "Governance event projection into bead field (pull-based notary)"
  returns_when: "bead field actively consumed by Dream Cycle"

principle: |
  The parked vision is not abandoned work. It is future capability
  whose preconditions are being built right now. en1gma builds the
  runtime that generates the data that feeds the Dream Cycle that
  compounds the edge over time. Each layer enables the next.
```

---

## 7. KEY DECISIONS

The architectural pivots that shaped the system:

```yaml
DEC-KERNEL-BIRTH:
  date: 2026-03-29
  what: "Create en1gma as clean runtime kernel from 4 source repos"
  why: "42 sprints of exploration produced correct principles but sprawling structure"
  principle: "System gets SMALLER to get STRONGER"

DEC-MAP-IS-STRATEGY:
  date: 2026-03-28
  what: "HTF Map is the missing architectural layer. Strategies are Map configurations."
  why: "Olya's cognition = persistent spatial model + LTF execution. Two clocks."

DEC-ORACLE-SINGLETON:
  date: 2026-03-27
  what: "detect.py is the sole detection authority. 11 producers archived."
  why: "Multiple producers caused threshold drift from Olya's calibration"

DEC-ARS-BYPASSES-MAP:
  date: 2026-03-29
  what: "ARS is structurally Map-independent. Feature, not hack."
  why: "Self-contained on raw bars. Forcing through Map is artificial."

DEC-5-DRAWER-SUPERSEDED:
  date: 2026-03-29
  what: "Map + Gate replaces 5-drawer CSO evaluation model"
  why: "Map covers Drawers 1-3. LTF chain covers 4-5."

DEC-ENRICHMENT-SUPERSEDED:
  date: 2026-03-29
  what: "Map replaces per-bar enrichment pipeline"
  why: "Persistent spatial context replaces per-bar feature computation"

DEC-ROLLING-DEALING-RANGE:
  date: 2026-03-29
  what: "Dealing range tracks pullback→displacement cycles within regime"
  why: "Olya calibration: origin = highest liquidity before displacement, not MSS origin"
```

---

## 8. THE LONG ARC

```yaml
phase_current: |
  FOUNDATION → EXPANSION transition.
  ARS live on paper. Map-gated path proven (6/6 ground truth).
  Chain evaluator + full wiring operational. 95 tests.
  DMB strategy config + walk-forward validation next.

phase_next: |
  EXPANSION — DMB paper trading alongside ARS.
  Walk-forward validation. Dual strategy on M3.
  Production trading data accumulating.

phase_future: |
  LEARNING — Dream Cycle activated.
  Production trading data feeds bead field.
  Shadow Field mined for failures → new strategies.
  SkillRL distils patterns into tradeable rules.
  System compounds edge over time.

phase_horizon: |
  MULTI-GENERATIONAL — family office infrastructure.
  Multiple pairs. Multiple strategies. Multiple operators.
  The system absorbs expertise, anchors it cryptographically,
  and makes it reproducible across time and people.

timeframe: |
  Each phase earns the next. No skipping.
  Foundation must be proven before expansion.
  Expansion must generate data before learning.
  Learning must demonstrate edge before scaling.
```

---

*"Human frames. Machine computes. Human promotes."*

*The kernel is lean. The vision is long. The principles are permanent.*
