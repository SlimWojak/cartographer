# CANON UPDATE PATCHES — POST-SW51b CLOSEOUT (2026-04-25)

```yaml
purpose: surgical updates to FORWARD_PLAN.md and CLAUDE.md following SW51b ratification (cb8e4e9)
applies_after: G ratifies SW51B_RATIFICATION_2026_04_25.md
patches: 6 inline replacements + 1 new SW51b entry + 2 invariant updates
estimated_apply_time: ~10 min hand-edit
precedent: SW51a closeout pattern (5c1d647 was canon-only commit on main, separate from feature-branch code)
```

---

## PATCH 1 — FORWARD_PLAN.md §1 baseline (current state)

REPLACE:
```yaml
phase_4b_progress:
  closed: [SW48, SW49_narrow, SW56, SW57, SW51a]
  parked: [SW44_tier_1]
  deferred: [SW52]
  in_authoring: [SW51b]
  queued: [SW27, SW31, SW58, SW50]
  last_close_sha: c3b716a (SW51a, 2026-04-25)
```

WITH:
```yaml
phase_4b_progress:
  closed: [SW48, SW49_narrow, SW56, SW57, SW51a, SW51b]
  parked: [SW44_tier_1]
  deferred: [SW52]
  in_authoring: []
  queued: [SW27, SW31, SW58, SW50]
  last_close_sha: cb8e4e9 (SW51b, 2026-04-25; feature/sw51b-active-move-classifier)
  cluster_status: SW51_cluster_COMPLETE — SW51a + SW51b both closed; 010+011 SW58 territory by design
```

ALSO update tests count line:
```yaml
tests: 863 passing + 4 xfailed (SW51a +14 tests / -4 from prior count reconciliation; verify exact at next test run)
```
becomes:
```yaml
tests: 897 + 47 SW51b + 4 xfailed (verify exact at next full test run; sentinel weekend pre-existing failure documented in SW51b §4 note 2)
```

ALSO update the chart_truth line in §1:
```yaml
daily_expansion: 6/6 fingerprint parity; chart-truth semantic coverage expanded to 12 state_gated fixtures (6 PASS / 6 RED diagnostic)
```
becomes:
```yaml
daily_expansion: 6/6 fingerprint parity; chart-truth 12 state_gated fixtures: 10 PASS / 2 RED (010, 011 — SW58 fallback territory by design)
```

---

## PATCH 2 — FORWARD_PLAN.md §4 — SW51b entry replacement

REPLACE the entire `4b_mission_5b_SW51b_active_move_and_retrace_classifier:` block (currently in AUTHORING status from SW51a closeout PATCH 2) WITH:

```yaml
4b_mission_5b_SW51b_active_move_and_retrace_classifier:
  status: CLOSED 2026-04-25 (sha cb8e4e9)
  ratification_record: docs/reviews/SW51B_RATIFICATION_2026_04_25.md
  brief: docs/briefs/draft/SW51B_BRIEF_v0_4_2026_04_25.md (promote to docs/briefs/shipped/2026-04/ on canon commit)
  outcome:
    chart_truth_12: 10 PASS / 2 RED (010, 011 — SW58 territory by design)
    RED_flips_landed: trade_002, 008, 012, 014 (4 of 4 target)
    PASS_preserved: 6 of 6
    trade_014_mechanism_verified: 4H BEARISH at 1.189475 INSIDE Daily ActiveMove invalidation 1.15788 → RETRACE classification
    ARS_parity: 151/151 byte-identical / 0 divergences
    LOC_landed: ~564 source / ~331 tests across 11 files
  invariants_promoted:
    - INV-STRUCTURE-BOUNDARY-EVIDENCE-OR-UNAVAILABLE: scaffold-armed → ACTIVE (consumer enforcement live)
    - INV-RETRACE-BOUNDED-BY-STRUCTURE: NEW; ACTIVE (production RETRACE emission bounded to structure-aware path)
  implementation_shape:
    classifier_owner: MapEngine.classify_structural_event
    atomic_transition: MapEngine._commit_regime_boundary_transition
    state_mutator: RegimeTracker (unchanged ownership; permission derivation updated for RETRACE with-move)
    update_on_mss_signature: PRESERVED
    gate_py: UNTOUCHED
    phase_source: trace-only metadata via MapEngine._last_phase_source

4b_mission_5_overall_status: COMPLETE (SW51a + SW51b both CLOSED; SW51 cluster done)
```

---

## PATCH 3 — FORWARD_PLAN.md §4 — SW27 dependency update

REPLACE in `4b_mission_6_SW27_first_FVG_for_non_ars_cartridges:` block:

```yaml
  dependency: SW51b must land first (SW51a CLOSED provides MoveStructureBoundary + DIRECT_ID_LINK; SW51b consumer enforcement)
  outstanding_observation_from_SW51a: |
    SW51a §4 discipline note 2 — displacement match rule slightly
    broader than strict 1:1 PATCH_2 spec. Empirically clean at 119/119
    in SW51a, but SW27 brief authoring should re-check rule against
    Olya Q3 STRICT 1:1 mapping. If multi-match cases surface, narrow
    PATCH Mission may be required pre-SW27.
```

WITH:

```yaml
  dependency: SATISFIED — SW51a + SW51b both CLOSED; MoveStructureBoundary ACTIVE; DIRECT_ID_LINK in place (119/119)
  status: ELIGIBLE_FOR_AUTHORING (next cycle)
  expected_complexity: lower than feared (Olya Q3 STRICT 1:1 sharp; SW51a primitive available; SW51b ActiveMove not strictly required for SW27 but cleaner with it)
  outstanding_observation_from_SW51a: |
    SW51a §4 discipline note 2 — displacement match rule slightly
    broader than strict 1:1 PATCH_2 spec. Empirically clean at 119/119
    in SW51a, but SW27 brief authoring should re-check rule against
    Olya Q3 STRICT 1:1 mapping. If multi-match cases surface, narrow
    PATCH Mission may be required pre-SW27.
  per_commit_smoke_required: MANDATORY (binding rule from SW51a + SW51b §4 note 1)
```

---

## PATCH 4 — FORWARD_PLAN.md §4 — SW58 entry update (dependencies satisfied)

REPLACE in `4b_mission_9_SW58_fallback_regime_and_cascade_authority:` block:

```yaml
  dependencies: SW51b GREEN; audit findings (SW51 audit + SW51a discipline notes) already in hand
  classification: Category 2 single Mission (scope discoverable post-SW51b; may split if cascade authority deserves own seam)
  not_blocking: SW51b critical path; SW27 + SW31 also independent
  size_estimate: TBD at brief authoring (post-SW51b)
```

WITH:

```yaml
  dependencies: SATISFIED — SW51a + SW51b both CLOSED; clean substrate for fallback regime work
  classification: Category 2 single Mission (may split into SW58a fallback guard + SW58b cascade authority — discoverable at brief authoring)
  status: ELIGIBLE (queued; not next-cycle priority — SW27/SW31 typically smaller and forward queue prioritization is G call)
  size_estimate: TBD at brief authoring
  per_commit_smoke_required: MANDATORY
```

---

## PATCH 5 — FORWARD_PLAN.md §4 — SW31 status update

REPLACE in `4b_mission_7_SW31_L2_displacement_grade:` block, the status note:

```yaml
  ratified_invariants_on_commit:
    - INV-CARTRIDGE-ABSENCE-IMPLIES-NO-TRADE
```

WITH (add per_commit_smoke + status):

```yaml
  ratified_invariants_on_commit:
    - INV-CARTRIDGE-ABSENCE-IMPLIES-NO-TRADE
  status: ELIGIBLE (independent of SW51 cluster; can author parallel to SW27 if G prefers)
  per_commit_smoke_required: MANDATORY
```

---

## PATCH 6 — CLAUDE.md status block update

REPLACE:
```yaml
  phase_4b_status: |
    SW48, SW49_narrow, SW56, SW57, SW51a CLOSED.
    SW44 tier-1 PARKED. SW52 DEFERRED. SW51b in authoring.
    SW27, SW31, SW58, SW50 queued.
  last_canon_sha_origin: c3b716a (SW51a, 2026-04-25)
  identity_link_status: DIRECT_ID_LINK (post-SW51a; 119/119 MSS Detections)
  boundary_surface: MoveStructureBoundary at MapState; OK | UNAVAILABLE construction_mode
```

WITH:
```yaml
  phase_4b_status: |
    SW48, SW49_narrow, SW56, SW57, SW51a, SW51b CLOSED.
    SW51 cluster COMPLETE.
    SW44 tier-1 PARKED. SW52 DEFERRED.
    SW27, SW31, SW58, SW50 queued (all dependencies satisfied; eligible to author).
  last_canon_sha_origin: cb8e4e9 (SW51b, 2026-04-25; feature/sw51b-active-move-classifier; canon push pending)
  identity_link_status: DIRECT_ID_LINK (post-SW51a; 119/119 MSS Detections — preserved)
  boundary_surface: MoveStructureBoundary at MapState; OK | UNAVAILABLE construction_mode; ACTIVE | ENDED status (post-SW51b)
  retrace_emission_status: PRODUCTION ACTIVE via MapEngine.classify_structural_event → structure-aware path (post-SW51b)
  chart_truth_12_status: 10 PASS / 2 RED (010, 011 — SW58 territory by design)
```

ALSO REPLACE:
```yaml
  finding_register_highwater: SW58 registered (2026-04-25 post-SW51a); SW51a CLOSED at c3b716a; SW51b in authoring; SW27/SW31/SW50 queued
```

WITH:
```yaml
  finding_register_highwater: |
    SW51a CLOSED at c3b716a; SW51b CLOSED at cb8e4e9; SW51 cluster complete.
    SW27 / SW31 / SW58 / SW50 queued (all eligible).
    Discipline binding rule: per-commit FULL 12-fixture chart-truth + ARS + mypy + lint smoke MANDATORY for all multi-commit Phase 4b Missions forward.
```

---

## PATCH 7 — CLAUDE.md §6 invariants — promote scaffold-armed + add new

LOCATE the invariants section. UPDATE entry for INV-STRUCTURE-BOUNDARY-EVIDENCE-OR-UNAVAILABLE:

REPLACE:
```yaml
INV-STRUCTURE-BOUNDARY-EVIDENCE-OR-UNAVAILABLE:
  parent: INV-EPISTEMIC-INTEGRITY
  sibling: INV-MAP-CONSTRUCTION-MODE-EXPLICIT
  state: scaffold-armed (SW51a c3b716a; will activate at SW51b consumer enforcement)
  text: |
    A MoveStructureBoundary may be OK only when constructed from an
    MSS-emitted protected swing plus direct confirming displacement
    identity. If evidence is missing, boundary is UNAVAILABLE.
    DealingRange or any adjacent spatial surface must never be
    substituted as boundary evidence.
  precedent_pattern: SW49 INV-GATE-REFUSES-FALLBACK-MAP scaffold-armed → active
```

WITH:
```yaml
INV-STRUCTURE-BOUNDARY-EVIDENCE-OR-UNAVAILABLE:
  parent: INV-EPISTEMIC-INTEGRITY
  sibling: INV-MAP-CONSTRUCTION-MODE-EXPLICIT
  state: ACTIVE (promoted scaffold-armed → ACTIVE on SW51b cb8e4e9, 2026-04-25)
  text: |
    A MoveStructureBoundary may be OK only when constructed from an
    MSS-emitted protected swing plus direct confirming displacement
    identity. If evidence is missing, boundary is UNAVAILABLE.
    DealingRange or any adjacent spatial surface must never be
    substituted as boundary evidence.
  consumer_enforcement: MapEngine.classify_structural_event refuses construction_mode=UNAVAILABLE OR status=ENDED boundaries
  precedent_pattern: SW49 INV-GATE-REFUSES-FALLBACK-MAP scaffold-armed → active (same pattern repeated cleanly)
```

ADD new invariant entry (under INV-EPISTEMIC-INTEGRITY family):

```yaml
INV-RETRACE-BOUNDED-BY-STRUCTURE:
  parent: INV-EPISTEMIC-INTEGRITY
  sibling: INV-STRUCTURE-BOUNDARY-EVIDENCE-OR-UNAVAILABLE
  state: ACTIVE (registered at SW51b cb8e4e9, 2026-04-25)
  text: |
    Regime.phase = RETRACE may be emitted only from an OK, ACTIVE
    MoveStructureBoundary when an opposite-direction structural event
    is observed inside that boundary. RETRACE must not be emitted from
    UNAVAILABLE boundary evidence, DealingRange substitution, fallback
    regime stamping, or test-only phase mutation.
  consumer_enforcement: production RETRACE emission path is structure-aware classifier only; LEGACY_UNAVAILABLE_BOUNDARY_DISP_DERIVED path explicitly does not emit RETRACE
```

---

## APPLICATION ORDER

```yaml
1: open FORWARD_PLAN.md
2: apply PATCH 1 (§1 baseline + tests count + chart_truth line)
3: apply PATCH 2 (§4 SW51b CLOSED; cluster COMPLETE)
4: apply PATCH 3 (§4 SW27 dependencies satisfied)
5: apply PATCH 4 (§4 SW58 dependencies satisfied)
6: apply PATCH 5 (§4 SW31 per-commit smoke binding)
7: open CLAUDE.md
8: apply PATCH 6 (status block + finding register)
9: apply PATCH 7 (invariant promotion + new INV-RETRACE-BOUNDED-BY-STRUCTURE)
10: copy SW51B_RATIFICATION_2026_04_25.md into docs/reviews/ from outputs
11: optional: promote brief from docs/briefs/draft/SW51B_BRIEF_v0_4_2026_04_25.md → docs/briefs/shipped/2026-04/ (move + commit; NOT required for canon push but cleaner)
12: verify with `git diff` — should be docs-only changes (no code, no tests)
13: commit on main: "docs(canon): SW51b CLOSED — SW51 cluster complete; INV-STRUCTURE-BOUNDARY ACTIVE; INV-RETRACE-BOUNDED-BY-STRUCTURE registered"
14: push origin/main
```

---

## CTO_VERIFICATION_AFTER_PUSH

```yaml
git log origin/main --oneline -3
# expect:
#   <new_sha> docs(canon): SW51b CLOSED — SW51 cluster complete; ...
#   5c1d647 docs(canon): SW51a CLOSED — FORWARD_PLAN + CLAUDE.md + INV-STRUCTURE-BOUNDARY scaffold-armed + SW58 registered
#   8f2ba99 Relocate SW51 synthesis note to docs/briefs/draft

git status
# expect: nothing to commit, working tree clean (on main)
# (untracked: handover doc + SW54 parity test — pre-existing, deliberate)

git branch -v
# expect:
#   * main                              <new_sha> docs(canon): SW51b CLOSED ...
#     feature/sw51a-structure-boundary  ~49b5c3e docs(brief): SW51b fresh agent handoff note
#     feature/sw51b-active-move-classifier  cb8e4e9 Add SW51b active move retrace classifier
```

---

*Surgical patches only. Same precedent as SW51a closeout (5c1d647). Apply in order; verify diff is doc-only; commit + push to main; feature branches preserved as audit trail.*
