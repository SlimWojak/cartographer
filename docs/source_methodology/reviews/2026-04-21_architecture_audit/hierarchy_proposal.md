# docs/ HIERARCHY PROPOSAL

```yaml
document: hierarchy_proposal
version: 0.1 (PROPOSAL — G ratification required before any filesystem change)
date: 2026-04-21
author: Fresh Opus 4.7 (Cursor, v0.2 refinement context)
companion_docs: reorganization_plan.md, canonical_updates_needed.md
scope: docs/ only. /ground_truth/, /tests/, /methodology/, and code directories are out of scope.
rule: |
  This is a PROPOSAL. No moves, renames, or deletions are executed here.
  G ratifies the target tree before any mechanical reorganization runs.
```

---

## 1. WHY THIS PROPOSAL

en1gma is entering the cartridge-architecture execution phase (Phase 1 canonicalization of CARTRIDGE_CONTRACT; Phase 2/2.5/3 structural work). A fresh agent landing in the project today cannot quickly distinguish between:

- canonical authority (always current, tier 1)
- locked methodology reference (read-only)
- active execution plans (in-flight)
- per-sprint implementation briefs (scoped)
- historical handovers and sweeps (archival)
- superseded build briefs (archive or delete)

The current `docs/` has real content, but the hierarchy does not teach status. Fifteen files sit flat at the top level alongside nine subfolders with mixed authority tiers. The test for a fresh agent tomorrow — "does this doc influence the work I'm about to do?" — has no structural answer.

This proposal reshapes `docs/` so that directory membership **is** the answer.

---

## 2. TARGET TREE (proposed)

```
docs/
├── canonical/                      # Tier 1 authority — always current
│   ├── NORTH_STAR.md
│   ├── FORWARD_PLAN.md
│   ├── VAULT.md
│   ├── MAP_SPATIAL_PRIMER_v1.md
│   └── CARTRIDGE_CONTRACT.md       # post Phase 1 canonicalization
│
├── doctrine/                       # How we work — supporting canonical
│   ├── AGENT_HABITAT.md
│   └── BRIEF_PATTERN.md
│
├── reviews/                        # Fresh-eyes audits, sweeps, external reviews
│   ├── 2026-04-17_sweep/
│   │   ├── CTO_BRIEF.yaml
│   │   ├── SWEEP_FINDINGS.yaml
│   │   └── OPUS_FRESH_LOOK.md
│   └── 2026-04-21_architecture_audit/
│       ├── DESIGN.md
│       ├── COMPARISON.md
│       ├── ORACLE.md
│       ├── AUDIT_STREAM_A.md
│       └── AUDIT_STREAM_B.md
│
├── plans/                          # Active execution plans
│   ├── CARTRIDGE_IMPLEMENTATION_DRAFT.md
│   ├── BLOCK_2_PRIORITIZATION_M3_5_2.md
│   ├── BLOCK_2_RIVER_RELIABILITY_M3_5_3.md
│   └── DUCKDB_INSTALL_PLAN.md
│
├── briefs/                         # Per-sprint implementation briefs
│   ├── active/
│   │   └── REFINEMENT_BRIEF.md     # (archived once v0.2 canonicalizes)
│   └── shipped/
│       └── 2026-04/
│           ├── BRIEF.M3.5.1.SW01.yaml
│           ├── BRIEF.M3.5.1.SW04.yaml
│           ├── BRIEF.M3.5.1.SW08.yaml
│           └── BRIEF.M3.5.1.SW24.yaml
│
├── handovers/                      # CTO handovers, by date
│   └── 2026-04/
│       ├── 2026-04-17_morning.md
│       ├── 2026-04-17_evening.md
│       └── 2026-04-19_eod.md
│
├── contracts/                      # Shipped contracts
│   └── SW08_CONTRACT.yaml
│
├── workshop_sessions/              # Olya / strategy sessions, dated
│   └── 2026-04/
│       └── 2026-04-20_olya.md
│
├── findings/                       # Registered findings not yet fully resolved
│   └── SW26_ledger_entry.yaml
│
└── archive/                        # Superseded, pre-M3, or fully historical
    ├── build_briefs/
    │   ├── BRIEF_CHAIN_EVALUATOR.md
    │   ├── BRIEF_M3_ADDENDUM.md
    │   ├── BRIEF_MILESTONE_2_WIRING.md
    │   └── BRIEF_MILESTONE_3_DAILY_EXPANSION.md
    ├── scans/
    │   └── discovery_scan_2025_06_2026_03_olya.md
    └── superpowers/
        └── 2026-04-03-gemma-sentinel.md
```

---

## 3. CATEGORY RATIONALE

### `canonical/` — Tier 1 authority, always current

Five documents that every fresh agent reads before doing anything. Authority tier 1. Updated when the system changes; never archived.

- **NORTH_STAR.md** — strategic vision, two-clock model, top-level architecture
- **FORWARD_PLAN.md** — current roadmap, priorities, in-flight work
- **VAULT.md** — parked ideas and proven architecture
- **MAP_SPATIAL_PRIMER_v1.md** — locked spatial doctrine (tier 1 per CLAUDE.md)
- **CARTRIDGE_CONTRACT.md** — once Phase 1 canonicalizes it (post v1.0)

Rationale: today these are scattered across `docs/` and `docs/cartridge_contract/`. A fresh agent has to read CLAUDE.md to discover which docs are canonical. Placing the five in one prominent folder makes "what must I read?" answerable by `ls docs/canonical/`.

Note: CLAUDE.md stays at repo root — it is the entry point and serves as the index into `canonical/`.

### `doctrine/` — How we work

Authority tier 2. Supports canonical by prescribing process. Updated when working conventions change.

- **AGENT_HABITAT.md** — how agents live in the kernel (tools, data, authority)
- **BRIEF_PATTERN.md** — canonical brief shape for agent-executed work

Rationale: these are neither strategic vision nor active execution. They are the rules of the workshop. Separating them prevents them from cluttering canonical and prevents them from getting lost in plans.

### `reviews/` — Fresh-eyes audits and sweeps

External or independent evaluations of the system. Timestamped and grouped by sweep. Archival once superseded but valuable as historical reference.

- **2026-04-17_sweep/** — the 22-finding multi-model audit (Opus + GPT)
- **2026-04-21_architecture_audit/** — the cartridge-architecture fresh-eyes audit (DESIGN, COMPARISON, ORACLE, STREAM_A, STREAM_B)

Rationale: audits come in bundles of related documents. Keeping the bundle together by date preserves context. Flat top-level placement loses that grouping. Today's `docs/audit/` already uses this pattern — extend it and give the 2026-04-17 sweep the same treatment.

### `plans/` — Active execution plans

Multi-document plans driving current or near-term work. Each plan may span multiple sprints. Each has a clear lifecycle: active → superseded → archive.

- **CARTRIDGE_IMPLEMENTATION_DRAFT.md** — post-Phase-1, this is the execution plan
- **BLOCK_2_PRIORITIZATION_M3_5_2.md** — armed-on-shelf Block 2 sequencing
- **BLOCK_2_RIVER_RELIABILITY_M3_5_3.md** — bundled SW14+SW18+SW26 plan
- **DUCKDB_INSTALL_PLAN.md** — M3 DuckDB MCP install spec

Rationale: plans have longer lives than briefs but shorter than canonical. A fresh agent asking "what is actively being worked on?" reads `plans/`. Each plan names its own exit state — it either becomes archive or becomes canonical (rare).

### `briefs/` — Per-sprint implementation briefs

The unit of agent-executed work. Organized by lifecycle (active vs shipped) and by date.

- **briefs/active/** — briefs currently being implemented or under review
- **briefs/shipped/2026-04/** — briefs that delivered their work, kept for audit trail

Rationale: flat `docs/briefs/` already exists. Introducing `active/` and `shipped/<YYYY-MM>/` subfolders preserves the existing pattern while teaching lifecycle. A fresh agent glancing at `briefs/active/` sees "what is in flight right now." Shipped briefs by month prevent unbounded accumulation.

### `handovers/` — CTO handovers

Point-in-time snapshots produced when context is handed between sessions. Organized by date.

- **handovers/2026-04/** — all April 2026 handovers

Rationale: handovers are inherently historical artifacts — a handover from three weeks ago is not canonical, but it may be the most concise summary of what happened in a given window. Dating them and bucketing by month makes it easy to scan "what was the kernel state on date X?"

### `contracts/` — Shipped contracts

Invariant-defining contract documents that have been ratified and shipped. Minimal folder today; grows as more contracts ship.

- **SW08_CONTRACT.yaml** — governance enforcement contract

Rationale: already exists as `docs/contracts/`. Preserve verbatim. When CARTRIDGE_CONTRACT.md canonicalizes, its ratification commit may want to leave a reference contract here too — flagged as ambiguity (see §5).

### `workshop_sessions/` — Olya / strategy sessions

Session notes from F2F methodology work. Timestamped and bucketed by month.

- **workshop_sessions/2026-04/** — April 2026 sessions

Rationale: these are historical artifacts but methodologically valuable. Dating them keeps them findable. Already exists as `docs/workshop_sessions/`; add month bucketing when volume grows.

### `findings/` — Registered findings not yet fully resolved

Individual finding ledger entries that describe a known issue or pending fix. Adjacent to `plans/` (plans reference them) but separate (findings are facts; plans are intentions).

- **SW26_ledger_entry.yaml** — registered Sentinel heartbeat finding

Rationale: today `SW26_ledger_entry.yaml` sits in `build_docs/` alongside obsolete milestone briefs. Separating lifts it out of archive-adjacent noise and gives it a natural home next to the plans that may consume it.

### `archive/` — Superseded, pre-M3, or fully historical

Documents that no longer drive work. Kept in-tree for context; git history would preserve them if deleted, but explicit archive-by-category makes intent legible.

- **archive/build_briefs/** — pre-M3 implementation briefs whose features have shipped
- **archive/scans/** — discovery scan from Q1 2026
- **archive/superpowers/** — sentinel design doc from the Gemma era (implementation shipped)

Rationale: distinguishing archive-by-category from deletion preserves history for future fresh-eyes reviews. The test is inverted: if a doc is referenced by any active plan, canonical, or brief, it is not archive.

---

## 4. THE TEST FOR ANY DOC

Applied to every file in the proposed tree:

```
1. Does a fresh agent tomorrow need this to DO their work?
   Yes → canonical/ or doctrine/ or plans/ or briefs/active/
   No  → continue

2. Is this a reference they may want to consult?
   Yes, methodology reference            → (stays at en1gma/methodology/)
   Yes, historical audit of the system   → reviews/
   Yes, past sprint record               → briefs/shipped/, handovers/, workshop_sessions/
   Yes, registered open issue            → findings/
   No, superseded or completed           → archive/

3. Does nothing reference it and is it superseded?
   Yes → flag for deletion proposal (git preserves it)
```

Applied here: none in this proposal are marked for deletion. `archive/` is sufficient for this pass; deletion can be a subsequent cleanup.

---

## 5. AMBIGUITIES FLAGGED FOR G

Items where canonical status is unclear or where the classification depends on upcoming decisions. Not resolved here.

- **`FLAG_FOR_G`: MAP_SPATIAL_PRIMER_v1.md placement.** Currently at `docs/` root; CLAUDE.md marks it tier 1. Proposed home: `canonical/`. Alternative: it is methodology-reference-style and could live at `en1gma/methodology/` near other locked methodology. Proposal defaults to `canonical/` because its authority is architectural, not algorithmic, and because CLAUDE.md already treats it as canonical.

- **`FLAG_FOR_G`: CARTRIDGE_CONTRACT.md placement.** Today at `docs/cartridge_contract/CARTRIDGE_CONTRACT.md` (alongside the implementation draft). Post-Phase-1 canonicalization, proposal moves it to `canonical/`. Until then, it remains in its current folder. The `canonical_updates_needed.md` companion tracks the move trigger.

- **`FLAG_FOR_G`: DUCKDB_INSTALL_PLAN.md status.** Written 2026-04-19 as a plan awaiting COO execution. Is it still in flight, complete, or deferred? If complete, move to `archive/plans/`. If in flight, leave in `plans/`. Needs a single-line status check before finalization.

- **`FLAG_FOR_G`: `docs/cartridge_contract/` disposition.** After Phase 1 canonicalization, CARTRIDGE_CONTRACT.md moves to `canonical/` and CARTRIDGE_IMPLEMENTATION_DRAFT.md moves to `plans/`. The folder itself is then empty. Proposal: remove the folder in the same commit that canonicalizes the contract.

- **`FLAG_FOR_G`: SW26_ledger_entry vs plans.** SW26 is in the BLOCK_2_RIVER_RELIABILITY_M3_5_3 bundle. The ledger entry describes the finding; the plan describes the remediation approach. Keeping ledger entries under `findings/` and remediation plans under `plans/` splits a naturally-linked pair. Alternative: put all finding-and-plan pairs together under `plans/`. Proposal keeps them separated because findings outlive any particular plan.

- **`FLAG_FOR_G`: Does `methodology/` stay at `en1gma/methodology/`?** Task 2 is scoped to `docs/` only; `en1gma/methodology/` is code-adjacent and out of scope for this pass. Flagged so G knows it was considered. If Phase 2 of the cartridge refactor moves `en1gma/methodology/` into `console/methodology/` or similar, `docs/` ordering is unaffected.

---

## 6. WHAT THIS PROPOSAL DOES NOT DO

Explicit non-goals, per task 2 constraints:

- No reorganization of `/ground_truth/`, `/tests/`, or any code directory
- No content changes to any doc (header updates, cross-reference fixes, rewrites — all out of scope)
- No filesystem operations (see `reorganization_plan.md` for the plan)
- No resolution of flagged ambiguities — G ratifies before execution
- No changes to `en1gma/methodology/` (code-adjacent, out of scope)

---

## 7. PRINCIPLES SATISFIED

Each proposal principle from task 2 is satisfied:

- **Fresh-agent test**: a fresh agent lands, sees `canonical/` + `doctrine/` + `plans/` + `briefs/active/`, reads those, and is oriented. Everything else is marked historical by directory membership.
- **Authority-tier preservation**: tier 1 (`canonical/`) and tier 2 (`doctrine/`) are at the top of the listing; tier 3+ (reviews, plans, briefs, handovers) are below.
- **Ambiguity flagged**: §5 lists every doc whose classification depends on a decision not yet made.
- **Per-sprint organization**: `briefs/shipped/<YYYY-MM>/`, `handovers/<YYYY-MM>/`, `workshop_sessions/<YYYY-MM>/`, `reviews/<date>_<slug>/` all use date-based organization instead of flat directories.
- **Scope discipline**: nothing outside `docs/` is touched.

---

*Proposal produced alongside `reorganization_plan.md` and `canonical_updates_needed.md`. G ratifies the target tree; reorganization is a half-day of mechanical work once ratified.*
