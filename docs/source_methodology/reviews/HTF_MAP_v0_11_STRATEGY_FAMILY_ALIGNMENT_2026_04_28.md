# HTF Map v0.11 Strategy-Family Alignment Note

```yaml
review_id: HTF_MAP_v0_11_STRATEGY_FAMILY_ALIGNMENT_2026_04_28
mission_id: POST_4B.H6.HTF_MAP_SPEC_v0_11_GAP_ANALYSIS
classification: READ_ONLY_METHODOLOGY_INTAKE | STRATEGY_FAMILY_ALIGNMENT
scope: console_map_to_strategy_boundary
behavior_change: none
baseline_commit: 063cb6a
review_date: 2026-04-28
authoritative_source: docs/reviews/OLYA_HTF_MAP_SPEC_INTAKE_2026_04_28.md
runtime_changes: NONE
schema_changes: NONE
cartridge_changes: NONE
strategy_performance_judgment: NONE
```

---

## 1. Alignment verdict

HTF Map v0.11 clarifies that **core Map is Daily interpreted context**. H4 is not a Map authority layer; it is `strategy_specific_only` and belongs in strategy confirmation or strategy-specific selection logic, not in the core Map.

This changes how the DMB blocker set should be classified: DMB's Daily+H4 alignment and 4H FVG fallback are **not** reasons to keep H4 in core Map. They become strategy-specific confirmation/selection gaps that must be built without violating `INV-CONSOLE-STRATEGY-BLIND`.

---

## 2. DMB implications

```yaml
DMB_current_review_source: docs/reviews/DMB_expressibility_review_2026_04_28.md
DMB_draft_source: docs/cartridges/drafts/STRATEGY_CARTRIDGE_DMB_REVISED_DRAFT.md
DMB_prior_verdict: REQUIRES_CONSOLE_CAPABILITY_WORK
DMB_v0_11_updated_verdict: REQUIRES_CONSOLE_CAPABILITY_WORK
DMB_shadow_run_feasibility_under_v0_11: still_blocked_by_console_gap
```

| DMB requirement | Prior classification | v0.11 reclassification | Implication |
|---|---|---|---|
| Daily+H4 aligned HTF continuation | Console gap in expressibility review | **Strategy-specific H4 confirmation gap**, not core Map authority | Core Map should output Daily direction/state/targets. DMB may separately ask for H4 confirmation, but that surface must not turn H4 into Map authority. |
| Daily FVG primary, 4H FVG fallback | Console gap | **Strategy-specific PDA/FVG selection gap** | v0.11 makes Daily Map primary. A 4H fallback, if retained by Olya, belongs to DMB-specific confirmation/selection logic. |
| Correct PD zone | Existing Map/Gate partial | **Behavioral mismatch** | v0.11 says PD zone/quadrant are label-only. Current gate uses premium/discount as permission logic, so DMB should consume labels explicitly rather than rely on core Map gate permission semantics. |
| HTF external-liquidity target | Console gap | **Core Map v0.11 gap** | DMB target selection becomes a consumer of `available_targets` / external liquidity outputs. Current Map lacks those outputs. |
| RR to nearest HTF target | Schema/console gap | **Depends on core Map target output plus DMB strategy logic** | v0.11 says no hard ranking and strategy selects execution target. DMB can enforce nearest target/RR only after Map emits external targets. |
| Target completion stop-trading/reassessment | Not previously central | **Core Map v0.11 gap** | DMB should respect `target_completion_status` and `market_state=reassessment`, but current Map cannot emit either. |
| MSS-close entry, sweep timing, momentum filter, BE management | Console gaps | Unchanged by v0.11 | These remain Chain/Execution capability gaps, not Map gaps. |

### DMB blocker reclassification under v0.11

```yaml
DMB_blockers_reclassified:
  becomes_core_map_gap:
    - htf_external_liquidity_available_targets
    - dominant_draw_target
    - target_completion_status
    - proximity_to_target
    - market_state_reassessment
    - quadrant_or_pd_zone_label_output
  becomes_strategy_specific_non_map_gap:
    - daily_and_h4_alignment
    - h4_fvg_fallback
    - h4_confirmation_context
  remains_chain_or_execution_gap:
    - session_sweep_source_filter
    - sweep_to_mss_three_15m_candles
    - mss_momentum_body_percent_and_pips_filter
    - market_entry_at_15m_mss_close
    - sweep_wick_extreme_stop
    - break_even_management
  remains_schema_or_loader_gap:
    - loader_surface_for_strategy_specific_h4_confirmation
    - loader_surface_for_target_consumption_and_rr_filter
```

---

## 3. MEM implications

No MEM draft cartridge was found in the current repository during this read-only pass. Therefore this note does **not** classify MEM loader fit or performance. It only records likely family implications under the v0.11 Map boundary.

```yaml
MEM_source_status: no_current_MEM_draft_found_in_repo
MEM_assessment_scope: family_alignment_only
```

| MEM concern | v0.11 implication | Current system status | Note |
|---|---|---|---|
| Daily directional context | MEM should consume core Map `direction` if it is a Daily-momentum strategy. | Direction exists, but v0.11 evidence pairing is partial. | No MEM-specific rule can be confirmed without a draft. |
| Pullback/expansion/approaching-target/reassessment state | MEM likely benefits from v0.11 `market_state` to distinguish continuation vs late-move conditions. | Current state vocabulary does not match. | This is a core Map gap before MEM can consume it cleanly. |
| External target awareness | MEM may use `dominant_draw_target`, `available_targets`, and `proximity_to_target` to avoid entries into completed or near-complete draws. | Missing. | This is Map read-model work, not MEM-specific code first. |
| H4 role | Any H4 MEM confirmation must be strategy-specific only. | Current core Map embeds H4. | MEM must not become a reason to preserve H4 as core Map authority. |
| H1 narrative confirmation | v0.11 allows H1 narrative confirmation but says it is not trade gating. | No clean Map output exists; execution detectors may observe H1/session liquidity. | Needs MEM spec before deciding whether this is documentation, trace, or strategy-side context. |

---

## 4. TRM relevance / non-relevance

TRM is currently captured as a **map-independent** draft (`map_required: false`) centered on a Pre-LOKZ range trap/rejection model. HTF Map v0.11 should not be contorted to serve TRM.

| TRM area | v0.11 relevance | Current implication |
|---|---|---|
| Core setup | Low relevance. TRM is a 5m Pre-LOKZ range trap model, not a Daily HTF continuation map consumer. | Do not make v0.11 Map rules depend on TRM. |
| HTF bias | TRM draft explicitly sets `htf_bias_filter: false`. | Core Map should remain optional/irrelevant for TRM unless Olya revises TRM. |
| External/internal liquidity | TRM excludes PDH/PDL, Asia H/L, equal highs/lows, random swing liquidity in range filter. | v0.11 external/internal target system is not a TRM prerequisite. |
| H4 role | No current TRM H4 role. | H4 strategy-specific confirmation is irrelevant unless a future TRM variant asks for it. |
| Console capability | TRM still needs a new session trap/rejection canon if implemented. | That work is separate from HTF Map v0.11. |

```yaml
TRM_alignment_verdict: NOT_A_CORE_HTF_MAP_DRIVER
TRM_implementation_implication: separate_session_model_or_canon_algorithm_if_prioritized
```

---

## 5. H4 role clarified

```yaml
v0_11_h4_rule:
  h4_role: strategy_specific_only
  h4_not_used_in_core_map: true

current_mismatch:
  loader_requires_h4_for_map_required_cartridges: true
  map_uses_h4_for_dealing_range_cascade: true
  map_ingests_h4_structural_events: true
  day_state_allows_h4_transition_tf: true
  pda_creation_stamps_non_daily_as_h4: true

alignment_decision_needed_before_build: |
  H4 must be moved out of core Map authority before v0.11 can be called implemented.
  Strategies may later consume H4 confirmation through a strategy-specific surface, but
  that surface must preserve console strategy-blindness and must not silently restore
  H4 as core Map authority.
```

---

## 6. Family sequencing implication

```yaml
recommended_family_order:
  first: HTF_Map_v0_11_core_Daily_read_model
  second: DMB_strategy_specific_H4_confirmation_and_chain_gaps
  third: MEM_intake_once_source_exists
  fourth: TRM_separate_map_independent_session_canon_if_prioritized

why: |
  DMB and any future MEM can consume Daily Map v0.11 outputs only after the core
  Map emits targets, draw, completion, proximity, and market_state. TRM should not
  drive Map design because its draft is map-independent.
```

---

## 7. Read-only scope statement

```yaml
runtime_behavior_changed: false
console_files_modified: false
schema_files_modified: false
cartridge_files_modified: false
performance_or_profitability_claims: false
```
