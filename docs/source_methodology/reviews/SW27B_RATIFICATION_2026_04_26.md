# SW27b RATIFICATION — IDENTITY-GROUNDED FVG SELECTION

```yaml
mission_id: SW27b
mission_name: IDENTITY_GROUNDED_FVG_SELECTION
mission_classification: Phase 4b behavior-change Mission; closes SW27 lane
ratification_date: 2026-04-26
ratification_status: CLOSED
ratification_authority: G (sovereign) + CTO (Opus 4.7) + COO (Droid on M4)

implementation_branch: feature/sw27b-causal-fvg-selector
branch_HEAD: 6e06b98
branch_base: origin/feature/sw27a-fvg-causal-identity@9c44737

commits:
  98833c0: feat(sw27b) — plumb causal FVG selector substrate
  9fa5ea8: feat(sw27b) — apply identity-grounded FVG selector
  eb2b5cf: test(sw27b) — pin FVG selector edge cases
  6e06b98: docs(sw27b) — record brief and selector distribution

precedent_branches_preserved:
  feature/sw51a-structure-boundary@c3b716a
  feature/sw51b-active-move-classifier@cb8e4e9
  feature/sw27-identity-grounded-fvg@bede128 (v1 SW27; reference; semantically stale)
  feature/sw27a-fvg-causal-identity@9c44737 (SW27a; preserved)

upstream_audits:
  - SW27_AMBIGUITY_DIAGNOSTIC_2026_04_26 (CASE_C confirmed; 28 same-TF cases)
  - SW27a_RATIFICATION_2026_04_26 (CLOSED; INV-FVG-CAUSAL-IDENTITY-SURFACE ACTIVE)
  - SW27b_TECHNICAL_SUBSTRATE_2026_04_26 (6/6 gates PASS)
  - GPT_LATERAL_skeleton_v0_0 (10 patches; in skeleton)
  - GPT_ORIENTATION_on_substrate (5 patches; in v0.1)
  - GPT_LATERAL_v0_1 (9 patches; in v0.2)
  - DROID_PRE_FLIGHT_v0_2 (7 amendments A1-A7; in v0.3 via delegation pattern)
  - GPT_LATERAL_on_pre_flight_amendments (accept all 7)

upstream_olya_rulings_locked_and_implemented:
  Q3_2026_04_25: STRICT 1:1 — FVG to trade = FVG created BY structure-breaking displacement
  universality_2026_04_26: ratified UNIVERSAL scope
  leg_location_2026_04_26: anchor + premium/discount within displacement leg
  leg_midpoint_mechanical_2026_04_26:
    leg_midpoint = (displacement_span_high + displacement_span_low) / 2
    fvg_location = (fvg.top + fvg.bottom) / 2 (NOT fvg.ce)
    bullish: fvg_middle <= leg_midpoint (below/equal — discount)
    bearish: fvg_middle >= leg_midpoint (above/equal — premium)
    multiple_survivors: chart examples; do NOT hardcode tiebreak
```

---

## §1 — Mission summary

SW27b is the consumer of SW27a's FVG causal identity surface — the second behavior-change Mission of the SW27 lane and the closure of the lane.

The Mission replaced ChainEvaluator._match_fvg's largest-gap heuristic with a TWO-STAGE FILTER per Olya 2026-04-25 Q3 + Olya 2026-04-26 leg-location ruling:

- **Stage 1 — Causal Identity:** candidate FVG must contain `MSSMatch.confirming_displacement_id` in `upstream_refs`, match chain direction, be available at current bar (via `properties['detect_time']`, NOT anchor timestamp), and share timeframe with MSS / confirming displacement.
- **Stage 2 — Leg Location:** FVG middle `(top+bottom)/2` must lie on the favorable side of the displacement leg's midpoint, computed from displacement bar source (`bar_index..bar_index_end` at displacement TF). Bullish: at or below midpoint (discount). Bearish: at or above midpoint (premium).

Eight outcome categories emit with deterministic `rejection_reason` mapping:

- `CAUSAL_FVG_FOUND` — exactly one survivor → chain advances
- `CAUSAL_FVG_ABSENT` — no Stage 1 candidates (valid no-setup)
- `LOCATION_FILTER_REJECTED` — Stage 1 candidates exist; all fail Stage 2 (valid no-setup)
- `MULTIPLE_LOCATION_VALID_CAUSAL_FVGS` — >1 survives both stages (epistemic refusal)
- `LEG_MIDPOINT_UNAVAILABLE` — cannot compute leg span (epistemic refusal)
- `NO_UPSTREAM_REFS` — MSSMatch lacks `confirming_displacement_id`
- `NO_CONFIRMING_DISPLACEMENT_ID` — id present but lookup fails in `ltf_detections`
- `AMBIGUOUS_CONFIRMING_DISPLACEMENT` — preserved category

`AMBIGUOUS_CAUSAL_FVG_MATCH` (from SW27 v0.4) deprecated; zero production references.

This Mission is a **methodology + behavior change** at consumer decision level. Old largest-gap heuristic eliminated. No first/last/largest fallback under any condition. FVG location uses raw zone midpoint (NOT `fvg.ce`). Leg span uses displacement bar source via no-lookahead bar plumbing — no approximation.

The 28 same-TF ambiguous cases identified in SW27 ambiguity diagnostic (CASE_C) — which post-SW27a remained 28/28 ONE_TO_MANY — resolve to **28/28 CAUSAL_FVG_FOUND** post-SW27b. Olya's two-stage methodology fully disambiguates the cluster cases. **No Olya tiebreak chart-example session needed.**

---

## §2 — Mission gates (G1–G20)

```yaml
G1_chart_truth_12_preserved: PASS_EXPECTED_RED
  evidence: 10 PASS / 2 expected RED [trade_010, trade_011]
  measurement: pytest test_daily_expansion_chart_truth.py

G2_ars_parity_preserved: PASS
  evidence: 151/151 byte-identical
  measurement: python3 test_ars_parity.py (script-backed)

G3_new_unit_tests_green: PASS
  evidence: 22 SW27b unit tests PASS
  coverage: full taxonomy + boundaries + raw-midpoint-not-ce +
            no-lookahead + ref-not-found + TF predicate + chart-example packet

G4_mypy_strict_local_zero: PASS
  evidence: 0 errors

G5_lint_imports_preserved: PASS
  evidence: 6 KEPT / 0 broken

G6_per_commit_smoke_log: PASS
  evidence: per-commit smoke executed with commit type tags per SW27a refinement
            commits 1, 2 (production code) ran FULL bundle
            commit 3 (test-only) reduced bundle
            commit 4 (docs/diagnostic) reduced bundle

G7_invariant_consumer_enforcement: PASS
  evidence: no largest-gap fallback path; no first/last/largest tiebreak;
            no fvg.ce substitution; no leg span approximation;
            no v1 SW27 selector resurrection

G8_canon_doc_isolation: PASS
  evidence: git diff --name-only 9c44737..6e06b98 -- CLAUDE.md docs/canonical docs/briefs docs/handovers => empty
  authorized_tracked_artifacts (NOT canon doc):
    docs/briefs/draft/SW27b_BRIEF_v0_3_2026_04_26.md (per delegation pattern)
    docs/reviews/SW27B_28_CASE_DISTRIBUTION_2026_04_26.json (per GPT P2 auditable path)

G9_repo_topology_preserved: PASS
  evidence:
    sw27b_log: 6e06b98 + eb2b5cf + 9fa5ea8 + 98833c0 over 9c44737
    main_HEAD: ea7d27d (untouched at ratification time)
    sw27a_HEAD: 9c44737 (preserved)
    sw27_v1_HEAD: bede128 (preserved)
    no_rebase_or_force_push: confirmed
    no_push_yet: feature branch push pending canon push step

G10_three_caller_compatibility_with_8_outcomes: PASS
  callers_verified:
    map_canon/session.py: passes truncated bars_by_tf; handles all 8 outcomes
    chain_evaluator.py:180 internal: updated path
    run_discovery_scan.py: passes truncated bars_by_tf; handles outcomes
  discovery_scan_output_change: documented as informational (per GPT P9)

G11_boundary_inclusivity_verified: PASS
  evidence: at-midpoint cases ACCEPTED (bullish + bearish); just-past-midpoint REJECTED

G12_raw_midpoint_not_ce: PASS
  evidence: test where fvg.ce ≠ raw midpoint shows selector uses raw

G13_displacement_bar_traceability: PASS
  evidence: leg_high/low computed from same-TF same-source bars as confirming displacement
            via plumbed bars_by_tf[displacement.tf].iloc[bar_index:bar_index_end+1]

G14_multiple_survivor_diagnostic_complete: PASS
  evidence: MULTIPLE_LOCATION_VALID emission would include all candidate diagnostic fields
            (in 28-case run, count was 0; test verifies emission shape)

G15_28_case_distribution_recorded: PASS
  artifact_path: docs/reviews/SW27B_28_CASE_DISTRIBUTION_2026_04_26.json
  classification: INFO_REQUIRED (per GPT P8)
  result:
    total_cases: 28
    CAUSAL_FVG_FOUND: 28 (100%)
    LOCATION_FILTER_REJECTED: 0
    MULTIPLE_LOCATION_VALID_CAUSAL_FVGS: 0
    LEG_MIDPOINT_UNAVAILABLE: 0
    NO_CONFIRMING_DISPLACEMENT_ID: 0
  HT4_HT14_HT16_all_FALSE: confirmed
  no_chart_example_packet_needed: MULTIPLE_LOCATION_VALID was 0

G16_no_lookahead_invariant_preserved: PASS
  evidence: bars truncated at caller; selector slices/filters before computing leg span

G17_TF_predicate_explicit: PASS
  evidence: cross-TF FVG with matching upstream_refs rejected at Stage 1

G18_rejection_reason_deterministic_mapping: PASS
  evidence: each of 8 outcome categories emits exact rejection_reason string per spec

G19_canonical_confirmation_detect_time_pinned: PASS
  evidence: Stage 1 availability uses fvg.properties['detect_time'] (NOT Detection.time anchor)

G20_auditable_artifacts_path: PASS
  evidence: docs/reviews/SW27B_28_CASE_DISTRIBUTION_2026_04_26.json tracked
```

---

## §3 — Per-commit smoke log

### Commit 98833c0 (feat — production code: plumbing substrate)

```yaml
classification: production_code (FULL bundle binding)
chart_truth: PASS (10/2)
ars_parity: PASS (151/151)
existing_chain_unit_tests: PASS
existing_detection_tests: PASS (SW27a tests continue passing)
existing_map_tests: PASS
new_sw27b_plumbing_tests: PASS
mypy_strict: PASS
lint_imports: PASS (6/0)
full_integration_excluding_SW54_chart_truth: PASS
cascade_smoke: PASS (FVG remains non-leaf; cascade graph valid)
```

### Commit 9fa5ea8 (feat — production code: two-stage selector)

```yaml
classification: production_code (FULL bundle binding)
chart_truth: PASS (10/2)
ars_parity: PASS (151/151)
existing_chain_unit_tests: PASS
new_sw27b_selector_tests: PASS
existing_detection_tests: PASS
existing_map_tests: PASS
three_caller_compatibility_verified: PASS
mypy_strict: PASS
lint_imports: PASS (6/0)
full_integration_excluding_SW54_chart_truth: PASS
discovery_scan_output_delta_documented: yes (informational)
```

### Commit eb2b5cf (test — selector edge case pins)

```yaml
classification: test_only (reduced bundle per SW27a refinement)
new_sw27b_regression_pins: PASS
chart_truth: PASS (10/2)
ars_parity: PASS (151/151)
chain_unit_tests: PASS
mypy_strict: PASS
lint_imports: PASS
discipline_note: full bundle not literally rerun for test-only commit; per SW27a refinement
```

### Commit 6e06b98 (docs — brief artifact + diagnostic)

```yaml
classification: docs (reduced bundle per SW27a refinement)
new_artifacts:
  docs/briefs/draft/SW27b_BRIEF_v0_3_2026_04_26.md
  docs/reviews/SW27B_28_CASE_DISTRIBUTION_2026_04_26.json
chart_truth: PASS (10/2)
ars_parity: PASS (151/151)
chain_unit_tests: PASS
mypy_strict: PASS
lint_imports: PASS
diagnostic_artifact_parseable: PASS
```

---

## §4 — Diff review

```yaml
diff_command: git diff 9c44737..6e06b98 --stat
file_changes_summary:
  source_files_modified:
    - en1gma/console/chain/chain_types.py — MSSMatch.confirming_displacement_id field; ChainDiagnostic SW27b outcome fields
    - en1gma/console/chain/chain_evaluator.py — _match_fvg replaced with two-stage filter; rejection_reason mapping
    - en1gma/console/chain/canon/map_canon/session.py — bars_by_tf plumbing; trace propagation
    - en1gma/console/chain/canon/map_canon/trace_schema.py — ChainEvaluation field extensions
    - en1gma/scripts/run_discovery_scan.py — bars_by_tf plumbing; outcome handling

  test_files_added:
    - en1gma/tests/console/chain/test_sw27b_plumbing.py
    - en1gma/tests/console/chain/test_sw27b_selector.py (covers Stage 1 + Stage 2 + outcome taxonomy)

  artifact_files_added (per GPT P2 auditable path):
    - docs/briefs/draft/SW27b_BRIEF_v0_3_2026_04_26.md
    - docs/reviews/SW27B_28_CASE_DISTRIBUTION_2026_04_26.json

  zero_canon_doc_modifications_on_branch: confirmed
  zero_data_fixture_modifications: confirmed
```

---

## §5 — Empirical state at SW27b close

```yaml
fidelity_baseline_at_branch_HEAD:
  chart_truth_12: 10 PASS / 2 RED [trade_010, trade_011] — UNCHANGED
  ars_parity_151: 151/151 byte-identical — UNCHANGED
  identity_link_mss_to_displacement: DIRECT_ID_LINK 119/119 (SW51a; preserved)
  identity_link_fvg_to_displacement: DIRECT_ID_LINK populated (SW27a; preserved)
  fvg_selection_rule: TWO-STAGE FILTER (causal identity + leg location) (NEW post-SW27b)
  ars_chain_evaluator_isolation: ISOLATED (preserved)
  mypy_strict_local: 0 errors / 191+ source files
  lint_imports: 6 KEPT / 0 broken

28_same_TF_case_distribution_post_SW27b:
  total_cases: 28
  CAUSAL_FVG_FOUND: 28 (100%)
  LOCATION_FILTER_REJECTED: 0
  MULTIPLE_LOCATION_VALID_CAUSAL_FVGS: 0
  LEG_MIDPOINT_UNAVAILABLE: 0
  NO_CONFIRMING_DISPLACEMENT_ID: 0

  empirical_significance: |
    Olya's two-stage methodology (causal identity → premium/discount
    location) cleanly disambiguates every same-TF cluster case. The
    28 cases that were ambiguous in v1 SW27 (case_C in ambiguity
    diagnostic), and remained ONE_TO_MANY post-SW27a, all resolve
    to a single causal+location-valid FVG post-SW27b. Olya tiebreak
    chart-example session is NOT needed.

methodology_completeness_at_lane_close:
  Olya_Q3_2026_04_25: implemented (causal identity)
  Olya_universality_2026_04_26: implemented (UNIVERSAL chain FVG selection)
  Olya_leg_location_2026_04_26: implemented (premium/discount within displacement leg)
  Olya_leg_midpoint_mechanical_2026_04_26: implemented (raw midpoint; bar source; inclusive)

forward_input_for_remaining_phase_4b:
  SW31: independent (displacement grade filter; HTF alignment)
  SW58: independent (fallback regime guard; closes 010+011 RED)
  SW50: independent (H4 cascade replay fidelity)
```

---

## §6 — Discipline carry-forward

```yaml
sw27b_workflow_innovations_to_carry_forward:

  delegation_pattern_proven_at_v0_3:
    droid_amendment_proposal_workflow_validated:
      - Droid surfaced 7 amendments at pre-flight (A1-A7)
      - GPT lateral confirmed all 7 as precision (no design change)
      - CTO independent assessment confirmed (no dissent)
      - G ratified
      - COO authored v0.3 + auto-dispatched implementation
      - guardrail 1 (self-check): COO confirmed clean before dispatch
      - guardrail 2 (change summary in ratification report): COO recorded summary

    pattern_eligibility_for_forward_Missions:
      eligible: precision / implementation / correctness / hygiene amendments
      NOT_eligible: methodology / scope / forbidden semantics / invariant statements

    save_relative_to_pure_CTO_reprint: ~30-45 min CTO context per cycle

  per_commit_smoke_refinement_validated:
    SW27a refinement (commit type tags; reduced bundle for test-only / scratch-only)
    applied cleanly to SW27b 4-commit Mission
    pattern_carries_forward: yes

  GPT_lateral_layer_density:
    cumulative_GPT_patches_in_SW27b_brief: 24 patches across cycle
      - 10 (skeleton lateral)
      - 5 (orientation on substrate)
      - 9 (v0.1 lateral)

    each_layer_caught_distinct_class_of_issue
    no_layer_redundant

    forward_pattern: continue hybrid workflow with full GPT lateral chain for
                     methodology-class Missions

  delegation_+_amendment_proposal_extends_to_factory_MISSION:
    next_iteration: Phase 4b lane close as holistic factory.ai MISSION
                   (SW31 + SW50 + SW58)
    orchestrator: Opus on factory.ai
    workers: GPT5.5 sub-agent
    CTO_role: methodology gate at checkpoints
    G_role: ratification at checkpoints

    workflow_evolution_summary:
      SW51_cluster: full per-Mission CTO authoring
      SW27_cluster: hybrid (CTO authors brief; COO Substrate; Droid amendments at v0.3)
      SW27b_v0_3: COO auto-dispatch with self-check + guardrails
      Phase_4b_lane_close: factory.ai MISSION orchestrator pattern (forthcoming)

  workflow_assessment_at_SW27_lane_close:
    pattern_holds_at_growing_complexity
    each_innovation_validated_before_next_layer_introduced
    no_signal_loss_at_any_layer

methodology_observation:
  olya_rulings_specified_at_right_altitude:
    Q3 (2026-04-25): general principle
    universality (2026-04-26): scope
    leg_location (2026-04-26): mechanical filter
    leg_midpoint_mechanical (2026-04-26): exact field references

    each_subsequent_ruling_added_precision_without_contradicting_prior
    28/28_clean_resolution_demonstrates_specification_was_complete
    no_methodology_question_left_for_SW27b

    forward_principle: |
      Olya questions are most efficient when bounded to mechanical
      questions Olya can answer in 5-10 minutes. CTO's role is to
      decompose methodology into sharp questions, not bring Olya
      ambiguous "what should we do?" prompts.
```

---

## §7 — Invariant family state at SW27b close

```yaml
INV-EPISTEMIC-INTEGRITY (parent — unchanged)
  peers (3 — unchanged):
    INV-STRATEGY-CONFIG-SINGLE-SOURCE
    INV-FIDELITY-ANCHORED-TO-CHART-TRUTH
  children (7 — was 6; one new):
    INV-STRATEGY-LOAD-MUST-SUCCEED
    INV-MAP-CONSTRUCTION-MODE-EXPLICIT
    INV-GATE-REFUSES-FALLBACK-MAP
    INV-STRUCTURE-BOUNDARY-EVIDENCE-OR-UNAVAILABLE
    INV-RETRACE-BOUNDED-BY-STRUCTURE
    INV-FVG-CAUSAL-IDENTITY-SURFACE (SW27a; ACTIVE; consumed by SW27b)
    INV-CHAIN-FVG-CAUSAL-SELECTION (NEW; ACTIVE post-SW27b)

INV-CHAIN-FVG-CAUSAL-SELECTION statement (locked):
  "Chain FVG selection for trade evaluation must use a TWO-STAGE FILTER:

   Stage 1 (causal identity): candidate FVG must contain confirming
   displacement's id in upstream_refs (per INV-FVG-CAUSAL-IDENTITY-SURFACE),
   match chain direction, be available at current bar (via
   confirmation/detect_time, NOT anchor timestamp), and share timeframe
   with MSS / confirming displacement.

   Stage 2 (leg location): FVG middle (top+bottom)/2 must lie on
   favorable side of structure-breaking displacement leg's midpoint,
   computed from the displacement's bar source (bar_index..bar_index_end).
   Bullish: at or below midpoint (discount). Bearish: at or above
   midpoint (premium). At-midpoint INCLUSIVE on favorable side.

   Eight outcome categories emit with deterministic rejection_reason
   mapping:
     CAUSAL_FVG_FOUND, CAUSAL_FVG_ABSENT, LOCATION_FILTER_REJECTED,
     MULTIPLE_LOCATION_VALID_CAUSAL_FVGS, LEG_MIDPOINT_UNAVAILABLE,
     NO_UPSTREAM_REFS, NO_CONFIRMING_DISPLACEMENT_ID,
     AMBIGUOUS_CONFIRMING_DISPLACEMENT.

   No heuristic substitute permitted at any stage. No first/last/largest
   tiebreak. FVG location uses raw zone midpoint (top+bottom)/2, NOT
   fvg.ce. Leg span uses displacement bar source via no-lookahead bar
   plumbing — no approximation."

scaffold_armed_at: commit 1 (98833c0; plumbing)
activation: commit 2 (9fa5ea8; full two-stage active)
enforcement: commit 3 (eb2b5cf; regression pins)
diagnostic: commit 4 (6e06b98; 28/28 clean distribution)
```

---

## §8 — SW27 lane closure

```yaml
sw27_lane_status: CLOSED
lane_components:
  SW27_v1: superseded (architecture insufficient — bar-index inference; case_C identified)
  SW27a: CLOSED 2026-04-26 (FVG causal identity primitive; INV-FVG-CAUSAL-IDENTITY-SURFACE ACTIVE)
  SW27b: CLOSED 2026-04-26 (causal identity + leg-location selector; INV-CHAIN-FVG-CAUSAL-SELECTION ACTIVE)

methodology_questions_remaining_for_SW27_lane: NONE
  Olya rulings fully implemented
  28/28 ambiguous cases resolved
  No tiebreak question remains
  No chart-example packet needed

forward_consumers_of_SW27_lane_invariants:
  - all production chain FVG selection paths (UNIVERSAL per Olya 2026-04-26)
  - map_canon/session.py
  - chain_evaluator.py internal
  - run_discovery_scan.py (discovery scan output naturally reflects new methodology)
  - any future cartridge or selector consuming chain logic

discovery_scan_v4_rerun_disposition:
  status: enabled (post-SW27b implementation)
  classification: forward action; not blocking SW58/SW31/SW50
  not_a_methodology_gate: scan is consumer; new selection rule changes scan output
  recommendation: rerun after Phase 4b lane close (post-SW58); document new baseline
```

---

## §9 — Forward queue update

```yaml
phase_4b_status_at_SW27b_close:

  closed (8):
    - SW48 (state-gating reproducibility)
    - SW49_narrow (chain TF determinism)
    - SW56 (orchestrator wiring)
    - SW57 (replay context)
    - SW51a (MSS structure boundary identity)
    - SW51b (active move classifier)
    - SW27a (FVG causal identity surface)
    - SW27b (identity-grounded FVG selection) [NEW]

  in_flight: none

  next_active: PHASE_4B_LANE_CLOSE (holistic factory.ai MISSION encompassing SW31 + SW50 + SW58)
    classification: orchestrator-pattern Mission with internal serial/parallel structure
    orchestrator: Opus on factory.ai
    workers: GPT5.5 sub-agent + COO Droid as needed
    CTO_role: 6 ratification checkpoints + escalation triggers
    G_role: holistic Mission ratification + canon push

  remaining_methodology_missions_within_holistic_Mission:
    SW31: displacement grade filter; HTF alignment per Olya 2026-04-25 Q1+Q2
    SW58: fallback regime guard + cascade authority; closes 010+011 RED → 12/12 GREEN
    SW50: H4 cascade replay fidelity; small cleanup

  housekeeping_registered:
    SW-INFRA-1: mypy CI types-PyYAML + river.py cleanup (PRE-EXISTING; backlog)
    SW-INFRA-2: SW54 fingerprint baseline regeneration (post-SW58)

phase_4b_methodology_lane_distance_remaining:
  with_holistic_Mission_pattern:
    optimistic ~3-5 days (parallel SW31+SW50; SW58 isolated)
    realistic ~5-7 days
  if_revert_to_per_Mission_pattern:
    optimistic ~5-7 days
    realistic ~7-10 days

  pessimistic_either_pattern: ~10-14 days (if SW58 splits or methodology surprise)

post_phase_4b_methodology_lane_close:
  walk_forward_re_validation (5-year; Olya-gated)
  M3 deployment cycle (feature branch code merged to main; pinned to M3)
  Olya extreme confidence checkpoint (G's stated criterion)
  G ratifies execution mode → T2 active → system online
```

---

*SW27 lane CLOSED. Two new invariants ACTIVE. 28/28 ambiguity resolved. No outstanding Olya touch for SW27 lane. Phase 4b methodology lane proceeds via holistic factory.ai MISSION encompassing SW31 + SW50 + SW58.*
