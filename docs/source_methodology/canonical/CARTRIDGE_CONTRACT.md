# CARTRIDGE CONTRACT — en1gma Architectural Interface

```yaml
document: CARTRIDGE_CONTRACT
version: 1.0.3 (CANONICAL)
date: 2026-04-21
status: CANONICAL — ratified by G on 2026-04-21; v1.0.1 patch amendment 2026-04-21 evening; v1.0.2 patch amendment 2026-04-21 (Phase 2.5 A1 consolidation ship); v1.0.3 patch amendment 2026-04-21 (Phase 2.5 closeout — intent_id format rationale recorded)
owner: G (Sovereign Operator), Chairperson (architectural steward)
authority_tier: 1 (alongside NORTH_STAR, MAP_SPATIAL_PRIMER)
purpose: |
  Define the formal boundary between en1gma's universal ICT machinery
  (the CONSOLE) and its strategy declarations (the CARTRIDGES).
  This document is the primary orientation surface for every agent
  and every decision in the project.
rule: |
  If a ruling, brief, or change cannot be classified as console work
  or cartridge work against this contract, stop and escalate.
```

```yaml
changelog:
  v1.0.3 (2026-04-21, Phase 2.5 closeout — intent_id format rationale recorded):
    status: CANONICAL (patch amendment — no schema change, no new invariant, no breaking change)
    amendment: |
      Record the rationale for the intent_id format collapse that
      shipped inside Phase 2.5 Brief 1 §A2 (intent_builder cartridge-
      neutral neutralization, commit c542c94). The format change was
      ratified by G in conversation during §A2 review (Deviation 2 in
      the Brief 1 reply) but never formally anchored in a canonical
      doc. This entry gives future readers tracing intent_id history
      a discoverable audit trail without retroactively editing v1.0.2.

      Format transition:
        pre-§A2 (two-function split):
          chain path : "MAP-{strategy}-{YYYYMMDD-HHMMSS}"
          ARS  path  : "ARS-{session_date}-{HHMMSS}"
        post-§A2 (cartridge-neutral single-function):
          all paths  : "{STRATEGY_UPPER}-{intent_id_context}-{HHMMSS}"

      Rationale for the collapse:
        - The "MAP-" and "ARS-" prefixes were artifacts of the
          two-function split (build_intent_from_chain vs
          build_intent_from_ars). They disambiguated which function
          had produced the intent, not the strategy itself.
        - §A2 collapsed both producers into a single
          build_intent(CanonIntent) function. The prefix distinction
          has no producer-function to disambiguate.
        - Forensic value of the old prefix ("this came from the chain
          path" vs "this came from ARS") is now carried by the
          strategy name itself (DAILY_EXPANSION vs ARS_V1_3) because
          the two-function split no longer leaks at the format level.
        - intent_id_context preserved per (a-thin) pattern — retains
          session_date forensic anchor for ARS, strategy name for
          chain cartridges.

    body_changes:
      - "Changelog entry only — records the format rationale that shipped under v1.0.2 §A2 work."
      - "No body section edits. No invariant added. No schema change."

    relationship_to_existing:
      - "Phase 2.5 Brief 1 §A2 (commit c542c94): the implementation ship that carried this change."
      - "CanonIntent.intent_id_context (en1gma/execution/intent_types.py): the cartridge-supplied context string the new format consumes."
      - "§10 no-retroactive rule: honored — this is a NEW version entry recording ratified history, not an edit to v1.0.2."
      - "Operational observable: test_map_wiring::TestIntentFromChain updated in c542c94 to assert 'DAILY_EXPANSION-' prefix post-collapse (was 'MAP-' pre-collapse)."

    unchanged: "All schema, all fourteen cartridge-boundary invariants, all §1-§12 body content verbatim from v1.0.2"

  v1.0.2 (2026-04-21, Phase 2.5 §A1 consolidation ship):
    status: CANONICAL (patch amendment — no schema change, no breaking change)
    amendment: |
      Register INV-PDA-MITIGATION-SINGLE-SITE in §6 as the auditable
      structural invariant protecting the Phase 2.5 §A1 consolidation
      (duplicate FVG retrace-fill mitigation logic in pda_store +
      map_engine collapsed to a single authoritative site per Olya/NEX
      methodology ruling 2026-04-21: "PDA mitigation is PDA lifecycle
      logic. Lifecycle ownership belongs to pda_store by responsibility
      and name. map_engine should consume PDA state, not define PDA
      state transitions.").
    body_changes:
      - "§6 adds INV-PDA-MITIGATION-SINGLE-SITE to the CARTRIDGE_BOUNDARY / STRUCTURAL_COHERENCE invariant set with auditable violation clause"
    relationship_to_existing:
      - "INV-PDA-MITIGATION-IS-RETRACE-FILL (CLAUDE.md §6, SW01): methodology — WHAT the semantic is. Retained verbatim."
      - "INV-PDA-MITIGATION-SINGLE-SITE: structural — WHERE the semantic lives. Protects against silent parallel-implementation drift."
      - "INV-NO-REIMPLEMENTATION: parallel principle for extracted modules; this extends it to within-module lifecycle logic."
      - "INV-STRUCTURAL-REFACTOR-NO-SEMANTIC-DRIFT: protected the consolidation itself (151/151 ARS + ground truth parity held; comparison test 6/6 pre and post)."
    unchanged: "All schema, all thirteen other cartridge-boundary invariants (now fourteen including this one), all other section content verbatim from v1.0.1"
  v1.0.1 (2026-04-21 evening, post-Phase-1-canonicalization):
    status: CANONICAL (patch amendment — no schema change, no breaking change)
    amendment: |
      Register INV-DAY-STATE-MAP-COHERENT in §6 per Olya methodology
      ruling 2026-04-21. Day_state derives from the same structural
      primitives (MSS + displacement) that drive regime and dealing-
      range updates — it is part of the unified Map read, not a
      parallel computation.
    body_changes:
      - "§6 adds INV-DAY-STATE-MAP-COHERENT to the CARTRIDGE_BOUNDARY / STRUCTURAL_COHERENCE invariant set with auditable violation clause"
    relationship_to_existing:
      - "INV-DAY-STATE-MARKET-DRIVEN (CLAUDE.md §6): weaker form — constrains the trigger source only. Retained."
      - "INV-DAY-STATE-MAP-COHERENT: stronger structural form — constrains the derivation pipeline."
      - "INV-NO-REIMPLEMENTATION: parallel principle for extracted modules; this extends it to derivation logic across modules."
    resolved_open_questions_from_implementation_draft:
      Q3_day_state_placement: "console/map/day_state.py confirmed; Olya ruling"
    unchanged: "All schema, all twelve other cartridge-boundary invariants, all other section content verbatim from v1.0"
  v1.0 (2026-04-21):
    status: CANONICAL (ratified by G)
    resolutions_absorbed:
      flag_1_ote_entry_levels: "BUNDLE_WITH_DF-02 — defers to Block 4"
      flag_2_sweep_model: "DEFER_TO_RETRACE_RANGE_DESIGN — defers to Map v2"
      flag_3_trace_determinism: "COMMIT_TO_STRONGER_INVARIANT — registered as written, single-cartridge runtime trivially satisfies"
    body_changes:
      - "Added §12 Flag Resolutions (absorbs v0.2 §11 flags with ratified dispositions)"
      - "Single-sentence clarification added to INV-TRACE-DETERMINISM-BY-CARTRIDGE in §6"
      - "v0.2 §11 FLAGS section preserved as §11 with pointer to §12 for dispositions"
    unchanged: "All schema, all other invariants, all other section content verbatim from v0.2"
  v0.2 (2026-04-21):
    tightenings_absorbed:
      T1: "canon runtime as console infrastructure — explicit registry, stateful canon runner interface, INV-CANON-RUNTIME-FIXED"
      T2: "effect classification field alongside scope on every brief / ruling / change"
      T3: "(v2) markers on non-existent schema fields + loader rejection; INV-CONSOLE-NO-CARTRIDGE-SHAPED-BRANCHES; INV-TRACE-DETERMINISM-BY-CARTRIDGE; INV-STRUCTURAL-REFACTOR-NO-SEMANTIC-DRIFT"
    reviewers: [NEX (methodology), Opus-RepoPrompt (engineering)]
    status: "DRAFT — pending second review cycle before canonicalization"
    sections_touched: [§2, §3, new §5A, §6, §7, §8, new §11 flags]
  v0.1 (2026-04-21):
    initial_draft: "Chairperson synthesis; ten immovable constraints; seven cartridge boundary invariants; phased sequencing."
```

---

## 1. THE GOVERNING METAPHOR

en1gma is a CONSOLE + CARTRIDGE system.

The **CONSOLE** is a single, stable platform that encodes Olya's ICT methodology precisely. It understands primitives, HTF spatial reasoning, the LTF execution chain, governance, and observability. It is strategy-blind — it does not know which cartridge is loaded.

**CARTRIDGES** are discrete strategy declarations. Each cartridge is a complete "game" that configures which console capabilities to activate. Different cartridges are different games running on the same console. ARS is a simple game. DAILY_EXPANSION is more complex. Future cartridges (RETRACE, RANGE, SILVER_BULLET) will be authored within the same contract.

The console is the swiss watch. Cartridges are the creative surface.

---

## 2. WHAT THE CONSOLE OWNS

The console is the authoritative encoding of ICT methodology. It owns:

```yaml
detection:
  - The 13 vLOCK primitives (FVG, MSS, sweep, displacement, OB, IFVG,
    BPR, swing points, session boundaries, PDH/PDL, liquidity, OTE,
    asia range)
  - Detection singleton (detect.py is the sole oracle)
  - The methodology definitions of each primitive — what a sweep IS,
    what mitigation MEANS, what direction conventions apply

map_and_spatial_context:
  - Regime detection and tracking
  - Dealing range mechanics (wick-to-wick, rolling supersession,
    daily → H4 authority cascade)
  - PDA lifecycle (OPEN → TOUCHED → REJECTED | MITIGATED | INVALIDATED)
  - Day state FSM (PRE_EXPANSION / POST_EXPANSION)
  - Map persistence across sessions

execution_chain:
  - The universal chain topology: sweep → MSS → FVG → OTE → entry
  - The execution gate's boolean logic (4 conditions for ARMED)
  - Chain evaluator mechanics
  - LTF → HTF relationship logic

canon_runtime:                # NEW in v0.2 (T1) — see §5A
  - The canon runner registry, dispatch, and interface (stateful or stateless)
  - Every registered canon algorithm (ARS today; future canons as registered)
  - Session state / checkpoint / recovery machinery available to canons

governance_and_safety:
  - Halt, lease, risk state machines
  - check_governance() as the single authorization function
  - Operating mode enforcement (TEST / SHADOW / PAPER / LIVE)
  - Broker interface

infrastructure:
  - Data ingestion (River, bar types, TF aggregation)
  - Observability (decision trace, replay, map timeline)
  - Cartridge loader and contract validation

naming_and_vocabulary:
  - Universal ICT terminology: "bearish sweep" means one specific thing,
    documented once, consumed identically everywhere
  - Temporal evaluation semantics (point-in-time vs window vs terminal)
  - All invariants that apply to any cartridge
```

**The console never asks "which cartridge am I running?"** Console code contains zero references to specific cartridges by name.

---

## 3. WHAT A CARTRIDGE OWNS

A cartridge is a declaration of which console capabilities to activate and how to parameterize them. A cartridge declares:

```yaml
identity:
  name: string              # unique identifier (e.g. "ARS_v1_3", "DAILY_EXPANSION")
  family: string            # strategy family grouping
  version: semver
  description: string       # what this game is, in Olya's words

map_configuration:
  map_required: bool        # does this cartridge use the HTF Map?
  # Fields below apply only if map_required: true
  regime_requirement:
    direction: BEARISH | BULLISH | EITHER
    phase: EXPANSION | RETRACE | RANGE | ANY
  dealing_range:
    primary_tf: DAILY | H4
    cascade_tf: H4 | NONE   # fallback when primary is expanding
  pda:
    types: [FVG, OB, IFVG, ...]    # which PDA types arm the gate
    timeframes: [DAILY, H4, ...]   # which TFs create PDAs
    zone_requirement: PREMIUM | DISCOUNT | EITHER
  day_state:
    required: PRE_EXPANSION | POST_EXPANSION | ANY

liquidity_targets: (v2)     # console does not yet consume this block
  external_pools: [asia_high, asia_low, pwh, pwl, equal_highs, ...]
  internal_pools: [swing_high, swing_low, ...]
  priority_order: [list]    # if multiple valid, which matters first

chain_parameters:           # tuning for the universal chain
  sweep_lookback_hours: float
  mss_min_quality: VALID | STRONG        # (v2) — not consumed today
  fvg_min_size_pips: float
  ote_entry_levels: [0.50, 0.618, 0.705, 0.79]   # (v2) — today's console
                                                  # consumes ote_fib: float
                                                  # and ote_zone: (lo, hi)
  min_rr: float
  max_chain_bars: int       # declared; SW13 flags enforcement gap
  sweep_model: REVERSAL | CONTINUATION    # (v2) — not consumed today

time_windows:
  kill_zones:
    - name: LOKZ
      start: "HH:MM"
      end: "HH:MM"
      tz: America/New_York
    - name: NYOKZ
      start: "HH:MM"
      end: "HH:MM"
      tz: America/New_York
  session_cutoff: "HH:MM"    # no new setups after

risk_parameters:
  max_risk_per_trade_R: float
  max_trades_per_day: int
  max_daily_loss_R: float
  governance_profile: string  # references a governance config

canon_algorithm:              # optional, for Map-independent cartridges
  name: string                # e.g. "ars_canon_v1_3" — must be registered
                              # in the console's CANON_RUNNERS registry
  params: {...}               # algorithm-specific parameters, validated by
                              # the registered canon's params schema
  # When present, bypasses Map+Chain; console dispatches to canon runner.
  # Selecting an existing canon_algorithm is CARTRIDGE work.
  # Introducing or modifying a canon runtime is CONSOLE work (see §5A, §6).
```

**A cartridge declares ONLY. It contains no executable code.**

### 3.1 `(v2)` marker discipline

A field marked `(v2)` is reserved vocabulary the console does not yet consume. Cartridges must not declare `(v2)` fields today — the loader rejects any cartridge that carries a `(v2)` field until the corresponding console capability ships. The markers exist so that cartridge authors see the planned surface without mistaking it for supported behavior.

When a `(v2)` capability ships, its marker is removed here and the loader's strict-mode schema is extended in the same commit. `(v2)` markers are lifted only by the commit that ships the corresponding console capability.

---

## 4. WHAT A CARTRIDGE MUST NEVER DO

These are the hard boundaries. A cartridge attempting any of these violates the contract:

- Modify detection logic or primitive definitions
- Redefine what a sweep, MSS, FVG, OTE, or any ICT primitive means
- Modify the execution chain topology (adding, removing, or reordering steps)
- Modify gate logic or add new gate conditions
- Modify PDA lifecycle semantics
- Modify governance mechanics
- Contain executable code (Python, shell, or otherwise — only YAML declarations)
- Import from other cartridges
- Assume the presence of any other specific cartridge
- Declare a `canon_algorithm.name` that is not registered in the console
- Declare a `(v2)` field before the corresponding console capability ships

**If a strategy idea requires any of the above, it is not a cartridge change — it is a console change, which requires methodology review and Olya's recalibration authority.**

---

## 5. THE CARTRIDGE LOADER CONTRACT

The cartridge loader is console infrastructure. It is the only component that reads cartridge YAML. Its responsibilities:

```yaml
on_load:
  - Parse YAML into CartridgeSpec dataclass
  - Validate against schema (strict: unknown fields rejected)
  - Reject any (v2)-marked field that has no corresponding console capability
  - Verify every declared capability maps to a known console capability
  - Verify declared values are within allowed ranges
  - If map_required: false, verify canon_algorithm is declared AND
    canon_algorithm.name is registered in CANON_RUNNERS AND
    canon_algorithm.params validates against that runner's params schema
  - If map_required: true, verify all map_configuration fields are present
  - Emit CartridgeSpec object to orchestrator

on_runtime:
  - Loader is not consulted after load
  - Console reads CartridgeSpec fields as configuration inputs
  - Cartridge declarations are immutable during a session

on_failure:
  - Fail closed: invalid cartridge does not load
  - Clear error message naming the specific field and rule violated
  - No partial loads
```

---

## 5A. CANON RUNNER CONTRACT (NEW in v0.2 — T1)

Some cartridges bypass the Map+Chain pipeline and run a self-contained canon algorithm (today: ARS). The canon runtime is console infrastructure. Cartridges select from it; they do not author it.

### 5A.1 Registration pattern

Registration is **explicit**, not decorator-based.

```python
# console/chain/canon/registry.py (illustrative location)
from .ars.runner import ARSRunner

CANON_RUNNERS: dict[str, type[CanonRunner]] = {
    "ars_canon_v1_3": ARSRunner,
    # Every registered canon appears here. One file shows the full set.
}
```

Rationale: auditability and deterministic visibility outweigh the ergonomics of decorator-based auto-discovery. Anyone asking "what canons does this console support?" reads one file and gets a complete answer. Adding an entry to `CANON_RUNNERS` is **console work**, gated by methodology review per §7 and INV-CANON-RUNTIME-FIXED.

### 5A.2 Canon runner interface

Canon algorithms are not uniform. ARS has session state, checkpoints, recovery paths, and phase progression. Future stateless canons may declare none of these. The interface accommodates both.

```python
class CanonRunner(Protocol):
    # Required
    name: str                                        # matches CANON_RUNNERS key
    params_schema: type                              # dataclass / pydantic model
    def run(self, ctx: CanonContext) -> CanonResult: ...

    # Optional — declared by stateful canons only
    session_state_type: type | None = None           # e.g. SessionState (ARS)
    checkpoint_path: Path | None = None              # where JSONL checkpoint lives
    recovery_strategy: RecoveryStrategy | None = None  # FAST/SLOW/FRESH/OUT_OF_WINDOW
    phase_enum: type[Enum] | None = None             # e.g. ARS Phase enum
```

ARS declares all four optional attributes. A hypothetical stateless canon declares none. The orchestrator inspects the registered runner and wires only what the runner exposes.

### 5A.3 Cartridge work vs console work

Cartridge work: selecting `canon_algorithm.name` from registered runners; tuning `canon_algorithm.params` within the runner's declared params schema.

Console work: introducing a new canon runner (new `CANON_RUNNERS` entry); modifying an existing runner's algorithm, state shape, checkpoint format, or recovery semantics; extending the `CanonRunner` protocol. All enforced by INV-CANON-RUNTIME-FIXED.

---

## 6. INVARIANTS REGISTERED BY THIS CONTRACT

```yaml
INV-CARTRIDGE-PURE-DECLARATION:
  Cartridges contain only YAML declarations. Zero executable code.
  Violation: any .py file inside cartridges/ that isn't schema or loader infrastructure.

INV-CONSOLE-STRATEGY-BLIND:
  No module inside console/ may reference any specific cartridge by name.
  Violation: grep console/ for cartridge names (ARS, DAILY_EXPANSION, etc.).
  Cartridge-specific runtime behavior lives in cartridge YAML alone.

INV-CONSOLE-NO-CARTRIDGE-SHAPED-BRANCHES:       # NEW in v0.2 (T3)
  Console runtime must not contain branches whose semantics are specific
  to any individual cartridge, even if not explicitly named. A branch that
  exists "because ARS needs it" is a violation even if the word "ARS" never
  appears. Today's concrete example: execution/intent_builder.py imports
  ARSCandidate directly — this must be factored through a cartridge-neutral
  interface before the invariant is enforced in CI.

INV-NEW-CARTRIDGE-NO-CONSOLE-CHANGE:
  Adding a new cartridge requires only new YAML. No console/ file changes.
  Violation: a commit that adds a cartridge AND modifies console/ in the same change.
  Exception: if a new cartridge requires a new primitive, a new canon runner,
  or a new capability, the console change is separated into a prior commit
  with explicit methodology review.

INV-CARTRIDGE-SCHEMA-UNIFIED:
  All cartridges conform to the same CartridgeSpec schema.
  Violation: cartridges with fundamentally different YAML shapes that cannot be
  parsed by the same loader.

INV-CANON-RUNTIME-FIXED:                         # NEW in v0.2 (T1)
  Selecting an existing canon_algorithm from CANON_RUNNERS is cartridge work.
  Introducing or modifying a canon runtime (new registry entry, changed
  runner, changed protocol) is console work and is gated by methodology
  review. The registry is the boundary.

INV-TRACE-DETERMINISM-BY-CARTRIDGE:              # NEW in v0.2 (T3)
  For identical bars + cartridge + governance state, console outputs
  (decision_trace, chain_trace) must be identical regardless of which
  other cartridges are present or registered. Presence of additional
  cartridges must not perturb any single cartridge's replay.
  Validation: cross-cartridge replay determinism test — run cartridge X
  alone, then with cartridges Y and Z loaded, confirm byte-identical
  traces for X in both runs. Extends INV-REPLAY-DETERMINISM.
  Current single-cartridge runtime trivially satisfies this invariant;
  the cross-cartridge replay determinism harness is a required exit gate
  for any future concurrent-cartridge work (see §12 Flag 3).

INV-STRUCTURAL-REFACTOR-NO-SEMANTIC-DRIFT:       # NEW in v0.2 (T5, protective)
  Any structural refactor (directory move, rename, consolidation,
  canon-runner dispatch swap) must not change detection, map, or execution
  semantics. Parity tests (151/151 ARS, 6/6 DAILY_EXPANSION) green before
  and after. Any deviation = immediate halt + escalation. Lives at contract
  scope because semantic drift during structural work is the worst failure
  mode of the cartridge realignment.

INV-DAY-STATE-MAP-COHERENT:                      # NEW in v1.0.1 (Olya ruling 2026-04-21)
  Day_state derives from the same structural primitives as the Map
  (MSS + displacement). It updates on the same detection events that
  drive regime and dealing-range updates. It cannot be computed from
  an independent logic tree.
  Auditable violation: any code path that triggers a day_state
  transition without going through the same detection event that
  triggers regime / DR updates. Concrete enforcement test: detect
  parallel MSS or displacement derivation logic in the day_state code
  path.
  Relationship: strengthens INV-DAY-STATE-MARKET-DRIVEN (which
  constrains the trigger source only). This invariant constrains the
  derivation pipeline. Extends INV-NO-REIMPLEMENTATION across modules.
  Rationale: Olya methodology ruling (2026-04-21) — "Day_state is not
  something you check. It is something the map IS. Same way: regime =
  directional state, dealing_range = spatial state, PDA = location,
  day_state = phase of delivery. All four are part of ONE map read."

INV-PDA-MITIGATION-SINGLE-SITE:                  # NEW in v1.0.2 (Phase 2.5 §A1 ship 2026-04-21)
  FVG retrace-fill mitigation logic is implemented in exactly one
  site: PDAStore.apply_bar_close (en1gma/context/pda_store.py).
  PDAStore.update_on_bar_close is a thin iterator over this method,
  and MapEngine._replay_price_forward delegates to it rather than
  reimplementing the semantic. All other modules consuming PDA
  mitigation outcomes must call into pda_store rather than inlining
  their own retrace-fill comparison.
  Auditable violation: any module other than
  en1gma/context/pda_store.py containing the FVG retrace-fill
  comparison pattern (bar.close against PDA.zone_top / PDA.zone_bottom
  with the mitigation effect of setting status = PDAStatus.MITIGATED)
  is a violation. Concrete enforcement: `grep -n "PDAStatus.MITIGATED"
  en1gma/` under production code paths should return matches only
  inside pda_store.py (definition + apply_bar_close), context_types.py
  (enum + PDA_TERMINAL_STATES), and tests / methodology YAML.
  Relationship: pairs WHAT (INV-PDA-MITIGATION-IS-RETRACE-FILL —
  methodology, SW01 2026-04-20) with WHERE (this invariant —
  structural). Extends INV-NO-REIMPLEMENTATION inside the map layer.
  Protected the Phase 2.5 §A1 consolidation itself via
  INV-STRUCTURAL-REFACTOR-NO-SEMANTIC-DRIFT (parity gate: 6/6 cross-
  implementation comparison test green pre and post; 151/151 ARS +
  6/6 DAILY_EXPANSION ground truth unchanged; replay determinism
  preserved).
  Rationale: Olya/NEX methodology ruling 2026-04-21 — "PDA mitigation
  is PDA lifecycle logic. Lifecycle ownership belongs to pda_store by
  responsibility and name. map_engine should consume PDA state, not
  define PDA state transitions." Prior to consolidation, parallel
  implementations in pda_store.update_on_bar_close and
  map_engine._replay_price_forward were kept in lock-step by brief
  discipline (SW01) — a known hazard formalized by AUDIT_STREAM_B
  DF-07 (map_engine's terminal-state check missed REJECTED). The
  consolidation closes DF-07 as a side-effect.

INV-BOUNDARY-CLASSIFIABLE:
  Every brief, ruling, or change must be classifiable as console work or cartridge work.
  If classification is ambiguous, the change must be paused and the ambiguity resolved
  before proceeding.

INV-AUTHORITY-BOUNDARY-EXPLICIT:
  Methodology questions (what concepts mean) route to Olya.
  Logic/engineering questions (how concepts are evaluated) route to CTO.
  Cartridge design questions (which console capabilities this strategy activates)
  route to Olya.
  Cartridge implementation questions (how the declaration gets wired) route to CTO.

INV-RULING-SCOPE-EXPLICIT:
  Every Olya ruling declares scope: console-level (applies to all cartridges) or
  cartridge-level (applies to a specific cartridge). No ruling is treated as
  universal by default.
```

---

## 7. THE DECISION GATE

Before any change is made to the system, the answering agent (human or AI) must declare TWO dimensions: `scope` and `effect`.

### 7.1 Scope — where the change lands

```yaml
it_is_console_work_if:
  - The change modifies what an ICT primitive IS or HOW it is detected
  - The change modifies the chain topology or gate logic
  - The change modifies governance, safety, or determinism
  - The change affects all cartridges equally
  - The change introduces or modifies a primitive
  - The change introduces or modifies a canon runtime (see §5A)
  - The change modifies shared vocabulary or temporal semantics

it_is_cartridge_work_if:
  - The change modifies only one specific cartridge's YAML
  - The change activates or deactivates console capabilities for one strategy
  - The change tunes parameters within declared ranges for one strategy
  - The change selects an existing registered canon_algorithm
  - The change adds a new cartridge without touching console/

it_is_example_only_if:
  - The change is documentation, a tutorial, a worked example, or a test
    fixture that does not ship as a real cartridge or console capability

if_ambiguous:
  - Stop
  - Escalate to Chairperson for architectural review
  - Do not proceed until classification is unambiguous
  - Ambiguity itself is a signal that the contract needs refinement
```

### 7.2 Effect — what kind of change it is (NEW in v0.2 — T2)

`scope` alone does not tell an auditor what the change DOES. Two changes can share a scope and have entirely different natures. Declare `effect`:

```yaml
methodology:    # Changes what an ICT concept means. Olya authority.
                # Example: redefining when a PDA is mitigated.
evaluation:     # Changes how signals are judged or composed, within methodology.
                # Example: adjusting how the gate combines 4 conditions.
configuration:  # Parameter tuning within an existing schema. No code/schema change.
                # Example: bumping sweep_lookback_hours from 4 to 5 in one cartridge.
structure:      # Filesystem / module layout / registration-pattern change. No
                # behavioral change expected. INV-STRUCTURAL-REFACTOR-NO-SEMANTIC-DRIFT
                # applies. Example: moving pda_store.py from context/ to console/map/.
workflow:       # Process, pipeline, or developer ergonomics change.
                # Example: adding a pre-commit hook, changing brief template.
```

### 7.3 Required declaration

Every brief, ruling, and change header now carries both dimensions:

```yaml
scope: console | cartridge | example_only
effect: methodology | evaluation | configuration | structure | workflow
```

A change is classified only when both fields are declared unambiguously. Compound changes (e.g., `structure` + `evaluation`) are split into separate commits or briefs with each dimension declared independently.

---

## 8. SPECIAL CASES

### ARS as a cartridge

ARS declares `map_required: false` and provides `canon_algorithm: ars_canon_v1_3`. The console dispatches to the ARS canon runner via the registry. ARS is a stateful canon (SessionState + checkpoint + recovery + phase progression) — the canon runner interface in §5A accommodates this. ARS is a simple cartridge, not an exception to the architecture.

### Future canon algorithms

If another self-contained strategy emerges (e.g., a pure Silver Bullet pattern that doesn't fit the Map+Chain model), a new canon runner is authored, registered in `CANON_RUNNERS`, and made available to cartridges. Adding the runner is **console work** (§5A.3). Selecting it from a cartridge YAML is **cartridge work**. INV-CANON-RUNTIME-FIXED draws this line.

### Cartridge families

Cartridges may share a family designation (e.g., DAILY_MOMENTUM family containing DAILY_EXPANSION, DAILY_CONTINUATION). Family membership is declarative metadata — it does not grant privileged runtime behavior. Each cartridge still conforms to the full contract independently.

---

## 9. WHAT THIS CONTRACT CHANGES

### For Olya

You have a bounded, formal creative surface. When you want to propose a new strategy, you are designing a cartridge. You fill in the declared interface. You do not need to reason about console internals. If your idea cannot be expressed within the cartridge schema, that is a signal the idea requires new methodology — a separate, explicit conversation with full recalibration.

### For CTO

Every brief is either console work or cartridge work, and every brief declares its `effect`. Console work requires architectural review (this contract is the reference). Cartridge work is bounded: new YAML, validated by the loader, consumed by universal console machinery. The boundary is lintable: `console/` cannot import from `cartridges/`; cartridges cannot contain code; the canon registry is the single admission gate for new canon runtimes.

### For agents (AI and human)

Your first question on any task is the classification question: is this console work or cartridge work, and what effect? Your second question is: which invariants from this contract apply? Your third question begins the work.

### For RepoPrompt audits

This contract is an input document. Conformance to it is a first-class audit dimension. Violations are findings. The cross-cartridge replay determinism test (INV-TRACE-DETERMINISM-BY-CARTRIDGE) is auditable.

---

## 10. HOW THIS CONTRACT EVOLVES

This contract is version-locked. Changes require:

1. A named reason (new capability, discovered ambiguity, learned improvement)
2. Chairperson review
3. CTO engineering review
4. Olya's advisor methodology review (if the change affects methodology scope)
5. G's ratification

No change to the contract is retroactive. Cartridges and console code written against v0.1 remain valid under v0.2 unless explicitly migrated.

---

## 11. FLAGS FOR CHAIRPERSON

Items surfaced during v0.2 refinement. Ratified dispositions are in §12.

- `FLAG_FOR_CHAIRPERSON`: `ote_entry_levels` (list of fib levels) is marked `(v2)` because today's console consumes `ote_fib: float` + `ote_zone: (lo, hi)` instead. The semantic question behind the schema question is DF-02 in AUDIT_STREAM_B.md (vLOCK 4-level OTE vs 2-level implementation). Resolving one resolves the other; they should travel together.
  → See §12 Flag 1 for ratified disposition.
- `FLAG_FOR_CHAIRPERSON`: `sweep_model: REVERSAL | CONTINUATION` is marked `(v2)`. DF-04 in AUDIT_STREAM_B.md surfaces a related dormant field (`sweep_required`) that could be read as an Anti-Pattern 2 hazard. Whether sweep variation lives in the cartridge schema or in Map configuration (different PDA-type gate) is a methodology question for Olya when RETRACE/RANGE cartridges are designed.
  → See §12 Flag 2 for ratified disposition.
- `FLAG_FOR_CHAIRPERSON`: INV-TRACE-DETERMINISM-BY-CARTRIDGE assumes multiple cartridges can coexist in a single console process. Today only one cartridge runs per `run_map_replay` / `run_ars_session` invocation. If concurrent cartridges never ship, the invariant degrades to INV-REPLAY-DETERMINISM per cartridge; if they do, a cross-cartridge replay harness must be built.
  → See §12 Flag 3 for ratified disposition.

---

## 12. FLAG RESOLUTIONS (ratified 2026-04-21)

The three `FLAG_FOR_CHAIRPERSON` items surfaced in §11 were ratified by G on 2026-04-21. Dispositions below are canonical.

### Flag 1 — `ote_entry_levels` / DF-02 coupling

```yaml
disposition: BUNDLE_WITH_DF-02
rule: |
  ote_entry_levels remains (v2)-marked in v1.0. It ships when DF-02
  ships — not before, not after. DF-02 is Block 4 methodology work:
  console moves from 2-level OTE to 4-level tracking per vLOCK,
  Olya rules on which levels are entry surfaces vs observation
  levels, and the cartridge schema lights up ote_entry_levels as
  a first-class field at that moment.
owner: CTO (coordination), Olya (methodology ruling on levels)
trigger: DF-02 implementation
contract_effect: |
  No change to v1.0 schema. ote_entry_levels stays (v2). When DF-02
  ships, a contract v1.1 bump activates the field.
```

### Flag 2 — `sweep_model` / DF-04 / Anti-Pattern 2 hazard

```yaml
disposition: DEFER_TO_RETRACE_RANGE_DESIGN
rule: |
  sweep_model stays (v2)-marked in v1.0. The decision between
  "sweep variation as cartridge-schema field" vs "sweep variation
  as Map-configuration (different PDA types arming different gates)"
  is a methodology-architecture question that cannot be decided
  without Olya designing RETRACE and RANGE cartridges. The current
  DAILY_EXPANSION cartridge does not need the field.

  sweep_required (the related dormant field flagged as Anti-Pattern 2
  hazard) is removed in Phase 2.5 if trivial, or deferred to Block 4
  if it carries any live dependency. Pre-move audit (implementation
  draft §4A.3) identifies which.
owner: Olya (when RETRACE/RANGE cartridge design begins), Chairperson (architectural framing)
trigger: Map v2 work begins — RETRACE or RANGE cartridge authored
contract_effect: |
  No change to v1.0 schema. sweep_model stays (v2). When RETRACE or
  RANGE cartridges are designed, Olya rules on whether sweep variation
  is cartridge-schema or Map-config; contract v1.x adjusts accordingly.

  Anti-Pattern 2 hazard prevented by INV-CONSOLE-NO-CARTRIDGE-SHAPED-
  BRANCHES enforcement in Phase 2.5 audit — any dormant field that
  enables strategy-shaped branching gets surfaced and dispositioned.
```

### Flag 3 — INV-TRACE-DETERMINISM-BY-CARTRIDGE multi-cartridge assumption

```yaml
disposition: COMMIT_TO_STRONGER_INVARIANT
rule: |
  Adopt the stronger invariant as stated. The console is designed
  to be cartridge-blind — if its behavior for cartridge X can be
  influenced by cartridge Y being present, that IS the leak this
  invariant exists to prevent, regardless of whether concurrent
  cartridges ship soon.

  Runtime context today: one cartridge per invocation. The invariant
  is trivially satisfied in that context (no other cartridges to
  coexist with). When concurrent cartridges ship (if ever), the
  invariant is already registered and an enforcement harness is
  built as part of that delivery.
owner: CTO (enforcement when concurrent runtime ships), Chairperson (invariant preservation)
trigger: |
  (a) Automatic — current single-cartridge runtime trivially
      satisfies. No action needed today.
  (b) When concurrent-cartridge runtime is proposed, a cross-
      cartridge replay determinism harness is a required exit gate
      of that work.
contract_effect: |
  Single-sentence clarification added to INV-TRACE-DETERMINISM-BY-
  CARTRIDGE in §6 noting that current single-cartridge runtime
  trivially satisfies the invariant, and the cross-cartridge harness
  is an exit gate for any future concurrent-cartridge work.
```

---

*"The console is the swiss watch. The cartridges are the games. The contract is the slot."*

*v1.0 CANONICAL — ratified by G on 2026-04-21. Absorbs three FLAG_FOR_CHAIRPERSON dispositions (§12) on top of v0.2's six-tightening refinement pass. No schema changes, no invariant changes beyond the single clarification on INV-TRACE-DETERMINISM-BY-CARTRIDGE. This is the console/cartridge contract en1gma builds against.*
