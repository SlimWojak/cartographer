# Mission inputs — what the build agent has to work with

This file is the index. The brief (`CARTOGRAPHER_V0_MISSION_BRIEF.md`) is the
contract. Both should be read together.

## Source-of-authority documents (read first)

| Document | Path | Why |
| --- | --- | --- |
| Concept board | `cartographer_concept_board.md` | The original idea + advisor framing. North star: "candidate-only, not truth engine." |
| V0 mission brief | `CARTOGRAPHER_V0_MISSION_BRIEF.md` | What you're being asked to build. Hard rules and deliverables. |
| en1gma orientation | `docs/source_methodology/root/CLAUDE.md` | What en1gma is. Cartographer must not interfere with it. |
| HTF Map primer | `docs/source_methodology/canonical/MAP_SPATIAL_PRIMER_v1.md` | The HTF map concept in depth. Required reading to understand candidate types. |
| Methodology index | `docs/source_methodology/methodology/METHODOLOGY_INDEX.md` | Map to the full methodology corpus. |
| Olya methodology digest | `docs/source_methodology/reviews/PHASE_5_C2_OLYA_METHODOLOGY_DIGEST_2026_04_30.md` | Current state of the methodology conversation with Olya. |
| WP2 strong-close-through gap report | `docs/source_methodology/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md` | Directly relevant to V0 heuristic #1. |
| Calibration results | `docs/source_methodology/root/calibration_results.yaml` | 27 Olya answers — informs heuristic parameter defaults. |

## Data

| Artifact | Path | Notes |
| --- | --- | --- |
| Frozen 1m EURUSD | `data/cartographer.duckdb` | Tables `bars_1m`, view `bars_daily`, table `meta`. Open `read_only=True`. |
| Data README + schema | `data/README.md` | Field-by-field schema, access pattern. |

## Reference clone

| Path | Notes |
| --- | --- |
| `en1gma-ref/` | Full en1gma snapshot at SHA `7202a5c4...`. Remote stripped — no fetch/push possible. Use for: looking up code patterns, understanding existing detector implementations. **Do not import as a Python package.** |
| `en1gma-ref/.READ_ONLY_SNAPSHOT` | Marker file; presence asserts read-only intent. |

## Output destinations

| Path | What goes here |
| --- | --- |
| `cartographer/heuristics/` | One Python module per heuristic. Pure functions, deterministic. |
| `cartographer/scans/` | Loop runner, scan-by-week / scan-by-range entry points. |
| `cartographer/scene_store/` | Scene record dataclass + read/write helpers. |
| `cartographer/reports/` | Report generators (markdown / yaml). |
| `scene_bank/candidates/` | One YAML file per candidate scene (deterministic id-based filename). |
| `scene_bank/reviewed/` | Olya-ratified scenes (V0 leaves this empty — feedback loop is V0.2). |
| `scene_bank/rejected/` | Olya-rejected scenes (V0 leaves this empty). |
| `reports/weekly/` | One markdown summary per scanned week. |
| `reports/experiments/` | Ad-hoc reports — including the V0 Olya review pack. |
| `notebooks/` | Exploratory notebooks. Not part of the deterministic loop. |

## Forbidden destinations

| Path | Why |
| --- | --- |
| `~/en1gma/**` | Production system. Off-limits. |
| `~/phoenix-river/**` | Live data pipeline. Off-limits. |
| `cartographer/en1gma-ref/**` | Read-only snapshot. Editing breaks provenance. |
| `cartographer/docs/source_methodology/**` | Verbatim snapshot. Editing breaks PROVENANCE.md guarantee. |

## Local model endpoints (for the runtime split — see brief §5)

| Model | Endpoint | Use |
| --- | --- | --- |
| Qwen3.6-35B-A3B-4bit | `http://localhost:8090/v1` (mlx-lm, OpenAI-compatible) | Default cartographer runtime LLM (24/7 operation) |
| Frontier (Opus / GPT) | via Droid CLI or API | Build-time model; optional adjudication tier |
| DeepSeek / GLM API | TBD | Alternative runtime if local model insufficient |

The build agent **must** make the LLM backend pluggable so the runtime can be
swapped without code changes (env var or config). See brief §5.
