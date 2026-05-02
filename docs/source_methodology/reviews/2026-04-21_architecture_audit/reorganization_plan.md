# docs/ REORGANIZATION PLAN

```yaml
document: reorganization_plan
version: 0.1 (PROPOSAL — do NOT execute until G ratifies)
date: 2026-04-21
author: Fresh Opus 4.7 (Cursor, v0.2 refinement context)
companion_docs: hierarchy_proposal.md, canonical_updates_needed.md
format: one line per file — source → destination, classification, rationale
rule: |
  This document PROPOSES moves. No git mv runs here. G ratifies first.
  After ratification, execution is a single mechanical pass + canonical
  doc updates (see canonical_updates_needed.md).
```

---

## 1. HOW TO READ THIS PLAN

Each row below declares:

- **source**: current path (relative to `docs/`)
- **destination**: proposed path (relative to `docs/`)
- **action**: `move`, `rename+move`, `archive`, `keep_in_place`, `flag_for_g`
- **class**: canonical | doctrine | reviews | plans | briefs_active | briefs_shipped | handovers | contracts | workshop | findings | archive | ambiguous
- **rationale**: one-line reason

Order mirrors the target tree in `hierarchy_proposal.md`. Execution order does not matter except: create new directories first, move contents, then remove emptied directories.

---

## 2. CANONICAL (tier 1 authority — always current)

| source | destination | action | class | rationale |
|--------|-------------|--------|-------|-----------|
| `NORTH_STAR.md` | `canonical/NORTH_STAR.md` | move | canonical | strategic vision, tier 1 per CLAUDE.md |
| `FORWARD_PLAN.md` | `canonical/FORWARD_PLAN.md` | move | canonical | current roadmap, tier 1 per CLAUDE.md |
| `VAULT.md` | `canonical/VAULT.md` | move | canonical | parked architecture, tier 1 per CLAUDE.md |
| `MAP_SPATIAL_PRIMER_v1.md` | `canonical/MAP_SPATIAL_PRIMER_v1.md` | move | canonical | spatial doctrine, tier 1 per CLAUDE.md (FLAG §5 in hierarchy_proposal.md) |
| `cartridge_contract/CARTRIDGE_CONTRACT.md` | `canonical/CARTRIDGE_CONTRACT.md` | move (on Phase 1 canonicalization) | canonical | tier 1 post-ratification only — until then, stays put |

---

## 3. DOCTRINE (how we work — tier 2)

| source | destination | action | class | rationale |
|--------|-------------|--------|-------|-----------|
| `AGENT_HABITAT.md` | `doctrine/AGENT_HABITAT.md` | move | doctrine | agent habitat contract, process-scope |
| `BRIEF_PATTERN.md` | `doctrine/BRIEF_PATTERN.md` | move | doctrine | canonical brief shape, process-scope |

---

## 4. REVIEWS (fresh-eyes audits, sweeps, external evaluations)

### 2026-04-17 sweep (22-finding multi-model audit)

| source | destination | action | class | rationale |
|--------|-------------|--------|-------|-----------|
| `CTO_BRIEF_2026-04-17.yaml` | `reviews/2026-04-17_sweep/CTO_BRIEF.yaml` | rename+move | reviews | strategic triage from 04-17 sweep |
| `SWEEP_FINDINGS_2026-04-17.yaml` | `reviews/2026-04-17_sweep/SWEEP_FINDINGS.yaml` | rename+move | reviews | full finding detail SW01-SW25 |
| `OPUS_FRESH_LOOK_2026-04-17.md` | `reviews/2026-04-17_sweep/OPUS_FRESH_LOOK.md` | rename+move | reviews | 10 gaps/tensions cross-analysis |

### 2026-04-21 architecture audit (cartridge-architecture fresh eyes)

| source | destination | action | class | rationale |
|--------|-------------|--------|-------|-----------|
| `audit/DESIGN.md` | `reviews/2026-04-21_architecture_audit/DESIGN.md` | move | reviews | first-principles design |
| `audit/COMPARISON.md` | `reviews/2026-04-21_architecture_audit/COMPARISON.md` | move | reviews | design vs en1gma comparison |
| `audit/ORACLE.md` | `reviews/2026-04-21_architecture_audit/ORACLE.md` | move | reviews | current-state snapshot for sprint planning |
| `audit/AUDIT_STREAM_A.md` | `reviews/2026-04-21_architecture_audit/AUDIT_STREAM_A.md` | move | reviews | drift audit stream A |
| `audit/AUDIT_STREAM_B.md` | `reviews/2026-04-21_architecture_audit/AUDIT_STREAM_B.md` | move | reviews | drift audit stream B |
| `audit/hierarchy_proposal.md` | `reviews/2026-04-21_architecture_audit/hierarchy_proposal.md` | move | reviews | this exercise's proposal artifact |
| `audit/reorganization_plan.md` | `reviews/2026-04-21_architecture_audit/reorganization_plan.md` | move | reviews | this exercise's plan artifact |
| `audit/canonical_updates_needed.md` | `reviews/2026-04-21_architecture_audit/canonical_updates_needed.md` | move | reviews | this exercise's updates artifact |

After moves: `docs/audit/` is empty → remove directory.

---

## 5. PLANS (active execution plans)

| source | destination | action | class | rationale |
|--------|-------------|--------|-------|-----------|
| `cartridge_contract/CARTRIDGE_IMPLEMENTATION_DRAFT.md` | `plans/CARTRIDGE_IMPLEMENTATION_DRAFT.md` | move (on Phase 1 canonicalization) | plans | execution plan against canonical contract |
| `build_docs/BLOCK_2_PRIORITIZATION_M3_5_2.md` | `plans/BLOCK_2_PRIORITIZATION_M3_5_2.md` | move | plans | armed-on-shelf Block 2 sequencing |
| `build_docs/BLOCK_2_RIVER_RELIABILITY_M3_5_3.md` | `plans/BLOCK_2_RIVER_RELIABILITY_M3_5_3.md` | move | plans | bundled SW14+SW18+SW26 plan |
| `DUCKDB_INSTALL_PLAN.md` | `plans/DUCKDB_INSTALL_PLAN.md` | move (or archive — flag) | plans | DuckDB MCP install spec (FLAG: status check needed, hierarchy_proposal.md §5) |

After moves: `docs/cartridge_contract/` is empty → remove directory (see FLAG in hierarchy_proposal.md §5).

---

## 6. BRIEFS (per-sprint implementation)

### Active

| source | destination | action | class | rationale |
|--------|-------------|--------|-------|-----------|
| `briefs/REFINEMENT_BRIEF.md` | `briefs/active/REFINEMENT_BRIEF.md` | move | briefs_active | v0.2 cartridge refinement brief (archives to shipped once v0.2 canonicalizes) |

### Shipped (2026-04 bucket)

| source | destination | action | class | rationale |
|--------|-------------|--------|-------|-----------|
| `briefs/BRIEF.M3.5.1.SW01.yaml` | `briefs/shipped/2026-04/BRIEF.M3.5.1.SW01.yaml` | move | briefs_shipped | SW01 PDA mitigation — shipped 2026-04-20 |
| `briefs/BRIEF.M3.5.1.SW04.yaml` | `briefs/shipped/2026-04/BRIEF.M3.5.1.SW04.yaml` | move | briefs_shipped | SW04 PDA direction/zone fidelity — shipped 2026-04-19 |
| `briefs/BRIEF.M3.5.1.SW08.yaml` | `briefs/shipped/2026-04/BRIEF.M3.5.1.SW08.yaml` | move | briefs_shipped | SW08 governance enforcement — shipped 2026-04-19 |
| `briefs/BRIEF.M3.5.1.SW24.yaml` | `briefs/shipped/2026-04/BRIEF.M3.5.1.SW24.yaml` | move | briefs_shipped | SW24 ra_engine tz source-of-truth — shipped 2026-04-19 |

---

## 7. HANDOVERS (CTO handovers, by date)

| source | destination | action | class | rationale |
|--------|-------------|--------|-------|-----------|
| `CTO_HANDOVER_2026_04_17.md` | `handovers/2026-04/2026-04-17_morning.md` | rename+move | handovers | Friday 04-17 morning handover |
| `CTO_HANDOVER_2026_04_17_EVE.md` | `handovers/2026-04/2026-04-17_evening.md` | rename+move | handovers | Friday 04-17 evening handover |
| `CTO_HANDOVER_2026_04_19_EOD.md` | `handovers/2026-04/2026-04-19_eod.md` | rename+move | handovers | Weekend 04-19 EOD handover |

Rationale for rename: normalizing to `<YYYY-MM-DD>_<slug>.md` makes sort order natural and the `_morning` / `_evening` / `_eod` slug carries the same info as the ALL_CAPS variant.

---

## 8. CONTRACTS (shipped contracts)

| source | destination | action | class | rationale |
|--------|-------------|--------|-------|-----------|
| `contracts/SW08_CONTRACT.yaml` | `contracts/SW08_CONTRACT.yaml` | keep_in_place | contracts | already in right folder |

No change needed. Folder is preserved.

---

## 9. WORKSHOP SESSIONS (Olya / strategy sessions)

| source | destination | action | class | rationale |
|--------|-------------|--------|-------|-----------|
| `workshop_sessions/OLYA_SESSION_2026_04_20.md` | `workshop_sessions/2026-04/2026-04-20_olya.md` | rename+move | workshop | date-prefix naming + month bucket |

Rationale for rename: consistent `<YYYY-MM-DD>_<slug>.md` pattern across handovers and workshop sessions.

---

## 10. FINDINGS (registered, not yet fully resolved)

| source | destination | action | class | rationale |
|--------|-------------|--------|-------|-----------|
| `build_docs/SW26_ledger_entry.yaml` | `findings/SW26_ledger_entry.yaml` | move | findings | registered open finding, adjacent to plans that reference it |

---

## 11. ARCHIVE (superseded, pre-M3, fully historical)

### build_briefs (pre-M3 implementation briefs whose features shipped)

| source | destination | action | class | rationale |
|--------|-------------|--------|-------|-----------|
| `build_docs/BRIEF_CHAIN_EVALUATOR.md` | `archive/build_briefs/BRIEF_CHAIN_EVALUATOR.md` | archive | archive | chain evaluator shipped (M1 complete) |
| `build_docs/BRIEF_M3_ADDENDUM.md` | `archive/build_briefs/BRIEF_M3_ADDENDUM.md` | archive | archive | M3 milestone shipped |
| `build_docs/BRIEF_MILESTONE_2_WIRING.md` | `archive/build_briefs/BRIEF_MILESTONE_2_WIRING.md` | archive | archive | M2 wiring shipped |
| `build_docs/BRIEF_MILESTONE_3_DAILY_EXPANSION.md` | `archive/build_briefs/BRIEF_MILESTONE_3_DAILY_EXPANSION.md` | archive | archive | DAILY_EXPANSION YAML shipped |

After moves: `docs/build_docs/` is empty → remove directory.

### scans

| source | destination | action | class | rationale |
|--------|-------------|--------|-------|-----------|
| `scans/discovery_scan_2025_06_2026_03_olya.md` | `archive/scans/discovery_scan_2025_06_2026_03_olya.md` | archive | archive | Q1 2026 discovery scan, reference only |

After moves: `docs/scans/` is empty → remove directory.

### superpowers

| source | destination | action | class | rationale |
|--------|-------------|--------|-------|-----------|
| `superpowers/plans/2026-04-03-gemma-sentinel.md` | `archive/superpowers/2026-04-03-gemma-sentinel.md` | archive | archive | sentinel design doc — implementation shipped and evolved |

After moves: `docs/superpowers/plans/` empty → remove; `docs/superpowers/` empty → remove.

---

## 12. POST-MOVE DIRECTORY STATE

Directories that should exist after execution:

```
docs/archive/
docs/archive/build_briefs/
docs/archive/scans/
docs/archive/superpowers/
docs/briefs/active/
docs/briefs/shipped/2026-04/
docs/canonical/
docs/contracts/
docs/doctrine/
docs/findings/
docs/handovers/2026-04/
docs/plans/
docs/reviews/2026-04-17_sweep/
docs/reviews/2026-04-21_architecture_audit/
docs/workshop_sessions/2026-04/
```

Directories to REMOVE after moves complete:

```
docs/audit/                        # contents moved to reviews/2026-04-21_architecture_audit/
docs/build_docs/                   # contents moved to plans/, findings/, archive/build_briefs/
docs/cartridge_contract/           # contents moved to canonical/ and plans/ (post Phase 1 only)
docs/scans/                        # contents moved to archive/scans/
docs/superpowers/                  # contents moved to archive/superpowers/
docs/superpowers/plans/            # parent already removed
```

Files that stay at `docs/` root: NONE. Every doc file is categorized. `docs/` root contains only subdirectories.

---

## 13. EXECUTION ORDER (post-ratification reference)

When G ratifies, mechanical execution runs in this order. Half-day of work.

1. **Create new directories** — `mkdir -p` all directories in §12.
2. **Move canonical docs** (§2) — `git mv` four files to `canonical/` (contract waits until Phase 1).
3. **Move doctrine docs** (§3).
4. **Move review bundles** (§4) with renames.
5. **Move plans** (§5) — `CARTRIDGE_IMPLEMENTATION_DRAFT.md` waits for Phase 1.
6. **Move briefs** (§6) with active/shipped split.
7. **Move handovers** (§7) with normalized names.
8. **Move workshop session** (§9) with normalized name.
9. **Move findings** (§10).
10. **Move archive items** (§11).
11. **Remove empty directories** (§12 removal list).
12. **Run canonical doc updates** per `canonical_updates_needed.md`.
13. **Verify** — run `git status`, confirm only moves + the canonical-doc edits, no surprise deletions.

Every move preserves git history (`git mv`). No `rm`s.

---

## 14. CONDITIONAL OPERATIONS

Some moves depend on other milestones:

- **CARTRIDGE_CONTRACT.md → `canonical/`**: condition = Phase 1 canonicalization ratified (contract v1.0)
- **CARTRIDGE_IMPLEMENTATION_DRAFT.md → `plans/`**: condition = Phase 1 canonicalization ratified (draft becomes the plan against v1.0)
- **DUCKDB_INSTALL_PLAN.md placement**: condition = status check (see FLAG in hierarchy_proposal.md §5) — if complete, goes to `archive/plans/`; if active, stays in `plans/`
- **REFINEMENT_BRIEF.md → `briefs/shipped/2026-04/`**: condition = v0.2 of contract + implementation draft ratified and second review cycle passed

If G wants to execute the non-conditional moves first, do §§2 (minus contract), 3, 4, 5 (minus cartridge draft), 6, 7, 8, 9, 10, 11 immediately; defer the conditional moves to the corresponding ratification commits.

---

## 15. WHAT THIS PLAN DOES NOT DO

- No content changes to any doc (cross-reference updates live in `canonical_updates_needed.md`)
- No deletions (everything either moves or is archived in-tree)
- No changes to `en1gma/methodology/` or any code directory
- No changes to `/ground_truth/`, `/tests/`, or `/traces/`
- No `.gitignore` or tooling config changes

---

*Plan produced alongside `hierarchy_proposal.md` and `canonical_updates_needed.md`. Execution is single-day mechanical work once ratified.*
