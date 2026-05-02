# CANONICAL UPDATES NEEDED

```yaml
document: canonical_updates_needed
version: 0.1 (PROPOSAL — do NOT execute until G ratifies the hierarchy)
date: 2026-04-21
author: Fresh Opus 4.7 (Cursor, v0.2 refinement context)
companion_docs: hierarchy_proposal.md, reorganization_plan.md
purpose: |
  List the content changes required in canonical docs to absorb:
    1. New paths from the proposed docs/ reorganization
    2. The arrival of CARTRIDGE_CONTRACT.md as a fifth canonical entry
  This is a change LIST, not an execution. All updates land as part of
  Phase 1 canonicalization (for CARTRIDGE_CONTRACT arrivals) or as the
  reorganization commit (for path changes).
rule: |
  No content is updated here. This document tells the operator exactly
  which lines in which files need to change, and why, so the canonical
  updates can ship in tight, reviewable commits.
```

---

## 1. SCOPE

Four canonical docs need updates:

1. `CLAUDE.md` (repo root)
2. `docs/canonical/NORTH_STAR.md` (after move from `docs/NORTH_STAR.md`)
3. `docs/canonical/FORWARD_PLAN.md` (after move from `docs/FORWARD_PLAN.md`)
4. `docs/canonical/VAULT.md` (after move from `docs/VAULT.md`)

No content updates needed in `docs/canonical/MAP_SPATIAL_PRIMER_v1.md` — the primer references methodology docs and nothing in this reorganization changes methodology paths.

---

## 2. UPDATE SET A — ABSORB NEW PATHS (reorganization commit)

This set ships as part of the filesystem reorganization commit (post-G-ratification).

### 2.1 CLAUDE.md (repo root)

**Trigger:** reorganization executes.
**Kind:** `effect: structure` per contract v0.2 §7.
**Changes required:**

- §1 "Document Architecture" block: update `location` field from `"CLAUDE.md at repo root. Others in ~/en1gma/docs/"` to `"CLAUDE.md at repo root. Canonical companions in ~/en1gma/docs/canonical/"`.

- §1 `session_artifacts` block: update every path that moves. Specific lines:
  - `current_weekend_handover: "docs/CTO_HANDOVER_2026_04_19_EOD.md"` → `"docs/handovers/2026-04/2026-04-19_eod.md"`
  - `prior_weekend_handovers.friday_eve: "docs/CTO_HANDOVER_2026_04_17_EVE.md"` → `"docs/handovers/2026-04/2026-04-17_evening.md"`
  - `prior_weekend_handovers.friday_morning: "docs/CTO_HANDOVER_2026_04_17.md"` → `"docs/handovers/2026-04/2026-04-17_morning.md"`
  - `sweep_artifacts_2026_04_17.CTO_BRIEF: "docs/CTO_BRIEF_2026-04-17.yaml"` → `"docs/reviews/2026-04-17_sweep/CTO_BRIEF.yaml"`
  - `sweep_artifacts_2026_04_17.SWEEP_FINDINGS: "docs/SWEEP_FINDINGS_2026-04-17.yaml"` → `"docs/reviews/2026-04-17_sweep/SWEEP_FINDINGS.yaml"`
  - `sweep_artifacts_2026_04_17.FRESH_LOOK: "docs/OPUS_FRESH_LOOK_2026-04-17.md"` → `"docs/reviews/2026-04-17_sweep/OPUS_FRESH_LOOK.md"`
  - `contracts_and_briefs_shipped.SW08_contract: "docs/contracts/SW08_CONTRACT.yaml"` → unchanged (stays in contracts/)
  - `contracts_and_briefs_shipped.SW08_brief: "docs/briefs/BRIEF.M3.5.1.SW08.yaml"` → `"docs/briefs/shipped/2026-04/BRIEF.M3.5.1.SW08.yaml"`
  - `contracts_and_briefs_shipped.SW04_brief: "docs/briefs/BRIEF.M3.5.1.SW04.yaml"` → `"docs/briefs/shipped/2026-04/BRIEF.M3.5.1.SW04.yaml"`
  - `contracts_and_briefs_shipped.SW24_brief: "docs/briefs/BRIEF.M3.5.1.SW24.yaml"` → `"docs/briefs/shipped/2026-04/BRIEF.M3.5.1.SW24.yaml"`
  - `contracts_and_briefs_shipped.SW01_brief: "docs/briefs/BRIEF.M3.5.1.SW01.yaml"` → `"docs/briefs/shipped/2026-04/BRIEF.M3.5.1.SW01.yaml"`
  - `doctrine_and_planning_2026_04_19.AGENT_HABITAT: "docs/AGENT_HABITAT.md"` → `"docs/doctrine/AGENT_HABITAT.md"`
  - `doctrine_and_planning_2026_04_19.BRIEF_PATTERN: "docs/BRIEF_PATTERN.md"` → `"docs/doctrine/BRIEF_PATTERN.md"`
  - `doctrine_and_planning_2026_04_19.DUCKDB_PLAN: "docs/DUCKDB_INSTALL_PLAN.md"` → `"docs/plans/DUCKDB_INSTALL_PLAN.md"` (or archive path — see FLAG)
  - `doctrine_and_planning_2026_04_19.BLOCK_2_PRIO: "docs/build_docs/BLOCK_2_PRIORITIZATION_M3_5_2.md"` → `"docs/plans/BLOCK_2_PRIORITIZATION_M3_5_2.md"`
  - `doctrine_and_planning_2026_04_19.OLYA_SESSION: "docs/workshop_sessions/OLYA_SESSION_2026_04_20.md"` → `"docs/workshop_sessions/2026-04/2026-04-20_olya.md"`
  - `monday_2026_04_20_artifacts.MAP_SPATIAL_PRIMER: "docs/MAP_SPATIAL_PRIMER_v1.md"` → `"docs/canonical/MAP_SPATIAL_PRIMER_v1.md"`
  - `monday_2026_04_20_artifacts.RIVER_RELIABILITY: "docs/build_docs/BLOCK_2_RIVER_RELIABILITY_M3_5_3.md"` → `"docs/plans/BLOCK_2_RIVER_RELIABILITY_M3_5_3.md"`

- §1 `cross_refs` block: update three lines:
  - `strategic_vision: "See docs/NORTH_STAR.md"` → `"See docs/canonical/NORTH_STAR.md"`
  - `current_priorities: "See docs/FORWARD_PLAN.md"` → `"See docs/canonical/FORWARD_PLAN.md"`
  - `parked_architecture: "See docs/VAULT.md"` → `"See docs/canonical/VAULT.md"`

- §1 `canonical_docs` block: no path change yet (these are bare filenames today), but when CARTRIDGE_CONTRACT canonicalizes (Update Set B), it is added here.

- Anywhere in CLAUDE.md that references `docs/build_docs/*` → update to new paths (`docs/plans/*` or `docs/findings/*` per reorganization_plan.md).
- Anywhere in CLAUDE.md that references `docs/audit/*` → update to `docs/reviews/2026-04-21_architecture_audit/*`.

### 2.2 docs/canonical/NORTH_STAR.md (post-move)

**Trigger:** reorganization executes.
**Kind:** `effect: structure`.
**Changes required:**

- Update any `docs/`-prefixed cross-reference to use the new paths from `reorganization_plan.md`. This is a find-and-verify pass — NORTH_STAR currently has few explicit doc paths, but any cross-reference to FORWARD_PLAN.md, VAULT.md, or CLAUDE.md should be sanity-checked.

Action for operator: `rg 'docs/' docs/canonical/NORTH_STAR.md` after move; fix any stale references.

### 2.3 docs/canonical/FORWARD_PLAN.md (post-move)

**Trigger:** reorganization executes.
**Kind:** `effect: structure`.
**Changes required:**

- Any reference to `docs/build_docs/` → `docs/plans/` or `docs/findings/` per reorganization_plan.md §§5, 10, 11
- Any reference to `docs/audit/` → `docs/reviews/2026-04-21_architecture_audit/`
- Any reference to `docs/CTO_HANDOVER_*` → `docs/handovers/2026-04/<renamed>.md`
- Any reference to `docs/briefs/BRIEF.M3.5.1.SW*.yaml` → `docs/briefs/shipped/2026-04/...`
- Any reference to `docs/AGENT_HABITAT.md` / `docs/BRIEF_PATTERN.md` → `docs/doctrine/...`
- Any reference to `docs/MAP_SPATIAL_PRIMER_v1.md` → `docs/canonical/MAP_SPATIAL_PRIMER_v1.md`

Action for operator: `rg 'docs/' docs/canonical/FORWARD_PLAN.md` after move; fix all stale paths. FORWARD_PLAN has many more cross-references than NORTH_STAR; this is the biggest update in Set A.

### 2.4 docs/canonical/VAULT.md (post-move)

**Trigger:** reorganization executes.
**Kind:** `effect: structure`.
**Changes required:**

- Check for any `docs/` cross-references. VAULT is parked-architecture notes; cross-references are likely few.

Action for operator: `rg 'docs/' docs/canonical/VAULT.md` after move; fix any stale references.

---

## 3. UPDATE SET B — ABSORB CARTRIDGE_CONTRACT CANONICALIZATION

This set ships as part of the Phase 1 canonicalization commit (when CARTRIDGE_CONTRACT reaches v1.0 and moves to `docs/canonical/`).

### 3.1 CLAUDE.md (repo root)

**Trigger:** CARTRIDGE_CONTRACT v1.0 ratified.
**Kind:** `effect: structure + methodology` per contract v0.2 §7.
**Changes required:**

- §1 `canonical_docs` block: add fifth entry. Proposed value:
  ```yaml
  CARTRIDGE_CONTRACT.md: "Formal console/cartridge interface — what every
                          change classifies against (scope + effect)"
  ```
- §1 `canonical_docs.location` comment: reconfirm that five canonical docs live at `docs/canonical/`.
- §1 `canonical_docs.rule`: update from `"These 4 documents are the complete orientation surface"` to `"These 5 documents are the complete orientation surface"`.
- Opening orientation paragraph: rewrite to lead with the console/cartridge metaphor, per CARTRIDGE_IMPLEMENTATION_DRAFT v0.2 §3.2. The exact rewrite is not specified here — it is content work that lands in the canonicalization commit.
- §6 INVARIANTS block: add the eleven cartridge-contract invariants (see CARTRIDGE_IMPLEMENTATION_DRAFT v0.2 §3 for the full list including the four new ones from v0.2):
  - INV-CARTRIDGE-PURE-DECLARATION
  - INV-CONSOLE-STRATEGY-BLIND
  - INV-CONSOLE-NO-CARTRIDGE-SHAPED-BRANCHES (new in contract v0.2)
  - INV-NEW-CARTRIDGE-NO-CONSOLE-CHANGE
  - INV-CARTRIDGE-SCHEMA-UNIFIED
  - INV-CANON-RUNTIME-FIXED (new in contract v0.2)
  - INV-TRACE-DETERMINISM-BY-CARTRIDGE (new in contract v0.2)
  - INV-STRUCTURAL-REFACTOR-NO-SEMANTIC-DRIFT (new in contract v0.2)
  - INV-BOUNDARY-CLASSIFIABLE
  - INV-AUTHORITY-BOUNDARY-EXPLICIT
  - INV-RULING-SCOPE-EXPLICIT

### 3.2 docs/canonical/NORTH_STAR.md

**Trigger:** CARTRIDGE_CONTRACT v1.0 ratified.
**Kind:** `effect: methodology`.
**Changes required:**

- Add a paragraph or block referencing the console/cartridge boundary as a first-class architectural principle. The 5-layer spine diagram should be updated to reflect the console/ grouping (per CARTRIDGE_IMPLEMENTATION_DRAFT v0.2 §4.5 — "NORTH_STAR.md: 5-layer spine diagram updated to reflect console/ grouping").

### 3.3 docs/canonical/FORWARD_PLAN.md

**Trigger:** CARTRIDGE_CONTRACT v1.0 ratified.
**Kind:** `effect: workflow + structure`.
**Changes required:**

- Add a section noting that from Phase 1 onward, every brief and ruling declares `scope` + `effect` per contract §7.
- Reference CARTRIDGE_CONTRACT.md as the classification authority for all in-flight items.
- Re-classify existing in-flight items per CARTRIDGE_IMPLEMENTATION_DRAFT v0.2 §3 point 5 (Q3 sweep direction, Q4 OTE body/wick, Q5 F10 4-level OTE, SW27 FVG initial guard, Block 2 remaining).

### 3.4 docs/canonical/VAULT.md

**Trigger:** CARTRIDGE_CONTRACT v1.0 ratified.
**Kind:** `effect: documentation`.
**Changes required:**

- Minor: if any parked-architecture note relates to a capability that is now formally a cartridge schema field (e.g., `sweep_model`, `liquidity_targets`), add a one-line pointer to CARTRIDGE_CONTRACT §3 and its `(v2)` marker status.

### 3.5 docs/canonical/MAP_SPATIAL_PRIMER_v1.md

**Trigger:** CARTRIDGE_CONTRACT v1.0 ratified.
**Kind:** `effect: documentation`.
**Changes required:**

- Possibly none. The primer teaches how to think about the Map; the contract defines the outer boundary. They are complementary. A single cross-reference sentence ("See CARTRIDGE_CONTRACT for the console/cartridge boundary that surrounds the Map") may be useful at the top of §1 or in the header, but this is optional.

---

## 4. WHAT IS NOT IN THIS LIST

Intentional exclusions:

- **Content changes beyond path updates and the canonicalization deltas above.** Rewrites, clarifications, new sections — all out of scope for this exercise.
- **Non-canonical docs** (plans, briefs, handovers, etc.). These may have internal cross-references that go stale after moves, but they are not authority artifacts. Stale cross-references in handovers do not harm fresh-agent onboarding (handovers are explicitly point-in-time). Cross-references in plans/briefs will be updated ad-hoc as those plans/briefs are consulted, or in a follow-up cleanup commit.
- **`en1gma/methodology/` changes.** Out of scope per task 2 constraints.
- **Code-side docstrings or README updates.** Out of scope.
- **`pyproject.toml`, `.gitignore`, CI config updates.** Out of scope.
- **CARTRIDGE_CONTRACT.md itself.** Its content is authored in the refinement brief cycle (v0.1 → v0.2 → v1.0); canonicalization is a status change, not a content edit.

---

## 5. COMMIT SEQUENCING (post-ratification reference)

Two distinct commits, two distinct triggers:

### Commit 1 — Reorganization (Set A)

Triggered by: G ratifies hierarchy_proposal.md + reorganization_plan.md.

Scope: file moves per `reorganization_plan.md` §§2-11, plus path updates in:
- `CLAUDE.md` (per §2.1 above)
- `docs/canonical/NORTH_STAR.md` (per §2.2)
- `docs/canonical/FORWARD_PLAN.md` (per §2.3)
- `docs/canonical/VAULT.md` (per §2.4)

Effort: ~0.5 day of mechanical work + grep-verify pass.

### Commit 2 — Cartridge canonicalization (Set B)

Triggered by: CARTRIDGE_CONTRACT v1.0 ratified (post second-review cycle).

Scope: move `CARTRIDGE_CONTRACT.md` to `docs/canonical/`; move `CARTRIDGE_IMPLEMENTATION_DRAFT.md` to `docs/plans/`; remove `docs/cartridge_contract/`; plus content updates in:
- `CLAUDE.md` (per §3.1 above — orientation rewrite, canonical_docs expansion, invariants registered)
- `docs/canonical/NORTH_STAR.md` (per §3.2 — console/cartridge principle, spine diagram)
- `docs/canonical/FORWARD_PLAN.md` (per §3.3 — scope+effect declaration, classification of in-flight items)
- `docs/canonical/VAULT.md` (per §3.4 — optional pointers to `(v2)` fields)
- `docs/canonical/MAP_SPATIAL_PRIMER_v1.md` (per §3.5 — optional cross-reference)

Effort: ~1 day of content work + review.

These two commits are sequential by trigger, not by dependency. Commit 1 can land before Commit 2 is scoped. If the order reverses (canonicalization lands first), Commit 2's path updates must anticipate the pre-reorganization paths — cleaner to land Commit 1 first.

---

## 6. VERIFICATION

After each commit, the operator should be able to run:

```
# After Commit 1:
rg 'docs/(NORTH_STAR|FORWARD_PLAN|VAULT|MAP_SPATIAL_PRIMER_v1|AGENT_HABITAT|BRIEF_PATTERN|CTO_HANDOVER|CTO_BRIEF_2026|SWEEP_FINDINGS_2026|OPUS_FRESH_LOOK_2026|DUCKDB_INSTALL_PLAN)\.md' CLAUDE.md docs/canonical/
# → should return ZERO hits with old paths (excluding intentional history references)

# After Commit 2:
rg 'CARTRIDGE_CONTRACT' CLAUDE.md docs/canonical/
# → should return hits in canonical_docs, invariant blocks, and cross-refs
```

Both checks are cheap and produce a clear pass/fail signal on whether the canonical surface absorbed the changes cleanly.

---

*Updates list produced alongside `hierarchy_proposal.md` and `reorganization_plan.md`. Nothing is executed here. G ratifies, then the two commits above ship the changes in reviewable slices.*
