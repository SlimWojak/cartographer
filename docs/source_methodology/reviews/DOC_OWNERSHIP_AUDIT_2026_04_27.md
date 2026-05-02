# Doc Ownership Audit - Post Phase 4b

```yaml
document: DOC_OWNERSHIP_AUDIT_2026_04_27
mission_id: DOCS_CANON_OWNERSHIP_AUDIT_POST_4B
classification: DOC_HYGIENE_AUDIT_ONLY
effect: workflow + orientation
date: 2026-04-27
auditor: GPT-5.5 in Cursor
mode: read-only audit of existing canon surfaces; no canon edits in this mission
branch_observed: feature/phase4b-lane-close
head_observed: cef8fc5
status: AUDIT_COMPLETE
```

---

## 1. Executive verdict

```yaml
verdict: B - AUDIT_FIRST_THEN_SURGICAL_HYGIENE

summary: |
  The post-4b doc architecture has one clean new owner and two bloated live
  surfaces. CERTIFICATION_STATE.md is correctly scoped as the evidence and
  certification state home. CLAUDE.md and FORWARD_PLAN.md now overlap with
  each other, ratification docs, and the new certification doc.

primary_risk: |
  A fresh agent can still recover the truth, but the fastest path now requires
  reading duplicated and partially stale history. That is a doc architecture
  failure, not a methodology failure.

recommended_next_step: |
  Approve a narrow hygiene patch that slims CLAUDE.md and FORWARD_PLAN.md,
  demotes snapshot docs from live orientation, and adds explicit pointers to
  CERTIFICATION_STATE.md, ratification docs, VAULT.md, and methodology seeds.

do_not_do: |
  Do not rewrite doctrine, change invariants, change acceptance gates, hide
  trade_011, or move bloat wholesale into a new "mega" document.
```

---

## 2. Current doc ownership map

```yaml
CLAUDE.md:
  current_role: "Orientation + architecture + invariant encyclopedia + sprint ledger + findings archive"
  target_role: "Stable orientation surface and pointer map"
  should_own:
    - "what en1gma is"
    - "stable architecture spine"
    - "repo structure and execution paths at high level"
    - "current one-screen status"
    - "critical invariant index with pointers"
    - "role map and operating norms"
    - "where to read next"
  should_not_own:
    - "full invariant bodies already owned by ratified docs"
    - "full findings register detail"
    - "feature branch archaeology"
    - "walk-forward evidence tables"
    - "closed sprint/lane narratives"

FORWARD_PLAN.md:
  current_role: "Roadmap + historical Phase 4a/4b mission ledger + stale closeout state"
  target_role: "Live action map only"
  should_own:
    - "next 3-5 actions"
    - "phase gates"
    - "open, parked, deferred items"
    - "current sprint sequence"
    - "decision gates"
  should_not_own:
    - "closed mission implementation detail"
    - "ratification evidence"
    - "walk-forward proof"
    - "historical changelog"

CERTIFICATION_STATE.md:
  current_role: "Evidence state, walk-forward proof, doctrine gaps, upgrade gates"
  target_role: "Same"
  should_own:
    - "what has been proven"
    - "what has not been proven"
    - "walk-forward evidence"
    - "known doctrine gaps"
    - "upgrade conditions"
    - "rerun triggers"
  should_not_own:
    - "implementation roadmap beyond certification gates"
    - "closed mission narratives"
    - "strategy design or future cartridge speculation beyond evidence notes"

RATIFICATION_DOCS:
  target_role: "Closed mission detail and closure authority"
  should_own:
    - "gates run"
    - "commit provenance"
    - "why a lane closed"
    - "fixture-specific closure narratives"

VAULT.md:
  target_role: "Parked strategies and deferred capabilities"
  should_own:
    - "future strategy ideas"
    - "parked capability inventory"
    - "return conditions"
    - "source repo lineage"

POST_PHASE_3_ORACLE.md:
  current_role: "Snapshot code territory map from post-Phase-3"
  target_role: "Archive/reference snapshot, not tier-1 live orientation"
  should_own:
    - "historical post-Phase-3 code map"
    - "snapshot line refs with explicit staleness warning"
  should_not_own:
    - "current authority surface status"
    - "current SW priority"
    - "current orientation map"

PHASE_4_RATIFICATION.md:
  current_role: "Ratified decision snapshot for Phase 4 path"
  target_role: "Canonical historical ratification, not live sprint status"
  should_own:
    - "Phase 4 decision, scope rule, and original operating model"
    - "ratified invariant family origin"
  should_not_own:
    - "current Phase 4b/4c execution state"
    - "live prerequisites after they have closed"
```

---

## 3. Stale/conflict findings

```yaml
F1_FORWARD_PLAN_baseline_stale:
  severity: HIGH
  location: docs/canonical/FORWARD_PLAN.md §1
  finding: |
    daily_expansion is listed as 10 PASS / 2 RED, while current lane close
    and CERTIFICATION_STATE record 11/12 GREEN with trade_011 blocked by
    methodology seed.
  target_owner: CERTIFICATION_STATE.md for evidence; FORWARD_PLAN.md only
    needs a one-line pointer.

F2_FORWARD_PLAN_phase_4b_state_conflict:
  severity: HIGH
  location: docs/canonical/FORWARD_PLAN.md §4
  finding: |
    The document both records Phase 4b lane close and still says
    PHASE_4B_LANE_CLOSE is queued / NEXT_ACTIVE in multiple places.
  target_owner: FORWARD_PLAN.md should retain only current next actions
    after lane close.

F3_FORWARD_PLAN_SW51_SW27_conflict:
  severity: HIGH
  location: docs/canonical/FORWARD_PLAN.md §4 phase_4b_exit
  finding: |
    phase_4b_exit says SW51 and SW27 remain open, but the same document
    and CLAUDE.md say SW51 cluster COMPLETE and SW27 lane CLOSED.
  target_owner: Ratification docs own closure detail; FORWARD_PLAN.md should
    compress to current open items.

F4_FORWARD_PLAN_trade_007_stale:
  severity: MEDIUM
  location: docs/canonical/FORWARD_PLAN.md §1 known_fidelity_gap
  finding: |
    trade_007 is still framed as a known fidelity gap and Phase 4a
    prerequisite. CLAUDE.md says the trade_007 investigation closed on
    2026-04-24 and current code produces BULLISH at the trade evaluation
    moment.
  target_owner: Historical detail belongs in shipped brief/review docs;
    live plan should not surface trade_007 as current gap.

F5_CLAUDE_branch_archaeology_overweight:
  severity: MEDIUM
  location: CLAUDE.md §7
  finding: |
    The code-vs-canon asymmetry and branch inventory consume live orientation
    space and are now likely too detailed for CLAUDE.md. Current observed
    branch is feature/phase4b-lane-close at cef8fc5, not main. CERTIFICATION_STATE
    correctly records merge_status as TBD.
  target_owner: A short repo_state pointer in CLAUDE.md; detailed branch
    history in ratification/handover docs.

F6_CLAUDE_invariant_body_bloat:
  severity: MEDIUM
  location: CLAUDE.md §6
  finding: |
    CLAUDE.md contains full invariant text for many invariants whose durable
    authority lives in CARTRIDGE_CONTRACT.md, PHASE_4_RATIFICATION.md, and
    shipped ratification docs. This makes CLAUDE.md an encyclopedia, not an
    orientation surface.
  target_owner: CLAUDE.md should keep an invariant index with owner pointers;
    full text remains in the ratified owner docs.

F7_CLAUDE_findings_register_bloat:
  severity: MEDIUM
  location: CLAUDE.md §15
  finding: |
    The findings register is useful but too detailed for first-pass
    orientation. It duplicates closeout detail now owned by ratification docs.
  target_owner: CLAUDE.md should keep open/current finding index plus pointer;
    closed detail should live in review/ratification/archive docs.

F8_POST_PHASE_3_ORACLE_live_status_stale:
  severity: HIGH
  location: docs/archive/POST_PHASE_3_ORACLE.md
  finding: |
    This doc is a post-Phase-3 snapshot with stale pointers to CLAUDE v0.15
    and FORWARD_PLAN v2.3, stale test counts, and multiple hazards listed as
    candidates that later closed (SW47, SW48, SW50, SW51, SW27/SW31).
  target_owner: Archive/reference snapshot. Do not keep in tier-1 orientation
    unless it is regenerated from current code and clearly renamed.

F9_PHASE_4_RATIFICATION_snapshot_status:
  severity: MEDIUM
  location: docs/archive/PHASE_4_RATIFICATION.md
  finding: |
    The document is still valuable as the ratified Phase 4 decision record,
    but sections on pre-Mission-1 prerequisites and initial operating model
    are snapshot state, not live state after Phase 4b lane close.
  target_owner: Historical canonical ratification. CLAUDE.md should point to
    it as origin/decision record, not as live status.

F10_CERTIFICATION_STATE_consistency:
  severity: LOW
  location: docs/canonical/CERTIFICATION_STATE.md
  finding: |
    CERTIFICATION_STATE.md is aligned with the intended ownership model after
    the tightening pass: it records 11/12, trade_011 seed, walk-forward
    evidence, unknown taxonomy, FALLBACK reporting, and scoped upgrade gates.
  target_owner: Keep as evidence home.
```

---

## 4. CLAUDE.md proposed surgery

```yaml
target_size: "fresh-agent orientation in <15 minutes; ideally 8-12k words"
edit_mode: "compress in place; preserve pointers"

section_classification:
  header_status_block:
    classification: COMPRESS
    action: |
      Keep one-screen current status. Update to post-4b lane close and
      CERTIFICATION_STATE pointer. Remove long branch/highwater detail.

  §1_WHAT_THIS_IS:
    classification: KEEP
    action: |
      Keep identity, console/cartridge model, lineage summary. Reduce tier-1
      document architecture list after ownership decisions.

  §2_ARCHITECTURE:
    classification: KEEP
    action: "Keep stable 5-layer spine and two clocks/two paths."

  §3_DIRECTORY_STRUCTURE:
    classification: KEEP
    action: "Keep, but ensure it is current and not line-ref dependent."

  §4_STRATEGY_MODEL:
    classification: KEEP
    action: "Keep compressed. Point detailed boundary semantics to CARTRIDGE_CONTRACT.md."

  §5_MAP_OLYA_CALIBRATED_DESIGN:
    classification: KEEP
    action: "Keep as stable methodology summary; no expansion."

  §6_INVARIANTS:
    classification: COMPRESS
    action: |
      Replace full invariant bodies with an index grouped by owner:
      CLAUDE-owned core safety, CARTRIDGE_CONTRACT boundary invariants,
      PHASE_4_RATIFICATION epistemic family, mission-ratified invariants.
      Preserve names and current state; point to full owner docs.

  §7_CURRENT_STATE:
    classification: COMPRESS
    action: |
      Replace branch archaeology with:
        - certification_level pointer to CERTIFICATION_STATE.md
        - phase_4b_lane_close: 11/12, trade_011 seed
        - repo_state: current branch/merge status pointer
        - next_action pointer to FORWARD_PLAN.md

  §7_branch_inventory:
    classification: MOVE
    action: |
      Move detailed branch inventory to a handover/review doc or archive
      appendix. CLAUDE.md keeps only current checkout guidance.

  §8_CLUSTER_TOPOLOGY:
    classification: KEEP
    action: "Keep short; this is useful orientation."

  §9_ROLES:
    classification: KEEP
    action: "Keep. Trim historical advisor detail only if needed."

  §10_COMMUNICATION_STANDARD:
    classification: KEEP
    action: "Keep if still operationally true."

  §11_DEVELOPMENT_RULES:
    classification: COMPRESS
    action: |
      Preserve only high-value rules and pointers. Longer doctrine blocks
      can move to a dedicated doctrine/reference doc if not already owned.

  §12_EXTRACTION_MANIFEST:
    classification: COMPRESS
    action: "Keep lineage summary; detailed extraction status can point to VAULT.md / archive."

  §13_PHASE_PLAN:
    classification: MOVE
    action: |
      Live phase state belongs in FORWARD_PLAN.md. CLAUDE.md should only say
      current phase and pointer.

  §14_CALIBRATION_REFERENCE:
    classification: KEEP
    action: "Keep short; pointer to calibration_results.yaml."

  §15_SWEEP_FINDINGS_STATUS:
    classification: COMPRESS
    action: |
      Keep open/current high-risk index only. Closed details should be
      represented as ID + status + pointer, not full closeout ledger.
```

---

## 5. FORWARD_PLAN.md proposed surgery

```yaml
target_shape: "live roadmap, not sprint ledger"
edit_mode: "replace large historical sections with current-state pointers"

proposed_new_sections:
  1_current_state:
    owns:
      - "certification_level pointer"
      - "11/12 lane close"
      - "trade_011 methodology seed pointer"
      - "current branch/merge/deployment state"
    source_pointer:
      - docs/canonical/CERTIFICATION_STATE.md
      - docs/reviews/PHASE_4B_LANE_CLOSE_RATIFICATION_2026_04_27.md

  2_next_actions:
    owns:
      - "unknown near-miss taxonomy cleanup"
      - "FALLBACK direction reporting cleanup"
      - "walk-forward re-run after cleanup"
      - "M3 deployment/merge state if still pending"
      - "methodology-seed fixture collection"

  3_phase_gates:
    owns:
      - "TRACE_CERTIFIED_DAILY_AUTHORITY_V1 gate"
      - "FULLY_EPISTEMICALLY_CERTIFIED gate pointer"
      - "Phase 4c/4d gates if still live"

  4_parked_deferred:
    owns:
      - "SW44 tier disposition"
      - "SW52 deferred"
      - "H4/NEUTRAL doctrine track"
      - "VAULT pointers"

  5_decision_discipline:
    owns:
      - "scope/effect pointer to CARTRIDGE_CONTRACT.md"
      - "no-new-capability if still active"

section_classification_current_file:
  §1_Current_state:
    classification: STALE_CONFLICT
    action: "Replace with concise current state and CERTIFICATION_STATE pointer."

  §2_Phase_4_scope:
    classification: KEEP
    action: "Keep if Phase 4 scope rule remains active; otherwise mark historical or point to PHASE_4_RATIFICATION.md."

  §3_Phase_4a_prerequisites:
    classification: DELETE_WITH_POINTER
    action: "Closed prerequisite narrative belongs in PHASE_4_RATIFICATION / shipped reviews."

  §4_Phase_4b:
    classification: DELETE_WITH_POINTER
    action: |
      Closed mission detail belongs in PHASE_4B_LANE_CLOSE_RATIFICATION
      and individual SW ratification docs. Retain only current residuals:
      trade_011 seed, unknown taxonomy, fallback reporting, deployment state.

  §5_Phase_4c:
    classification: COMPRESS
    action: "Keep only live verification hardening items and return conditions."

  §6_Phase_4d:
    classification: KEEP
    action: "Keep if schema v2 remains active future work; compress if not next sprint."

  §7_Phase_4_close_Phase_5_readiness:
    classification: COMPRESS
    action: "Align with CERTIFICATION_STATE upgrade gates and remove duplicate evidence."

  §8_Open_findings:
    classification: COMPRESS
    action: "Keep active/parked/deferred list only. Closed findings move to pointers."

  §9_Decision_gate_discipline:
    classification: KEEP
    action: "Keep short pointer to CARTRIDGE_CONTRACT.md §7."
```

---

## 6. CERTIFICATION_STATE validation

```yaml
status: GOOD_KEEP_AS_EVIDENCE_HOME

validated_ownership:
  current_status: KEEP
  walk_forward_evidence: KEEP
  validated_surfaces: KEEP
  known_doctrine_gaps: KEEP
  pending_hygiene_items: KEEP
  certification_upgrade_conditions: KEEP
  walk_forward_provenance: KEEP
  observations_for_future_methodology: KEEP

consistency_checks:
  trade_011: "visible as BLOCKED_BY_METHODOLOGY_SEED"
  MSS_NOT_EQUAL_ACTIVE_CONTROL: "correctly referenced as methodology seed, not invariant"
  chart_truth: "11/12 GREEN represented near top"
  fallback_refusal: "evidence phrasing, not overclaim"
  unknown_taxonomy: "explicit blocker for next scoped certification"
  H4_cascade: "correctly outside current certification scope"

minor_future_watch:
  - "Update merge_status when feature/phase4b-lane-close is merged or main is advanced."
  - "Update head_sha only if walk-forward is re-run from a different commit."
  - "Do not add roadmap narrative; keep roadmap in FORWARD_PLAN.md."
```

---

## 7. Cross-link plan

```yaml
CLAUDE.md:
  should_link_to:
    CERTIFICATION_STATE.md: "current evidence/certification status"
    FORWARD_PLAN.md: "what to do next"
    CARTRIDGE_CONTRACT.md: "console/cartridge boundary and scope/effect"
    MAP_SPATIAL_PRIMER_v1.md: "spatial doctrine"
    VAULT.md: "parked/future concepts"
    PHASE_4B_LANE_CLOSE_RATIFICATION_2026_04_27.md: "why lane closed at 11/12"
    MSS_NOT_EQUAL_ACTIVE_CONTROL.md: "trade_011 methodology seed"

FORWARD_PLAN.md:
  should_link_to:
    CERTIFICATION_STATE.md: "upgrade gates and walk-forward proof"
    PHASE_4B_LANE_CLOSE_RATIFICATION_2026_04_27.md: "closed lane detail"
    VAULT.md: "future strategy/cartridge ideas"
    CARTRIDGE_CONTRACT.md: "scope/effect decision discipline"

CERTIFICATION_STATE.md:
  should_link_to:
    PHASE_4B_LANE_CLOSE_RATIFICATION_2026_04_27.md: "11/12 lane closure evidence"
    MSS_NOT_EQUAL_ACTIVE_CONTROL.md: "seed blocking full epistemic certification"
    VAULT.md: "H4 neutral daily momentum continuation parked strategy"

POST_PHASE_3_ORACLE.md:
  should_link_to:
    replacement_status: "archived snapshot; not live orientation"
    current_code_map_owner: "CLAUDE.md high-level map + repo source + future regenerated ORACLE if needed"

PHASE_4_RATIFICATION.md:
  should_link_to:
    replacement_status: "historical ratification; not live sprint state"
    current_status_owner: CERTIFICATION_STATE.md
    current_plan_owner: FORWARD_PLAN.md
```

---

## 8. Second-pass edit brief

```yaml
mission_id: DOCS_CANON_SURGICAL_HYGIENE_POST_4B
classification: DOC_HYGIENE_PATCH
effect: workflow + orientation
precondition: "G/Architect approval of this audit"

allowed_edits:
  - "Slim CLAUDE.md to orientation + pointer map."
  - "Slim FORWARD_PLAN.md to live roadmap."
  - "Update document architecture lists and cross-links."
  - "Demote POST_PHASE_3_ORACLE.md from live tier-1 orientation to snapshot/reference status."
  - "Clarify PHASE_4_RATIFICATION.md as historical ratification if still listed as live orientation."

forbidden_edits:
  - "No methodology changes."
  - "No invariant semantic changes."
  - "No acceptance gate changes."
  - "No deletion of historical record without pointer."
  - "No hiding trade_011 or MSS_NOT_EQUAL_ACTIVE_CONTROL."
  - "No certification status reclassification."
  - "No moving bloat into a new undefined owner doc."

minimal_diff_plan:
  step_1:
    file: CLAUDE.md
    patch: |
      Replace detailed current-state, branch inventory, invariant bodies,
      phase plan, and findings ledger with compressed indexes and owner
      pointers. Preserve stable architecture, roles, repo map, and critical
      invariants names.

  step_2:
    file: docs/canonical/FORWARD_PLAN.md
    patch: |
      Replace closed Phase 4a/4b mission ledger with live next-actions,
      phase gates, parked/deferred items, and pointers to ratification docs.

  step_3:
    file: docs/archive/POST_PHASE_3_ORACLE.md
    patch: |
      Either add a top warning banner marking it SNAPSHOT_ARCHIVE_REFERENCE
      or move it to docs/archive/ with a pointer from CLAUDE.md. Do not use
      its line refs for current Mission briefs without re-verification.

  step_4:
    file: docs/archive/PHASE_4_RATIFICATION.md
    patch: |
      Do not rewrite ratification content. If needed, add a small status note
      that live Phase 4 execution state now lives in FORWARD_PLAN.md and
      evidence state in CERTIFICATION_STATE.md.

  step_5:
    file: docs/canonical/CERTIFICATION_STATE.md
    patch: |
      No change unless merge_status has resolved by then.

acceptance_checks:
  - "A fresh agent can identify current certification state in <3 minutes."
  - "A fresh agent can identify next 3-5 actions in <5 minutes."
  - "CLAUDE.md target: <12k words or <15 minute read."
  - "FORWARD_PLAN target: live actions visible in first 2 pages."
  - "CLAUDE.md no longer serves as sprint ledger."
  - "FORWARD_PLAN.md contains no closed mission narrative except pointers."
  - "trade_011 remains visible in CLAUDE.md, FORWARD_PLAN.md, and CERTIFICATION_STATE.md."
  - "Every removed historical detail has a surviving pointer."
  - "No new mega-doc absorbs the removed bloat."
```

---

## 9. Bottom line

```yaml
bottom_line: |
  The doc system should now be split cleanly:
    CLAUDE.md = orient
    FORWARD_PLAN.md = direct
    CERTIFICATION_STATE.md = certify
    ratification docs = prove closure
    VAULT.md = park future ideas

  CERTIFICATION_STATE.md is already doing its job. The next hygiene pass
  should be surgical and mostly subtractive: remove duplicated history from
  CLAUDE.md and FORWARD_PLAN.md, replace it with precise pointers, and keep
  trade_011 / MSS_NOT_EQUAL_ACTIVE_CONTROL impossible to miss.
```
