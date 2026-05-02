# COO Inputs — Post-Phase-3

```yaml
document: COO_INPUTS_POST_PHASE_3
version: 1.0
date: 2026-04-26
authored_by: Opus (COO / Chief Engineer, Phase 3)
ratified_by: G (pending)
purpose: |
  Single canonical input artifact for incoming CTO dispatching
  Post-Phase-3 / Phase 4+ work. Synthesises the external advisor
  review (docs/reviews/ADVISOR_REVIEW_2026_04_26.md, b3f5e11) with
  current-codebase verdict + COO additions, ranked by priority.
  Supersedes the advisor review as the Post-Phase-3 scope input —
  incoming CTO should read THIS first; advisor review remains as
  reference.
rule: |
  DENSE. Each item = source + current-code verdict + fix shape +
  priority + owner. No prose bloat. Cross-references CLAUDE.md §15
  + FORWARD_PLAN v2.3 §P3_POST_PHASE_3_SCOPE for comprehensive
  finding detail.
```

---

## 1. Executive Verdict

Advisor diagnosis ACCURATE. Phase 3 closed the assurance gap (mypy
strict CI activated; 8 findings closed) and the cartridge-contract
gap (D4 WIRE_3 + REMOVE landed). The two **Critical** items from the
advisor review are STILL LIVE in current code — verified against
phase_3_5-exit HEAD. Phase 4+ posture: "swiss-watch certification"
via authority-surface hardening + fail-closed discipline, NOT
architectural rewrite.

---

## 2. Ratified Reality Check

```yaml
advisor_diagnosis_accuracy:
  architecture_read: correct
  failure_class_framing: correct (semantic drift at authority surfaces)
  priority_ordering: correct (Critical 1 + 2 are the time-sensitive items)

phase_3_closures_aligned_with_advisor:
  static_assurance_not_credible (Medium 9): RESOLVED — phase_3_5 c3
    activated mypy strict CI; 0 errors / 176 files on enforced
    surface
  day_state_strategy_name_branching (part of High 6): RESOLVED —
    phase_3_4 c4 (SW29 CLOSED) moved to declarative signature
  max_trades_per_window unused (part of High 3): RESOLVED — phase_3_4
    c2 removed with strict-mode rejection
  map_required unused (part of High 3): RESOLVED — phase_3_4 c3
    option (a)-lite entry-script assertion (SW34 CLOSED)
  day_state_requirement unused (part of High 3): RESOLVED —
    phase_3_4 c4 with CARTRIDGE_CONTRACT §3 schema migration
  htf_timeframes unused (part of High 3): RESOLVED — phase_3_4 c1
    wired at loader boundary (INV-HTF-INCLUDES-CASCADE-PAIR)

phase_3_registered_aligned_with_advisor:
  mss_silent_upgrade (part of Medium 7): SW32 already registered
    (Phase 2.5 Closeout); §11 silent_upgrade_discipline doctrine
    entry landed
  terminal_pda_persistence (part of Medium 8): SW06 already
    registered (Block 2)
  map_timeline_non_determinism (part of Medium 8): SW25 already
    registered (Block 3 LOW)
  dispatch_path_asymmetry (part of Lean/Bloat 4): SW39 already
    registered (Phase-4-pending); clusters with SW40/41/42/43
```

---

## 3. Post-Phase-3 Priority Items

### 3.1 IMMEDIATE (correctness; unblocked; land before structural work)

```yaml
P1_gate_mixed_direction_arming:
  source: advisor Critical 1
  sw_candidate: SW47
  current_code_evidence: |
    en1gma/console/chain/gate.py:114-118
    candidates filter:
      p.status in PDA_ACTIVE_STATES
      AND (required is None OR p.location_class == required)
    Does NOT filter on p.direction_context vs regime.direction.
    Post-SW04, PDAs carry detector-faithful direction_context
    (bullish FVG → BULLISH, bearish FVG → BEARISH). Under a BULLISH
    regime with LONG_ONLY permission (required=DISCOUNT), a BEARISH
    PDA in the discount zone passes the filter and can arm the gate.
  correctness_impact_today: |
    No known failure on 6/6 DAILY_EXPANSION ground truth (mixed-
    direction-in-correct-zone is rare in test fixtures). Production
    hazard: real markets can produce bearish PDAs in discount during
    retests before regime flip; gate would arm on wrong truth.
  fix_shape: |
    Add direction clause to gate.py candidates filter:
      AND (regime.direction == MarketDirection.NEUTRAL
           OR p.direction_context == regime.direction)
    + parity test seeding mixed-direction PDA in required zone +
      asserting gate rejects wrong-direction PDA.
  size: ~10 LOC + 1 test case
  risk: LOW (adds constraint; narrows arming; cannot false-arm more)
  parity_impact: 151/151 + 6/6 expected preserved (fixtures do not
                 exercise the hazard today)
  priority: IMMEDIATE
  owner: Opus (Phase 4 c1 candidate)

P2_fail_closed_strategy_loader:
  source: advisor Critical 2
  sw_candidate: SW48
  current_code_evidence: |
    en1gma/orchestrator/map_orchestrator.py:137-141
    sp = strategy_params
    if sp is None:
        try:
            sp = load_strategy_by_name(strategy)
        except Exception:
            sp = None
    Silent exception swallow → sp=None → ChainConfig() defaults +
    default kz_windows + default ltf_tfs + day_state_required=None
    + all D4-wired fields silently inactive.
  configuration_split_brain: |
    scripts/run_map_session.py:76-97 loads governance via
    --strategy-yaml path; run_map_replay() separately calls
    load_strategy_by_name(strategy) using STRATEGIES_DIR / f"{
    strategy.lower()}.yaml". Two YAML sources for one run.
  phase_3_4_partial_mitigation: |
    load_map_required entry-script assertion (SW34 closure) catches
    cartridge-route mismatch on map_required flag. Does NOT catch
    downstream load_strategy_by_name failures (schema error / missing
    cartridge / malformed chain steps / etc.).
  fix_shape: |
    (a) remove try/except at map_orchestrator.py:137-141; let
        load_strategy_by_name raise.
    (b) replace load_strategy_by_name(strategy) with explicit
        strategy_yaml path threaded from CLI arg (consume what was
        already validated at entry).
    (c) register INV-STRATEGY-LOAD-MUST-SUCCEED — reaching the
        bar-processing loop with sp=None is a contract violation.
  size: ~20 LOC + 2 tests (load failure halts; split-brain closed)
  risk: LOW-MEDIUM (removes silent-fallback path; TEST-mode callers
        with sp=None explicitly may need separate handling)
  parity_impact: 151/151 + 6/6 preserved IF TEST-mode sp=None path
                 is preserved via explicit TEST-mode branch
  priority: IMMEDIATE
  owner: Opus + COO coordinate (entry scripts + orchestrator touched)
  couples_with: SW44 tier-3 utility-script sprint (same entry-script
                surface)
```

### 3.2 HIGH (structural / methodology-adjacent)

```yaml
P3_map_init_fail_closed_pass:
  source: advisor High 4
  sw_candidate: SW49 (methodology-ruling dependent)
  current_code_evidence: |
    en1gma/console/map/map_engine.py:287-293 fallback_full_range on
      no displacement events
    en1gma/console/map/map_engine.py:384-387 pullback_bars fallback:
      tail(5) → head(len/2)
    en1gma/console/map/map_engine.py:302-317 `except Exception: pass`
      on timestamp compare inside regime-disp loop
    _initialize_pdas_from_detections loops across tfs loading FVGs
      without regime-establishment-time or current-DR boundary
      filtering (against docstring intent at :186-193)
  disposition_shape: |
    Olya session: partition existing fallbacks into
      (a) methodology-acceptable (cold-start / bootstrap cases) —
          keep with invariant declaration
      (b) fail-closed — halt with explicit error
    Per-fallback ruling needed; not a single sweep.
  priority: HIGH
  gate: Olya availability
  owner: Olya methodology ruling + Opus implementation

P4_H4_cascade_replay_fidelity:
  source: advisor High 5
  sw_candidate: SW50
  current_code_evidence: |
    en1gma/console/map/map_engine.py:236-244 cascade correctly sets
      authority_tf = "H4" when daily DR invalid
    en1gma/console/map/map_engine.py:248 _replay_price_forward(
      daily_bars) — lifecycle replay always uses daily regardless
      of active authority TF
  correctness_impact: |
    H4 PDA lifecycle (OPEN → TOUCHED → MITIGATED) resolved against
    daily bars misses intraday H4 state changes. Daily bar contains
    the H4 extremes but not the sequence — if an H4 PDA would touch
    + mitigate within one daily bar, lifecycle replay under-resolves.
  fix_shape: |
    _replay_price_forward receives bars at authority_tf granularity.
    Signature:
      _replay_price_forward(self, bars: pd.DataFrame, tf: str)
    Caller (initialize) passes h4_bars when authority_tf == "H4".
    + H4 PDA lifecycle test (seed H4 PDA; walk H4 bars; assert state
      transitions at H4 granularity).
  size: ~15 LOC + 1 test
  risk: LOW-MEDIUM (touches lifecycle-replay surface; well-tested
        via existing PDA lifecycle tests)
  priority: HIGH
  owner: Opus (Phase 4 mid-stream)

P5_day_state_causal_linkage:
  source: advisor High 6 (second half — first half closed by SW29)
  sw_candidate: SW51 (methodology-ruling dependent)
  current_code_evidence: |
    en1gma/console/map/day_state.py::_check_expansion_delivered
    calls _find_aligned_event("displacement", ...) AND
    _find_aligned_event("mss", ...) independently. No check that
    the matched displacement and MSS are from the same structural
    event (causally linked in time, TF, direction).
  disposition_shape: |
    Olya ruling: does day_state transition require displacement AND
    MSS to be the same structural event, or is any-matched-pair
    sufficient?
    If causally-linked required: add linkage check
      (same TF + displacement.time < mss.time + matching direction +
       MSS falls within N bars of displacement).
    If any-pair sufficient: document current semantic explicitly.
  priority: HIGH (methodology-ruling)
  gate: Olya availability
  owner: Olya ruling + Opus implementation

P6_semantic_detection_parity:
  source: advisor Medium 7 (count-parity gap half; MSS silent-upgrade
          half already registered as SW32)
  sw_candidate: SW52
  current_code_evidence: |
    en1gma/tests/console/detection/test_detection_parity.py compares
    bucket counts (len(detections)) not IDs/properties/timestamps.
    A detection set with identical COUNT but different CONTENT passes.
  fix_shape: |
    Extend parity test to compare:
      - detection IDs (set equality)
      - properties dict (deep equality on key fields:
        quality_grade / qualification_path / displacement_type /
        atr_value / range_pips / time_end)
      - time field (byte-identical tz-aware datetime)
  size: ~50 LOC test extension (no runtime surface)
  risk: LOW (pure test assertion tightening)
  priority: MEDIUM-HIGH
  owner: Opus (standalone sprint)
```

### 3.3 MEDIUM (existing backlog aligned with advisor findings)

```yaml
P7_SW06_terminal_pda_persistence:
  source: advisor Medium 8 (sub-finding) + Block 2 existing
  already_registered: SW06
  scope: CLAUDE.md §15 existing entry; Block 2
  priority: MEDIUM

P8_SW25_map_timeline_non_determinism:
  source: advisor Medium 8 (sub-finding) + Block 3 existing
  already_registered: SW25
  scope: CLAUDE.md §15 existing entry; Block 3 LOW
  priority: LOW (unchanged)

P9_SW11_chain_config_unloaded_fields:
  source: advisor Lean/Bloat 2
  already_registered: SW11 (7/12 ChainConfig fields use hardcoded
                     defaults)
  scope: Block 2
  advisor_framing_match: "ChainConfig knobs that exist but are not
                          cartridge-driven"
  priority: MEDIUM
```

### 3.4 PHASE-4-PENDING CLUSTER (already scoped)

```yaml
cartridge_schema_v2_cluster:
  findings: [SW38, SW39, SW40, SW41, SW42, SW43]
  status: registered 2026-04-22 (Phase-4-pending)
  treat_as_bundle: yes — five findings, one resolution surface
  resolution_path: |
    cartridge schema v2 ratification (Olya + CTO + G) +
    canon_runner / canon_runner_params fields on map-required
    cartridges + orchestrator dispatch migration to CANON_RUNNERS
    lookup + SW42 BrokerProtocol / IntentBuilderProtocol (SW33
    HaltChecker precedent at runner level) + SW43 AuthorityTF
    redesign
  priority: HIGH (biggest structural Phase 4+ item)
  owner: Olya + CTO + G design session, Opus implementation

SW44_tiered_mypy_sprint:
  tier_1_tests: ~976 errors; mechanical batch; sprint first
  tier_3_utility_scripts:
    general: ~105 errors mechanical
    flagged_latent_defect_AUDIT_FIRST: henry_analyst.py:253
      (mlx_lm.load return-arity mismatch)
    pairs_naturally_with: P2_fail_closed_strategy_loader (both
      touch entry-script surface)
  tier_2_ra_engine_vendored: ~200 errors; LAST; gated on upstream
    parity contract
  priority: MEDIUM (each tier independently schedulable)
  owner: Opus (scripted batch work)
```

---

## 4. COO-Originated Items (beyond advisor review)

Items I'd add based on Phase 3 execution experience that the advisor
review didn't surface (snapshot timing or scope).

```yaml
C1_cartridge_schema_v2_is_primary_phase_4_work:
  observation: |
    Advisor review's Lean/Bloat item 4 ("Registry and protocol
    surfaces cleaner than runtime dispatch reality") understates the
    centrality. The SW38-SW43 cluster is five windows into ONE
    seam: dispatch convergence + AuthorityTF redesign + Protocol
    formalisation. This is the single largest Phase 4+ structural
    item by LOC-to-be-touched.
  implication: |
    Phase 4+ should not be mistaken for "a bunch of small items."
    If schema v2 lands cleanly, SW39/40/41/42/43 all close.
    Sprint ordering: complete P1/P2 (correctness) + P6 (semantic
    parity) + SW44 tier-1 first; schema v2 is the third major
    arc.

C2_INV_DAEMON_REAL_TIME_SCOPE_applies_beyond_ARS:
  observation: |
    INV-DAEMON-REAL-TIME-SCOPE registered 2026-04-22 via SW38 is
    framed around ARS daemon↔batch asymmetry. Every future cartridge
    will face the same question. Retrospective §8.2 notes this; worth
    elevating into CARTRIDGE_CONTRACT §6 as the generic framing so
    schema v2 can cite it by number not by SW38 context.
  implication: |
    Post-Phase-3 hygiene pass on CARTRIDGE_CONTRACT — lift the
    daemon-specific language into a generic "each cartridge's canon
    runner declares its observation-scope semantic" invariant.

C3_olya_queue_bottleneck:
  observation: |
    Olya methodology rulings gate P3 (map init fallbacks), P5
    (day_state causal linkage), and residual items from the Phase
    2.5 audit (SW27 FVG initial guard, SW31 displacement quality
    threshold). Without a session, P3/P5 cannot start.
  implication: |
    Olya session should batch-process these four methodology
    rulings in one F2F. Prep pack would include:
      - P3 fallback inventory (table of existing fallbacks +
        methodology-intent per each)
      - P5 causal-linkage question (2 options, pick one)
      - SW27 FVG initial guard (existing queued item)
      - SW31 displacement quality threshold (existing queued item)
    Value per session-hour is high; prep is where the leverage is.

C4_MapConfig_largely_unused:
  observation: |
    Advisor Lean/Bloat item 3 noted MapConfig as largely unused.
    I have not deep-verified. COO verification task: grep
    en1gma/console/map/context_types.py::MapConfig + every site
    that reads self._config from MapEngine. If confirmed unused,
    candidate for removal (aligned with D4 posture — "if a field
    is not live, enforce / reject / delete").
  verification_task: ~30 min grep + read
  owner: Opus or COO Claude (incoming CTO dispatches)

C5_chain_sequence_runtime_dispatch_unverified:
  observation: |
    Advisor Lean/Bloat item 1 noted chain.sequence parsed at load
    but runtime ordering may be hardcoded in chain_evaluator.
    I have not deep-verified. If true, sequence field is trust-debt
    (YAML says one thing, runtime does another) — same class as
    max_trades_per_window was pre-D4.
  verification_task: ~20 min read chain_evaluator.evaluate's step
                     ordering vs ChainConfig.sequence field usage
  owner: Opus or COO Claude

C6_governance_precedence_unverified:
  observation: |
    Advisor High 3 evidence line "governance_precedence appears
    unused in runtime." I have not deep-verified. If true, candidate
    for D4-pattern REMOVE with strict-mode rejection.
  verification_task: ~15 min grep
  owner: Opus or COO Claude

C7_sl_method_runtime_consumption_unverified:
  observation: |
    Advisor High 3 evidence line. I have not deep-verified.
    ChainConfig has sl_placement + sl_buffer_pips fields; the
    cartridge YAML has sl_method key. The loader's _build_chain_
    config derives sl_placement from sl_method (SWEEP_EXTREME →
    SWEEP_EXTREME_BUFFERED if sl_buffer > 0). Likely WIRED but
    worth confirming the runtime path honors the cartridge value.
  verification_task: ~15 min grep + trace
  owner: Opus or COO Claude

C8_orchestrator_file_has_29_references_to_SW_ids_in_body:
  observation: |
    en1gma/orchestrator/map_orchestrator.py and
    en1gma/console/chain/canon/map_canon/session.py carry heavy SW
    number embedding in docstrings + comments (SW02/03/04/07/08/09/
    24/30/33/36/37/39/40/41/42/43 cited inline). Useful for audit
    trail today; becomes noise as the kernel matures and those SW
    numbers feel archaic.
  implication: |
    Not Phase 4+ urgent. Worth a lean pass in a later phase —
    keep invariant citations (INV-* still useful); collapse SW
    citations into "see CLAUDE.md §15 SWxx" shorthand once the
    count exceeds a readable-in-line threshold.
  priority: LOW (lean-pass backlog)
```

---

## 5. Verification Gaps (30-90 min work; land before scope locks)

Items C4, C5, C6, C7 above. Plus:

```yaml
V1_ars_yaml_load_strategy_failure_mode:
  evidence: |
    Advisor High 3 cites "load_strategy(ars_v1_3.yaml) fails with
    schema mismatch." ARS YAML has strategy: as a nested mapping;
    load_strategy expects strategy: as a string (strategy name).
    Confirmed. Question: is this a real Phase 4+ item (unified
    loader) or deliberate (ARS bypasses StrategyParams intentionally
    per DEC-ARS-BYPASSES-MAP)?
  disposition: deliberate per current architecture; will close when
               schema v2 unifies dispatch. NOT a separate finding.
  verification: done

V2_MapTimeline_datetime_now_sites:
  evidence: advisor Medium 8 cites map_timeline.py:60-66 + session.
            py:445-451 omitting explicit time.
  sw25_registered: yes (Block 3 LOW)
  verification_needed: none — covered by SW25
```

---

## 6. Recommended Phase 4+ Ordering

```yaml
phase_4_opener_candidates:
  immediate_sprint:
    1: verification_pass (C4 + C5 + C6 + C7) — 90 min COO task;
       narrows Phase 4+ scope before dispatch
    2: P1 (SW47 gate direction filter) — ~1 hr; standalone
    3: P2 (SW48 fail-closed loader + split-brain) — ~1.5 hr;
       pairs with SW44 tier-3 entry-script work
  methodology_window:
    4: Olya session prep (C3) — batches P3 + P5 + SW27 + SW31
    5: Olya session execution
    6: Post-Olya methodology-dependent fixes (P3 + P5 +
       SW27-SW31 implementation)
  structural_sprint:
    7: cartridge schema v2 (SW38-SW43 cluster) — biggest item;
       coordinate Olya + CTO + G design session
  hygiene_sprints:
    8: SW44 tier-1 (tests annotation batch)
    9: SW44 tier-3 (utility scripts + henry:253 audit) — couples
       with P2 naturally
   10: P4 (SW50 H4 cascade replay fidelity) — standalone
   11: P6 (SW52 semantic detection parity) — standalone
   12: C4 MapConfig cleanup (if verified unused) — standalone
  deferred_backlog:
   13: SW44 tier-2 (ra_engine vendored) — gated on upstream
   14: SW06 / SW25 / SW11 / other Block 2-3 work
   15: SW34 full launcher convergence (option (a) beyond (a)-lite)
   16: walk-forward re-validation
   17: discovery scan v4 full coverage

bundle_recommendations:
  dont_split:
    - P1 + P2 (both correctness; ship before structural work)
    - SW38-SW43 cluster (one resolution surface)
    - P2 + SW44_tier_3 (same entry-script surface)
    - P3 + P5 + SW27 + SW31 (one Olya session prep pack)
  parallelisable:
    - SW44 tier-1 (tests) can run alongside any other sprint;
      it's pure mechanical
    - P6 (semantic parity) independent of everything else
    - C4 verification independent
```

---

## 7. "Swiss-Watch" Outcome Definition

Ratify as the success criterion for Phase 4+. Gives future-
reviewers + CTO + G a shared definition that isn't "SW list closed."

```yaml
swiss_watch_certification_criteria:
  smaller_in_authority_surfaces:
    - no duplicate dispatch paths (SW38-SW43 close this)
    - no dead cartridge fields (SW11 + C4/C5/C6/C7 close this)
    - no strategy-name string branches in console (SW29 closed;
      maintain)
  harsher_in_failure_behavior:
    - fail-closed on strategy load (P2 / SW48)
    - fail-closed on map init invalid input (P3 / SW49)
    - strict-mode rejection pattern for schema evolution (SW45
      precedent; maintain)
  stricter_in_config_truth:
    - every cartridge field enforced / rejected / absent
      (D4 posture; extend to residuals per C5/C6/C7)
    - no configuration split-brain between CLI and orchestrator
      (P2 / SW48)
  more_provable_in_replay_persistence:
    - terminal PDA persistence (SW06)
    - deterministic map_timeline (SW25)
    - full-state forensic roundtrip equivalence (new gate)
    - semantic detection parity (P6 / SW52)
  less_tolerant_of_plausible_state:
    - mixed-direction gate proof (P1 / SW47)
    - current-DR-scoped PDA proof (part of P1)
    - H4 cascade replay fidelity (P4 / SW50)
    - day_state causal linkage (P5 / SW51)
    - map init fallback inventory ruled by Olya (P3 / SW49)

non_negotiable_phase_4_exit_gates:
  1: P1_SW47_gate_direction_filter_proof
  2: P2_SW48_fail_closed_loader_proof (loader failure halts;
     split-brain closed)
  3: P3_SW49_map_init_fallback_ruled_and_applied
  4: P4_SW50_h4_cascade_replay_fidelity_proof
  5: P5_SW51_day_state_causal_linkage_ruled_and_applied
  6: P6_SW52_semantic_detection_parity_proof
  7: SW38-SW43 cluster resolved (cartridge schema v2 landed)
  8: SW44 tier-1 + tier-3 complete (tier-2 separate gate)

maintain_through_phase_4:
  - 853 + 4 test baseline (grows as new tests land; never shrinks)
  - lint-imports 6 KEPT / 0 broken every commit
  - mypy strict 0 errors on enforced surface every commit
  - atomic commit + parity gate discipline (Phase 3 precedent)
  - §11 finding_id_discipline (SWxx registration at moment of naming)
  - CHAIR SPLIT-HAZARD (flag + register + resolve, never silently
    preserve)
```

---

## 8. References

```yaml
primary:
  advisor_review: docs/reviews/ADVISOR_REVIEW_2026_04_26.md (b3f5e11)
  phase_3_retrospective: docs/plans/archive/PHASE_3_RETROSPECTIVE_2026_04_26.md (c7596fe)
  forward_plan: docs/canonical/FORWARD_PLAN.md v2.3
  findings_register: CLAUDE.md §15 (SW01-SW46)
  invariants: CLAUDE.md §6
  cartridge_contract: docs/canonical/CARTRIDGE_CONTRACT.md v1.0.3

sw_ids_referenced_for_incoming_cto:
  closed_phase_3: [SW29, SW30, SW34, SW35, SW36, SW37-partial, SW45, SW46]
  phase_4_pending_registered: [SW38, SW39, SW40, SW41, SW42, SW43, SW44]
  block_2_existing: [SW06, SW10, SW11, SW12, SW13, SW14, SW22, SW23, SW26, SW32]
  block_3_existing: [SW15, SW16, SW17, SW18, SW19, SW20, SW25, SW28]
  sw_candidates_this_document: [SW47, SW48, SW49, SW50, SW51, SW52]
  numbering_discipline: |
    P1-P7 numbers in this document are PRIORITY rankings, not SW
    IDs. SW IDs assigned at moment of formal registration per §11
    finding_id_discipline. Next free SW ID at session close: SW47.

commit_sha_references:
  phase_3_close: 9a0c7c7 (CLAUDE.md v0.15 + FORWARD_PLAN v2.3)
  phase_3_retrospective: c7596fe
  mypy_strict_CI_activation: 388ad25
  native_kernel_cleanup: 778704a
  advisor_review_archival: b3f5e11
```

---

*COO inputs artifact. Authoritative for Post-Phase-3 scope framing.*
*Advisor review (b3f5e11) is the raw input; this document is the
synthesis + reality-check + prioritisation. Incoming CTO dispatches
from this document; advisor review remains as the source trail.*