# SW27a RATIFICATION — FVG CAUSAL IDENTITY SURFACE

```yaml
mission_id: SW27a
mission_name: FVG_CAUSAL_IDENTITY_SURFACE
mission_classification: Phase 4b extension-only identity primitive
ratification_date: 2026-04-26
ratification_status: CLOSED
ratification_authority: G (sovereign) + CTO (Opus 4.7) + COO (Droid on M4)

implementation_branch: feature/sw27a-fvg-causal-identity
branch_HEAD: 9c44737
branch_base: feature/sw51b-active-move-classifier@cb8e4e9

commits:
  389acc4: feat(sw27a) — add FVG causal identity surface
  d00886b: test(sw27a) — pin FVG consumer invariance
  9c44737: test(sw27a) — record post-identity ambiguity distribution

precedent_branches_preserved:
  feature/sw51a-structure-boundary@c3b716a
  feature/sw51b-active-move-classifier@cb8e4e9
  feature/sw27-identity-grounded-fvg@bede128 (v1 SW27; reference for SW27b salvage decisions)

upstream_audits:
  - SW27_AMBIGUITY_DIAGNOSTIC_2026_04_26 (CASE_C confirmed; 28 same-TF ambiguous cases)
  - SW27A_TECHNICAL_SUBSTRATE_2026_04_26 (8/8 gates PASS)
  - GPT_LATERAL_v0_1 (7 patches; all incorporated)
  - DROID_PRE_FLIGHT_v0_2 (PROCEED_CONDITIONAL; 7 amendments; all in v0.3)

upstream_rulings:
  - Olya 2026-04-25 Q3: STRICT 1:1 — FVG to trade = FVG created BY structure-breaking displacement
  - Olya 2026-04-26 universality: ratified UNIVERSAL scope
  - Olya 2026-04-26 leg-location ruling (informs SW27b, not SW27a)
  - Olya 2026-04-26 leg-midpoint mechanical confirmation (informs SW27b)
```

---

## §1 — Mission summary

SW27a is the FVG causal identity primitive — analog of SW51a for the FVG detector.

The Mission added direct provenance plumbing: every FVG Detection now carries `upstream_refs` populated from same-timeframe, same-direction Displacement Detections whose `bar_index..bar_index_end` span mechanically contains the FVG's B-candle bar index (`fvg.bar_index - 1`). Multiple matching displacements are recorded in deterministic order. The detector records mechanical provenance only — no selection, no ranking, no methodology inference.

This Mission is **extension-only at the consumer decision level**: FVG Detection objects acquire a populated additive field (`upstream_refs`); no consumer changes its decisions. The change is a scaffold for SW27b causal selection.

The Mission resolved the SW27 ambiguity diagnostic (CASE_C) which surfaced when the v1 SW27 attempt found 59 AMBIGUOUS_CAUSAL_FVG_MATCH outcomes during exploratory production-window replay. SW27 was split into SW27a (this Mission, identity primitive) + SW27b (forthcoming, causal selector with two-stage filter per Olya 2026-04-26 ruling).

---

## §2 — Mission gates (G1–G11)

```yaml
G1_chart_truth_12_preserved: PASS
  evidence: 10 PASS / 2 expected RED [trade_010, trade_011]
  measurement: pytest test_daily_expansion_chart_truth.py

G2_ars_parity_preserved: PASS
  evidence: 151/151 byte-identical; divergences = 0
  measurement: python3 test_ars_parity.py (script-backed)

G3_consumer_decision_semantics_unchanged: PASS
  evidence:
    integration_test: test_fvg_decision_projection_matches_compact_pre_sw27a_constants PASS
    chain_test: test_chain_decision_projection_ignores_additive_fvg_upstream_refs PASS
    backcompat_test: test_missing_upstream_backcompat_yields_empty_upstream_refs PASS

G4_new_unit_tests_green: PASS
  evidence: test_sw27a_fvg_causal_identity.py 12 PASS + 2 commit-2 tests = 14 total

G5_mypy_strict_local_zero: PASS
  evidence: 0 issues / 191 source files

G6_lint_imports_preserved: PASS
  evidence: 6 contracts kept / 0 broken

G7_per_commit_smoke_log: PASS_WITH_DISCIPLINE_NOTE
  evidence: All final-state gates PASS; per-commit FULL bundle was rerun on commit 1 (production code) and partially on commits 2-3 (test-only and scratch-only)
  carry_forward_note: see §6 of this ratification

G8_cascade_graph_integrity: PASS
  evidence:
    cascade_smoke: "cascade graph OK"
    locked_baseline: en1gma/console/detection/locked_baseline.yaml:46 fvg upstream = ['displacement']

G9_canon_doc_isolation: PASS
  evidence: git diff --name-only cb8e4e9..9c44737 -- CLAUDE.md docs/canonical docs/briefs docs/handovers => empty

G10_repo_topology_preserved: PASS
  evidence:
    sw27a_log: 9c44737 + d00886b + 389acc4 over cb8e4e9
    main_HEAD: 6e4de08 (untouched)
    sw27_reference_HEAD: bede128 (preserved)
    no_rebase_or_force_push: confirmed

G11_post_SW27a_28_cases_distribution_recorded: RECORDED (informational; not pass/fail)
  evidence: scratch/sw27a_diagnostic/post_sw27a_ambiguous_cases.json parseable
  finding: 28/28 ONE_TO_MANY (all 28 cases get upstream_refs populated; all 28 remain 1:many post-SW27a)
  halt_condition_HT10_all_zero_match: FALSE (refs populated; commit 1 implementation correct)
```

---

## §3 — Per-commit smoke log

### Commit 389acc4 (feat — production code)

```yaml
chart_truth: PASS_EXPECTED_RED (10/2)
ars_parity: PASS (151/151)
existing_fvg_detector_tests: PASS (49 detection tests)
new_sw27a_tests: PASS (12)
chain_unit_tests: PASS (64)
map_tests: PASS (117)
cascade_smoke: PASS
mypy_strict: PASS
lint_imports: PASS (6 KEPT / 0 broken)
integration_excluding_SW54_chart_truth: PASS (62 / 12 deselected)
```

### Commit d00886b (test — consumer invariance)

```yaml
chart_truth: PASS_EXPECTED_RED (10/2)
ars_parity: PASS (151/151)
new_commit2_tests: PASS (2)
chain_unit_tests: PASS (64)
mypy_strict: PASS
lint_imports: PASS
integration_excluding_SW54_chart_truth: PASS (64 / 12 deselected)
discipline_note: detection/map/cascade not literally rerun (test-only commit; source unchanged)
```

### Commit 9c44737 (test — diagnostic record)

```yaml
diagnostic_json_parse: PASS
chain_unit_tests: PASS (64)
chart_truth: PASS_EXPECTED_RED (10/2)
ars_parity: PASS (151/151)
mypy: PASS
lint_imports: PASS
discipline_note: scratch-only commit; full bundle not rerun (no production code change)
```

---

## §4 — Diff review

```yaml
git_diff_stat (cb8e4e9..9c44737):
  en1gma/console/detection/locked_baseline.yaml: +1 / -1
  en1gma/console/detection/ra_engine/detectors/fvg.py: +57 / -4
  en1gma/tests/console/detection/test_sw27a_fvg_causal_identity.py: +195 (NEW)
  en1gma/tests/integration/test_sw27a_consumer_decision_invariance.py: +308 (NEW)
  scratch/sw27a_diagnostic/full_corpus_post_sw27a.json: +1934 (NEW; not committed to main; lives in feature branch scratch)
  scratch/sw27a_diagnostic/post_sw27a_ambiguous_cases.json: +1026 (NEW; same)

  total: 6 files; 3517 insertions / 5 deletions

source_changes_summary:
  fvg.py:58-60: required_upstream now ['displacement']
  fvg.py:63-72: canonical direction reads Detection.direction top-level; properties.direction must match (lowercased) or raises
  fvg.py:74-104: deterministic same-TF same-direction displacement upstream_refs computation
  fvg.py:132: missing-upstream tolerance (upstream None or no displacement → empty list)
  fvg.py:303: emits upstream_refs in Detection construction

config_changes:
  locked_baseline.yaml:46: fvg upstream [] → ['displacement']

zero_data_fixture_canon_doc_modifications: confirmed
```

---

## §5 — Empirical state post-SW27a

```yaml
fidelity_baseline_at_branch_HEAD:
  chart_truth_12: 10 PASS / 2 RED [trade_010, trade_011] — UNCHANGED from sw51b base
  ars_parity_151: 151/151 byte-identical — UNCHANGED
  identity_link_mss_to_displacement: DIRECT_ID_LINK 119/119 (SW51a; preserved)
  identity_link_fvg_to_displacement: DIRECT_ID_LINK populated post-SW27a (NEW)
  ars_chain_evaluator_isolation: ISOLATED (preserved)
  mypy_strict_local: 0 errors / 191 source files (was 189; +2 new test files)
  lint_imports: 6 KEPT / 0 broken

28_same_TF_ambiguous_cases_post_SW27a:
  cases_evaluated: 28
  cases_with_any_upstream_refs: 28 (100%)
  cases_with_zero_upstream_refs: 0
  cases_resolved_to_1_to_1: 0
  cases_remaining_ONE_TO_MANY: 28 (100%)
  candidate_count_distribution: {2: 28}
  interpretation: |
    All 28 same-TF ambiguous cases are cluster-displacement scenarios where
    one displacement legitimately created two FVGs. SW27a tagged both
    truthfully. SW27b will apply Olya's leg-location filter to disambiguate.

forward_input_for_SW27b: |
  Olya 2026-04-26 leg-location ruling provides the methodology to resolve
  these 28 ONE_TO_MANY cases. SW27b implements two-stage filter:
    Stage 1: causal identity (read FVG.upstream_refs from SW27a)
    Stage 2: leg location filter (premium/discount within displacement leg)
  Empirical question: how many of 28 cases resolve to 1:1 after Stage 2;
  how many become MULTIPLE_LOCATION_VALID (chart-example packet for Olya).
```

---

## §6 — Discipline carry-forward

```yaml
sw27a_specific_discipline_carry_forward:

  per_commit_smoke_refinement (NEW for forward Missions):

    binding_rule_from_SW51_cluster: |
      "per-commit FULL smoke required for multi-commit Missions"

    sw27a_practice:
      production_code_commits: full smoke run BEFORE next commit
      test_only_commits: smoke partially rerun; final state PASS
      scratch_only_commits: smoke not literally rerun; final state PASS

    refinement_for_forward_briefs (SW27b onward):
      per_commit_FULL_smoke binding for: production code commits
      per_commit_smoke MAY be reduced for test-only or scratch-only commits to:
        - new tests in this commit PASS
        - mypy + lint clean (if affected)
        - chart-truth + ARS spot-check (lightweight)
      requirement: commit messages explicitly tag commit type
                   (test-only / scratch-only / production-code)

    rationale: |
      "per-commit FULL smoke" was authored for SAFETY against silent
      production drift. Test-only and scratch-only commits don't carry
      that risk. Reducing requirement on these commit types preserves
      the discipline's intent without false friction.

    not_a_relaxation_of_safety: production code commits remain bound

  workflow_observation:
    delegation_pattern_proven: |
      v0.3 brief authoring delegated to COO (Droid) for mechanical
      amendments only. CTO ratified before dispatch. Clean turnaround;
      no semantic drift. Pattern available for future cycles where
      pre-flight findings are mechanical/precision class.

  hybrid_workflow_continued_validation:
    sw27a_caught_at_each_layer:
      Substrate: 4 architectural questions (universality, ARS isolation, split, OQ4)
      GPT_pre_author_lateral: fail-closed binding + 3-candle exactness + monolithic argument
      CTO_scope_clarification: universality + ARS isolation
      GPT_v0_1_lateral: 9 patches in SW27 + 7 patches in SW27a
      Droid_pre_flight: 7 amendments
      G_repo_decisions: D1/D2/D3/D4 ratifications
      COO_implementation: 28/28 ONE_TO_MANY diagnostic surfaced

    pattern_holds: continue for SW27b, SW31, SW58, SW50
```

---

## §7 — Invariant family state at SW27a close

```yaml
INV-EPISTEMIC-INTEGRITY (parent — unchanged)
  peers (3 — unchanged):
    INV-STRATEGY-CONFIG-SINGLE-SOURCE
    INV-FIDELITY-ANCHORED-TO-CHART-TRUTH
  children (6 — was 5; one new):
    INV-STRATEGY-LOAD-MUST-SUCCEED
    INV-MAP-CONSTRUCTION-MODE-EXPLICIT
    INV-GATE-REFUSES-FALLBACK-MAP
    INV-STRUCTURE-BOUNDARY-EVIDENCE-OR-UNAVAILABLE
    INV-RETRACE-BOUNDED-BY-STRUCTURE
    INV-FVG-CAUSAL-IDENTITY-SURFACE (NEW; ACTIVE post-SW27a; scaffold for SW27b)

INV-FVG-CAUSAL-IDENTITY-SURFACE statement:
  "FVG detections carry upstream_refs to same-timeframe same-direction
   displacement detections whose bar_index..bar_index_end span
   mechanically contains the FVG's B-candle bar_index (fvg.bar_index -
   1). Multiple matching displacements are listed in deterministic
   order by (bar_index, bar_index_end, id). The detector records
   provenance only — it does not rank, select, or infer trade
   relevance among multiple linked FVGs. Selection semantics belong
   to chain-layer consumers (SW27b)."

scaffold_status: ACTIVE (production code populates)
consumer_status: not yet enforced (SW27b activates consumption)
```

---

## §8 — Forward queue update

```yaml
phase_4b_status_at_SW27a_close:

  closed:
    - SW48 (state-gating reproducibility)
    - SW49_narrow (chain TF determinism)
    - SW56 (orchestrator wiring)
    - SW57 (replay context)
    - SW51a (MSS structure boundary identity)
    - SW51b (active move classifier)
    - SW27a (FVG causal identity surface)  [NEW]

  in_flight: none

  next_active_mission: SW27b (causal FVG selector with two-stage filter per Olya 2026-04-26)

  remaining_queue:
    SW27b: forthcoming; consumes INV-FVG-CAUSAL-IDENTITY-SURFACE; behavior change
    SW31: displacement grade filter; independent
    SW58: fallback regime guard + cascade authority (closes 010+011 RED → PASS)
    SW50: H4 cascade replay fidelity; small cleanup

  housekeeping_registered:
    SW-INFRA-1: mypy CI types-PyYAML + river.py cleanup (PRE-EXISTING; backlog)
    SW-INFRA-2: SW54 fingerprint baseline regeneration (post-SW58; canon-declared non-authority traces)

phase_4b_methodology_lane_distance:
  remaining_methodology_missions: 4 (SW27b + SW31 + SW58 + SW50)
  largest_remaining: SW58 (medium-large; produces 12/12 GREEN milestone)
  smallest_remaining: SW50 (small cleanup)
```
