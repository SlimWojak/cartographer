# Cartographer

> *Cartographer prepares the terrain; Olya names the truth.*

A read-only HTF candidate-scene mining tool for EURUSD, built to make Olya's
discretionary chart-review time more surgical. The system proposes candidate
scenes; **Olya is the only labeler of truth.**

This is a **lab fork** — fully isolated from `~/en1gma` and `~/phoenix-river`.
Outputs do not flow back to en1gma without explicit human ratification.

---

## What's in this repo

```
cartographer_concept_board.md          ← Source-of-authority concept (G + advisor)
CARTOGRAPHER_V0_MISSION_BRIEF.md       ← Formal brief for the build mission
MISSION_INPUTS.md                      ← Index of everything the build agent needs
data/cartographer.duckdb               ← Frozen 1m EURUSD snapshot (2020-11 → 2026-04)
data/README.md                         ← Data provenance + schema
docs/source_methodology/               ← Read-only en1gma methodology snapshot
en1gma-ref/                            ← Pinned read-only clone of en1gma @ 7202a5c
cartographer/                          ← Source package (empty — mission fills)
scene_bank/                            ← Candidate / reviewed / rejected scenes
reports/                               ← Weekly summaries + experiment outputs
notebooks/                             ← Exploratory work
```

## Hard rules

1. **Candidate-only.** Cartographer never asserts methodology truth.
2. **Olya labels.** The system flags candidates; Olya names what's real.
3. **No writes outside `~/cartographer/`.** `~/en1gma` and `~/phoenix-river` are off-limits.
4. **No automatic methodology mutation.** Heuristic updates require human ratification.
5. **No trade signals, ever.** This is a research/review tool, not a strategy.

## Seeding (after a fresh clone)

Two artifacts are gitignored to keep the GitHub repo lean. Regenerate them
locally before running anything:

```bash
# 1. Build the EURUSD DuckDB snapshot from ~/phoenix-river/ (M3 only).
python scripts/seed_data.py
# → data/cartographer.duckdb (~220 MB, 2M 1m bars, 2020-11 → 2026-04)

# 2. Reclone en1gma at the SHA pinned in PROVENANCE.md, strip remote.
bash scripts/seed_en1gma_ref.sh
# → en1gma-ref/ (~24 MB, no .git, .READ_ONLY_SNAPSHOT marker)
```

`seed_data.py` requires `~/phoenix-river/EURUSD/` to exist locally. On a
machine without it, copy the `.duckdb` file in directly from M3.

## Status

- **2026-05-02** — Repo scaffolded. Concept doc + methodology snapshot in place.
  Awaiting DROID V0 build mission. Olya/advisor review of brief pending.

## How to run (after V0 build)

The mission will populate `cartographer/` with the scan engine and add
run instructions here. Until then, this repo is a scaffold only.
