# Cartographer V0 — DROID Mission Brief

| Field | Value |
| --- | --- |
| Version | v0.1 — DRAFT pending Olya + advisor review |
| Date drafted | 2026-05-02 |
| Drafted by | COO (Claude Code, M3) |
| Build agent | Frontier (Opus / GPT) via Droid `exec` |
| Runtime agent (post-build) | Local model (Qwen3.6 / GLM) — see §5 |
| Working directory | `~/cartographer/` |
| Target completion | 48 hours of build-agent wall time |
| Authority lineage | en1gma SHA `7202a5c4` (lab fork; no merge-back without ratification) |

---

## §0. North star

> **Cartographer prepares the terrain; Olya names the truth.**

Olya's HTF map intelligence is the bottleneck. Today, calibrating an HTF rule
means asking Olya "share an example of X" and waiting while she sifts charts.
Cartographer flips the burden: the machine sweeps history, surfaces *candidate*
scenes for a given heuristic, and Olya verifies — *"yes, exactly that"* /
*"no, that one's a near-miss because…"*.

The output is **never** ground truth. The output is a **review queue**.

---

## §1. Mission

Build a read-only candidate-scene mining tool for **EURUSD Daily HTF logic**,
fed by a frozen 6-year DuckDB snapshot, that produces a reviewable atlas of
candidate market scenes for Olya. V0 covers **8–12 weeks of EURUSD Daily**
across **four heuristics**.

The pain point being solved:

> "Olya, can you share an example of a strong close-through?"
> "…give me a moment, I'll go find one."

Cartographer's V0 success criterion is that Olya can instead say:

> "Show me your top 5 strong-close-through candidates for the last 8 weeks."

…and get a curated review pack with chart context, machine reasoning, and a
yes/no/near-miss form to fill in.

---

## §2. Hard rules (non-negotiable)

These rules apply to **every line of code, every output, every commit**.

| # | Rule | Why |
| - | --- | --- |
| H1 | **Candidate-only output.** Every scene record carries `review_status: pending_review`. No field anywhere claims "true" / "valid" / "signal". | Olya is the only labeler. |
| H2 | **No writes outside `~/cartographer/`.** | This is a sandboxed lab. en1gma and phoenix-river are off-limits. |
| H3 | **No methodology authoring.** Heuristics are an *interpretation* of methodology, not new methodology. The interpretation is explicit and parameterised. | en1gma owns methodology. Cartographer interprets it for example-finding. |
| H4 | **No automatic heuristic mutation.** Olya feedback is collected (V0.2), proposed heuristic deltas require human ratification. | Prevents heuristic drift away from Olya's actual logic. |
| H5 | **No trade signals, no certification claims, no producer outputs.** | Cartographer is a research/review tool, not a strategy. |
| H6 | **Deterministic and resumable.** Same inputs → byte-identical outputs. Resuming a partial scan never duplicates work. | Lets Olya trust that she's not seeing different scenes on different runs. |
| H7 | **Read-only against the DuckDB.** The scan loop opens `cartographer.duckdb` with `read_only=True`. Scene outputs go to `scene_bank/`, never back into the DB. | Snapshot integrity. |
| H8 | **Offline by default.** No network calls in the scan loop. LLM calls (if used) go through one explicit module so they can be disabled or swapped. | Lets the runtime sit on a local model with no API egress. |

If any rule conflicts with a deliverable, **the rule wins** — flag it and stop.

---

## §3. Deliverables (V0)

### 3.1 Code

| Path | What |
| --- | --- |
| `cartographer/heuristics/<name>.py` | One module per heuristic — pure functions, deterministic, parameters from YAML. |
| `cartographer/heuristics/registry.py` | Loads heuristic configs, validates, version-stamps. |
| `cartographer/scene_store/schema.py` | `CandidateScene` dataclass — see §6. |
| `cartographer/scene_store/io.py` | YAML read/write, deterministic filename per scene_id. |
| `cartographer/scans/engine.py` | Core loop — scan window → run heuristics → emit scenes. |
| `cartographer/scans/run_week.py` | CLI: scan one ISO week. |
| `cartographer/scans/run_range.py` | CLI: scan a date range. Idempotent. |
| `cartographer/reports/weekly.py` | Generate `reports/weekly/<date>.md`. |
| `cartographer/reports/review_pack.py` | Generate the Olya review pack (see §3.3). |
| `cartographer/llm/backend.py` | LLM abstraction — see §5. Default backend: `none` (deterministic only). |

### 3.2 Documents (authored by build agent)

| Path | Content |
| --- | --- |
| `CANDIDATE_ONLY_CONTRACT.md` | Formal restatement of the H1–H8 rules + commit-time check list. |
| `HEURISTIC_REGISTRY.md` | One section per V0 heuristic: id, version, rule prose, parameters, what it does NOT claim. |
| `SCENE_SCHEMA.yaml` | Authoritative schema for a candidate scene record (machine-readable). |
| `TESTING.md` | How to verify determinism, how to run a sanity scan, what "passing" means. |
| `RUNTIME.md` | How to swap LLM backends (none / local Qwen / DeepSeek-API / frontier). |

### 3.3 Generated artifacts (V0 run output)

| Path | Content |
| --- | --- |
| `scene_bank/candidates/<scene_id>.yaml` | One file per candidate. Deterministic filename (hash of inputs). |
| `reports/weekly/<YYYY-Www>.md` | Per-week markdown summary, grouped by candidate type, max 5 per type per week. |
| `reports/weekly/INDEX.md` | Master index of all weeks scanned. |
| `reports/experiments/V0_OLYA_REVIEW_PACK_<date>.md` | The deliverable for Olya: top candidates per type across the V0 window, with chart context, machine reasoning, and a verification slot. |
| `reports/experiments/V0_NOTES.md` | Build agent's own notes — noisiest heuristic, false-positive patterns, suggested next heuristics, anything Olya should know before reviewing. |

---

## §4. V0 heuristics

All four are **candidate-only** and emit `review_status: pending_review`.
Parameter values below are **starting points** — the build agent should set
them by reading the methodology corpus, not by guessing.

### 4.1 `strong_close_through_candidate` (priority: high)

Daily candle that closes beyond a candidate HTF level/zone with a clear,
non-marginal break.

Required signal features:
- Daily close beyond the level (level families: PDH, PDL, PWH, PWL, Daily swing high/low, Weekly swing high/low, PDA zone — see methodology corpus).
- Body size large relative to recent N-day distribution.
- Close not "barely beyond" the level (parameterise the threshold).
- No dominant rejection wick on the breaking side.

Source basis:
- `docs/source_methodology/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md`
- Olya's "quality signs" (see methodology digest)

Forbidden claims: `valid_break`, `confirmed_break`, `signal`.

### 4.2 `basic_close_through_control_candidate` (priority: high)

Daily candle that closes *marginally* beyond a level — the **control** for
heuristic 4.1. Surfaces near-misses so Olya can sharpen the strong/basic
boundary.

Required signal features:
- Daily close beyond the level.
- One or more of: small body / dominant rejection wick / quick re-entry next session.

Forbidden claims: `weak_break`, `failed_break` — these are Olya's calls.

### 4.3 `balance_escape_candidate` (priority: high)

Daily session that exits an overlapping/balance window via a directional close.

Required signal features:
- Preceded by an overlap window (define overlap operationally — methodology corpus + concept board).
- Daily close outside the box.
- Body large / close near extreme.

Source basis:
- `methodology/STATE_DETECTION_LOGIC_v2.yaml`
- `OLYA_NEX_HTF_MAP_v0_15_BALANCE_PATCH.md` (in `reviews/`)

Forbidden claims: `balance_break`, `expansion_started`.

### 4.4 `clean_pullback_candidate` (priority: high)

A pullback inside a directional move where the pullback respects structure
(no overlap into prior expansion, controlled retrace, fresh continuation).

Required signal features:
- Identified directional move (parameterise minimum length).
- Pullback retrace within a parameterised band (e.g. 38–62% — verify against methodology).
- No structural breach during the pullback.

Source basis:
- Olya digest entries on pullback quality.

Forbidden claims: `valid_pullback`, `entry_signal`.

### Heuristic registry rules

- Each heuristic has a `heuristic_id` (e.g. `strong_close_through_candidate@0.1.0`).
- Bumping any parameter bumps the version.
- The registry is a dict keyed by `heuristic_id` — version-stamped, immutable post-write.
- A scene's `heuristic_version` is recorded with it; rerunning a heuristic at a new version produces *new* scenes, never overwrites old ones.

---

## §5. Architecture: build-time vs runtime split

This is critical and shapes the V0 design.

```
┌────────────────────────────────────────┐
│ BUILD AGENT — frontier (Opus / GPT)   │
│ One-off: writes code, schemas, docs   │
│ Reads methodology corpus              │
│ Authors heuristic logic               │
│ Drafts review pack templates          │
└──────────────┬─────────────────────────┘
               │
               ▼
┌────────────────────────────────────────┐
│ CARTOGRAPHER RUNTIME — local model    │
│ 24/7 loop: scan → score → emit        │
│ Default: Qwen3.6 @ localhost:8090     │
│ Optional: DeepSeek / GLM API          │
│ Optional: NO model (deterministic)    │
└────────────────────────────────────────┘
```

**Implication for code design:**

1. **The per-candidate scoring loop must be deterministic Python — no LLM
   call.** A 35B local model running 24/7 cannot afford an LLM call per
   candidate; even if it could, determinism would die.
2. **The LLM is used only for narration and adjudication tiers**, both of
   which are *optional* and pluggable:
   - **Narration** (optional, runtime-tier): given a scene, produce a one-paragraph "what does this look like?" summary. Used in the review pack. Disabled by default.
   - **Adjudication** (V0.2; not built in V0 but interface stubbed): ingest Olya's correction notes and propose a heuristic-delta diff. Never auto-applied.
3. **The LLM backend is an interface, not a hardcoded client.** `cartographer/llm/backend.py` exposes a single `narrate(scene, context) -> str` method. Backends:
   - `none` (default): returns empty string. Deterministic.
   - `local`: OpenAI-compatible HTTP client pointed at `http://localhost:8090/v1`.
   - `api`: OpenAI-compatible HTTP client pointed at any external endpoint (DeepSeek, GLM, etc.) — credentials via env var.
   - `frontier`: same interface, used during development.
4. **The scan loop must run with `backend=none` and produce identical scenes.**
   If swapping the backend changes the scenes, the LLM has leaked into the
   deterministic path — that's a bug.

This split is **the** key architectural decision. It means cartographer can run
24/7 on a quiet local model, and the frontier model is only summoned for
human-in-the-loop adjudication moments.

---

## §6. Scene record schema

Every candidate is a single YAML file in `scene_bank/candidates/`. Filename is
the deterministic `scene_id` (truncated SHA-256 of canonicalised inputs).

```yaml
# Example — exact field names enforced by SCENE_SCHEMA.yaml
scene_id: sct_eurusd_2026-03-14_a3f2b1
schema_version: 0.1.0

# What was looked at
instrument: EURUSD
timeframe: D
window_start: 2026-03-14T00:00:00Z
window_end:   2026-03-14T23:59:59Z

# What heuristic fired
candidate_type: strong_close_through_candidate
heuristic_id: strong_close_through_candidate
heuristic_version: 0.1.0
heuristic_parameters_hash: 7c4f...    # changes when params change

# Machine score (NOT a probability of truth — a relative ranker)
score: 0.78

# What the machine observed (bullet list of features it saw)
machine_observation:
  - "close 1.0892 > PDH 1.0871 by 21 pips"
  - "body 84 pips vs 20-day median 47 pips (1.79x)"
  - "upper wick 6 pips, lower wick 11 pips"
  - "no overlap with prior 3-day range"

# Linked structure
linked_levels:
  - kind: PDH
    value: 1.0871
    age_days: 1
linked_prior_scenes: []   # other scene_ids related by structure
linked_future_scenes: []  # populated retroactively if structure links forward

# Review fields — Olya only
review_status: pending_review     # one of: pending_review, reviewed_positive, reviewed_negative, reviewed_near_miss, wrong_candidate, needs_more_context, deferred
olya_label: null
olya_notes: null
olya_corrected_to: null           # if Olya redirected to a different scene_id
correction_type: null             # if reviewed_negative: e.g. "wrong_level_family", "marginal_break", "wick_dominant"

# Provenance
created_at: 2026-05-03T08:14:22Z
data_snapshot_sha: 7202a5c4        # en1gma SHA the snapshot was taken against
runtime_backend: none              # which LLM backend was active
```

**Design notes:**
- `score` is an internal ranker only. It does not assert probability.
- `machine_observation` is plain English, deterministic, generated without an LLM.
- `linked_prior_scenes` enables the "wiki linking" property the concept board hinted at — but the wiki layer is V0.2.
- All review fields are nullable in V0; the feedback loop integration is V0.2.

---

## §7. Olya review pack (the V0 deliverable to Olya)

`reports/experiments/V0_OLYA_REVIEW_PACK_<date>.md` is the proof point. It is
the human-facing artifact the V0 mission must produce.

**Required structure:**

```markdown
# V0 Olya Review Pack — EURUSD Daily, <date_range>

## How to use this pack
[2 sentences: what cartographer is, what we need from Olya]

## Section A — Strong close-through candidates (top 5)

### Candidate A1 — 2026-03-14
- Level: PDH 1.0871 (1 day old)
- Close: 1.0892 (21 pips beyond, body 84 pips, 1.79x median)
- Why the machine flagged this: [1 sentence]
- Chart context: [data table — 5 days before, the candidate day, 3 days after]
- Olya verdict (please fill):
  - [ ] yes — strong close-through
  - [ ] no — explain: ___
  - [ ] near-miss — explain: ___

[… 4 more …]

## Section B — Basic close-through controls (top 5)
[…]

## Section C — Balance escape candidates (top 5)
[…]

## Section D — Clean pullback candidates (top 5)
[…]

## Section E — Build-agent notes
- Noisiest heuristic: ___
- False-positive patterns observed: ___
- Suggested next heuristics: ___
```

The "chart context" can be a small markdown table of OHLC values for the
surrounding window — V0 does not produce chart images. (V0.2 may.)

---

## §8. Verification gates (build agent self-checks before declaring done)

The build agent must run and pass these before reporting completion:

| Gate | Check |
| --- | --- |
| G1 — Determinism | Run `scan_range.py` over the V0 window twice. Diff `scene_bank/candidates/`. Zero differences. |
| G2 — Read-only | After a full scan, `git diff` in `~/en1gma`, `~/phoenix-river`, `en1gma-ref/`, `docs/source_methodology/` shows zero changes. |
| G3 — Backend independence | Run scan with `backend=none` and `backend=local` (if local is up). Scene set must be identical. |
| G4 — Coverage | All four V0 heuristics produce ≥1 candidate over the V0 window. (If a heuristic produces zero, that's a parameter / methodology question — flag in V0_NOTES, do not silently relax.) |
| G5 — Schema conformance | Every YAML in `scene_bank/candidates/` validates against `SCENE_SCHEMA.yaml`. |
| G6 — Performance | One full pass over 8 weeks completes in < 60 seconds on M3. |
| G7 — Documentation | `README.md`, `CANDIDATE_ONLY_CONTRACT.md`, `HEURISTIC_REGISTRY.md`, `RUNTIME.md`, `TESTING.md` all populated. |

---

## §9. Out of scope for V0

Explicit list — do not do these in V0, even if tempting:

- Olya feedback loop integration (V0.2 — schema is ready, code is not)
- Heuristic update proposals from corrections (V0.2)
- Wiki rendering / web UI (V0.2 or later — concept board says wiki is a *layer*, not the primary store)
- Multi-instrument (V0 is EURUSD only)
- Multi-timeframe (V0 is Daily only; H4 / H1 noted in schema for V0.2)
- Live data sync (V0 uses the frozen snapshot)
- Backtesting / performance metrics (cartographer is not a strategy)
- Adjudication tier implementation (V0 stubs the interface only)
- Scene-to-scene structural linking algorithm (V0 leaves `linked_*` lists empty unless trivially derivable)

---

## §10. Governance

- **Lab fork.** No merge-back to en1gma without explicit ratification.
- **Brief approval.** This brief must be reviewed by **G**, **Olya**, and **Olya's advisor** before the build mission is launched. Any changes from review go into `CARTOGRAPHER_V0_MISSION_BRIEF.md` as v0.2-draft, etc.
- **Build review checkpoints.** The build agent should pause and emit status at three points so COO can confirm direction before the next stage:
  1. After heuristic logic for all four is implemented (before scan engine).
  2. After scan engine + first weekly report is generated.
  3. After the V0 Olya review pack is generated, before declaring done.
- **No autonomous heuristic changes.** If during the build the agent thinks a heuristic should change, it stops and asks. It does not invent methodology.

---

## §11. Reference reading list (in priority order)

For the build agent, before writing any code:

1. `cartographer_concept_board.md` — context.
2. `MISSION_INPUTS.md` — repo orientation.
3. `data/README.md` — data schema.
4. `docs/source_methodology/PROVENANCE.md` — what's authoritative and what's not.
5. `docs/source_methodology/canonical/MAP_SPATIAL_PRIMER_v1.md` — the HTF map concept.
6. `docs/source_methodology/methodology/METHODOLOGY_INDEX.md` — methodology map.
7. `docs/source_methodology/reviews/PHASE_5_C2_OLYA_METHODOLOGY_DIGEST_2026_04_30.md` — current Olya methodology summary.
8. `docs/source_methodology/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md` — directly informs heuristic 4.1.
9. `docs/source_methodology/methodology/SYNTHETIC_OLYA_METHOD_vLOCK.yaml` — the 13 L1 primitives.
10. `docs/source_methodology/methodology/STATE_DETECTION_LOGIC_v2.yaml` — HTF phase classifier (informs balance heuristic).
11. `docs/source_methodology/root/calibration_results.yaml` — 27 Olya answers.

The handovers folder gives operational context but is not required reading for V0.

---

## §12. Definition of done

V0 is done when:

- [ ] All seven verification gates (§8) pass.
- [ ] `reports/experiments/V0_OLYA_REVIEW_PACK_<date>.md` exists, populated, and reads cleanly to a non-technical reviewer.
- [ ] The repo can be cloned to a fresh machine, `pip install -e .`, and `cartographer scan-range 2026-02-15 2026-04-30` produces identical output to the original.
- [ ] All hard rules (§2) hold under spot-check.
- [ ] `V0_NOTES.md` includes: (a) noisiest heuristic, (b) at least 3 false-positive patterns observed, (c) at least 2 suggested next heuristics.
- [ ] No file under `~/en1gma`, `~/phoenix-river`, `en1gma-ref/`, or `docs/source_methodology/` has been modified.

---

## Appendix A — Architect's framing (preserved verbatim)

The original advisor framing from the chat-log is preserved at
`cartographer_concept_board.md`. Key quotes for orientation:

> "What you are describing is not a 'wiki' in the loose sense. It is closer to
> a read-only HTF cartography index: a continuously generated candidate atlas
> of market scenes, linked to heuristic provenance, pending Olya adjudication.
> The key is: candidate atlas, not truth engine."

> "The system should prepare the field, not ask her to roam."

> "Cartographer is good. It maps terrain; it does not decide whether to trade."

These are values, not requirements. The requirements are §2 (Hard rules) and
§3 (Deliverables). If a value and a requirement conflict, the requirement wins
and we update the brief.
