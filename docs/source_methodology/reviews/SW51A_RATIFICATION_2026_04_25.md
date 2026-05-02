# SW51a RATIFICATION — 2026-04-25

```yaml
document: SW51A_RATIFICATION_2026_04_25
classification: ratification + closeout record
mission_id: SW51a
mission_name: STRUCTURE_BOUNDARY_AND_EVENT_IDENTITY_SURFACE
verdict: GREEN
authoring_CTO: Opus 4.7
ratifying_authority: G
date: 2026-04-25
branch: feature/sw51a-structure-boundary
branch_head_sha: c3b716a
implementation_commits:
  - 3bb5732 — Add MSS structure identity surface
  - c3b716a — Add move structure boundary surface
brief_authority: docs/briefs/shipped/2026-04/SW51A_BRIEF_2026_04_25.md (v0.2 final, post-GPT-lateral)
upstream_audit: docs/reviews/SW51_PRE_IMPLEMENTATION_AUDIT_2026_04_25.md (b5170ad)
upstream_rulings: docs/reviews/OLYA_SESSION_RULINGS_2026_04_25.md
g_ratifications_consumed: E1 + E2 + E3 + E4 + cautions C1-C5 + GPT additive patches C1-C6
```

---

## §1 — Mission outcome

```yaml
empirical_target_at_authoring: zero behavior change; primitive surface emitted
empirical_outcome: matched exactly

structural_health:
  identity_link: 119/119 MSS Detections with upstream_refs populated (DIRECT_ID_LINK target reached from prior TIME_AND_TF_JOIN_ONLY)
  boundary_distribution: OK=10 / UNAVAILABLE=2 / NONE=0 (correctly bimodal on construction evidence)
  test_baseline: 849 passed + 4 xfailed (preserved from pre-SW51a baseline) + 14 new SW51a tests
  ARS_parity: 151/151 byte-identical / 0 divergences
  mypy_strict: 0 errors / 183 source files
  lint_imports: 6 KEPT / 0 broken
  detection_parity: 11 passed
```

---

## §2 — Verification asks (4) — all resolved

```yaml
ASK_1_chart_truth_explicit_matrix:
  status: PASS
  PASS_set_confirmed: {trade_001, trade_003, trade_005, trade_006, trade_007, trade_013}
  RED_set_confirmed: {trade_002, trade_008, trade_010, trade_011, trade_012, trade_014}
  semantic_fields_unchanged_vs_baseline_8f2ba99: confirmed via detached worktree comparison
  comparison_method: semantic-output (not byte-trace parity)

ASK_2_UNAVAILABLE_case_identification:
  status: PASS
  cases:
    trade_010:
      date: 2025-11-12
      source_regime_event: disp_derived_displacement_1D_2025-10-13T00:00:00_bull
      confirming_mss_id: None
      fallback_path: YES
    trade_011:
      date: 2025-11-28
      source_regime_event: disp_derived_displacement_1D_2025-10-29T00:00:00_bear
      confirming_mss_id: None
      fallback_path: YES
  epistemic_guard: fired correctly — disp_derived_* paths produce UNAVAILABLE (never OK)
  alignment: matches audit §4 prediction (010 + 011 both classified disp_derived_* fallback class)

ASK_3_per_commit_6_PASS_smoke_log:
  status: MINOR_DISCIPLINE_NOTE
  finding: per-commit chart-truth smoke deferred to mission-end; not run after each atomic commit
  fatality: not halt-class (final gates GREEN)
  record: documented in §4 below; SW51b brief MUST require strict per-commit smoke (full 12-fixture) given behavior-changing surface

ASK_5_targeted_diff_review:
  status: PASS
  file_list (5a):
    expected_modified: 4/4 ✓
    expected_created: 3/3 ✓
    forbidden_files_in_diff: NONE (regime.py, gate.py, cartridges, fixtures, chart_truth test ALL absent)
    line_signature: 974 insertions / 3 deletions — extension-only profile
  protected_swing_selection (5b):
    rule_in_code: "for s in reversed(swing_highs): if s.bar_index < i: ..." matches PATCH_1 "before break bar"
    preference_clause: implicit but correct — reversed iteration finds nearest preceding swing, satisfying "AFTER broken_swing if available"
    forbidden_patterns: ALL absent (no swings AT or AFTER break bar; no DR substitution; no price-extremity selection)
    verdict: conforms to PATCH_1 exactly
  upstream_refs_population (5c):
    rule_in_code: "disp_end >= break_idx OR k >= break_idx" handles both bar_index_end == break and contains-break cases
    zero_match_handling: returns None → upstream_refs=[] → boundary UNAVAILABLE downstream (correct chain)
    identity_link: direct Detection.id from displacement_ids_by_idx — no heuristic synthesis
    minor_observation: rule slightly broader than PATCH_2's strict bounds; multi-match returns first not escalates; 119/119 empirically clean; recorded for SW27 follow-up
  MoveStructureBoundary_dataclass (5d):
    fields_locked: 12/12 brief-specified fields present and correctly typed
    construction_mode_enum: only OK and UNAVAILABLE (no FALLBACK leak)
    structural_origin_time_naming: correctly named (not "origin_time")
    status_field_correctly_deferred: ACTIVE | ENDED is SW51b territory
  boundary_construction_site (5e):
    OK_path: regime update + boundary construction from same MSS
    UNAVAILABLE_path: disp_derived_* fallback explicitly produces _unavailable_boundary call
    no_DR_substitution: confirmed
    construction_mode_derivation: clean two-state (OK if polarity_ok and confirming_displacement_id; else UNAVAILABLE)
    deviation_recorded: regime mutation precedes boundary construction (sequential, not atomic); see §4
```

---

## §3 — Exit gates (12) — all resolved

```yaml
gate_1_chart_truth_6_PASS_unchanged: PASS (matrix in ASK_1)
gate_2_chart_truth_6_RED_unchanged_or_trace_enriched: PASS (semantic fields unchanged for all 6 RED)
gate_3_ars_parity_unchanged: PASS (151/151 / 0 divergences)
gate_4_identity_link_DIRECT: PASS (119/119)
gate_5_protected_swing_emission_correct: PASS (5b conformance + 14 new tests)
gate_6_boundary_construction: PASS (OK on MSS-driven; UNAVAILABLE on disp_derived_*)
gate_7_persistence_round_trip: PASS (test_move_structure_boundary.py round-trip + legacy load)
gate_8_no_DR_substitution: PASS (5e static review confirms no fallback branch)
gate_9_mypy_strict_zero_errors: PASS (0 errors / 183 files)
gate_10_lint_imports_preserved: PASS (6 KEPT / 0 broken)
gate_11_no_behavioral_hash_drift: PASS (existing detection fields byte-identical pre/post; only added keys diverge)
gate_12_persistence_backwards_compat: PASS (legacy snapshots load with boundary=None / UNAVAILABLE; never auto-promoted)

aggregate: 12/12 PASS
```

---

## §4 — Discipline notes recorded for canon and SW51b

```yaml
note_1_per_commit_smoke_was_deferred:
  what_happened: chart-truth smoke run at mission-end, not after each atomic commit
  fatality: not halt-class for SW51a (extension-only; final gates GREEN)
  why_recording: Phase 4b discipline mantra is per-commit; even when not fatal, slippage compounds
  rule_for_SW51b: per-commit FULL 12-fixture smoke MANDATORY — not subset; not deferred. SW51b touches RegimeTracker (regime.py:31-71) and emits production RETRACE; risk surface is materially higher than SW51a.
  brief_text_for_SW51b: "After every commit on this branch: run en1gma/tests/integration/test_daily_expansion_chart_truth.py FULL 12-fixture suite. Halt the commit cadence on any 6_PASS regression OR any unexpected RED→PASS flip."

note_2_displacement_match_rule_strictness_minor:
  what_happened: 5c match rule is "disp_end >= break_idx OR k >= break_idx" — slightly broader than PATCH_2's strict "bar_index <= break_bar_index <= bar_index_end"
  empirical_impact_in_SW51a: zero (119/119 produced upstream_refs cleanly with no multi-match issues)
  practical_effect: code accepts displacement starting AT break_idx ending after — the legitimate cluster case PATCH_2 wanted to allow
  open_concern: under multi-match scenarios, code returns FIRST match (window order) rather than escalating per PATCH_2 "if multiple_matches: STOP AND ESCALATE"
  classification: not halt-class — empirically empty risk surface today
  follow_up: SW27 brief authoring should re-check this rule against Olya Q3 STRICT 1:1; if SW27 surfaces multi-match cases, narrow PATCH Mission required

note_3_construction_ordering_sequential_not_atomic:
  what_happened: in map_engine.py boundary construction site (5e), regime mutation happens BEFORE boundary construction (regime_updated = update_on_mss(...); if regime_updated: build boundary)
  brief_intent: "construction at MSS-driven regime establishment (alongside Regime update)"
  delta: sequential ordering rather than atomic
  fatality: net behavior identical for SW51a; not halt-class
  SW51b_implication: when SW51b adds RETRACE classifier consuming MoveStructureBoundary, regime emission and boundary construction are 2 statements apart — not atomic. SW51b implementation must explicitly keep these synchronized (or refactor to atomic construction) to prevent intermediate-state divergence.
  brief_text_for_SW51b: must include explicit constraint on regime/boundary co-mutation atomicity (or refactor justification)
```

---

## §5 — Invariant registration

```yaml
invariant_id: INV-STRUCTURE-BOUNDARY-EVIDENCE-OR-UNAVAILABLE
parent: INV-EPISTEMIC-INTEGRITY
sibling: INV-MAP-CONSTRUCTION-MODE-EXPLICIT
text: |
  A MoveStructureBoundary may be OK only when constructed from an
  MSS-emitted protected swing plus direct confirming displacement
  identity. If evidence is missing, boundary is UNAVAILABLE.
  DealingRange or any adjacent spatial surface must never be
  substituted as boundary evidence.
state_at_SW51a_commit (this ratification): scaffold-armed
state_at_SW51b_commit (future): active (consumer enforcement when SW51b adds RETRACE classifier and ActiveMove lifecycle that refuses UNAVAILABLE boundary)
precedent_pattern: SW49 INV-GATE-REFUSES-FALLBACK-MAP scaffold-armed → active transition
auditable_in_code: yes — _boundary_from_mss + _unavailable_boundary in map_engine.py emit OK/UNAVAILABLE deterministically; tests assert distribution
g_ratification: REQUIRED for canon commit (this artifact)
```

---

## §6 — Canon update plan

```yaml
forward_plan:
  4b_mission_5_SW51a_status: CLOSED
  4b_mission_5_SW51b_status: AUTHORING (replaces prior SW51 day_state_causal_linkage entry)
  forward_queue_addition:
    SW58_FALLBACK_REGIME_AND_CASCADE_AUTHORITY:
      scope: guard or replace displacement_fallback regime stamping (map_engine.py:278-296); cascade authority three-field disposition
      empirical_target: trade_010 + trade_011 flip RED → PASS
      dependencies: SW51a + SW51b GREEN; audit findings already in hand
      classification: Category 2 single Mission
      register_state: queued (not authoring)

claude_md:
  finding_register: SW51a CLOSED at c3b716a; SW58 registered as queued
  invariants_active_or_scaffold_armed:
    add: INV-STRUCTURE-BOUNDARY-EVIDENCE-OR-UNAVAILABLE (scaffold-armed)
  baseline_status_line:
    test_count: 849 + 14 SW51a + 4 xfailed = 867 + 4 xfailed (verify on canon commit)
    chart_truth_12: unchanged (6 PASS / 6 RED) — primary fidelity surface preserved
    boundary_surface: introduced with construction_mode discipline
    identity_link: TIME_AND_TF_JOIN_ONLY → DIRECT_ID_LINK (119/119)

discipline_record:
  - SW51a closeout demonstrates: extension-Mission discipline holds when (a) audit-first (b) brief patches via GPT lateral (c) targeted diff review (d) explicit verification asks before ratification
  - per-commit smoke deferral logged as discipline note; SW51b brief must restore per-commit cadence
```

---

## §7 — Closeout

```yaml
SW51a: CLOSED
verdict: GREEN
canon_update: PENDING G ratification of this artifact
SW51b: NOT YET AUTHORING (deliberate; new work cycle)

next_steps_authorized_by_G:
  1_ratification_artifact: this document (G ratifies)
  2_canon_updates: FORWARD_PLAN + CLAUDE.md + SW58 registration + invariant scaffold-arm (next)
  3_SW51b_brief_drafting: separate work cycle (NOT parallel — clean closeout first)

risk_surface_handover_for_SW51b:
  - SW51b is first behavior-changing Mission in this cluster
  - touches RegimeTracker.update_on_mss flip rule (regime.py:61-68)
  - introduces production RETRACE phase emission
  - changes DirectionPermission consumption behavior (gate.py)
  - per-commit FULL 12-fixture smoke MANDATORY
  - atomic regime/boundary co-mutation (per discipline note 3)
  - 4 RED targets: trade_002, 008, 012, 014 (010 + 011 explicitly OUT — SW58 territory)
  - 6 PASS preserved at every commit boundary
  - GPT lateral REQUIRED on brief authoring (load-bearing precedent: 3x in current cluster)
```

---

*Ratification record. Closeout for canon. Changes to SW51a code beyond this point require new SW Mission ID.*
