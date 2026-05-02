# CARTRIDGE LIFECYCLE PROTOCOL

```yaml
document: CARTRIDGE_LIFECYCLE_PROTOCOL
version: 0.2
date: 2026-04-28
status: CANONICAL_LIGHT
classification: GOVERNANCE_LIGHT | LAYER_A_ONLY
effect: workflow + repository hygiene
behavior_change: none
owner: CTO (maintained), G (promotion/demotion approval), Olya (methodology approval/acknowledgment)
authority_boundary: docs/canonical/CARTRIDGE_CONTRACT.md
conflict_rule: "CARTRIDGE_CONTRACT wins over this lifecycle protocol."
purpose: |
  Define where cartridge drafts live, how they move through review,
  what promotes/demotes/rejects them, and how evidence is linked. This
  protocol does not change cartridge schema, loader behavior, console
  behavior, or strategy semantics.

changelog:
  v0_2: |
    Completes transition matrix, adds REJECTED state, adds REVIEWED→DRAFT
    rework path, records demotion authority, tightens Olya non-methodology
    acknowledgment, and adds review-artifact naming convention. No schema,
    loader, console, or strategy behavior changes.

scope_lock:
  in_scope:
    - lifecycle_states
    - storage_locations
    - promotion_gates
    - demotion_archive_rejection_triggers
    - evidence_links
    - authority_approval_flow
  out_of_scope:
    - cartridge_schema_changes
    - cartridge_template_rewrite
    - DMB_TRM_MEM_semantic_review
    - console_code_changes
    - strategy_behavior_changes
    - ARS_or_DAILY_EXPANSION_parity_surface_changes

states:
  DRAFT: "Candidate only; no runtime authority; not loader-visible."
  REVIEWED: "Schema/contract/delta review completed; not promoted."
  PROMOTED: "Approved cartridge YAML in canonical loader-visible cartridge path."
  DEMOTED: "Previously promoted cartridge removed from active use or superseded."
  REJECTED: "Reviewed candidate rejected before promotion; no runtime authority; may be archived with rejection evidence."
  ARCHIVED: "Historical record only; not eligible for runtime use."

storage_locations:
  draft_candidate_location:
    path: docs/briefs/draft/
    rule: "Draft presence implies no runtime authority."
  review_artifact_location:
    path: docs/reviews/
    rule: "Semantic diff, schema-fit review, run delta, Olya ruling, rejection, and promotion/demotion decision live here."
  promoted_cartridge_location:
    path: en1gma/cartridges/<cartridge_id>.yaml
    rule: "Only PROMOTED cartridge YAML belongs in the loader-visible cartridge directory."
  archive_location:
    path: docs/archive/
    rule: "Superseded, rejected, or demoted materials move or point here with a surviving pointer."
  rejected_candidate_rule: "Rejected candidates remain outside en1gma/cartridges/."

review_artifact_naming:
  pattern: "<cartridge_id>_<review_type>_<YYYY_MM_DD>.md"
  examples:
    - DMB_semantic_diff_2026_04_28.md
    - TRM_schema_fit_review_2026_04_28.md
    - MEM_run_delta_2026_04_28.md
    - DMB_promotion_decision_2026_04_28.md

candidate_identity_minimum:
  required_fields:
    - cartridge_id
    - candidate_version
    - prior_state
    - target_state
    - evidence_artifact_paths
  note: "Lifecycle metadata only; not cartridge YAML schema."

promotion_gates:
  - schema_valid_against_current_loader
  - cartridge_contract_compliant
  - no_console_change_required_or_gap_declared
  - Olya_methodology_approval
  - G_CTO_promotion_approval
  - shadow_or_delta_review_completed
  - no_regression_existing_cartridge_parity_surfaces

gate_definitions:
  schema_valid_against_current_loader: "Current loader accepts the candidate without schema/template changes."
  cartridge_contract_compliant: "Candidate is pure declaration and respects console/cartridge boundary."
  no_console_change_required_or_gap_declared: "Either no console work is needed, or a separate console capability gap is declared."
  Olya_methodology_approval: "Methodology semantics approved by Olya; if CTO classifies a candidate as not methodology-changing, Olya acknowledgment is still required."
  G_CTO_promotion_approval: "Promotion decision is explicitly recorded by G/CTO."
  G_CTO_demotion_approval: "Demotion decision is explicitly recorded by G/CTO, with demotion trigger named and evidence linked."
  shadow_or_delta_review_completed: "Semantic diff and/or shadow-run delta reviewed before promotion."
  no_regression_existing_cartridge_parity_surfaces: "Existing ARS and DAILY_EXPANSION parity/evidence surfaces remain intact."

demotion_triggers:
  - methodology_superseded
  - schema_obsolete
  - behavior_invalidated
  - console_capability_gap_discovered

evidence_links:
  semantic_diff: "What changed versus current or prior cartridge semantics."
  schema_fit_review: "Whether current loader/schema accepts the candidate."
  run_delta: "Replay/shadow delta, or explicit reason no run was performed."
  Olya_ruling: "Methodology approval, rejection, or bounded non-methodology acknowledgment."
  promotion_decision: "G/CTO approve, reject, defer, demote, or archive."

allowed_transitions:
  DRAFT_to_REVIEWED: "Requires schema-fit review + contract review + semantic diff."
  REVIEWED_to_DRAFT: "Review found blocking issues requiring authoring-team revision; review artifacts point to gaps."
  REVIEWED_to_PROMOTED: "Requires every promotion gate with evidence."
  REVIEWED_to_REJECTED: "Requires recorded rejection decision, named blocking reason, and surviving review artifact."
  PROMOTED_to_DEMOTED: "Requires demotion trigger + G_CTO_demotion_approval."
  PROMOTED_to_ARCHIVED: "Requires explicit CTO/G archive decision and surviving pointer; use only when obsolete/superseded, not merely inactive."
  DEMOTED_to_ARCHIVED: "Requires surviving review/archive/finding pointer."
  REJECTED_to_ARCHIVED: "Requires rejection artifact pointer and archive location."

rules:
  - "Any transition not listed is disallowed unless protocol is amended."
  - "Draft, review, rejection, or archive artifacts never imply promotion."
  - "Only PROMOTED state plus loader-visible cartridge YAML carries runtime authority."
  - "Do not place draft, rejected, or experimental YAML under en1gma/cartridges/."
  - "If a candidate requires console code, classify it as a console capability gap, not cartridge work."
  - "This protocol does not add, remove, or rename cartridge YAML fields."
  - "Schema/template issues discovered during lifecycle review are logged as Layer-B design items, not patched here."
  - "Do not rewrite cartridge templates or schemas during Layer-A lifecycle review."
```
