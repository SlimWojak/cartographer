# Cartographer V0 — DROID Mission Brief

| Field | Value |
| --- | --- |
| Version | **v0.2** — DRAFT pending Olya + advisor review |
| Date drafted | 2026-05-02 |
| Drafted by | COO (Claude Code, M3) |
| Build agent | Frontier (Opus / GPT) via Droid `exec` |
| Runtime agent (post-build) | Local model (Qwen3.6 / GLM) — see §5 |
| Working directory | `~/cartographer/` |
| Target completion | 48–72 hours of build-agent wall time |
| Authority lineage | en1gma SHA `7202a5c4` (lab fork; no merge-back without ratification) |

## Changelog from v0.1

| Change | Reason |
| --- | --- |
| Added §0.5 — Constitutional alignment with en1gma Phase 5 / WP2 posture | en1gma's WP2 gap report concluded `methodology_examples_needed_for_tie_break=true` for strong_close_through. Cartographer is now directly serving an open en1gma question, not just a side bet. |
| Added §3.5 / §4.6 — Level primitive porting strategy | Olya asked: *"do we have a primitive to recognise PDH/PDL?"* Yes, in en1gma `reference_levels.py`. Brief now specifies port strategy. |
| Added §4.5 — `trap_extreme_state_machine` heuristic | Olya's most cartographer-shaped open question (3-stage state machine: candidate → marginal → confirmed leg extreme). Pulled forward from V0.2 to V0. |
| Added H4 derivation throughout (§5.bis, §6, heuristics) | Q2 / Q3 / trap-extreme are inherently multi-timeframe. 1m parquets make H4 trivial. |
| Added §8 G8 — signal-to-noise spot-check gate | The value of the review pack is signal density. A V0 with 30%+ obvious noise wastes Olya's time. |
| Removed H4 and trap-extreme from §9 (out of scope) | Both now in scope per above. |
| Updated §11 reading order — WP2 gap report at top | Highest contextual relevance; explicitly states the open question cartographer addresses. |

---

## §0. North star

> **Cartographer prepares the terrain; Olya names the truth.**

Olya's HTF map intelligence is the bottleneck. Today, calibrating an HTF rule
means asking Olya "share an example of X" and waiting while she sifts charts.
Cartographer flips the burden: the machine sweeps history, surfaces *candidate*
scenes for a given heuristic, and Olya verifies — *"yes, exactly that"* /
*"no, that one's a near-miss because…"*.

The output is **never** ground truth. The output is a **review queue.**

---

## §0.5. Constitutional alignment

Cartographer is a lab fork. It must respect en1gma's current Phase 5 / WP2
constitutional posture.

**en1gma's current state (as of SHA `7202a5c4`):**

- WP2 strong-close-through primitive-gap report concluded
  `final_recommendation=existing_surface_extension_needed`,
  `new_primitive_decision=not_made`,
  `methodology_examples_needed_for_tie_break=true`.
- Hard guardrail forbids: producer work, schema/cartridge change, threshold
  invention, lower-timeframe confirmation logic, "acceptance"/strong-close-through
  proxies, primitive implementation/extension, daily_momentum/daily_decisive
  primitive work, third-fixture authorization, trade_011 canonicalization.
- Stage 2D fixtures and C2 design scoping are **inert/design-only**.
- H4 is **strategy-specific only** — not core Map authority, not global alignment.

**What cartographer therefore MUST NOT do:**

| Forbidden | Why |
| --- | --- |
| Propose new primitives | en1gma's posture: existing surface extension only. |
| Propose primitive thresholds or parameters as "correct" | Threshold invention is forbidden in en1gma posture. |
| Propose strong-close-through proxies or deltas | Specifically forbidden. |
| Make H4 carry authority | en1gma rule: H4 is sensor only. |
| Output anything labeled as "valid", "confirmed", "true" | Olya labels truth; we surface candidates. |
| Touch en1gma runtime, schemas, cartridges | Lab fork; out of scope by definition. |

**What cartographer MAY do:**

| Allowed | Why |
| --- | --- |
| Port locked L1 algorithms verbatim from en1gma into the lab | The algorithms are settled; we're using them, not modifying them. |
| Apply locked L1 algorithms to Daily/H4 with experimental L1.5 parameters | TF-scoping is per VLOCK design — same algorithm, different parameters per TF. |
| Surface candidate scenes for Olya | This is exactly the `methodology_examples_needed_for_tie_break` deliverable. |
| Surface multiple parameter sets side-by-side as "compare these" packs | Olya needs to see how parameter choice affects which scenes get flagged. |

**Where cartographer fits the en1gma sprint:** the WP2 gap report blocked on
methodology examples. Cartographer's V0 review pack is — directly — the
methodology examples WP2 needs. If V0 produces a high-signal pack and Olya
verifies it, en1gma can resume WP2 tie-break decisions with evidence.

---

## §1. Mission

Build a read-only candidate-scene mining tool for **EURUSD HTF logic** (Daily
+ H4), fed by a frozen 6-year DuckDB snapshot, that produces a reviewable atlas
of candidate market scenes for Olya. V0 covers **8–12 weeks of EURUSD**
across **five heuristics**, including the multi-stage **trap-extreme state
machine** that is currently Olya's most-asked open question.

The pain point being solved (verbatim from the most recent Olya exchange):

> "Should the system allow one additional marginal Daily extreme after the
> first H4 pause sensor before confirming the final expansion-leg high/low?
> How should the system distinguish accepted momentum continuation from a
> bull/bear-trap extreme?"

Cartographer's V0 success criterion: produce a curated review pack where Olya
can verify her proposed multi-stage rule against 8–12 weeks of historical
candidates, instead of weeks of manual chart roaming.

---

## §2. Hard rules (non-negotiable)

These rules apply to **every line of code, every output, every commit**.

| # | Rule | Why |
| - | --- | --- |
| H1 | **Candidate-only output.** Every scene record carries `review_status: pending_review`. No field anywhere claims "true" / "valid" / "signal" / "confirmed". | Olya is the only labeler. |
| H2 | **No writes outside `~/cartographer/`.** | This is a sandboxed lab. en1gma and phoenix-river are off-limits. |
| H3 | **No methodology authoring.** Heuristics are an *interpretation* of locked primitives, not new methodology. The interpretation is explicit and parameterised. | en1gma owns methodology. Cartographer interprets it for example-finding. |
| H4 | **No automatic heuristic mutation.** Olya feedback is collected (V0.2), proposed heuristic deltas require human ratification. | Prevents heuristic drift away from Olya's actual logic. |
| H5 | **No trade signals, no certification claims, no producer outputs.** | Cartographer is a research/review tool, not a strategy. |
| H6 | **Deterministic and resumable.** Same inputs → byte-identical outputs. Resuming a partial scan never duplicates work. | Lets Olya trust she's not seeing different scenes on different runs. |
| H7 | **Read-only against the DuckDB.** The scan loop opens `cartographer.duckdb` with `read_only=True`. Scene outputs go to `scene_bank/`, never back into the DB. | Snapshot integrity. |
| H8 | **Offline by default.** No network calls in the scan loop. LLM calls (if used) go through one explicit module so they can be disabled or swapped. | Lets the runtime sit on a local model with no API egress. |
| H9 | **No threshold invention.** Cartographer surfaces candidates at *multiple* parameter settings side-by-side; it never declares one set "correct". | en1gma posture forbids threshold invention. |
| H10 | **Ported algorithms are byte-faithful.** When porting from en1gma, code carries `# Ported verbatim from en1gma:<path> @ SHA 7202a5c4` and is never tweaked without explicit ratification. | Preserves the L1-locked status of the underlying primitive. |

If any rule conflicts with a deliverable, **the rule wins** — flag it and stop.

---

## §3. Deliverables (V0)

### 3.1 Code

| Path | What |
| --- | --- |
| `cartographer/primitives/reference_levels.py` | **Ported** from `en1gma/console/detection/ra_engine/detectors/reference_levels.py`. PDH/PDL/PWH/PWL/Equilibrium/Midnight Open. 17:00 NY forex-day boundary, wick-based. See §3.5. |
| `cartographer/primitives/swing_points.py` | **Ported** from en1gma SWING_POINTS L1 algorithm (VLOCK §SWING_POINTS). Timeframe-agnostic; parameters per TF. |
| `cartographer/primitives/mss.py` | **Ported** from en1gma MSS L1 (carries break_type REVERSAL/CONTINUATION). |
| `cartographer/primitives/displacement.py` | **Ported** from en1gma DISPLACEMENT L1 (ATR + body ratio). |
| `cartographer/primitives/fvg.py` | **Ported** from en1gma FVG L1. |
| `cartographer/data/h4.py` | H4 OHLC derivation from `bars_1m` via DuckDB. UTC sessions. See §5.bis. |
| `cartographer/heuristics/<name>.py` | One module per heuristic — pure functions, deterministic, parameters from YAML. |
| `cartographer/heuristics/registry.py` | Loads heuristic configs, validates, version-stamps. |
| `cartographer/scene_store/schema.py` | `CandidateScene` dataclass — see §6. |
| `cartographer/scene_store/io.py` | YAML read/write, deterministic filename per scene_id. |
| `cartographer/scans/engine.py` | Core loop — scan window → run heuristics → emit scenes. Includes multi-stage state-machine driver for §4.5. |
| `cartographer/scans/run_week.py` | CLI: scan one ISO week. |
| `cartographer/scans/run_range.py` | CLI: scan a date range. Idempotent. |
| `cartographer/reports/weekly.py` | Generate `reports/weekly/<date>.md`. |
| `cartographer/reports/review_pack.py` | Generate the Olya review pack (see §3.3). |
| `cartographer/llm/backend.py` | LLM abstraction — see §5. Default backend: `none` (deterministic only). |

### 3.2 Documents (authored by build agent)

| Path | Content |
| --- | --- |
| `CANDIDATE_ONLY_CONTRACT.md` | Formal restatement of the H1–H10 rules + commit-time check list. |
| `LEVEL_PRIMITIVES.md` | What was ported, from where, at what SHA. Diff-friendly so Olya/CTO can see the lab is using locked algorithms unchanged. |
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
| `reports/experiments/V0_OLYA_REVIEW_PACK_<date>.md` | The deliverable for Olya: top candidates per heuristic across the V0 window, with chart context, machine reasoning, and a verification slot. **Includes a dedicated trap-extreme section (§7).** |
| `reports/experiments/V0_NOTES.md` | Build agent's own notes — noisiest heuristic, false-positive patterns, suggested next heuristics, signal-to-noise spot-check results (§8 G8). |
| `reports/experiments/V0_PARAM_SENSITIVITY.md` | For each heuristic, side-by-side count of candidates produced under different parameter settings (per H9). Olya sees how parameter choice affects yield. |

### 3.5 Level primitive port strategy

Olya's open question — *"do we have a primitive to recognise PDH/PDL?"* —
is answered: **yes, in en1gma `reference_levels.py`**, version 1.0.0, status
CONFIRMED correct in canon. Cartographer ports the algorithm verbatim.

**Port mechanic:**

1. Read `en1gma-ref/en1gma/console/detection/ra_engine/detectors/reference_levels.py`.
2. Re-implement the algorithm in `cartographer/primitives/reference_levels.py` **with no semantic changes**. Strip en1gma framework imports (`PrimitiveDetector` base, `Detection` types) and replace with a plain function returning a list of `LevelRecord` dataclasses.
3. Top-of-file comment: `# Ported verbatim from en1gma/console/detection/ra_engine/detectors/reference_levels.py @ SHA 7202a5c4. Do not modify L1 logic. Pip floors / parameters live in heuristics/configs.`
4. Add a sanity test: feed identical 1m bars to both implementations and assert PDH/PDL match.

**Same approach for SWING_POINTS, MSS, DISPLACEMENT, FVG.** SWING_POINTS gets
its L1.5 parameters per TF from a config, with **multiple candidate parameter
sets** for Daily/H4 (since Olya hasn't calibrated those — V0 surfaces the
choice rather than picking one).

---

## §4. V0 heuristics

All five are **candidate-only** and emit `review_status: pending_review`.
Parameter values below are **starting points** — the build agent should set
defaults by reading the methodology corpus, then run a parameter sweep to
populate `V0_PARAM_SENSITIVITY.md` per H9.

### 4.1 `strong_close_through_candidate` (priority: high)

Daily candle that closes beyond a candidate HTF level/zone with a clear,
non-marginal break.

Required signal features:
- Daily close beyond the level (level families: PDH, PDL, PWH, PWL, Daily swing high/low, Weekly swing high/low — from `cartographer/primitives/reference_levels.py` and `swing_points.py`).
- Body size large relative to recent N-day distribution.
- Close not "barely beyond" the level (parameterise threshold; sweep multiple).
- No dominant rejection wick on the breaking side.

Per Olya 2026-05-02 ruling:
- Hard level → bullish: Daily close *strongly* above the level.
- Zone/PDA → bullish: Daily close *strongly* above the *upper boundary* of the zone (not inside, not at touch, not at mitigation).
- Bearish symmetric.

Source basis:
- `docs/source_methodology/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md`
- Olya 2026-05-02 reply Q1 (preserved at the equivalent en1gma path; reproduced inline in V0_NOTES).

Forbidden claims: `valid_break`, `confirmed_break`, `signal`, `acceptance`,
`strong_close_through_true`, `invalidated_true`.

### 4.2 `basic_close_through_control_candidate` (priority: high)

Daily candle that closes *marginally* beyond a level — the **control** for
heuristic 4.1. Surfaces near-misses so Olya can sharpen the strong/basic boundary.

Required signal features:
- Daily close beyond the level.
- One or more of: small body / dominant rejection wick / quick re-entry next session.

Forbidden claims: `weak_break`, `failed_break` — these are Olya's calls.

### 4.3 `balance_escape_candidate` (priority: high)

Daily session that exits an overlapping/balance window via a directional close,
optionally with H4 confirmation.

Required signal features (per Olya 2026-05-02 ruling Q2):
- Preceded by an overlap/balance window (define operationally — methodology corpus + concept board).
- Daily close outside the box (above for bullish, below for bearish).
- Body large / close near extreme.
- **Optional H4 confirmation:** 4H_MSS in the escape direction + 4H_displacement in the escape direction. Surface candidates **with and without** H4 confirmation separately so Olya sees both populations.

Source basis:
- `methodology/STATE_DETECTION_LOGIC_v2.yaml`
- `OLYA_NEX_HTF_MAP_v0_15_BALANCE_PATCH.md` (in `reviews/`)
- Olya 2026-05-02 reply Q2.

Forbidden claims: `balance_break`, `expansion_started`, `permission_granted`.

### 4.4 `clean_pullback_candidate` (priority: high)

A pullback inside a directional move where the pullback respects structure.

Required signal features:
- Identified directional move (parameterise minimum length).
- Pullback retrace within a parameterised band (e.g. 38–62% — verify against methodology and surface multiple candidate bands).
- No structural breach during the pullback.

Forbidden claims: `valid_pullback`, `entry_signal`.

### 4.5 `trap_extreme_state_machine` (priority: highest — flagship V0 heuristic)

This heuristic is the answer to Olya's 2026-05-02 open question on bull/bear
trap extremes. It is **multi-stage** and operates over a sequence of bars,
not a single point.

**The state machine (per Olya's proposed logic, verbatim from her 2026-05-02 message):**

```
state_0: WAITING
    ↓ (Daily expansion direction confirmed via existing primitives)
state_1: DAILY_EXPANSION_ACTIVE
    ↓ (Daily prints a current expansion extreme)
state_2: DAILY_EXTREME_PRINTED
    ↓ (H4 MSS forms against Daily expansion direction
       AND H4 displacement away from Daily extreme)
state_3: CANDIDATE_LEG_EXTREME
    ↓ branches:
    ├─ continuation_branch:
    │    Price breaks beyond candidate_leg_extreme in original direction
    │    AND Daily shows acceptance/continuation
    │    → state_3a: CONTINUATION_OBSERVED
    │      → emit scene type: "continuation_after_pause_signal"
    │
    └─ trap_extreme_branch:
         Price prints one more marginal extreme after candidate
         AND fails to continue
         AND fresh H4 MSS + H4 displacement against Daily expansion
         → state_3b: CONFIRMED_LEG_EXTREME
           → emit scene type: "trap_extreme_confirmed"
```

**Output scenes (one of three types per qualifying sequence):**

| Scene type | Meaning |
| --- | --- |
| `candidate_leg_extreme_pending` | First H4 MSS detected; outcome not yet known (window not closed) |
| `continuation_after_pause_signal` | Candidate was early; Daily expansion continued |
| `trap_extreme_confirmed` | Marginal new extreme + fresh H4 MSS → confirmed leg extreme |

**Why this is the V0 flagship:**

- It is the most cartographer-shaped question Olya has asked: *"verify my
  proposed multi-stage rule against history."*
- It exercises the scene-linking machinery (the candidate scene → outcome
  scene chain) that the rest of cartographer will need eventually.
- A high-signal trap-extreme review pack would directly accelerate Olya's
  HTF leg-measurement methodology calibration.

**Required scene record fields beyond the standard schema:**

- `state_machine_id` (uuid; same for all scenes in one resolved chain)
- `state_at_emission` (one of: `candidate_pending`, `continuation`, `trap_confirmed`)
- `candidate_extreme_timestamp` and `candidate_extreme_price`
- `confirmed_extreme_timestamp` and `confirmed_extreme_price` (when state 3b reached)
- `marginal_break_pips` (distance from candidate to confirmed extreme)
- `linked_h4_mss_scene_ids` (the one or two H4 MSS scenes that fired)
- `linked_displacement_scene_ids`
- `daily_expansion_direction` (`up` | `down`)

**Forbidden claims:** `proposed_logic_validated`, `trap_rule_correct`,
`leg_extreme_authoritative`. Cartographer surfaces the chain; Olya confirms
or rejects.

### Heuristic registry rules

- Each heuristic has a `heuristic_id` (e.g. `strong_close_through_candidate@0.1.0`).
- Bumping any parameter bumps the version.
- The registry is a dict keyed by `heuristic_id` — version-stamped, immutable post-write.
- A scene's `heuristic_version` is recorded with it; rerunning a heuristic at a new version produces *new* scenes, never overwrites old ones.
- **Per H9:** for each heuristic, V0 ships at least 2 parameter sets and runs both. The review pack labels candidates by which parameter set produced them.

### 4.6 What we do NOT include in V0 heuristics

Excluded explicitly to align with en1gma posture:

- No "Daily momentum" or "Daily decisive" candle primitives — en1gma WP2 has not authorised these.
- No "acceptance" classification — en1gma forbids the acceptance proxy.
- No `level_state` lifecycle ladder (`not_touched → touched → inside → above → below → closed_through → rejected → invalidated`). The level_state ladder belongs in en1gma. Cartographer references levels but does not emit lifecycle events.
- No FVG/OB-as-zone close-through detection in V0 (PDH/PDL/PWH/PWL/swing only). FVG/OB are ported as primitives but used as supplementary `linked_levels` context, not as primary close-through targets, until Olya validates the simpler hard-level cases first.

---

## §5. Architecture: build-time vs runtime split

Critical and shapes the V0 design.

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

1. **The per-candidate scoring loop must be deterministic Python — no LLM call.** A 35B local model running 24/7 cannot afford an LLM call per candidate; even if it could, determinism would die. **This includes the trap-extreme state machine — it is a pure state machine over deterministic primitive outputs.**
2. **The LLM is used only for narration and adjudication tiers**, both pluggable:
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

### §5.bis H4 derivation

H4 is required for heuristics 4.3, 4.5 (and informs 4.1 wick-quality context).

- **Source:** `bars_1m` table in `cartographer.duckdb`.
- **Mechanism:** SQL aggregation by 4-hour buckets, UTC. Boundaries: 00, 04, 08, 12, 16, 20 UTC.
- **Output:** materialised as a view `bars_h4` in cartographer (added at scan startup, not stored in the DB), with the same OHLC + minute_bar_count + session_start/end columns as `bars_daily`.
- **MSS / displacement / swing on H4:** apply the ported L1 algorithms with H4-appropriate L1.5 parameters. Surface multiple param sets per H9.
- **No H4 authority:** per en1gma rule, H4 outputs are sensors only. Scene records may say `h4_mss_present: true`; they may not say `h4_decided_direction: bullish`.

---

## §6. Scene record schema

Every candidate is a single YAML file in `scene_bank/candidates/`. Filename is
the deterministic `scene_id` (truncated SHA-256 of canonicalised inputs).

```yaml
# Example — exact field names enforced by SCENE_SCHEMA.yaml
scene_id: sct_eurusd_2026-03-14_a3f2b1
schema_version: 0.2.0

# What was looked at
instrument: EURUSD
timeframe: D                          # D | H4 (V0 supports both)
window_start: 2026-03-14T00:00:00Z
window_end:   2026-03-14T23:59:59Z

# What heuristic fired
candidate_type: strong_close_through_candidate
heuristic_id: strong_close_through_candidate
heuristic_version: 0.1.0
heuristic_parameters_set: "default"   # or "tight_threshold", "loose_threshold" — per H9
heuristic_parameters_hash: 7c4f...    # changes when params change

# Machine score (NOT a probability of truth — a relative ranker)
score: 0.78

# What the machine observed (bullet list of features)
machine_observation:
  - "Daily close 1.0892 > PDH 1.0871 by 21 pips (above level)"
  - "Body 84 pips vs 20-day median 47 pips (1.79x)"
  - "Upper wick 6 pips, lower wick 11 pips"
  - "No overlap with prior 3-day range"

# Linked structure (level reference is from ported reference_levels.py)
linked_levels:
  - kind: PDH
    value: 1.0871
    age_days: 1
    source_primitive: "reference_levels@1.0.0"
linked_prior_scenes: []   # other scene_ids related by structure
linked_future_scenes: []  # populated retroactively (V0: only for trap_extreme chains)

# State-machine fields (only populated for trap_extreme heuristic)
state_machine_id: null
state_at_emission: null              # candidate_pending | continuation | trap_confirmed
candidate_extreme_timestamp: null
candidate_extreme_price: null
confirmed_extreme_timestamp: null
confirmed_extreme_price: null
marginal_break_pips: null
linked_h4_mss_scene_ids: []
linked_displacement_scene_ids: []
daily_expansion_direction: null      # up | down

# Review fields — Olya only
review_status: pending_review        # pending_review | reviewed_positive | reviewed_negative | reviewed_near_miss | wrong_candidate | needs_more_context | deferred
olya_label: null
olya_notes: null
olya_corrected_to: null              # if Olya redirected to a different scene_id
correction_type: null                # if reviewed_negative: e.g. "wrong_level_family", "marginal_break", "wick_dominant"

# Provenance
created_at: 2026-05-03T08:14:22Z
data_snapshot_sha: 7202a5c4          # en1gma SHA the snapshot was taken against
runtime_backend: none                # which LLM backend was active
```

**Design notes:**
- `score` is an internal ranker only. It does not assert probability.
- `machine_observation` is plain English, deterministic, generated without an LLM.
- `linked_prior_scenes` / `linked_future_scenes` are populated for trap_extreme chains in V0; other heuristics leave them empty.
- All review fields are nullable in V0; the feedback loop integration is V0.2.

---

## §7. Olya review pack (the V0 deliverable to Olya)

`reports/experiments/V0_OLYA_REVIEW_PACK_<date>.md` is the proof point. It is
the human-facing artifact the V0 mission must produce.

**Required structure:**

```markdown
# V0 Olya Review Pack — EURUSD HTF, <date_range>

## How to use this pack
[2 sentences: what cartographer is, what we need from Olya]

## Section A — Strong close-through candidates (top 5)

### Candidate A1 — 2026-03-14
- Level: PDH 1.0871 (1 day old, source: reference_levels@1.0.0)
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
- For each: shown twice, once with H4 confirmation present, once without.
- Olya verdict includes "is H4 confirmation needed for THIS case?"
[…]

## Section D — Clean pullback candidates (top 5)
[…]

## Section E — Trap-extreme chains (the flagship section)

For each trap_extreme chain, the pack shows the **full sequence**:
1. The candidate_leg_extreme bar (when first H4 MSS fired)
2. The marginal new extreme bar (if it occurred)
3. The fresh H4 MSS bar (if it occurred)
4. Outcome label: continuation / trap_confirmed / pending

### Chain E1 — 2026-02-14 to 2026-02-19
- Daily expansion direction: bullish since 2026-02-10
- Candidate leg extreme: 2026-02-14 high 1.0934
- First H4 MSS bearish: 2026-02-14 16:00 UTC
- Marginal new high: 2026-02-15 high 1.0941 (+7 pips)
- Fresh H4 MSS bearish: 2026-02-16 04:00 UTC
- Outcome scene type: trap_extreme_confirmed
- Olya verdict (please fill):
  - [ ] confirms trap-extreme rule
  - [ ] this should NOT be classified as trap (wrong because: ___)
  - [ ] near-miss — explain: ___
  - Was the marginal break magnitude meaningful (___)?
  - Should the system require minimum candle separation (___)?

[… 4 more chains …]

## Section F — Build-agent notes
- Noisiest heuristic: ___
- False-positive patterns observed: ___
- Suggested next heuristics: ___
- Signal-to-noise spot-check (per G8): ___ obvious-keep / ___ borderline / ___ obvious-noise per heuristic
- Parameter sensitivity summary (per H9): see V0_PARAM_SENSITIVITY.md
```

The "chart context" is a small markdown table of OHLC values for the
surrounding window — V0 does not produce chart images. (V0.2 may.)

---

## §8. Verification gates (build agent self-checks before declaring done)

The build agent must run and pass these before reporting completion:

| Gate | Check |
| --- | --- |
| G1 — Determinism | Run `scan_range.py` over the V0 window twice. Diff `scene_bank/candidates/`. Zero differences. |
| G2 — Read-only | After a full scan, `git diff` in `~/en1gma`, `~/phoenix-river`, `en1gma-ref/`, `docs/source_methodology/` shows zero changes. |
| G3 — Backend independence | Run scan with `backend=none` and `backend=local` (if local is up). Scene set must be identical. |
| G4 — Coverage | All five V0 heuristics produce ≥1 candidate over the V0 window. (If a heuristic produces zero, that's a parameter / methodology question — flag in V0_NOTES, do not silently relax.) |
| G5 — Schema conformance | Every YAML in `scene_bank/candidates/` validates against `SCENE_SCHEMA.yaml`. |
| G6 — Performance | One full pass over 8 weeks completes in < 90 seconds on M3 (relaxed from 60s in v0.1 to allow H4 derivation + state machine). |
| G7 — Documentation | `README.md`, `CANDIDATE_ONLY_CONTRACT.md`, `LEVEL_PRIMITIVES.md`, `HEURISTIC_REGISTRY.md`, `RUNTIME.md`, `TESTING.md` all populated. |
| **G8 — Signal-to-noise spot check** | **For each heuristic, build agent randomly samples 10 candidates and hand-rates them as obvious-keep / borderline / obvious-noise. Records ratio in V0_NOTES. Build is BLOCKED for review if obvious-noise > 30% on any heuristic.** |
| G9 — Trap-extreme reproducibility | At least one trap-extreme chain in the V0 window resolves to `trap_extreme_confirmed`. (If none do, parameters need adjustment OR the V0 window doesn't contain one — flag honestly.) |
| G10 — Port fidelity | Sanity test confirms `cartographer/primitives/reference_levels.py` produces the same PDH/PDL values as the en1gma source for a sample week. |

---

## §9. Out of scope for V0

Explicit list — do not do these in V0, even if tempting:

- Olya feedback loop integration (V0.2 — schema is ready, code is not).
- Heuristic update proposals from corrections (V0.2).
- Wiki rendering / web UI (V0.2 or later — concept board says wiki is a *layer*, not the primary store).
- Multi-instrument (V0 is EURUSD only).
- M5/M15 timeframes (Daily + H4 only in V0).
- Live data sync (V0 uses the frozen snapshot).
- Backtesting / performance metrics (cartographer is not a strategy).
- Adjudication tier implementation (V0 stubs the interface only).
- Scene-to-scene structural linking algorithm beyond the trap-extreme chain (other heuristics leave `linked_*` empty).
- FVG / OB as primary close-through targets (V0 covers hard levels + swings; FVG/OB ported but used as context only).
- `level_state` lifecycle ladder (belongs in en1gma).
- Anything that en1gma's hard guardrail forbids (see §0.5).

---

## §10. Governance

- **Lab fork.** No merge-back to en1gma without explicit ratification.
- **Brief approval.** This brief must be reviewed by **G**, **Olya**, and **Olya's advisor** before the build mission is launched. Any changes from review go into `CARTOGRAPHER_V0_MISSION_BRIEF.md` as v0.3-draft, etc.
- **Build review checkpoints.** The build agent should pause and emit status at four points:
  1. After all five primitives are ported and the port-fidelity test (G10) passes.
  2. After heuristic logic for all five is implemented (before scan engine).
  3. After scan engine + first weekly report is generated.
  4. After the V0 Olya review pack is generated, before declaring done.
- **No autonomous heuristic changes.** If during the build the agent thinks a heuristic should change, it stops and asks. It does not invent methodology.
- **Constitutional alignment with en1gma.** Per §0.5, cartographer's V0 deliverable is the methodology examples WP2 needs. The mission brief should be reviewed alongside `docs/source_methodology/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md` so reviewers see the contextual fit.

---

## §11. Reference reading list (in priority order)

For the build agent, before writing any code:

1. **`docs/source_methodology/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md`** — the open question cartographer addresses. Read first.
2. `cartographer_concept_board.md` — context.
3. `MISSION_INPUTS.md` — repo orientation.
4. `data/README.md` — data schema.
5. `docs/source_methodology/PROVENANCE.md` — what's authoritative and what's not.
6. `docs/source_methodology/canonical/MAP_SPATIAL_PRIMER_v1.md` — the HTF map concept.
7. `docs/source_methodology/methodology/METHODOLOGY_INDEX.md` — methodology map.
8. `docs/source_methodology/methodology/SYNTHETIC_OLYA_METHOD_vLOCK.yaml` — locked L1 primitives (especially SWING_POINTS, FVG, MSS, DISPLACEMENT, REFERENCE_LEVELS sections).
9. `docs/source_methodology/methodology/STATE_DETECTION_LOGIC_v2.yaml` — HTF phase classifier (informs balance + trap-extreme heuristics).
10. `docs/source_methodology/reviews/PHASE_5_C2_OLYA_METHODOLOGY_DIGEST_2026_04_30.md` — current Olya methodology summary.
11. `en1gma-ref/en1gma/console/detection/ra_engine/detectors/reference_levels.py` — ported into cartographer per §3.5.
12. `docs/source_methodology/root/calibration_results.yaml` — 27 Olya answers.
13. Olya 2026-05-02 reply (Q1, Q2, Q3, Q4, trap-extreme question) — drafted into `V0_NOTES.md` for inline reference. Sourced from G's relay.

The handovers folder gives operational context but is not required reading for V0.

---

## §12. Definition of done

V0 is done when:

- [ ] All ten verification gates (§8) pass.
- [ ] `reports/experiments/V0_OLYA_REVIEW_PACK_<date>.md` exists, populated, and reads cleanly to a non-technical reviewer. **Includes the trap-extreme chains section (§7 Section E).**
- [ ] `reports/experiments/V0_PARAM_SENSITIVITY.md` exists, showing yield comparison across parameter sets per heuristic.
- [ ] `LEVEL_PRIMITIVES.md` exists, documenting what was ported, from where, at what SHA, with the diff-friendly pseudocode.
- [ ] The repo can be cloned to a fresh machine, `pip install -e .`, `python scripts/seed_data.py`, and `python -m cartographer.scans.run_range 2026-02-15 2026-04-30` produces identical output to the original.
- [ ] All hard rules (§2) hold under spot-check.
- [ ] `V0_NOTES.md` includes: (a) noisiest heuristic, (b) at least 3 false-positive patterns observed, (c) at least 2 suggested next heuristics, (d) signal-to-noise spot-check ratios per G8.
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
§3 (Deliverables). If a value and a requirement conflict, the requirement
wins and we update the brief.

---

## Appendix B — Olya 2026-05-02 ruling extracts (the proximate trigger for v0.2)

The build agent should reproduce these in `V0_NOTES.md` for ground-level
reference. Two extracts most relevant:

**Q1 close-through ruling:**
> "Close-through requires a strong Daily candle close beyond the relevant
> level or zone boundary. Close-through is a Daily-only object-boundary event.
> 4H MSS/displacement is not part of close-through logic. … For a bearish
> order block acting as resistance, bullish close-through requires Daily
> close above the top of the OB. For a bullish FVG acting as support, bearish
> close-through requires Daily close below the bottom of the FVG."

**Trap-extreme question (proposed logic, awaiting verification):**
> "Should the system treat the first H4 MSS against Daily expansion as only
> a candidate pause, not a final confirmed Daily leg extreme? Should the
> system allow one additional marginal Daily extreme after the first H4 pause
> sensor before confirming the final expansion-leg high/low? How should the
> system distinguish accepted momentum continuation from a bull/bear-trap
> extreme?"

Cartographer's V0 review pack is the answer to "show me historical examples
so I can verify my proposed rule."
