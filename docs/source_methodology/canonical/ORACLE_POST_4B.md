# ORACLE POST-4B

```yaml
document: ORACLE_POST_4B
version: 1.0
date: 2026-04-27
status: CANONICAL_SNAPSHOT_CANDIDATE
owner: CTO (maintained), G (approval authority)
approval_state: "drafted per G request; pending explicit final ratification"
audience: CTO, Chief Architect, advisors, future agents
purpose: |
  Dense agent orientation after Phase 4b lane close and walk-forward
  re-validation. Compresses system shape, authority surfaces, current
  certification, known doctrine gaps, and next architectural moves.
rule: |
  This is an orientation snapshot, not a live roadmap, evidence ledger,
  invariant encyclopedia, or closed-mission proof. If this conflicts
  with the owner docs, the owner docs win.
size_intent: "dense, precise, not verbose"
```

```yaml
source_of_truth_hierarchy:
  live_orientation: CLAUDE.md
  live_roadmap: docs/canonical/FORWARD_PLAN.md
  evidence_state: docs/canonical/CERTIFICATION_STATE.md
  architecture_boundary: docs/canonical/CARTRIDGE_CONTRACT.md
  spatial_doctrine: docs/canonical/MAP_SPATIAL_PRIMER_v1.md
  strategic_why: docs/canonical/NORTH_STAR.md
  parked_future: docs/canonical/VAULT.md
  lane_close_proof: docs/reviews/PHASE_4B_LANE_CLOSE_RATIFICATION_2026_04_27.md
  phase_4_decision_origin: docs/archive/PHASE_4_RATIFICATION.md
  methodology_seed: docs/methodology_seeds/MSS_NOT_EQUAL_ACTIVE_CONTROL.md
  prior_snapshot_reference: docs/archive/POST_PHASE_3_ORACLE.md
staleness_policy: |
  Prefer file-level references. Do not treat old oracle line refs, old
  test counts, old branch state, or old SW candidate labels as live.
  Re-check code directly before briefing implementation.
```

---

## 1. Current status banner

```yaml
phase: POST_PHASE_4B_LANE_CLOSE
system_status: OPERATIONAL
certification_level: PROVISIONALLY_STABLE_WITH_KNOWN_DOCTRINE_GAP
pair: EUR/USD
core_principle: "Human frames. Machine computes. Human promotes."

phase_4b_lane_close:
  status: CLOSED_AT_11_OF_12
  target: "12/12 DAILY_EXPANSION chart-truth"
  achieved: "11/12 GREEN"
  blocked_fixture: trade_011
  blocked_reason: BLOCKED_BY_METHODOLOGY_SEED
  proof: docs/reviews/PHASE_4B_LANE_CLOSE_RATIFICATION_2026_04_27.md

walk_forward:
  status: PROVISIONAL_STABILITY_ESTABLISHED
  window: "2021-01-01 -> 2026-03-20"
  trading_days: 1633
  trades: 88
  fallback_trades: 0
  init_failures: 0
  evidence_owner: docs/canonical/CERTIFICATION_STATE.md

known_gap:
  name: MSS_NOT_EQUAL_ACTIVE_CONTROL
  status: SEED_NOT_INVARIANT_NOT_IMPLEMENTATION_SPEC
  summary: |
    The regime engine currently has no NEUTRAL state once any Daily MSS
    exists. It cannot represent "Daily MSS exists but no longer governs."
  owner: docs/methodology_seeds/MSS_NOT_EQUAL_ACTIVE_CONTROL.md

phase_4_posture:
  rule_source: docs/archive/PHASE_4_RATIFICATION.md
  default: "No new strategy capability unless G/CTO explicitly revise or retire Phase 4 scope."
  current_work_bias: "truth enforcement, ambiguity reduction, fail-closed discipline, certification hygiene"

repo_state_note: |
  Live docs record merge_status as merged_to_main_on_2026-04-27 while
  some repo_state fields still say observed_head: pending_merge_commit.
  Treat deployment/main reconciliation as a live-roadmap item if touched;
  do not infer branch truth from this snapshot.
```

---

## 2. 30-second mental model

en1gma is a **CONSOLE + CARTRIDGE** system.

```yaml
console:
  definition: "strategy-blind ICT machinery"
  owns:
    - data ingestion and timeframe aggregation
    - detection primitives and detect.py facade
    - HTF Map / spatial context
    - LTF execution chain
    - canon runtime
    - governance, execution, observability
  rule: "Console code must not branch on cartridge names."

cartridge:
  definition: "YAML-only strategy declaration"
  owns:
    - identity
    - map_required
    - regime / phase / PDA / day-state requirements
    - chain parameters
    - execution windows
    - governance/risk config
    - optional canon_algorithm selection
  rule: "New cartridge should not require console code changes unless a new universal console capability is explicitly scoped."

one_sentence: |
  A constitutional trading kernel that reads market structure, holds
  persistent spatial context, and executes only when structure and
  context align under sovereign human governance.
```

```yaml
two_clocks:
  Map:
    speed: SLOW
    question: "Where should we watch, and in which direction?"
    character: "persistent, structural, quiet; updates only on structural events"
  Chain:
    speed: FAST
    question: "How do we enter right now at this approved location?"
    character: "per-bar inside kill zones; activates only when Map/Gate arms"

two_paths:
  ARS:
    cartridge: en1gma/cartridges/ars_v1_3.yaml
    map_required: false
    path: "canon algorithm -> governance -> broker"
  DAILY_EXPANSION:
    cartridge: en1gma/cartridges/daily_expansion.yaml
    map_required: true
    path: "detect -> Map -> Gate -> Chain -> Intent -> Governance -> Broker"

singletons:
  detection_oracle: en1gma/console/detection/detect.py
  governance_authorization_site: en1gma/console/governance/governance.py::check_governance
  architecture_boundary: docs/canonical/CARTRIDGE_CONTRACT.md
```

---

## 3. What changed since Post-Phase-3

`docs/archive/POST_PHASE_3_ORACLE.md` is now a snapshot reference only. Its code geography remains useful as shape, but status pointers, line refs, open-item priorities, and some hazard labels are stale after Phase 4b.

```yaml
phase_4b_landed_work:
  SW31:
    area: console/chain
    summary: "Displacement grade filter in chain_evaluator.py"
    effect: "STRONG eligible; VALID/WEAK require HTF alignment; unknown ineligible"
  SW50:
    area: console/map
    summary: "H4 cascade replay fidelity plumbing in map_engine.py"
    effect: "replay_price_forward can route H4 bars when DR authority is H4"
  SW58a:
    area: console/map
    summary: "Displacement-only regime init stamps FALLBACK"
    effect: "existing gate refusal now catches sparse-evidence authority construction"
  SW58b1:
    area: orchestrator + map canon session
    summary: "HTF warmup 45 -> 90 days"
    effect: "captures recent regime-defining MSS evidence without future leak"
  SW58b1_test:
    area: tests
    summary: "explicit no-lookahead guard for 90-day warmup"

resulting_truth:
  chart_truth: "11/12 GREEN; trade_011 intentionally visible"
  fallback_surface: "FALLBACK construction mode now honest and refused"
  walk_forward: "5+ years re-run; provisional stability established"
  restraint: "No single-fixture Daily-control/H4-cascade mechanization"
```

Architectural reading: Phase 4b did **not** make the system fully epistemically certified. It made the current Daily-authority implementation honest enough to be provisionally stable, while exposing a known methodology gap that remains unimplemented.

---

## 4. Code geography / architecture spine

```yaml
repo_spine:
  en1gma/console/data:
    layer: L1_DATA
    owns: "bar types, River loading, timeframe aggregation"
  en1gma/console/detection:
    layer: L2_DETECTION
    owns: "detect.py facade + vendored ra_engine primitives"
  en1gma/console/map:
    layer: L3_MAP
    owns: "regime, dealing range, PDA lifecycle, day_state, MapState persistence"
  en1gma/console/chain:
    layer: L4_CHAIN
    owns: "gate, chain evaluator, chain config/types, canon runtime"
  en1gma/console/governance:
    layer: L5A_GOVERNANCE
    owns: "halt, lease, risk, validate_config, check_governance"
  en1gma/console/execution:
    layer: L5B_EXECUTION
    owns: "CanonIntent, intent building, broker adapter, position"
  en1gma/cartridges:
    layer: CARTRIDGE_DECLARATIONS
    owns: "YAML strategies + loader/schema conversion"
  en1gma/orchestrator:
    layer: TOP_WIRING
    owns: "entry-path wiring only; no methodology decisions"
  en1gma/observe:
    layer: CROSS_CUTTING_CONSUMER
    owns: "decision traces, replay shims, map timeline, schemas"
  en1gma/scripts:
    layer: ENTRYPOINTS_OPS
    owns: "run_ars_session, run_map_session, run_walk_forward, sentinel, health checks"
  en1gma/methodology:
    layer: READ_ONLY_REFERENCE
    owns: "vLOCK/canon references and calibration artifacts"
  en1gma/tests:
    layer: PROOF_SURFACE
    owns: "unit, contract, integration, parity, ops tests"
```

```yaml
import_boundary_contracts:
  source: pyproject.toml
  checker: "lint-imports --config pyproject.toml"
  active_shape:
    - "console must not import cartridges"
    - "console data-flow layers: chain > map > detection > data"
    - "governance and execution are peers"
    - "orchestrator is top layer; lower layers do not import it"
    - "observe is cross-cutting consumer; console does not import it"
    - "chain -> execution boundary is restricted to intent handoff types"
  placeholder:
    - "cartridges independent of each other activates when per-cartridge Python modules exist"

mypy_posture:
  source: pyproject.toml
  kernel: "strict"
  deferred:
    tests: "Tier 1 annotation debt"
    vendored_ra_engine: "Tier 2 parity/upstream-gated"
    utility_scripts: "Tier 3 calibration/run_discovery_scan/henry_analyst"
  strict_operational_surface:
    - en1gma/scripts/run_ars_session.py
    - en1gma/scripts/run_map_session.py
    - en1gma/scripts/sentinel.py
    - en1gma/scripts/health_check.py
```

---

## 5. Execution paths

### 5.1 ARS path

```yaml
path: ARS
cartridge: en1gma/cartridges/ars_v1_3.yaml
map_required: false
canon_runner: en1gma/console/chain/canon/ars/runner.py::ARSRunner
registry: en1gma/console/chain/canon/registry.py::CANON_RUNNERS
core_algorithm: en1gma/console/chain/canon/ars/ars_canon.py
state: en1gma/console/chain/canon/ars/session_state.py
checkpoint_recovery:
  - en1gma/console/chain/canon/ars/checkpoint.py
  - en1gma/console/chain/canon/ars/recovery.py
entrypoint: en1gma/scripts/run_ars_session.py
batch_orchestration: en1gma/orchestrator/orchestrator.py
converges_at: check_governance -> broker
orientation: |
  ARS is a self-contained canon algorithm. It bypasses Map, carries its
  own session state/checkpoint/recovery machinery, and should remain
  protected by parity and replay discipline when touched.
```

### 5.2 DAILY_EXPANSION / Map-gated path

```yaml
path: DAILY_EXPANSION
cartridge: en1gma/cartridges/daily_expansion.yaml
map_required: true
entrypoint: en1gma/scripts/run_map_session.py
orchestration: en1gma/orchestrator/map_orchestrator.py
runner: en1gma/console/chain/canon/map_canon/runner.py::MapCanonRunner
session_core: en1gma/console/chain/canon/map_canon/session.py::_run_map_session
flow:
  - load strategy YAML via en1gma/cartridges/loader.py
  - load HTF lookback bars with 90-day warmup policy
  - run detection through detect.py / ra_engine
  - initialize MapEngine from historical HTF evidence
  - hold MapState: regime, dealing range, active PDAs, construction_mode
  - evaluate Gate at kill-zone bars
  - if ARMED, run ChainEvaluator
  - if chain completes, build CanonIntent
  - call check_governance
  - route to broker / position surface
trace_surfaces:
  - en1gma/console/chain/canon/map_canon/trace_schema.py
  - en1gma/observe/map_timeline.py
```

```yaml
current_authority_scope:
  daily_authority: PROVISIONALLY_STABLE_DAILY_AUTHORITY_WITH_KNOWN_NEUTRAL_GAP
  h4_authority_cascade: NOT_CERTIFIED_AS_ACTIVE_REGIME_AUTHORITY
  neutral_daily_state: NOT_IMPLEMENTED
  pda_scope_v1: "FVG only"

important_distinction: |
  SW50 improved H4 replay fidelity plumbing for cases where H4 bars must
  be routed. It did not certify or implement a general H4-primary regime
  authority path for trade_011-style Daily-neutral cases.
```

---

## 6. Map / chain semantics to preserve

```yaml
map_v1_locked_semantics:
  source: docs/canonical/MAP_SPATIAL_PRIMER_v1.md + CARTRIDGE_CONTRACT
  principles:
    - "Map is spatial picture, not checklist"
    - "Map never fires a trade"
    - "Execution never decides direction"
    - "Direction permission comes from Map"
    - "Execution trigger comes from LTF confirmation at a map-approved location"
    - "dealing range measured wick-to-wick"
    - "dealing range rolls/supersedes inside regime"
    - "PDA midpoint vs DR equilibrium classifies PREMIUM/DISCOUNT"
    - "TOUCHED is permanent"
    - "no age expiry; structure invalidates structure"
    - "PDA created at confirmation, not anchor"
    - "v1 PDA scope is FVG"

gate_all_required_for_armed:
  - "regime.direction != NEUTRAL"
  - "active PDA exists in correct zone"
  - "PDA direction_context matches regime.direction"
  - "price contacts PDA zone on the bar"
  - "current time is inside configured kill zone"
  - "map_state.construction_mode == OK"

chain_topology:
  fixed_sequence: "sweep -> MSS -> FVG -> OTE -> entry"
  current_hygiene_issue: "114 unknown near-miss diagnostics need classification or explicit justification"
```

---

## 7. Certification state snapshot

Full evidence belongs in `docs/canonical/CERTIFICATION_STATE.md`. This section is only the agent-orientation headline.

```yaml
walk_forward_run:
  date_run: 2026-04-27
  window: "2021-01-01 -> 2026-03-20"
  warmup: "90 days"
  script: en1gma/scripts/run_walk_forward.py
  command: "python -m en1gma.scripts.run_walk_forward --start 2021-01-01 --end 2026-03-20 --workers 4"
  output: reports/walk_forward_2021_2026.yaml
  days: 1633
  wall_time: "~7055s / 117.6min"

headline_numbers:
  total_days: 1633
  construction_mode:
    OK: 1564
    FALLBACK: 69
    FAILED: 0
  init_failed: 0
  authority_tf:
    DAILY: 1633
    H4: 0
  gate_armed: 706
  chain_complete: 88
  trades: "88 (48W / 40L, 54.5% WR, +56R)"
  max_consecutive_losses: 3

validated_surfaces:
  FALLBACK_refusal:
    status: VALIDATED
    evidence: "69 FALLBACK days; zero FALLBACK trades"
  Map_initialization:
    status: VALIDATED
    evidence: "0 init failures across 1,633 trading days"
  trade_distribution_stability:
    status: SANITY_SIGNAL_ONLY
    evidence: "11-22 trades/year, both directions, both kill zones"
  regime_phase_alternation:
    status: VALIDATED
    evidence: "EXPANSION / RETRACE balance not pathologically skewed"

not_validated_or_not_certified:
  strategy_edge: "Do not treat +56R as certified edge or optimization authority."
  NEUTRAL_regime: "0 NEUTRAL days; no neutral-control path implemented."
  H4_authority: "0 H4 authority days; future H4 cascade not covered."
  unknown_taxonomy: "114 unknown near-misses remain pending hygiene."
```

Upgrade target:

```yaml
TRACE_CERTIFIED_DAILY_AUTHORITY_V1:
  all_required:
    - "unknown near-miss count reduced to zero or residuals explicitly justified"
    - "walk-forward re-run preserves headline distribution after cleanup"
    - "FALLBACK direction reporting separated from valid OK regime direction"
  not_required:
    - "NEUTRAL regime implementation"
    - "H4 cascade authority"
    - "long-side weakness resolution"
    - "P&L optimization"

FULLY_EPISTEMICALLY_CERTIFIED:
  phase: "Phase 5+ gate"
  additionally_requires:
    - "MSS_NOT_EQUAL_ACTIVE_CONTROL resolved from multi-fixture evidence"
    - "NEUTRAL regime state implemented"
    - "H4 cascade authority implemented if methodology ratifies it"
    - "14/14 chart-truth including trade_011"
    - "Olya extreme-confidence checkpoint"
```

---

## 8. Known doctrine gap: MSS ≠ Active Control

```yaml
seed: docs/methodology_seeds/MSS_NOT_EQUAL_ACTIVE_CONTROL.md
status: METHODOLOGY_SEED_ONLY
observed_fixture: trade_011 / 2025-11-28
phase_4b_disposition: BLOCKED_BY_METHODOLOGY_SEED
not_an_invariant: true
not_an_implementation_spec: true

principle: |
  A Daily MSS can be valid historically but no longer govern active
  directional control if continuation fails, opposing HTF PDA reactions
  persist, or Daily structure becomes conflicted/unresolved.

current_system_limitation: |
  Regime initialization has two effective paths: Daily MSS -> BULLISH or
  BEARISH OK, or no Daily MSS -> displacement FALLBACK refused. There is
  no third path for "Daily MSS exists but no longer governs."

trade_011_shape:
  expected_by_chart_truth:
    daily_direction: NEUTRAL
    authority_tf: H4
    htf_phase: RANGE
  current_system_output:
    daily_direction: BEARISH
    authority_tf: DAILY
    htf_phase: RETRACE
  interpretation: |
    Honest chart-truth gap. Not safe to patch from one fixture. May be
    future regime-engine doctrine or a separate H4 momentum-continuation
    cartridge; this distinction is unresolved.
```

```yaml
explicit_prohibitions:
  - "Do not implement Daily-control-check from trade_011 alone."
  - "Do not register INV-PRIMARY-AUTHORITY-REQUIRES-ACTIVE-CONTROL yet."
  - "Do not register INV-LOWER-TF-CASCADE-ONLY-AFTER-PRIMARY-NEUTRAL yet."
  - "Do not alter trade_011 expected state to match current code."
  - "Do not use latest-wins, net-count, or ad hoc H4 MSS heuristics."
  - "Do not treat H4 as higher priority than Daily. Daily control check comes first."

required_next_step:
  - "Collect 2-3 additional fixtures exercising MSS exists but no longer governs."
  - "Return to Olya with multi-fixture evidence."
  - "Mechanize only after deterministic rule + Olya confidence + CTO brief."
```

---

## 9. Invariant / authority index

This is an index, not the full invariant text.

```yaml
sovereignty_and_safety:
  owners:
    - CLAUDE.md
    - docs/canonical/NORTH_STAR.md
    - code/tests
  key_rules:
    - "Human sovereignty over capital is absolute."
    - "Halt overrides all."
    - "Live execution requires human T2 approval."
    - "Every trade passes through governance."
    - "check_governance() is the single authorization site."
    - "Olya's NO on methodology/detection is final."

cartridge_boundary:
  owner: docs/canonical/CARTRIDGE_CONTRACT.md
  key_rules:
    - "cartridges are pure declarations"
    - "console is strategy-blind"
    - "no cartridge-shaped console branches"
    - "new cartridge should not require console changes"
    - "canon runtime is console infrastructure"
    - "trace determinism by cartridge"
    - "structural refactor must not drift semantics"
    - "scope + effect must be declared for briefs/rulings/changes"

map_and_chain_methodology:
  owners:
    - docs/canonical/MAP_SPATIAL_PRIMER_v1.md
    - docs/canonical/CARTRIDGE_CONTRACT.md
    - ratification docs
  key_rules:
    - "PDA creation at confirmation"
    - "PDA direction fidelity"
    - "PDA zone from detector / EQ relationship"
    - "PDA mitigation is retrace-fill and has a single ownership site"
    - "day_state is market-driven and Map-coherent"
    - "HTF includes cascade pair, but current Daily-authority certification does not certify H4 regime authority"
    - "chain sequence fixed"
    - "Map behavior from methodology, not config toggles"
    - "FVG causal identity and chain FVG causal selection"

epistemic_integrity_family:
  owner: docs/archive/PHASE_4_RATIFICATION.md
  evidence_owner: docs/canonical/CERTIFICATION_STATE.md
  parent: INV-EPISTEMIC-INTEGRITY
  children:
    - INV-SYSTEM-NO-STATE-INVENTION
    - INV-MAP-CONSTRUCTION-MODE-EXPLICIT
    - INV-GATE-REFUSES-FALLBACK-MAP
    - INV-UNKNOWN-STATE-HALTS
    - INV-NO-EVIDENCE-NO-TRADE
    - INV-REGIME-FROM-METHODOLOGY-NOT-FALLBACK
  peers:
    - INV-FIDELITY-ANCHORED-TO-CHART-TRUTH
    - INV-STRATEGY-CONFIG-SINGLE-SOURCE
    - INV-CARTRIDGE-ABSENCE-IMPLIES-NO-TRADE
```

---

## 10. Live work index for next architects

Do not turn this section into a mission ledger. Live status lives in `FORWARD_PLAN.md`.

```yaml
as_of: "2026-04-27; mirrors FORWARD_PLAN v2.5 for orientation only"
authority: "docs/canonical/FORWARD_PLAN.md remains the live roadmap"
priority_now:
  1_unknown_near_miss_taxonomy_cleanup:
    purpose: "Make chain refusal diagnostics deterministic."
    current_metric: "114 unknown near-misses"
    target: "0 unknown or explicitly justified residual count"
    default_scope: "diagnostics/reporting first; behavior change only if separately proven/scoped"
    dependency_for: TRACE_CERTIFIED_DAILY_AUTHORITY_V1

  2_fallback_direction_reporting_cleanup:
    purpose: "Keep placeholder FALLBACK direction out of valid regime analytics."
    target: "valid_regime_direction excludes construction_mode != OK"
    dependency_for: TRACE_CERTIFIED_DAILY_AUTHORITY_V1

  3_walk_forward_rerun_after_cleanup:
    purpose: "Regression gate after taxonomy/reporting cleanup."
    expected_shape: "same headline distribution, cleaner refusal surface"

  4_deployment_merge_state_reconciliation:
    purpose: "Resolve branch/main/M3 state if still inconsistent in live docs."
    gate: "chart truth, ARS parity, mypy, lint-imports, doc repo_state coherence"

  5_MSS_NOT_EQUAL_ACTIVE_CONTROL_fixture_collection:
    purpose: "Determine whether trade_011 principle generalizes."
    target: "2-3 additional fixtures"
    hard_rule: "No mechanization until Olya ratifies deterministic multi-fixture rule."

next_horizon_design_only:
  SW38_SW43_schema_v2_cluster:
    status: DESIGN_SESSION_GATED
    includes:
      - "map-required canon_runner / params schema"
      - "CANON_RUNNERS dispatch convergence"
      - "BrokerProtocol + IntentBuilderProtocol formalisation"
      - "AuthorityTF redesign"
      - "daily_expansion.yaml schema migration"
  SW52_semantic_detection_parity:
    status: DEFERRED
    return_condition: "CTO-authored adapter/event-identity/tolerance design"
  SW44:
    status: PARKED_OR_LOW_PRIORITY_BY_TIER
    caution: "henry_analyst latent-defect candidate before mechanical annotations"
```

---

## 11. Hard prohibitions / failure modes

```yaml
do_not:
  - "Do not optimize P&L from provisional walk-forward numbers."
  - "Do not claim edge certification from +56R."
  - "Do not treat trade_011 as a simple bug."
  - "Do not implement single-fixture methodology inference."
  - "Do not add new strategy capability under active Phase 4 posture without explicit G/CTO reprioritization."
  - "Do not create cartridge-specific branches inside console code."
  - "Do not hide missing evidence behind plausible defaults."
  - "Do not conflate no qualifying setup with cannot determine."
  - "Do not use archived oracle line refs as live implementation authority."
  - "Do not delete closed-history detail without ratification/archive/finding pointer."

stop_and_escalate_if:
  - "A change cannot be classified against CARTRIDGE_CONTRACT scope/effect."
  - "A methodology question requires Olya judgment."
  - "A fallback path would produce OK authority without detector/methodology evidence."
  - "A brief proposes H4 authority or NEUTRAL regime from trade_011 alone."
  - "A change alters Map/Chain behavior while pretending to be reporting-only."
```

---

## 12. Pointer map

```yaml
read_for_system_orientation:
  - CLAUDE.md
  - docs/canonical/NORTH_STAR.md

read_for_dense_post_4b_snapshot:
  - docs/canonical/ORACLE_POST_4B.md

read_for_next_actions:
  - docs/canonical/FORWARD_PLAN.md

read_for_certification_evidence:
  - docs/canonical/CERTIFICATION_STATE.md
  - reports/walk_forward_2021_2026.yaml

read_for_architecture_boundary:
  - docs/canonical/CARTRIDGE_CONTRACT.md
  - pyproject.toml

read_for_spatial_methodology:
  - docs/canonical/MAP_SPATIAL_PRIMER_v1.md
  - en1gma/methodology/HTF_MAP_SPEC_v0_1.yaml
  - calibration_results.yaml

read_for_lane_close_proof:
  - docs/reviews/PHASE_4B_LANE_CLOSE_RATIFICATION_2026_04_27.md

read_for_phase_4_scope:
  - docs/archive/PHASE_4_RATIFICATION.md

read_for_doctrine_gap:
  - docs/methodology_seeds/MSS_NOT_EQUAL_ACTIVE_CONTROL.md

read_for_parked_future:
  - docs/canonical/VAULT.md

read_for_old_code_map_shape_only:
  - docs/archive/POST_PHASE_3_ORACLE.md
```

---

## 13. Final orientation checksum

```yaml
if_you_only_remember_twelve_things:
  1: "en1gma is CONSOLE + CARTRIDGE."
  2: "Map is spatial context; Chain is execution confirmation."
  3: "Map never fires; Execution never decides direction."
  4: "detect.py is the sole detection oracle."
  5: "check_governance() is the sole authorization site."
  6: "Phase 4b closed honestly at 11/12, not fragily at 12/12."
  7: "Walk-forward proved provisional stability, not certified edge."
  8: "FALLBACK is now explicit and refused; zero FALLBACK trades in 5+ years."
  9: "NEUTRAL Daily regime and H4 authority cascade are not implemented/certified."
  10: "trade_011 is methodology seed territory, not implementation authority."
  11: "Next certification upgrade is diagnostics/reporting hygiene + rerun."
  12: "When in doubt, preserve chart truth, fail closed, and ask Olya before mechanizing methodology."
```

*ORACLE_POST_4B v1.0 — current dense snapshot after Phase 4b lane close and walk-forward re-validation. Live plan lives in FORWARD_PLAN. Evidence lives in CERTIFICATION_STATE. Methodology truth belongs to Olya.*
