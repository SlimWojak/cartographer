# Cartographer V0 — DROID Mission Brief

| Field | Value |
| --- | --- |
| Version | **v0.3** — DRAFT pending Olya + advisor review |
| Date drafted | 2026-05-02 |
| Drafted by | COO (Claude Code, M3) |
| Build agent | Frontier (Opus / GPT) via Droid `exec` |
| Runtime agent (post-build) | Local model (Qwen3.6 / GLM) — see §5 |
| Working directory | `~/cartographer/` |
| Target completion | 48 hours of build-agent wall time |
| Authority lineage | en1gma SHA `7202a5c4` (lab fork; no merge-back without ratification) |

## Changelog

**v0.3 (current)** — refocused after rules-vs-examples synthesis from advisor.

| Change | Reason |
| --- | --- |
| Added §0.1 — the workflow breakthrough (rules-vs-examples asymmetry) | This is the load-bearing rationale for cartographer's existence; v0.1/v0.2 understated it. |
| Pulled `trap_extreme_state_machine` out of V0 → deferred to V0.1 | Per advisor synthesis: "should not be rushed... should become a future Daily leg lifecycle design artifact, not be mixed into WP2 close-through examples." V0 must be unimpeachably useful for the WP2 close-through tie-break Olya is in TODAY. |
| Tightened §1 mission to name the active sprint conversation | V0's first delivery should drop directly into the WP2 follow-up Olya is now answering. |
| Removed v0.2's review-pack Section E and gate G9 | Both were trap-extreme specific. |
| Kept state-machine schema fields nullable in §6 | Forward-compat for V0.1; no V0 code populates them. |

**v0.2** — widened scope after primitive audit + Olya 2026-05-02 exchange.

- §0.5 constitutional alignment with en1gma Phase 5 / WP2 posture; H1–H10 rules.
- §3.5 level-primitive port strategy (PDH/PDL/PWH/PWL from `reference_levels.py` v1.0.0; SWING_POINTS from VLOCK).
- §5.bis H4 derivation as sensor only.
- Gates G8 (signal-to-noise), G10 (port fidelity).

---

## §0. North star

> **Cartographer prepares the terrain; Olya names the truth.**

Olya's HTF map intelligence is the bottleneck. Cartographer surfaces *candidate*
scenes for a given heuristic; Olya verifies — *"yes, exactly that"* / *"no,
near-miss because…"*. The output is **never** ground truth. The output is a
**review queue.**

## §0.1. The workflow breakthrough

This is why cartographer exists.

**Olya's brain naturally produces *rules*** — fast, dense, ontologically
precise. The team needs **examples** to calibrate those rules. Producing
examples requires Olya to context-switch into chart-archaeology mode — a
different and slower cognitive mode for her.

Today, both rules and examples flow through the same channel ("send Olya a
packet"). That channel is **asymmetric**: the rule side runs at Olya's natural
speed; the example side bottlenecks her. The most recent WP2 exchange proved
it — packet asked for chart examples, Olya delivered rulings + a leg-lifecycle
proposal, because rules and design extension are what her brain produces fast.
Examples did not come back; the team must now ask again for "2–3 concrete
examples".

**Cartographer is the missing second channel:**

```
RULES   :  Olya  →  team        (cheap for Olya)
EXAMPLES:  Cartographer  →  Olya for verification  (cheap for the machine,
                                                    cheap for Olya to validate)
```

Every methodology evolution generates a new "show me 2–3 examples" round.
WP2 close-through today, leg-lifecycle next, balance-quality after. A
repeatable example-channel removes that recurring cost permanently.

**Strategic stakes.** en1gma's HTF spatial map is the brain that decides
direction permission. Without robust HTF calibration, en1gma is a scalping
system. The HTF map's calibration speed is currently rate-limited by Olya's
example-sourcing throughput. Cartographer attacks exactly this rate limit.

---

## §0.5. Constitutional alignment

Cartographer is a lab fork. It must respect en1gma's current Phase 5 / WP2
constitutional posture.

**en1gma's current state (as of SHA `7202a5c4`):**

- WP2 strong-close-through primitive-gap report concluded
  `final_recommendation=existing_surface_extension_needed`,
  `new_primitive_decision=not_made`,
  `methodology_examples_needed_for_tie_break=true`.
- The 2026-05-02 Olya exchange answered with rulings; the team is now sending
  a smaller follow-up asking for **2–3 concrete close-through examples**.
- Hard guardrail forbids: producer work, schema/cartridge change, threshold
  invention, lower-timeframe confirmation logic, "acceptance"/strong-close-through
  proxies, primitive implementation/extension, daily_momentum/daily_decisive
  primitive work.
- H4 is **strategy-specific only** — not core Map authority.

**Cartographer MUST NOT:**

| Forbidden | Why |
| --- | --- |
| Propose new primitives, thresholds, deltas | en1gma forbids primitive/threshold invention. |
| Make H4 carry authority | en1gma rule: H4 is sensor only. |
| Output anything labeled "valid" / "confirmed" / "true" | Olya labels truth; we surface candidates. |
| Touch en1gma runtime, schemas, cartridges | Lab fork; out of scope by definition. |

**Cartographer MAY:**

| Allowed | Why |
| --- | --- |
| Port locked L1 algorithms verbatim from en1gma | The algorithms are settled; we use, not modify. |
| Apply locked L1 algorithms to Daily/H4 with experimental L1.5 parameters | TF-scoping is per VLOCK design. |
| Surface candidates for Olya at multiple parameter settings side-by-side | Olya needs to see how parameter choice affects which scenes get flagged. |

**Where cartographer fits the en1gma sprint:** the WP2 follow-up Olya is now
answering asks for examples. Cartographer's V0 review pack is — directly —
the methodology examples WP2 needs. If V0 produces a high-signal pack, the
team can short-circuit weeks of "send another packet, wait" cycles.

---

## §1. Mission

Build a read-only candidate-scene mining tool for **EURUSD Daily HTF
close-through logic**, fed by a frozen 6-year DuckDB snapshot, that produces
a reviewable atlas of candidate strong-close-through and balance-escape scenes
for Olya. V0 covers **8–12 weeks of EURUSD** across **four close-through
heuristics**.

**The active sprint conversation V0 drops into:**

- WP2 gap report (`@ef185f8`) blocked on `methodology_examples_needed_for_tie_break=true`.
- Olya 2026-05-02 reply gave rulings, not examples.
- Team is preparing a follow-up packet asking for "2–3 concrete close-through examples".
- **V0 ships before that follow-up gets a full reply.** If V0 lands well,
  cartographer becomes the next round's example source instead of Olya.

V0 success = a curated review pack where Olya can verify the WP2
close-through definition (hard-level vs zone, strong vs basic, far-side
boundary rule) against pre-found candidates in one sitting, instead of weeks
of chart roaming.

---

## §2. Hard rules (non-negotiable)

| # | Rule | Why |
| - | --- | --- |
| H1 | **Candidate-only output.** Every scene record carries `review_status: pending_review`. No field anywhere claims "true" / "valid" / "signal" / "confirmed". | Olya is the only labeler. |
| H2 | **No writes outside `~/cartographer/`.** | Sandboxed lab. en1gma and phoenix-river off-limits. |
| H3 | **No methodology authoring.** Heuristics are an *interpretation* of locked primitives, not new methodology. | en1gma owns methodology. |
| H4 | **No automatic heuristic mutation.** Olya feedback is collected (V0.2), proposed deltas require human ratification. | Prevents drift from Olya's actual logic. |
| H5 | **No trade signals, no certification claims, no producer outputs.** | Cartographer is a research tool, not a strategy. |
| H6 | **Deterministic and resumable.** Same inputs → byte-identical outputs. | Olya must trust she's not seeing different scenes on different runs. |
| H7 | **Read-only against the DuckDB.** `read_only=True`. Scenes written to `scene_bank/`, never the DB. | Snapshot integrity. |
| H8 | **Offline by default.** No network calls in the scan loop. LLM calls go through one explicit module. | Lets the runtime sit on a local model. |
| H9 | **No threshold invention.** Cartographer surfaces candidates at *multiple* parameter settings side-by-side; never declares one set "correct". | en1gma posture forbids threshold invention. |
| H10 | **Ported algorithms are byte-faithful.** Each port carries `# Ported verbatim from en1gma:<path> @ SHA 7202a5c4`. Never tweaked without explicit ratification. | Preserves L1-locked status. |

If any rule conflicts with a deliverable, **the rule wins** — flag it and stop.

---

## §3. Deliverables (V0)

### 3.1 Code

| Path | What |
| --- | --- |
| `cartographer/primitives/reference_levels.py` | **Ported** from en1gma `reference_levels.py` v1.0.0. PDH/PDL/PWH/PWL/Equilibrium/Midnight Open. 17:00 NY forex-day boundary, wick-based. See §3.5. |
| `cartographer/primitives/swing_points.py` | **Ported** from en1gma SWING_POINTS L1 (VLOCK). TF-agnostic algorithm; parameters per TF. |
| `cartographer/primitives/displacement.py` | **Ported** from en1gma DISPLACEMENT L1 (used as feature in heuristics 4.1 / 4.3). |
| `cartographer/primitives/mss.py` | **Ported** from en1gma MSS L1 (used by heuristic 4.3 H4 confirmation). |
| `cartographer/data/h4.py` | H4 OHLC derivation from `bars_1m` via DuckDB view. UTC sessions. See §5.bis. |
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
| `CANDIDATE_ONLY_CONTRACT.md` | Formal restatement of H1–H10 + commit-time check list. |
| `LEVEL_PRIMITIVES.md` | What was ported, from where, at what SHA. Diff-friendly so reviewers see locked algorithms unchanged. |
| `HEURISTIC_REGISTRY.md` | One section per V0 heuristic: id, version, rule prose, parameters, what it does NOT claim. |
| `SCENE_SCHEMA.yaml` | Authoritative schema for a candidate scene record. |
| `TESTING.md` | How to verify determinism, sanity scan, "passing" definition. |
| `RUNTIME.md` | How to swap LLM backends (none / local Qwen / DeepSeek-API / frontier). |

### 3.3 Generated artifacts (V0 run output)

| Path | Content |
| --- | --- |
| `scene_bank/candidates/<scene_id>.yaml` | One file per candidate. Deterministic filename. |
| `reports/weekly/<YYYY-Www>.md` | Per-week markdown summary, max 5 per heuristic per week. |
| `reports/weekly/INDEX.md` | Master index of all weeks scanned. |
| `reports/experiments/V0_OLYA_WP2_CLOSE_THROUGH_REVIEW_PACK_<date>.md` | The deliverable for Olya. Top candidates per heuristic across the V0 window, with chart context and verification slots. **Named to dock directly into the WP2 sprint conversation.** |
| `reports/experiments/V0_NOTES.md` | Build agent's notes — noisiest heuristic, false-positive patterns, suggested next heuristics, signal-to-noise spot-check (G8). |
| `reports/experiments/V0_PARAM_SENSITIVITY.md` | Per heuristic, side-by-side count of candidates produced under different parameter settings (per H9). |

### 3.5 Level primitive port strategy

Olya's open question — *"do we have a primitive to recognise PDH/PDL?"* — is
answered: **yes, in en1gma `reference_levels.py`**, version 1.0.0, status
CONFIRMED in canon. Cartographer ports the algorithm verbatim.

**Port mechanic:**

1. Read `en1gma-ref/en1gma/console/detection/ra_engine/detectors/reference_levels.py`.
2. Re-implement in `cartographer/primitives/reference_levels.py` with **no semantic changes**. Strip en1gma framework imports; replace with a plain function returning a list of `LevelRecord` dataclasses.
3. Top-of-file comment: `# Ported verbatim from en1gma/console/detection/ra_engine/detectors/reference_levels.py @ SHA 7202a5c4. Do not modify L1 logic.`
4. Sanity test: feed identical 1m bars to both implementations and assert PDH/PDL match (gate G10).

**Same approach for SWING_POINTS, MSS, DISPLACEMENT.** SWING_POINTS gets its
L1.5 parameters per TF from a config, with **multiple candidate parameter sets**
for Daily/H4 (Olya hasn't calibrated those — V0 surfaces the choice rather
than picking).

---

## §4. V0 heuristics

All four are **candidate-only** and emit `review_status: pending_review`.
Defaults are starting points — the build agent reads the methodology corpus,
then runs a parameter sweep populating `V0_PARAM_SENSITIVITY.md` per H9.

### 4.1 `strong_close_through_candidate` (priority: highest)

Daily candle that closes beyond a hard HTF level with a clear, non-marginal break.

Required signal features (per Olya 2026-05-02 ruling Q1):
- Daily close beyond a hard level — PDH, PDL, PWH, PWL, Daily swing high/low, Weekly swing high/low. (Hard levels only in V0; zones/PDA in V0.1.)
- Body size large relative to recent N-day distribution.
- Close not "barely beyond" the level (parameterise; sweep multiple thresholds).
- No dominant rejection wick on the breaking side.

Per Olya's ruling:
- Bullish: Daily close *strongly* above the level.
- Bearish: Daily close *strongly* below the level.

Forbidden claims: `valid_break`, `confirmed_break`, `signal`, `acceptance`,
`strong_close_through_true`, `invalidated_true`.

### 4.2 `basic_close_through_control_candidate` (priority: high)

Daily candle that closes *marginally* beyond a level — the **control** for
4.1. Surfaces near-misses so Olya can sharpen the strong/basic boundary.

Required features:
- Daily close beyond the level.
- One or more of: small body / dominant rejection wick / quick re-entry next session.

Forbidden claims: `weak_break`, `failed_break` — these are Olya's calls.

### 4.3 `balance_escape_candidate` (priority: high)

Daily session that exits an overlapping/balance window via a directional close,
optionally with H4 confirmation.

Required features (per Olya 2026-05-02 ruling Q2):
- Preceded by an overlap/balance window (operationalise per methodology corpus).
- Daily close outside the box (above for bullish, below for bearish).
- Body large / close near extreme.
- **Optional H4 confirmation:** 4H_MSS in escape direction + 4H_displacement in escape direction. Surface candidates **with and without** H4 confirmation separately so Olya sees both populations.

Forbidden claims: `balance_break`, `expansion_started`, `permission_granted`.

### 4.4 `clean_pullback_candidate` (priority: medium)

A pullback inside a directional move where the pullback respects structure.

Required features:
- Identified directional move (parameterise minimum length).
- Pullback retrace within a parameterised band (e.g. 38–62%; surface multiple bands).
- No structural breach during the pullback.

Forbidden claims: `valid_pullback`, `entry_signal`.

### 4.5 Deferred to V0.1 (NOT in V0)

`trap_extreme_state_machine` — multi-stage state machine answering Olya's
2026-05-02 candidate-vs-confirmed leg-extreme question. **Pulled out of V0
per advisor synthesis** (*"should not be rushed... should become a future
Daily leg lifecycle design artifact, not be mixed into WP2 close-through
examples"*).

V0.1 will add this as a separately-packaged review pack under its own
methodology thread (Daily leg lifecycle), not blended with WP2 close-through.
The schema in §6 keeps state-machine fields nullable so V0.1 can land without
schema changes.

### Heuristic registry rules

- Each heuristic has a `heuristic_id` (e.g. `strong_close_through_candidate@0.1.0`).
- Bumping any parameter bumps the version.
- Per H9: each heuristic ships with **at least 2 parameter sets** and runs both. The review pack labels candidates by which parameter set produced them.

### What we do NOT include in V0 heuristics

Excluded explicitly per en1gma posture:

- No `daily_momentum` or `daily_decisive` candle primitives — explicitly forbidden.
- No "acceptance" classification — forbidden.
- No `level_state` lifecycle ladder — belongs in en1gma.
- No FVG/OB-as-zone close-through detection in V0 (hard levels + swings only). FVG/OB porting deferred to V0.1 when zones are added.

---

## §5. Architecture: build-time vs runtime split

```
┌────────────────────────────────────────┐
│ BUILD AGENT — frontier (Opus / GPT)   │
│ One-off: writes code, schemas, docs   │
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

**Implications:**

1. **Per-candidate scoring is deterministic Python — no LLM call.** A 35B local model running 24/7 cannot afford an LLM call per candidate; determinism would die anyway.
2. **The LLM is used only for narration and adjudication tiers**, both pluggable:
   - **Narration** (optional, runtime): given a scene, produce a one-paragraph "what does this look like?" summary. Disabled by default.
   - **Adjudication** (V0.2; interface stubbed only in V0): ingest Olya's correction notes and propose heuristic-delta diffs. Never auto-applied.
3. **The LLM backend is an interface, not a hardcoded client.** `cartographer/llm/backend.py` exposes `narrate(scene, context) -> str`. Backends: `none` (default, deterministic), `local` (Qwen3.6), `api` (DeepSeek/GLM via env-var creds), `frontier`.
4. **Scan with `backend=none` and `backend=local` must produce identical scenes** (gate G3). If swapping the backend changes scenes, the LLM has leaked into the deterministic path — that's a bug.

### §5.bis H4 derivation

H4 is required only for heuristic 4.3 (balance escape, optional confirmation)
in V0. (V0.1 trap-extreme will lean on it more heavily.)

- **Source:** `bars_1m` table in `cartographer.duckdb`.
- **Mechanism:** SQL aggregation by 4-hour buckets, UTC. Boundaries: 00, 04, 08, 12, 16, 20 UTC.
- **Output:** materialised as a view `bars_h4` in cartographer at scan startup (not stored in the DB).
- **No H4 authority:** per en1gma rule, H4 outputs are sensors only. Scene records may say `h4_mss_present: true`; they may not say `h4_decided_direction: bullish`.

---

## §6. Scene record schema

Every candidate is a single YAML file in `scene_bank/candidates/`. Filename
is the deterministic `scene_id`.

```yaml
scene_id: sct_eurusd_2026-03-14_a3f2b1
schema_version: 0.3.0

instrument: EURUSD
timeframe: D                          # D | H4
window_start: 2026-03-14T00:00:00Z
window_end:   2026-03-14T23:59:59Z

candidate_type: strong_close_through_candidate
heuristic_id: strong_close_through_candidate
heuristic_version: 0.1.0
heuristic_parameters_set: "default"   # or "tight_threshold", "loose_threshold" — per H9
heuristic_parameters_hash: 7c4f...

score: 0.78                           # internal ranker, NOT a probability of truth

machine_observation:
  - "Daily close 1.0892 > PDH 1.0871 by 21 pips (above level)"
  - "Body 84 pips vs 20-day median 47 pips (1.79x)"
  - "Upper wick 6 pips, lower wick 11 pips"
  - "No overlap with prior 3-day range"

linked_levels:
  - kind: PDH
    value: 1.0871
    age_days: 1
    source_primitive: "reference_levels@1.0.0"
linked_prior_scenes: []
linked_future_scenes: []

# Forward-compat fields for V0.1 trap-extreme — null in V0 output
state_machine_id: null
state_at_emission: null
candidate_extreme_timestamp: null
candidate_extreme_price: null
confirmed_extreme_timestamp: null
confirmed_extreme_price: null
marginal_break_pips: null
linked_h4_mss_scene_ids: []
linked_displacement_scene_ids: []
daily_expansion_direction: null

# Review fields — Olya only
review_status: pending_review
olya_label: null
olya_notes: null
olya_corrected_to: null
correction_type: null

# Provenance
created_at: 2026-05-03T08:14:22Z
data_snapshot_sha: 7202a5c4
runtime_backend: none
```

**Design notes:**
- `score` is an internal ranker. Not a probability assertion.
- `machine_observation` is plain English, deterministic, generated without an LLM.
- State-machine fields are reserved nullable for V0.1 — no V0 code populates them.
- All review fields nullable in V0; feedback loop integration is V0.2.

---

## §7. Olya review pack (the V0 deliverable to Olya)

`reports/experiments/V0_OLYA_WP2_CLOSE_THROUGH_REVIEW_PACK_<date>.md` is the
proof point. Named to dock directly into the WP2 sprint conversation.

**Required structure:**

```markdown
# V0 Olya WP2 Close-Through Review Pack — EURUSD Daily, <date_range>

## How to use this pack
[2 sentences: what cartographer is, what we need from Olya, framed as
the answer to her recent "share 2-3 examples" follow-up.]

## Section A — Strong close-through candidates (top 5 per parameter set)

### Candidate A1 — 2026-03-14
- Level: PDH 1.0871 (1 day old, source: reference_levels@1.0.0)
- Close: 1.0892 (21 pips beyond, body 84 pips, 1.79x median)
- Parameter set that flagged this: "default"
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

## Section E — Build-agent notes
- Noisiest heuristic: ___
- False-positive patterns observed: ___
- Suggested next heuristics: ___
- Signal-to-noise spot-check (per G8): ___ obvious-keep / ___ borderline / ___ obvious-noise per heuristic
- Parameter sensitivity summary (per H9): see V0_PARAM_SENSITIVITY.md
```

"Chart context" is a small markdown table of OHLC values for the surrounding
window — V0 does not produce chart images. (V0.1 may.)

---

## §8. Verification gates

Build agent must run and pass these before reporting completion:

| Gate | Check |
| --- | --- |
| G1 — Determinism | Run `scan_range.py` over the V0 window twice. Diff `scene_bank/candidates/`. Zero differences. |
| G2 — Read-only | After a full scan, `git diff` in `~/en1gma`, `~/phoenix-river`, `en1gma-ref/`, `docs/source_methodology/` shows zero changes. |
| G3 — Backend independence | Run scan with `backend=none` and `backend=local` (if local up). Scene set identical. |
| G4 — Coverage | All four V0 heuristics produce ≥1 candidate over the V0 window. (If a heuristic produces zero, flag in V0_NOTES — do not silently relax.) |
| G5 — Schema conformance | Every YAML in `scene_bank/candidates/` validates against `SCENE_SCHEMA.yaml`. |
| G6 — Performance | One full pass over 8 weeks completes in < 60 seconds on M3. |
| G7 — Documentation | `README.md`, `CANDIDATE_ONLY_CONTRACT.md`, `LEVEL_PRIMITIVES.md`, `HEURISTIC_REGISTRY.md`, `RUNTIME.md`, `TESTING.md` all populated. |
| **G8 — Signal-to-noise spot check** | **For each heuristic, build agent randomly samples 10 candidates and hand-rates as obvious-keep / borderline / obvious-noise. Records ratio in V0_NOTES. Build BLOCKED for review if obvious-noise > 30% on any heuristic.** |
| G10 — Port fidelity | Sanity test confirms `cartographer/primitives/reference_levels.py` produces identical PDH/PDL values as the en1gma source for a sample week. |

---

## §9. Out of scope for V0

- `trap_extreme_state_machine` heuristic — deferred to V0.1 (separate packed methodology thread; not blended into WP2 review pack).
- Olya feedback loop integration — V0.2.
- Heuristic update proposals from corrections — V0.2.
- Wiki rendering / web UI — V0.1+ (concept board says wiki is a *layer*, not the primary store).
- Multi-instrument — V0 is EURUSD only.
- M5/M15 timeframes — Daily + H4 (H4 only for heuristic 4.3 in V0).
- Live data sync — V0 uses the frozen snapshot.
- Backtesting / performance metrics — cartographer is not a strategy.
- FVG / OB as primary close-through targets — V0.1 (V0 covers hard levels + swings).
- `level_state` lifecycle ladder — belongs in en1gma.
- Anything en1gma's hard guardrail forbids (see §0.5).

---

## §10. Governance

- **Lab fork.** No merge-back to en1gma without explicit ratification.
- **Brief approval.** Reviewed by **G**, **Olya**, and **Olya's advisor** before the build mission is launched. Changes from review go into the next brief version.
- **Build review checkpoints.** Build agent pauses at three points:
  1. After all four primitives are ported and port-fidelity (G10) passes.
  2. After heuristic logic for all four is implemented (before scan engine).
  3. After the V0 review pack is generated, before declaring done.
- **No autonomous heuristic changes.** If during the build the agent thinks a heuristic should change, it stops and asks. It does not invent methodology.
- **Constitutional alignment with en1gma.** Per §0.5, V0's deliverable is the methodology examples WP2 needs. The brief should be reviewed alongside `docs/source_methodology/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md` so reviewers see the contextual fit.

---

## §11. Reference reading list (priority order)

For the build agent, before writing any code:

1. **`docs/source_methodology/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md`** — the open question V0 addresses. Read first.
2. `cartographer_concept_board.md` — context.
3. `MISSION_INPUTS.md` — repo orientation.
4. `data/README.md` — data schema.
5. `docs/source_methodology/PROVENANCE.md` — what's authoritative.
6. `docs/source_methodology/canonical/MAP_SPATIAL_PRIMER_v1.md` — HTF map concept.
7. `docs/source_methodology/methodology/METHODOLOGY_INDEX.md` — methodology map.
8. `docs/source_methodology/methodology/SYNTHETIC_OLYA_METHOD_vLOCK.yaml` — locked L1 primitives (especially SWING_POINTS, MSS, DISPLACEMENT, REFERENCE_LEVELS).
9. `docs/source_methodology/methodology/STATE_DETECTION_LOGIC_v2.yaml` — HTF phase classifier.
10. `docs/source_methodology/reviews/PHASE_5_C2_OLYA_METHODOLOGY_DIGEST_2026_04_30.md` — current Olya methodology summary.
11. `en1gma-ref/en1gma/console/detection/ra_engine/detectors/reference_levels.py` — port target.
12. `docs/source_methodology/root/calibration_results.yaml` — 27 Olya answers.
13. Olya 2026-05-02 ruling (Q1, Q2) — drafted into `V0_NOTES.md` for inline reference.

---

## §12. Definition of done

- [ ] All nine verification gates (§8) pass.
- [ ] `reports/experiments/V0_OLYA_WP2_CLOSE_THROUGH_REVIEW_PACK_<date>.md` exists, populated, reads cleanly to a non-technical reviewer.
- [ ] `reports/experiments/V0_PARAM_SENSITIVITY.md` shows yield comparison across parameter sets per heuristic.
- [ ] `LEVEL_PRIMITIVES.md` documents what was ported, from where, at what SHA.
- [ ] Repo can be cloned to a fresh machine, `pip install -e .`, `python scripts/seed_data.py`, and `python -m cartographer.scans.run_range 2026-02-15 2026-04-30` produces identical output.
- [ ] All hard rules (§2) hold under spot-check.
- [ ] `V0_NOTES.md` includes: (a) noisiest heuristic, (b) ≥3 false-positive patterns observed, (c) ≥2 suggested next heuristics, (d) signal-to-noise spot-check ratios per G8.
- [ ] No file under `~/en1gma`, `~/phoenix-river`, `en1gma-ref/`, or `docs/source_methodology/` modified.

---

## Appendix A — Architect's framing (preserved verbatim)

The original advisor framing is preserved at `cartographer_concept_board.md`.
Key quote:

> "Cartographer is good. It maps terrain; it does not decide whether to trade."

Values, not requirements. The requirements are §2 (Hard rules) and §3
(Deliverables).

---

## Appendix B — Olya 2026-05-02 ruling extracts (the proximate trigger)

Build agent reproduces these in `V0_NOTES.md` for ground-level reference.

**Q1 close-through ruling:**
> "Close-through requires a strong Daily candle close beyond the relevant
> level or zone boundary. Close-through is a Daily-only object-boundary event.
> 4H MSS/displacement is not part of close-through logic. ... For a bearish
> order block acting as resistance, bullish close-through requires Daily
> close above the top of the OB. For a bullish FVG acting as support, bearish
> close-through requires Daily close below the bottom of the FVG."

**Q2 balance-exit ruling (excerpt):**
> "4H MSS/displacement is used to help identify direction when price is
> leaving Daily balance or consolidation. ... Balance exit only means price
> is leaving compression. Trade permission is separate."

**Trap-extreme question** — captured in `cartographer_concept_board.md` and
in V0.1 planning. **Not addressed by V0** per advisor synthesis (do not blend
into WP2 close-through work).
