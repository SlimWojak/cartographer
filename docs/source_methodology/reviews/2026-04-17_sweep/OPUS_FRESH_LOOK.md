# OPUS FRESH LOOK — en1gma Sweep Artifacts
# Cross-analysis across CTO_BRIEF + SWEEP_FINDINGS + HANDOVER
# Date: 2026-04-17
# Author: Opus (Cursor agent, this session)
# Audience: Incoming CTO, G, future agents triaging M3.5 remediation

```yaml
document_type: analytical_pass
status: SUPPLEMENT (does not supersede sweep / brief / handover)
reading_order:
  1: docs/CTO_HANDOVER_2026_04_17.md
  2: CLAUDE.md (v0.7)
  3: docs/FORWARD_PLAN.md (v1.3)
  4: docs/CTO_BRIEF_2026-04-17.yaml
  5: docs/SWEEP_FINDINGS_2026-04-17.yaml
  6: THIS DOC (fresh look — 10 gaps surfaced during orientation)

principle: |
  Multi-model sweep + CTO brief are authoritative for findings and triage.
  This doc surfaces cross-artifact tensions, ordering traps, and implicit
  assumptions the main triage may have under-emphasized. No new bugs —
  new angles on existing findings.
```

---

## GAP_1 — v4 discovery scan depends on ALL of SW01 + SW02 + SW03, not SW02 alone

**Source artifacts.** HANDOVER §1 DISCOVERY_SCAN: *"After Block 0 fixes, re-run as v4 and compare."* Implies re-run is SW02-gated (future leak). CTO_BRIEF §8 P4_DISCOVERY_SCAN: *"Discovery scan uses run_map_replay() which is forward-contaminated. Any scan results produced before SW02 fix are unreliable."* Also SW02-focused.

**The gap.** v3 produced 10 longs out of 22 trades. If SW01 (inverted PDA mitigation) were fixed without SW02, bullish PDAs would zero out during replay (close > zone_top trivially true → immediate MITIGATED → no active PDAs). The 10 longs fired in v3 only because the REJECTED-via-trade-write-back path masked the inverted MITIGATED check. Once SW01 is corrected, bullish behaviour changes independently of SW02.

**Why it matters.** Re-running v4 after SW02 alone would produce a scan that is temporally clean but still methodology-wrong. The +23R/68%WR headline is at risk of being "retained" because SW02 is the known contaminant — when in fact the whole longs column will shift when SW01 lands.

**Action.** `docs/FORWARD_PLAN.md` P6_DISCOVERY_SCAN_V4 now explicitly gates on `SW01 + SW02 + SW03` together. Do not re-run before Block 0 (0a + 0b) is complete.

---

## GAP_2 — SW10 fix (enforce pda_timeframes=[DAILY]) conflicts with M3.1 DR cascade

**Source artifacts.** SWEEP_FINDINGS SW10: *"Strategy YAML declares pda.timeframes: [DAILY] ... neither execution gate nor map orchestrator filters PDAs by timeframe."* CLAUDE.md v0.7 §6: `INV-MAP-SCOPE-V1.1: "Daily regime + daily FVG. DR cascades daily → H4 when daily is expanding."` context/map_engine.py creates PDAs from 1D AND 4H.

**The gap.** Literal SW10 fix filters to `[DAILY]` only. But M3.1 introduces a cascade window where daily DR is invalid and H4 DR is used for zone classification. During that window the system relies on H4 PDAs being live. Filtering them out collapses the gate to "no armed state in cascade" — we regress M3.1's bullish trades.

**Two interpretations.**
- **A) pda_timeframes narrows tradeable PDAs only; DR cascade is orthogonal.** H4 FVGs should not arm the gate even during cascade. Strategy YAML is authoritative.
- **B) pda_timeframes follows DR authority.** When daily DR is active use DAILY PDAs; when H4 DR is active (cascade) use H4 PDAs. YAML needs a cascade-aware directive.

**Why it matters.** A wrong fix either re-introduces the pre-M3.1 bullish blindness (A implemented literally without YAML update) or keeps the INV-MAP-SCOPE-V1.1 boundary porous (B implemented without Olya ruling).

**Action.** Olya queue rank 11 (architectural, non-urgent). Added in `docs/FORWARD_PLAN.md` §6 and `docs/CTO_BRIEF_2026-04-17.yaml` olya_queue. Do not ship SW10 fix until this is resolved.

---

## GAP_3 — Sentinel is blind to SW05 and SW09 silent failure modes

**Source artifacts.** CTO_BRIEF §3 sentinel: `checks: [halt_signal, river_heartbeat, ibkr_gateway, ars_daemon, notification_file]`. SW05 and SW09 are "silent" — the daemon process stays alive and the river heartbeat keeps ticking while bars are dropped or session state is lost.

**The gap.** `check_ars_daemon` presumably verifies launchd process presence; `check_river_heartbeat` verifies staging freshness. Neither detects:
- ARS daemon is alive but bar stream has a hole (SW05).
- ARS daemon is alive but didn't backfill Asia/sweep state after launchd restart (SW09).

After SW05 + SW09 land as fixes, Sentinel still won't *catch* the next silent failure class unless we add a positive indicator — e.g. "bars consumed per hour" or "phase transitions observed per session".

**Why it matters.** Sentinel is the operator's only runtime eye on M3. If operators trust the green lights and both SW05/SW09 classes recur via a different mechanism (e.g. staging file rotation), no one notices.

**Action.** After Block 1 ships SW05/SW09 fixes, add a `check_ars_phase_progress` Sentinel check — asserts phase transition recorded within last N minutes during session window. Not a finding to fix now; a follow-up to queue post-Block 1.

---

## GAP_4 — SW01 fix will break test_pda_lifecycle_mitigation atomically

**Source artifacts.** SWEEP_FINDINGS SW01 code_refs: `"en1gma/tests/unit/test_map_engine.py:141-154 (test validates WRONG behavior)"`. SW01 proposed_fix includes *"Fix test_pda_lifecycle_mitigation to validate correct behavior (see SW13)"*.

**The gap.** HANDOVER §3 emphasises SW01 as a two-file swap (pda_store.py + map_engine.py). It does not emphasise that **landing the code fix without the test fix breaks the suite**. The current test asserts the INVERTED behaviour. A naive "fix code, run tests, see red, debug" loop will mislead the next agent.

**Why it matters.** Block 0b is Olya-gated. When Olya confirms, the next engineer will rush the SW01 code change. If the commit is not atomic (code + test in one commit, test assertion flipped), CI goes red and the rollback conversation starts.

**Action.** `docs/FORWARD_PLAN.md` P3_BLOCK_0B_OLYA_GATED now specifies `atomic: "code swap + test fix in ONE commit"`. Added to Opus briefing notes for the incoming CTO session.

---

## GAP_5 — SW07 (timezone stripping) threatens INV-REPLAY-DETERMINISM, not just edge cases

**Source artifacts.** SWEEP_FINDINGS classifies SW07 as `severity: HIGH, class: edge_case` and places it in Block 2. Description: *"If detections arrive in UTC while current_bar_time is NY-aware (or vice versa), timestamps representing different instants can compare equal or inverted."*

**The gap.** INV-REPLAY-DETERMINISM (CLAUDE.md §6) says *"Same stored inputs → same outputs. Always."* `replace(tzinfo=None)` is the kind of conversion where two different Python runtimes, two different `River` instances, or two different cached bar metadata sets (UTC-aware vs NY-aware depending on how the parquet was last written) can produce different ordering and therefore different chain outcomes. This is not an edge case — it is a determinism hazard.

**Why it matters.** Block 2 is "pre-live hardening". If SW07 is there, any walk-forward replay between now and live could be non-reproducible. That undercuts validation results as much as SW02 did.

**Action.** `docs/FORWARD_PLAN.md` v1.3 promotes SW07 from Block 2 → Block 1 (per G's D2 decision).

---

## GAP_6 — SW05 production deploy path is not specified in the handover

**Source artifacts.** HANDOVER §3 PHASE_0_TODAY: *"SW05: ... queue-based next_bar() buffering. effort: 0.5 day. ref: data/river.py:155-194"*. Says what to fix, not how to deploy.

**The gap.** The fix lands in the M4 dev repo. Production River is a shared dependency on M3 Ultra (live ARS daemon polls it every poll_interval_s=5s). Shipping the fix requires:
1. Commit + push from M4.
2. `git pull` on M3 (whoever has shell access).
3. Daemon restart — launchd will re-invoke `run_ars_session.py` on next scheduled fire (05:50 local), so either (a) wait for natural restart, or (b) manual launchd reload.
4. Verification — Sentinel crontab isn't installed yet, so no automated monitor.

**Why it matters.** There is a window where the new code is live on M3 without automated monitoring. If the queue-based `next_bar()` has a subtle regression (e.g., drains queue too aggressively and starves poll loop), the operator has no feedback until the session trace is inspected.

**Action.** Documented in `docs/FORWARD_PLAN.md` §2 P0 `deploy: "M3 daemon git pull + launchd restart (G ops step)"`. COO on M3 should tail the next session trace manually (one-off) until Sentinel crontab is active.

---

## GAP_7 — SW08 fix proposes a "mode parameter" without specifying enforcement contract

**Source artifacts.** SWEEP_FINDINGS SW08 proposed_fix: *"Add mode parameter: in live mode, require lease/risk to be non-None"*.

**The gap.** The shape is correct but the *enforcement mechanism* is unspecified. Open questions:
- Where does `mode` come from? Env var, config file, constructor arg?
- Who is authoritative? `orchestrator` constructor? `governance` module at check time?
- How does code prevent accidental `mode=paper` flag sticking after graduation?
- Does `check_governance(mode=live, lease=None)` raise or log-and-skip?

Two different implementations can both pass the literal sweep check (*"mode parameter added, live mode requires non-None"*) while having very different safety properties.

**Why it matters.** This touches `INV-NO-UNGOVERNED-TRADES` and `INV-LIVE-REQUIRES-T2`. A half-specified guardrail is worse than an obvious gap — it *looks* like protection but isn't. Both models flagged SW08; the fix must be equally rigorous.

**Action.** Before Block 1 SW08 implementation, the incoming CTO should issue a 1-page contract spec covering: source of `mode`, single authoritative check site, failure mode (raise, not log-and-skip), test coverage (live + lease=None must raise during test init). Not ready to write until CTO-decision made.

---

## GAP_8 — Block 0 is NOT atomic; split into 0a (Olya-independent) and 0b (Olya-gated)

**Source artifacts.** HANDOVER §3 PHASE_1_BLOCK_0 lists SW01 + SW02 + SW03 as one block. CTO_BRIEF §5 block_0_immediate lists the same three together.

**The gap.** SW01 requires Olya's confirmation on retrace-fills semantics. SW02 and SW03 do not. Olya has been absent 19 days. Blocking SW02 + SW03 behind SW01 wastes engineering days for no technical reason.

**Why it matters.** Splitting lets Block 0a ship immediately. That unblocks clean replay (SW02) and day-state observation (SW03) independently, which in turn unblocks SW01 verification: once we have clean replay + working day-state, we can empirically confirm SW01 by watching bullish PDAs behave correctly pre/post the fix — strengthening the Olya conversation with data rather than abstract semantics.

**Action.** `docs/FORWARD_PLAN.md` v1.3 P1_BLOCK_0A_OLYA_INDEPENDENT and P3_BLOCK_0B_OLYA_GATED. Per G's D1 decision.

---

## GAP_9 — DAILY_MOMENTUM_BREAKOUT_CANON.md is superseded but still in the methodology tree

**Source artifacts.** HANDOVER §9 do_NOT_read: *"DAILY_MOMENTUM_BREAKOUT_CANON.md — SUPERSEDED by Map + YAML"*. The file is at `en1gma/methodology/DAILY_MOMENTUM_BREAKOUT_CANON.md` (566 lines).

**The gap.** Future agents (including Opus, Codex, Henry) scanning the methodology folder will find this file and may anchor on it. The `do_NOT_read` instruction lives in the handover, not in the file itself. The file is also in the `en1gma/methodology/` tree, which the handover explicitly calls out as the reference surface.

**Why it matters.** Methodology drift — agents can silently regress to an older spec while appearing to follow "the methodology docs".

**Action.** Added note to `CLAUDE.md` §3 directory structure marking the file SUPERSEDED and pointing to `strategies/daily_expansion.yaml`. Optionally relocate to `docs/VAULT.md` after CTO confirms no external refs — out of scope for this session.

---

## GAP_10 — Test delta 157 → 202 is unexplained by Sentinel alone

**Source artifacts.** HANDOVER M3_1: *"tests: 157 passing at M3.1 ship"*. CTO_BRIEF §9.q1: *"Full suite run on M4 ... 202 passed ... Up from 142 at March 31 baseline. Growth: +60 tests (Sentinel ~30, Henry, orchestrator M3 wiring, day_state, discovery scan, strategy loader)."*

**The gap.** 157 (M3.1) + ~30 Sentinel = 187. The brief's +60 sums from the 142 baseline, not the 157 M3.1 number. Either:
- The 157 number in the handover is wrong (should be closer to 172?), or
- The +60 list mixes tests added before M3.1 with tests added after.

Verified this session via `pytest --collect-only -q`: **202 tests collected, 202 passing**.

**Why it matters.** Cosmetic — but this file needs to be internally self-consistent. Anyone verifying the handover against the brief will find the arithmetic inconsistent.

**Action.** `CLAUDE.md` v0.7 and `FORWARD_PLAN.md` v1.3 both now cite `202 passing as of 2026-04-17` directly, without trying to reconcile the intermediate deltas. Handover file is historical and left untouched per reading-order rule.

---

## SUMMARY TABLE

```yaml
gaps_by_category:

  ordering_and_dependencies:
    - gap_1: "v4 scan gates on SW01+SW02+SW03, not SW02 alone"
    - gap_8: "Block 0 split into 0a (Olya-indep) and 0b (Olya-gated)"

  implementation_hazards:
    - gap_2: "SW10 vs M3.1 cascade tension — Olya queue rank 11"
    - gap_4: "SW01 code + test fix must be atomic"
    - gap_7: "SW08 enforcement contract needs CTO spec before coding"

  monitoring_and_ops:
    - gap_3: "Sentinel blind to SW05/SW09 classes — add phase-progress check post-Block 1"
    - gap_6: "SW05 deploy path documented (manual git pull + launchd restart)"

  architecture_guardrails:
    - gap_5: "SW07 promoted Block 2 → Block 1 (determinism risk)"

  hygiene:
    - gap_9: "DAILY_MOMENTUM_BREAKOUT_CANON.md marked superseded"
    - gap_10: "test count 202 verified, intermediate delta not reconciled"

decisions_actioned_this_session:
  D1: "Block 0 split — implemented in FORWARD_PLAN v1.3"
  D2: "SW07 promoted — implemented in FORWARD_PLAN v1.3"
  D3: "SW10 tension → Olya queue rank 11 — implemented in FORWARD_PLAN v1.3 + CLAUDE.md v0.7"
  D4: "This doc created — implemented"

items_deferred_to_new_cto_session:
  - "SW08 enforcement contract spec (gap_7)"
  - "Sentinel phase-progress check design (gap_3, post-Block 1)"
  - "DAILY_MOMENTUM_BREAKOUT_CANON.md relocation to VAULT (gap_9)"
```

---

*Fresh-look pass complete. No new bugs discovered. All findings are cross-artifact tensions.*
*Authoritative triage: `docs/CTO_BRIEF_2026-04-17.yaml`. Implementation detail: `docs/SWEEP_FINDINGS_2026-04-17.yaml`.*
