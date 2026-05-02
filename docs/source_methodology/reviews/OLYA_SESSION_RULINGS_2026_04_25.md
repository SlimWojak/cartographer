# OLYA SESSION RULINGS — 2026-04-25

```yaml
document: OLYA_SESSION_RULINGS_2026_04_25
purpose: canonical methodology record of Olya's rulings on SW51 prep pack questions
session_format: async (Olya via NEX advisor)
prep_pack: docs/reviews/OLYA_PREP_PACK_SW51_2026_04_25.md
preceded_by: docs/reviews/OLYA_SESSION_RULINGS_2026_04_24.md
confidence_overall: HIGH
implementation_unlock:
  - SW51 (active leg / causal linkage) — UNBLOCKED
  - SW27 (FVG selection for DAILY_EXPANSION) — UNBLOCKED
```

---

## Q1 — When does an active expansion leg END?

**Olya's ruling (her words):**

> "When I'm watching a move, I don't consider it finished just because price pauses or shows counter-structure on a lower timeframe — that is usually just a pullback. The move is only finished when there is a real MSS, meaning a displacement candle that breaks structure and shows clear intent in the opposite direction."

**Conditions and caveats:**
- Pullbacks ≠ end of move
- Lower timeframe flips ≠ end of move
- A real MSS requires:
  - displacement
  - that breaks structure
  - opposite-direction intent
- Only then → move is finished

**Confidence:** HIGH

**CTO classification:**

```yaml
scope: console
effect: methodology + structure
affected_SW_IDs: [SW51 (primary)]
chosen_option_from_prep_pack: A_OR_B (combined — opposing expansion that breaks structure)
invariant_alignment:
  - INV-MAP-CONSTRUCTION-MODE-EXPLICIT (active leg state is structural; absence of evidence to terminate = leg remains active)
  - INV-REGIME-FROM-METHODOLOGY-NOT-FALLBACK (current latest-opposing-MSS-wins logic is the bug)
implementation_implication: |
  An "active leg" / "active move" is a system-tracked object that PERSISTS
  through pullbacks. The end condition is symmetric with the start condition:
  a real MSS (displacement + structure break + opposite-direction intent).
  
  Crucially: lower-timeframe counter-structure does NOT end an HTF move.
  This rules out the current system behavior of treating any same-TF or
  lower-TF opposing MSS as a regime flip.
key_principle: "End of move = real MSS. Anything else = same move."
outstanding_clarification: 
  structure_boundary_definition: |
    Olya says "structure of the move." CTO must map to existing system
    objects: likely the move's MSS-origin / protected swing high-low pair.
    Pre-implementation read-only audit recommended (per GPT assessment).
```

---

## Q2 — Retrace vs reversal during an active move

**Olya's ruling (her words):**

> "When I'm watching a move, I first define the structure of that move. As long as price stays within that structure, I treat any counter-movement as a pullback. I only consider it a reversal when price breaks that structure and shows displacement in the opposite direction."

**Conditions and caveats:**
- Structure defines the move
- Counter-moves inside structure = pullbacks
- Reversal requires:
  - break of structure
  - AND displacement in opposite direction

**Confidence:** HIGH

**CTO classification:**

```yaml
scope: console
effect: methodology + evaluation
affected_SW_IDs: [SW51 (primary)]
chosen_option_from_prep_pack: B (structural origin / structure boundary defined by the move)
                              with_A_caveat (counter-MSS plus displacement is the signal — same as Q1's end-of-move definition)
invariant_alignment:
  - INV-EPISTEMIC-INTEGRITY (system must not lie at authority surfaces — current system reports EXPANSION when methodology says RETRACE)
  - INV-REGIME-FROM-METHODOLOGY-NOT-FALLBACK
implementation_implication: |
  The "structure of the move" is a first-class object. While price stays
  inside the move's structure boundary, every counter-direction event
  (including same-TF or lower-TF MSS, including displacement) is RETRACE.
  
  Reversal requires BOTH conditions:
    1. break of that structure (price exits the move's boundary)
    2. displacement in the opposite direction
  
  This is the unification of Q1 and Q2: the END condition for the active
  move is THE SAME as the REVERSAL condition. Olya's mental model treats
  these as one event, not two.
empirical_validation: |
  This rule predicts 5 of the 6 chart-truth RED fixtures will flip from
  EXPANSION to RETRACE when implemented. Those 5 fixtures are exactly the
  case where current system sees counter-MSS and promotes to EXPANSION
  while the move's structure remained intact.
edge_case_check_volunteered_by_Olya: |
  Olya did NOT explicitly address the prep pack's TF-priority hierarchy
  question. Implicit answer from Q1: lower-TF counter-structure does NOT
  end an HTF move. So the structure boundary is read at the move's HTF;
  lower-TF events are evaluated against that HTF boundary.
outstanding_clarification: 
  none (rule operationalized cleanly)
```

---

## Q3 — Displacement-MSS pairing

**Olya's ruling (her words):**

> "I use the displacement that actually breaks the structure. That is the move that matters to me, because it's the one that creates the MSS and shows real intent."

**Conditions and caveats:**
- Not any nearby displacement
- Must be the one that directly causes the structure break
- That move defines the valid expansion leg and context

**Confidence:** HIGH

**CTO classification:**

```yaml
scope: console
effect: methodology + evaluation
affected_SW_IDs: [SW27 (primary)]
chosen_option_from_prep_pack: A (STRICT 1:1 — the bar that broke structure IS the confirming displacement)
invariant_alignment:
  - INV-EPISTEMIC-INTEGRITY (FVG selection must be rule-anchored, not heuristic-defaulted)
implementation_implication: |
  The structural break bar IS the confirming displacement bar. 1:1 mapping.
  
  For SW27 (FVG selection in DAILY_EXPANSION):
    - the FVG to trade is the FVG created BY the structure-breaking
      displacement bar
    - NOT the strongest nearby bar (B from prep pack)
    - NOT the leg-wide strongest displacement (C from prep pack)
    - NOT first/smallest/nearest by other criteria
  
  The existing MSS detector already identifies the structural-break bar.
  SW27 implementation reads from that detector's output; no new
  computation required for displacement identification.
sw27_complexity: lower than feared (per GPT assessment)
sw27_dependency: requires SW51 to land first (active leg as first-class concept exposes the structural break bar with the right context)
outstanding_clarification:
  none
```

---

## Anchor — trade_007 leg story

```yaml
status: NOT_ANSWERED_BY_OLYA_IN_THIS_PASS
note: |
  Olya's prep pack reply addressed Q1+Q2+Q3 with high-confidence rulings.
  The trade_007 anchor narrative was not returned.
  
  Disposition: NOT BLOCKING. The Q1+Q2+Q3 rulings are sharp enough to
  drive SW51 implementation without the anchor. If implementation surfaces
  ambiguity that the anchor would resolve, request narrowly at that time.
follow_up_if_needed: optional narrow ping for trade_007 specifically
```

---

## Summary of Mission implications

```yaml
SW51_active_leg_causal_linkage:
  ruling_input: Q1 (primary — end condition) + Q2 (primary — boundary + retrace/reversal)
  status: UNBLOCKED for implementation brief authoring
  implementation_shape_per_GPT_recommendation: |
    Minimal ActiveMove object with fields {direction, structure_high,
    structure_low, origin_time, structure_break_time, confirming_displacement_id,
    confirming_mss_id, status: ACTIVE | ENDED}.
    
    AVOID big engine. AVOID time expiry. AVOID displacement-strength alone.
  pre_implementation_audit_required: |
    Read-only inspection of existing system data objects to determine
    whether regime/MSS already exposes the structure boundary. If yes,
    use existing surface. If not, narrow extension brief lands the
    boundary primitive first.
  empirical_target: 5 of 6 chart-truth RED fixtures flip to PASS

SW27_FVG_selection_for_DAILY_EXPANSION:
  ruling_input: Q3 (primary)
  status: UNBLOCKED
  dependency: SW51 lands first (need active-leg context exposed)
  implementation_shape: trivial — read structural-break bar from existing MSS detector; FVG associated with that bar's displacement is the trade target

SW31_displacement_grade_filter:
  ruling_input: Q4 from 2026-04-24 (primary)
  status: HTF_alignment_clarification_now_resolved per Q1+Q2 of this session
  HTF_alignment_now_means: "weak displacement direction matches the active move's HTF direction" (not "co-located with HTF PDA"; Q4's three-condition list resolves this naturally per Q1+Q2 of THIS session — Q1 establishes HTF move persistence, Q2 establishes the structure that defines direction context)
  implementation_unblocked: yes
  not_in_critical_path: SW31 is independent of SW51/SW27 sequencing

trade_011_three_field_failure:
  status: hypothesized_resolvable_by_SW51 (per CTO synthesis 2026-04-25)
  if_SW51_lands_and_trade_011_remains_RED: register narrow follow-on (SW58-class) for cascade-authority logic
  monitoring: chart-truth gate post-SW51

residual_NYOKZ_reversal_potential:
  ruling_input: 2026-04-24 residual_1
  status: PARKED in VAULT (DAILY_CONTINUATION / DAILY_REVERSAL future cartridge family)
  no_current_action
```

---

*Canonical methodology record. Changes require Olya ratification. Implementation scopes referenced above belong in Phase 4b Mission briefs, not in this document.*