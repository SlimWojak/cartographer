# FIDELITY AUDIT AND PATH RECOMMENDATION — ADVISOR PACK

```yaml
document: FIDELITY_AUDIT_AND_PATH_RECOMMENDATION
version: 1.1 (ADVISOR PACK — extended with autonomous-execution reframe)
date: 2026-04-24
author: Opus (Cursor, fresh session per G brief FIDELITY_AUDIT_AND_PATH_RECOMMENDATION + CTO extension brief FIDELITY_AUDIT_ADVISOR_PACK_EXTENSION)
audience: G (sovereign), CTO Claude, Fresh Chair Opus, GPT (lateral), Olya
purpose: |
  Authoritative input artifact for the four-way review that ratifies
  en1gma's Phase 4+ path. Review panel decides on the basis of this
  document; this document does not decide.
format: prose where prose clarifies; YAML where YAML disambiguates
rule: |
  Honest read. Not a sales pitch for any path. Recommend what the
  evidence supports under the capability environment we actually
  operate in (including autonomous execution as a real capability).
scope: read-only investigation + written opinion; no code touched; one docs commit
source_head: e2ecbde (phase_3_5-exit) + staged ADVISOR / COO / Phase 4a artefacts
reading_order_observed:
  - NORTH_STAR, MAP_SPATIAL_PRIMER, CARTRIDGE_CONTRACT
  - ARS_CANON_v1_3, SYNTHETIC_OLYA_METHOD_vLOCK (partial — 1,000+ lines), annotated_trades
  - VAULT
  - CLAUDE.md §6 + §11 (targeted), FORWARD_PLAN v2.3, POST_PHASE_3_ORACLE v1.0
  - ADVISOR_REVIEW_2026_04_26, COO_INPUTS_POST_PHASE_3, Phase 4a D3 verification pass
  - OLYA_PREP_PACK_24_04_26
  - Direct code read: gate.py, map_engine.py, regime.py, day_state.py, mss.py, map_orchestrator.py, session.py, detect.py, test_daily_expansion_6_trade_parity.py

v1_1_changelog:
  reframe_received: |
    CTO brief FIDELITY_AUDIT_ADVISOR_PACK_EXTENSION introduced
    autonomous execution (factory.ai Opus Mission orchestration) as
    a real capability in scope. Wall-clock for "sequential 3-6
    months" rework collapses to ~12-48 hours of autonomous execution
    plus human review cycles. Spec precision becomes the binding
    constraint, not implementation hours.
  additions:
    - §4.1: PATH_MIDDLE_C added — autonomous spec-driven rebuild of
      orchestration layer only
    - §4.1: PATH_REFACTOR_CONTINUE reframed as CONTINUE (human) vs
      CONTINUE-AUTONOMOUS execution models
    - §4.2: recommendation revised under new math
    - §5: autonomous-execution-specific risks
    - §8: Advisor Review Protocol (new)
    - §9: Decision Questions (new, binary)
    - §10: Implications for G and CTO Operating Model (new)
  what_did_not_change:
    - §1 executive read (direction of verdict holds; execution model shifts)
    - §2 fidelity audit findings (code-level; reframe-independent)
    - §3 architectural assessment (structural; reframe-independent)
    - §6 verification requests (execution-scope-independent)
    - §7 "one thing on the record" (strengthens under reframe, if anything)
  confidence_ratios:
    before_reframe: "CONTINUE ~90% / rebuild ~10%"
    after_reframe: "CONTINUE-AUTONOMOUS ~60% / MIDDLE_C_AUTONOMOUS ~35% / FRESH_NUCLEUS ~5%"
  honesty_note: |
    The reframe genuinely moved me. If the panel reads this and
    asks "did the reframe change your answer?", the answer is
    "yes, materially, but not flipped." MIDDLE_C_AUTONOMOUS is
    a legitimate path I would not have dismissed under the new
    math even if I had thought of it v1.0. My §4.2 reasoning
    for why CONTINUE-AUTONOMOUS still wins on risk-adjusted
    terms is specifically the meta-irony that spec-incompleteness
    in MIDDLE_C is the same hazard class (plausible-state cascade)
    we are trying to close in the current kernel. That argument
    is strong but not airtight; panel should challenge it.
```

---

## 1. Executive read

The architecture is right. The kernel is already small. The doctrine is unusually strong. The discipline accumulated across Phases 1–3 is real. But the system is not yet swiss‑watch; it is a lean instrument with a small number of concrete semantic leaks at the seams where primitives become regime, regime becomes gate, and cartridge declarations become runtime behaviour. Those leaks are local, not systemic — they live at named line numbers, not in the shape of the thing.

The brief raises the prospect of a fresh‑nucleus rebuild. Having read the canonical doctrine first, then the code, then the advisor review and COO inputs, I do not think rebuilding would land you at swiss‑watch faster or cleaner than finishing the authority‑surface hardening program that is already in flight. The reason is specific: the painful findings encoded as `INV-*` and `SW*` are not architectural debt — they are *learnings*, each purchased by a concrete production near‑miss or audit, each now machine‑enforced. A rebuild would re‑run those experiments at great cost with no structural advantage, because the calibration ground truth (detect.py, vLOCK, annotated_trades, the Map ↔ Chain separation, the canon runtime) is what you would carry forward anyway, and the things you would throw away (MapEngine, day_state FSM, gate.py, chain_evaluator, canon registry, governance single‑check site) are each under 1 kLOC and already correct in shape.

The Trade 007 BULLISH → BEARISH cascade divergence is not evidence of systemic rot. It is evidence of one specific plausible‑fallback path (`_initialize_regime_from_detections` → displacement fallback ranked by `range_pips` when no 1D MSS is found) producing a methodology‑incoherent answer on a window where the 1D MSS detector didn't fire because its composite dependencies (swings + displacement + FVG on 1D) interact with ATR warmup at the edge of the 45‑day lookback. That is a known pattern with a named fix class (P3/SW49 Olya‑gated fail‑closed ruling, already framed by COO). Do not treat it as a rebuild trigger.

My recommendation is **PATH_REFACTOR_CONTINUE — but with two non‑negotiable additions not currently scoped**: (a) make Trade 007 itself a ratified swiss‑watch exit gate with its root cause publicly attributed and fixed *before* reference re‑baselining; (b) adopt the SW54 byte‑identity harness as a permanent correctness gate at the Olya level (like the 151/151 ARS canon), but on *chart‑truth*, not on pre‑SW02 reference files. Details in §4.

---

## 2. Part 1 — Fidelity audit

### 2.1 Method used

I did not run the cascade end‑to‑end (no runtime execution in this session). Instead I did a **code‑path fidelity audit**: I traced, line by line in the current HEAD (e2ecbde), the cascade from `detect.py` output through `_initialize_regime_from_detections` → `update_on_mss` → `_initialize_dealing_range_from_detections` → `_initialize_pdas_from_detections` → `_replay_price_forward` → `get_state` → `evaluate_gate`. I cross‑referenced each step against (a) Olya's methodology as encoded in vLOCK + the 27 calibrated answers, (b) MAP_SPATIAL_PRIMER doctrine, (c) the six annotated trades' `expected_state` blocks in `annotated_trades.yaml`, and (d) the two most recent artefacts surfaced by CTO's investigation: the SW54 test file (`test_daily_expansion_6_trade_parity.py`) and the COO/advisor findings inventories.

I then classified each trade against **chart‑truth** as declared in `annotated_trades.yaml` (Olya's annotation is the ground truth per INV‑OLYA‑ABSOLUTE), **not** against the committed `traces/ground_truth/` reference files — because the brief itself and FORWARD_PLAN v1.3 note those reference files were produced by pre‑SW02 future‑leaking code and are declared invalid by SW02's own commit body.

Classifications: `FAITHFUL` (cascade output matches chart‑truth at the regime/DR/PDA/gate semantic level), `LOCAL_DIVERGENCE` (one named step produces wrong output; fix is localized and parity‑preserving), `SYSTEMIC_DIVERGENCE` (cascade would need structural change to produce the right answer; the model itself is not faithful).

### 2.2 Per‑trade findings

```yaml
# Note: the advisor and COO inputs already surveyed the authority surfaces.
# What follows is my INDEPENDENT mapping of each trade's chart-truth
# against the cascade code path, not a re-read of those artefacts.

trade_001 (2025-10-01, BEARISH SHORT, LOKZ, EXPANSION):
  chart_truth_per_annotation: |
    BEARISH regime. 4H bearish MSS Sept 24. Daily bearish displacement
    Sept 23-24. Counter-move (RETRACE) exhausted by Oct 1. 15m bearish
    MSS 03:30 LOKZ is the execution trigger.
  cascade_code_path:
    regime_init:
      - "_initialize_regime_from_detections finds 1D MSS event(s) in the
        Aug 17 → Oct 1 window (45-day HTF lookback from start)."
      - "Sept 24 4H bearish MSS is in the upstream detection set but NOT
        consumed by regime init (line 257: hardcoded 'for tf_key in [\"1D\"]')."
      - "A 1D bearish MSS must exist in that window for regime to land
        BEARISH. Per CLAUDE.md closed-defects, the 45-day HTF lookback
        provides ATR warmup and the Sept 24 bearish MSS IS detected on 1D."
    DR:
      - "Verified at 0.1-pip accuracy in prior work (FORWARD_PLAN §5 CLOSED
        dealing_range_extreme_delta): origin=1.18199, extreme=1.16454."
    gate:
      - "Post-SW47 direction filter is live. BEARISH PDAs in PREMIUM under
        SHORT_ONLY permission — correct arming."
  classification: FAITHFUL (with known local dependency on 1D MSS firing)
  caveat: |
    Trade 001 was the original 6/6 exemplar and is the most-tested single
    date. It is the trade whose integrity is most stable.
  fidelity_signal: green

trade_003 (2025-12-12, BULLISH LONG, NYOKZ, EXPANSION):
  chart_truth_per_annotation: |
    BULLISH regime. Daily bullish MSS from Dec 4 + 4H bullish MSS Dec 10
    with strong displacement. Original RANGE annotation was CORRECTED to
    BULLISH on 2026-03-19 by Olya.
  cascade_code_path:
    regime_init:
      - "1D MSS detector may or may not fire on Dec 4 depending on whether
        the swing structure + displacement + FVG cascade all qualify. The
        annotation explicitly notes: 'Daily bullish MSS from Dec 4 (not
        captured by detection engine due to ATR warmup limitation, but
        confirmed by Olya visual assessment 2026-03-19).'"
      - "IF 1D MSS not emitted → falls through to displacement fallback
        (map_engine.py:280-292): 'best_disp = max(disp_events,
        key=lambda d: d.properties.get(\"range_pips\", 0))' — picks the
        LARGEST displacement by range, regardless of whether it is the
        structurally governing event."
  classification: LOCAL_DIVERGENCE (methodology-gated)
  mechanism: |
    detect.py is known to not emit the Dec 4 daily MSS. The cascade's
    silent fallback onto the biggest-range displacement is a plausible-
    state authority surface (advisor High 4). Whether that fallback
    happens to pick the correct direction for this specific date is
    luck, not fidelity. The fact that trade_003 and trade_005 produce
    IDENTICAL replay hashes (per SW54 manifest and Olya prep pack
    flag 2) tells us the cascade is deterministic — but byte-identity
    is not the same as methodology-faithful.
  fidelity_signal: amber

trade_005 (2025-12-12, BULLISH LONG, NYOKZ, EXPANSION):
  classification: LOCAL_DIVERGENCE (same-window duplicate of trade_003)
  note: |
    Same date, same session window. The replay is byte-identical to
    trade_003 per Olya prep pack flag 2. Methodology-wise, Olya's two
    annotations capture two setups (8am MSS+FVG + 9am OTE); the
    current kernel with max_trades_per_day=1 masks the second. This is
    a DAILY_CONTINUATION cartridge question parked in VAULT — not a
    fidelity defect, a feature absence.
  fidelity_signal: amber (masked by max_trades=1)

trade_006 (2025-12-15, BULLISH LONG, LOKZ, EXPANSION):
  chart_truth_per_annotation: |
    BULLISH. 4H bullish expansion targeting H 1.17628 still not reached
    from previous day. Asia range lows swept at LOKZ; 3:30am MSS+FVG;
    OTE entry at 3:45am.
  cascade_code_path:
    regime_init: |
      Dec 15 is 3 days after Dec 12. If Dec 12's 1D bullish MSS is not
      detected (per trade_003 annotation note), Dec 15's regime init
      depends on whether a 1D MSS fires in the Nov 1 → Dec 15 window.
  classification: LOCAL_DIVERGENCE (shares trade_003's 1D MSS dependency)
  fidelity_signal: amber

trade_007 (2025-09-16, BULLISH LONG, NYOKZ, EXPANSION — 5m continuation):
  chart_truth_per_annotation: |
    Daily BULLISH with direction. 4hr bullish. 1hr in bullish order flow.
    5min continuation trade in NYOKZ. Price took pre NYOKZ SSLQ into 15m
    bullish FVG. MSS at 9:15am. Entry on 5m OTE at 9:45am.
  brief_evidence_provided:
    - "detect.py standalone on raw River bars correctly identifies the
      Sep 7 BULLISH daily MSS flip AND Sep 15 STRONG confirmation."
    - "The refactored system's cascade from primitive → regime produces
      BEARISH on the same bars."
    - "Chart is unambiguously BULLISH."
    - "Olya's annotation (independent) says BULLISH, matching chart truth."
  code_path_attribution (MECHANISM HYPOTHESIS, not execution-verified):
    step_1: |
      For trade_date 2025-09-16, map_engine.initialize receives HTF bars
      for the window [2025-08-02, 2025-09-16] (45-day lookback).
    step_2: |
      _initialize_regime_from_detections (map_engine.py:250-292) looks
      ONLY at results["mss"]["1D"].detections. If detect.py standalone
      finds Sep 7 + Sep 15 BULLISH 1D MSS, the same detect.py invoked
      from the cascade SHOULD too — unless the cascade passes a
      different bar set or applies a different filter.
    step_3_hypothesis: |
      Either (a) the 1D MSS detector output is being FILTERED somewhere
      between detect.py and _initialize_regime_from_detections (I did
      not find such a filter by inspection, but I did not execute), OR
      (b) ra_engine's cascade on this specific window emits an EARLIER
      bearish 1D MSS (e.g. August) that is post-Sept-15 in detection
      output order but pre-Sept-15 in event.time ordering — and the
      loop processes ALL of them in time order, so the LAST MSS wins
      (regime.update_on_mss at line 61-68 flips direction on every
      same-or-higher-TF opposing MSS).
    step_4_if_1D_MSS_is_absent: |
      Fallback at map_engine.py:280-292 picks 'best_disp = max by
      range_pips'. On a window that straddles a multi-week structural
      pivot, the LARGEST-RANGE displacement may well be a pre-Sept-7
      BEARISH one that preceded the BULLISH flip — producing exactly
      the BULL→BEAR misread observed.
    step_5_secondary: |
      MSS detector (mss.py:284-286, 364-366) applies semantic defaults:
        quality_grade = disp.get("quality_grade", "VALID")
        path = disp.get("qualification_path", "ATR_RELATIVE")
        displacement_type = disp.get("displacement_type", "SINGLE")
      This is advisor Medium 7 / SW32 — silent upgrade of meaning.
      If the Sep 7 BULLISH MSS depends on a displacement whose quality
      properties are missing (warmup edge), MSS invents "VALID" quality
      and the event is emitted at full strength. That is not the bug
      here (the bug is the cascade under-emitting BULLISH 1D MSS, not
      over-emitting), but it is a latent hazard on the same surface.
  classification: SYSTEMIC_DIVERGENCE at the primitive→regime seam —
    but LOCALLY PATCHABLE, not structurally irreducible.
  why_SYSTEMIC: |
    The mechanism is not "this fallback is wrong"; it is "the cascade
    silently substitutes a plausible answer for a methodology-absent
    one." Same class of hazard recurs across map_engine.py (15
    fallback sites per the Olya Prep Pack P3 cluster inventory) —
    zero-input bootstraps, tz-swallow try/except, regime direction
    fallback, pullback-substitute, missing-property semantic defaults.
    Any of these can turn methodology-absence into a plausible-but-
    wrong Map. Trade 007 happens to be the first annotated trade that
    exercises the hazard visibly.
  why_LOCALLY_PATCHABLE: |
    The fix shape is known: P3/SW49 Olya ruling on each fallback
    cluster (A-F per OLYA_PREP_PACK §1), combined with
    MapConstructionMode.FALLBACK propagation to the gate (SW47 F1
    scaffold — already armed but unfired per gate.py:122-129). Once
    Olya rules each cluster as KEEP_WITH_INVARIANT / FAIL_CLOSED /
    BOOTSTRAP_ONLY / LOG_AND_FLAG, the cascade either produces the
    correct answer OR refuses to produce one. No structural change.
  fidelity_signal: red — but with a named, existing remediation path

trade_013 (2026-03-12, BEARISH SHORT, NYOKZ, EXPANSION):
  chart_truth_per_annotation: |
    BEARISH. 4hr/1hr bearish. Price retraced into 1hr bearish OB and FVG.
    Swept LOKZ liquidity at 7:30am. Bearish MSS at 8am. OTE at 9am.
  concerns_from_olya_prep_pack:
    - "annotated_trades.yaml header notes 2026-W11 is OUTSIDE current
      data range (ends at 2026-W08). Test manifest includes trade_013
      with end_date=2026-03-15 and reportedly green at baseline."
    - "If the fixture is green because bars are present, the header note
      is stale. If the fixture was fingerprint-only validated, the
      byte-identity signal is less meaningful than on trade_001."
  classification: UNVERIFIED — fixture status ambiguous, Olya prep pack
    flag 1 open.
  fidelity_signal: amber
```

### 2.3 Overall pattern

Reading across the six trades, a consistent mechanism emerges. Every trade whose chart‑truth depends on a *structural event at the very edge of detect.py's confidence* (Dec 4 1D MSS, Sep 7 1D MSS) is at risk of the cascade silently substituting a plausible‑state answer. Every trade whose chart‑truth lives well inside the detector's competence band (trade_001's Sept 24 4H MSS is in an interior window; trade_013's Feb 4 4H MSS is also interior) is not at risk from this class of hazard. Trade 007 is the one where the mechanism is audibly wrong because the window puts the decisive 1D MSS at the last week of a 45‑day lookback, right where ATR warmup and swing confirmation are most fragile.

This is not a detect.py problem. detect.py, run standalone on the same bars, gets the answer right. The fidelity gap is introduced in the Map's *assembly* of detect.py's output into a regime. Specifically:

1. `_initialize_regime_from_detections` (map_engine.py:250) looks only at `"1D"` MSS events, not 4H MSS. If 1D MSS doesn't fire for a given window, there is no secondary check against 4H.
2. If no 1D MSS events at all, the code falls through to "biggest displacement by `range_pips`" (map_engine.py:281‑284). This is a plausible fallback, not a methodology‑correct one. It can pick an earlier opposite‑direction displacement and stamp regime with the wrong direction.
3. No `MapConstructionMode.FALLBACK` tag is set when this happens. The gate's SW47 F1 scaffold (gate.py:122‑129) is armed but nothing sets FALLBACK, so the gate cannot refuse to evaluate on a silently‑fallen‑back Map.
4. Per‑trade validity is therefore latently contingent on whether detect.py's 1D MSS fires cleanly for that trade's window — and nothing enforces it.

This is *exactly* the failure class the advisor named Critical 1 + High 4 + High 6 and the COO input framed as P1 + P3 + P5. The evidence from Trade 007 confirms those priorities are correct and urgent.

### 2.4 Fidelity gap inventory (summary)

```yaml
total_trades_audited: 6
FAITHFUL: 1 (trade_001 — with green signal contingent on 1D MSS firing in its window)
LOCAL_DIVERGENCE: 3 (trade_003, trade_005, trade_006 — 1D MSS warmup + duplicate)
SYSTEMIC_DIVERGENCE_locally_patchable: 1 (trade_007 — plausible-fallback picks wrong regime)
UNVERIFIED: 1 (trade_013 — fixture status ambiguous; Olya prep pack flag 1)

overall_pattern: |
  One mechanism dominates: plausible-fallback state at the
  primitive→regime seam. Every amber/red signal above traces to
  the same authority surface (_initialize_regime_from_detections
  + its downstream silent fallbacks). This is patchable. It is
  not evidence that the architecture is wrong.

not_yet_audited: |
  Trades 002, 004, 008-012, 014 from annotated_trades.yaml. Five of
  these (002/008/010/012/014) are RETRACE cartridge cases which v1
  Map does not yet support (regime_required_phase deferred per
  FORWARD_PLAN §P3 D4_RESIDUAL). Two (004/009) are Asia Range Scalp
  cases handled by ARS canon (different path, 151/151 parity
  preserved). Trade 011 is RANGE cartridge case also deferred.
  Post-fix, re-audit 003/005/006/007 is the first priority; 001/013
  are the control cases.
```

---

## 3. Part 2 — Architectural assessment

### 3.1 Lean or bloated?

The native kernel is already small. Measured:

| Layer | Files | LOC (excluding vendored `ra_engine/`) |
|---|---|---|
| `console/map/` (Map) | 9 | 1,922 |
| `console/chain/` (gate + evaluator + canon runtime) | 18 | 4,635 |
| `console/governance/` | 5 | 558 |
| `console/execution/` | 6 | 466 |
| `console/data/` (bar/river/tf_aggregator) | 4 | 369 |
| `orchestrator/` | 2 | 571 |
| `observe/` (trace/replay shims) | 4 | 319 |
| `cartridges/` (loader + 2 YAML) | 3 | 500 |
| **Native kernel total** | **51** | **9,340** |
| `ra_engine/` (vendored detection — parity contract) | 39 | 12,036 |
| Tests | ~80 | 12,020 |

Observations:

- The Map (regime + DR + PDA + gate + day_state + persistence) fits in **under 2,000 LOC**. `regime.py` is 97 LOC. `gate.py` is 195 LOC. `pda_store.py` is 226 LOC. These are not bloated files.
- `chain_evaluator.py` at 581 LOC is doing real work (sweep → MSS → FVG → OTE matching); `ars_canon.py` at 492 LOC is a full mechanical canon. Neither reads as inherited complexity.
- The canon runtime (`chain/canon/` — runner_base, registry, ars/, map_canon/) sits at ~2,100 LOC including tracers and trace schemas. That is the real cost of separating strategy‑independent machinery from strategy‑specific logic. Some of it (MapCanonParams empty placeholder, SW41; dual `_find_armed_pda` functions, SW46) is acknowledged friction, but the total is well under what a bespoke orchestrator per cartridge would cost.
- `ra_engine/` at ~12 kLOC is the single dominant weight. It is declared vendored (parity contract with `~/research_accelerator`). It is not re‑authorable without breaking the contract with the source of truth for detection. The mypy‑strict SW44 tier 2 override lives here; strict typing is ambiguous under the parity posture.
- Tests at ~12 kLOC (853 passed + 4 xfailed) are roughly 1× production code weight. For a trading system that ratchets invariants, this is appropriate, not excessive.

The lean/bloat findings identified by the advisor (MapConfig — 0/18 fields read; `chain.sequence` parsed but not consumed; `governance_precedence` never read; `sl_method` presence‑required but content‑ignored) are real and are **already being closed** — the Phase 4a D3 verification pass enumerated them with REMOVE shapes and an invariant (`INV-MAP-BEHAVIOR-FROM-METHODOLOGY-NOT-CONFIG`) is registered. These are the tail‑end hygiene items of the refactor, not evidence of a bloated architecture.

**Verdict on Lean:** the kernel is already lean. The remaining "fake optionality" is enumerated, sized, and in flight. A rebuild would not produce a smaller kernel — the irreducible weight of the problem is in `ra_engine/`, which neither path touches.

### 3.2 Is the SYSTEM/CARTRIDGE split genuinely clean?

Nominally, yes. In practice, almost — with one honest asymmetry.

- `INV-CONSOLE-STRATEGY-BLIND` is grep‑auditable and clean post‑SW29: no cartridge names appear in `console/` executable code.
- `INV-CONSOLE-NO-CARTRIDGE-SHAPED-BRANCHES` is enforced post‑phase_3_4 c4.
- The cartridge loader is fail‑closed on strict schema (`day_state.required` migration landed; `max_trades_per_window` rejected; `htf_timeframes` enforced with cascade‑pair invariant).
- 6 import‑linter contracts KEPT + 0 broken at every atomic commit in Phase 3 (22 commits) is a strong signal — the architectural boundaries are machine‑enforced, not just declared.

The honest asymmetry: **the Map path does not dispatch through the canon registry.** `MapCanonRunner` is registered in `CANON_RUNNERS` to satisfy `G_PROVABLY_UNIVERSAL`, but `run_map_replay` constructs it directly (map_orchestrator.py:209‑221), not via registry lookup, because `daily_expansion.yaml` does not declare `canon_algorithm`. This is SW39 and it clusters with SW40/41/42/43 under the cartridge schema v2 resolution surface. Today the Map dispatches on entry‑script identity, not on cartridge declaration. It works, it is internally consistent, and it is named as not‑yet‑convergent. That is the correct disposition, not a concealment.

**Verdict on SYSTEM/CARTRIDGE:** clean in structure, pending convergence on dispatch. The split is the right split.

### 3.3 Does the cascade match the PRIMER's minimal shape?

PRIMER §1 describes the cascade as: "*Map holds regime + DR + active PDAs. When price arrives at an active PDA in the correct zone during a kill zone, the gate arms. The chain (sweep → MSS → FVG → OTE) fires inside the armed location.*"

Compared to the current cascade:

- Regime ← last matching‑or‑higher‑TF MSS. (`regime.py:31‑71`.) **Matches PRIMER.**
- Dealing range ← wick‑to‑wick of the regime‑establishing displacement leg, with daily→H4 authority cascade when daily is still expanding. (`dealing_range.py` + `map_engine.py:229‑242`.) **Matches PRIMER** (including Olya's ruling on rolling supersession).
- Active PDAs ← FVG detections with detector‑faithful direction + zone (SW04). Lifecycle (OPEN → TOUCHED → MITIGATED/INVALIDATED) in pda_store (SW01 retrace‑fill). **Matches PRIMER.**
- Gate ← ARMED iff regime permits direction + active PDA in correct zone + direction‑consistent PDA (SW47) + price contacts + kill zone. **Matches PRIMER.**
- Chain ← sequential sweep → MSS → FVG → OTE (INV‑CHAIN‑SEQUENCE‑FIXED). **Matches PRIMER.**

What PRIMER does *not* prescribe and the cascade silently inserts:

- Plausible‑fallback regime when 1D MSS absent (Trade 007 mechanism). PRIMER says *quiet*; the cascade says *plausible*. **Doctrine violation, patchable at 15 named sites.**
- Independent (not causally linked) matching of displacement + MSS in `day_state._check_expansion_delivered` (advisor High 6 / P5). PRIMER implies structural linkage; the code finds them separately. **Doctrine ambiguity pending Olya ruling.**
- H4 cascade authority is set but lifecycle replay uses daily bars (advisor High 5 / P4). **Mechanical partiality; not structural.**
- `_initialize_pdas_from_detections` loads all FVGs across selected TFs into current DR without regime‑establishment‑time scoping (docstring claims scoping; implementation does not enforce; advisor High 4 / P3 cluster A). **Doctrine‑implementation gap.**

**Verdict on PRIMER fidelity:** the cascade is the shape PRIMER describes. The fidelity leaks are at the *transitions between steps*, not in the steps themselves. Each leak has a name, a line number, and a sized fix.

### 3.4 If I were building from scratch today

I would start from exactly the same inputs you have (detect.py, vLOCK, ARS_CANON, annotated_trades, MAP_SPATIAL_PRIMER) and I would produce something that is within 10% LOC of what's currently in `console/` and `orchestrator/`. I would not produce something meaningfully smaller. The reason: the irreducible complexity is the four spatial objects (regime + DR + PDA + gate) plus the four‑step chain plus the canon runtime, and each is already at or near its minimal form.

Where I would do things differently on day one:

- I would require every authority surface (regime, DR, gate arming, day_state transition) to emit an explicit *confidence* or *construction mode* marker alongside its value, and make the gate refuse to evaluate on anything below a declared threshold. This is essentially what the SW47 F1 `MapConstructionMode.FALLBACK` scaffold is — already designed, currently unfired. I would wire it from the start.
- I would not permit silent `try/except: pass` on timezone compares anywhere in the Map. One `INV-DETECTION-TIME-TZ-AWARE`‑class invariant at the source (already established as SW24) plus a hard fail at every consumer would remove the advisor Medium 8 tail of hazards.
- I would make cartridge YAML the single source of governance + chain + Map configuration, loaded once at CLI entry and passed as an immutable object to everything downstream. No "reload by name" downstream. This closes the split‑brain (advisor Critical 2 / SW48) at day one rather than retrofitting.
- I would not have two separate `_find_armed_pda` functions (SW46 acknowledged). I would have one, parameterized by a `fallback: bool` flag.

These are five concrete *starting‑constraint* changes, not a different architecture. They save maybe 5‑8% LOC and eliminate a specific hazard class. Against the cost of re‑writing `MapEngine`, the canon registry, the day_state FSM, the chain evaluator, the governance single‑check site, and re‑deriving the 20+ named invariants — no, the saving does not come close to justifying the cost.

### 3.5 Swiss‑watch, honestly

The advisor's phrasing ("architecturally strong, operationally promising, not yet swiss‑watch certified") is the right read and I will not soften it. The things that block swiss‑watch certification, in order of how many trades they would affect if exercised in production:

1. **Silent plausible fallbacks in Map init.** (Trade 007 mechanism. Directly exercised by any window where 1D MSS doesn't fire cleanly. The 15 sites enumerated in OLYA_PREP_PACK §1 are the full inventory.)
2. **Fail‑open loader.** (`map_orchestrator.py:137‑141`. Any strategy YAML load failure silently degrades to `ChainConfig()` defaults + default kz + default LTF + no day_state gating.)
3. **Partial H4 cascade** (`_replay_price_forward(daily_bars)` always, not `h4_bars` under H4 authority).
4. **Day_state independent matching of displacement + MSS** (no causality check; methodology‑ruling‑dependent).
5. **MSS silent upgrade of displacement metadata** (`"VALID"`, `"ATR_RELATIVE"`, `"SINGLE"` defaults when properties absent).
6. **Count‑only detection parity** (SW52 / P6 — semantic parity not yet asserted).
7. **Terminal PDA not persisted** (SW06 — doesn't affect live but breaks forensic replay).
8. **`map_timeline` non‑determinism** (SW25 — `datetime.now()` on time‑omitted calls).

Gate (SW47) is closed. Dead config surfaces (MapConfig / chain.sequence / governance_precedence / sl_method) are D4‑REMOVE in flight. The surface that remains is defined, sized, and mostly independent — each item can ship on its own commit without cascading dependencies.

**Honest read on where en1gma sits today:** it is closer to swiss‑watch than the current test posture suggests (853 tests green, 6 lint contracts kept, mypy strict on enforced surface, 151/151 ARS canon parity, 6/6 DAILY_EXPANSION fingerprint‑level parity). The remaining distance is ~8 items with named fix shapes, not ~80 items of structural debt. But some of those 8 are methodology‑ruling‑gated, so they cannot be closed without an Olya session.

---

## 4. Part 3 — Path recommendation

### 4.0 Two axes, not one

The v1.0 report assumed a single axis of variation (rebuild vs harden) under sequential human-paced development. The CTO reframe surfaces a second axis: **execution model** (human sequential vs autonomous swarm under spec). The full decision surface is therefore:

```
                    ┌──────────────────┬──────────────────────────┐
                    │ HUMAN SEQUENTIAL │ AUTONOMOUS (spec-driven) │
  ──────────────────┼──────────────────┼──────────────────────────┤
  CONTINUE          │  CONTINUE-SEQ    │  CONTINUE-AUTONOMOUS     │
  (harden seams)    │  (Phase 4 as     │  (factory.ai Missions    │
                    │   currently      │   per seam, parity gate  │
                    │   scoped)        │   per Mission)           │
  ──────────────────┼──────────────────┼──────────────────────────┤
  MIDDLE_A/B        │  MIDDLE_A-SEQ    │  MIDDLE_A-AUTONOMOUS     │
  (subsystem        │  (4-12 wks)      │  (~1 wk spec + hours     │
   replacement)     │                  │   execution)             │
  ──────────────────┼──────────────────┼──────────────────────────┤
  MIDDLE_C          │  N/A             │  MIDDLE_C_AUTONOMOUS     │
  (orchestration    │  (would take     │  (~2-3 wks spec +        │
   layer rebuild)   │   months of      │   24-48hr execution +    │
                    │   handwork; not  │   review cycles)         │
                    │   a serious      │                          │
                    │   option)        │                          │
  ──────────────────┼──────────────────┼──────────────────────────┤
  FRESH_NUCLEUS     │  N/A             │  FRESH_NUCLEUS_AUTO      │
  (full kernel      │  (months)        │  (3-6 wks; preserves     │
   rebuild;         │                  │   detect.py+ra_engine    │
   ars preserved)   │                  │   only)                  │
  ──────────────────┴──────────────────┴──────────────────────────┘
```

Three live candidates for the panel: CONTINUE-AUTONOMOUS, MIDDLE_C_AUTONOMOUS, FRESH_NUCLEUS_AUTONOMOUS. MIDDLE_A-AUTONOMOUS remains valid as a conservative fallback and is evaluated briefly. MIDDLE_C-SEQUENTIAL and MIDDLE_B under any execution model are dominated by their neighbours and are not evaluated independently.

### 4.1 Candidate paths (evaluated honestly)

#### PATH_REFACTOR_CONTINUE (execution: SEQUENTIAL or AUTONOMOUS)

Close the advisor/COO‑enumerated authority‑surface gaps within the current structure. Phase 4a is actively doing this (SW47 landed; D3 verification pass completed; dead‑config D4 REMOVE batch in flight). Adds SW48‑SW52 + Olya‑gated P3/P5 + SW27/SW31. Runs the SW54 byte‑identity harness as the permanent correctness gate. Finishes cartridge schema v2 (SW38‑SW43 cluster) as the structural capstone.

Under SEQUENTIAL execution (v1.0 default assumption): ~3 months elapsed wall-clock, Olya session + schema v2 design session gating. Per §4.3 timeline.

Under AUTONOMOUS execution (CTO-authored brief per seam → factory.ai Opus Mission → parity-gated commit): ~3-6 weeks elapsed wall-clock, Olya session + schema v2 design session still gating. Per-seam implementation collapses from days to hours; integration review stays human-paced. The parity gate *at every atomic commit* is preserved and becomes a spec-incompleteness detector — any seam brief that produces commits which break 151/151 ARS or 6/6 semantic chart-truth fails the gate before merge, and the brief iterates. This is a critical property (see §4.1 MIDDLE_C_AUTONOMOUS for why).

```yaml
execution_model: SEQUENTIAL or AUTONOMOUS (recommend AUTONOMOUS for speed
                 with no risk penalty; SEQUENTIAL if autonomous capacity
                 is constrained)
lands_us_at_swiss_watch: YES, with disciplined execution
fidelity_preservation_risk: LOW — each change is parity-gated (151/151 ARS + 6/6 ground truth + lint + mypy strict at every commit, Phase 3 precedent).
structural_clarity_gained:
  - Every cartridge field is enforced, rejected, or absent (D4 complete)
  - No silent fallbacks (P3 Olya rulings land)
  - Gate arms only on methodology-coherent Map (SW47 + MapConstructionMode.FALLBACK fires)
  - Day_state is declarative + structurally linked (P5 ruling)
  - H4 cascade is fully authoritative (P4 SW50)
  - Semantic detection parity asserted (P6 SW52)
  - Dispatch converges via cartridge schema v2 (SW38-SW43)
time_rough_order:
  sequential: 8-16 weeks elapsed
  autonomous: 3-6 weeks elapsed (Olya + schema v2 design session gated)
  binding_constraint: Olya session scheduling, not implementation hours
preserved:
  - 22 Phase 3 atomic commits + parity discipline
  - 20+ named INV-* invariants
  - 47 named SW findings register (audit trail for every lesson)
  - 6 import-linter contracts, mypy strict CI, 853+4 test baseline
  - detect.py + ra_engine parity with source
  - 151/151 ARS canon + 306 advance() parity
  - ARS live paper trading continuity (zero touch)
discarded: nothing structural; dead config fields removed
rebuilt: nothing structural; seams tightened
failure_modes_honest:
  - Olya session delay extends the methodology-gated path indefinitely
  - Reference-re-baseline trap: if SW54 references are rebased to current
    (flawed-on-trade_007) output before P3/SW49 fixes, the harness
    codifies the fidelity gap as "correct."
  - Drip-feed exhaustion (SEQUENTIAL only): CTO + COO fatigue on the
    tail of findings could let minor items slide. AUTONOMOUS execution
    substantially mitigates this — the tail collapses from months to
    days once Olya rulings land.
  - Under AUTONOMOUS: CTO-brief quality becomes the binding constraint
    on per-seam correctness. Brief incompleteness produces commits
    that fail parity gate; that is a detector, not a silent failure —
    iterate the brief.
```

#### PATH_MIDDLE_C_AUTONOMOUS — spec-driven rebuild of the orchestration layer

**The CTO-proposed path.** Preserve detect.py, ra_engine, ars_canon + canon/ars/\*, methodology documents, cartridge YAMLs, the 20+ INV-\* invariants as specification, and the 46 closed SW findings as explicit requirements. Rebuild the Map orchestration layer under factory.ai Opus autonomous execution against a tight, gap-free specification that encodes everything the current codebase has learned plus the six day-one constraints from §3.4.

Scope of rebuild: ~5 kLOC of orchestration-layer code (`MapEngine`, `day_state`, `gate`, `canon/map_canon/*`, `orchestrator/map_orchestrator.py`, `cartridges/loader.py`, `observe/*`). ARS canon path — the self-contained `ars_canon.py` + `canon/ars/*` + the 151/151 parity surface + ARS paper trading on M3 — is explicitly **not touched**.

```yaml
execution_model: AUTONOMOUS only (sequential MIDDLE_C is not a serious option)
lands_us_at_swiss_watch: POSSIBLY YES, conditional on spec quality
fidelity_preservation_risk: MEDIUM — with an important caveat.
  spec_quality_is_the_whole_game: |
    Autonomous execution against a gap-free spec produces clean,
    fail-closed code that bakes in the five day-one constraints from
    §3.4 (ConstructionMode propagation, no silent try/except on tz,
    immutable cartridge-YAML-as-single-source, single parameterized
    _find_armed_pda, chart-truth-anchored fidelity gate). This is
    what rebuild advocates are right about.
  spec_incompleteness_hazard: |
    Autonomous execution against an INCOMPLETE spec produces code
    that is PLAUSIBLE-BUT-WRONG at the points the spec didn't cover.
    That is the same failure class — silent plausible state in
    absence of methodology ruling — that we are trying to close in
    the current cascade. Meta-irony: the rebuild is asked to fix a
    plausible-fallback hazard by invoking a capability whose
    characteristic failure mode is plausible-fallback at the spec
    layer. This is not disqualifying, but it is the single biggest
    risk of this path.
  mitigation_shape: |
    Spec discipline must be proportional to the semantic surface.
    ~5 kLOC of rebuild LOC implies ~2-3 kLOC of tight spec (~40-60%
    ratio) covering 20+ INVs, 46 closed SWs, chart-truth assertions
    for all 14 annotated trades, six day-one constraints, and
    explicit fail-closed disposition for every surface that currently
    silently defaults. Spec is written by CTO + Opus iteratively,
    with Olya session feeding the methodology-gated sections
    (P3 fallbacks, P5 causal linkage, SW27 FVG guard, SW31
    displacement grade). Spec is review-gated before execution
    begins. Spec gaps found during execution halt the Mission.
structural_clarity_gained:
  - Five day-one constraints baked in from line one rather than retrofitted
  - Meaningfully cleaner code surface (maybe 5-8% LOC reduction; morally
    larger reduction in "surface area of plausible-fallback hazard")
  - One unified dispatch path (no SW39 dispatch asymmetry to close later —
    it's gone by design)
  - Cartridge loader is fail-closed from line one; no SW48 split-brain
    surface exists to fix
  - ConstructionMode is load-bearing from day one; gate's SW47 F1
    scaffold is fired by construction, not aspirational
time_rough_order:
  spec_writing: ~2-3 weeks CTO+Opus iterative (Olya session feeds
    methodology-gated sections; spec writing is the dominant cost)
  autonomous_execution: ~24-48 hours factory.ai Opus Mission
  human_review_iteration: ~1-2 weeks (parity re-verification on 151/151
    ARS untouched, 6/6 chart-truth on new cascade, every INV re-enforced)
  total_elapsed: ~4-6 weeks, Olya session-gated identically to CONTINUE
preserved:
  - detect.py (88 LOC facade) + ra_engine (12 kLOC vendored) — untouched
  - ars_canon.py (492 LOC) + canon/ars/* (~1,500 LOC) — untouched
  - All methodology documents
  - All cartridge YAMLs (ars_v1_3 + daily_expansion)
  - 20+ INV-* specifications (encoded in new code, not in new docs)
  - 46 closed SW findings (encoded as test assertions on new code)
  - ARS live paper trading continuity (ars path is zero-touch)
  - Canonical surfaces (NORTH_STAR, PRIMER, CARTRIDGE_CONTRACT)
discarded:
  - ~5 kLOC of orchestration-layer code (the parts with accumulated
    fallback debt)
  - ~5-7 kLOC of tests tightly coupled to current cascade shape
  - 22 Phase 3 atomic commits' encoded discipline as LIVE CODE (it
    becomes spec input — still not lost, but no longer compounding
    in-place)
rebuilt: orchestration layer (~5 kLOC) + tests (~5-7 kLOC) against
  tight spec under autonomous execution
failure_modes_honest:
  - Spec incompleteness producing plausible-state code — the dominant
    risk. Mitigation is spec quality + per-Mission parity gate +
    review iteration. Non-zero even with discipline.
  - Implicit knowledge loss — some learnings from Phase 1-3 live in
    commit messages, PR discussions, in-session context that was
    never promoted to doctrine. A spec that captures "what we know we
    know" misses "what we know we learned but didn't write down."
    This is the real meaning of "re-earning invariants" — it is not
    the 20 named INVs (those transfer cleanly to spec) but the
    unnamed discipline those invariants protect.
  - Review bottleneck — ~5 kLOC of new code + all re-earned test
    assertions requires human review before merging against the
    current HEAD. CTO capacity is the secondary binding constraint.
  - Verification valley — during the review iteration period,
    DAILY_EXPANSION paper trading cannot run on the new stack. ARS
    continues. Dual-strategy paper trading delayed until MIDDLE_C
    closes.
  - Olya session still gating — P3 fallback dispositions and P5
    causal linkage rulings must land in the spec before execution.
    Timeline advantage vs CONTINUE is modest if Olya is the
    binding constraint for both paths (which she is).
  - Rebuild-completion trap — panel declares MIDDLE_C "done" when
    parity is green and tests pass, but a subtle implicit lesson
    re-emerges 3 months later as a new SW entry. Hard to guard
    against without a conservative lead-time before committing
    to dual paper trading on the new stack.

specification_shape_if_chosen: |
  Spec document structure I would propose to CTO:
    §1 Preserved substrates (links, versions, parity contracts)
    §2 Invariants to enforce (~20 INV-* reproduced verbatim with
       code-site mappings)
    §3 Closed findings to protect against regression (~46 SW entries
       reproduced with fix-class + test assertion shape)
    §4 Methodology constraints from vLOCK + Olya rulings
       (post-session-gated content)
    §5 Day-one constraints (six from §3.4 + chart-truth anchoring)
    §6 Module-by-module requirements with acceptance criteria
    §7 Test surface — semantic assertions from annotated_trades.yaml
       + byte-identity determinism + per-INV enforcement tests
    §8 Parity gates — 151/151 ARS preserved (untouched path);
       chart-truth-anchored 14/14 annotated trades (rebuilt path);
       mypy strict; import-lint contracts
    §9 Out-of-scope (ars_canon path, ra_engine internals)
    §10 Handoff — what Mission receives, what it returns, what
        constitutes done
```

#### PATH_FRESH_NUCLEUS_AUTONOMOUS

Preserve only the calibrated substrates (detect.py, ra_engine, vLOCK, ARS_CANON methodology doc, annotated_trades, MAP_SPATIAL_PRIMER, CARTRIDGE_CONTRACT). Rebuild everything above them — including `ars_canon.py` implementation — from scratch against tight spec under autonomous execution.

Under autonomous execution, the wall-clock for FRESH_NUCLEUS collapses from 3-6 months to ~4-8 weeks. But that is not the argument against it. The argument against it is that **it does not buy anything that MIDDLE_C_AUTONOMOUS does not already buy** — and it discards the 151/151 ARS zero-divergence canon, the 306 advance() parity cases, the live paper-trading continuity, and the most thoroughly-tested subsystem in the kernel, for no structural gain.

```yaml
execution_model: AUTONOMOUS only
lands_us_at_swiss_watch: POSSIBLY YES, conditional on spec quality (same
  as MIDDLE_C_AUTONOMOUS) — at higher total risk
fidelity_preservation_risk: HIGH. Every MIDDLE_C risk applies, plus:
  - ARS canon must be re-earned against 151/151 parity. Zero-divergence
    canon was expensive to establish originally (Phase 1 work) and
    has been treated as untouchable since. Rebuilding it under
    autonomous execution carries a real probability of introducing
    a subtle regression in a surface that currently has demonstrated
    production-grade trustworthiness.
  - ARS live paper trading on M3 must stop or run on the old kernel
    in parallel during transition. If it stops, a production-proven
    surface goes dark. If it runs in parallel, operational complexity
    during the most delicate part of the migration.
  - Every closed SW finding applies to TWO paths (ars + map) instead
    of one. Regression risk doubles at minimum.
structural_clarity_gained:
  - Same day-one constraints as MIDDLE_C_AUTONOMOUS
  - Uniform architecture across both paths — but this uniformity is
    cosmetic. DEC-ARS-BYPASSES-MAP is ratified. ARS doesn't need to
    share dispatch shape with Map to be correct.
  - Slightly cleaner canon runtime surface (SW41 empty params
    placeholder resolved at design time rather than retrofitted)
time_rough_order:
  spec_writing: ~3-4 weeks CTO+Opus iterative (larger surface, more
    methodology-gating because ARS rulings also re-grounded)
  autonomous_execution: ~48-96 hours factory.ai Opus Mission
  human_review_iteration: ~2-4 weeks (parity re-verification on
    everything; nothing preserved as a zero-touch surface)
  total_elapsed: ~6-10 weeks
preserved:
  - detect.py + ra_engine (vendored, unchanged)
  - Methodology canon as documentation (vLOCK + ARS_CANON.md + 
    annotated_trades + PRIMER + CARTRIDGE_CONTRACT)
  - 20+ INV-* as specifications
  - 46 closed SWs as requirements
discarded:
  - 9 kLOC of native kernel code (including ars_canon.py + canon/ars/*)
  - 12 kLOC of tests
  - 22 Phase 3 atomic commits' encoded discipline
  - 151/151 ARS zero-divergence canon as LIVE CODE (only as
    specification)
  - ARS paper trading continuity (must be re-earned)
rebuilt: everything above detect.py + ra_engine
failure_modes_honest:
  - All MIDDLE_C_AUTONOMOUS failure modes, at higher amplitude
  - ARS regression risk (highest-trust subsystem re-authored)
  - Opportunity cost: ARS data generation on M3 interrupted or
    duplicated; Dream Cycle data horizon delayed by the transition
    period
  - "Better on paper, worse in practice" — the six day-one
    constraints read clean, but applying them to a canon that was
    born mechanical and has 151 trades of zero-divergence parity
    risks "refactoring for cleanliness at the cost of battle-tested
    correctness"
my_honest_view: |
  FRESH_NUCLEUS is strictly dominated by MIDDLE_C under autonomous
  execution. If MIDDLE_C is right, FRESH_NUCLEUS is wrong. If
  MIDDLE_C is wrong, FRESH_NUCLEUS is more wrong. The only scenario
  where FRESH_NUCLEUS would be right is if the ars_canon + canon/ars
  path were ALSO exhibiting fidelity drift — which it is not
  (151/151 zero-divergence, 306 advance() parity, P1-verified on M3).
  Panel should treat FRESH_NUCLEUS as the control option that
  demonstrates the bar MIDDLE_C must clear, not as a recommended path.
```

#### PATH_MIDDLE_A_AUTONOMOUS — `MapEngine.initialize` replacement (fallback option)

Retained from v1.0 for completeness. Under autonomous execution, replace `_initialize_regime_from_detections`, `_initialize_dealing_range_from_detections`, `_initialize_pdas_from_detections`, `_replay_price_forward`, `_find_origin_before_displacement`, `_find_displacement_extreme`, `_compute_h4_dealing_range` as a single Mission. Spec is narrower than MIDDLE_C (~500 LOC of rebuild + ~500 LOC of tests). Closes the Trade 007 mechanism directly without touching gate, day_state, canon runtime, or orchestrator.

Timeline: ~2-3 weeks elapsed (spec ~1 week, execution ~24hrs, review ~1 week). Olya P3 session still gating.

**When MIDDLE_A beats CONTINUE-AUTONOMOUS:** if the panel decides that fixing the Trade 007 mechanism in one atomic well-scoped cleanroom replacement is preferable to closing 15 fallback sites incrementally. Both paths deliver the same semantic outcome (fail-closed Map init); MIDDLE_A does it as one large commit, CONTINUE-AUTONOMOUS does it as many small commits with parity gate at each.

**When MIDDLE_A loses to CONTINUE-AUTONOMOUS:** if the panel values parity-gate-at-every-commit as a structural property worth preserving (which the Phase 3 track record supports) over one-atomic-commit cleanliness.

### 4.2 Recommendation (revised under autonomous-execution reframe)

**Recommended path: PATH_REFACTOR_CONTINUE_AUTONOMOUS**, with the two non-negotiable additions from v1.0 preserved.

My confidence moved from ~90/10 CONTINUE/rebuild (v1.0, human cadence assumed) to ~60/35/5 across CONTINUE-AUTONOMOUS / MIDDLE_C_AUTONOMOUS / FRESH_NUCLEUS (v1.1, autonomous cadence available). The reframe moved me materially but did not flip me, for four reasons I will state clearly so the panel can attack them.

**Reason 1 — Olya is the binding constraint under both paths, and her session feeds a spec either way.** The reframe's speed advantage is largest when implementation hours dominate the critical path. For en1gma's Phase 4+ work, implementation hours are not on the critical path — Olya's methodology ruling on P3 fallback disposition and P5 day_state causal linkage is. Both CONTINUE-AUTONOMOUS and MIDDLE_C_AUTONOMOUS wait on the same session. The schedule-compression benefit is real but smaller than the reframe makes it look.

**Reason 2 — Parity-gate-at-every-commit is load-bearing, not ceremonial.** Phase 3 shipped 22 atomic commits × full parity gate × 0 reverts. That track record is not Phase 3's *output*; it is Phase 3's *property*. Under CONTINUE-AUTONOMOUS, this property is preserved — each autonomous Mission produces commits that must green the gate before merge. Under MIDDLE_C_AUTONOMOUS, parity-gate discipline is concentrated at the end of the rebuild (review iteration) rather than distributed across every step. If the spec has a gap, CONTINUE-AUTONOMOUS surfaces it at a single-Mission review (narrow context, fast iteration). MIDDLE_C_AUTONOMOUS surfaces it at rebuild-completion review (broad context, harder attribution). The distributed detector is structurally safer than the concentrated one.

**Reason 3 — The meta-irony is real.** The current kernel's fidelity problem is silent plausible-state substitution at seams where methodology is absent. MIDDLE_C_AUTONOMOUS asks us to close that problem by invoking a capability whose characteristic failure mode — when under-specified — is silent plausible-state substitution at seams the spec didn't cover. This is not disqualifying; spec discipline can cover it. But it is asymmetric: CONTINUE-AUTONOMOUS's characteristic failure mode is "slow iteration on a tight scope" and MIDDLE_C_AUTONOMOUS's is "fast iteration on an unclear scope." For a swiss-watch target, slow-on-tight dominates fast-on-unclear.

**Reason 4 — The implicit-knowledge tax is asymmetric.** en1gma's 20+ named INVs transfer cleanly to spec; those are the things we wrote down. Some of the 46 closed SWs transfer cleanly (the ones with registered invariants). Some transfer lossily (the ones with doctrine notes and commit-message reasoning). And some unnamed lessons — the stuff that lives in "Opus-era context," in the session logs, in the intuitions built over Phase 1-3 — do not transfer at all without explicit archaeology. CONTINUE-AUTONOMOUS inherits all of this for free because the code stays in place. MIDDLE_C_AUTONOMOUS must re-earn the unnamed subset, and we do not know the size of that subset until we miss one.

**Under what conditions would I flip to MIDDLE_C_AUTONOMOUS?** If all three of the following hold:

1. Spec discipline can be demonstrated *before* execution commits — by producing a full spec of the current kernel's orchestration layer that re-derives the 151/151 ARS parity and 6/6 chart-truth parity *without looking at the current code*. If that spec survives a CTO + Fresh Chair Opus + GPT review without ambiguity surfacing, spec quality is demonstrated.
2. The Olya session covers not just P3 + P5 but also an explicit "what did we know that we didn't write down" pass — a session specifically aimed at surfacing implicit calibration that would be at risk under rebuild. A tested yes.
3. The panel genuinely values the cleanliness of day-one constraints over the safety of incremental parity. This is a doctrine preference, not a factual matter. G rules on this.

If any of (1)(2)(3) fails, CONTINUE-AUTONOMOUS is the safer pick. If all three hold, MIDDLE_C_AUTONOMOUS becomes competitive — I would still pick CONTINUE-AUTONOMOUS by a narrow margin for the distributed-parity-detector reason, but I would not argue against MIDDLE_C_AUTONOMOUS as a defensible alternative.

**I would not recommend FRESH_NUCLEUS under any condition I can construct.** It is strictly dominated by MIDDLE_C_AUTONOMOUS. The only lever that reverses this is evidence that the ARS canon path is ALSO drifting — and that evidence does not exist (151/151 zero-divergence, 306 advance() parity, P1-verified on M3).

The two non-negotiable additions to CONTINUE (v1.0 §4.2) carry through unchanged:

**Addition 1: Chart‑truth as the fidelity gate, not pre‑SW02 reference files.** The SW54 test manifest (`test_daily_expansion_6_trade_parity.py`) uses byte‑identity against `traces/ground_truth/trade_NNN/`. Those reference files were generated by pre‑SW02 future‑leaking code. The current harness design is SHA‑based byte identity against those references — which means, if the references are regenerated from current code before the P3/SW49 fixes, the harness encodes the Trade 007 BEARISH output as "correct" and drives future regressions against a wrong answer. The correct anchoring is:

- Per trade, define `expected_regime`, `expected_authority_tf`, `expected_direction_permission`, `expected_pda_zone_class`, `expected_chain_completion` as semantic assertions pulled directly from `annotated_trades.yaml`'s `expected_state` block. This is the authoritative chart‑truth per INV‑OLYA‑ABSOLUTE.
- The SHA‑based byte‑identity harness can continue for determinism detection (re‑running the same code on the same bars must produce the same bytes), but the *fidelity* gate is the semantic gate.
- Re‑baseline the reference JSONL files *only after* P3/SW49 closes and semantic gates green — not before.

This is approximately a 50‑100 LOC test extension and delivers the SW54 intent without the encoding‑wrong‑answer trap.

**Addition 2: Make Trade 007 a named swiss‑watch exit gate.** Not "SW54 green on 6 trades." Specifically: "on bars from 2025‑08‑01 to 2025‑09‑16, `_initialize_regime_from_detections` produces `regime.direction == BULLISH` with `authority_tf == DAILY` (or cascades to 4H and produces BULLISH), with `MapConstructionMode == OK` (not FALLBACK), matching Olya's chart annotation." Two lines of assert, one named invariant (`INV-TRADE-007-REGIME-FIDELITY` or the generic `INV-REGIME-FROM-METHODOLOGY-NOT-FALLBACK`), and now the system cannot regress the mechanism that currently makes it produce BEARISH on a BULLISH chart.

Wire that as a Phase 4a exit gate and Phase 4 b/c scope can proceed with confidence.

### 4.3 Sequencing that supports the recommendation (CONTINUE-AUTONOMOUS)

Short of prescribing a Phase 4a/b plan (the CTO owns that), the sequencing I would defend in review under autonomous execution is:

```yaml
week_1:
  mission_1_dead_config_batch:
    what: "Phase 4a D4+ REMOVE batch — MapConfig + governance_precedence
           + sl_method + chain.sequence (partially registered already)"
    brief_author: CTO; mission: factory.ai Opus; parity gate: full
    elapsed: ~1 day including review
  mission_2_SW48_fail_closed_loader:
    what: "Collapse map_orchestrator.py:137-141 silent fallback;
           thread --strategy-yaml path through run_map_replay;
           register INV-STRATEGY-LOAD-MUST-SUCCEED"
    elapsed: ~0.5 day
  mission_3_sw54_semantic_gate:
    what: "Extend test_daily_expansion_6_trade_parity.py with
           semantic assertions pulled from annotated_trades.yaml
           expected_state blocks (Addition 1)"
    elapsed: ~0.5 day

week_2:
  olya_session:
    what: "P3 fallback cluster disposition (A-F) + P5 causal linkage
           + SW27 FVG initial guard + SW31 displacement grade +
           Shape 2 DEC-ARS-BYPASSES-MAP ratification + residual flags"
    format: 90-120min F2F per OLYA_PREP_PACK §7
    deliverable: OLYA_SESSION_RULINGS_2026_XX_XX.md (dense YAML per
                 §7 capture format)

week_3:
  mission_4_trade_007_root_cause:
    what: "Instrument + execute: verify the §2.2 mechanism hypothesis.
           Output: root-cause attribution + Trade 007 named exit gate
           (Addition 2: INV-REGIME-FROM-METHODOLOGY-NOT-FALLBACK)"
    elapsed: ~1 day
  mission_5_P3_SW49_fallback_dispositions:
    what: "Ship all 15 fallback sites per Olya rulings; wire
           MapConstructionMode.FALLBACK propagation so SW47 F1
           scaffold at gate.py:122-129 actually fires"
    elapsed: ~2-3 days autonomous, ~1 day review
  mission_6_P5_SW51_day_state_causal_linkage:
    elapsed: ~1 day

week_4:
  mission_7_P4_SW50_H4_cascade_replay:
    what: "_replay_price_forward(bars, tf); caller passes h4_bars
           when authority_tf=='H4'; add H4 PDA lifecycle test"
    elapsed: ~0.5 day
  mission_8_P6_SW52_semantic_detection_parity:
    elapsed: ~1 day
  mission_9_SW44_tier_1_test_annotations:
    what: "Mechanical mypy strict closure on tests/ (~976 errors)"
    elapsed: parallelisable with any other mission; ~1-2 days

week_5:
  mission_10_SW44_tier_3_utility_scripts:
    what: "Utility-script annotations + henry_analyst.py:253 latent-
           defect audit-first"
    elapsed: ~1 day

week_6_to_8:
  schema_v2_design_session:
    attendees: Olya + CTO + G
    what: "SW38-SW43 cluster design — canon_runner / canon_runner_params
           fields; CANON_RUNNERS lookup dispatch migration; BrokerProtocol
           + IntentBuilderProtocol formalisation; AuthorityTF redesign"
  mission_11_schema_v2_implementation:
    elapsed: ~3-5 days autonomous, ~1 week review (largest change in Phase 4)
  mission_12_walk_forward_revalidation:
    what: "Re-run on clean surface — DAILY_EXPANSION paper trading
           unblocks"
    elapsed: ~2 days

week_9_onward:
  - dual-strategy paper trading (ARS + DAILY_EXPANSION)
  - DAILY_CONTINUATION cartridge design (Olya chain spec gated)
  - graduation ceremony scoping
  - Dream Cycle data horizon begins
```

Total elapsed: ~6-8 weeks (not 3 months as v1.0 estimated). Binding constraints remain Olya session timing + schema v2 design session — neither is implementation-hour-limited. Existing ARS paper trading continues uninterrupted on M3 throughout. SW54 harness + chart-truth semantic gate becomes the DAILY_EXPANSION analogue of the 151/151 ARS canon — a permanent correctness gate. Every Mission carries full parity gate + lint + mypy strict at merge.

---

## 5. Risks and caveats to my recommendation

**I did not run the cascade end‑to‑end.** The Trade 007 mechanism hypothesis (§2.2) is attributed from code inspection, not execution. If the actual runtime produces BEARISH via a different mechanism than the displacement‑fallback I identified, the fix shape changes but the overall path recommendation does not — because every plausible mechanism I can think of is still a *local* seam problem, not a structural one. If live execution reveals the mechanism is something else entirely (e.g. a data pipeline issue, a detect.py output being truncated, an HTF lookback window miscalculation), the specific remediation would shift. The path recommendation would not.

**I weighted doctrine heavily.** NORTH_STAR, MAP_SPATIAL_PRIMER, and CARTRIDGE_CONTRACT are strong documents. It is possible that a fresh reader with different priors would read the same docs and find them more aspirational than they are. If, in practice, the console *is* leaking strategy knowledge in ways I missed by grep and direct read, the CARTRIDGE_CONTRACT enforcement signal is weaker than I reported. `rg -i "DAILY_EXPANSION|DAILY_CONTINUATION|ARS_V1|ars_v1_3" en1gma/console/` in an execution context would verify. I performed the read and trust the registered invariant; a third‑party check in an actual live run would be reassuring.

**I did not weigh timeline pressure.** The brief says "take as long as needed. No sprint pressure." I took that at face value. If there is in fact a business deadline (pair expansion, external capital, a review cycle) that makes the 3‑month CONTINUE path unacceptable, MIDDLE_A is the fallback — it closes the Trade 007 class of hazards in ~4‑6 weeks at higher within‑scope risk. FRESH_NUCLEUS remains wrong under any timeline I can imagine.

**I trust the closed‑defect register.** CLAUDE.md §15 (closed) lists 18 closed findings from SW01 to SW46. I read a sample (SW01, SW04, SW07, SW08, SW09, SW24, SW29) and found them substantive and well‑resolved. If that register is optimistic — if some closed findings are actually masked rather than closed — my confidence in CONTINUE should drop. A spot check by Fresh Chair Opus or a targeted re‑audit of 3‑5 closed items from different epochs would validate the register's integrity.

**Olya's availability is the critical path.** CONTINUE routes through one Olya session. If that session is 6+ weeks away, Trade 007 remains an open hazard for that long. The COO input notes "Olya's availability" as the gating event for P3 + P5 + SW27 + SW31. If Olya's schedule is the binding constraint and she is available sooner for a narrow session (e.g. P3 fallback cluster only), that changes the ordering but not the path.

**SW54 is already correctly designed for semantic drift detection, just not for chart‑truth fidelity.** My Addition 1 is additive, not a correction. The CTO may reasonably argue that chart‑truth anchoring belongs in a separate harness from byte‑identity determinism. That is a packaging question; the substance holds either way.

### 5.1 Autonomous-execution-specific risks (v1.1 addition)

These risks apply differentially across the three live paths and should shape how the panel weighs them.

**Risk A — Spec-incompleteness → plausible-state code at spec layer (dominant for MIDDLE_C / FRESH_NUCLEUS; minor for CONTINUE).** Autonomous execution is a multiplier on spec quality. A complete, tight spec produces clean code; an incomplete one produces plausible-but-wrong code at the uncovered points. This is the same failure class — silent plausible state in absence of authority — that we are trying to close in the current cascade. For MIDDLE_C, the whole orchestration layer is newly specified, so the attack surface for spec incompleteness is large. For CONTINUE-AUTONOMOUS, each Mission is narrowly scoped (one seam, one brief), so the attack surface per Mission is small and a gap surfaces at that Mission's parity gate, not at end-of-rebuild review.

**Risk B — Implicit-knowledge loss (dominant for FRESH_NUCLEUS; meaningful for MIDDLE_C; negligible for CONTINUE).** Some of en1gma's most valuable calibration is not in doctrine, not in named invariants, not in closed findings — it is in commit messages, PR discussions, session transcripts, and agent context. A rebuild that starts from spec + preserved substrates has a blind spot on "lessons we learned but didn't promote to doctrine." CONTINUE keeps all of this alive in the live code. MIDDLE_C loses the map-orchestration subset; FRESH_NUCLEUS loses more.

**Risk C — Review bottleneck (dominant for MIDDLE_C / FRESH_NUCLEUS; manageable for CONTINUE).** Autonomous execution can produce code faster than a human can review. Under CONTINUE-AUTONOMOUS, each Mission is ~1-3 days of output reviewed in 0.5-1 day — the ratio stays manageable. Under MIDDLE_C_AUTONOMOUS, ~5 kLOC of new orchestration + ~5 kLOC of re-authored tests arrives at review in one pass, against a human CTO whose attention on semantic correctness does not parallelise. CTO capacity is not an execution-speed concern under CONTINUE; it is an execution-speed concern under MIDDLE_C.

**Risk D — Brief-quality leverage (applies to CONTINUE-AUTONOMOUS as a new CTO skill).** Under CONTINUE-AUTONOMOUS, CTO brief authorship becomes the binding constraint on per-Mission correctness. A vague brief produces commits that fail parity gate and iterate — not silent failure, but slow. A precise brief produces clean Missions and fast closure. CTO brief-writing discipline needs to scale from "occasional dispatch" to "weekly throughput." This is a new skill, not a pre-existing capability gap.

**Risk E — Autonomous execution as a capability dependency.** Any path that routes through autonomous execution is dependent on that capability's availability, cost, and reliability. factory.ai Opus Missions are a capability, not a guarantee. If the capability degrades or becomes unavailable mid-program, CONTINUE-AUTONOMOUS degrades gracefully to CONTINUE-SEQUENTIAL (same path, slower). MIDDLE_C_AUTONOMOUS does not degrade gracefully — its whole premise is autonomous throughput on a single spec.

**Risk F — Swarm coherence across concurrent Missions.** If multiple Missions run concurrently (week 3-4 per §4.3), the resulting commits must merge cleanly. Under CONTINUE-AUTONOMOUS this is manageable because each Mission is a narrow seam (gate.py, day_state.py, etc.) and cross-seam conflicts are rare. Under MIDDLE_C_AUTONOMOUS the whole orchestration layer is in flight; if the Mission is split into parallel sub-Missions, coherence management becomes a significant CTO task.

**Risk G — "Looks swiss-watch, isn't" regression at closure.** Under any autonomous-execution path, the panel declaring "done" on the basis of "parity green + tests pass + lint clean + mypy strict" could miss a subtle fidelity issue that a week of live paper trading would surface. This risk is lower under CONTINUE-AUTONOMOUS (each seam is a small delta against a live system) and higher under MIDDLE_C_AUTONOMOUS (whole new cascade that has not traded a bar). Mitigation: mandatory shadow-mode observation period before DAILY_EXPANSION paper trading turns on, under any path. Recommend: 2 weeks minimum for CONTINUE-AUTONOMOUS, 4 weeks minimum for MIDDLE_C_AUTONOMOUS.

**What's risky about autonomous execution that isn't risky about human refactor?** The speed itself. Human-paced refactor has natural friction that forces reflection between steps. That friction is a feature when the steps are semantically subtle. Autonomous execution removes that friction; the parity gate partially substitutes for it, but only partially. Under any autonomous path, CTO owes explicit reflection time between Missions — this is not the default and has to be built in.

**What's risky about human refactor that isn't risky about autonomous execution?** Cognitive load fatigue over a long tail. CONTINUE-SEQUENTIAL would stretch over months; CTO attention naturally drifts. Autonomous execution compresses the tail and keeps it in one attention-coherent period. Under CONTINUE-SEQUENTIAL this risk was real and I rated it in v1.0 as "drip-feed exhaustion." Under CONTINUE-AUTONOMOUS it substantially evaporates.

---

## 6. What I'd want verified before acting on this recommendation

Short list. Most are ~30‑90 minutes of targeted work.

1. **Execute** the SW54 harness on the current HEAD with `SW47` direction filter on, and capture the actual per‑trade regime/DR/PDA/gate output. Confirm trade_007 produces BEARISH regime. Confirm trades_001/003/005/006/013 produce the expected regime. This grounds §2.2 in execution, not inference.
2. **Instrument** `_initialize_regime_from_detections` temporarily to log: (a) count of 1D MSS events received, (b) time + direction of each, (c) whether the displacement‑fallback branch fires, (d) what `best_disp.direction` picks if so. Run on trade_007 bars. This confirms the mechanism hypothesis.
3. **Run** detect.py standalone on the exact trade_007 window bars (2025‑08‑02 to 2025‑09‑16) and capture `results["mss"]["1D"]` detection list. Verify the Sep 7 BULLISH MSS is or is not present. This confirms whether the problem is "detector doesn't fire" vs "detector fires but cascade drops it."
4. **Spot‑audit** 3 closed SW findings from different epochs (e.g. SW01 from Block 0b, SW08 from Block 1, SW29 from Phase 3) by re‑reading the invariant's enforcement site + test coverage to confirm substance. This validates the closed‑defect register.
5. **Grep‑verify** `INV-CONSOLE-STRATEGY-BLIND` by running `rg -n "DAILY_EXPANSION|DAILY_CONTINUATION|ARS_V1|ars_v1_3|daily_expansion|ars_v1" en1gma/console/` and confirming zero hits in executable code. The Oracle claims this; a live grep verifies.
6. **Read** one Olya ruling record end‑to‑end to confirm the calibration authority trail is real (e.g. the 2026‑04‑20 F2F "YES SWAP IT" ruling that became SW01 / INV‑PDA‑MITIGATION‑IS‑RETRACE‑FILL). The `docs/workshop_sessions/` folder should contain the session record.
7. **Confirm with G** that the "take as long as needed" framing in the brief reflects actual timeline latitude. If there is in fact a nearby hard deadline (paper trading graduation date, ARS live capital request, Dream Cycle data horizon), say so — the recommendation may shift from CONTINUE to MIDDLE_A.

---

## 7. One thing I want on the record

The brief framed the question as a potential rebuild trigger, and invited an honest "rebuild from nucleus" answer. I have written the honest answer: under v1.0's human-cadence assumption, do not rebuild. Under v1.1's autonomous-execution reframe, MIDDLE_C_AUTONOMOUS becomes a legitimate path with a ~35% share of my confidence — but CONTINUE-AUTONOMOUS still wins on risk-adjusted terms at ~60%. The reframe moved the needle materially; it did not flip it.

I want to underline one thing that holds under **either** execution model, because the rebuild option can bias a fresh reader toward the more dramatic answer.

The kernel en1gma has today is not flawed because it was built wrong. It is flawed because a specific class of seam — the transition from *methodology‑absent* to *methodology‑present* inside the Map — was built to degrade plausibly rather than halt visibly. That choice was defensible early (the alternative was a system that refused to boot on noisy warmup data), but it is no longer defensible now that ARS is live on paper and DAILY_EXPANSION is being certified against chart‑truth. The correct response is to change the seam's discipline ("plausible → halt") at 15 named sites under methodology ruling. That is a finite, named, sized work package. It is not a rebuild, and it is not made more correct by being delivered in one atomic rebuild rather than 15 narrow seam changes.

The hardest work — the calibration of detect.py against Olya's eye, the derivation of vLOCK, the 27 answers, the ARS canon, the 14 annotations, the CARTRIDGE_CONTRACT — is already done. What remains is to make the kernel honor that work faithfully at every surface.

**Does autonomous execution change how we best do that honoring?** Yes — it removes implementation hours as a constraint on closing the seam, which means the Olya session's rulings can be baked in across all 15 sites in days rather than weeks. But it does not change *which seams need closing*, and it does not make "close them in one commit" safer than "close them in many parity-gated commits." The honoring is the same work under either execution model. Autonomous execution accelerates it. It does not redefine it.

---

## 8. Advisor review protocol

This section specifies what each seat should evaluate, what evidence they should challenge, and how convergence or divergence is resolved. Designed to make the four-way review decision-forcing rather than discussion-forcing.

### 8.1 Seat-by-seat charter

```yaml
G_sovereign:
  authority: final ratification; scope lock; capital implication
  evaluate:
    - Does the path recommended here match the vision in NORTH_STAR?
    - Is the "measure twice / permanent final form" principle honored
      by the execution model proposed?
    - Does the recommended Olya session cadence respect Olya's time
      as the scarce resource it is?
    - Are the capital implications of each path understood (ARS
      paper continuity, DAILY_EXPANSION paper trading unblock date,
      graduation ceremony timeline)?
  challenge:
    - "Is Opus's §4.2 confidence ratio honest, or is there pattern
      bias (fresh-reader tendency to favour conservative options)?"
    - "Is the autonomous-execution reframe being weighted correctly,
      or is Opus under-indexing on a capability that changes the
      economic calculus?"
    - "Is my 'prepared to go back to nucleus' framing being honored,
      or politely declined without adequate evidence?"
  bring_to_review:
    - Any timeline constraint not reflected in the v1.1 text
    - Any capital allocation implication for paper/live graduation
    - Any preference on "measure twice" vs "move faster" doctrine
      weighting the panel needs to know

CTO_Claude_session_experienced:
  authority: architectural coherence; invariant protection; execution design
  evaluate:
    - Coherence of each path with the 20+ ratified INV-* invariants
    - Coherence with Phase 3 parity-gate discipline (load-bearing vs
      ceremonial)
    - Feasibility of CONTINUE-AUTONOMOUS brief authorship at the
      weekly throughput §4.3 implies
    - Realism of MIDDLE_C_AUTONOMOUS spec quality expectations
    - Whether the Addition 1 + Addition 2 (chart-truth anchoring +
      Trade 007 exit gate) can be delivered inside any recommended
      path without scope creep
  challenge:
    - "Opus has not executed the cascade. How confident are we in
      the Trade 007 mechanism attribution (§2.2) without execution?"
    - "Is the §3.4 'if I were building this today' starting
      constraint list the RIGHT list, or has Opus missed items the
      current kernel has learned that a clean-slate would also need?"
    - "Is there a 7th or 8th day-one constraint that MIDDLE_C_AUTONOMOUS
      would need to be credible?"
    - "Spec quality claim: can CTO commit to producing a spec for
      MIDDLE_C_AUTONOMOUS that would survive Fresh Chair Opus + GPT
      review? Yes/no commitment question."
  bring_to_review:
    - In-flight Phase 4a work that would need to pause, halt, or
      fold into a chosen path
    - Estimated brief-authorship bandwidth given CTO's other scope
    - Any concrete hazards known from session context that v1.1
      doesn't capture (things the fresh reader wouldn't see)

Fresh_Chair_Opus_challenger:
  authority: red-team; challenge Opus-Cursor's recommendation on merit
  evaluate:
    - Is the autonomous-execution reframe being weighted fairly, or is
      Opus-Cursor conservative-biased?
    - Does the "meta-irony" argument (§4.2 Reason 3) hold up, or is
      it a rhetorical move?
    - Is "distributed parity detector > concentrated parity detector"
      (§4.2 Reason 2) actually true under autonomous execution, or
      is that artifact of human-review-cadence thinking?
    - Are any of the §2.2 mechanism hypotheses speculative enough to
      be wrong in ways that change the path recommendation?
    - Is there a 4th path (not considered) that dominates the 3 live
      candidates?
  challenge:
    - "Pick the single strongest argument for MIDDLE_C_AUTONOMOUS
      that Opus-Cursor did not make, and defend it."
    - "Pick the single weakest argument Opus-Cursor made for
      CONTINUE-AUTONOMOUS, and attack it."
    - "Is there evidence in the closed-SW register (§15 of CLAUDE.md)
      that a specific closed finding is actually only masked and
      would re-emerge under either CONTINUE or MIDDLE_C?"
    - "Is the '~60/35/5' confidence ratio calibrated or anchored?"
  bring_to_review:
    - Independent read of the 6 trade manifests without Opus-Cursor's
      framing
    - Independent evaluation of MIDDLE_C_AUTONOMOUS against the
      six day-one constraints; does Fresh Chair agree or differ?
    - Any structural read of en1gma that suggests a path Opus-Cursor
      missed

GPT_lateral:
  authority: second-order failures, scope-drift risk, orthogonal angles
  evaluate:
    - Second-order effects of each path that the close readers may miss
    - Scope drift risk — what could turn CONTINUE-AUTONOMOUS into
      CONTINUE-EVERYTHING-AUTONOMOUS (scope explosion via swarm)?
    - Scope drift risk — what could turn MIDDLE_C_AUTONOMOUS into
      FRESH_NUCLEUS_AUTONOMOUS (moving the knife from orchestration
      to ars path during review because "while we're here")?
    - Are there decisions the panel is about to make implicitly that
      would be better made explicitly?
  challenge:
    - "What is the second-order effect on COO / Sentinel / operator
      docs / launchd of each path? Has Opus-Cursor accounted for it?"
    - "Autonomous execution at scale is new operating territory for
      en1gma. Is the governance model for 'Opus runs Missions'
      actually safe? Where are the supervision failure modes?"
    - "What decisions does each path DEFER that the panel may regret
      not making now?"
    - "Is there a 'free optionality' choice where starting
      CONTINUE-AUTONOMOUS with an explicit decision point at Mission 3
      to re-evaluate MIDDLE_C_AUTONOMOUS keeps the option alive?"
  bring_to_review:
    - Any governance-layer question about autonomous execution
      supervision that the panel hasn't named
    - Any decision that implicitly ratifies something the panel may
      not want to ratify (e.g., "choosing CONTINUE-AUTONOMOUS
      implicitly chooses factory.ai as our primary execution
      capability going forward — is that the intent?")
    - Scope discipline recommendations per path
```

### 8.2 Convergence / divergence resolution

```yaml
if_all_four_seats_converge_on_one_path:
  action: G ratifies; CTO opens Phase 4+ under chosen execution model
  artifact: brief OLYA_SESSION + first Mission brief landed same week

if_three_seats_agree_one_disagrees:
  action: dissenter articulates blocking concern in writing; panel
          addresses each blocker individually; re-vote; if still 3-1
          after written addressing, G rules.
  discipline: dissent is captured, not papered over. If Fresh Chair Opus
              picks MIDDLE_C_AUTONOMOUS and rest pick CONTINUE-AUTONOMOUS,
              that is useful information for G even if CONTINUE proceeds.

if_two_two_split:
  action: G calls for second-round written briefs from each seat that
          name the single strongest argument for their pick and the
          single strongest argument AGAINST the other side. Re-read
          §4.1 + §4.2 + §5.1. If split persists, G rules under
          INV-SOVEREIGN-1.
  timeline: 48-72 hours for the second-round briefs; do not extend
            past one week.

if_a_seat_proposes_a_fifth_path:
  action: panel evaluates against §4.1 paths using §4.0 two-axis grid.
          If the fifth path fits a cell currently marked N/A or
          "dominated by its neighbour," revisit. If the fifth path
          introduces a new axis, escalate to Chairperson for
          architectural-framework review; do not rule this session.

if_olya_session_cannot_be_scheduled_within_2_weeks:
  action: panel considers MIDDLE_A_AUTONOMOUS as narrow-scope
          interim that closes Trade 007 mechanism without waiting
          on full P3 ruling. Review timeline accordingly.
  note: this is the only scenario in which I would prefer
        MIDDLE_A_AUTONOMOUS over CONTINUE-AUTONOMOUS.
```

### 8.3 What a successful review produces

A ratified path (one of: CONTINUE-AUTONOMOUS / MIDDLE_C_AUTONOMOUS / MIDDLE_A_AUTONOMOUS / hold-for-more-data), dated and signed by G; a ratified OLYA_SESSION agenda; a first Mission brief in CTO's hands within 72 hours of ratification; and captured dissent from any non-converging seats.

What a successful review does NOT produce: a long-form discussion of the architecture. The v1.1 advisor pack is the long-form discussion. The review ratifies or dissents.

---

## 9. Decision questions

The binary questions the panel must resolve to ratify a path. If the panel answers all of §9, a path has been picked. Designed that way deliberately.

```yaml
Q1_path_family:
  question: "Do we CONTINUE (harden seams in place) or REBUILD
            (replace orchestration layer, preserving substrates)?"
  binary_options:
    A: CONTINUE — retain current orchestration layer, close seams
    B: REBUILD — replace orchestration layer under spec
  opus_recommendation: A
  consequence_of_A: proceed to Q2 execution model; §4.3 sequencing
  consequence_of_B: proceed to Q3 rebuild scope; skip to Q5

Q2_continue_execution_model:
  applies_if: Q1 = A
  question: "Under CONTINUE, do we execute SEQUENTIALLY (CTO + Opus
            human-paced as Phase 3 shipped) or AUTONOMOUSLY (factory.ai
            Opus Missions with CTO-authored briefs + parity gate at
            every commit)?"
  binary_options:
    A: SEQUENTIAL (Phase 3 execution model continued)
    B: AUTONOMOUS (new execution model; CTO-brief authorship is the
       binding constraint)
  opus_recommendation: B
  consequence_of_B: CTO commits to weekly brief-authorship throughput
  consequence_of_A: v1.0 §4.3 timeline holds (~3 months)

Q3_rebuild_scope:
  applies_if: Q1 = B
  question: "Under REBUILD, do we rebuild the ORCHESTRATION LAYER only
            (MIDDLE_C — preserve ars_canon + ra_engine) or FULL KERNEL
            (FRESH_NUCLEUS — preserve only ra_engine)?"
  binary_options:
    A: MIDDLE_C (orchestration layer only; ars path untouched)
    B: FRESH_NUCLEUS (everything except detect.py + ra_engine)
  opus_recommendation: A
  consequence_of_A: proceed to Q4
  consequence_of_B: I advise against this; panel should re-read §4.1
                    FRESH_NUCLEUS_AUTONOMOUS before proceeding

Q4_spec_quality_demonstrated:
  applies_if: Q1 = B (any rebuild path)
  question: "Before execution begins, does CTO commit to producing a
            spec that (a) re-derives the current orchestration layer's
            behavior WITHOUT looking at the current code, (b) captures
            all 20+ INV-* invariants as requirements, (c) captures all
            46 closed SW findings as requirements, (d) captures the
            six day-one constraints from §3.4 as requirements, (e)
            survives Fresh Chair Opus + GPT review without material
            ambiguity?"
  binary_options:
    A: YES — CTO commits; spec review is a pre-execution gate
    B: NO — spec quality cannot be demonstrated to that bar
  opus_recommendation: this is a capability question, not a preference
    question. If A, rebuild is viable. If B, rebuild is not viable
    under the spec-quality-is-the-whole-game framing — revert to
    Q1 = CONTINUE.

Q5_olya_session_cadence:
  question: "Within what window is the next Olya session schedulable
            to cover P3 + P5 + SW27 + SW31 + Shape 2 + residual flags?"
  binary_options:
    A: within 2 weeks
    B: longer than 2 weeks (specify)
  opus_recommendation: A — this is the binding constraint on every
    live path. If B, panel considers MIDDLE_A_AUTONOMOUS as interim
    per §8.2.

Q6_trade_007_exit_gate:
  question: "Is 'on bars 2025-08-01 to 2025-09-16, regime
            initialization produces BULLISH with MapConstructionMode==OK
            (not FALLBACK), matching annotated_trades.yaml chart-truth'
            ratified as a Phase 4a exit gate under INV-REGIME-FROM-
            METHODOLOGY-NOT-FALLBACK?"
  binary_options:
    A: YES — ratified as exit gate
    B: NO — Trade 007 closure is aspirational, not gating
  opus_recommendation: A (Addition 2 from §4.2; non-negotiable)

Q7_chart_truth_anchoring:
  question: "Is the SW54 harness extended with semantic assertions
            derived from annotated_trades.yaml expected_state blocks
            (chart-truth anchoring), in addition to the existing SHA
            byte-identity gate?"
  binary_options:
    A: YES — semantic + byte-identity both enforced; byte-identity
       references are re-baselined ONLY after semantic gate greens
    B: NO — byte-identity alone (accept reference-re-baseline trap)
  opus_recommendation: A (Addition 1 from §4.2; non-negotiable)

Q8_dead_config_batch:
  question: "Does Phase 4a continue to ship the D4 REMOVE batch
            (MapConfig + governance_precedence + sl_method +
            chain.sequence) as currently scoped by Phase 4a D3
            verification pass?"
  binary_options:
    A: YES — ship as CONTINUE Mission 1 per §4.3, or fold into
       MIDDLE_C spec as 'these fields are not present in new schema'
    B: NO — defer or descope
  opus_recommendation: A (this is live Phase 4a work; halting it
    creates its own hazard)

Q9_autonomous_execution_governance:
  applies_if: Q2 = B or Q1 = B (any autonomous path chosen)
  question: "Is the governance model for autonomous Mission execution
            defined before first Mission runs? Specifically:
              (a) who authors briefs
              (b) who reviews Mission output before merge
              (c) what constitutes 'done' for a Mission
              (d) what happens when parity gate fails
              (e) how cross-Mission coherence is managed"
  binary_options:
    A: YES — defined in a short doc (autonomous_execution_protocol.md
       or similar) BEFORE first Mission
    B: NO — governance is ad-hoc per Mission
  opus_recommendation: A (GPT's legitimate concern from §8.1; this
    is the thing we should not learn through a Mission gone sideways)

Q10_post_review_dispatch:
  question: "Within 72 hours of ratification, does the chosen path's
            first Mission brief (or first Olya session agenda, or both)
            land on CTO's desk, with named owner + deadline?"
  binary_options:
    A: YES — ratification triggers dispatch
    B: NO — ratification is informational; execution starts later
  opus_recommendation: A (ratification without dispatch is not
    ratification; it is a pause)
```

---

## 10. Implications for G and CTO operating model

If the panel chooses any path that involves autonomous execution at scale (i.e., Q2=B or Q1=B), the operating model shifts in specific ways. This section names those shifts so the panel can ratify them explicitly rather than drift into them.

### 10.1 The mode shift

```yaml
before (Phase 1-3 mode):
  G_mode: sovereign — brief authorship, scope ratification, Olya F2F,
          occasional in-session review, capital approvals
  CTO_mode: synthesis + dispatch — author briefs, co-design with Olya,
            manage in-flight sprints, review Opus output at sprint
            boundaries, run retros
  Opus_mode: execute brief — hot-context sprint, parity-gated atomic
             commits, author retrospectives
  rhythm: briefs authored, sprints dispatched, rets authored; ~1-2
          ship cycles per week at peak
  throughput: Phase 3 shipped 22 atomic commits across 5 sub-phases in
              ~5 weeks — that's the baseline
  primary_cost: CTO context-load to author briefs + review output
  implicit_assumption: briefs and sprints happen one at a time;
                       CTO attention is the bottleneck

after (autonomous-execution mode):
  G_mode: unchanged (sovereign — path ratification, Olya F2F, capital
          approvals). G mostly sees this shift through CTO's
          throughput increase.
  CTO_mode: "coordinate the swarm" → "design the spec". Brief
            authorship bandwidth must scale from ~1/week to ~3-5/week.
            Review cadence must scale from sprint-boundary to
            Mission-boundary (multiple per week).
  Opus_orchestrator_mode: author + dispatch factory.ai Missions
            against CTO briefs; monitor; return output to CTO review
  factory.ai_Opus_Mission_mode: execute brief against spec; parity-gate
            at commit; halt + escalate on ambiguity
  rhythm: briefs authored weekly, Missions dispatched daily, review
          cadence weekly; multiple concurrent Missions possible
  primary_cost: CTO spec + brief quality
  implicit_assumption: the spec is the leverage point; briefs and
                       Missions are throughput-scaled against it
```

### 10.2 What CTO's attention needs to be on that it hasn't been on before

**Spec precision.** Under Phase 1-3, "brief" was a 2-5 page document describing a sprint scope with acceptance criteria. Under autonomous execution, the brief is the only thing the Mission sees. A paragraph that was unambiguous to a hot-context Opus is not unambiguous to a fresh factory.ai Mission. CTO spec discipline needs to rise correspondingly — more up-front work per brief, less mid-sprint clarification.

**Mission-brief dispatch cadence.** If CTO authors 1 brief/week, CONTINUE-AUTONOMOUS stretches to 8+ weeks. If CTO authors 3/week, it closes in 3-4. This is a direct conversion between CTO input bandwidth and elapsed wall-clock. Phase 1-3 did not reward higher brief-authorship throughput because Opus sprint capacity was the bottleneck. Now CTO is the bottleneck.

**Spec-gap detection via parity gate.** Under Phase 1-3, parity gate was a correctness check; CTO could trust that Opus had internalized doctrine. Under autonomous execution, parity gate is a spec-quality detector. A Mission whose commits fail parity is *telling* CTO the brief was incomplete. CTO has to read the failures as signal on the brief, not (only) signal on the Mission output. This is a new interpretive skill.

**Concurrent-Mission coherence.** If CTO dispatches 2-3 concurrent Missions per week (§4.3 week 3-4), cross-Mission conflicts at merge become a new failure mode. CTO needs explicit discipline on which Missions can run concurrently and which must serialize. Under CONTINUE-AUTONOMOUS this is manageable because each Mission is a narrow seam. Under MIDDLE_C_AUTONOMOUS this becomes a first-class CTO task.

**Autonomous-execution governance.** "Opus runs Missions" is a capability that needs a governance model before first Mission. Q9 captures this. Without it, the first Mission-gone-sideways writes the governance model post-hoc, and that is the wrong time to write it.

### 10.3 What stays the same

- **INV-OLYA-ABSOLUTE**: methodology rulings route to Olya. Autonomous execution does not change that.
- **Parity gate at every commit**: the single most valuable Phase 3 property. Preserved under CONTINUE-AUTONOMOUS. Slightly redefined under MIDDLE_C_AUTONOMOUS (concentrated at rebuild-review rather than distributed).
- **Halt overrides everything**: governance semantics unchanged.
- **INV-SOVEREIGN-1**: G's capital authority is orthogonal to execution model.
- **Atomic commits**: each Mission produces one or more atomic commits, each parity-gated. The unit of integration does not change.

### 10.4 Explicit ratification recommended

If the panel chooses Q2=B (any autonomous path), I recommend the panel also explicitly ratify:

- CTO brief-authorship throughput expectation (e.g., "~3-5 briefs/week during Phase 4")
- Autonomous-execution governance protocol (Q9 answer must be A before first Mission)
- Review cadence (e.g., "CTO reviews Mission output within 24 hours of completion; Missions do not merge without review")
- Capability-dependency posture (what happens if factory.ai Opus Missions degrade or become unavailable mid-Phase-4?)
- Post-Phase-4 continuation: does autonomous execution become the Phase 5+ default, or is Phase 4 a one-shot use?

These are not implementation details; they are operating-model changes that deserve explicit ratification alongside the path choice.

---

*End of advisor pack v1.1. Read-only investigation completed. No code touched. One docs commit proposed (this file — v1.1 replaces v1.0 in-place). Handoff to G for four-way review convening.*
