# CLAUDE.md - en1gma Kernel
# The First Deployable Trading Kernel

```yaml
system: en1gma
type: Constitutional Algorithmic Trading Kernel
pair: EUR/USD
version: 0.28 (Phase 5 Day 2026-05-01 evening; Droid multi-role relay rhythm added; no producer)
date: 2026-05-01
status: OPERATIONAL | PHASE_5_C2_WP2_GAP_REPORT_RATIFIED_NO_PRODUCER
owner: G (Sovereign Operator)
methodology_authority: Olya (Chief Strategy Officer)
principle: "Human frames. Machine computes. Human promotes."

orientation_target:
  max_read_time: "<15 minutes"
  size_target: "<12k words"
  rule: |
    This file orients. It is not the sprint ledger, invariant encyclopedia,
    walk-forward evidence table, or closed-mission archive.
```

---

## 0. Droid Operating Workflow

```yaml
operating_model: SINGLE_VISIBLE_CTO_ORCHESTRATOR_WITH_READ_ONLY_ADVISORY_RELAY
purpose: "Optimize Droid as the main harness while preserving constitutional authority boundaries."

truth_stack:
  canon_persistent:
    - CLAUDE.md
    - docs/canonical/FORWARD_PLAN.md
    - docs/canonical/CERTIFICATION_STATE.md
    - current docs/handovers/* handoff
  sprint_packet_active: "bounded task packet / review packet for the current slice"
  transcripts_disposable: "never source of truth; summarize into packets instead of stuffing context"

roles:
  G:
    authority: "scope, ratification, veto, phase/capital decisions, Olya dispatch"
  Olya:
    authority: "methodology truth; addressed only via G; never an agent relay slot"
  CTO_GPT55_orchestrator:
    authority: "visible control plane; drafts briefs, executes or delegates inside G-approved scope"
    must_not: "self-ratify, invent methodology, expand scope by implication"
  Chair_Opus:
    authority: "read-only governance challenge: PASS | CONDITIONAL | BLOCK"
    must_not: "implement, mutate canon, authorize work"
  Chief_Architect_GPT:
    authority: "read-only synthesis, operator packet, next-slice proposal"
    must_not: "become second CTO or mutate canon"
  Scribe:
    authority: "read-only state hygiene, stale-anchor scans, bounded handoff packets"
    must_not: "interpret methodology, decide next gate, quietly rewrite canon"
  Code_Engineer:
    authority: "implementation delegate only under G-ratified scope and CTO-issued brief"
    must_not: "cross non-authorized scope or make methodology decisions"

state_hygiene_rhythm:
  before_slice:
    - "fetch origin"
    - "record branch, local HEAD, origin/main, pushed_status"
    - "confirm clean worktree or explicitly name dirty paths"
    - "name the active artifact owner/path"
  during_slice:
    - "one active packet per slice"
    - "all role reports state blockers, required_changes, optional_tightenings, and role_boundary_held"
    - "Chair/Architect/Scribe are read-only by default"
  after_slice:
    - "run relevant validators/scans"
    - "commit, push, archive, or discard deliberately"
    - "label final state: clean | dirty | committed_local | pushed | archived | discarded"
    - "canon refresh only after ratified state change"

hard_rules:
  - "transport automation is not dispatch authority"
  - "repo visibility can be broad; repo write authority stays narrow"
  - "advisory output never becomes canon without G-ratified state change"
  - "no ambiguous local-only artifacts before real external dispatch"
  - "archive or supersede stale MD drafts under explicit docs-hygiene scope; do not sprawl near-duplicates"
```

---

## 1. Current Status

```yaml
certification:
  level: TRACE_CERTIFIED_DAILY_AUTHORITY_V1
  scope: "Current runtime Daily-authority path only; Map v2 producer/runtime is not implemented or certified"
  evidence_home: docs/canonical/CERTIFICATION_STATE.md
  walk_forward: "2021-01-01 -> 2026-03-20; 1,633 trading days; 88 trades; zero FALLBACK trades; raw_unknown_near_misses=0"
  chart_truth: "11/12 GREEN; trade_011 BLOCKED_BY_METHODOLOGY_SEED"
  ratification: docs/reviews/POST_4B_H1_DIAG_UNKNOWN_CHAIN_REASON_RATIFICATION_2026_04_28.md

phase_transition:
  phase_4_status: CLOSED_BY_G_RATIFICATION
  phase_5_status: ACTIVE_DESIGN_LANE_LIVE_NO_PRODUCER
  phase_5_candidate_thesis: HTF_MAP_V2
  decision_owner: G
  decision_brief: docs/reviews/PHASE_4_CLOSE_PHASE_5_OPEN_DECISION_BRIEF_2026_04_29.md
  status: G_RATIFIED_APPROVED_WITH_BOUNDARIES
  stage_1_brief: docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md
  stage_1_status: FROZEN_BY_G_APPROVAL
  stage_2A_status: INERT_READ_MODEL_TRACE_SNAPSHOT_SHELL_PUSHED
  stage_2B_status: CONSTRUCTION_REPLAY_HARNESS_PUSHED
  stage_1A_balance_status: BALANCE_MARKET_STATE_CONTRACT_AMENDMENT_RATIFIED_AND_PUSHED
  stage_2C_status: BALANCE_ENUM_TYPE_TEST_AND_FIXTURE_EXTENSION_PUSHED
  c2_preflight_status: PRODUCER_DESIGN_PREFLIGHT_PUSHED
  c2_methodology_status: OLYA_VERBATIM_ARCHIVED_AND_DIGEST_PUSHED
  c2_olya_bundled_digest_status: OLYA_BUNDLED_DIGEST_RATIFIED_AT_7ad7833
  c2_design_scoping_status: MAP_V2_PRODUCER_DESIGN_SCOPING_RATIFIED_AT_3d09e8b
  c2_wp1_contract_delta_preflight_status: RATIFIED_AT_6002d6f
  c2_wp2_primitive_gap_brief_status: RATIFIED_AT_c9ff53e
  c2_wp2_gap_report_status: RATIFIED_AT_ef185f8
  c2_brief_authorization_status: FIRST_PRODUCER_SLICE_BRIEF_BOUNDARY_RATIFIED_AND_PUSHED
  c2_execution_authorization_status: FIRST_SLICE_EXECUTION_BOUNDARY_RATIFIED_AND_PUSHED
  stage_2D_status: TWO_INERT_FIXTURES_LANDED_NO_PRODUCER
  stage_2D_first_fixture_status: FIRST_INERT_BALANCE_FIXTURE_LANDED_AT_8d67740
  stage_2D_second_fixture_status: SECOND_INERT_NOT_BALANCE_RETRACE_FIXTURE_LANDED_AT_6d4e5d6
  stage_2D_canon_content_refresh: 20f06735fe5f3e8372940cd82e547c9a4ed121d5
  stage_2D_canon_anchor_patch: 470c44c0e70b1cc5da41195c3a397b2c4c41f8ba
  c4_anchor: docs/canonical/PHASE_5_KICKOFF_CLOSE_2026_04_29.md
  hard_guardrail: "Stage 2D fixtures and C2 design scoping are inert/design-only; delivery_quality and level_state require a future explicit G-ratified contract amendment before any output change; no MapV2Engine producer, runtime consumption, consumer path, schema/cartridge change, strategy migration, v2 certification, paper-trading claim, trade_011 resolution/canonicalization, daily_momentum or daily_decisive primitive implementation/extension, threshold invention, lower-timeframe confirmation logic, Q4/Q5/Q6 operationalization, acceptance/strong-close-through proxy, followthrough activation gate, third fixture, existing-surface-sufficient claim, new-primitive-required claim, or implementation/design next gate is authorized."

htf_map_v0_14:
  role: METHODOLOGY_AND_DESIGN_INPUT_ONLY
  source: docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md
  design_brief: docs/reviews/HTF_MAP_v0_14_DESIGN_BRIEF_DRAFT_2026_04_29.md
  supersedes: [v0.13, v0.12, v0.11]
  current_runtime_effect: NONE
  certification_transfer: "V1 certification does not transfer to Map v2."
  future_certification: TRACE_CERTIFIED_DAILY_AUTHORITY_V2_PENDING_AFTER_IMPLEMENTATION_AND_REPLAY
  boundary:
    - "Daily authority only for core Map v2 direction."
    - "H4 is strategy-specific only; not core Map authority, not global alignment, not conflict state."
    - "PD/quadrant location is Map label output; strategy owns any PD gating."

known_v1_doctrine_gap:
  seed: docs/methodology_seeds/MSS_NOT_EQUAL_ACTIVE_CONTROL.md
  summary: |
    The current v1 runtime regime engine has no NEUTRAL state once any Daily
    MSS exists. v0.14 addresses the future Map v2 direction/actionability split,
    but that design is not live runtime until Map v2 producer/runtime is
    implemented, replayed, and recertified.
  rule: "Do not patch v1 or author C2/producer work from this orientation note."

cartridge_lifecycle:
  protocol: docs/canonical/CARTRIDGE_LIFECYCLE_PROTOCOL.md
  status: "v0.2 remains in force."
  phase_5_note: |
    Phase 5 may surface Layer-B cartridge template/schema work later as Map v2
    consumer surfaces mature, but this canon sync makes no lifecycle protocol change.
  strategy_status:
    DMB: "DRAFT/REVIEWED surfaces only; no promotion or implementation."
    TRM: "DRAFT surface only; no implementation."
    MEM: "No current draft in repo; waits for Olya source after HTF Map grounding."

repo_state:
  observed_branch: main
  last_verified_origin_main_before_anchor_semantics_patch: 470c44c0e70b1cc5da41195c3a397b2c4c41f8ba
  last_verified_origin_main_note: "origin/main after same-cycle Stage 2D canon anchor patch."
  canon_content_refresh_sha: 20f06735fe5f3e8372940cd82e547c9a4ed121d5
  canon_anchor_patch_sha: 470c44c0e70b1cc5da41195c3a397b2c4c41f8ba
  current_remote_rule: "Use git rev-parse origin/main; this orientation file does not self-anchor its own final patch SHA."
  olya_bundled_digest_ratified_sha: 7ad7833948f1656bcaa75b4a3dcb83c65e3c5b85
  design_scoping_ratified_sha: 3d09e8b7ef2d6436bc2b47d9f5541105b6a6e5d3
  wp1_contract_delta_preflight_ratified_sha: 6002d6f2576dde6e56521119dba381e2601f3701
  wp2_primitive_gap_brief_ratified_sha: c9ff53eaa617ba900a61162e9d97017dd674bac1
  wp2_gap_report_ratified_sha: ef185f8410f27460face0c3f9b45889bc786eadb
  worktree_status_rule: "Use git status live; this orientation file does not self-anchor current dirty/clean state."

live_plan:
  owner: docs/canonical/FORWARD_PLAN.md
  current_next_actions:
    - "Stage 2D two inert fixtures landed: first BALANCE fixture at 8d67740f7654b32a20c9ac22c5c4fd3c4932bad1 and trade_014 NOT_BALANCE/RETRACE fixture at 6d4e5d6c8fb7a4a35a1d460b3e9b476a6eb0a362."
    - "First fixture: tests/fixtures/map_v2/stage_2D/eurusd_daily_2024_08_15_2024_09_12_balance_snapshot.yaml (EURUSD_Daily_2024-08-15_to_2024-09-12 BALANCE)."
    - "Second fixture: tests/fixtures/map_v2/stage_2D/eurusd_daily_2026_02_04_trade_014_retrace_not_balance_snapshot.yaml (trade_014 EURUSD_Daily_2026-02-04 NOT_BALANCE/RETRACE)."
    - "Olya bundled methodology digest ratified at 7ad7833948f1656bcaa75b4a3dcb83c65e3c5b85."
    - "Map v2 producer design-scoping artifact ratified at 3d09e8b7ef2d6436bc2b47d9f5541105b6a6e5d3."
    - "WP1 contract-delta preflight for delivery_quality and level_state ratified at 6002d6f2576dde6e56521119dba381e2601f3701; it defines amendment shape only."
    - "WP2 Daily strong-close-through primitive-gap inspection brief ratified at c9ff53eaa617ba900a61162e9d97017dd674bac1."
    - "WP2 read-only primitive-gap report ratified at ef185f8410f27460face0c3f9b45889bc786eadb with final_recommendation=existing_surface_extension_needed, new_primitive_decision=not_made, and methodology_examples_needed_for_tie_break=true."
    - "Olya verbal NOT_BALANCE confirmation record landed at ea1011d1761a03fda2d60759f50f536ed68cfc72; trade_011 remains provisional and not canonicalized."
    - "Fixtures are inert metadata only; Map v2 producer/runtime/consumer remains not implemented and not certified."
    - "delivery_quality and level_state are preflight-scoped only; future schema/output changes require explicit G-ratified contract amendment parallel to the Stage 1A BALANCE path."
    - "execution_permission separation is design-scoped only; no implementation is authorized."
    - "Strong Daily close-through remains Daily-only; WP2 found existing_surface_extension_needed but no primitive decision, no implementation, no thresholds, and no LTF dependency. Future Olya examples are needed for the daily_momentum_candle/daily_decisive_candle tie-break."
    - "Next implementation/design gate is undecided; trade_013 is held for separate decision; third fixture remains unauthorized."
    - "No runtime consumption, schema/cartridge change, producer work, strategy migration, v2 certification, paper-trading claim, trade_011 resolution/canonicalization, daily_momentum/daily_decisive primitive implementation or extension, threshold invention, LTF confirmation logic, acceptance/strong-close-through proxy, followthrough activation gate, or Q4/Q5/Q6 predicate work is authorized."

audit_trail_rule: |
  Closed mission detail lives in ratification docs, archive docs, review docs,
  or finding ID pointers. No historical block should be deleted without a
  surviving pointer.
```

---

## 2. What en1gma Is

en1gma is a **CONSOLE + CARTRIDGE** system.

The **CONSOLE** is the universal ICT machinery: data ingestion, detection primitives, HTF spatial reasoning, LTF execution chain, governance, execution, and observability. It is strategy-blind.

**CARTRIDGES** are YAML-only strategy declarations that configure which console capabilities to activate. ARS and DAILY_EXPANSION are cartridges. Future strategies must enter through the cartridge contract unless they require explicit console/methodology work.

```yaml
one_sentence: |
  A constitutional trading system that reads market structure, holds persistent
  spatial context, and executes entries when structure and context align under
  sovereign human governance.

core_contract:
  console: "stable machinery"
  cartridge: "strategy declaration"
  boundary: docs/canonical/CARTRIDGE_CONTRACT.md
```

---

## 3. Architecture Spine

```yaml
layers:
  L1_DATA:
    path: en1gma/console/data/
    owns: "River, bar types, timeframe aggregation"
  L2_DETECTION:
    path: en1gma/console/detection/
    owns: "detect.py facade + vendored ra_engine primitives"
  L3_MAP:
    path: en1gma/console/map/
    owns: "regime, dealing range, PDA lifecycle, day_state, gate inputs"
  L4_CHAIN:
    path: en1gma/console/chain/
    owns: "sweep -> MSS -> FVG -> OTE evaluation and canon runtime"
  L5_GOVERNANCE_EXECUTION:
    paths:
      - en1gma/console/governance/
      - en1gma/console/execution/
    owns: "halt/lease/risk/check_governance and broker/position/intent"
  ORCHESTRATOR:
    path: en1gma/orchestrator/
    owns: "wiring only; never methodology decisions"

two_clocks:
  Map: "slow, structural, persistent, quiet; updates on structural events"
  Chain: "fast, per-bar within kill zones; fires only when Map-approved location is contacted"

two_paths:
  ARS:
    cartridge: en1gma/cartridges/ars_v1_3.yaml
    map_required: false
    path: "canon algorithm bypasses Map"
  DAILY_EXPANSION:
    cartridge: en1gma/cartridges/daily_expansion.yaml
    map_required: true
    path: "detect -> Map -> Gate -> Chain -> Intent -> Governance -> Broker"
```

---

## 4. Directory Map

```yaml
en1gma/:
  console/: "strategy-blind ICT machinery"
  cartridges/: "YAML strategy declarations + loader only"
  orchestrator/: "top-layer wiring"
  observe/: "cross-cutting trace/replay consumers"
  methodology/: "read-only vLOCK / canon references"
  scripts/: "entry points and operational tooling"
  tests/: "unit, contract, integration, parity, ops"
  ground_truth/: "Olya annotations and reference fixtures"

external_lineage:
  phoenix: "governance architecture proof bank"
  dexter: "detection/methodology proof bank"
  research_accelerator: "methodology oracle and calibration proving ground"
  phoenix_swarm: "coordination archive"
  source_repo_rule: "read-only reference; runtime development happens in en1gma"
```

For code-level line references, use the source code directly. `docs/archive/POST_PHASE_3_ORACLE.md` is now a snapshot reference, not live line-ref authority.

---

## 5. Strategy And Map Model

```yaml
cartridge_shape:
  declares: "which console capabilities to activate + configuration"
  never_contains: "executable code or cartridge-specific console branches"

gate_conditions_all_required_for_ARMED:
  1: "regime.direction != NEUTRAL"
  2: "active PDA in correct zone"
  3: "PDA direction_context matches regime.direction"
  4: "price contacts PDA zone this bar"
  5: "current time within kill zone"
  6: "map_state.construction_mode == OK"

map_v1_locked_semantics:
  note: "Current runtime only; do not rewrite as v0.14 behavior."
  semantics:
    - "wick-to-wick dealing range measurement"
    - "rolling dealing range with sweep priority within regime"
    - "daily -> H4 authority cascade when daily DR is still expanding"
    - "PDA midpoint vs DR equilibrium for zone classification"
    - "TOUCHED is permanent lifecycle state"
    - "no age expiry; structure invalidates structure"
    - "v1 scope: FVG only"

map_v2_design_input:
  status: PHASE_5_C2_DESIGN_SCOPING_RATIFIED_NO_PRODUCER
  methodology: docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md
  design_brief: docs/reviews/HTF_MAP_v0_14_DESIGN_BRIEF_DRAFT_2026_04_29.md
  stage_1_brief: docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md
  stage_1A_balance: docs/reviews/PHASE_5_STAGE_1A_BALANCE_MARKET_STATE_CONTRACT_AMENDMENT_BRIEF_DRAFT_2026_04_29.md
  stage_2C_balance_bridge: docs/reviews/PHASE_5_STAGE_2C_BALANCE_ENUM_AND_FIXTURE_EXTENSION_BRIEF_DRAFT_2026_04_29.md
  c2_preflight: docs/reviews/PHASE_5_C2_PRODUCER_PREFLIGHT_2026_04_30.md
  c2_verbatim_source: docs/reviews/PHASE_5_OLYA_METHOD_REPLY_VERBATIM.md
  c2_methodology_digest: docs/reviews/PHASE_5_C2_OLYA_METHODOLOGY_DIGEST_2026_04_30.md
  c2_brief_authorization: docs/reviews/PHASE_5_C2_FIRST_PRODUCER_SLICE_BRIEF_AUTHORIZATION_2026_04_30.md
  c2_execution_authorization: docs/reviews/PHASE_5_C2_FIRST_PRODUCER_SLICE_EXECUTION_AUTHORIZATION_2026_04_30.md
  c2_stage_2D_packet: docs/reviews/PHASE_5_C2_STAGE_2D_SINGLE_FIXTURE_DROID_PACKET_DRAFT_2026_05_01.md
  c2_not_balance_confirmation: docs/reviews/PHASE_5_C2_OLYA_VERBAL_NOT_BALANCE_CONFIRMATION_2026_05_01.md
  c2_trade_014_packet: docs/reviews/PHASE_5_C2_STAGE_2D_TRADE_014_NOT_BALANCE_FIXTURE_DROID_PACKET_DRAFT_2026_05_01.md
  c2_olya_bundled_digest: docs/reviews/PHASE_5_C2_OLYA_BUNDLED_TOUCHPOINT_DIGEST_2026_05_01.md @ 7ad7833
  c2_design_scoping: docs/reviews/PHASE_5_C2_MAP_V2_PRODUCER_DESIGN_SCOPING_2026_05_01.md @ 3d09e8b
  c2_wp1_contract_delta_preflight: docs/reviews/PHASE_5_C2_WP1_DELIVERY_QUALITY_LEVEL_STATE_CONTRACT_DELTA_PREFLIGHT_2026_05_01.md @ 6002d6f
  c2_wp2_primitive_gap_brief: docs/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_INSPECTION_BRIEF_2026_05_01.md @ c9ff53e
  c2_wp2_gap_report: docs/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md @ ef185f8
  stage_2D_first_fixture: tests/fixtures/map_v2/stage_2D/eurusd_daily_2024_08_15_2024_09_12_balance_snapshot.yaml
  stage_2D_second_fixture: tests/fixtures/map_v2/stage_2D/eurusd_daily_2026_02_04_trade_014_retrace_not_balance_snapshot.yaml
  phase_decision: docs/reviews/PHASE_4_CLOSE_PHASE_5_OPEN_DECISION_BRIEF_2026_04_29.md
  c4_anchor: docs/canonical/PHASE_5_KICKOFF_CLOSE_2026_04_29.md
  note: "Stage 2D has two inert example snapshots plus ratified C2 design scoping, WP1 contract-delta preflight, WP2 primitive-gap brief, and WP2 read-only gap report. WP2 disposition is existing_surface_extension_needed with new_primitive_decision=not_made and methodology_examples_needed_for_tie_break=true; producer/runtime/consumer/schema/cartridge/certification remain absent."

doctrine_sources:
  spatial_v1_runtime: docs/canonical/MAP_SPATIAL_PRIMER_v1.md
  map_v2_methodology_input: docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md
  map_v2_design_brief: docs/reviews/HTF_MAP_v0_14_DESIGN_BRIEF_DRAFT_2026_04_29.md
  boundary: docs/canonical/CARTRIDGE_CONTRACT.md
  lifecycle: docs/canonical/CARTRIDGE_LIFECYCLE_PROTOCOL.md
  calibration: calibration_results.yaml
```

---

## 6. Invariant Index

CLAUDE.md indexes invariants. Full invariant text belongs in the ratified owner documents.

```yaml
core_safety_and_runtime:
  owner: CLAUDE.md + code/tests
  invariants:
    INV-SOVEREIGN-1: "Human sovereignty over capital is absolute"
    INV-SOVEREIGN-2: "Live execution requires human T2 approval"
    INV-HALT-OVERRIDES-ALL: "Halt wins over any system state"
    INV-DETECTION-AUTHORITY-SINGLETON: "detect.py is the sole detection oracle"
    INV-OLYA-ABSOLUTE: "Olya's NO on detection/methodology is final"
    INV-REPLAY-DETERMINISM: "Same stored inputs -> same outputs"
    INV-NO-UNGOVERNED-TRADES: "Every trade passes through governance"
    INV-LIVE-REQUIRES-T2: "Paper -> live requires human T2 token"
    INV-GOVERNANCE-SINGLE-CHECK-SITE: "check_governance() is the authorization site"

cartridge_boundary:
  owner: docs/canonical/CARTRIDGE_CONTRACT.md
  invariants:
    - INV-CARTRIDGE-PURE-DECLARATION
    - INV-CONSOLE-STRATEGY-BLIND
    - INV-CONSOLE-NO-CARTRIDGE-SHAPED-BRANCHES
    - INV-NEW-CARTRIDGE-NO-CONSOLE-CHANGE
    - INV-CARTRIDGE-SCHEMA-UNIFIED
    - INV-CANON-RUNTIME-FIXED
    - INV-TRACE-DETERMINISM-BY-CARTRIDGE
    - INV-STRUCTURAL-REFACTOR-NO-SEMANTIC-DRIFT
    - INV-BOUNDARY-CLASSIFIABLE
    - INV-AUTHORITY-BOUNDARY-EXPLICIT
    - INV-RULING-SCOPE-EXPLICIT

map_and_chain_methodology:
  owners:
    - docs/canonical/CARTRIDGE_CONTRACT.md
    - docs/reviews/*_RATIFICATION_*.md
  invariants:
    - INV-PDA-CREATED-AT-CONFIRMATION
    - INV-DAY-STATE-MARKET-DRIVEN
    - INV-PDA-DIRECTION-FIDELITY
    - INV-PDA-ZONE-FROM-DETECTOR
    - INV-PDA-MITIGATION-IS-RETRACE-FILL
    - INV-DAY-STATE-MAP-COHERENT
    - INV-PDA-MITIGATION-SINGLE-SITE
    - INV-HTF-INCLUDES-CASCADE-PAIR
    - INV-CHAIN-SEQUENCE-FIXED
    - INV-MAP-BEHAVIOR-FROM-METHODOLOGY-NOT-CONFIG
    - INV-FVG-CAUSAL-IDENTITY-SURFACE
    - INV-CHAIN-FVG-CAUSAL-SELECTION

epistemic_integrity_family:
  owner: docs/archive/PHASE_4_RATIFICATION.md
  current_evidence: docs/canonical/CERTIFICATION_STATE.md
  invariants:
    INV-EPISTEMIC-INTEGRITY: "Authority surfaces must not lie"
    child_INV-SYSTEM-NO-STATE-INVENTION: "No plausible state substitution"
    child_INV-MAP-CONSTRUCTION-MODE-EXPLICIT: "Every MapState declares construction mode"
    child_INV-GATE-REFUSES-FALLBACK-MAP: "Gate refuses non-OK MapState"
    child_INV-UNKNOWN-STATE-HALTS: "Cannot-determine is distinct from no-setup"
    child_INV-NO-EVIDENCE-NO-TRADE: "Absence of setup is valid NO_TRADE"
    child_INV-REGIME-FROM-METHODOLOGY-NOT-FALLBACK: "Regime is detector/methodology sourced"
    peer_INV-FIDELITY-ANCHORED-TO-CHART-TRUTH: "Chart truth beats old reference artifacts"
    peer_INV-STRATEGY-CONFIG-SINGLE-SOURCE: "CLI strategy YAML is the single config source"
    peer_INV-CARTRIDGE-ABSENCE-IMPLIES-NO-TRADE: "Missing eligibility fields are ineligible"
```

---

## 7. Open / Current Work Index

Closed mission detail belongs in ratification/review docs. This index is only for live orientation.

```yaml
certification_hygiene:
  POST_4B_H1_DIAG_UNKNOWN_CHAIN_REASON:
    status: CLOSED_AND_RATIFIED
    evidence: "raw_unknown=0; true KZ near-misses=1003; bookkeeping_artifacts=114; FALLBACK direction partitioned"
    ratification: docs/reviews/POST_4B_H1_DIAG_UNKNOWN_CHAIN_REASON_RATIFICATION_2026_04_28.md
    owner: docs/canonical/CERTIFICATION_STATE.md

phase_4_to_phase_5_governance:
  status: G_RATIFIED_APPROVED_WITH_BOUNDARIES
  decision_brief: docs/reviews/PHASE_4_CLOSE_PHASE_5_OPEN_DECISION_BRIEF_2026_04_29.md
  candidate_thesis: HTF_MAP_V2
  methodology_input: docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md
  design_brief: docs/reviews/HTF_MAP_v0_14_DESIGN_BRIEF_DRAFT_2026_04_29.md
  stage_1_brief: docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md
  c4_anchor: docs/canonical/PHASE_5_KICKOFF_CLOSE_2026_04_29.md
  current_next: "Stage 2D two inert fixtures, C2 design scoping, WP1 preflight, WP2 brief, and WP2 gap report are ratified; next natural decision is Olya example routing for Daily strong close-through or WP1 contract-amendment scoping, not implementation. trade_013 is held for separate decision, third fixture remains unauthorized, and trade_011 remains provisional/not canonicalized."
  hard_guardrail: "No MapV2Engine producer, runtime migration, runtime consumption, consumer path, schema/cartridge change, strategy migration, v2 certification, paper-trading claim, trade_011 resolution/canonicalization, third fixture, daily_momentum/daily_decisive primitive implementation or extension, threshold invention, LTF confirmation logic, acceptance/strong-close-through proxy, followthrough activation gate, existing-surface-sufficient claim, new-primitive-required claim, or Q4/Q5/Q6 predicate work without separate G authorization."

map_v2_design_lane:
  status: STAGE_2D_TWO_INERT_FIXTURES_AND_C2_WP2_GAP_REPORT_RATIFIED_NO_PRODUCER
  stage_1_candidate: Map_v2_output_contract_freeze
  stage_1_brief: docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md
  stage_2A: "Inert read-model/trace/snapshot shell pushed @ 335a8f15."
  stage_2B: "Construction replay harness pushed @ 95e321b."
  stage_1A_balance: "BALANCE market_state contract amendment pushed @ 59985ce."
  stage_2C_balance: "BALANCE enum/type/test + fixture extension pushed @ 67f6647."
  c2_day_2026_04_30:
    preflight: "docs/reviews/PHASE_5_C2_PRODUCER_PREFLIGHT_2026_04_30.md @ d56f141"
    routing_prep: "docs/reviews/PHASE_5_C2_OLYA_ROUTING_PREPARATION_2026_04_30.md @ a59ee2e"
    packet_draft: "docs/reviews/PHASE_5_C2_OLYA_FACING_METHOD_PACKET_DRAFT_2026_04_30.md @ 9789e4a"
    verbatim_source: "docs/reviews/PHASE_5_OLYA_METHOD_REPLY_VERBATIM.md @ 4785101"
    methodology_digest: "docs/reviews/PHASE_5_C2_OLYA_METHODOLOGY_DIGEST_2026_04_30.md @ 1c2c525"
    brief_authorization: "docs/reviews/PHASE_5_C2_FIRST_PRODUCER_SLICE_BRIEF_AUTHORIZATION_2026_04_30.md @ 05da749"
    brief_draft: "docs/reviews/PHASE_5_C2_FIRST_PRODUCER_SLICE_BRIEF_DRAFT_2026_04_30.md @ 7b23206"
    execution_authorization: "docs/reviews/PHASE_5_C2_FIRST_PRODUCER_SLICE_EXECUTION_AUTHORIZATION_2026_04_30.md @ b28f668"
  c2_day_2026_05_01:
    stage_2D_packet: "docs/reviews/PHASE_5_C2_STAGE_2D_SINGLE_FIXTURE_DROID_PACKET_DRAFT_2026_05_01.md @ b019e25"
    stage_2D_first_fixture: "tests/fixtures/map_v2/stage_2D/eurusd_daily_2024_08_15_2024_09_12_balance_snapshot.yaml @ 8d67740"
    not_balance_confirmation: "docs/reviews/PHASE_5_C2_OLYA_VERBAL_NOT_BALANCE_CONFIRMATION_2026_05_01.md @ ea1011d"
    trade_014_packet: "docs/reviews/PHASE_5_C2_STAGE_2D_TRADE_014_NOT_BALANCE_FIXTURE_DROID_PACKET_DRAFT_2026_05_01.md @ 2a432e3"
    stage_2D_second_fixture: "tests/fixtures/map_v2/stage_2D/eurusd_daily_2026_02_04_trade_014_retrace_not_balance_snapshot.yaml @ 6d4e5d6"
    olya_bundled_digest: "docs/reviews/PHASE_5_C2_OLYA_BUNDLED_TOUCHPOINT_DIGEST_2026_05_01.md @ 7ad7833"
    design_scoping: "docs/reviews/PHASE_5_C2_MAP_V2_PRODUCER_DESIGN_SCOPING_2026_05_01.md @ 3d09e8b"
    wp1_contract_delta_preflight: "docs/reviews/PHASE_5_C2_WP1_DELIVERY_QUALITY_LEVEL_STATE_CONTRACT_DELTA_PREFLIGHT_2026_05_01.md @ 6002d6f"
    wp2_primitive_gap_brief: "docs/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_INSPECTION_BRIEF_2026_05_01.md @ c9ff53e"
    wp2_gap_report: "docs/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md @ ef185f8"
  certification_note: "Future V2 certification requires new replay, chart-truth, and walk-forward evidence; current Stage 2D fixtures, C2 design scoping, WP1 preflight, WP2 brief, and WP2 gap report are not certification evidence."
  not_authorized_without_separate_G_decision:
    - MapV2Engine_producer
    - C2_producer_work
    - runtime_migration
    - schema_changes
    - cartridge_changes
    - DMB_MEM_TRM_implementation
    - H4_authority_resurrection
    - automatic_target_ranking
    - third_fixture_without_G_authorization
    - trade_011_canonicalization
    - daily_momentum_or_daily_decisive_primitive_implementation_or_extension
    - threshold_invention
    - lower_timeframe_confirmation_logic
    - Q4_Q5_Q6_operationalization

strategy_family_status:
  DMB: "Draft/reviewed only; no promotion, no implementation."
  TRM: "Draft only; separate session/canon lane if prioritized later."
  MEM: "Awaiting Olya draft after HTF Map grounding."

methodology_seed_track:
  MSS_NOT_EQUAL_ACTIVE_CONTROL:
    status: VISIBLE_IN_V1_RUNTIME_SCOPE
    fixture: trade_011
    owner: docs/methodology_seeds/MSS_NOT_EQUAL_ACTIVE_CONTROL.md
    phase_5_note: |
      Map v2 design scoping preserves direction/actionability separation as
      design-only input. trade_011 remains provisional and not canonicalized;
      any chart-truth resolution remains pending Olya laptop review and any
      later Map v2 implementation/replay/G review. v1 runtime is unchanged.
    parked_strategy_pointer: docs/canonical/VAULT.md

phase_4c_4d_deferred:
  SW52_semantic_detection_parity:
    status: DEFERRED
    reason: "requires CTO-authored adapter/event-identity/tolerance design"
  SW44_test_mypy_tier_1:
    status: PARKED
    reason: "test typing architecture, not current safety blocker"
  SW44_utility_scripts_tier_3:
    status: OPEN_IF_PRIORITIZED
  SW38_SW43_schema_v2_cluster:
    status: FUTURE_DESIGN_SESSION
    note: "May be revisited after Phase 5 governance and Map v2 output contract freeze."
```

---

## 8. Roles

```yaml
G:
  role: "Sovereign Operator"
  authority: "vision, veto, capital decisions, graduation ceremonies, phase ratification"

Olya:
  role: "Chief Strategy Officer"
  authority: "methodology truth, strategy calibration, detection validation"
  rule: "INV-OLYA-ABSOLUTE"

CTO:
  role: "strategic synthesis, architectural decisions, mission brief authorship"
  mode: "dense signal; owns spec quality"

Opus / Cursor / factory.ai Mission:
  role: "implementation and doc/code execution against briefs"
  rule: "halt on ambiguity; preserve parity and audit trail"

COO:
  role: "operational diagnostics, runtime ops, Olya calibration support"

Sentinel:
  role: "always-on system monitor"

Advisors:
  GPT: "architect lint"
  OWL: "structural audit"
  BOAR: "chaos audit"
  Fresh_Chair_Opus: "challenger"
```

---

## 9. Operating Norms

```yaml
communication:
  format: DENSE_M2M
  prefer: "YAML / structured output, binary verdicts, explicit refs"
  avoid: "recap loops, hedging, stale narrative"

development:
  classification_first: "Every brief/ruling/change declares scope + effect per CARTRIDGE_CONTRACT.md §7"
  parity_discipline: "Production-code commits require relevant parity/smoke gates"
  no_new_capability_without_ratification: "No Map v2 implementation or strategy build before contract freeze plus separate G-ratified implementation mission"
  canon_first: "Check canon before drafting Olya questions"
  no_orphan_deletion: "Removed history must leave a ratification/archive/finding pointer"
  no_mega_doc: "Do not replace bloat with a new undefined owner document"

testing_pointers:
  static:
    - "lint-imports --config pyproject.toml"
    - "mypy en1gma/"
  parity:
    - "ARS parity: 151/151"
    - "DAILY_EXPANSION chart-truth: see CERTIFICATION_STATE.md"
```

---

## 10. Document Map

```yaml
orientation:
  CLAUDE.md: "what the system is and where to read next"
  docs/canonical/NORTH_STAR.md: "strategic why"
  docs/canonical/CARTRIDGE_CONTRACT.md: "console/cartridge interface"
  docs/canonical/MAP_SPATIAL_PRIMER_v1.md: "spatial doctrine"

live_control:
  docs/canonical/PHASE_5_KICKOFF_CLOSE_2026_04_29.md: "Phase 5 prior-session state anchor; superseded for live state by 2026-05-01 C2 artifacts"
  docs/canonical/FORWARD_PLAN.md: "what happens next"
  docs/canonical/CERTIFICATION_STATE.md: "what has and has not been proven"
  docs/reviews/PHASE_4_CLOSE_PHASE_5_OPEN_DECISION_BRIEF_2026_04_29.md: "G-ratified decision closing Phase 4 / opening Phase 5"
  docs/reviews/HTF_MAP_v2_OUTPUT_CONTRACT_FREEZE_BRIEF_DRAFT_2026_04_29.md: "Frozen Stage 1 Map v2 output contract surface"
  docs/reviews/PHASE_5_STAGE_1A_BALANCE_MARKET_STATE_CONTRACT_AMENDMENT_BRIEF_DRAFT_2026_04_29.md: "BALANCE market_state contract amendment; no detection algorithm"
  docs/reviews/PHASE_5_STAGE_2C_BALANCE_ENUM_AND_FIXTURE_EXTENSION_BRIEF_DRAFT_2026_04_29.md: "BALANCE inert enum/type/test + fixture bridge; no producer"
  docs/reviews/HTF_MAP_v0_14_DESIGN_BRIEF_DRAFT_2026_04_29.md: "Map v2 no-code design input; no producer/runtime implementation"
  docs/reviews/PHASE_5_OLYA_METHOD_REPLY_VERBATIM.md: "Olya C2 methodology source truth; formatting-cleaned verbatim archive"
  docs/reviews/PHASE_5_C2_OLYA_METHODOLOGY_DIGEST_2026_04_30.md: "Digest for first-slice scoping; do not duplicate methodology content here"
  docs/reviews/PHASE_5_C2_FIRST_PRODUCER_SLICE_BRIEF_AUTHORIZATION_2026_04_30.md: "Boundary for future first producer-slice brief draft; no code/no producer"
  docs/reviews/PHASE_5_C2_FIRST_PRODUCER_SLICE_BRIEF_DRAFT_2026_04_30.md: "First producer-slice brief draft; review-held, no producer"
  docs/reviews/PHASE_5_C2_FIRST_PRODUCER_SLICE_EXECUTION_AUTHORIZATION_2026_04_30.md: "Execution boundary for one inert Stage 2D fixture; no producer/runtime"
  docs/reviews/PHASE_5_C2_STAGE_2D_SINGLE_FIXTURE_DROID_PACKET_DRAFT_2026_05_01.md: "Droid packet for first inert Stage 2D fixture"
  docs/reviews/PHASE_5_C2_OLYA_VERBAL_NOT_BALANCE_CONFIRMATION_2026_05_01.md: "G-attested Olya verbal confirmation that trade_013 and trade_014 are NOT BALANCE; trade_011 deferred"
  docs/reviews/PHASE_5_C2_STAGE_2D_TRADE_014_NOT_BALANCE_FIXTURE_DROID_PACKET_DRAFT_2026_05_01.md: "Droid packet for one inert trade_014 NOT_BALANCE/RETRACE fixture"
  docs/reviews/PHASE_5_C2_OLYA_BUNDLED_TOUCHPOINT_DIGEST_2026_05_01.md: "Ratified Olya bundled methodology digest; source for design scoping; no implementation authorization"
  docs/reviews/PHASE_5_C2_MAP_V2_PRODUCER_DESIGN_SCOPING_2026_05_01.md: "Ratified Map v2 producer design-scoping artifact; design-only; future contract amendment required for delivery_quality/level_state"
  docs/reviews/PHASE_5_C2_WP1_DELIVERY_QUALITY_LEVEL_STATE_CONTRACT_DELTA_PREFLIGHT_2026_05_01.md: "Ratified WP1 contract-delta preflight; amendment shape only; no schema/output change"
  docs/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_INSPECTION_BRIEF_2026_05_01.md: "Ratified WP2 read-only primitive-gap inspection brief; no implementation"
  docs/reviews/PHASE_5_C2_WP2_DAILY_STRONG_CLOSE_THROUGH_PRIMITIVE_GAP_REPORT_2026_05_01.md: "Ratified WP2 read-only gap report; existing_surface_extension_needed; primitive decision not made; Olya examples needed"
  tests/fixtures/map_v2/stage_2D/eurusd_daily_2024_08_15_2024_09_12_balance_snapshot.yaml: "First inert Olya-asserted BALANCE example snapshot"
  tests/fixtures/map_v2/stage_2D/eurusd_daily_2026_02_04_trade_014_retrace_not_balance_snapshot.yaml: "Second inert Stage 2D fixture: trade_014 NOT_BALANCE/RETRACE adjacent-state example"

closure_and_history:
  docs/reviews/PHASE_4B_LANE_CLOSE_RATIFICATION_2026_04_27.md: "why Phase 4b lane closed at 11/12"
  docs/archive/PHASE_4_RATIFICATION.md: "historical Phase 4 decision and invariant origin"
  docs/archive/POST_PHASE_3_ORACLE.md: "snapshot reference; not live line-ref authority"
  docs/archive/: "superseded versions and historical records"

future_and_parked:
  docs/canonical/VAULT.md: "parked ideas, deferred capabilities, source lineage"
  docs/canonical/CARTRIDGE_LIFECYCLE_PROTOCOL.md: "v0.2 lifecycle remains in force; Layer-B template work may surface later"
  docs/methodology_seeds/MSS_NOT_EQUAL_ACTIVE_CONTROL.md: "trade_011 seed; not implementation spec"
```

---

*CLAUDE.md v0.28 - slim orientation surface. For evidence state read CERTIFICATION_STATE. For action state read FORWARD_PLAN. For C2 methodology/design scope read the ratified bundled digest, design scoping, WP1 preflight, WP2 brief, WP2 gap report, and G-approved Olya strong-close-through routing packet; all remain docs-only/inert with no producer/runtime/certification.*
