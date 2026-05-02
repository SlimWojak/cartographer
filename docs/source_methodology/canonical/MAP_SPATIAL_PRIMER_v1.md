# MAP SPATIAL PRIMER — How to Think About Olya's Logic

```yaml
document: MAP_SPATIAL_PRIMER
version: 1.0
date: 2026-03-30
format: DENSE_M2M
audience: "Dexter (Lab R&D Manager agent, Qwen backbone)"
purpose: |
  Teach you to reason about the HTF Map as a SPATIAL MODEL,
  not as a filter chain. If you treat the Map as a checklist
  of conditions, you will produce incorrect strategy proposals.
  This document corrects that failure mode.
authority: |
  Derived from: HTF_MAP_SPEC_v0_1.yaml, calibration_results.yaml,
  SYNTHETIC_OLYA_METHOD_vLOCK.yaml, 14 Olya-annotated ground truth trades.
  Olya's judgment is absolute. This document encodes her cognitive model.
```

---

## 0. THE CRITICAL DISTINCTION

```yaml
WRONG_MODEL:
  name: "Filter Chain"
  how_it_thinks: |
    "Check regime: BEARISH ✓
     Check PDA exists: FVG above EQ ✓
     Check kill zone: LOKZ active ✓
     Check chain: sweep→MSS→FVG→OTE ✓
     → TRADE"
  why_wrong: |
    This treats the Map as a sequence of boolean gates.
    It will produce superficially correct but fundamentally
    wrong strategy proposals because it has no concept of
    WHERE price is in space, only WHETHER conditions are met.

CORRECT_MODEL:
  name: "Spatial Picture"
  how_it_thinks: |
    "I am looking at a landscape:
     - We are in a BEARISH world (daily MSS broke down)
     - The dealing range spans from 1.18199 down to 1.16454
     - Equilibrium sits at 1.17327
     - There are unfilled daily FVGs sitting ABOVE equilibrium, in premium
     - Price is currently below EQ, in discount
     - IF price retraces UP into premium and ARRIVES at one of those FVGs
       during a kill zone, THEN I will look at LTF for confirmation
     - Until that happens, I am just watching the picture. Nothing fires."
  why_correct: |
    This is how Olya actually thinks. She holds a persistent mental
    picture of the spatial layout. The picture changes rarely (only on
    structural events). Most of the time she is WAITING for price to
    arrive at a location the picture tells her matters.
```

---

## 1. THE TWO CLOCKS — WHAT vs HOW

```yaml
THE_MAP:
  clock: SLOW
  question_it_answers: "WHERE should I be watching, and in WHICH direction?"
  persistence: "days to weeks — survives across sessions"
  update_frequency: "only on structural events (daily MSS, regime change, new displacement)"
  character: |
    QUIET. Most days produce zero Map updates. This is correct.
    A day with no events means the Map holds exactly as it was.
    The Map is a PICTURE that persists. It does not fire.
    It does not trigger. It does not signal. It just IS.

  contains:
    regime: "BEARISH or BULLISH — set by daily MSS, holds until opposing MSS"
    dealing_range: "origin → extreme, with equilibrium at 50% (wick-to-wick)"
    active_pdas: "FVGs (v1) with lifecycle: OPEN → TOUCHED → MITIGATED/INVALIDATED"
    zone_classification: "each PDA classified as PREMIUM or DISCOUNT relative to EQ"

  anti_pattern: |
    If you find yourself saying "when the Map conditions are met, execute..."
    you are thinking about it wrong. The Map does not have "conditions to meet."
    The Map is a spatial layout that EXISTS. Price moves THROUGH it.
    The question is: "where is price relative to the Map's objects?"

THE_EXECUTION_CHAIN:
  clock: FAST
  question_it_answers: "HOW do I enter, right now, at this specific location?"
  persistence: "intraday — resets each session"
  update_frequency: "per-bar within kill zones"
  character: |
    ACTIVE but only when the Map says price is at a live PDA
    in the correct zone during a kill zone. The chain is a
    stateless sequence: sweep → MSS → FVG → OTE → entry.
    It fires identically regardless of WHICH strategy armed it.

  relationship_to_map: |
    The chain does not know WHY it was activated.
    It does not know the regime, the dealing range, or the PDA type.
    It only knows: "I have been told to scan for LTF confirmation here."
    The chain is INFRASTRUCTURE. The Map is STRATEGY.

SEPARATION_RULE: |
  The Map NEVER fires a trade. The Execution NEVER decides direction.
  Direction PERMISSION comes from the Map.
  Execution TRIGGER comes from LTF confirmation inside a map-approved location.
  These responsibilities NEVER cross.
```

---

## 2. THE MAP AS A LANDSCAPE — Four Persistent Objects

```yaml
OBJECT_1_REGIME:
  what: "The directional bias of the current market structure"
  set_by: "Daily MSS (Market Structure Shift) — a break of prior swing structure"
  persistence: "holds until OPPOSING daily MSS fires"
  values: [BEARISH, BULLISH]
  spatial_meaning: |
    BEARISH regime means: the landscape tilts downward.
    Price is expected to make lower lows. Retracements upward
    are opportunities to enter short, not reasons to go long.
    The regime is the TILT of the landscape.
  update_frequency: "rare — regime changes happen weeks apart in trending markets"

OBJECT_2_DEALING_RANGE:
  what: "The spatial boundaries of the current expansion move"
  components:
    origin: "where the move started (wick of highest liquidity before displacement)"
    extreme: "where the move reached (wick of displacement extreme)"
    equilibrium: "(origin + extreme) / 2 — the midpoint"
    premium: "above equilibrium (for BEARISH: where shorts are valid)"
    discount: "below equilibrium (for BULLISH: where longs are valid)"
  measurement: "wick-to-wick (Olya confirmed Q1/Q2: always wick, full move)"
  persistence: |
    ROLLING — each new pullback→displacement cycle within the same regime
    creates a new dealing range that SUPERSEDES the previous one.
    Regime change → dealing range resets entirely.
  spatial_meaning: |
    The dealing range is the PLAYING FIELD. Everything outside it is noise.
    Equilibrium divides premium from discount. A BEARISH trader wants price
    to be in PREMIUM (above EQ) to sell. A BULLISH trader wants price to be
    in DISCOUNT (below EQ) to buy.
    The dealing range does NOT change because price moves within it.
    It changes only when a new structural expansion creates a new range.

OBJECT_3_ACTIVE_PDAS:
  what: "Price Delivery Arrays — persistent spatial zones of interest"
  v1_scope: "Daily FVGs only (INV-MAP-SCOPE-V1)"
  lifecycle: "OPEN → TOUCHED → REJECTED | MITIGATED | INVALIDATED"
  classification: |
    Each PDA is classified by its position relative to dealing range EQ:
      PREMIUM: PDA midpoint above EQ (valid for shorts in BEARISH regime)
      DISCOUNT: PDA midpoint below EQ (valid for longs in BULLISH regime)
  spatial_meaning: |
    PDAs are LOCATIONS ON THE MAP. They are places where price left
    an imbalance that institutional orders may fill on a return visit.
    They are detected once and HELD — not re-scanned every bar.
    When price ARRIVES at an active PDA in the correct zone,
    that is when the execution gate arms.
  key_rules:
    - "TOUCHED is permanent — once price enters the zone, it stays TOUCHED"
    - "No age expiry — a 3-week-old PDA is as valid as a 3-day-old PDA"
    - "Scoped to CURRENT dealing range — regime change invalidates all PDAs"
    - "PDA created_at = Candle C close (confirmation), not Candle A (anchor)"

OBJECT_4_EXECUTION_GATE:
  what: "Boolean: should LTF chain scan right now?"
  conditions_ALL_required:
    1: "regime.direction != NEUTRAL"
    2: "price is at an active PDA (OPEN or TOUCHED) in the correct zone"
    3: "current time is within a kill zone (LOKZ 03:00-04:00 or NYOKZ 08:00-09:00 NY)"
    4: "regime permits this direction"
  output: "ARMED or DISARMED"
  spatial_meaning: |
    The gate answers: "Is price at a place the Map says matters,
    at a time the Map says to look, in a direction the Map permits?"
    If all four are true: the fast clock activates.
    If ANY is false: the fast clock stays off. Nothing happens.
  persistence: |
    Gate PERSISTS and RE-ARMS each kill zone (Olya Q18 calibration).
    If price is at a PDA and LOKZ passes without a chain completing,
    the gate re-arms for NYOKZ if price is still there.
```

---

## 3. SPATIAL WALKTHROUGH — Trade 001

This is how to narrate a setup in Map language.
Use this structure when proposing new strategy configurations.

```yaml
trade: "001 — Oct 1 2025, SHORT, LOKZ, BEARISH"

THE_PICTURE_ON_SEPT_30:
  regime: |
    BEARISH. Daily MSS broke structure downward in late September.
    The landscape tilts down. We expect lower lows.
    This regime has been active for ~1 week. No opposing MSS in sight.

  dealing_range: |
    Origin: 1.18199 (wick high — highest liquidity before the displacement down)
    Extreme: 1.16454 (wick low — how far the displacement reached)
    Equilibrium: 1.17327 (midpoint)
    
    The playing field: 175 pips from origin to extreme.
    PREMIUM: above 1.17327 (where shorts are valid)
    DISCOUNT: below 1.17327 (where longs would be valid — but regime is bearish, so we don't want longs)

  active_pdas: |
    19 active PDAs detected. Among them: daily FVGs sitting in PREMIUM,
    above equilibrium. These are zones where price left an upside
    imbalance during the displacement. If price retraces UP to fill
    these gaps, that's where Olya expects institutional selling.

  spatial_summary: |
    "We are in a bearish world. Price has displaced down and left
    gaps above equilibrium. If price comes back up to those gaps,
    we will look for LTF confirmation to enter short."
    
    This is the MAP. It does not change tonight. It does not change
    tomorrow morning. It holds until a structural event changes it.

WHAT_HAPPENS_ON_OCT_1:
  gate_arms: |
    LOKZ opens (03:00 NY). Price is at/near an active PDA in premium.
    Gate evaluates: regime BEARISH ✓, price at active PDA ✓,
    PDA in premium (correct zone for shorts) ✓, kill zone active ✓.
    Gate → ARMED.

  execution_chain_activates: |
    Now the fast clock runs. On LTF (15m/5m), the chain scans:
    1. SWEEP: did price take out a nearby liquidity level? (stop hunt)
    2. MSS: did LTF structure shift in the regime direction? (confirmation)
    3. FVG: did the LTF MSS leave a gap? (entry zone)
    4. OTE: is price in the optimal trade entry zone? (precision)
    
    If all four: entry signal. If not: chain stays incomplete.
    The chain does not know WHY it was activated. It just executes.

  what_the_map_did_NOT_do: |
    The Map did not "signal" a trade. The Map did not "trigger."
    The Map provided the SPATIAL CONTEXT — where to watch, which
    direction, which zone. The chain provided the ENTRY MECHANISM.
    These are fundamentally different responsibilities.
```

---

## 4. STRATEGY = MAP CONFIGURATION

```yaml
CORE_PRINCIPLE: |
  "The Map IS the strategy."
  Different strategies are NOT different code paths.
  They are different CONFIGURATIONS of the same Map —
  which regime to require, which PDAs to track, which zone to demand,
  which gate conditions to enforce.

  The execution chain is INFRASTRUCTURE. It does not change
  between strategies. sweep → MSS → FVG → OTE → entry.
  Always. The chain is universal.

HOW_TO_PROPOSE_A_NEW_STRATEGY:
  step_1: "Describe the MAP PICTURE — what does the landscape look like when this setup is live?"
  step_2: "Identify the PDA TYPE — what spatial object does price need to arrive at?"
  step_3: "Identify the ZONE — where relative to equilibrium must the PDA be?"
  step_4: "Identify any GATE MODIFICATIONS — time windows, regime requirements, phase requirements"
  step_5: "The execution chain stays the same — do NOT propose chain modifications"

  format: |
    STRATEGY: [name]
    MAP_PICTURE: [narrative of what the spatial landscape looks like]
    REGIME: [BEARISH | BULLISH | EITHER]
    DEALING_RANGE: [how is it derived — same as standard, or different?]
    PDA_TYPE: [FVG | OB | IFVG | other — must be in vLOCK or flagged as 'needs new primitive']
    PDA_TIMEFRAME: [DAILY | H4 | H1 | LTF]
    ZONE: [PREMIUM | DISCOUNT]
    GATE_MODIFICATIONS: [additional time windows, phase requirements, etc.]
    CHAIN: "standard (sweep → MSS → FVG → OTE)" [DO NOT MODIFY]

EXAMPLE_DMB_EXPANSION:
  strategy: "DMB_EXPANSION"
  map_picture: |
    "We are in a trending regime (BEARISH or BULLISH). Daily MSS has fired.
    The dealing range is established. There are daily FVGs in the
    correct zone (premium for bearish, discount for bullish).
    We wait for price to retrace to one of those FVGs during a kill zone."
  regime: "BEARISH or BULLISH (not NEUTRAL)"
  dealing_range: "standard (wick-to-wick, rolling within regime)"
  pda_type: "FVG"
  pda_timeframe: "DAILY"
  zone: "PREMIUM (bearish) or DISCOUNT (bullish)"
  gate_modifications: "none — standard kill zones"
  chain: "standard"

EXAMPLE_SILVER_BULLET_HYPOTHESIS:
  strategy: "SILVER_BULLET (HYPOTHESIS — requires Olya validation)"
  map_picture: |
    "We are in a trending regime. The dealing range is established.
    But instead of waiting for price to reach a DAILY FVG, we look
    for a 15m FVG that forms within a specific time window (the
    Silver Bullet window) in the direction of the daily bias.
    The spatial picture is the same — regime + direction + zone —
    but the PDA is on a lower timeframe and time-gated."
  regime: "BEARISH or BULLISH"
  dealing_range: "standard"
  pda_type: "FVG"
  pda_timeframe: "15M (NOTE: this is LTF — may require MAP-SCOPE expansion)"
  zone: "PREMIUM or DISCOUNT (aligned with regime)"
  gate_modifications: |
    TIME WINDOW: FVG must form between specific hours.
    Academic ICT says 10:00-11:00 NY.
    BUT: Olya's kill zones are LOKZ (03:00-04:00) and NYOKZ (08:00-09:00).
    CRITICAL QUESTION FOR OLYA: "Does Silver Bullet use YOUR kill zones
    or the academic ones? Or is it a different time window entirely?"
  chain: "standard"
  open_questions:
    - "Does Olya recognise Silver Bullet as a distinct setup?"
    - "If yes, what time window does she use?"
    - "Does it use a 15m PDA (requires MAP-SCOPE expansion) or can it be expressed with existing daily PDAs?"
    - "Is the chain modified (e.g., no sweep required)?"
```

---

## 5. ANTI-PATTERNS — How NOT to Think

```yaml
ANTI_PATTERN_1:
  name: "Checklist Thinking"
  symptom: "Describing the Map as 'when condition X AND condition Y are true'"
  correction: "Describe the Map as a PICTURE — what does the landscape look like?"
  test: |
    If your proposal reads like an IF-THEN chain, rewrite it.
    If it reads like a spatial narrative, you're on track.

ANTI_PATTERN_2:
  name: "Chain Modification"
  symptom: "Proposing a strategy that changes the execution chain order or steps"
  correction: |
    The chain is INFRASTRUCTURE. It does not vary by strategy.
    sweep → MSS → FVG → OTE → entry. Always.
    If your strategy seems to need a different chain, you are probably
    confusing a Map configuration with a chain modification.
    Ask: "Can this be expressed as a different PDA type, zone, or gate condition?"

ANTI_PATTERN_3:
  name: "Parameter Hunting"
  symptom: "Proposing 'change FVG threshold from X to Y' as a strategy finding"
  correction: |
    Parameter tuning is Olya's domain. The Lab proposes STRUCTURAL insights:
    new Map configurations, new PDA scoping rules, new time windows.
    "FVGs in this time window show higher quality" is structural.
    "Change the FVG ATR multiplier from 1.5 to 1.7" is parameter hunting.

ANTI_PATTERN_4:
  name: "Conflating Map and Execution"
  symptom: "Describing LTF events (5m FVGs, 15m MSS) as Map objects"
  correction: |
    The Map operates on HTF: daily, 4H, H1. LTF events feed the
    execution chain, not the Map. If your strategy proposal puts
    a 5m FVG into the Map, you are crossing the clock boundary.
    Exception: time-gated LTF PDAs (like Silver Bullet) MAY be a
    Map expansion — but this requires explicit INV-MAP-SCOPE upgrade.

ANTI_PATTERN_5:
  name: "Signal Thinking"
  symptom: "Saying the Map 'generates a signal' or 'triggers an alert'"
  correction: |
    The Map generates NOTHING. The Map IS a persistent spatial state.
    The execution gate reads the Map state and decides whether to arm.
    The chain fires when armed and conditions met on LTF.
    Signal language implies the Map is active. It is passive.
    The Map is the TERRITORY. The chain is the SCOUT walking through it.
```

---

## 6. TESTING YOUR UNDERSTANDING

```yaml
SELF_CHECK:
  before_proposing_any_strategy_ask_yourself:

    Q1: "Can I draw the Map picture for this strategy on a blank chart?"
    fail: "If no → you don't understand the spatial layout yet"

    Q2: "Does my proposal change the execution chain?"
    fail: "If yes → reframe as a Map configuration instead"

    Q3: "Does my proposal require parameters not in vLOCK?"
    action: "If yes → flag as 'requires new primitive' and note which vLOCK primitive is closest"

    Q4: "Can I narrate this setup the way Trade 001 was narrated in Section 3?"
    fail: "If no → your proposal is too abstract. Ground it in spatial language."

    Q5: "What structural events would change this Map picture?"
    fail: "If you can't answer → you don't understand Map persistence"

    Q6: "Is my finding structural or parametric?"
    structural: "Silver Bullet uses a time-windowed 15m FVG" → VALID
    parametric: "FVG works better with 1.7x ATR threshold" → INVALID for Lab
```

---

```yaml
SUMMARY: |
  The Map is a picture. It persists. It is quiet.
  The Chain is a mechanism. It activates. It is brief.
  The Map answers WHERE. The Chain answers HOW.
  Strategies are Map configurations, not Chain modifications.
  
  When you propose a new strategy, DRAW THE PICTURE FIRST.
  If you can describe what the landscape looks like when
  the setup is live, you understand the Map.
  If you can only list conditions, you don't.
```

*"The Map is the territory. The Chain is the scout."*
