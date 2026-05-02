# VAULT
# en1gma — Parked Ideas and Proven Architecture

```yaml
document: VAULT
version: 1.1
date: 2026-03-31
status: CANONICAL
purpose: "Index of deferred capabilities, proven infrastructure, and historical lineage."
rule: "One paragraph per concept. Key principles. Return condition. Pointer. Not a copy."
```

---

## 1. PARKED CONCEPTS

```yaml
bead_field:
  summary: "Crypto-anchored knowledge substrate — bi-temporal, provenance-linked. 564K beads, 66GB."
  principles: ["commitment-based", "bi-temporal", "rejection-rich", "SHA-256 chain + Merkle + PQC signing"]
  status: "built — 274 tests, 789 genesis beads"
  returns_when: "Dream Cycle needs training data from production trading"
  spec: "~/dexter/ — BEAD_FIELD_SPEC_v0_3.md"

dream_cycle:
  summary: "Learning engine — mines rejected trades, simulates counterfactuals, distils strategy configs."
  principles: ["DEC-ENERGY-NOT-STORED (energy over beads, not on them)", "Shadow Field (negative space)", "LeCun/JEPA alignment", "SkillRL"]
  status: "v1 operational, v2 designed"
  returns_when: "6+ months production trading data"
  spec: "~/dexter/ — DREAM_CYCLE_DESIGN_INTENT_v0_1.md"
  hardware: "DGX Sparks (standing by)"

bridge:
  summary: "Pull-based notary — governance events → bead field. 7 modules, 191 tests."
  principles: ["pull-based", "fail-closed", "idempotent"]
  returns_when: "bead field consumed by Dream Cycle"
  spec: "~/dexter/bridge/"

ceremony_engine:
  summary: "Weekly governance attestation — blocks capital if overdue. Evidence-hashed."
  principles: ["bounds-monotonic", "G attests before renewal"]
  returns_when: "paper trading stable, G wants formal review cadence"
  spec: "~/phoenix/governance/"

en1gma Wiki — Living Methodology Brain (Operator-Stage Idea)

Once en1gma is operational and the Map v2 build phase closes, consider commissioning a persistent LLM-maintained wiki as the system’s long-term memory layer. The pattern (per Karpathy’s llm-wiki gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) sits between raw sources (live trade outcomes, regime annotations, Olya methodology rulings, Map state observations, decision logs) and the agents reasoning over them — the wiki is a structured, interlinked, continuously-maintained markdown corpus that compounds rather than re-derives knowledge on every query. A local librarian agent (likely Qwen on the MacBook in a Droid harness, with Obsidian as the human-facing IDE) handles the bookkeeping humans abandon: cross-references, contradiction flags, supersession tracking, stale-claim lint. Scope when commissioned should start narrow — methodology corpus and live operational learnings only — and expand outward from there as value proves itself. Trigger condition: Map v2 operational, Olya validation complete, system in operation stage where new knowledge accumulates from live behavior rather than build decisions. Sequencing principle: start with a one-shot Opus distillation of methodology state to prove value before standing up the daemon. Failure modes to avoid (identified during build stage): premature commissioning while substrate is still moving, scope creep beyond methodology into full repo archaeology, librarian writing back into canonical docs, expansion to fill Droid downtime during active sprints. Related archaeological project worth running once: extract decision-points from old a8ra/earlier-iteration code as a one-shot question-finder, not as wiki ingestion.


cartridge_insertion:
  summary: "N64 slot-in strategy deployment. 8-step insertion + cabinet validation."
  survived: "lease state machine + halt override (in en1gma)"
  superseded: "5-drawer cabinet (replaced by Map + Gate)"
  spec: "~/phoenix/docs/ — CARTRIDGE_AND_LEASE_DESIGN_v1.1.md"

mirror_dashboard:
  summary: "Live EURUSD chart with detection overlays. mirror.a8ra.com (Cloudflare Tunnel)."
  returns_when: "Olya needs observation beyond TradingView"
  spec: "~/dexter/ (Bun + WebSocket server)"

cascade_model:
  summary: "LOKZ-first suppress-NYOKZ cascade for kill zone priority."
  superseded_by: "day-state engine (market-centric, 2-state FSM)"
  date_superseded: "2026-03-31"
  note: "Correct intuition (don't trade twice), wrong mechanism. State > timing."

dmb_canon_v01:
  summary: "DAILY_MOMENTUM_BREAKOUT_CANON.md v0.1 — pre-Map strategy approximation."
  superseded_by: "Map engine + Olya calibration (27/27) + DAILY_EXPANSION YAML"
  date_superseded: "2026-03-31"
  note: "Good early shaping. 12 flagged items resolved by calibration. 8 divergences from locked design."
  location: "methodology/DAILY_MOMENTUM_BREAKOUT_CANON.md"

per_window_parameters:
  summary: "ATR multiples, bar progress limits, aggression tuning per kill zone."
  source: "Olya advisor spec"
  returns_when: "DMB maturation phase, walk-forward data available for KZ-specific tuning"

daily_continuation:
  summary: "DAILY_CONTINUATION child strategy of DAILY_MOMENTUM family."
  gated_by: "day_state == POST_EXPANSION"
  returns_when: "Olya provides chain/entry spec for post-expansion plays"

momentum_continuation_h4_neutral_daily:
  summary: "H4 momentum continuation when Daily is neutral/conflicted. Candidate edge surfaced by trade_011 analysis."
  date_parked: "2026-04-27"
  source: "Phase 4b lane-close trace analysis + Olya/NEX ruling"
  classification: "future cartridge / strategy candidate"
  evidence: "trade_011 (2025-11-28) — Olya reads H4 bullish authority when Daily is conflicted"
  distinction: "NOT a broken DAILY_EXPANSION instance — structurally different edge requiring different regime logic"
  gated_by: "methodology seed validation (MSS_NOT_EQUAL_ACTIVE_CONTROL.md) + multi-fixture confirmation"
  returns_when: "2-3 fixtures confirm the principle + Olya ratifies deterministic rule + cartridge design session"
  note: "Do not mix into DAILY_EXPANSION regime logic. Different edge = different strategy module."
  see: "docs/methodology_seeds/MSS_NOT_EQUAL_ACTIVE_CONTROL.md"
```

---

## 2. PROVEN INFRASTRUCTURE

Built, tested, archived — available for future integration.

```yaml
bead_field_data: "564K beads, 66GB on M3 — audit trail + training data"
bridge_code: "7 modules, 191 tests, 7 invariants — governance→analytical projection"
verification_suite: "7 scripts at ~/dexter/scripts/verification/ — bead field integrity"
research_accelerator: "calibration UI, evaluate.py, sweep.py — methodology proving ground"
phoenix_governance: "1887+ tests, 259 invariants, 273 chaos vectors — governance architecture"
coo_augmentations: "QMD 2.0.1, Superpowers 5.0.2, Ralph Loop 1.0.0 on M3"
```

---

## 3. HISTORICAL RECORD

Sprint history and pre-en1gma system state — reference only.

```yaml
sprint_roadmap: "42 sprints (S28-S70) — full journey record"
system_manifest: "pre-en1gma 4-repo system state"
architecture_audit: "216-file RepoPrompt scan that sparked the en1gma pivot"
unified_roadmap: "S62-S70 forward planning (superseded by FORWARD_PLAN)"
deployment_roadmap: "P0-P3 build plan (completed, superseded)"
location: "~/phoenix-swarm/ and project knowledge archives"
```

---

## 4. SOURCE REPOS — LINEAGE

Where en1gma was extracted from. These repos are read-only reference.

### phoenix

```yaml
path: "~/phoenix"
role: "governance architecture proof bank"
extracted: "halt, lease, paper broker, position, gate registry"
remaining: "ceremony, 5-drawer CSO, 10-step orchestrator, enrichment (all superseded)"
tests: "1887+"
```

### dexter

```yaml
path: "~/dexter"
role: "detection and methodology proof bank"
extracted: "tf_aggregator, state classifier concepts"
remaining: "bead field, bridge, dream cycle, mirror, producer framework"
tests: "1122+"
```

### research_accelerator

```yaml
path: "~/research_accelerator"
role: "methodology oracle and calibration proving ground"
extracted: "detect.py, ARS simulator, annotated trades"
remaining: "calibration UI, evaluate.py, sweep.py"
status: "LIVING REFERENCE — still used for future calibration"
```

### phoenix-swarm

```yaml
path: "~/phoenix-swarm"
role: "coordination archive"
extracted: "vLOCK.yaml, STATE_DETECTION_LOGIC, cluster manifest"
remaining: "office CLAUDE.md files, sprint briefs, ansible playbooks"
```

---

*"Nothing lost. Nothing wasted. Everything indexed."*
