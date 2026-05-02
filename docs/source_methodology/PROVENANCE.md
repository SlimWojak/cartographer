# Source methodology — provenance

All files under `docs/source_methodology/` are **verbatim snapshots** copied
from the en1gma repository. They are intentionally **byte-identical** to the
upstream source so an agent can diff cleanly and trust the content.

| Field | Value |
| --- | --- |
| Source repo | `git@github.com:SlimWojak/en1gma.git` |
| Source SHA | `7202a5c4edcff04976295fa5aef7e7116f1e88e7` |
| Source branch | `main` |
| Snapshot date | 2026-05-02 |
| File count | 95 |

## Tree

| Cartographer path | Source path in en1gma |
| --- | --- |
| `root/CLAUDE.md` | `CLAUDE.md` |
| `root/calibration_results.yaml` | `calibration_results.yaml` |
| `canonical/` | `docs/canonical/` |
| `methodology/` | `en1gma/methodology/` |
| `reviews/` | `docs/reviews/` |
| `handovers/` | `docs/handovers/` |

## Hard rules

1. **Do not edit these files.** They are a snapshot, not a working copy. If you
   want to change methodology, that change must happen in en1gma, be ratified,
   and a new snapshot pulled here.
2. **Do not treat these files as cartographer-authored.** They represent
   en1gma's authority, not cartographer's.
3. **Do not push cartographer-derived content back into the same paths.**
   Cartographer outputs live in `scene_bank/`, `reports/`, and the
   `cartographer/` source package — never in `docs/source_methodology/`.

## To refresh

```bash
# from cartographer repo root
rm -rf docs/source_methodology en1gma-ref
git clone --depth 1 git@github.com:SlimWojak/en1gma.git en1gma-ref
( cd en1gma-ref && git remote remove origin )
mkdir -p docs/source_methodology/{root,canonical,methodology,reviews,handovers}
cp en1gma-ref/CLAUDE.md docs/source_methodology/root/
cp en1gma-ref/calibration_results.yaml docs/source_methodology/root/
cp -R en1gma-ref/docs/canonical/.   docs/source_methodology/canonical/
cp -R en1gma-ref/en1gma/methodology/. docs/source_methodology/methodology/
cp -R en1gma-ref/docs/reviews/.     docs/source_methodology/reviews/
cp -R en1gma-ref/docs/handovers/.   docs/source_methodology/handovers/
# update this file's SHA + snapshot_date
```

## Key entry points (orientation reading order)

For an agent new to en1gma's HTF logic:

1. `root/CLAUDE.md` — what en1gma is, current architecture, invariants
2. `canonical/MAP_SPATIAL_PRIMER_v1.md` — the HTF map concept, in depth
3. `canonical/NORTH_STAR.md` — strategic vision, two-clock model
4. `canonical/FORWARD_PLAN.md` — current sprint state
5. `methodology/METHODOLOGY_INDEX.md` — index of all methodology docs
6. `methodology/SYNTHETIC_OLYA_METHOD_vLOCK.yaml` — 13 L1 primitives
7. `methodology/STATE_DETECTION_LOGIC_v2.yaml` — HTF phase classifier
8. `root/calibration_results.yaml` — 27 Olya answers for the Map engine
9. `reviews/PHASE_5_C2_OLYA_METHODOLOGY_DIGEST_2026_04_30.md` — current Olya methodology summary
10. `reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md` — directly relevant to V0 heuristic #1

The handovers folder gives recent operational context; reviews contains the
running advisor / Olya conversation.
