# HTF Map Spec v0.11 Gap Analysis

```yaml
review_id: HTF_MAP_SPEC_v0_11_GAP_ANALYSIS_2026_04_28
mission_id: POST_4B.H6.HTF_MAP_SPEC_v0_11_GAP_ANALYSIS
classification: READ_ONLY_METHODOLOGY_INTAKE | CONSOLE_GAP_ANALYSIS
scope: console_map
behavior_change: none
baseline_commit: 063cb6a
review_date: 2026-04-28
authoritative_source: docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md
authoritative_spec: htf_map_spec_v0_11
supersedes: htf_map_spec_v0_1
runtime_changes: NONE
schema_changes: NONE
cartridge_changes: NONE
strategy_performance_judgment: NONE
final_verdict: CURRENT_MAP_PARTIAL_V0_11_ALIGNMENT_REQUIRES_CONSOLE_WORK
```

---

## 1. Executive verdict

The current certified Map is **not v0.11-complete**. It has a usable Daily-direction / dealing-range / midpoint / PDA foundation, but v0.11 adds an interpreted Daily Map read-model that the current `MapState` does not expose: quadrants, external/internal liquidity classification, dominant draw, available targets, target completion, proximity-to-target, and the new market-state vocabulary.

Two architectural mismatches dominate the gap:

1. **H4 is currently embedded in core Map behavior** through the loader invariant, daily-to-H4 dealing-range cascade, structural event ingestion, day-state eligibility, and PDA construction; v0.11 says H4 is `strategy_specific_only` and `not_used_in_map`.
2. **Premium/discount location currently gates trade permission**, while v0.11 says PD zone and quadrant outputs are location labels only and strategies decide behavior.

No build decision is made here. This is a read-only intake and gap map.

---

## 2. Source and current-support surfaces

```yaml
source_spec:
  path: docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md
  relevant_lines:
    direction: 16-22
    dealing_range: 24-35
    pd_zones_and_quadrants: 37-52
    liquidity: 54-77
    targets_and_draw: 79-106
    target_completion_and_proximity: 108-123
    market_state: 125-149
    htf_layers: 151-170
    map_output: 172-184

current_code_surfaces:
  map_types: en1gma/console/map/context_types.py:30-89,162-284
  map_engine_init: en1gma/console/map/map_engine.py:226-309
  regime_init: en1gma/console/map/map_engine.py:311-369
  dealing_range: en1gma/console/map/dealing_range.py:1-160
  dealing_range_engine: en1gma/console/map/map_engine.py:906-1164
  pda_store: en1gma/console/map/pda_store.py:1-210
  gate: en1gma/console/chain/gate.py:49-189
  h4_loader_invariant: en1gma/cartridges/loader.py:60-69,406-423
  production_cartridge_htf: en1gma/cartridges/daily_expansion.yaml:39-41
  map_state_emit: en1gma/console/map/map_engine.py:1297-1310
```

---

## 3. Specific questions answered

| Question | Answer | Current support | Gap classification | Evidence |
|---|---|---|---|---|
| Does current direction require both Daily MSS and Daily displacement? | **Partial.** Current OK path establishes regime from `1D` MSS. The MSS detector is displacement-backed upstream, but Map itself does not explicitly require and bind a Daily MSS + Daily displacement pair. If no Daily MSS exists, Map can still derive a displacement-only fallback regime, then marks `construction_mode=FALLBACK`; gate refuses it. | Partial/fail-closed | `CONSOLE_GAP` for explicit paired evidence; fallback is safely blocked | `map_engine.py:311-369`, `gate.py:120-125` |
| Can current Map persist direction until opposing Daily MSS while separately entering reassessment after target completion? | **No.** Regime direction persists in spirit, but there is no target object and no reassessment state. Current phase is `EXPANSION/RETRACE/RANGE`; direction permission is coupled to phase and zone gating. | Partial direction persistence; no reassessment | `SCHEMA_GAP` + `CONSOLE_GAP` + `METHODOLOGY_RESIDUAL` | `context_types.py:30-33,162-169`, `regime.py:36-58`, `gate.py:127-146` |
| Does current Map define range start as `swing_that_created_daily_mss` and end as `displacement_extreme`? | **Partial.** End is displacement/extreme-wick based. Start is currently pullback-origin / highest-liquidity point before displacement, not an explicit MSS-creating swing identity. | Partial | `CONSOLE_GAP` + `METHODOLOGY_RESIDUAL` | `dealing_range.py:1-9,28-51`, `map_engine.py:958-1098` |
| Does current Map expose quadrant labels? | **No.** It exposes only `PREMIUM/DISCOUNT/NEUTRAL`. | Gap | `SCHEMA_GAP` + `CONSOLE_GAP` | `context_types.py:63-66`, `pda_store.py:35-58` |
| Does current Map classify external vs internal liquidity? | **No in Map.** Detector-side liquidity substrates exist, but `RestingLiquidity` is stub/narrow and `MapState` does not expose v0.11 liquidity classes. | Detector substrate only | `SCHEMA_GAP` + `CONSOLE_GAP` | `liquidity.py:1-39`, `context_types.py:74-89,258-284`, `htf_liquidity.py:426-431`, `liquidity_sweep.py:4-7` |
| Can current Map emit `dominant_draw_target`? | **No.** | Gap | `SCHEMA_GAP` + `CONSOLE_GAP` | `context_types.py:271-284`, `map_engine.py:1297-1310` |
| Can current Map emit `available_targets`? | **No.** Reference/HTF liquidity detectors can produce some raw ingredients, but Map emits none. | Detector substrate only | `SCHEMA_GAP` + `CONSOLE_GAP` | `reference_levels.py:1-8`, `liquidity_sweep.py:208-464`, `map_engine.py:1297-1310` |
| Can current Map track `target_completion_status` by wick touch? | **No.** PDA touch exists, not target-object completion. | PDA analog only | `SCHEMA_GAP` + `CONSOLE_GAP` | `pda_store.py:68-118`, `context_types.py:271-284` |
| Can current Map compute `proximity_to_target` at 75-100% of dealing range? | **No.** Current proximity is PDA candidate sorting/contact, not DR progress toward external target. | Gap | `SCHEMA_GAP` + `CONSOLE_GAP` | `pda_store.py:193-210`, `gate.py:156-165` |
| Can current Map output `market_state = pullback | expansion | approaching_target | reassessment`? | **No.** Current `MarketPhase` is `EXPANSION/RETRACE/RANGE`; day-state is separate PRE/POST expansion and not equivalent. | Partial vocabulary overlap | `SCHEMA_GAP` + `CONSOLE_GAP` | `context_types.py:30-33`, `day_state.py:31-46` |
| Can range update trigger on `continuation_displacement_after_pullback`? | **Not as an active live path.** `DealingRangeTracker.create_range()` can supersede ranges, and initialization can choose a current displacement, but bar processors only update PDA lifecycle. | Latent helper only | `CONSOLE_GAP` + `METHODOLOGY_RESIDUAL` | `dealing_range.py:28-51`, `map_engine.py:1231-1284` |
| Does current system keep H4 out of core Map while allowing strategy-specific H4 confirmation? | **No.** H4 is required by the loader for Map-required cartridges and participates in DR cascade, structural events, day-state, and PDA creation. There is no clean strategy-specific H4 confirmation surface. | Not aligned | `CONSOLE_GAP` + architecture risk | `loader.py:60-69,406-423`, `map_engine.py:290-298,371-390,1100-1164,1190-1195`, `day_state.py:36-46,182-216`, `daily_expansion.yaml:39-41` |

---

## 4. Per-spec-element table

| v0.11 element | Spec requirement | Current support | Partial support | Schema gap | Console gap | Methodology residual | Cost/risk | High-level sequence |
|---|---|---|---|---|---|---|---|---|
| Core principle | Map outputs interpreted Daily context: direction, DR, location, liquidity targets, dominant draw, market state | Direction/DR/PDA foundation exists | PDA and midpoint context are present, not full interpreted output | Missing target/state/location read-model fields | Need target/liquidity/state computation | None beyond listed residuals | `HIGH` | Define v0.11 MapState read model after residual closure |
| Direction rule | Daily MSS + Daily displacement required | Daily MSS is primary regime source | MSS detector is displacement-backed; Map does not bind pair explicitly; displacement-only fallback exists fail-closed | No paired-evidence field | Need explicit Daily MSS+displacement evidence assertion | Define accepted displacement quality, if not detector default | `MEDIUM` | Pair regime evidence and preserve fallback refusal |
| Direction persistence | Direction remains until opposing Daily MSS | Regime persists until reverse MSS | Current mutator is TF-rank based, not explicitly Daily-only; no reassessment split | Missing direction-vs-trade-bias split | Need target-completion reassessment without erasing direction | Required residual: persistence vs no-trade-bias | `HIGH` | Separate `direction` from `market_state`/trade-bias consumers |
| Dealing range start/end | Start `swing_that_created_daily_mss`, end `displacement_extreme`, wick-to-wick | Wick-to-wick and displacement extreme mostly supported | Start is pullback-origin/highest-liquidity before displacement | Missing explicit source swing identity | Need DR builder tied to MSS swing identity | Which swing exactly created MSS? | `MEDIUM` | Resolve swing identity, then re-anchor DR creation |
| DR lifecycle bias reset | Opposing Daily MSS resets bias | Opposing MSS can reverse regime | Not daily-only in generic tracker; no target completion interaction | None | Need daily-only authority semantics | Interaction with reassessment | `MEDIUM` | Daily authority model first |
| DR lifecycle range update | Continuation displacement after pullback updates range | Tracker can supersede ranges | No live update path for continuation displacement after pullback | No event/provenance field for update trigger | Need runtime detection/processing path | Required residual: machine definition | `HIGH` | Define trigger, wire daily structural update, trace provenance |
| No time reset | No time-based reset | Mostly aligned | Existing initialization windows may still limit discovery but no explicit age expiry | None | Audit warm-state persistence separately | None | `LOW` | Preserve invariant in implementation design |
| Midpoint | `(high + low) / 2` | Supported via `DealingRange.equilibrium` | None | None | None | None | `LOW` | Reuse equilibrium |
| Quadrants | Four quarter-range labels | Not supported | None | Add quadrant enum/field(s) | Need classify current price/PDA/location to quadrants | Direction-neutral naming conventions | `MEDIUM` | Add label-only quadrant output after read-model design |
| PD zone usage | Location label only; no trade permission logic | Current gate uses PD zone as permission filter | Label exists as `PREMIUM/DISCOUNT/NEUTRAL` | Need label fields distinct from gate rules | Remove/relocate permission semantics into strategy-specific cartridge gate | Whether existing Daily Expansion parity must retain old gating behind strategy behavior | `HIGH` | Strategy-behavior preservation plan before changing gate consumption |
| External liquidity | Primary HTF targets/dominant draw: PDH/PDL/PWH/PWL/unswept daily-weekly/monthly | Detector ingredients exist | Map liquidity is stub and narrow | Add liquidity target objects/classes | Need assemble unswept external targets in Map | Exact `available_targets` membership | `HIGH` | Map target object model, detector ingestion, completion tracking |
| Internal liquidity | H1 equal highs/lows, session highs/lows, pre-LOKZ, pre-NY | Execution detectors have session/sweep substrates | Not Map-classified as internal liquidity | Add internal liquidity class/output | Need classify and expose, but not primary draw | H1 narrative/non-gating boundary | `MEDIUM` | Surface as context-only after external target work |
| Target outputs | PDH/PDL/PWH/PWL/unswept daily/weekly swings | Reference detectors and liquidity sweep use some raw levels | Map emits none | Add `available_targets` | Need canonical unswept-target assembly | Available-target eligibility | `HIGH` | Build read-only target list before strategy target selection |
| Draw on liquidity | Highest timeframe available objective; distance does not override TF; output `dominant_draw_target` | Not supported | None | Add dominant draw field | Need monthly/weekly/daily priority selection | Monthly-level presence rules | `MEDIUM/HIGH` | Implement selection after target object model |
| Target completion | Wick touch = achieved; stop trading into level; enter reassessment | PDA touch analog exists | No target object or active draw status | Add completion status | Need wick-touch tracking against dominant/available targets | Completion of intermediate vs dominant target | `HIGH` | Completion engine before reassessment behavior |
| Proximity | 75-100% of DR near-target zone, context flag only | Not supported | PDA proximity sorting is unrelated | Add proximity field | Need DR-progress-to-target calculation | Denominator and directional calculation details | `MEDIUM` | Add once target and DR endpoints are explicit |
| Market state | `pullback`, `expansion`, `approaching_target`, `reassessment` | Current `EXPANSION/RETRACE/RANGE`; separate DayState PRE/POST | `RETRACE` resembles pullback but semantics differ | Add v0.11 market-state enum/field | Need range-position and target-state logic | Required residuals for reassessment exit | `HIGH` | Model state after target/proximity/completion surfaces exist |
| Weekly layer | Targets only, not direction | Weekly/PWH/PWL detector ingredients exist | Not Map output | Target fields missing | Need weekly targets in Map | Weekly unswept swing identity | `MEDIUM` | Fold into external target assembly |
| Daily layer | Primary direction, DR, PD zones, state | Direction/DR/PD midpoint supported | State and target/proximity missing | Add state/read-model fields | Rework lifecycle | Residuals above | `HIGH` | Daily-first Map v0.11 core |
| H4 layer | Strategy-specific only; not used in Map | Not aligned | H4 is core today | Need no core H4 Map fields after redesign | Retire/move loader invariant and cascade behavior | Whether to retire vs sidecar current cascade | `HIGH` | Settle authority model before code work |
| H1 layer | Narrative confirmation, not trade gating | Not core Map today | Some execution detectors use H1/session liquidity | No narrative output | Strategy-specific consumers only | Define if MEM consumes H1 narrative | `MEDIUM` | Keep out of core Map unless Olya defines output |
| Map output shape | Includes direction, DR high/low, midpoint, quadrant, dominant draw, targets, completion, proximity, market_state | Current `MapState` emits regime, DR, PDAs, resting_liquidity stub, construction mode | Direction/DR/PDA subset | Major read-model gap | Computation gaps for missing fields | Several residuals | `HIGH` | Add explicit output contract after methodology closure |
| Old high/low definition | Structural Daily/Weekly swing, unswept; exclude intraday/arbitrary recent levels | HTF liquidity detector has structural substrates | Map does not expose or enforce as target eligibility | Add structural target metadata | Need unswept lifecycle | Exact swing strength/minor exclusion threshold | `MEDIUM` | Target object eligibility rules |
| Exclusions v1 | Exclude IPDA 20-day, minor swing detection, OB/IFVG, automatic ranking | Mostly not implemented today | No automatic ranking exists, but no target list either | None for exclusions | Ensure target work does not add excluded features | None | `LOW` | Maintain exclusion guardrails |

---

## 5. Gap count summary

```yaml
summary_counts:
  fully_supported: 2
  partial_or_latent_support: 8
  schema_gaps: 13
  console_gaps: 16
  methodology_residuals: 7
  architecture_mismatches:
    - h4_currently_core_but_v0_11_says_strategy_specific_only
    - pd_zone_currently_trade_permission_but_v0_11_says_label_only

no_runtime_decision: true
no_strategy_performance_claim: true
```

---

## 6. Likely implementation sequence — high level only

```yaml
sequence:
  step_0_methodology_closure:
    purpose: "Resolve residuals before code."
    includes:
      - direction_persists_vs_reassessment_no_trade_bias
      - continuation_displacement_after_pullback_machine_definition
      - new_structure_or_expansion_after_reassessment_definition
      - exact_swing_that_created_daily_mss_identity
      - available_targets_membership
      - h4_cascade_retire_vs_strategy_sidecar_confirmation

  step_1_authority_model_split:
    purpose: "Make core Map Daily-only per v0.11 and define H4 as strategy-specific consumer context."
    risk: HIGH

  step_2_v0_11_map_output_contract:
    purpose: "Add read-model fields for quadrants, targets, dominant draw, completion, proximity, and market_state."
    risk: HIGH

  step_3_daily_regime_and_dr_lifecycle:
    purpose: "Explicit Daily MSS+displacement pairing, DR start/end identity, continuation-displacement range update."
    risk: HIGH

  step_4_liquidity_target_engine:
    purpose: "Assemble external/internal liquidity, unswept status, wick-touch completion, dominant draw."
    risk: HIGH

  step_5_strategy_consumption:
    purpose: "Let DMB/MEM/TRM consume or ignore Map outputs without making core Map strategy-shaped."
    risk: MEDIUM_HIGH
```

---

## 7. Read-only scope statement

```yaml
files_created_by_this_review:
  - docs/reviews/HTF_MAP_SPEC_v0_11_GAP_ANALYSIS_2026_04_28.md
  - docs/reviews/HTF_MAP_v0_11_STRATEGY_FAMILY_ALIGNMENT_2026_04_28.md
  - docs/reviews/HTF_MAP_v0_11_RESIDUAL_CLARIFICATIONS_2026_04_28.md

files_intake_source:
  - docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md

forbidden_actions_observed:
  console_code_changes: false
  schema_changes: false
  cartridge_edits: false
  dmb_mem_trm_implementation: false
  h4_authority_implementation: false
  neutral_state_implementation: false
  target_ranking_implementation: false
  strategy_performance_judgment: false
```
