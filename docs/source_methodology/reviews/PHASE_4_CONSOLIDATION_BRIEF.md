# PHASE 4 CONSOLIDATION BRIEF

```yaml
document: PHASE_4_CONSOLIDATION_BRIEF
version: 1.0
date: 2026-04-24
author: CTO (Claude, Opus 4.7)
ratified_by: G (sovereign)
audience: Opus (Cursor, continuing from FIDELITY_AUDIT_AND_PATH_RECOMMENDATION v1.1 authorship)
purpose: |
  Stage the Phase 4 chapter inside the repo. Consolidate the ratified
  path, clean house on orientation docs, write the autonomous execution
  governance protocol, and reshape the Olya prep pack under canon-first
  discipline. Deliverable: a set of coherent docs that a fresh CTO or
  advisor can orientate against in ~30 minutes and begin execution.
rule: |
  Clean, crisp, non-bloated. Doc hygiene is a first-class success
  variable for CONTINUE-AUTONOMOUS. Do not preserve session-continuity
  residue that doesn't serve fresh orientation. If a paragraph doesn't
  earn its place, cut it.
scope: documentation consolidation + governance drafting; no code changes
source_head: current main at ratification time
```

---

## 1. Ratified position

Four-way review (G sovereign + CTO Claude + GPT lateral + Chair Opus
review) has converged. The path is ratified.

```yaml
ratified_path: CONTINUE_AUTONOMOUS
rationale: |
  Kernel architecture is correct; fidelity gaps are local (seam discipline)
  not structural. The §3.4 LOC analysis (9.3 kLOC native kernel, not
  bloated) kills the rebuild argument. Olya is the binding constraint
  under any path, so implementation-speed advantage of rebuild collapses.
  Meta-irony: fixing plausible-fallback-at-seams by invoking a capability
  whose failure mode is plausible-fallback-at-spec-seams is asymmetric
  against a swiss-watch target.

execution_model: AUTONOMOUS
  briefs_authored_by: CTO
  missions_dispatched_via: factory.ai Opus Mission tool
  parity_gate: at every commit (Phase 3 discipline preserved and distributed)
  review_cadence: Mission-boundary (within 24h of Mission output)

confidence_ratio_at_ratification:
  CONTINUE_AUTONOMOUS: ~70%
  MIDDLE_C_AUTONOMOUS: ~25%
  FRESH_NUCLEUS: ~5%
  note: "Chair and GPT reads strengthened CONTINUE slightly over Opus-Cursor v1.1 ~60/35/5."
```

---

## 2. Phase 4 animating principle

Per GPT lateral synthesis — the single principle that subsumes the
swiss-watch criteria into one test:

```yaml
phase_4_definition: EPISTEMIC_CERTIFICATION
  core_rule: "the system must be incapable of lying"
  operational_statement: |
    At every authority surface, the system either:
      A: produces the methodology-correct answer with explicit confidence
      B: explicitly refuses to evaluate
    It never substitutes plausible state for missing evidence.
  
  three_sub_principles:
    - "system never invents structure"
    - "system never substitutes missing evidence"
    - "system never arms on silently-constructed authority"

  failure_class_being_closed: |
    "The system degrades plausibly instead of failing visibly"
    (GPT's framing — the cleanest articulation of the actual bug class)

  evaluation_test_for_any_work_item: |
    Does this work item reduce the system's ability to invent state
    when methodology is absent? If yes, it's Phase 4 work. If no,
    it's parked or deferred.
```

This principle overrides older swiss-watch phrasings ("stricter, smaller,
less tolerant, more provable") not by replacing them, but by unifying
them. Use this language in briefs and specs.

---

## 3. Three-way advisor synthesis — what sharpens CONTINUE-AUTONOMOUS

```yaml
universally_agreed:
  - CONTINUE-AUTONOMOUS is the correct path
  - Addition 1 (chart-truth anchoring, not byte-identity against pre-SW02 references)
  - Addition 2 (Trade 007 as named swiss-watch exit gate)
  - §3.4 LOC analysis is decisive against rebuild
  - Olya-as-binding-constraint dominates speed considerations
  - Phase 4 is a finishing problem (~10-20% remaining), not a rebuild problem

GPT_additive_builds:
  epistemic_integrity_framing: |
    Replace older "swiss-watch" phrasings in primary docs with the
    epistemic-certification framing above. Single principle, unified test.
  failure_mode_choice: |
    "The decision isn't which architecture is better; it's which failure
    mode you trust more." CONTINUE's failure mode is small, local,
    detectable. That dominates for swiss-watch.
  cto_discipline_dependency: |
    Success of CONTINUE-AUTONOMOUS depends on sustained operator
    discipline. Caveat addressed by G ruling: discipline is operator
    hygiene (clean docs + lateral checks), not CTO cognitive capability.

Chair_Opus_additive_builds:
  mechanism_verification_prerequisite: |
    Execute instrumented cascade to verify Trade 007 mechanism BEFORE
    Mission 1 dispatches. Hours of cost. Prevents Phase 4 being scoped
    against a wrong root cause.
  governance_protocol_prerequisite: |
    Autonomous execution governance doc must land BEFORE Mission 1, not
    alongside. One Mission-gone-sideways before governance is written
    costs more than the governance doc itself.
  ARS_continuity_as_explicit_argument: |
    ARS paper trading on M3 generates Dream Cycle data. Any path that
    pauses or disrupts it compounds operationally. CONTINUE preserves
    it by default; rebuild paths do not.
  sixth_day_one_constraint: |
    SW47 F1 MapConstructionMode scaffold must FIRE, not just be armed.
    If gate can evaluate on silently-fallen-back Map, swiss-watch fails
    regardless of other discipline. Explicit constraint, not detail.
  broader_audit_post_SW49: |
    Opus-Cursor audited 6 of 14 annotated trades. Re-audit all 14 after
    SW49 ships, not just the 4 currently in scope. Prevents side-effect
    regressions on un-audited cases.
  schedule_realism: |
    §4.3 week-by-week plan is defensible but optimistic. Treat as
    4-8 weeks realistic, Olya-session-bound, not 3-5 weeks committed.
```

---

## 4. G rulings on open items (ratified)

```yaml
Q1_CTO_capability_and_discipline:
  reframe: "Not CTO capability — operator hygiene"
  ruling: |
    The success variable is the ENVIRONMENT around CTO, not CTO
    cognitive reliability. Clean, crisp, non-bloated orientation docs
    plus lateral checks and balances during brief/sprint/mission
    processes structurally enforce discipline. Opus 4.7 CTO capability
    is not the variable.
  consolidation_implication: |
    Invest in doc hygiene and review structure, not in "CTO tries
    harder." Phase 4 succeeds or fails on environmental quality.

Q2_Olya_availability:
  ruling: |
    Olya is ABSOLUTELY available. She is not the scheduling constraint.
    The constraint is question quality: ask in human language (not
    system jargon), per her expertise (not system semantics), and
    NEVER on items canon already resolved.
  consolidation_implication: |
    Olya prep pack must be reshaped under canon-first discipline.
    Residual questions must be chart-language, methodology-scoped,
    and pre-filtered against ARS_CANON_v1_3, SYNTHETIC_OLYA_METHOD_vLOCK,
    annotated_trades.yaml, and prior session records.

Q3_heavy_lifting:
  ruling: |
    Push heavy doc lifting to Opus in Cursor (this brief). Stage the
    Phase 4 chapter inside the repo for a fresh CTO and advisors to
    orientate on. Clean house. Clear path. Coherent forward.

Q4_operating_model_shift:
  ruling: RATIFIED
  specifics:
    - CTO authors briefs at Mission cadence (multiple per week during Phase 4)
    - Parity gate is a spec-quality detector under autonomous execution
      (not just a correctness check on Opus output)
    - Concurrent-Mission coherence is a first-class CTO discipline
    - Mission review within 24h; Missions do not merge without review
    - INV-OLYA-ABSOLUTE and INV-SOVEREIGN-1 unchanged under new model
```

---

## 5. Your deliverables

Produce five artifacts as one coherent docs commit. Target: a fresh
CTO or advisor can read them in 30 minutes and be operationally ready.

### 5.1 PHASE_4_RATIFICATION.md

```yaml
purpose: |
  Single canonical record of the ratified path. Captures the advisor
  convergence, the four G rulings, and the operating model shift.
  This is the document that "closes" the decision phase.

required_content:
  - Ratified path (CONTINUE_AUTONOMOUS) with one-paragraph rationale
  - Phase 4 epistemic-certification principle (GPT framing) as the
    animating doctrine
  - Three-way advisor synthesis (compressed — one YAML block)
  - The two non-negotiable additions (chart-truth anchoring,
    Trade 007 exit gate) with invariant names:
      INV-FIDELITY-ANCHORED-TO-CHART-TRUTH
      INV-REGIME-FROM-METHODOLOGY-NOT-FALLBACK
  - Six day-one constraints (Opus-Cursor's five + Chair's F1 scaffold firing)
  - Operating model shift (compressed from §10 of v1.1 pack)
  - Pre-flight items that must close before Mission 1:
      (a) Trade 007 mechanism verification via execution
      (b) Autonomous execution governance doc landed
      (c) CLAUDE.md + FORWARD_PLAN cleaned
      (d) Olya prep pack reshaped
      (e) First Mission brief authored

constraint: ≤400 lines; YAML-dense where YAML clarifies; prose
  only where it adds signal.

not_required:
  - Session-arc narrative ("how we got here")
  - Meta-commentary on CTO process
  - Residue from path evaluations we dismissed
```

### 5.2 FORWARD_PLAN.md (v2.4 or clean replacement)

```yaml
purpose: |
  The current FORWARD_PLAN is ~72KB. That is bloat. Fresh CTO
  orientation needs a clean, sharp forward view. Replace entirely
  with a plan reflecting CONTINUE-AUTONOMOUS.

required_content:
  - Current state (ratified via PHASE_4_RATIFICATION)
  - Phase 4a remaining work (dead-config REMOVE completion + SW48
    fail-closed loader + semantic fidelity gate + Trade 007 root cause
    verification)
  - Olya session scope (residual chart-language questions only)
  - Phase 4b work (P3/SW49 + P5/SW51 + SW27 + SW31 + Shape 2)
  - Phase 4c work (P6/SW52 semantic parity + SW44 tier 1/3)
  - Phase 4d work (SW38-SW43 cartridge schema v2)
  - Exit gates per sub-phase (binary, measurable)
  - Olya-session gating points
  - Mission sequencing (what runs in parallel, what serializes)

constraint: ≤500 lines. If the prior FORWARD_PLAN had content not
  relevant to the ratified forward path, drop it. If something is
  genuinely parked-but-worth-preserving, move it to VAULT.md.

not_required:
  - Detailed historical rationale (lives in SW register + commit history)
  - Session continuity artifacts (handover docs)
  - Speculative Phase 5+ planning
```

### 5.3 CLAUDE.md (audit + reshape)

```yaml
purpose: |
  Current CLAUDE.md is ~142KB. That is bloat. A fresh CTO should be
  able to orientate from CLAUDE.md in <15 minutes. Today, a fresh
  CTO cannot.

action:
  audit_pass: |
    Read current CLAUDE.md top-to-bottom. Classify each section:
      KEEP: constitutional — invariants (§6), findings register (§15),
            architecture overview, doctrine (§11)
      STRIP: session-continuity artifacts, accumulated historical
             rationale, resolved-issue narratives
      MOVE: specific historical records → dedicated archive dir
            (docs/archive/ or equivalent)
      COMPRESS: verbose sections that can say the same thing shorter
  
  reshape_target: ≤50KB; orientation time for fresh CTO <15 min
  
  preserve_at_all_costs:
    - §6 invariants (all 20+ INV-* entries)
    - §15 findings register (all 46+ SW entries with resolution SHAs)
    - §11 doctrine (silent_upgrade_discipline, finding_id_discipline,
      add LIVE_PARITY_ASSERTION_DISCIPLINE per our this-week work,
      add CANON_FIRST_DISCIPLINE per our this-week learning)
    - Architecture overview
  
  can_strip:
    - Sprint-level history (lives in git log)
    - Session continuity narratives
    - Accumulated "as of" dated blocks that no longer reflect current state
    - Deprecated approaches retained for context
    - Advisor-review-specific content (lives in docs/reviews/)

deliverable: CLAUDE.md v0.16 (or equivalent) — leaner, still constitutional
  archive: docs/archive/CLAUDE_md_pre_phase4_consolidation.md (preserved
    at full length for historical record; never live-read)
```

### 5.4 AUTONOMOUS_EXECUTION_GOVERNANCE.md

```yaml
purpose: |
  Prerequisite before Mission 1 dispatches. Chair's correct point:
  one Mission-gone-sideways before governance is written costs more
  than the governance doc itself.

required_content:

  brief_authorship:
    - who: CTO authors all Mission briefs
    - review: G ratifies scope; CTO ratifies implementation detail
    - format: standardized Mission brief template (include)
    - exit_gates: binary, measurable, in every brief

  mission_dispatch:
    - who: G dispatches to factory.ai Opus Mission tool
    - handoff_artifacts: brief + spec inputs + parity contract
    - ambiguity_protocol: Mission halts and escalates on spec ambiguity
      (does NOT make plausible guesses — same failure class we are closing)

  mission_review:
    - reviewer: CTO reviews Mission output within 24h of completion
    - parity_gate_interpretation: |
        Parity failure under autonomous execution is SPEC-QUALITY signal,
        not just Opus-output signal. CTO reads parity failure as "what
        was missing from the brief?"
    - merge_protocol: Missions do not merge to main without CTO review
    - rollback_protocol: revert > patch when output is materially wrong

  concurrent_missions:
    - coherence: CTO explicitly rules which Missions can run concurrently
      and which must serialize
    - conflict_resolution: merge conflicts escalate to CTO; do not auto-resolve
    - parallel_safety: default is serial; parallel requires explicit CTO
      statement that Missions touch non-overlapping surfaces

  escalation:
    - spec_ambiguity: Mission halts, CTO re-scopes brief
    - parity_failure: Mission halts, CTO reviews brief gaps
    - invariant_violation: Mission halts, CTO + G review
    - methodology_question_surfaced: Mission halts, route to Olya via G

  capability_dependency:
    - primary: factory.ai Opus Mission tool
    - fallback: sequential execution (Cursor Opus or Claude Code) if
      autonomous capability degrades
    - cadence_under_fallback: treat v1.0 pack timeline as floor (weeks, not days)

  governance_of_governance:
    - this doc is itself a ratifiable artifact
    - changes require G ratification
    - reviewed at end of Phase 4 for Phase 5+ continuation

constraint: ≤300 lines. Operational, not philosophical.
```

### 5.5 OLYA_PREP_PACK_RESHAPED.md

```yaml
purpose: |
  The original OLYA_PREP_PACK_24_04_26 drifted into asking questions
  canon already answered (caught this morning). Reshape under
  canon-first discipline.

canon_first_discipline_statement: |
  Before any methodology question is drafted for Olya, CTO MUST consult:
    1. ARS_CANON_v1_3.md — if answer is locked in canon, no ruling needed
    2. SYNTHETIC_OLYA_METHOD_vLOCK.yaml — if LOCKED at L1/L15, no ruling
    3. annotated_trades.yaml — if trade is annotated, ruling is in the annotation
    4. prior CTO handovers / ORACLE docs / workshop session records
  Only questions unanswered by all four sources are candidates for Olya.

canon_pass_results_from_this_week:
  Q1_FVG_first_vs_nearest: LOCKED (ARS Canon v1.3 §5 + §14; COO + CTO confirmed)
    → REMOVED FROM PACK
  Q2_displacement_grade_at_L1_L15: LOCKED (vLOCK lines 2253-2254)
    → L1/L15 removed; only cartridge-specific L2 usage remains if applicable
  Q3_trade_003_005_same_date: DIRECTLY ANSWERED in annotated_trades.yaml
    → REMOVED FROM PACK
  Q4_ARS_bypasses_Map: RATIFIED (DEC-ARS-BYPASSES-MAP; COO + CTO confirmed)
    → REMOVED FROM PACK
  Q5_trade_007_regime: CHART-READ CONFIRMED BULLISH (COO independent read +
    detect.py standalone MSS detection; matches Olya annotation)
    → NO METHODOLOGY RULING NEEDED; becomes SW49 code investigation
  Q6_DAILY_EXPANSION_cartridge_status: OPERATIONAL but not Olya-ratified as
    locked cartridge spec (COO confirmed)
    → NOT a session question; cartridge-spec work is separate

residual_olya_questions_for_pack:

  P3_fallback_dispositions:
    scope: "15 fallback sites in map_engine.py need methodology ruling
            per cluster (A-F from evidence pack T1)"
    chart_language_framing: |
      For each fallback cluster, ask in chart-language:
        "When the system has no chart evidence for [X], what should
         a methodology-disciplined strategy do?
           (a) skip the day entirely (no valid setup)
           (b) use [specific cold-start rule Olya defines]
           (c) other — please describe"
    pre_filter_check: |
      For each cluster, verify: is this ALREADY ruled in canon or
      vLOCK? If yes, do not ask Olya.

  P5_day_state_causal_linkage:
    scope: "DAILY_EXPANSION chain sequence — is displacement + MSS
            independence acceptable for delivery, or must they be
            causally linked?"
    chart_language_framing: |
      "When you look at a chart to decide DAILY_EXPANSION has delivered,
       do the displacement and the MSS need to be part of the SAME move,
       or can they be independent events that both happen to occur?"
    note: "DAILY_EXPANSION cartridge is operational but not Olya-ratified
           as locked spec. Treat this ruling as cartridge-spec input,
           not methodology-universal."

  SW27_first_FVG_vs_nearest (for non-ARS cartridges):
    scope: |
      ARS is LOCKED (first-formed, confirmed). Does the same rule apply
      to DAILY_EXPANSION and other future cartridges, or is it cartridge-scoped?
    chart_language_framing: |
      "In DAILY_EXPANSION, when multiple imbalances form after a sweep,
       do you trade the first one, the nearest one, or something else?"
    pre_filter_check: |
      Verify whether this is already implicit in annotated_trades.yaml
      examples (check chain step 3 timing across trades 001, 003, 005,
      006, 007, 013).

  SW31_displacement_grade_consumption:
    scope: |
      L1/L15 calibration is LOCKED. L2 usage (per-cartridge filter vs
      advisory) is open per vLOCK.
    chart_language_framing: |
      "For DAILY_EXPANSION specifically, when you see a weak displacement
       (grade WEAK or below some threshold), do you ignore it, or treat
       it as valid?"

  residual_verifications:
    trade_013_data_range: "quick confirmation only; <5 min"
    F2_2_Shape_2_ARS_Map_convergence: |
      Chair + GPT confirmed DEC-ARS-BYPASSES-MAP ratifies independence.
      CTO recommends: drop from session. If G wants explicit ratification
      from Olya, keep as 2-min confirmation ("confirm ARS and DAILY_EXPANSION
      can disagree on same date without it being a bug").

session_time_estimate: 30-60 min F2F (down from 90-120 min in original pack)

format_for_pack:
  - one question per primary item
  - chart-language, not system-jargon
  - 2-3 options where applicable, binary where possible
  - counter-example trade per option where available
  - CTO suspicion flagged (may diverge from Olya ruling — that's the signal)

constraint: ≤300 lines. Focused. Minimal canon-resolvable items.
```

---

## 6. Discipline constraints (doc hygiene ethos)

```yaml
principle: "a fresh CTO orientates in 30 minutes or the docs are broken"

tests_to_apply_per_doc:
  - If this paragraph doesn't earn its place, cut it
  - If this section explains "how we got here," it belongs in git log or archive
  - If this section is session-continuity residue, it belongs in archive
  - If this section restates something in another doc, pick one home
  - If this section is aspirational or speculative, move to VAULT or cut

format_preferences:
  - YAML-dense where YAML clarifies (structure, options, enumerations)
  - prose where prose adds signal (rationale, doctrine, nuance)
  - no mixed "YAML inside prose inside YAML" nesting
  - no emoji, no decorative separators beyond --- between major sections
  - tables only when they clarify comparison (rare)

preserve_at_all_costs:
  - invariants (INV-* register)
  - findings register (SW* entries with resolution SHAs)
  - doctrine statements (§11 equivalent)
  - canonical methodology references (ARS_CANON, vLOCK, annotated_trades, PRIMER)

strip_without_hesitation:
  - dated "status as of" blocks that are stale
  - session narrative ("in session X we did Y")
  - advisor review commentary (lives in docs/reviews/)
  - explanatory meta-commentary
  - sprint-level historical detail (git log is the record)
```

---

## 7. Execution sequence

```yaml
step_1_audit:
  read_current_state_of:
    - CLAUDE.md (full)
    - FORWARD_PLAN.md (full)
    - OLYA_PREP_PACK_24_04_26.md (full)
    - FIDELITY_AUDIT_AND_PATH_RECOMMENDATION (v1.1 full)
    - advisor reads shared in this session (Chair Opus + GPT synthesis)
  classify_every_section: KEEP / STRIP / MOVE / COMPRESS
  time_budget: ~1-2 hours

step_2_draft_ratification:
  produce: PHASE_4_RATIFICATION.md
  time_budget: ~1 hour

step_3_reshape_FORWARD_PLAN:
  produce: FORWARD_PLAN.md v2.4 (clean)
  archive_prior: docs/archive/FORWARD_PLAN_v2_3.md
  time_budget: ~1-2 hours

step_4_reshape_CLAUDE_md:
  produce: CLAUDE.md v0.16 (leaner)
  archive_prior: docs/archive/CLAUDE_md_v0_15.md
  time_budget: ~2-3 hours (largest single lift)

step_5_draft_governance:
  produce: AUTONOMOUS_EXECUTION_GOVERNANCE.md
  time_budget: ~1 hour

step_6_reshape_olya_prep:
  produce: OLYA_PREP_PACK_RESHAPED.md
  archive_prior: docs/archive/OLYA_PREP_PACK_24_04_26.md
  time_budget: ~1 hour

step_7_commit:
  atomic: ALL deliverables ship as one docs commit
  rationale: they reference each other; fresh CTO reads them as a set
  commit_body: "docs: Phase 4 consolidation — ratification + clean house
                + autonomous execution governance + olya prep reshape"

total_estimated_time: 7-10 hours; do not rush

delivery_format:
  - single docs commit on main (no code changes)
  - present files via present_files for G review
  - G may request tightening; revise before merge if so
```

---

## 8. Standing instructions

```yaml
escalate_to_CTO_if:
  - any doc section you would write contains content that contradicts
    ratified invariants
  - you find yourself preserving content because "it might be useful"
    (this is the bloat trap — ask CTO)
  - you uncover evidence that any ratified decision in §1-4 needs
    revisiting (halt, report, do not paper over)
  - you encounter a methodology ambiguity that requires Olya ruling
    (do not guess; park in reshaped OLYA_PREP_PACK_RESHAPED.md)
  - CLAUDE.md audit surfaces a finding register item that appears
    closed-but-still-live (halt, flag, do not silently preserve)

do_not:
  - change any code in en1gma/
  - ship multiple commits (atomic docs commit only)
  - preserve session narrative for "completeness"
  - invent new invariants or findings (ratified set only)
  - author the first Phase 4 Mission brief (CTO's job post-consolidation)
  - reshape anything in VAULT.md (out of scope)

do:
  - cut aggressively
  - compress verbose to YAML where it clarifies
  - move historical detail to docs/archive/
  - preserve invariants + findings + doctrine at full fidelity
  - ask questions if scope unclear
  - flag surfaced issues rather than silently absorbing

close_with:
  - present_files: all 5 new docs
  - brief DENSE YAML summary of what landed
  - any residual items or recommendations for CTO
  - standing for next dispatch (Mission 1 brief authorship by CTO)
```

---

*End of consolidation brief. Execute read-only audit + docs consolidation
per §5 deliverables. Ship as atomic commit. CTO reviews, G ratifies,
Phase 4 execution begins.*
