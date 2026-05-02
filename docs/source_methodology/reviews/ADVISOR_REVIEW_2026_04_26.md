# Formal CTO Audit Mission — `en1gma`

Review performed read-only in the isolated clone at `/Users/echopeso/en1gma-review`.  
No code was changed.

## Executive Verdict

The core architecture is right.

The doctrine in `NORTH_STAR`, `MAP_SPATIAL_PRIMER_v1`, and `CARTRIDGE_CONTRACT` is unusually strong. The system has a real center of gravity: single detection authority, Map/Chain separation, console/cartridge split, governance as constitutional boundary.

My conclusion is:

- **Do not rewrite the architecture.**
- **Do not expand strategy surface yet.**
- **Do harden the seam lines ruthlessly.**

The main risk is not conceptual weakness.  
The main risk is **semantic drift at authority surfaces**: the exact places where the system decides what is true, what is active, and what is allowed to arm.

Today I would describe en1gma as:

- **architecturally strong**
- **operationally promising**
- **not yet swiss-watch certified**

## Audit Evidence

### Canonical surfaces reviewed
- `docs/canonical/NORTH_STAR.md`
- `docs/canonical/MAP_SPATIAL_PRIMER_v1.md`
- `docs/canonical/CARTRIDGE_CONTRACT.md`
- `docs/canonical/FORWARD_PLAN.md`
- `CLAUDE.md`

### Core runtime surfaces reviewed
- `en1gma/console/detection/**`
- `en1gma/console/map/**`
- `en1gma/console/chain/**`
- `en1gma/cartridges/**`
- `en1gma/orchestrator/**`
- `en1gma/observe/**`

### Validation run
- Full test suite: `829 passed, 4 xfailed`
- Import boundaries: `6 kept, 0 broken`
- Strict mypy on core runtime surfaces: `262 errors in 44 files`
- Strict mypy repo-wide: `1017 errors in 100 files`
- CI workflows present: only `.github/workflows/lint-imports.yml`

## Assurance Scorecard

| Surface | Verdict |
|---|---|
| Doctrine / architecture | Strong |
| Import boundary discipline | Strong |
| Detection singleton discipline | Strong, but semantic parity proof is incomplete |
| Map / Gate correctness | Needs hardening |
| Cartridge declaration authority | Weak / incomplete |
| Replay determinism | Strong for `chain_trace` + `decision_trace` |
| Full state / persistence determinism | Incomplete |
| Static assurance / CI depth | Weak |

## What Is Excellent and Should Be Preserved

1. **The two-clock model is correct.**  
   Map as persistent spatial truth, Chain as local execution mechanism.

2. **“The Map is the strategy” is the right abstraction.**  
   That is the deepest correct architectural decision in the repo.

3. **`detect.py` as sole oracle is the right constitutional constraint.**

4. **The console/cartridge split is the right long-term platform shape.**

5. **Import-linter and parity culture are exactly the right instincts.**  
   They are protecting the right thing: doctrine from erosion.

## Severity-Ranked Findings

## Critical 1 — The gate can arm on the wrong PDA truth

This is the most important finding.

### Why it matters
The system can preserve detector truth upstream and then ignore it at the actual arming surface.

### Evidence
- Mixed-direction PDAs are explicitly expected post-SW04:  
  `en1gma/tests/console/map/test_sw04_pda_fidelity.py`
- `evaluate_gate()` filters only by active status and zone, not PDA `direction_context`:  
  `en1gma/console/chain/gate.py:105-130`
- `MapEngine.get_state()` returns all open/touched PDAs, not current-DR-scoped PDAs:  
  `en1gma/console/map/map_engine.py:657-666`
- The stricter helper exists but is bypassed:  
  `en1gma/console/map/pda_store.py:193-211`  
  `en1gma/console/map/map_engine.py:672-678`

### CTO interpretation
This is a direct methodology-risk seam.  
If a bearish regime can arm from a bullish PDA merely because it sits in the right premium/discount zone, the brain is no longer faithfully expressing calibrated truth.

### Priority
Immediate.

---

## Critical 2 — The Map path is fail-open on strategy loading

### Why it matters
If strategy loading fails, the system silently degrades to defaults instead of halting.

### Evidence
- Loader failure is swallowed:  
  `en1gma/orchestrator/map_orchestrator.py:130-145`
- Runtime then falls back to:
  - default `ChainConfig()`
  - default kill zones
  - default LTF TFs
  - default trade limits
- Day-state gating is only enforced when `strategy_params_present` is true:  
  `en1gma/console/chain/canon/map_canon/session.py:124-130, 472-478`

### Worse: configuration split-brain at CLI entry
`run_map_session.py` loads governance from an explicit YAML path, but `run_map_replay()` later reloads strategy by name rather than consuming that already-loaded config:  
`en1gma/scripts/run_map_session.py:76-97`

That means governance can come from one YAML while runtime chain/map behavior comes from another surface or from defaults.

### CTO interpretation
For a trading kernel, methodology/config failure must be **fail-closed**, never fail-open.

### Priority
Immediate.

---

## High 3 — Cartridge declarations are not yet authoritative

### Why it matters
The cartridge surface currently overstates what the runtime actually obeys.

### Evidence
The loader parses or validates fields including:
- `day_state_requirement`
- `pda_timeframes`
- `htf_timeframes`
- `max_trades_per_window`
- `governance_precedence`
- `chain.sequence`
- `sl_method`

But runtime behavior does not consistently consume them:
- HTF detection is hardcoded to `["1D", "4H"]`:  
  `en1gma/console/chain/canon/map_canon/session.py:302-304`
- Day-state eligibility is strategy-name-based, not requirement-based:  
  `en1gma/console/map/day_state.py:96-101`
- `map_required`, `max_trades_per_window`, `governance_precedence` appear unused in runtime
- `pda_timeframes` is loaded but not enforced
- `load_strategy(ars_v1_3.yaml)` fails with schema mismatch, proving unified cartridge schema is not actually unified yet

### CTO interpretation
This is not just style debt. This is trust debt.  
If YAML says something the kernel does not truly honor, the cartridge is no longer the authority surface.

### Priority
Before adding more cartridges.

---

## High 4 — Map initialization is too permissive and too willing to fabricate plausible state

### Why it matters
A methodology kernel must prefer “cannot prove state” over “plausible fallback state.”

### Evidence
- Init docstring says PDAs should be after regime establishment/current DR:  
  `en1gma/console/map/map_engine.py:186-193`
- `_initialize_pdas_from_detections()` loads all FVG detections across selected TFs into the current DR without regime/range scoping:  
  `en1gma/console/map/map_engine.py:529-577`
- Dealing-range initialization contains permissive fallbacks and swallowed exceptions:
  - `fallback_full_range`
  - `tail(5)`
  - half-history fallback
  - `except Exception: pass`  
  in `map_engine.py`

### CTO interpretation
This is a classic “looks robust, can hide drift” pattern.  
For this domain, I would rather see loud failure on invalid structural inputs than silent boot into a plausible map.

### Priority
High.

---

## High 5 — H4 authority cascade is only partially real

### Why it matters
The doctrine says daily can cascade to H4 when daily is still expanding. If that happens, H4 must become fully authoritative, not cosmetically authoritative.

### Evidence
- Authority can switch to H4:  
  `en1gma/console/map/map_engine.py:211-224`
- But lifecycle replay after init still runs via daily bars:  
  `en1gma/console/map/map_engine.py:226-228, 579-617`
- Tests cover validator and authority tags, but not H4 PDA lifecycle replay fidelity:  
  `en1gma/tests/console/map/test_dr_cascade.py`

### CTO interpretation
This is a partial implementation of an authority shift.  
That is dangerous because it can look methodologically correct while being mechanically approximate.

### Priority
High.

---

## High 6 — DayState violates cartridge neutrality and is too loosely derived

### Why it matters
Day state is part of the Map. It should be derived structurally and consumed declaratively.

### Evidence
- Strategy-name branching in console code:  
  `en1gma/console/map/day_state.py:96-101`
- `_check_expansion_delivered()` independently finds one aligned displacement and one aligned MSS, without proving they are causally linked:  
  `en1gma/console/map/day_state.py:161-193`

### CTO interpretation
Two problems exist at once:
1. console knows strategy names
2. the transition rule is looser than the doctrine suggests

That is both architectural leakage and methodology risk.

### Priority
High.

---

## Medium 7 — Detection parity proves counts, not semantics

### Why it matters
Count parity can still hide semantic drift.

### Evidence
- `test_detection_parity.py` compares bucket counts, not IDs/properties/timestamps
- MSS detector defaults missing displacement metadata to stronger semantic values:
  - `quality_grade = "VALID"`
  - `path = "ATR_RELATIVE"`
  - `displacement_type = "SINGLE"`  
  `en1gma/console/detection/ra_engine/detectors/mss.py:281-286, 361-366`

### CTO interpretation
This is exactly the kind of silent upgrade that can pass a coarse parity gate while still drifting from Olya calibration.

### Priority
Medium-high.

---

## Medium 8 — Determinism is strong where tested, but incomplete as a full forensic guarantee

### Strong
- Replay determinism for `chain_trace.jsonl` and `decision_trace.jsonl` is well-protected
- No-future-leak tests are good
- Full test suite is green

### Gap
- `MapTimeline` uses `datetime.now()` when `time` is omitted:  
  `en1gma/observe/map_timeline.py:60-66`
- `_run_map_session()` omits an explicit time for `log_dealing_range_set()`:  
  `en1gma/console/chain/canon/map_canon/session.py:445-451`
- Persistence serializes only `active_pdas`, even though `all_pdas` exists in payload:  
  `en1gma/console/map/map_persistence.py:45-79, 127-134`
- Roundtrip tests only prove active PDA persistence, not terminal lifecycle history

### CTO interpretation
You have strong replay determinism for the fast-clock artifacts.  
You do **not** yet have full-state forensic determinism for the slow clock.

### Priority
Medium-high.

---

## Medium 9 — Static assurance posture is not credible yet

### Evidence
- `pyproject.toml` declares strict mypy
- Core runtime surfaces currently produce 262 mypy errors locally
- Repo-wide run produced 1017 errors
- CI present in repo only enforces import-linter, not tests or mypy

### CTO interpretation
This does not mean the runtime is broken.  
It means static typing is not yet a trustworthy assurance signal. Right now it is aspirational, not operational.

### Priority
Medium.

---

## Lean/Bloat Findings

This codebase is not bloated in philosophy.  
It is carrying **fake optionality** in a few places.

### The worst examples
1. **`StrategyParams` fields that are parsed but not authoritative**
2. **`ChainConfig` knobs that exist but are not cartridge-driven**
3. **`MapConfig` as a largely unused runtime config surface**
   - `MapEngine` stores `self._config`
   - almost none of `MapConfig` is actually consumed
4. **Registry and protocol surfaces are cleaner than runtime dispatch reality**
   - especially on the ARS vs Map asymmetry

### CTO rule
If a field is not live, do one of three things:
- enforce it
- reject it
- delete/defer it

Do not let it masquerade as live authority.

## What I Would Protect Ruthlessly

Do not let the audit overcorrect and damage what is good.

### Preserve
- two clocks
- Map/Chain separation
- `detect.py` singleton
- explicit canon registry
- governance single authorization site
- import boundary contracts
- replay parity culture

### Do not preserve
- fail-open config behavior
- strategy-shaped console logic
- unused declaration surface
- permissive map boot fallbacks on methodology-critical paths
- partial authority cascades
- coarse parity that ignores semantics

## Recommended CTO Program

## Phase 0 — Freeze expansion
Do not add new strategy surface until the current truth surfaces are hardened.

## Phase 1 — Close the authority-surface risks
1. Gate must only arm from:
   - current DR-scoped PDAs
   - direction-valid PDAs
   - correct zone
2. Strategy load failure must abort the run
3. Remove split-brain between CLI YAML and orchestrator config
4. DayState must be declarative and structurally linked
5. H4 authority must be fully authoritative or explicitly not supported

## Phase 2 — Make cartridge declarations real
For every cartridge field:
- live and enforced
- or rejected
- or deferred and absent

No middle state.

## Phase 3 — Build the swiss-watch proof layer
Add hard proof gates for:
- mixed-direction PDA gating
- stale/current DR PDA scoping
- H4 authority replay fidelity
- full lifecycle persistence roundtrip
- semantic detection parity
- deterministic `map_timeline`
- restart/recovery equivalence

## Phase 4 — Lean pass
After truth is locked:
- remove dead knobs
- collapse fake optionality
- narrow compatibility shims
- reduce surfaces that create interpretive freedom

## Non-Negotiable Exit Gates Before More Trust

I would require these before materially increasing trust in the brain:

1. **Mixed-direction gate proof**
2. **Fail-closed cartridge load proof**
3. **Current-DR PDA scoping proof**
4. **H4 authority fidelity proof**
5. **Terminal PDA persistence proof**
6. **Deterministic `map_timeline` proof**
7. **Semantic detection parity proof**
8. **Scoped static analysis gate on core runtime**
9. **CI runs more than import-linter**

## Final CTO View

My blunt view:

- You do **not** have an architecture problem.
- You have an **assurance and seam-discipline problem**.
- That is a much better problem to have.

The project is close to being very strong.  
But if the goal is Olya-grade determinism, then the next step is not more cleverness. It is **less ambiguity**.

The brain should become:
- smaller in authority surfaces
- harsher in failure behavior
- stricter in config truth
- more provable in replay/persistence
- less tolerant of “plausible” state

That is how this becomes a swiss watch.

## Validation Snapshot

- `pytest`: `829 passed, 4 xfailed`
- `lint-imports`: `6 kept, 0 broken`
- `mypy` core runtime: not green
- CI in repo: import boundaries only

## Bottom Line

If I were acting as CTO, my next move would be:

1. freeze expansion,
2. harden the two critical seams,
3. make the cartridge contract truly authoritative,
4. then run a proof-focused remediation cycle before any new strategic breadth.

If you want, next I can convert this audit into a **ranked remediation brief** with exact work packages, owners, and sequencing.
