# Branch/Main Reconciliation Audit - Phase 4b

```yaml
document: BRANCH_MAIN_RECONCILIATION_2026_04_27
mission_id: BRANCH_MAIN_RECONCILIATION_PHASE4B
classification: REPO_TOPOLOGY_AUDIT_THEN_SYNC
effect: workflow + release_hygiene
date: 2026-04-27
phase: PHASE_1_READ_ONLY_TOPOLOGY_REPORT
status: REPORT_ONLY_NO_SYNC_PERFORMED
```

---

## 1. Current branch / HEAD / dirty state

```yaml
fetch: "git fetch origin --prune completed cleanly"

current_branch:
  local: feature/phase4b-lane-close
  remote_tracking: origin/feature/phase4b-lane-close
  status: "local == remote"

heads:
  main: be1f2443b747c18a41d3e671992fafe6ce6d7e0c
  origin/main: be1f2443b747c18a41d3e671992fafe6ce6d7e0c
  feature/phase4b-lane-close: 1f23f0a09d51d27eb40e0f6dc2f3593c4f52f239
  origin/feature/phase4b-lane-close: 1f23f0a09d51d27eb40e0f6dc2f3593c4f52f239
  merge_base: ea50048b86d063ef3af886147376e5042a61e54b

dirty_state:
  tracked_changes: none
  untracked_files_present: true
  action_taken: "left untouched"
```

---

## 2. Commits on feature not on main

```yaml
main..feature/phase4b-lane-close:
  - "1f23f0a docs(canon): canonical document hygiene sweep"
  - "cef8fc5 docs(canon): CERTIFICATION_STATE v1.0 — walk-forward provisional stability"
  - "584309f feat(scripts): walk-forward re-validation harness (parallel)"

interpretation: |
  Feature contains the post-walk-forward certification doc and the doc hygiene
  sweep. It also contains the walk-forward harness commit that generated /
  supports the certification evidence surface.
```

---

## 3. Commits on main not on feature

```yaml
feature/phase4b-lane-close..main:
  - "be1f244 merge: Phase 4b lane-close → main (11/12 chart-truth GREEN)"
  - "491b694 docs(archive): archive superseded SW51b handover artifacts"

interpretation: |
  main is not simply behind feature. It already has a Phase 4b merge commit
  and one archive-only commit after the common base.
```

---

## 4. File diff summary

```yaml
main..feature_name_status:
  modified:
    - CLAUDE.md
    - docs/canonical/FORWARD_PLAN.md
    - en1gma/scripts/run_discovery_scan.py
  renamed:
    - "docs/canonical/PHASE_4_RATIFICATION.md -> docs/archive/PHASE_4_RATIFICATION.md"
    - "docs/canonical/POST_PHASE_3_ORACLE.md -> docs/archive/POST_PHASE_3_ORACLE.md"
  added:
    - docs/canonical/CERTIFICATION_STATE.md
    - docs/reviews/DOC_OWNERSHIP_AUDIT_2026_04_27.md
    - en1gma/scripts/run_walk_forward.py

main..feature_stat:
  files_changed: 8
  insertions: 1726
  deletions: 1723

feature..main_name_status:
  main_only_effective_diff:
    - "main has the Phase 4b merge commit"
    - "main has archive-only handover artifact changes"
    - "main lacks feature's CERTIFICATION_STATE, walk-forward harness, and doc hygiene sweep"
```

---

## 5. Phase 4b code / docs containment

```yaml
expected_phase4b_lane_close_commits:
  c34c844_SW31_displacement_grade_filter:
    contained_by: [feature/phase4b-lane-close, main]
  a27a6c6_SW50_H4_cascade_replay_fidelity:
    contained_by: [feature/phase4b-lane-close, main]
  13dccac_SW58a_FALLBACK_on_displacement_only_regime:
    contained_by: [feature/phase4b-lane-close, main]
  57d7824_SW58b1_HTF_warmup_90_days:
    contained_by: [feature/phase4b-lane-close, main]
  9758f4e_SW58b1_no_lookahead_guard:
    contained_by: [feature/phase4b-lane-close, main]
  eb4e493_ratification_methodology_seed_VAULT_FORWARD_PLAN:
    contained_by: [feature/phase4b-lane-close, main]

post_lane_feature_only_commits:
  584309f_walk_forward_harness:
    contained_by: [feature/phase4b-lane-close]
    contained_by_main: false
  cef8fc5_CERTIFICATION_STATE_v1:
    contained_by: [feature/phase4b-lane-close]
    contained_by_main: false
  1f23f0a_doc_hygiene_sweep:
    contained_by: [feature/phase4b-lane-close]
    contained_by_main: false

answer_main_already_contains_phase4b_code_commits: YES
answer_main_already_contains_doc_hygiene_commit: NO
answer_main_already_contains_certification_state_commit: NO
answer_main_already_contains_walk_forward_harness_commit: NO
```

---

## 6. Archive moves detected

```yaml
archive_moves_on_feature:
  - "docs/canonical/PHASE_4_RATIFICATION.md -> docs/archive/PHASE_4_RATIFICATION.md"
  - "docs/canonical/POST_PHASE_3_ORACLE.md -> docs/archive/POST_PHASE_3_ORACLE.md"

live_surface_stale_path_check:
  CLAUDE.md: "no stale docs/canonical/PHASE_4_RATIFICATION.md or docs/canonical/POST_PHASE_3_ORACLE.md references"
  docs/canonical/FORWARD_PLAN.md: "no stale docs/canonical/PHASE_4_RATIFICATION.md or docs/canonical/POST_PHASE_3_ORACLE.md references"
  docs/canonical/CERTIFICATION_STATE.md: "no stale docs/canonical/PHASE_4_RATIFICATION.md or docs/canonical/POST_PHASE_3_ORACLE.md references"
```

---

## 7. Visibility checks

```yaml
trade_011_visible:
  CLAUDE.md: YES
  docs/canonical/FORWARD_PLAN.md: YES
  docs/canonical/CERTIFICATION_STATE.md: YES

MSS_NOT_EQUAL_ACTIVE_CONTROL_visible:
  CLAUDE.md: YES
  docs/canonical/FORWARD_PLAN.md: YES
  docs/canonical/CERTIFICATION_STATE.md: YES
```

---

## 8. Untracked files left untouched

```yaml
untracked:
  - docs/briefs/PHASE_4B_LANE_CLOSE_MISSION_SPEC_2026_04_26.md
  - docs/briefs/draft/SW27A_BRIEF_v0_3_2026_04_26.md
  - docs/handovers/CTO_HANDOVER_2026_04_27_TO_OPUS_IN_DROID.md
  - docs/reviews/SW27A_CANON_PUSH_ARTIFACTS_2026_04_26.md
  - en1gma/.factory/
  - en1gma/tests/integration/test_daily_expansion_6_trade_parity.py
  - reports/
  - scratch/sw27_ambiguity_diagnostic/

rule: "No untracked scratch/brief/report artifact was modified or staged."
```

---

## 9. Recommended reconciliation path

```yaml
classification: CASE_B_WITH_MAIN_ALREADY_CONTAINING_PHASE4B_CODE

why_not_cherry_pick_1f23f0a_only: |
  main contains the ratified Phase 4b code commits, but not the feature-only
  walk-forward harness (584309f) or CERTIFICATION_STATE v1.0 commit (cef8fc5).
  The hygiene commit (1f23f0a) depends conceptually and partly textually on
  CERTIFICATION_STATE existing. Cherry-picking only 1f23f0a risks an incomplete
  evidence/control-plane sync.

recommendation: |
  After G approval, merge feature/phase4b-lane-close into main, preserving
  main's existing merge/archive commits and bringing over the feature-only
  walk-forward harness, CERTIFICATION_STATE, and document hygiene sweep.

preferred_shape: |
  Use --no-ff --no-commit, update repo_state/merge_status fields from TBD to
  merged-to-main during the merge, run gates, then create one explicit merge
  commit. If policy prefers pure merge commits, merge first and make the
  repo_state update as a separate docs commit.

conflict_forecast: |
  git merge-tree did not report Git conflict markers for the proposed
  main + feature merge. A full working-tree merge is still required after
  approval before declaring conflict-free.
```

---

## 10. Risks / conflicts

```yaml
risks:
  canon_code_asymmetry:
    status: "current risk on main"
    note: |
      main contains Phase 4b lane-close code, but not the post-walk-forward
      certification doc/hygiene state. Future agents branching from main do
      not receive the clean orientation surface.

  cherry_pick_partial_sync:
    status: "avoid"
    note: |
      Cherry-picking 1f23f0a alone omits cef8fc5 and 584309f. That would
      land doc hygiene without the certification state and supporting harness.

  main_only_commits:
    status: "present"
    note: |
      main has be1f244 and 491b694 not on feature. Merge feature into main,
      not force-push or rebase, to preserve them.

  untracked_artifacts:
    status: "present but unrelated"
    note: "Leave untouched unless G explicitly scopes them."
```

---

## 11. Exact commands for proposed sync after G approval

```bash
# 1. Start clean and current.
git checkout main
git pull --ff-only origin main

# 2. Stage the full feature branch integration without committing yet.
git merge --no-ff --no-commit feature/phase4b-lane-close

# 3. Patch repo_state / merge_status fields only after the merge is real.
# Suggested textual update:
#   merge_status: "merged to main at <merge_commit_or_pending_commit>"
# in CLAUDE.md, docs/canonical/FORWARD_PLAN.md, and docs/canonical/CERTIFICATION_STATE.md.

# 4. Required hygiene gate before committing.
git diff --check
rg "docs/canonical/PHASE_4_RATIFICATION\\.md" CLAUDE.md docs/canonical/FORWARD_PLAN.md docs/canonical/CERTIFICATION_STATE.md
rg "docs/canonical/POST_PHASE_3_ORACLE\\.md" CLAUDE.md docs/canonical/FORWARD_PLAN.md docs/canonical/CERTIFICATION_STATE.md
rg "trade_011" CLAUDE.md docs/canonical/FORWARD_PLAN.md docs/canonical/CERTIFICATION_STATE.md
rg "MSS_NOT_EQUAL_ACTIVE_CONTROL" CLAUDE.md docs/canonical/FORWARD_PLAN.md docs/canonical/CERTIFICATION_STATE.md

# 5. Required code gates because the feature-only walk-forward harness enters main.
lint-imports --config pyproject.toml
mypy en1gma/
# Run the focused chart-truth / ARS parity gates used by the lane close.
# Exact command names should be confirmed from current test layout before execution.

# 6. Commit and push only if gates pass.
git commit -m "merge: Phase 4b certification and canon hygiene"
git push origin main
```

---

## 12. Final verdict

```yaml
verdict: DO_NOT_CHERRY_PICK_1F23F0A_ALONE
recommended_action_after_G_APPROVAL: MERGE_FEATURE_BRANCH_INTO_MAIN
reason: |
  main already contains the Phase 4b code commits, but lacks the feature-only
  walk-forward harness, CERTIFICATION_STATE, and canonical document hygiene
  sweep. A full merge aligns main as the clean future orientation base without
  losing main-only commits.
```
