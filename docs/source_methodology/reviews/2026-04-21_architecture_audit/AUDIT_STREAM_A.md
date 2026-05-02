# AUDIT STREAM A — Architectural Drift Audit

## Ledger 1 — Architectural Commitments (Phase 1 Extraction)

> Sources read in required order: `docs/NORTH_STAR.md`, `docs/MAP_SPATIAL_PRIMER_v1.md`, `en1gma/methodology/HTF_MAP_SPEC_v0_1.yaml` (+ duplicate), `en1gma/methodology/SYNTHETIC_OLYA_METHOD_vLOCK.yaml`, `en1gma/methodology/calibration_results.yaml` (+ duplicate), `en1gma/methodology/STATE_DETECTION_LOGIC_v2.yaml`, `CLAUDE.md` §6, `docs/FORWARD_PLAN.md` (architectural content).

### C1. Two-clock separation is hard architecture
- **Commitment**: Map (slow clock) grants directional/location permission; execution (fast clock) handles trigger mechanics. Responsibilities never cross.
- **Source**: `NORTH_STAR.md` §3; `MAP_SPATIAL_PRIMER_v1.md` §1 (SEPARATION_RULE); `HTF_MAP_SPEC_v0_1.yaml` §1.
- **How to test**: Verify Map/context code does not place trades; verify chain/execution code requires upstream gate/direction and does not derive regime direction itself.

### C2. Universal chain is invariant infrastructure
- **Commitment**: Execution chain remains sweep → MSS → FVG → OTE → entry across strategies; strategy variation is not chain rewiring.
- **Source**: `NORTH_STAR.md` §3/§4; `MAP_SPATIAL_PRIMER_v1.md` §1/§4; `HTF_MAP_SPEC_v0_1.yaml` §7/§9.
- **How to test**: Verify chain evaluator enforces fixed step order and strategy configuration cannot alter chain topology.

### C3. Strategy = Map configuration (not codepath branching)
- **Commitment**: Strategy YAML/config should control map-scoped requirements (regime/PDA/zone/time windows), while chain engine remains common.
- **Source**: `NORTH_STAR.md` §2 (`strategy_as_configuration`), §7 (`DEC-MAP-IS-STRATEGY`); `MAP_SPATIAL_PRIMER_v1.md` §4; `HTF_MAP_SPEC_v0_1.yaml` §9.
- **How to test**: Verify loader surfaces strategy map constraints and orchestrator/gate enforces them at runtime.

### C4. Map v1 scope is constrained
- **Commitment**: v1 map scope is FVG-centric and intentionally bounded; broader PDA/liquidity/retrace/range behavior is deferred.
- **Source**: `calibration_results.yaml` Q5/Q6/Q9–Q11/Q16/Q17/Q20/Q21/Q24/Q25; `CLAUDE.md` §6 (`INV-MAP-SCOPE-V1.1`); `FORWARD_PLAN.md` capabilities + open items.
- **How to test**: Verify map PDA creation path only instantiates supported PDA types and respects declared scope boundaries.

### C5. Dealing range: wick-to-wick, rolling supersession
- **Commitment**: DR is wick-to-wick; each new pullback→displacement cycle supersedes prior DR; regime change resets context.
- **Source**: `MAP_SPATIAL_PRIMER_v1.md` §2 (Object 2); `calibration_results.yaml` Q1–Q4; `CLAUDE.md` §5.
- **How to test**: Verify DR builder uses wick inputs and marks prior range superseded when new range created.

### C6. PDA lifecycle is 5-state with permanent TOUCHED
- **Commitment**: OPEN → TOUCHED → REJECTED/MITIGATED/INVALIDATED, with TOUCHED persistent and no age expiry.
- **Source**: `calibration_results.yaml` Q12/Q15/Q27; `CLAUDE.md` §5/§6; `context model in HTF_MAP_SPEC + calibration lock`.
- **How to test**: Verify state enum + transitions match model; verify no age-based pruning logic.

### C7. PDA timestamp invariant
- **Commitment**: `PDA.created_at` must represent Candle C confirmation time, not Candle A anchor.
- **Source**: `CLAUDE.md` §6 (`INV-PDA-CREATED-AT-CONFIRMATION`); calibration timestamp note in `calibration_results.yaml` (FVG timestamp concern).
- **How to test**: Trace detector event timestamp semantics and map PDA creation call site.

### C8. Cross-session persistence must preserve slow-clock state
- **Commitment**: Map state (including relevant PDA lifecycle state) survives restarts/cold-start boundaries.
- **Source**: `NORTH_STAR.md` §3 (Map persistence), `HTF_MAP_SPEC_v0_1.yaml` §8 (initialization/persistence), `CLAUDE.md` map/persistence sections.
- **How to test**: Verify persistence serialization captures full required PDA lifecycle set, not a lossy subset.

### C9. Governance is mandatory chokepoint
- **Commitment**: No capital action without governance check; halt overrides all; live requires explicit graduation/T2 path.
- **Source**: `NORTH_STAR.md` §2/§5; `CLAUDE.md` §6 governance invariants; `FORWARD_PLAN.md` SW08 closure text.
- **How to test**: Verify orchestrator checks governance before broker call and governance code enforces halt/lease/risk/live-mode contracts.

### C10. Detection authority and timestamp contract
- **Commitment**: `detect.py` is sole detection authority; detection timestamps are tz-aware at source.
- **Source**: `NORTH_STAR.md` §7 (`DEC-ORACLE-SINGLETON`), `CLAUDE.md` §6 (`INV-DETECTION-AUTHORITY-SINGLETON`, `INV-DETECTION-TIME-TZ-AWARE`), `FORWARD_PLAN.md` SW24 architecture notes.
- **How to test**: Verify context/control call detection via `detect.py` facade; verify detector emission + core Detection model reject naive timestamps.

### C11. Gate conditions + kill-zone dependence
- **Commitment**: Gate arming requires (direction permission + active PDA/contact in correct zone + kill-zone timing); selection is first reached/nearest valid PDA.
- **Source**: `MAP_SPATIAL_PRIMER_v1.md` §2 Object 4; `calibration_results.yaml` Q18/Q19/Q22/Q23; `HTF_MAP_SPEC_v0_1.yaml` §5/§6.
- **How to test**: Verify gate implementation applies all conditions and PDA selection logic.

### Architectural ambiguities identified from docs (not forced into single truth)
1. **Kill-zone definitions conflict**:
   - Narrow reversal windows: `SYNTHETIC_OLYA_METHOD_vLOCK.yaml` (NY_WINDOWS) and `MAP_SPATIAL_PRIMER_v1.md` examples emphasize **03:00–04:00** and **08:00–09:00 NY**.
   - Broader gating windows: `HTF_MAP_SPEC_v0_1.yaml` and deployed strategy YAMLs use **02:00–05:00** and **07:00–10:00 NY**.
2. **Map scope wording tension**:
   - `INV-MAP-SCOPE-V1.1` wording in `CLAUDE.md` centers “daily regime + daily FVG.”
   - Calibration Q22/Q23 (`calibration_results.yaml`) locks daily/4H PDA parity logic.

---

## Ledger 2 — Drift + Conformance Findings (Phase 2 Audit)

### C1. Two-clock separation is hard architecture
- **Verdict**: **Conformance**
- **Evidence**:
  - `en1gma/control/map_orchestrator.py:490-537`
    - `chain_result = chain_evaluator.evaluate(...)`
    - `intent = build_intent_from_chain(...)`
    - `gov = check_governance(mode, halt, lease, risk_state, risk_limits_obj)`
    - Trade path proceeds only after gate+chain+governance.
  - `en1gma/chain/chain_evaluator.py:146-162`
    - `if gate_result.state != GateState.ARMED or gate_result.direction is None: return self._incomplete(...)`
    - `direction = gate_result.direction`
- **Assessment**: Execution only runs when gate arms; chain reads direction from gate, not map/regime recomputation.

### C2. Universal chain is invariant infrastructure
- **Verdict**: **Conformance**
- **Evidence**:
  - `en1gma/chain/chain_evaluator.py:163-201`
    - Fixed step progression in code: `_match_sweep(...)` → `_match_mss(...)` → `_match_fvg(...)` → `_check_ote(...)`.
  - `en1gma/chain/chain_config.py:1-8`
    - Module contract text: `The chain SEQUENCE is fixed (sweep → MSS → FVG → OTE).`
- **Assessment**: Chain topology is hardcoded and strategy-agnostic.

### C3. Strategy = Map configuration (runtime enforcement)
- **Verdict**: **Drift (partial implementation of config surface)**
- **Evidence**:
  - Loader captures map-constraint fields:
    - `en1gma/strategies/loader.py:225-236`
      - `regime_required_phase=...`
      - `regime_direction_permission=...`
      - `pda_types=...`
      - `pda_timeframes=...`
  - Orchestrator uses only subset of strategy surface:
    - `en1gma/control/map_orchestrator.py:271-275`
      - uses `max_trades_per_day`, kill-zone windows, `ltf_tfs_config`
      - no use of `pda_types/pda_timeframes/regime_required_phase/regime_direction_permission`
  - Zero references in orchestrator for these fields:
    - `en1gma/control/map_orchestrator.py` search for `regime_required_phase|pda_types|pda_timeframes|regime_direction_permission` → no matches.
- **Assessment**: Strategy map-configuration schema exists but key map-level constraints are not enforced in runtime path.

### C4. Map v1 scope constraints
- **Verdict**: **Mixed (conformance + scope tension)**
- **Evidence (conformance)**:
  - `en1gma/context/pda_store.py:33-36`
    - `"Manages PDA lifecycle. v1 = FVG only."`
  - `en1gma/context/pda_store.py:35-74`
    - creation entrypoint is `add_fvg(...)`; instantiated `type=PDAType.FVG`.
- **Evidence (tension/drift against declared strategy filter)**:
  - `en1gma/strategies/daily_expansion.yaml:20-22`
    - `pda.timeframes: [DAILY]`
  - `en1gma/context/map_engine.py:201-206`
    - `tfs = [tf for tf in ["1D", "4H"] if tf in bars_by_tf]`
  - `en1gma/context/map_engine.py:552-556`
    - `authority = AuthorityTF.DAILY if tf_key == "1D" else AuthorityTF.H4`
- **Assessment**: PDA type scope is FVG-only (conformant), but timeframe scope enforcement remains inconsistent with strategy-declared `DAILY` filter.

### C5. Dealing range wick-to-wick rolling supersession
- **Verdict**: **Conformance**
- **Evidence**:
  - `en1gma/context/dealing_range.py:36-60`
    - `create_range(origin_wick, extreme_wick, ...)`
    - previous `self.current` marked `SUPERSEDED` before setting new `ACTIVE` range.
  - `en1gma/context/map_engine.py:212-220`
    - daily validity check and H4 fallback (`_compute_h4_dealing_range`) for authority cascade.
- **Assessment**: Implementation aligns with wick-based rolling range model and daily→H4 authority behavior.

### C6. PDA lifecycle 5-state + permanent TOUCHED + no age expiry
- **Verdict**: **Conformance**
- **Evidence**:
  - `en1gma/context/context_types.py:50-55`
    - `PDAStatus = OPEN, TOUCHED, REJECTED, MITIGATED, INVALIDATED`.
  - `en1gma/context/pda_store.py:99-117`
    - OPEN transitions to TOUCHED on any zone contact.
  - `en1gma/context/pda_store.py:140-146`
    - explicit `reject_pda(...)` transition to REJECTED.
  - `en1gma/context/pda_store.py:162-179`
    - gate candidate states limited to active statuses (`OPEN`, `TOUCHED`), no revert-to-OPEN logic.
  - `en1gma/context/pda_store.py` (entire file) and `en1gma/context/regime.py` contain no PDA age-based expiry logic.
- **Assessment**: Lifecycle semantics and no-age-expiry behavior are present.

### C7. PDA created_at must be Candle C confirmation
- **Verdict**: **Drift**
- **Evidence**:
  - Detector timestamps FVG on anchor/candle A:
    - `en1gma/detection/ra_engine/detectors/fvg.py:219-223`
      - `# Use anchor time for the detection timestamp (candle A).`
      - `det_time = to_ny_aware(fvg["anchor_time"])`
    - Anchor assigned from bar A:
      - `en1gma/detection/ra_engine/detectors/fvg.py:111-114`
      - `anchor_time = ... ts_ny_series.iloc[i - 2]`
      - `detect_time = ... ts_ny_series.iloc[i]`
  - Map copies that detection time into PDA `created_at`:
    - `en1gma/context/map_engine.py:571-579`
      - `created_at=fvg.time`
- **Assessment**: Current code stamps PDA creation from candle A timestamp path, contradicting invariant requiring candle C confirmation timestamp.

### C8. Cross-session persistence preserves slow-clock state
- **Verdict**: **Drift (lossy persistence)**
- **Evidence**:
  - Serializer schema declares both arrays but populates only active subset:
    - `en1gma/context/map_persistence.py:60-66`
      - includes `"active_pdas": []` and `"all_pdas": []`
    - `en1gma/context/map_persistence.py:81-83`
      - loops only `for pda in state.active_pdas: ...`
  - Deserializer restores only active list:
    - `en1gma/context/map_persistence.py:133`
      - `active_pdas = [_deserialize_pda(p) for p in data.get("active_pdas", [])]`
- **Assessment**: Terminal PDA lifecycle history is not serialized/restored by this path.

### C9. Governance mandatory chokepoint, halt precedence, live gating
- **Verdict**: **Conformance**
- **Evidence**:
  - Runtime authorization before broker open:
    - `en1gma/control/map_orchestrator.py:533-549`
      - `gov = check_governance(...)`; blocked path `continue` on reject.
      - `broker.open_position(...)` only after approved governance.
  - Halt overrides + lease/risk checks:
    - `en1gma/control/governance.py:183-195` (halt first, blocker HALT)
    - `en1gma/control/governance.py:197-207` (lease block)
    - `en1gma/control/governance.py:209-219` (risk block)
  - Live-mode blocked pending ceremony/T2 contract:
    - `en1gma/control/governance.py:129-133` (`mode == LIVE` → `NotImplementedError`).
- **Assessment**: Governance chokepoint and fail-closed semantics are wired in audited surfaces.

### C10. Detection authority singleton + tz-aware detection times
- **Verdict**: **Conformance**
- **Evidence**:
  - Detection facade contract:
    - `en1gma/detection/detect.py:1-4`
      - `"Detection oracle — sole detection authority."`
  - Context/control consume facade `run_detection(...)`:
    - `en1gma/context/map_engine.py:194-207`
    - `en1gma/control/map_orchestrator.py:463-466`
  - tz-aware enforcement:
    - `en1gma/detection/ra_engine/engine/base.py:78-90`
      - `Detection.__post_init__` raises on naive `time`.
    - `en1gma/detection/ra_engine/detectors/_common.py:14-35`
      - `to_ny_aware(...)` localizes/normalizes detector timestamps.
- **Assessment**: Audited path consistently routes detection through the singleton facade and enforces aware timestamps at source.

### C11. Gate conditions + PDA selection semantics
- **Verdict**: **Conformance to implemented model; doc ambiguity remains**
- **Evidence**:
  - Gate requires permission + PDA existence/location + contact + kill-zone:
    - `en1gma/gating/execution_gate.py:1-8` (explicit 4-condition header)
    - `en1gma/gating/execution_gate.py:98-124` (permission + candidates + contact)
    - `en1gma/gating/execution_gate.py:136-143` (kill-zone required)
  - Primary PDA selection by nearest/contacted candidate:
    - `en1gma/gating/execution_gate.py:125`
      - `armed_pda = min(contact_pdas, key=lambda p: abs(p.zone_midpoint - current_price))`
- **Assessment**: Gate logic is explicit and deterministic; however, implemented kill-zone windows follow broad 02:00–05:00 / 07:00–10:00 model, which conflicts with narrow-window doctrine in other docs.

---

## Summary of Drift Findings (evidence-backed)
1. **Strategy config enforcement gap**: map-scoped strategy fields are loaded but not enforced in map-gated runtime path (`loader.py` vs `map_orchestrator.py`).
2. **PDA timestamp invariant breach**: PDA `created_at` is sourced from detector FVG timestamp that is explicitly candle A anchor time.
3. **Lossy map persistence**: persistence serializes only `active_pdas`; terminal lifecycle states are not retained by this serializer/deserializer path.
4. **Scope/timing tensions**:
   - H4 PDA ingestion present despite strategy-level DAILY-only timeframe declaration.
   - Kill-zone implementation matches broad windows while doctrine corpus contains contradictory narrow-window statements.
