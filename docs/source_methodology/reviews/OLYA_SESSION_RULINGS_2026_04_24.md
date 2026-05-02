# OLYA SESSION RULINGS — 2026-04-24

```yaml
document: OLYA_SESSION_RULINGS_2026_04_24
version: 1.0 (CANONICAL — methodology record)
date: 2026-04-24
session_format: async via Olya's GPT advisor (facilitation + capture)
ruling_authority: Olya (CSO)
captured_by: Olya's GPT advisor; classified by CTO
supersedes: OLYA_PREP_PACK_RESHAPED (pre-session artifact; archived)
purpose: |
  Canonical record of Olya's methodology rulings on the four primary
  questions plus residual from the 2026-04-24 async session. These
  rulings feed Phase 4b Missions (SW49/SW51/SW27/SW31) and are the
  authoritative methodology source for implementation scope.
rule: |
  This document captures rulings. Implementation belongs in the Phase
  4b Mission briefs that cite these rulings. Do not interpret beyond
  what is captured; route back to Olya if operational ambiguity surfaces.
authority_tier: 1 (methodology record; alongside ARS_CANON, vLOCK, annotated_trades)
```

---

## Q1 — Evidence absence: what to do when the chart doesn't show structure

**Olya's ruling (her words):**

> "When the chart is messy and there's no clear structure or direction, I don't force a bias — I wait for the market to show its hand through a clear move or structure forming. Usually I already have prior context, so I may hold that bias and wait for a range break or reaction from HTF PDAs to guide the next move. If nothing is clear, I stay out of directional trades."

**Conditions and caveats:**
- Prior bias can persist if already watching (not a cold-start mindset)
- Will wait for range break OR HTF PDA reaction to regain clarity
- LTF scalps are allowed only if a defined strategy exists (not random execution)

**Confidence:** high

**CTO classification:**

```yaml
scope: console
effect: evaluation + methodology
affected_SW_IDs: [SW49 (as rescoped per reset brief §6)]
invariant_alignment:
  - INV-SYSTEM-NO-STATE-INVENTION
  - INV-NO-EVIDENCE-NO-TRADE
  - INV-UNKNOWN-STATE-HALTS (partial — "stay out" maps to NO_TRADE, not HALT)
implementation_implication: |
  System must not fabricate regime direction when structure is absent.
  "No structure = no directional trade" is the operational rule.
  Distinction between cold-start (no prior context) and warm-state
  (prior context exists, now ambiguous) is methodologically real and
  may require separate code treatment: cold-start routes to
  NEUTRAL/PENDING, warm-state may persist prior regime until
  structural evidence (range break OR HTF PDA reaction) refreshes it.
  Second-order nuance — not a Phase 4a blocker.
outstanding_clarification: |
  Operational definition of "HTF PDA reaction" as a regime-refresh
  trigger. Olya mentions it explicitly but we don't have a crisp
  code-level rule. Defer to SW49 implementation brief or Phase 4b
  methodology follow-up.
confidence_that_rules_are_implementable: high
```

---

## Q2 — Chain delivery: displacement and MSS linkage

**Olya's ruling (her words):**

> "For me, expansion is a strong impulsive move that breaks structure — displacement and MSS are part of the same leg, not separate events. I don't treat displacement and MSS independently; the expansion itself creates the structure shift. If the move continues into the next day in the same direction, I still consider it part of the same expansion leg, even if the Daily doesn't show a fresh MSS."

**Conditions and caveats:**
- MSS + displacement = same continuous move (same leg)
- Can span multiple days if momentum continues
- Daily timeframe may not show MSS → LTF structure confirms it
- A pullback day after expansion = not a new expansion, just retrace phase

**Confidence:** high

**CTO classification:**

```yaml
scope: console
effect: methodology + evaluation
affected_SW_IDs: [SW51 (primary), SW49 (secondary — regime machine implications per reset brief §3)]
invariant_alignment:
  - INV-MAP-CONSTRUCTION-MODE-EXPLICIT (legs are structural state; absence of leg evidence = PENDING_METHODOLOGY_RULING)
  - INV-REGIME-FROM-METHODOLOGY-NOT-FALLBACK (current "latest-opposing-MSS-wins" logic is methodologically naive per Q2)
implementation_implication: |
  Current system treats displacement and MSS as independent signals.
  Olya's ruling requires a representation of "expansion leg" where
  displacement and structurally-linked MSS are components of the same
  move. Implementation shape TBD — GPT caution applies (avoid building
  a leg-engine; prefer authority-promotion-gate framing per reset
  brief §3).
  
  Multi-day continuation: a same-direction move continuing across
  day boundaries is still one leg. This has implications for how
  regime persists across replay dates.
  
  LTF confirmation: daily MSS absence doesn't negate expansion if
  LTF structure confirms. Connects to INV-MAP-SCOPE-V1.1 (daily → H4
  cascade) and may require activation of cascade under ambiguity
  conditions, not only under "daily expanding."
  
  Pullback vs reversal: a counter-directional MSS within an active
  leg is retrace, not regime flip. The operational rule for
  "retrace vs real reversal" is not captured in this ruling — likely
  requires follow-up Olya touch if SW51 implementation cannot
  disambiguate from Q2 alone.
outstanding_clarification: |
  What distinguishes a genuine reversal from a deep retrace? Olya's
  Q1 said "range break OR HTF PDA reaction" triggers regime refresh;
  plausibly the same rule applies here but not explicitly confirmed.
  Candidate narrow follow-up question if SW51 authoring stalls.
confidence_that_rules_are_implementable: medium-high (pending clarification above for edge cases)
```

---

## Q3 — FVG selection for DAILY_EXPANSION

**Olya's ruling (her words):**

> "The FVG selection rule is not universal — it depends on the strategy. For momentum-type setups like DAILY_EXPANSION, I take the FVG that forms after the sweep, specifically the one created by the displacement candle that confirms the MSS."

**Conditions and caveats:**
- FVG must be part of displacement that drives the MSS
- Not just any FVG after sweep → must be structurally tied to the move
- This is a momentum-specific rule, not global

**Confidence:** high

**CTO classification:**

```yaml
scope: cartridge
effect: evaluation
affected_SW_IDs: [SW27]
dependencies: [SW51 must land first — Q3 presupposes displacement-MSS linkage exists as a computed concept]
invariant_alignment:
  - INV-RULING-SCOPE-EXPLICIT (cartridge-scoped, not universal)
  - INV-CARTRIDGE-ABSENCE-IMPLIES-NO-TRADE (if no displacement-MSS-linked FVG exists, no trade)
implementation_implication: |
  SW27 cannot be implemented until SW51 (or equivalent work) exposes
  "the displacement that confirms this MSS" as a first-class object.
  Once that exists, SW27 is "find FVG inside that displacement candle
  and select it as the chain FVG."
  
  Prior CTO-suspicion (guarded-first with bar-distance parameter) was
  wrong. No bar-distance parameter needed. Selection is structural
  (displacement-MSS pairing), not temporal-proximity-based.
  
  Universality: explicitly ARS-vs-DAILY_EXPANSION different. ARS
  rule (first valid FVG post-sweep) locked in ARS Canon v1.3 §5/§14.
  DAILY_EXPANSION rule per this ruling. Future cartridges ask separately.
outstanding_clarification: none at methodology level
confidence_that_rules_are_implementable: high (after SW51 dependency resolves)
```

---

## Q4 — Displacement grade filter

**Olya's ruling (her words):**

> "Weak displacement can be valid, but only in the right context. I require HTF alignment, correct location, and a sweep — the market must show intention by taking liquidity before I act. Without a sweep, I don't trust weak displacement."

**Conditions and caveats:**
- HTF alignment = mandatory (for weak displacement)
- Must be at correct PDA / location
- Sweep required to confirm intention
- Weak displacement without sweep = reject
- Strong displacement doesn't need this strict filter

**Confidence:** high

**CTO classification:**

```yaml
scope: cartridge
effect: evaluation + configuration
affected_SW_IDs: [SW31]
invariant_alignment:
  - INV-CARTRIDGE-ABSENCE-IMPLIES-NO-TRADE (weak displacement without context = ineligible)
  - INV-RULING-SCOPE-EXPLICIT (cartridge-scoped per displacement-grade schema)
implementation_implication: |
  Grade is NOT removed from schema (earlier CTO-suspicion was wrong).
  Grade IS consumed as a filter, but not via simple threshold. Logic:
  
    if displacement.grade == "STRONG":
        eligible (no additional context check)
    elif displacement.grade in ("VALID", "WEAK"):
        require htf_alignment AND pda_location_match
        (sweep already required by chain structure)
    else:
        ineligible
  
  Sweep requirement is not new — it's chain discipline (sweep → MSS →
  FVG → OTE). Confirmation that existing chain is correct for this case.
outstanding_clarification: |
  "HTF alignment" operational definition. Olya's language is
  methodology-level; code needs specificity: does HTF alignment mean
  weak displacement direction matches HTF regime direction, or
  something more specific (e.g., weak displacement at HTF PDA with
  matching direction)? Recommend narrow clarifying ping to Olya's GPT
  before SW31 authoring:
  
    "When you say HTF alignment for weak displacement, do you mean the
    displacement direction must match the HTF regime direction, or
    something more specific like weak displacement at an HTF PDA that
    matches the expected reaction direction?"
  
  Non-blocking — CTO can author SW31 brief with placeholder and
  resolve clarification in parallel.
confidence_that_rules_are_implementable: medium-high (pending HTF alignment clarification)
```

---

## Residual 1 — trade_003 and trade_005 same-date intent

**Olya's ruling (her words):**

> "Yes — both trades are valid. Typically LOKZ gives the start of the move and NYOKZ provides continuation of that same expansion. However, NYOKZ can also produce a reversal instead of continuation."

**Conditions and caveats:**
- LOKZ = often initiation phase
- NYOKZ = can be continuation of same move OR reversal setup depending on context
- Not restricted to 1 trade per day from methodology perspective

**Confidence:** high

**CTO classification:**

```yaml
scope: cartridge (risk engineering, not methodology)
effect: configuration
affected_SW_IDs: none directly (informs future cartridge design, not current Phase 4)
invariant_alignment: none
implementation_implication: |
  max_trades_per_day=1 in current cartridges is risk-engineering, not
  methodology. Confirmed. No current action required.
  
  Forward implication: NYOKZ reversal-vs-continuation is a future
  cartridge consideration. Parked in VAULT as potential follow-up
  (DAILY_CONTINUATION or DAILY_REVERSAL cartridge family).
park_note: |
  Olya's mention of NYOKZ reversal is new methodology surface we
  hadn't asked about. Capture in VAULT.md under DAILY_MOMENTUM family
  expansions. Not Phase 4 scope.
confidence: high
```

---

## Summary of Mission implications

```yaml
SW49:
  ruling_input: Q1 (evidence absence), Q2 (regime machine methodological concern)
  status: scope to be re-decided per reset brief §6
  
SW51:
  ruling_input: Q2 (primary)
  status: scoped but requires implementation-shape decision (authority-promotion-gate vs explicit leg modeling); dependency target for SW27

SW27:
  ruling_input: Q3 (primary)
  status: clear scope; gated on SW51 landing (displacement-MSS linkage as first-class object)

SW31:
  ruling_input: Q4 (primary)
  status: clear scope; pending HTF-alignment operational clarification (small Olya ping)

residual_1:
  ruling_input: confirmed
  status: no current action; parked NYOKZ-reversal as future cartridge consideration

trade_007_BULLISH_annotation:
  ruling_input: Olya's original annotation confirmed valid; current code produces BULLISH at Sep 16
  status: reference truth superseded by chart truth; see PHASE_4A_RESET_AND_FORWARD_BRIEF §2
```

---

*Canonical methodology record. Changes require Olya ratification. Implementation scopes referenced above belong in Phase 4b Mission briefs, not in this document.*