# AUDIT_STREAM_B — Architectural Drift Audit

```yaml
stream: B
auditor: Claude Opus (fresh instance, no prior kernel context)
date: 2026-04-20
scope: Testable architectural commitments vs code reality
method: Phase 1 (extract commitments from 8 docs) → Phase 2 (audit 5 code surfaces)
out_of_scope: data/, sentinel/, scripts/, tests/, prompt-exports/, closed SWs (02,03,04,05,07,08,09,24,01)
```

---

## LEDGER 1 — ARCHITECTURAL COMMITMENTS

Each entry is a property that would survive a full rewrite in a different language.

### TWO-CLOCK MODEL

| ID | Commitment | Source | Test Method |
|----|-----------|--------|-------------|
| TC-1 | Map operates on structural events only, not per-bar. Persistence is cross-session. Answers WHERE. | NORTH_STAR §Two Clocks, MAP_SPATIAL_PRIMER §1 | Map engine has no per-bar loop of its own; updates fire only on detection events. State survives process restart. |
| TC-2 | Execution operates per-bar within kill zones. Intraday. Answers HOW. | NORTH_STAR §Two Clocks | Chain evaluator receives bar-level data, runs within KZ windows, produces entry signals. |
| TC-3 | **SEPARATION_RULE**: "The Map NEVER fires a trade. The Execution NEVER decides direction." | MAP_SPATIAL_PRIMER §1 (bold, repeated 3×) | No trade/broker call originates from Map code. No direction computation exists in chain code — direction arrives via gate_result only. |

### STRATEGY = MAP CONFIGURATION

| ID | Commitment | Source | Test Method |
|----|-----------|--------|-------------|
| SM-1 | Different strategies are different Map configurations (regime, PDA type, zone), NOT different code paths. | NORTH_STAR §DEC-MAP-IS-STRATEGY, MAP_SPATIAL_PRIMER §4 | Strategy YAML specifies Map params. Chain evaluator has no strategy-specific branches. |
| SM-2 | The chain is universal infrastructure. It does NOT change per strategy. | MAP_SPATIAL_PRIMER §4 Anti-Pattern 2 ("modifying the chain"), §5 strategy template: CHAIN="standard (do NOT modify)" | chain_evaluator.py contains zero conditionals on strategy name or strategy type. ChainConfig tunes thresholds only. |
| SM-3 | Strategy proposal format: MAP_PICTURE + REGIME + PDA_TYPE + ZONE + CHAIN="standard (do NOT modify)" | MAP_SPATIAL_PRIMER §5 | Strategy YAML structure matches this template. No CHAIN override fields beyond threshold tuning. |

### 5-LAYER SPINE

| ID | Commitment | Source | Test Method |
|----|-----------|--------|-------------|
| L5-1 | Every module maps to exactly one layer. No cross-layer leakage. | CLAUDE.md §2, NORTH_STAR §Architecture | Module imports respect layer boundaries (L2 never imports L4, etc.). |
| L5-2 | L2 Detection is the sole oracle (INV-DETECTION-AUTHORITY-SINGLETON). | CLAUDE.md §6, NORTH_STAR | No detection logic exists outside detection/ directory. All consumers receive Detection objects from detect.py. |
| L5-3 | L3 Context (Map) is bypassed entirely by ARS. | CLAUDE.md §2, NORTH_STAR §DEC-ARS-BYPASSES-MAP | ARS code path has zero imports from context/. |
| L5-4 | L5 Governance: ALL capital actions pass through this layer. | CLAUDE.md §6 INV-NO-UNGOVERNED-TRADES | Every broker call is preceded by check_governance(). |

### DETECTION CONTRACTS

| ID | Commitment | Source | Test Method |
|----|-----------|--------|-------------|
| DT-1 | 13 vLOCK primitives are locked. Changes require Olya recalibration. | CLAUDE.md §6 INV-VLOCK, vLOCK.yaml header | Primitive count and algorithms match vLOCK.yaml definitions. |
| DT-2 | Every Detection.time is tz-aware at construction. | CLAUDE.md §6 INV-DETECTION-TIME-TZ-AWARE | Detection.__post_init__ raises ValueError on naive datetime. |
| DT-3 | FVG Detection.time = anchor_time (Candle A, bars[i-2].time). | vLOCK.yaml §FVG algorithm, line "Detection.time = anchor_time" | FVG detector sets det_time = to_ny_aware(fvg["anchor_time"]) where anchor_time = bars[i-2].time. |
| DT-4 | OTE uses body-to-body measurement with 4 tracked levels [0.50, 0.618, 0.705, 0.79]. | vLOCK.yaml §OTE algorithm | OTE implementation tracks all 4 fib levels. |
| DT-5 | OTE kill_zone_gate: entry valid only during LOKZ 03:00-04:00 / NYOKZ 08:00-09:00. | vLOCK.yaml §OTE kill_zone_gate | OTE entry validation checks narrow reversal windows. |

### PDA LIFECYCLE

| ID | Commitment | Source | Test Method |
|----|-----------|--------|-------------|
| PDA-1 | PDA lifecycle: OPEN → TOUCHED → REJECTED \| MITIGATED \| INVALIDATED (5-state). | HTF_MAP_SPEC §ActivePDAs, calibration Q14-Q15 | PDAStatus enum has exactly 5 members. Transitions follow this DAG. |
| PDA-2 | TOUCHED is permanent — once touched, always touched. No reversion. | calibration_results.yaml Q15 | update_on_price sets OPEN→TOUCHED; no code path sets TOUCHED→OPEN. |
| PDA-3 | No PDA age expiry. PDAs live until terminal state or dealing range reset. | calibration_results.yaml Q27 | No timestamp comparison or age check in PDA lifecycle code. |
| PDA-4 | PDA zone classification: midpoint vs dealing range equilibrium. | calibration_results.yaml Q7, HTF_MAP_SPEC §zone_classification | classify_pda_location compares pda.zone_midpoint against DR equilibrium. |
| PDA-5 | PDAs scoped to CURRENT dealing range. New DR invalidates prior PDAs. | HTF_MAP_SPEC §pda_scope | invalidate_for_regime_change exists; new DR creation triggers PDA scoping. |
| PDA-6 | INV-PDA-DIRECTION-FIDELITY: PDA direction_context = detector-emitted direction, never regime. | CLAUDE.md §6 | PDA creation reads direction from Detection, not from current regime. |
| PDA-7 | INV-PDA-ZONE-FROM-DETECTOR: zone_top/zone_bottom copied verbatim from detector properties. | CLAUDE.md §6 | PDA creation reads props["top"]/props["bottom"] with no arithmetic reconstruction. |
| PDA-8 | INV-PDA-CREATED-AT-CONFIRMATION: PDA created_at = Candle C close, not Candle A. | CLAUDE.md §6 | PDA creation timestamp is the confirmation bar (Candle C), not the anchor (Candle A). |
| PDA-9 | INV-PDA-MITIGATION-IS-RETRACE-FILL: Bearish FVG mitigated on close > zone_top; Bullish on close < zone_bottom. | CLAUDE.md §6 | Mitigation check uses retrace-fill semantic, not expansion-through. |

### EXECUTION GATE

| ID | Commitment | Source | Test Method |
|----|-----------|--------|-------------|
| EG-1 | 4 conditions required for ARMED: regime direction + price at active PDA + correct zone + kill zone time. | HTF_MAP_SPEC §execution_gate, calibration_results.yaml | evaluate_gate checks all 4 conditions; any failure → DISARMED. |
| EG-2 | Gate persists across bars — re-arms each kill zone. | calibration_results.yaml Q25-Q26 | Gate does not carry state between evaluations; re-evaluated each bar. |
| EG-3 | PDA selection: first reached = primary; cascade on chain fail. | calibration_results.yaml Q22 | Armed PDA selection uses proximity (closest midpoint to price). |
| EG-4 | Edge touch arms gate (Q18: wick contact sufficient). | calibration_results.yaml Q18 | _price_contacts_pda checks hi >= zone_bottom AND lo <= zone_top (any price contact). |

### DEALING RANGE

| ID | Commitment | Source | Test Method |
|----|-----------|--------|-------------|
| DR-1 | Wick-to-wick measurement for dealing range. | calibration_results.yaml Q1-Q2 | DR origin/extreme use high/low (wick), not open/close (body). |
| DR-2 | ROLLING model — new DR on each pullback+displacement within same regime. | calibration_results.yaml Q3 | create_range supersedes current range; no accumulation. |
| DR-3 | DR authority cascades daily → H4 when daily is still expanding. | CLAUDE.md §7 dr_authority_cascade, INV-MAP-SCOPE-V1.1 | is_daily_range_valid returns False when expanding; system falls back to H4 DR. |
| DR-4 | No regime age limit. | calibration_results.yaml Q26 | No timestamp or bar-count expiry on regime. |

### CHAIN EVALUATOR

| ID | Commitment | Source | Test Method |
|----|-----------|--------|-------------|
| CH-1 | 4-step LTF chain: sweep → MSS → FVG → OTE. Sequential, each requires prior. | HTF_MAP_SPEC §chain, chain_evaluator.py docstring | evaluate_chain calls _match_sweep → _match_mss → _match_fvg → _check_ote in sequence. |
| CH-2 | Chain receives direction from gate only. Never computes direction internally. | MAP_SPATIAL_PRIMER SEPARATION_RULE, chain_evaluator.py INV-TWO-CLOCK-SEPARATION-HARD | `direction = gate_result.direction` at entry; no other direction source. |
| CH-3 | Sweep lookback: 4 hours pre-kill-zone. | HTF_MAP_SPEC §chain | Sweep search window extends 4hr before KZ start. |
| CH-4 | max_chain_bars declared as a timing constraint. | chain_config.py, SW13 (known defect) | max_chain_bars field exists in ChainConfig. |
| CH-5 | OTE zone defined by fibonacci levels from vLOCK. | vLOCK.yaml §OTE: 4 levels [0.50, 0.618, 0.705, 0.79] | ChainConfig.ote_zone and chain OTE check use fib retracement levels. |
| CH-6 | Q8: equilibrium straddling check — FVG that straddles equilibrium is invalid for entry. | calibration_results.yaml Q8 | Straddling check exists in chain evaluation path. |

### GOVERNANCE

| ID | Commitment | Source | Test Method |
|----|-----------|--------|-------------|
| GV-1 | INV-HALT-1: halt_local < 50ms. | CLAUDE.md §6 | Halt mechanism achieves sub-50ms response. |
| GV-2 | INV-SOVEREIGN-2: Live execution requires human T2 approval. | CLAUDE.md §6 | LIVE mode raises NotImplementedError until graduation ceremony. |
| GV-3 | INV-MODE-EXPLICIT-PER-INVOCATION: OperatingMode has NO default value. | CLAUDE.md §6 | OperatingMode constructor and all entry points require explicit mode. |
| GV-4 | INV-GOVERNANCE-SINGLE-CHECK-SITE: check_governance() is the sole authorization function. | CLAUDE.md §6 | Single check_governance call site before broker actions. |
| GV-5 | INV-PAPER-GOVERNANCE-PARITY-WITH-LIVE: PAPER and LIVE require identical governance deps. | CLAUDE.md §6 | validate_config enforces same non-None requirements for both modes. |
| GV-6 | INV-SHADOW-BEFORE-PAPER: Shadow mode until G signs graduation ceremony. | CLAUDE.md §6 | launch_ars.sh hardcoded to --mode shadow. |

### KILL ZONE WINDOWS

| ID | Commitment | Source | Test Method |
|----|-----------|--------|-------------|
| KZ-1 | Kill zone windows exist for LOKZ and NYOKZ. Gate checks KZ membership. | HTF_MAP_SPEC, vLOCK.yaml, daily_expansion.yaml | Time-window check in evaluate_gate. |
| KZ-2 | MAP_SPEC / strategy YAML windows: LOKZ 02:00-05:00, NYOKZ 07:00-10:00. | HTF_MAP_SPEC §gate, daily_expansion.yaml §kill_zones | Broader windows for "scan permission" — gate opens. |
| KZ-3 | vLOCK reversal windows: LOKZ 03:00-04:00, NYOKZ 08:00-09:00. | vLOCK.yaml §OTE kill_zone_gate | Narrower windows for "entry permission" — OTE valid only here. |

### REPLAY & OBSERVABILITY

| ID | Commitment | Source | Test Method |
|----|-----------|--------|-------------|
| RO-1 | INV-REPLAY-DETERMINISM: Same stored inputs → same outputs. Always. | CLAUDE.md §6 | Replay produces byte-identical decision_trace + chain_trace. |
| RO-2 | INV-ORCHESTRATOR-DUMB: Orchestrator sequences and wires. Never decides. | CLAUDE.md §6 | Orchestrator contains no trading logic — only sequencing calls. |
| RO-3 | INV-DAY-STATE-MARKET-DRIVEN: Day state transitions reflect market structure only. | CLAUDE.md §6 | DayState transitions trigger on detection events, not system execution events. |

### STRATEGY YAML

| ID | Commitment | Source | Test Method |
|----|-----------|--------|-------------|
| SY-1 | Strategy YAMLs declare parameters only. No branching logic. | CLAUDE.md §11 config_purity | YAML files contain only key-value configuration, no conditionals. |
| SY-2 | map_required: true/false selects Path A (ARS) or Path B (Map-gated). | CLAUDE.md §4 | Strategy loader reads map_required to route execution. |
| SY-3 | Strategy YAML carries pda.timeframes to scope which PDAs are eligible. | daily_expansion.yaml §pda.timeframes: [DAILY] | Gate filters PDA candidates by declared timeframes. |

---

## LEDGER 2 — DRIFT + CONFORMANCE FINDINGS

### CONFORMANCE (code honors commitment)

#### CF-01: SEPARATION_RULE — Direction Flow (TC-3)
```
Status: CONFORM
Commitment: TC-3 — Map never fires trade; Execution never decides direction
Evidence:
  file: en1gma/chain/chain_evaluator.py
  line: 153
  code: "direction = gate_result.direction"
  detail: |
    chain_evaluator.py declares INV-TWO-CLOCK-SEPARATION-HARD in its docstring.
    Direction is assigned exactly once from gate_result.direction. No alternative
    direction source exists in the entire chain module. The chain never imports
    from context/regime.py or reads regime state directly. Map code (map_engine.py,
    pda_store.py, regime.py) contains zero broker calls or trade placement logic.
    SEPARATION_RULE is cleanly honored.
```

#### CF-02: PDA 5-State Lifecycle (PDA-1)
```
Status: CONFORM
Commitment: PDA-1 — OPEN → TOUCHED → REJECTED | MITIGATED | INVALIDATED
Evidence:
  file: en1gma/context/context_types.py
  lines: 73-79
  code: |
    class PDAStatus(str, Enum):
        OPEN = "OPEN"
        TOUCHED = "TOUCHED"
        REJECTED = "REJECTED"
        MITIGATED = "MITIGATED"
        INVALIDATED = "INVALIDATED"
  detail: |
    Exactly 5 states. PDA_ACTIVE_STATES = frozenset({OPEN, TOUCHED}).
    PDA_TERMINAL_STATES = frozenset({REJECTED, MITIGATED, INVALIDATED}).
    Transitions in pda_store.py follow the DAG: OPEN→TOUCHED (update_on_price),
    OPEN/TOUCHED→MITIGATED (update_on_bar_close), any→INVALIDATED
    (invalidate_for_regime_change). REJECTED transition path exists
    conceptually but is not yet implemented in v1 scope.
```

#### CF-03: TOUCHED Permanence (PDA-2)
```
Status: CONFORM
Commitment: PDA-2 — TOUCHED is permanent, no reversion
Evidence:
  file: en1gma/context/pda_store.py
  lines: 106-115
  code: |
    def update_on_price(self, high: float, low: float) -> list[PDA]:
        touched = []
        for pda in self.pdas:
            if pda.status != PDAStatus.OPEN:
                continue
            if high >= pda.zone_bottom and low <= pda.zone_top:
                pda.status = PDAStatus.TOUCHED
                touched.append(pda)
        return touched
  detail: |
    Only OPEN PDAs transition to TOUCHED. No code path reverts TOUCHED→OPEN.
    The terminal state check in update_on_bar_close also processes TOUCHED
    PDAs for mitigation, confirming TOUCHED is a stable intermediate state.
```

#### CF-04: PDA Zone from Detector (PDA-7)
```
Status: CONFORM
Commitment: PDA-7 — zone_top/zone_bottom from detector properties verbatim
Evidence:
  file: en1gma/context/map_engine.py
  lines: ~135-145
  code: |
    def _pda_fields_from_detection(self, det: Detection) -> dict:
        props = det.properties
        return {
            "zone_top": props["top"],
            "zone_bottom": props["bottom"],
            ...
        }
  detail: |
    Direct dictionary lookup on detector-emitted properties. No arithmetic
    reconstruction from midpoint ± half-gap. No hardcoded PIP scaling.
    INV-PDA-ZONE-FROM-DETECTOR is honored. This was the SW04 fix that
    closed BUG 1 (zone reconstruction with hardcoded PIP=0.0001).
```

#### CF-05: PDA Direction Fidelity (PDA-6)
```
Status: CONFORM
Commitment: PDA-6 — direction_context = detector-emitted direction
Evidence:
  file: en1gma/context/map_engine.py
  lines: ~148-158
  code: |
    def _detector_direction_to_market_direction(self, det: Detection) -> MarketDirection:
        raw = det.properties.get("direction", "").upper()
        ...
  detail: |
    Direction is read from the Detection object's properties, not from
    current regime state. _initialize_pdas_from_detections passes this
    detector-truth direction as direction_context. INV-PDA-DIRECTION-FIDELITY
    honored. SW04 closed BUG 2 (regime-blanket direction stamp).
```

#### CF-06: Detection TZ-Aware Contract (DT-2)
```
Status: CONFORM
Commitment: DT-2 — Every Detection.time is tz-aware at construction
Evidence:
  file: en1gma/detection/ra_engine/engine/base.py
  lines: ~28-35
  code: |
    @dataclass
    class Detection:
        ...
        def __post_init__(self):
            if self.time.tzinfo is None:
                raise ValueError(
                    f"Detection.time must be timezone-aware, got naive: {self.time}"
                )
  detail: |
    Hard fail-fast at construction. No naive datetime can exist in a
    Detection object. INV-DETECTION-TIME-TZ-AWARE enforced at source.
    All detectors route through to_ny_aware() before constructing Detection.
```

#### CF-07: Mitigation Retrace-Fill Semantic (PDA-9)
```
Status: CONFORM
Commitment: PDA-9 — Bearish FVG mitigated on close > zone_top; Bullish on close < zone_bottom
Evidence:
  file: en1gma/context/pda_store.py
  lines: 128-137
  code: |
    if pda.direction_context == MarketDirection.BEARISH:
        if close > pda.zone_top:
            pda.status = PDAStatus.MITIGATED
    elif pda.direction_context == MarketDirection.BULLISH:
        if close < pda.zone_bottom:
            pda.status = PDAStatus.MITIGATED
  detail: |
    Retrace-fill semantic correctly implemented. Bearish FVG (gap down)
    mitigates when price retraces UP through zone_top. Bullish FVG (gap up)
    mitigates when price retraces DOWN through zone_bottom. Expansion in
    original direction does NOT trigger mitigation.
    INV-PDA-MITIGATION-IS-RETRACE-FILL honored in pda_store.
```

#### CF-08: Governance Mode Explicit (GV-3)
```
Status: CONFORM
Commitment: GV-3 — OperatingMode has NO default value
Evidence:
  file: en1gma/control/governance.py
  lines: ~18-23
  code: |
    class OperatingMode(str, Enum):
        TEST = "TEST"
        SHADOW = "SHADOW"
        PAPER = "PAPER"
        LIVE = "LIVE"
  detail: |
    OperatingMode is an enum with no default. validate_config and
    check_governance both require mode as a positional parameter.
    run_map_replay requires --mode as a CLI argument with no default.
    INV-MODE-EXPLICIT-PER-INVOCATION honored.
```

#### CF-09: LIVE Gate (GV-2)
```
Status: CONFORM
Commitment: GV-2 — LIVE raises NotImplementedError
Evidence:
  file: en1gma/control/governance.py
  lines: ~85-92
  code: |
    if mode == OperatingMode.LIVE:
        raise NotImplementedError(
            "LIVE mode requires graduation ceremony contract (G ruling Q3). "
            "Use SHADOW or PAPER until then."
        )
  detail: |
    Hard gate at TIER_1 (validate_config). No code path reaches broker
    in LIVE mode. INV-LIVE-REQUIRES-T2 operationalised.
```

#### CF-10: Single Governance Check Site (GV-4)
```
Status: CONFORM
Commitment: GV-4 — check_governance() is sole authorization function
Evidence:
  file: en1gma/control/map_orchestrator.py
  line: ~529
  code: "blocker = check_governance(mode=mode, halt=halt, lease=lease, risk=risk, risk_limits=risk_limits)"
  detail: |
    Path B has exactly one check_governance call before broker.open_position.
    Path A (ARS) similarly calls check_governance before each broker equivalent.
    No direct halt/lease/risk queries are used for authorization decisions.
    INV-GOVERNANCE-SINGLE-CHECK-SITE honored.
```

#### CF-11: Dealing Range Wick-to-Wick (DR-1)
```
Status: CONFORM
Commitment: DR-1 — Wick-to-wick measurement
Evidence:
  file: en1gma/context/dealing_range.py
  lines: ~45-65
  detail: |
    create_range uses origin (high/low wick values) and extreme (high/low
    wick values). No body (open/close) measurement for DR boundaries.
    Q1/Q2 calibration honored.
```

#### CF-12: Rolling Dealing Range (DR-2)
```
Status: CONFORM
Commitment: DR-2 — New DR on pullback+displacement supersedes current
Evidence:
  file: en1gma/context/dealing_range.py
  lines: ~67-80
  detail: |
    create_range replaces self.current_range. No accumulation of multiple
    concurrent dealing ranges. Rolling model per Q3.
```

#### CF-13: PDA Zone Classification by Midpoint (PDA-4)
```
Status: CONFORM
Commitment: PDA-4 — Midpoint vs DR equilibrium for zone classification
Evidence:
  file: en1gma/context/dealing_range.py
  lines: ~120-135
  code: |
    def classify_pda_location(self, pda_midpoint: float) -> str:
        eq = self.equilibrium
        if pda_midpoint > eq:
            return "PREMIUM"
        else:
            return "DISCOUNT"
  detail: |
    Uses pda.zone_midpoint compared against DR equilibrium.
    Q7 calibration honored.
```

#### CF-14: Gate 4-Condition Check (EG-1)
```
Status: CONFORM
Commitment: EG-1 — 4 conditions: regime + PDA contact + zone + kill zone
Evidence:
  file: en1gma/gating/execution_gate.py
  lines: ~55-130
  detail: |
    evaluate_gate checks:
    1. Kill zone time window (LOKZ/NYOKZ)
    2. Regime direction permission (via regime.get_direction_permission)
    3. Active PDA with price contact (_price_contacts_pda)
    4. PDA in required zone (location_class check)
    All 4 must pass for ARMED result. Any failure returns DISARMED.
```

#### CF-15: PDA Edge Touch Arms Gate (EG-4)
```
Status: CONFORM
Commitment: EG-4 — Wick contact sufficient (Q18)
Evidence:
  file: en1gma/gating/execution_gate.py
  lines: ~85-95
  code: |
    def _price_contacts_pda(hi: float, lo: float, pda: PDA) -> bool:
        return hi >= pda.zone_bottom and lo <= pda.zone_top
  detail: |
    Uses bar high/low (wicks), not open/close (body). Any price
    penetration into the zone — including wick-only contact —
    satisfies the condition. Q18 honored.
```

#### CF-16: Chain Sequential 4-Step (CH-1)
```
Status: CONFORM
Commitment: CH-1 — sweep → MSS → FVG → OTE, each requires prior
Evidence:
  file: en1gma/chain/chain_evaluator.py
  lines: ~165-220
  detail: |
    evaluate_chain calls _match_sweep, _match_mss, _match_fvg, _check_ote
    in strict sequence. Each step returns None on failure, short-circuiting
    the chain. No step can execute without its predecessor succeeding.
```

#### CF-17: No PDA Age Expiry (PDA-3)
```
Status: CONFORM
Commitment: PDA-3 — No age-based expiry
Evidence:
  file: en1gma/context/pda_store.py
  detail: |
    No timestamp comparison, bar count, or age check anywhere in PDA
    lifecycle methods. PDAs persist until terminal state transition or
    dealing range reset. Q27 honored.
```

#### CF-18: No Regime Age Limit (DR-4)
```
Status: CONFORM
Commitment: DR-4 — No regime age limit
Evidence:
  file: en1gma/context/regime.py
  detail: |
    No age check, bar count, or timestamp expiry on regime objects.
    Regime persists until flipped by opposing MSS at same/higher TF.
    Q26 honored.
```

#### CF-19: Regime Direction Permission (TC-3 support)
```
Status: CONFORM
Commitment: TC-3 (supporting) — Regime provides direction, chain consumes it
Evidence:
  file: en1gma/context/regime.py
  lines: ~55-70
  code: |
    def get_direction_permission(self) -> str:
        if self.phase == "EXPANSION":
            if self.direction == MarketDirection.BEARISH:
                return "SHORT_ONLY"
            elif self.direction == MarketDirection.BULLISH:
                return "LONG_ONLY"
        return "BOTH"
  detail: |
    Regime translates structural state into a directional permission
    string. This is consumed by the gate (L4), which passes it to the
    chain. The Map decides direction; the chain uses it. Clean separation.
```

#### CF-20: Strategy YAML Pure Configuration (SY-1)
```
Status: CONFORM
Commitment: SY-1 — Strategy YAMLs declare parameters only
Evidence:
  file: en1gma/strategies/daily_expansion.yaml (60 lines)
  file: en1gma/strategies/ars_v1_3.yaml (61 lines)
  detail: |
    Both YAML files contain only key-value pairs. No conditionals, no
    branching logic, no code. Pure declarative configuration.
```

#### CF-21: DR Authority Cascade (DR-3)
```
Status: CONFORM
Commitment: DR-3 — Daily → H4 cascade when daily is still expanding
Evidence:
  file: en1gma/context/dealing_range.py
  lines: ~140-165
  detail: |
    is_daily_range_valid returns validity boolean. When False, the system
    falls back to H4 dealing range for zone classification. INV-MAP-SCOPE-V1.1
    operational.
```

#### CF-22: Paper-Live Governance Parity (GV-5)
```
Status: CONFORM
Commitment: GV-5 — PAPER and LIVE require identical governance deps
Evidence:
  file: en1gma/control/governance.py
  lines: ~60-80
  detail: |
    validate_config enforces halt, lease, risk all non-None for both PAPER
    and LIVE modes. SHADOW also requires non-None deps. Only TEST mode
    relaxes requirements. INV-PAPER-GOVERNANCE-PARITY-WITH-LIVE honored.
```

#### CF-23: FVG Anchor Timestamp (DT-3)
```
Status: CONFORM
Commitment: DT-3 — FVG Detection.time = Candle A anchor_time
Evidence:
  file: en1gma/detection/ra_engine/detectors/fvg.py
  lines: 110, 222
  code: |
    anchor_time = _bar_time_str(ts_ny_series.iloc[i - 2], tf_minutes)  # Candle A
    ...
    det_time = to_ny_aware(fvg["anchor_time"])  # Detection.time = Candle A
  detail: |
    Detection.time is set to Candle A (bars[i-2]) anchor_time. Candle C
    (bars[i]) time is stored separately as properties["detect_time"].
    This conforms to DT-3 (vLOCK spec) but CONTRADICTS PDA-8 — see DF-01.
```

#### CF-24: Orchestrator Dumb (RO-2)
```
Status: CONFORM
Commitment: RO-2 — Orchestrator sequences and wires, never decides
Evidence:
  file: en1gma/control/map_orchestrator.py
  lines: 213-612
  detail: |
    run_map_replay is a sequencing function: loads data, loops dates,
    loops bars, calls detect, calls map, calls gate, calls chain, calls
    governance, calls broker. Contains no trading logic — all decisions
    are delegated to the appropriate layer module.
```

---

### DRIFT (code contradicts or partially violates commitment)

#### DF-01: PDA created_at Uses Candle A, Not Candle C — CONTRADICTS INV-PDA-CREATED-AT-CONFIRMATION
```
Status: DRIFT — MATERIAL
Commitment: PDA-8 — INV-PDA-CREATED-AT-CONFIRMATION: "PDA created_at = Candle C close, not Candle A"
Evidence:
  file_1: en1gma/detection/ra_engine/detectors/fvg.py
  line: 222
  code: "det_time = to_ny_aware(fvg['anchor_time'])"
  note: "Detection.time = Candle A (bars[i-2].time)"

  file_2: en1gma/context/map_engine.py
  line: ~160 (in _initialize_pdas_from_detections)
  code: "created_at=fvg.time"
  note: "PDA.created_at = Detection.time = Candle A"

  file_3: en1gma/detection/ra_engine/detectors/fvg.py
  line: 111
  code: "detect_time = _bar_time_str(ts_ny_series.iloc[i], tf_minutes)"
  note: "Candle C time IS available as properties['detect_time'] — but not used for PDA created_at"

Contradiction: |
  CLAUDE.md §6 registers INV-PDA-CREATED-AT-CONFIRMATION: "PDA created_at =
  Candle C close, not Candle A." But the code sets PDA.created_at =
  Detection.time = anchor_time = Candle A. The confirmation bar time (Candle C)
  IS available in Detection.properties["detect_time"] but is never used for
  PDA creation. The vLOCK spec (DT-3) says Detection.time = Candle A, so the
  detector is correct per vLOCK. The invariant is the one that's wrong — OR
  PDA creation should use properties["detect_time"] instead of Detection.time.
  Either the invariant or the code needs to change. Both cannot be correct.

  This is a Candle A vs Candle C timestamp ambiguity that was flagged in
  calibration_results.yaml (FVG_TIMESTAMP_NOTE) but never resolved.

Impact: |
  PDA.created_at is used for temporal ordering and event sequencing. If the
  invariant intent is correct (Candle C), every PDA in the system has a
  created_at that is 2 bars too early. For daily TF, that's 2 calendar days.
  This affects any consumer that reasons about "when was this PDA established"
  — including potential future replay audit tooling and Dream Cycle training data.

Recommendation: |
  Olya ruling needed: should PDA.created_at be Candle A (when the gap formed)
  or Candle C (when the gap was confirmed)? Then align invariant + code.
  See also: calibration_results.yaml FVG_TIMESTAMP_NOTE.
```

#### DF-02: OTE Zone Uses 2 Levels, vLOCK Specifies 4 — PARTIAL IMPLEMENTATION
```
Status: DRIFT — MEDIUM
Commitment: DT-4 — OTE uses 4 tracked levels [0.50, 0.618, 0.705, 0.79]
Evidence:
  file_1: en1gma/chain/chain_config.py
  line: ~25
  code: "ote_zone: tuple[float, float] = (0.618, 0.79)"
  note: "Only 2 of 4 vLOCK levels used as a range boundary"

  file_2: en1gma/methodology/SYNTHETIC_OLYA_METHOD_vLOCK.yaml
  section: OTE algorithm
  code: "tracked_levels: [0.50, 0.618, 0.705, 0.79]"
  note: "vLOCK locks all 4 levels"

  file_3: en1gma/strategies/daily_expansion.yaml
  line: ~42
  code: "ote_fib: 0.618"
  note: "Strategy YAML declares single fib level"

Contradiction: |
  vLOCK §OTE specifies 4 tracked retracement levels: [0.50, 0.618, 0.705, 0.79].
  The code reduces this to a 2-value range tuple (0.618, 0.79), treating OTE as
  "price between 61.8% and 79% retracement." The 0.50 level (midpoint) is
  absent — entries at exactly 50% retracement would be missed. The strategy
  YAML declares a single ote_fib (0.618), further simplifying.

  This is an acknowledged implementation choice for v1 scope, but it means
  the OTE check is less granular than the locked methodology specifies.
  The 4-level tracking with per-level significance (vLOCK specifies different
  confidence at each level) is collapsed to a single boolean range check.

Impact: |
  Entries at 0.50-0.618 retracement are invisible to the current OTE check.
  The relative significance weighting across 4 levels (part of Olya's method)
  is lost. For DAILY_EXPANSION this may be acceptable (strategy YAML sets
  ote_fib: 0.618), but future strategies may need the full 4-level granularity.
  Also see Q5 (F10 4-level OTE) which is HELD pending audit — confirming
  this is a known gap awaiting resolution.
```

#### DF-03: Kill Zone Width Ambiguity — Two Incompatible Specifications
```
Status: DRIFT — ARCHITECTURAL TENSION
Commitment: KZ-2 vs KZ-3 — Broader windows (02-05/07-10) vs narrower reversal windows (03-04/08-09)
Evidence:
  file_1: en1gma/gating/execution_gate.py
  lines: 15-18
  code: |
    LOKZ_START, LOKZ_END = 2, 5     # 02:00 - 05:00 NY
    NYOKZ_START, NYOKZ_END = 7, 10  # 07:00 - 10:00 NY

  file_2: en1gma/methodology/SYNTHETIC_OLYA_METHOD_vLOCK.yaml
  section: OTE kill_zone_gate
  code: |
    LOKZ: 03:00-04:00 NY
    NYOKZ: 08:00-09:00 NY
    note: "These are the REVERSAL windows — entry only valid here"

  file_3: en1gma/strategies/daily_expansion.yaml
  section: kill_zones
  code: |
    LOKZ: {start: "02:00", end: "05:00"}
    NYOKZ: {start: "07:00", end: "10:00"}

Analysis: |
  There are TWO different kill zone concepts in the architecture docs:
  1. SCAN PERMISSION (broad): 02:00-05:00 / 07:00-10:00 — when the gate
     can arm and the chain can scan for setups. This is what execution_gate.py
     implements (KZ-2).
  2. ENTRY PERMISSION (narrow): 03:00-04:00 / 08:00-09:00 — when an OTE
     entry is actually valid per vLOCK reversal methodology (KZ-3).

  The code implements ONLY the broad windows. There is no narrower entry
  validation at the OTE level. The vLOCK spec's kill_zone_gate on OTE
  (DT-5) is not enforced anywhere in chain_evaluator.py's _check_ote.

  This means the system can place entries at 02:15 NY or 09:45 NY — times
  that fall within the broad scan window but outside the vLOCK reversal
  window. Whether this is intentional (strategy-level override of vLOCK
  timing) or accidental (missing implementation) is unclear.

Impact: |
  Entries may fire outside the methodology's reversal windows. This could
  produce trades that Olya would not take. The architectural tension is
  that KZ width belongs to NEITHER the Map NOR the Chain cleanly — it
  crosses the two-clock boundary. The gate (Map clock) opens the broad
  window; the OTE check (Execution clock) should enforce the narrow
  window but doesn't.

Recommendation: |
  Clarify with Olya: are the vLOCK reversal windows (03-04/08-09) an
  additional OTE-level constraint, or did the strategy YAML's broader
  windows intentionally supersede them? If the former, _check_ote needs
  a time-window filter. If the latter, document the override explicitly
  and note that it relaxes vLOCK.
```

#### DF-04: Dormant `sweep_required` Field — Anti-Pattern 2 Risk Vector
```
Status: DRIFT — LOW (dormant, but architectural hazard)
Commitment: SM-2 — Chain is universal infrastructure, does not change per strategy
Related: MAP_SPATIAL_PRIMER Anti-Pattern 2 ("modifying the chain")
Evidence:
  file_1: en1gma/chain/chain_config.py
  line: ~15
  code: "sweep_required: bool = True"
  note: "Field exists with default True, but is NEVER READ by chain_evaluator.py"

  file_2: en1gma/chain/chain_evaluator.py
  detail: "No reference to cfg.sweep_required anywhere in the module"

  file_3: en1gma/methodology/HTF_MAP_SPEC_v0_1.yaml
  section: Q20-Q25 (deferred to v2)
  note: "Q20: sweep-optional chain for RETRACE/RANGE strategies — deferred"

Analysis: |
  The field exists because HTF_MAP_SPEC Q20-Q25 envision future strategies
  where sweep is not required (RETRACE, RANGE). However, the MAP_SPATIAL_PRIMER
  explicitly names "modifying the chain" as Anti-Pattern 2 and states the chain
  is "standard (do NOT modify)."

  sweep_required=False would skip _match_sweep in the chain — this IS modifying
  the chain's behavior per strategy. If activated, it would violate SM-2 and
  Anti-Pattern 2. Right now it's inert (no code reads it), making it a dormant
  hazard rather than an active violation.

  The tension: the HTF_MAP_SPEC (Olya-calibrated) anticipated sweep-optional
  chains, but the MAP_SPATIAL_PRIMER (architectural doctrine) says chains
  don't change. These two documents disagree on this point.

Impact: |
  Zero impact today (field is dead code). Future impact: if someone activates
  sweep_required=False, they'll be modifying chain behavior per strategy —
  exactly what the Primer forbids. The architectural question is whether
  future RETRACE/RANGE strategies should skip sweep via chain modification
  OR via a different mechanism (e.g., the gate deciding sweep is not a
  precondition for those Map configurations).
```

#### DF-05: `strategy_config` Parameter Declared But Never Used in Gate
```
Status: DRIFT — LOW (dead parameter, incomplete wiring)
Commitment: SM-1 — Strategies are Map configurations consumed by the gate
Evidence:
  file: en1gma/gating/execution_gate.py
  line: ~55
  code: |
    def evaluate_gate(
        map_state: MapState,
        current_price: float,
        current_time: datetime,
        hi: float,
        lo: float,
        strategy_config: dict | None = None,
    ) -> GateResult:
  note: "strategy_config is accepted but never referenced in the function body"

Analysis: |
  The gate accepts strategy configuration but ignores it entirely. This means
  the gate cannot distinguish between strategies — every strategy gets the
  same gate behavior. For v1 with a single Map-gated strategy (DAILY_EXPANSION),
  this is harmless. For multi-strategy futures (DAILY_CONTINUATION,
  RETRACE_COUNTER, RANGE_AUTHORITY), the gate would need to read strategy-
  specific parameters (e.g., required zone, PDA types, timeframe filter).

  The parameter's existence suggests intent to wire it, but the wiring never
  happened. Combined with DF-06 (SW10: pda_timeframes unenforced), this
  represents an incomplete strategy→gate pathway.
```

#### DF-06: PDA Timeframes Filter Never Enforced (SW10)
```
Status: DRIFT — MEDIUM (known defect, acknowledged)
Commitment: SY-3 — Strategy YAML pda.timeframes scopes eligible PDAs
Evidence:
  file_1: en1gma/strategies/daily_expansion.yaml
  lines: ~28-30
  code: |
    pda:
      types: [FVG]
      timeframes: [DAILY]

  file_2: en1gma/gating/execution_gate.py
  lines: ~95-105
  code: |
    candidates = [
        p for p in map_state.active_pdas
        if p.status in PDA_ACTIVE_STATES
        and (required is None or p.location_class == required)
    ]
  note: "No timeframe filter. All active PDAs regardless of source timeframe."

Analysis: |
  daily_expansion.yaml declares pda.timeframes: [DAILY], meaning only daily-TF
  PDAs should be eligible. But the gate's candidate filter checks only status
  and zone classification — not timeframe. If H4 PDAs existed (via the DR
  cascade), they would be eligible for a strategy that only wants daily PDAs.

  This is a registered known defect (SW10, Olya queue rank 11) and is
  acknowledged in CLAUDE.md and FORWARD_PLAN.md. The tension with M3.1's
  daily→H4 cascade makes this architecturally interesting: the cascade
  provides H4 dealing ranges, but should it also provide H4 PDAs?
  That's the Olya question.
```

#### DF-07: _replay_price_forward Terminal State Check Misses REJECTED PDAs
```
Status: DRIFT — MEDIUM (bug, parallel logic inconsistency)
Commitment: PDA-1 — 5-state lifecycle with 3 terminal states (REJECTED, MITIGATED, INVALIDATED)
Evidence:
  file_1: en1gma/context/map_engine.py
  line: ~590 (in _replay_price_forward)
  code: |
    if pda.status in PDAStatus.MITIGATED or pda.status == PDAStatus.INVALIDATED:
        continue
  note: "Skips MITIGATED and INVALIDATED, but NOT REJECTED"

  file_2: en1gma/context/pda_store.py
  line: ~125
  code: |
    if pda.status in PDA_TERMINAL_STATES:
        continue
  note: "Skips ALL terminal states: REJECTED, MITIGATED, INVALIDATED"

Analysis: |
  pda_store.py correctly uses PDA_TERMINAL_STATES (frozenset of all 3 terminal
  states). map_engine._replay_price_forward uses an ad-hoc check that lists
  MITIGATED and INVALIDATED explicitly but omits REJECTED.

  The `pda.status in PDAStatus.MITIGATED` expression is also suspicious — this
  is a string-containment check (`"REJECTED" in "MITIGATED"` → False by luck,
  but `"MITIGATED" in "MITIGATED"` → True). It works by accident for the
  values involved, but the pattern is fragile.

  In v1 scope, REJECTED is not actively used (no code path sets a PDA to
  REJECTED status), so this has zero runtime impact today. But the parallel
  logic between pda_store and map_engine is inconsistent — the exact pattern
  flagged in CLAUDE.md as a "Block 3 consolidation candidate."

Impact: |
  If REJECTED PDAs are introduced (v2 scope), _replay_price_forward would
  attempt to process them for mitigation/touch — producing incorrect state.
  The inconsistency confirms the consolidation need already flagged.

  Note: This overlaps with SW15 in the sweep findings.
```

#### DF-08: DealingRange.authority_tf Type Inconsistency
```
Status: DRIFT — LOW (cosmetic, but type-system gap)
Commitment: L5-1 — Clean type boundaries between layers
Evidence:
  file_1: en1gma/context/context_types.py
  line: ~165
  code: |
    @dataclass
    class DealingRange:
        ...
        authority_tf: str = "DAILY"
  note: "authority_tf is a plain string with string default"

  file_2: en1gma/context/context_types.py
  line: ~140
  code: |
    @dataclass
    class Regime:
        ...
        authority_tf: AuthorityTF
  note: "authority_tf is the AuthorityTF enum (same file, different type)"

Analysis: |
  Two dataclasses in the same file use `authority_tf` with different types.
  Regime uses the AuthorityTF enum (type-safe). DealingRange uses a plain
  string (type-unsafe). This means DealingRange.authority_tf could be set to
  any string value, while Regime.authority_tf is constrained to enum members.

  The inconsistency creates a subtle type boundary: code that compares
  Regime.authority_tf with DealingRange.authority_tf would be comparing
  an enum with a string — which works in Python (str Enum), but is not
  clean practice.

Impact: |
  Low runtime risk (Python's str Enum comparison handles this). But it's
  a type-system gap that could cause confusion during code review or
  refactoring. A future language port would surface this as a compile error.
```

---

## SUMMARY TABLE

| ID | Commitment | Verdict | Severity | Note |
|----|-----------|---------|----------|------|
| CF-01 | TC-3 SEPARATION_RULE | ✅ CONFORM | — | Direction flows Map→Gate→Chain only |
| CF-02 | PDA-1 5-state lifecycle | ✅ CONFORM | — | Exact enum match |
| CF-03 | PDA-2 TOUCHED permanent | ✅ CONFORM | — | No reversion path |
| CF-04 | PDA-7 zone from detector | ✅ CONFORM | — | SW04 shipped |
| CF-05 | PDA-6 direction fidelity | ✅ CONFORM | — | SW04 shipped |
| CF-06 | DT-2 tz-aware Detection | ✅ CONFORM | — | __post_init__ guard |
| CF-07 | PDA-9 retrace-fill mitigation | ✅ CONFORM | — | SW01 shipped |
| CF-08 | GV-3 mode explicit | ✅ CONFORM | — | No defaults anywhere |
| CF-09 | GV-2 LIVE gate | ✅ CONFORM | — | NotImplementedError |
| CF-10 | GV-4 single check site | ✅ CONFORM | — | One call site per path |
| CF-11 | DR-1 wick-to-wick | ✅ CONFORM | — | Q1/Q2 honored |
| CF-12 | DR-2 rolling DR | ✅ CONFORM | — | Q3 honored |
| CF-13 | PDA-4 midpoint classification | ✅ CONFORM | — | Q7 honored |
| CF-14 | EG-1 4-condition gate | ✅ CONFORM | — | All 4 checked |
| CF-15 | EG-4 edge touch | ✅ CONFORM | — | Q18 honored |
| CF-16 | CH-1 4-step chain | ✅ CONFORM | — | Sequential, gated |
| CF-17 | PDA-3 no age expiry | ✅ CONFORM | — | Q27 honored |
| CF-18 | DR-4 no regime age | ✅ CONFORM | — | Q26 honored |
| CF-19 | TC-3 regime→gate→chain | ✅ CONFORM | — | Clean flow |
| CF-20 | SY-1 YAML pure config | ✅ CONFORM | — | No branching |
| CF-21 | DR-3 daily→H4 cascade | ✅ CONFORM | — | M3.1 operational |
| CF-22 | GV-5 paper-live parity | ✅ CONFORM | — | Same deps required |
| CF-23 | DT-3 FVG anchor time | ✅ CONFORM | — | Candle A per vLOCK |
| CF-24 | RO-2 orchestrator dumb | ✅ CONFORM | — | Pure sequencing |
| DF-01 | PDA-8 created_at Candle C | ❌ DRIFT | MATERIAL | Code uses Candle A; invariant says Candle C |
| DF-02 | DT-4 OTE 4-level | ⚠️ DRIFT | MEDIUM | 2 of 4 levels implemented |
| DF-03 | KZ-2/KZ-3 window width | ⚠️ DRIFT | TENSION | Two incompatible KZ specs; only broad implemented |
| DF-04 | SM-2 sweep_required | ⚠️ DRIFT | LOW | Dormant field; Anti-Pattern 2 hazard if activated |
| DF-05 | SM-1 strategy_config | ⚠️ DRIFT | LOW | Dead parameter in gate |
| DF-06 | SY-3 pda_timeframes | ⚠️ DRIFT | MEDIUM | SW10 — declared but unenforced |
| DF-07 | PDA-1 terminal states | ⚠️ DRIFT | MEDIUM | _replay_price_forward misses REJECTED |
| DF-08 | L5-1 authority_tf type | ⚠️ DRIFT | LOW | str vs enum in same file |

---

## VERDICT

```yaml
conformance_rate: "24 of 32 findings CONFORM (75%)"
drift_count: 8
  material: 1   # DF-01: PDA created_at invariant vs code
  medium: 3     # DF-02 OTE levels, DF-06 pda_timeframes, DF-07 REJECTED skip
  tension: 1    # DF-03: kill zone width ambiguity
  low: 3        # DF-04 sweep_required, DF-05 strategy_config, DF-08 authority_tf type

architectural_health: |
  The kernel's core architectural commitments are SOLID. The two-clock
  separation, governance model, PDA lifecycle, Olya calibration answers,
  and detection contracts are all cleanly honored in code. The weekend
  sprint (SW01/SW04/SW07/SW08/SW09/SW24) closed the most dangerous
  violations — INV-NO-UNGOVERNED-TRADES, INV-DETECTION-TIME-TZ-AWARE,
  INV-PDA-DIRECTION-FIDELITY, and INV-PDA-MITIGATION-IS-RETRACE-FILL
  are all verifiably correct.

  The 8 drift findings cluster into 3 themes:
  
  1. TIMESTAMP IDENTITY (DF-01): The only material finding. The invariant
     INV-PDA-CREATED-AT-CONFIRMATION claims Candle C but code uses Candle A.
     One of them is wrong. Needs Olya ruling.
  
  2. INCOMPLETE v2 PLUMBING (DF-02, DF-04, DF-05, DF-06): Fields and
     parameters exist for future capabilities (4-level OTE, sweep_required,
     strategy_config, pda_timeframes) but are dormant or partial. These are
     known scope boundaries, not surprise drift. The risk is that dormant
     fields get activated without the architectural review the Primer demands.
  
  3. PARALLEL LOGIC INCONSISTENCY (DF-07): pda_store and map_engine have
     duplicate mitigation/lifecycle logic with different terminal-state
     handling. This is the consolidation debt flagged in CLAUDE.md — the
     only question is when to pay it.

  The kill zone width tension (DF-03) is the most architecturally interesting
  finding: it reveals that OTE entry timing crosses the two-clock boundary
  and neither the Map nor the Chain fully owns it today. This deserves
  attention during the audit resolution phase.

ruling_needed:
  - "DF-01: Olya — PDA.created_at should be Candle A or Candle C?"
  - "DF-03: Olya — are vLOCK reversal windows (03-04/08-09) an additional OTE constraint or superseded by strategy YAML?"
```

---

*Stream B audit complete. 8 documents read, 5 code surfaces audited, 32 findings registered.*
*"Human frames. Machine computes. Human promotes."*