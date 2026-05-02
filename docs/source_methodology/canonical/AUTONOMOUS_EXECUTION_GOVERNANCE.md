# AUTONOMOUS EXECUTION GOVERNANCE

```yaml
document: AUTONOMOUS_EXECUTION_GOVERNANCE
version: 1.0 (pending G ratification; Phase 4a prerequisite 2)
date: 2026-04-24
authored_by: CTO (Claude) + Opus (Cursor) — consolidation
purpose: |
  Operational protocol governing Mission-based autonomous execution
  under CONTINUE_AUTONOMOUS (Phase 4+). Authored BEFORE Mission 1
  dispatches per Chair Opus prerequisite requirement: "one Mission-
  gone-sideways before governance is written costs more than the
  governance doc itself."
scope: Phase 4 execution; reviewed at Phase 4 close for Phase 5+ continuation
rule: "Operational, not philosophical. Every rule here is a check or a deliverable."
ratification: "Pending G. Not live until G ratifies."
```

---

## 1. Scope and framing

```yaml
applies_to: |
  Every Phase 4 implementation Mission (SW48/49/50/51/52 Missions;
  SW44 tier-1 / tier-3 Missions; SW38-SW43 cluster Missions in
  Phase 4d; any other Mission authored under PHASE_4_SCOPE_RULE).

does_not_apply_to:
  - Doc-only changes authored by CTO or Opus directly (like this commit)
  - ARS live paper trading operations (unchanged operational model)
  - Olya methodology sessions (INV-OLYA-ABSOLUTE unchanged)
  - Emergency halt / rollback (halt overrides everything)

authority_preserved:
  INV-OLYA-ABSOLUTE:           "methodology rulings route to Olya regardless of execution model"
  INV-SOVEREIGN-1:             "G's capital authority orthogonal to execution model"
  INV-HALT-OVERRIDES-ALL:      "halt wins; autonomous Missions do not override"
  INV-STRUCTURAL-REFACTOR-NO-SEMANTIC-DRIFT: "every Mission commit preserves parity gates"
```

---

## 2. Brief authorship (CTO owns)

```yaml
authorship:
  who: CTO (Claude) authors every Mission brief
  review: G ratifies scope at a natural boundary (typically post-Olya-session brief batching); CTO ratifies implementation detail
  cadence_expectation: 3-5 briefs per week during Phase 4
  binding_constraint: CTO brief-authorship throughput (not Opus execution hours)

brief_template:
  required_sections:
    - mission_id: "e.g., PHASE_4B.M2.SW48_FAIL_CLOSED_LOADER"
    - scope: "console | cartridge | example_only" (per CARTRIDGE_CONTRACT §7)
    - effect: "methodology | evaluation | configuration | structure | workflow"
    - phase_4_scope_rule_check: "reduction of ambiguity OR enforcement of truth (allowlist item per PHASE_4_RATIFICATION §5). No new capability."
    - invariants_affected: "list of INV-* registered/enforced/extended"
    - preserved_parity_gates: "151/151 ARS, 14/14 semantic chart-truth, lint-imports 6 KEPT, mypy strict 0 errors"
    - acceptance_criteria_semantic: "chart-truth assertions passing from annotated_trades.yaml::expected_state"
    - acceptance_criteria_byte_identity: "tracked chart-truth/integration suite preserved; legacy SW54 byte-identity harness is superseded unless explicitly reintroduced with SW48-compatible strategy_params/chain_config wiring"
    - acceptance_criteria_mechanical: "tests pass; lint clean; mypy clean; no new SW IDs introduced except at Mission landing per §11"
    - exit_gate: "binary, measurable, quotable in commit body"
    - size_estimate: "LOC production + LOC tests; rough order"
    - concurrent_safety: "serial-only OR can-run-concurrent-with [list of Missions] because surfaces do not overlap"
    - rollback_criterion: "what constitutes 'abort this Mission' signal during execution"
  non_negotiable:
    - every brief CITES its Phase 4 invariant(s) from PHASE_4_RATIFICATION §4
    - every brief includes explicit semantic acceptance criteria (not only byte-identity)
    - every brief declares both scope AND effect
    - every brief confirms PHASE_4_SCOPE_RULE allowlist compliance
```

---

## 3. Mission dispatch

```yaml
dispatch:
  who: G dispatches to factory.ai Opus Mission tool
  handoff_artifacts:
    - brief (dense YAML per §2 template)
    - PHASE_4_RATIFICATION.md (spec input — invariants + constraints)
    - CLAUDE.md (spec input — §6 invariants + §11 discipline)
    - CARTRIDGE_CONTRACT.md (spec input — classification authority)
    - cartridge YAML files as needed for the specific Mission
    - current HEAD SHA (clean starting state)
  not_handed_off:
    - advisor pack historical reasoning (not needed for execution)
    - docs/archive/ (not needed for execution)
    - prior SW register narratives (only open items + the specific closed SWs the brief references)

ambiguity_protocol:
  rule: |
    Mission HALTS on brief ambiguity. Does NOT make plausible guesses.
    This is the same failure class — silent plausible state in absence
    of authority — that Phase 4 exists to close. Autonomous execution
    under that failure mode is the meta-irony CONTINUE_AUTONOMOUS is
    avoiding. Escalate; do not improvise.
  halt_triggers:
    - brief underspecifies an invariant enforcement point
    - brief does not cover an edge case the Mission finds in code
    - brief's methodology reference is not resolvable in canon
    - brief conflicts with another ratified invariant or doctrine
    - test or parity gate fails and root cause is not covered by brief
  escalation_route: "Mission halts → CTO reviews → brief re-scoped → re-dispatch"
  escalation_not_allowed:
    - silently continuing with a plausible interpretation
    - proposing methodology rulings in-Mission (route to Olya)
    - altering brief scope to match what Mission encountered
```

---

## 4. Mission review (CTO owns)

```yaml
review:
  reviewer: CTO (Claude)
  cadence: within 24h of Mission output (mandatory, GPT addendum A9)
  review_surface:
    - all commits produced by Mission
    - parity gate output (151/151 ARS + semantic chart-truth + lint + mypy)
    - test additions / modifications
    - any new INV registrations at §6
    - any new SW registrations at §15
    - any §11 doctrine additions

parity_gate_interpretation:
  rule: |
    Parity failure under autonomous execution is SPEC-QUALITY signal,
    not just Opus-output signal. Read parity failure as: "what was
    missing from the brief?" Iterate brief first; do not patch code
    to green the test without root-cause attribution.
  anti_pattern: "ad-hoc code patching to green a parity test"
  correct_pattern: "parity failure → brief gap identified → brief refined → Mission re-dispatches with corrected spec"
  reference: "CLAUDE.md §11 live_parity_assertion_discipline"

merge_protocol:
  rule: "Missions do not merge to main without explicit CTO approval"
  approval_criteria:
    - all parity gates green
    - semantic acceptance criteria met (not only byte-identity)
    - no unexpected behavioral changes beyond brief scope
    - INV registrations present if brief called for them
    - SW registrations present if brief introduced new findings
    - commit message cites: brief ID, invariants registered, exit gate met
  lint_imports_and_mypy: "must be 6 KEPT / 0 broken + 0 mypy errors at merge"

rollback_protocol:
  when_to_rollback:
    - output is materially wrong (wrong direction, wrong authority surface, wrong semantics)
    - Mission "finished green" but manual inspection reveals scope creep or undeclared capability addition
    - Mission introduces a plausible-state substitution anywhere (violation of INV-EPISTEMIC-INTEGRITY family)
  how_to_rollback: "git revert, not manual patch. Re-author brief. Re-dispatch Mission."
  why_revert_not_patch: |
    Patching post-hoc produces a commit history that silently encodes
    the fix discipline inside a repair commit. Revert-and-re-dispatch
    keeps the Mission as a first-class unit of audit.
```

---

## 5. Concurrent Missions

```yaml
default: SERIAL
reason: |
  Most Phase 4 Missions touch authority surfaces (gate.py, map_engine.py,
  day_state.py). Concurrent work on overlapping surfaces risks merge
  conflicts that hide semantic issues. Default serial; parallel
  requires affirmative CTO ruling.

parallel_safety_rule:
  requirement: |
    CTO MUST issue an explicit "non-overlap statement" before any two
    Missions run concurrently. Statement identifies the non-overlapping
    files / modules / invariants each Mission touches.
  template: |
    CONCURRENT_MISSIONS: [M_a, M_b]
    NON_OVERLAP_STATEMENT:
      M_a touches: [file_a1, file_a2, INV-X enforcement]
      M_b touches: [file_b1, file_b2, INV-Y enforcement]
      no_shared_authority_surfaces: TRUE
      merge_order: [M_a first, M_b second] OR [either order safe]
      conflict_protocol: CTO reviews; no auto-resolve

examples_naturally_parallel:
  - SW44 tier-1 (tests-only annotations) || any other Phase 4 Mission
  - SW52 semantic detection parity (test-only) || SW49 (code)
  
examples_must_serialize:
  - SW48 (map_orchestrator) and SW49 (map_engine) — adjacent call sites
  - SW49 and SW51 (map_engine and day_state) — INV-MAP-CONSTRUCTION-MODE-EXPLICIT propagation affects both
  - SW38-SW43 cluster Missions (schema v2) — serialize entire cluster; concurrent with no other Mission

conflict_resolution:
  rule: "merge conflicts ESCALATE to CTO; no auto-resolve"
  why: "a merge conflict in Phase 4 is either (a) brief overlap missed in non-overlap statement, or (b) concurrent edits touched the same seam — both require CTO rule, not git magic"
```

---

## 6. Escalation

```yaml
spec_ambiguity:
  who: Mission halts → CTO re-scopes → re-dispatch

parity_failure_root_cause_not_covered_by_brief:
  who: Mission halts → CTO reviews → brief refined → re-dispatch
  never: patch the code; never patch the reference

invariant_violation_detected:
  who: Mission halts → CTO + G review → ratified decision to proceed / revise / rollback
  when: any INV-* in CLAUDE.md §6 would be violated by the Mission output

methodology_question_surfaced:
  who: Mission halts → CTO routes to Olya via G → ruling captured → brief refined → re-dispatch
  never: invent methodology in-Mission

scope_creep_detected:
  who: Mission halts → CTO + G review — did brief overscope? does PHASE_4_SCOPE_RULE permit?
  default: revert + re-author brief with scope tightened

closed_SW_appears_to_re_emerge:
  who: HALT, flag, do not silently preserve (per CLAUDE.md §11 finding_id_discipline and PHASE_4_CONSOLIDATION_BRIEF §8 escalate conditions)
  action: CTO + G review; either (a) reopen SW with new evidence and resolution, or (b) confirm false positive with rationale
```

---

## 7. Capability dependency

```yaml
primary_capability: factory.ai Opus Mission tool
primary_failure_modes_to_plan_for:
  - API outage / rate limiting
  - Mission timeout (long-running brief doesn't converge)
  - Mission output quality degradation
  - factory.ai product changes that affect brief handoff format

fallback:
  option_a: Cursor Opus (current environment — CTO-in-the-loop sequential)
  option_b: Claude Code (CLI-driven sequential)
  cadence_under_fallback: |
    Treat advisor-pack v1.0 timeline as floor (3 months elapsed).
    CONTINUE path remains valid; execution model degrades to SEQUENTIAL
    which is Phase-3-shape. Not a crisis.
  graceful_degradation_commitment: |
    No Mission work becomes un-doable under fallback. Autonomous is
    speed, not capability. INV-* enforcement, parity gates, CTO brief
    discipline all work in sequential mode.

post_phase_4_decision:
  question: "Does autonomous execution become Phase 5+ default, or is Phase 4 a one-shot use?"
  ratification_moment: "Phase 4 close review"
  not_decided_now: "Explicitly deferred per PHASE_4_RATIFICATION §10.4"
```

---

## 8. Governance of this governance

```yaml
this_document:
  status: ratifiable artifact
  changes_require: G ratification + CTO proposal
  review_trigger: Phase 4 close (mandatory) or Mission-gone-sideways (ad-hoc)

precedence:
  higher_than: individual Mission briefs (this doc overrides)
  lower_than: CARTRIDGE_CONTRACT (invariants + classification authority) + PHASE_4_RATIFICATION (path + doctrine)
  orthogonal_to: methodology doctrine (vLOCK, annotated_trades, ARS_CANON)

amendment_protocol:
  propose: CTO authors delta brief
  review: G (ratification) + Fresh Chair Opus (challenge) + Opus-Cursor (detail)
  land: atomic docs commit updating this doc + reference pointers
```

---

## 9. Phase 4 start checklist (before Mission 1)

All four must be YES before the first implementation Mission dispatches:

```yaml
Q1_ratified: "G has ratified PHASE_4_RATIFICATION.md?"
Q2_governance_ratified: "G has ratified this document?"
Q3_prerequisite_1: "Trade 007 mechanism verified via instrumented cascade?"
Q4_prerequisite_3: "Chart-truth semantic gate landed in tracked chart-truth/integration suite? Legacy SW54 byte-identity harness is superseded unless explicitly reintroduced with SW48-compatible wiring."
Q5_prerequisite_4: "Olya session complete; OLYA_SESSION_RULINGS artifact landed?"
Q6_first_brief_authored: "PHASE_4B.M1.SW49 brief authored against Olya rulings?"
Q7_concurrent_policy: "Serial-by-default or explicit non-overlap statement in place?"

if_any_NO: do not dispatch Mission 1; close the gap first
if_all_YES: dispatch Mission 1; Phase 4b execution begins
```

---

## 10. One-line summary

```
CTO authors briefs. Opus Missions execute. Parity gate at every commit.
Review within 24h. Serial by default. Halt on ambiguity. Revert on wrong.
No methodology invention in-Mission. Olya rules methodology. G rules capital.
```

---

*Ratifiable artifact. Pending G ratification before first Mission dispatches. No code change authorized under this document until ratification.*
