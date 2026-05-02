# DMB Expressibility Review — Revised Draft v0.1

```yaml
review_id: DMB_expressibility_review_2026_04_28
mission_id: POST_4B.H5.DMB_REVISED_EXPRESSIBILITY_REVIEW
classification: READ_ONLY_ANALYSIS | CARTRIDGE_EXPRESSIBILITY_REVIEW
scope: cartridge
effect: evaluation
behavior_change: none
review_date: 2026-04-28
baseline_commit: 12cddd4

candidate_id: DMB
candidate_version: "0.1"
prior_state: DRAFT
target_state: REVIEWED
candidate_status: DRAFT | OLYA_REVIEWABLE
evidence_artifact_paths:
  - docs/cartridges/drafts/STRATEGY_CARTRIDGE_DMB_REVISED_DRAFT.md
  - en1gma/cartridges/daily_expansion.yaml
  - docs/canonical/CARTRIDGE_LIFECYCLE_PROTOCOL.md
  - docs/canonical/CARTRIDGE_CONTRACT.md

production_target: en1gma/cartridges/daily_expansion.yaml
lifecycle_protocol: docs/canonical/CARTRIDGE_LIFECYCLE_PROTOCOL.md
cartridge_contract: docs/canonical/CARTRIDGE_CONTRACT.md

verdict: REQUIRES_CONSOLE_CAPABILITY_WORK
shadow_run_feasibility: blocked_by_console_gap
promotion_decision: NONE
runtime_changes: NONE
schema_changes: NONE
cartridge_replacement: NONE
```

---

## 1. Source provenance

```yaml
candidate_source:
  path: docs/cartridges/drafts/STRATEGY_CARTRIDGE_DMB_REVISED_DRAFT.md
  source: "Olya Telegram message to G, 2026-04-27"
  captured_by: Chair
  methodology_content: VERBATIM_FROM_OLYA
  lifecycle_state: DRAFT
  reviewable_status: OLYA_REVIEWABLE

production_comparison_target:
  path: en1gma/cartridges/daily_expansion.yaml
  strategy: DAILY_EXPANSION
  family: DAILY_MOMENTUM
  version: "1.0"
  note: "Prior DMB lineage / production comparison target, not immutable methodology."

preflight_worktree_inventory:
  unrelated_existing_changes:
    - "D docs/doctrine/AGENT_HABITAT.md"
    - "D docs/doctrine/BRIEF_PATTERN.md"
    - "?? docs/cartridges/"
    - "?? docs/findings/doctrine/"
  handling: "Inventory only; no staging, normalization, or reclassification in this review."
```

---

## 2. Current-vs-revised semantic diff

```yaml
current_daily_expansion:
  map_required: true
  day_state_required: PRE_EXPANSION
  regime_phase: EXPANSION
  pda: "FVG, declared DAILY; runtime currently derives Daily/H4 PDAs from HTF detection feed"
  sessions: [LOKZ, NYOKZ]
  chain: "SWEEP -> MSS -> causal FVG -> OTE"
  entry_method: OTE_LEVEL
  take_profit: FIXED_2R
  stop_loss: "sweep level plus sl_buffer_pips"
  management: "no post-entry BE management"

revised_DMB:
  model: "Daily/4H aligned HTF continuation"
  pda: "Daily FVG primary, 4H FVG fallback"
  chain: "HTF FVG touch -> session-liquidity sweep -> 15m MSS momentum -> market entry at MSS close"
  target: "nearest HTF external liquidity: PDH/PDL then PWH/PWL"
  rr_filter: "RR to nearest HTF target must be >= 1.5"
  management: "move SL to BE on new 15m structure break in trade direction"

delta_summary: |
  Revised DMB is not a parameter-only variant of current DAILY_EXPANSION.
  It removes the current LTF FVG/OTE entry dependency, adds H4 alignment,
  adds PDA priority/fallback semantics, adds source-specific sweep rules,
  adds MSS momentum thresholds, changes target selection from fixed-R to
  HTF level, and adds post-entry management.
```

---

## 3. Per-field expressibility table

| DMB_field | candidate_value | production_equivalent_or_none | current_console_surface | expressibility_verdict | gap_classification | notes |
|---|---|---|---|---|---|---|
| cartridge wrapper / identity | `strategy_cartridge_draft`, `name`, `status`, `scope`, `classification`, `core_model` | Top-level `strategy`, `family`, `version`, `map_required`; no `name/status/scope/core_model` runtime fields | `loader.py` requires top-level keys and `chain` fields (`loader.py:263-325`) | `SCHEMA_GAP` | `SCHEMA_GAP` | As submitted, the candidate is review-doc YAML, not loader-ready cartridge YAML. Lifecycle metadata is valid in review artifacts, not cartridge runtime schema. |
| `map_required` | `true` | `map_required: true` | Loader resolves Map-gated path and requires cascade HTFs (`loader.py:406-423`) | `CARTRIDGE_CONFIG_OK` | none | Config-only. |
| `htf_context.direction_requirement.daily_and_4h_aligned` | `true` | none | Map has one active `regime.direction` and `authority_tf`; H4 is used for DR cascade/structural internals, not an exposed alignment gate (`map_engine.py:233-304`) | `CONSOLE_GAP` | `CONSOLE_GAP` | H4 authority/cascade is not the same as Daily+H4 direction alignment. Needs runtime context and declarative gate surface. |
| `htf_context.pda_priority` | Daily_FVG primary, 4H_FVG fallback | `pda.types: [FVG]`, `pda.timeframes: [DAILY]` | Gate chooses contacted PDA nearest current price; PDA list is flat (`gate.py:143-165`). `pda_timeframes` is loaded but no runtime consumer was found (`loader.py:432-433`; grep only tests/loader). | `CONSOLE_GAP` | `CONSOLE_GAP` | Also lacks a YAML priority/fallback shape, but the runtime currently treats candidates flat. |
| `htf_context.pd_zone` | Daily DR wick-to-wick, midpoint required, longs discount / shorts premium | Current Map/Gate premium-discount classification | Dealing range classifies PDA location by midpoint vs equilibrium; gate requires correct zone (`dealing_range.py:77-78`; `gate.py:143-150`) | `CARTRIDGE_CONFIG_OK` | none | Matches existing Daily-authority path semantics. |
| `htf_context.pda_interaction.valid_touch` | any touch into FVG | Gate arms on wick/body contact with PDA zone | `_price_contacts_pda` via `evaluate_gate(... bar_high/bar_low ...)` (`gate.py:91-99`, `gate.py:156-165`) | `CARTRIDGE_CONFIG_OK` | none | Config does not need a new field if current touch semantics are accepted. |
| `sessions.allowed` | `LOKZ`, `NYOKZ` | `execution_windows.windows: [LOKZ, NYOKZ]` | Loader builds execution windows from YAML (`loader.py:325`, `loader.py:465-481`) | `CARTRIDGE_CONFIG_OK` | none | Config-only after mapping field name to current schema. |
| `liquidity_sweep.required` | `true` | Chain step 1 always required | Fixed chain sequence starts with sweep (`chain_config.py:1-4`; `chain_evaluator.py:205-216`) | `CARTRIDGE_CONFIG_OK` | none | Current architecture already requires sweep before MSS. |
| `liquidity_sweep.source` | LOKZ sweeps Asia H/L; NYOKZ sweeps LOKZ or Pre-NY H/L | none | Sweep detector records `source/source_id/session/kill_zone`; Chain `_match_sweep` filters direction/time/proximity only (`liquidity_sweep.py:721-744`, `chain_evaluator.py:421-459`) | `CONSOLE_GAP` | `CONSOLE_GAP` | Detector has source metadata, but chain cannot declaratively require source by session. |
| `liquidity_sweep.mss_timing` | 15m MSS within 3 candles after sweep | none | Chain accepts any MSS after sweep and <= current bar; `max_chain_bars` exists in `ChainConfig` but is not consumed by matcher (`chain_config.py:47-48`, `chain_evaluator.py:461-520`) | `CONSOLE_GAP` | `CONSOLE_GAP` | Needs runtime timing enforcement and a schema surface. |
| `entry_trigger.system_detected_15m_MSS` | required | LTF timeframes `[M15, M5]`; chain MSS step | Detection timeframes are configurable; chain can consume MSS detections (`loader.py:436-437`, `chain_evaluator.py:461-520`) | `CARTRIDGE_CONFIG_OK` | none | If DMB requires 15m-only, current `detection.ltf_timeframes: [M15]` can express that subset. |
| `entry_trigger.momentum_filter` | body >= 60%, body >= 6 pips | none | Chain has displacement grade filter, not body-percent/body-pips threshold config (`chain_evaluator.py:483-502`) | `CONSOLE_GAP` | `CONSOLE_GAP` | Detection properties may carry candle data, but runtime has no declarative threshold path. |
| `entry.entry` | market entry at 15m MSS candle close | `chain.entry_method: OTE_LEVEL` | `EntryMethod` supports `OTE_LEVEL`, `FVG_CE`, `FVG_BOUNDARY`; chain still requires FVG+OTE before entry (`chain_config.py:22-26`, `chain_evaluator.py:225-359`, `chain_evaluator.py:832-842`) | `CONSOLE_GAP` | `CONSOLE_GAP` | This is the largest expressibility blocker: current canon is FVG/OTE entry, not MSS-close entry. |
| `stop_loss` | beyond sweep extreme, wick extreme | `sl_buffer_pips`; derived raw/buffered sweep-level SL | Chain SL uses `SweepMatch.price`, populated from swept level price, not breach wick extreme (`liquidity_sweep.py:1316-1323`, `chain_evaluator.py:844-856`) | `CONSOLE_GAP` | `CONSOLE_GAP` | `sl_buffer_pips: 0` gives raw swept level, not necessarily actual wick extreme. |
| `target` | HTF external liquidity; PDH/PDL then PWH/PWL | `tp_method: FIXED_2R` or `DEALING_RANGE_OPPOSITE` | Reference-level detector computes PDH/PDL/PWH/PWL, but chain TP supports fixed-R or dealing-range opposite (`reference_levels.py:1-8`, `chain_config.py:16-20`, `chain_evaluator.py:858-872`) | `CONSOLE_GAP` | `CONSOLE_GAP` | Target-by-HTF-level is detected but not wired to entry target selection. |
| `rr_filter.min_rr` | `1.5` to selected HTF target | `ChainConfig.min_rr` default `2.0`; loader does not map YAML `min_rr` | Runtime has pre-trade `risk_r < cfg.min_rr` gate, but loader `_build_chain_config` does not set `min_rr` from cartridge YAML (`chain_config.py:47`, `chain_evaluator.py:360-367`, `loader.py:448-462`) | `SCHEMA_GAP` | `SCHEMA_GAP` | Pre-trade RR gate exists; DMB's target-specific measurement remains blocked by target console gap. |
| `risk_management.move_sl_to_be` | enabled on new 15m structure break in trade direction | none | Paper position lifecycle has open/close/halt only; no SL modification or BE management surface (`position.py:1-41`, `broker_adapter.py:45-91`) | `CONSOLE_GAP` | `CONSOLE_GAP` | Post-entry management is not implemented. |
| `hard_invalidations` | explicit DMB skip conditions | partial implicit equivalents | Some invalidations correspond to existing gate/chain refusals; others map to gaps above | `METHODOLOGY_CLARIFICATION` | `METHODOLOGY_CLARIFICATION` | Need Olya/NEX to confirm whether hard-invalidations are audit labels only or must be first-class trace reasons. |

---

## 4. Schema-fit summary

```yaml
as_submitted_loader_fit: FAIL
reason: |
  Candidate is a review document with a nested strategy_cartridge_draft
  block. Current loader expects top-level strategy/family/version/map_required
  and a current-shape chain block.

config_only_subset:
  expressible_today:
    - map_required
    - execution windows LOKZ/NYOKZ
    - FVG-only PDA type in correct premium/discount zone
    - wick/body touch into PDA
    - sweep required
    - 15m-only MSS detection if ltf_timeframes is narrowed
  not_expressible_as_current_yaml:
    - Daily+H4 alignment requirement
    - Daily-FVG primary / 4H-FVG fallback priority
    - session-specific sweep target sources
    - 3-candle sweep-to-MSS timing
    - MSS momentum body/pip filter
    - MSS_CLOSE market entry
    - HTF external-liquidity target selection
    - min_rr 1.5 loader mapping
    - break-even management

schema_fit_verdict: |
  Not loader-fit as submitted. A current-shape YAML could encode only a
  reduced approximation and would silently omit core DMB semantics; that
  would not be a valid DMB shadow run.
```

---

## 5. Console-gap summary

```yaml
console_gaps:
  - daily_and_4h_alignment_context_not_exposed_to_gate_or_chain
  - pda_priority_fallback_runtime_selection_missing
  - session_sweep_target_source_filter_missing
  - sweep_to_mss_max_15m_candles_missing
  - mss_momentum_body_percent_and_pips_filter_missing
  - mss_close_market_entry_missing
  - sweep_wick_extreme_stop_loss_missing
  - htf_external_liquidity_target_selection_missing
  - break_even_management_missing

schema_gaps:
  - candidate_not_current_loader_shape
  - no_yaml_surface_for_priority_sweep_source_timing_momentum_mss_close_target_be
  - min_rr_runtime_exists_but_loader_does_not_map_it

methodology_clarification_items:
  - whether hard_invalidations must become first-class trace reasons
  - exact definitions for Daily+H4 alignment, fallback PDA selection, and BE trigger
```

---

## 6. Counts and final classification

```yaml
counts:
  cartridge_config_only_count: 6
  schema_gap_count: 2
  console_gap_count: 9
  methodology_clarification_count: 1
  out_of_scope_count: 0

final_classification: REQUIRES_CONSOLE_CAPABILITY_WORK

minimum_blocker_set:
  - MSS_CLOSE entry cannot be represented because current chain requires causal FVG + OTE.
  - HTF external-liquidity target selection is not wired into Chain/Execution TP.
  - Daily+H4 alignment and Daily/4H PDA priority/fallback are not exposed as runtime gate context.
  - Session-source sweep filters and 3-candle sweep-to-MSS timing are not configurable/enforced.
  - BE management is not implemented.

blocker_statement: |
  Revised DMB is not config-only expressible today. Schema work alone is
  insufficient because multiple required semantics lack runtime behavior.
```

---

## 7. Shadow-run feasibility

```yaml
answer: blocked_by_console_gap
possible_now_without_code_changes: false
possible_with_schema_mapping_only: false
blocked_by_console_gap: true
blocked_by_methodology_clarification: false

reason: |
  A current-shape YAML approximation could be loaded only by dropping or
  ignoring core revised-DMB semantics. Running that approximation would
  answer a different question and risks false confidence. No shadow run
  should be performed until expressibility blockers are resolved or Olya
  explicitly authorizes an approximation study.
```

---

## 8. Questions for Olya/NEX

```yaml
questions:
  daily_and_4h_alignment:
    - "Is alignment defined as latest Daily MSS direction == latest H4 MSS direction, or by another H4 structure state?"
    - "How stale may the H4 aligned state be before it no longer governs?"

  pda_priority:
    - "Does 4H FVG fallback activate only when no valid Daily FVG exists, when Daily FVG is not contacted, or after Daily FVG invalidation/mitigation?"

  session_sweep_sources:
    - "For NYOKZ, what exact timebox defines Pre-NY range?"
    - "Is LOKZ_high_or_low based on the completed LOKZ window only, or live partial LOKZ range before NYOKZ?"

  sweep_to_mss_timing:
    - "Is the 3-candle count inclusive of the sweep confirmation candle or only subsequent 15m candles?"

  momentum_filter:
    - "Is MSS body percent measured body/range of the MSS candle, displacement candle, or confirming 15m close candle?"
    - "Are the 6 pips body minimum and 60% threshold both mandatory hard gates?"

  target_selection:
    - "If nearest PDH/PDL fails RR >= 1.5, draft says do not extend to further targets; does this also block PWH/PWL fallback?"

  break_even:
    - "What exact event is 'new 15m structure break in trade direction' after entry: MSS, displacement, swing break, or detector-specific event?"
```

---

## 9. Recommended next state

```yaml
recommended_next_state: REVIEWED_TO_DRAFT
reason: |
  Candidate is coherent and reviewable, but not config-only expressible.
  Return to DRAFT/authoring with this gap list and Olya/NEX questions.

not_recommended:
  promotion: "Blocked; no promotion decision in this mission."
  shadow_run: "Blocked; would require approximation or runtime/schema changes."
  schema_patch_only: "Insufficient; console capability work is required."
  DMB_replacement: "Forbidden by mission scope."
```

---

## 10. Scope validation

```yaml
runtime_behavior_changed: false
files_reviewed_only:
  - docs/cartridges/drafts/STRATEGY_CARTRIDGE_DMB_REVISED_DRAFT.md
  - en1gma/cartridges/daily_expansion.yaml
  - docs/canonical/CARTRIDGE_LIFECYCLE_PROTOCOL.md
  - docs/canonical/CARTRIDGE_CONTRACT.md
  - en1gma/cartridges/loader.py
  - en1gma/console/chain/chain_config.py
  - en1gma/console/chain/chain_evaluator.py
  - en1gma/console/chain/gate.py
  - en1gma/console/map/map_engine.py
  - en1gma/console/map/pda_store.py
  - en1gma/console/execution/
forbidden_changes_made: none
```
