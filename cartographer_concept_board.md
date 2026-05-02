# Cartographer concept board — advisor discussion

**Purpose:** Capture an ad hoc brainstorm between **G** and **GPT (advisor)** so other advisors can review, challenge, or extend the idea.

**Scope:** Concept / design lane only — not an implementation or methodology commitment.

**Editing note:** Wording is preserved; structure was normalized into YAML for orientation and tooling.

---

## Full discussion (YAML)

```yaml
meta:
  document_id: cartographer_concept_board
  title: CONCEPT BOARD FROM AD HOC ADVISOR DISCUSSION - FOR TEAM REVIEW
  discussion_mode: brainstorm
  participants:
    g:
      role: idea_sketch
      tone: rough_spark_for_riff_or_pushback
    gpt_advisor:
      role: shape_constrain_name_architecture
      framing: first_glance_response_not_final_spec

g_idea_sketch:
  section_title: G IDEA SKETCH (ROUGH AND BRAINSTORM MODE)
  body: |
    So G, building on this last idea.  And just in brainstorm mode.   This is just for you to riff off, or destroy, the idea is just a spark for now

    I wonder if we deploy a functional agent to create a HTF Wiki inspired by https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

    The idea is that it just runs on a loop, like a Ralph loop or autoresearcher against a set of heuristics we define.

    It does a week, and then gradually starts to work its way through a year.  It creates a wiki such that all types of events it finds are linked so we can see when they occur.

    A master heuristic is held with the rule that finds it.

    This then creates a searchable archive of candidates, for Olya review.

    It goes one week at a time; and just notes down what happening on HTF against a set of criteria we define.

    It’s like a little AI cartographer tool that just beavers away building a multi year HTF candidate pool all linked together.

    Then with Olya we just start working through the candidates and dates.

    If Olya says “‘no, this is incorrect for these reasons, check this one” the cartographer goes off and checks the reference and updates the master rule.

    The idea is eventually we get to a full multi year HTF notations; and use that to run a curated review / refine process with Olya and the cartographer agent.

    Thoughts?

gpt_advisor_response:
  section_title: GPT RESPONSE - HELPING SHAPE THE IDEA, BUT FIRST GLANCE RESPONSE

  opening: |
    This is a strong idea. I would not destroy it. I would constrain it hard.

    What you are describing is not a “wiki” in the loose sense. It is closer to a read-only HTF cartography index: a continuously generated candidate atlas of market scenes, linked to heuristic provenance, pending Olya adjudication.

    The key is: candidate atlas, not truth engine.

  verdict:
    idea: HTF_Cartographer / HTF_Wiki
    assessment: high_leverage_if_bounded
    risk: high_if_allowed_to_become_methodology_engine
    recommended_status: PARK_AS_DESIGN_LANE_AND_PROTOTYPE_READ_ONLY
    core_principle:
      machine_role: discover_candidate_scenes
      Olya_role: label_and_correct
      canon_role: store_ratified_labels_only

  framing_the_useful_version: The useful version

  htf_cartographer:
    purpose: >
      Sweep historical HTF market data and produce a searchable candidate atlas
      of chart scenes for Olya review.
    outputs:
      - candidate_events
      - candidate_windows
      - heuristic_that_found_them
      - chart_context_snapshot
      - links_to_related_candidates
      - review_status
      - Olya_feedback_if_reviewed
    non_outputs:
      - no ground_truth
      - no strategy signals
      - no producer output
      - no certification evidence
      - no trade recommendation

  narrative_after_outputs: >
    This would solve a real problem: Olya’s time is scarce and chart review is high-friction. The system should prepare the field, not ask her to roam.

  framing_architecture: The architecture I’d use

  architecture_preamble: Do not start with a wiki frontend. Start with a candidate scene store.

  architecture:
    data_source:
      - DuckDB_HTF_bars
      - known_levels
      - existing_detector_outputs_if_available
      - annotated_trades_yaml
      - ratified_fixture_dates
    engine:
      name: HTF_Cartographer
      mode: read_only
      cadence: week_by_week
      deterministic: true
      resumable: true
    storage:
      candidate_scene_table:
        fields:
          - scene_id
          - instrument
          - timeframe
          - window_start
          - window_end
          - candidate_type
          - heuristic_id
          - heuristic_version
          - score
          - machine_observation
          - linked_levels
          - linked_prior_events
          - review_status
          - Olya_label
          - Olya_notes
          - superseded_by
          - created_at
          - updated_at
    wiki_layer:
      later: true
      role: read_view_over_candidate_store

  narrative_wiki_layer: The wiki should be a rendering layer, not the primary data model.

  framing_candidate_scene_types: Candidate scene types

  initial_scene_types:
    strong_close_through_candidate:
      source: WP2
      status: high_priority
    basic_closed_through_control:
      source: WP2
      status: high_priority
    balance_candidate:
      source: C2_BALANCE
      status: high_priority
    clean_pullback_candidate:
      source: Olya_digest
      status: high_priority
    failed_delivery_candidate:
      source: Olya_delivery_quality
      status: medium_priority
    reassessment_candidate:
      source: active_target_touched_then_chop
      status: medium_priority
    approaching_target_candidate:
      source: proximity_to_target
      status: medium_priority
    pullback_to_expansion_transition_candidate:
      source: Olya_trade011_addendum
      status: high_priority
    level_state_transition_candidate:
      source: level_state_enum
      status: high_priority

  framing_heuristic_registry: The heuristic registry is the heart

  heuristic_registry_preamble: Each heuristic should be explicit, versioned, and non-authoritative.

  heuristic_registry_example_entry:
    heuristic_id: htf_sct_candidate_v0_1
    candidate_type: strong_close_through_candidate
    status: experimental
    source_basis:
      - Olya_quality_signs
      - WP2_gap_report
    rule_summary: >
      Finds Daily candles closing beyond candidate Daily/Weekly levels with
      large relative body and limited opposing wick.
    parameters:
      lookback_days_for_body_relative: candidate_only
      level_families: [PDH, PDL, PWH, PWL, Daily_swing, Weekly_swing, PDA_zone]
    output_label: candidate_only
    forbidden_claims:
      - strong_close_through_true
      - invalidated_true
      - tradeable_signal

  framing_why_this_date: "Every candidate should answer:"

  why_this_date:
    - what heuristic fired
    - which level/zone was involved
    - what candle/window was involved
    - what similar prior/future scenes link to it
    - what question Olya should answer

  framing_olya_feedback_loop: Olya feedback loop

  olya_feedback_loop_preamble: This is where the idea becomes powerful.

  olya_review_loop:
    candidate_statuses:
      - pending_review
      - reviewed_positive
      - reviewed_negative
      - reviewed_near_miss
      - wrong_candidate
      - needs_more_context
      - deferred
    feedback_fields:
      - Olya_label
      - Olya_plain_language_reason
      - correction_type
      - should_update_heuristic: true_or_false
      - related_scene_to_check
      - confidence
    heuristic_update_rule:
      - never_auto_update_from_one_example
      - accumulate corrections
      - propose heuristic_delta
      - Chair/GPT/CTO review
      - G ratifies before heuristic version changes

  narrative_heuristic_updates: >
    Important: Olya can correct the candidate. The system should not immediately
    mutate the master heuristic. It should propose a heuristic update after enough
    corrections.

  framing_ralph_loop: The Ralph loop / autoresearcher analogy

  ralph_loop_preamble: >
    Karpathy’s vibe is useful: loop, inspect, write notes, improve search. But in
    en1gma, the loop must be constitutional.

  loop:
    for_each_week:
      - load_HTF_context
      - run_candidate_heuristics
      - write_candidate_scenes
      - link_related_candidates
      - produce_weekly_summary
      - mark_all_as_pending_review
      - stop
    never:
      - update methodology automatically
      - certify candidates
      - change heuristics without ratification
      - emit trading signals

  framing_naming: What I’d call it

  naming_preamble: Not “wiki” internally. Names matter.

  naming:
    preferred_internal_name: HTF_CARTOGRAPHER
    artifact_name: HTF_SCENE_ATLAS
    user_view: HTF_WIKI
    table_name: htf_candidate_scenes
    avoided_names:
      - oracle
      - truth_engine
      - labeler
      - classifier

  narrative_naming: >
    “Cartographer” is good. It maps terrain; it does not decide whether to trade.

  framing_prototype: Immediate prototype

  prototype_preamble: The first prototype should be tiny.

  prototype_v0:
    scope:
      instrument: EURUSD
      period: 8_weeks
      timeframe: Daily
      heuristics:
        - strong_close_through_candidate
        - basic_closed_through_control
        - balance_candidate
        - clean_pullback_candidate
    output:
      - markdown_or_yaml_candidate_index
      - max_5_candidates_per_week
      - no database mutation beyond candidate_store
      - no UI
    review_goal:
      - Does this reduce Olya chart-search time?
      - Are candidates mostly relevant?
      - Are machine reasons useful?
      - Which heuristics are noisy?

  narrative_scale: I would not start multi-year. Start 8 weeks. Then 6 months. Then 5 years.

  framing_risks: What could go wrong

  risks:
    methodology_drift:
      failure: machine labels candidates as truth
      mitigation: candidate_only_status_everywhere
    heuristic_overfitting:
      failure: rules chase Olya corrections too quickly
      mitigation: versioned heuristic deltas require review
    wiki_bloat:
      failure: thousands of low-quality pages
      mitigation: candidate scores, dedupe, weekly summaries, archival states
    Olya_overload:
      failure: too many candidates for review
      mitigation: top_N_by_bucket and curated review packs
    hidden_certification_claim:
      failure: candidate atlas treated as evidence of correctness
      mitigation: explicit non-certification banner
    agent_autonomy_creep:
      failure: cartographer updates rules unilaterally
      mitigation: heuristic registry is ratified, not self-modifying

  framing_stage_fit: How this fits the current Stage 2D / WP flow

  stage_fit_preamble: >
    This should not interrupt WP1/WP2. It should become a tooling lane that
    supports them.

  fit_with_current_work:
    supports_WP2:
      - finds strong_close_through positives
      - finds basic_closed_through controls
      - finds invalidation boundary examples
    supports_Stage_2D:
      - finds candidate balance / not_balance scenes
      - builds fixture candidate queue
    supports_future_producer:
      - provides reviewed example bank
      - informs replay and chart-truth suites
    does_not_replace:
      - Olya source authority
      - methodology digest
      - contract amendment
      - certification

  framing_next_artifact: Recommended next artifact

  next_artifact_if_you_proceed:
    path: docs/reviews/PHASE_5_C2_HTF_CARTOGRAPHER_CONCEPT_BRIEF_2026_05_02.md
    classification: TOOLING_CONCEPT_BRIEF | NO_CODE | NO_METHODOLOGY_LABELS | NO_RUNTIME
    purpose: >
      Define HTF Cartographer as a read-only candidate-scene mining tool for Olya
      review, with candidate-only semantics, heuristic registry, scene store,
      and review workflow.
    must_include:
      - candidate_only_rule
      - Olya_labels_truth
      - heuristic_registry
      - scene_store_schema_concept
      - weekly_loop
      - review_status_lifecycle
      - non_authorizations
      - v0 prototype scope

  next_after_concept:
    preamble: "Then if green:"
    artifact: HTF_CARTOGRAPHER_V0_READ_ONLY_PROTOTYPE_BRIEF
    scope:
      - EURUSD
      - 8_weeks
      - 3_to_4_heuristics
      - DuckDB_read_only
      - output_candidate_yaml_or_markdown

  framing_final_view: My final view

  final_view_opening: >
    This is probably one of the better ideas in the project.

    Not because it “automates Olya.” It does the opposite: it makes Olya’s review time more surgical.

  final_take:
    build_it: "yes"
    start_small: "yes"
    keep_candidate_only: absolutely
    no_auto_truth: non_negotiable
    likely_value: high
    first_test: does_it_surface_better_chart_review_targets_than_manual_search

  closing: |
    This could become the bridge between raw historical data and Olya’s discretionary map intelligence. The phrase I’d use:

    HTF Cartographer prepares the terrain; Olya names the truth.
```
