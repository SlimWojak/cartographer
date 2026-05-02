# Daily Momentum Breakout (DMB) Strategy - CANON
## Version: 0.1 - DRAFT (Shaping)
## Date: March 28, 2026
## Status: DRAFT — Olya review required before implementation
## Reference trade: trade_001 (2025-10-01, SHORT, LOKZ)

### Provenance
- Olya's annotated trade_001 in `~/research_accelerator/research/ground_truth/annotated_trades.yaml`
- HTF state detection from `~/research_accelerator/research/STATE_DETECTION_LOGIC_v2.yaml`
- Forensic reconstruction on River 1m bars verified Oct 1, 2025

---

## STRATEGY OVERVIEW

**Name:** Daily Momentum Breakout (DMB)
**Pair:** EUR/USD only
**Session:** LOKZ (02:00-05:00 NY) exclusively
**Edge:** Execution-timeframe entries aligned with daily structural momentum, entering at premium/discount areas of interest during retracement to daily imbalance zones
**Risk per trade:** 1% account equity
**TP:** 2R fixed
**Max trades per session:** 1 (hard cap)
**Complements:** ARS (state-independent) — DMB is state-gated, uses different primitives and timeframes

---

## 1. STRATEGY ARCHITECTURE — FOUR LAYERS

```
LAYER 1: DAILY DIRECTION (daily bars)
│   Daily MSS with displacement → establishes BEARISH or BULLISH bias
│   Daily FVG created by displacement → "area of interest"
│
├── LAYER 2: PREMIUM/DISCOUNT FILTER (daily dealing range)
│   │   50% fib of expansion defines equilibrium
│   │   BEARISH: shorts only in PREMIUM (above 50%)
│   │   BULLISH: longs only in DISCOUNT (below 50%)
│   │
│   ├── LAYER 3: AREA OF INTEREST TRIGGER (daily FVG)
│   │   │   Price must reach the Daily FVG to arm execution
│   │   │   Until price is in/at the daily FVG → no execution scan
│   │   │
│   │   └── LAYER 4: EXECUTION CHAIN (15m + 5m, LOKZ only)
│   │           SWEEP (15m swing point) → MSS (15m) → FVG (5m)
│   │           → retrace to OTE (0.62 fib) → ENTRY
│   │           SL = sweep extreme + 0.5 pip
│   │           TP = 2R fixed
│   │
│   NO TRADE if price not in correct premium/discount zone
│
NO TRADE if no daily MSS / daily direction unclear
```

Each layer gates the next. No layer can be skipped.

---

## 2. LAYER 1 — DAILY DIRECTION

### Daily MSS Detection

```python
# Determine daily structural direction
# Uses most recent Daily MSS (Market Structure Shift)

daily_direction = NEUTRAL  # default

# Primary: Daily MSS
if daily_mss_exists:
    if daily_mss.direction == BEARISH:
        # Daily made a Lower Low, breaking prior swing low
        # Displacement confirmed (strong bearish body candle)
        daily_direction = BEARISH
    elif daily_mss.direction == BULLISH:
        # Daily made a Higher High, breaking prior swing high
        # Displacement confirmed (strong bullish body candle)
        daily_direction = BULLISH

# MSS holds until opposing MSS fires (invalidation-based, not age-gated)
# No trade if daily_direction == NEUTRAL
```

### Daily Displacement Confirmation

```python
# The daily MSS must be accompanied by displacement
# Displacement = strong directional candle with significant body

displacement_valid = (
    daily_candle.body_ratio >= 0.55 AND    # Body >= 55% of total range
    daily_candle.range >= 40 pips           # Minimum daily range (FLAGGED — needs calibration)
)

# The displacement creates the Daily FVG (area of interest for Layer 3)
```

### Daily FVG (Area of Interest)

```python
# The daily displacement creates a 3-candle FVG on the daily chart
# This FVG becomes the "area of interest" — where we expect price to retrace to

# Bearish daily FVG:
#   Day A: candle before displacement
#   Day B: displacement candle (large bearish body)
#   Day C: candle after displacement
#   Gap: Day A low > Day C high

# Bullish daily FVG:
#   Gap: Day A high < Day C low

# The daily FVG zone boundaries become the trigger for Layer 3
daily_fvg_top = day_A.low     # for bearish
daily_fvg_bottom = day_C.high  # for bearish
# (reversed for bullish)
```

**Rules:**
- Daily MSS must exist with displacement confirmation
- Daily FVG must be ACTIVE (not yet filled/closed)
- MSS invalidated only by opposing MSS (not by age)
- If daily direction is NEUTRAL → no DMB trade permitted

**Reference (Oct 1, 2025):**
- Daily bearish MSS from Sept 23-24
- Strong bearish displacement candles Sept 23-24
- Daily bearish FVG created by the displacement

---

## 3. LAYER 2 — PREMIUM/DISCOUNT FILTER

### Dealing Range & Equilibrium

```python
# The dealing range is anchored to the Daily MSS
# It measures the expansion move from MSS origin

# BEARISH MSS:
dealing_range_high = mss_origin_candle.body_high    # Where the move started
dealing_range_low = displacement_extreme_candle.body_low  # Where the move reached

# BULLISH MSS:
dealing_range_high = displacement_extreme_candle.body_high
dealing_range_low = mss_origin_candle.body_low

# Equilibrium = 50% fib (midpoint)
equilibrium = (dealing_range_high + dealing_range_low) / 2
```

### Premium/Discount Classification

```python
# BEARISH daily direction:
#   PREMIUM = price above equilibrium → SHORT entries only
#   DISCOUNT = price below equilibrium → no shorts (price already expanded)

# BULLISH daily direction:
#   DISCOUNT = price below equilibrium → LONG entries only
#   PREMIUM = price above equilibrium → no longs (price already expanded)

if daily_direction == BEARISH:
    if current_price > equilibrium:
        zone = PREMIUM       # ✓ SHORT permitted
    else:
        zone = DISCOUNT      # ✗ No short — price already in discount

if daily_direction == BULLISH:
    if current_price < equilibrium:
        zone = DISCOUNT      # ✓ LONG permitted
    else:
        zone = PREMIUM       # ✗ No long — price already in premium
```

**Rules:**
- Price must be in the correct zone for the daily direction
- BEARISH + PREMIUM = trade permitted
- BULLISH + DISCOUNT = trade permitted
- Any other combination = no trade

**Reference (Oct 1, 2025):**
- Daily bearish → dealing range from Sept 23-24 MSS
- By Oct 1, price had retraced UP above equilibrium → PREMIUM zone
- SHORT permitted

---

## 4. LAYER 3 — AREA OF INTEREST TRIGGER

### Daily FVG as Execution Trigger

```python
# The daily FVG from Layer 1 is the "area of interest"
# Price must REACH this zone before we look at the execution TF

# For BEARISH daily:
#   Price retracing UP into the bearish Daily FVG = trigger armed
#   daily_fvg_bottom <= current_price <= daily_fvg_top

# For BULLISH daily:
#   Price retracing DOWN into the bullish Daily FVG = trigger armed

execution_armed = price_inside(daily_fvg) OR price_touched(daily_fvg)
```

**Rules:**
- Execution scan (Layer 4) ONLY activates when price has reached the Daily FVG
- The Daily FVG must still be ACTIVE (not fully filled by a close through it)
- Price touching the edge of the FVG zone is sufficient to arm
- Once armed for a session date, stays armed for that LOKZ window

**Reference (Oct 1, 2025):**
- Daily bearish FVG from Sept 23-24 displacement
- Price retraced up into this zone during Sept 26-29
- By Oct 1, price is IN the daily FVG → execution armed

### FLAGGED — Daily FVG Lifecycle

```
Questions for calibration:
- How long does a daily FVG remain valid? Until opposing MSS?
- If price passes through the FVG and closes beyond it, is it invalidated?
- Can price re-enter an FVG after leaving it?
- Multiple daily FVGs may exist — which one is the trigger?

These need Olya's input during implementation. For initial shaping,
use the most recent active daily FVG in the MSS direction.
```

---

## 5. LAYER 4 — EXECUTION CHAIN (15m + 5m)

### Pre-conditions

```python
# ALL must be true before scanning for execution:
assert daily_direction != NEUTRAL           # Layer 1
assert zone == PREMIUM or zone == DISCOUNT  # Layer 2 (correct zone)
assert execution_armed                       # Layer 3 (price at daily FVG)
assert current_session in LOKZ              # 02:00-05:00 NY
```

### Step 1: Liquidity Sweep (15m)

```python
# Detect sweep of a 15m swing point
# For BEARISH (SHORT setup):
#   Price sweeps ABOVE a prior 15m swing high
#   Extension: price exceeds the swing high, then reverses

# For BULLISH (LONG setup):
#   Price sweeps BELOW a prior 15m swing low

sweep_detected = (
    price_exceeded(prior_15m_swing_point) AND
    price_reversed_from(sweep_extreme)
)

# The sweep extreme becomes the SL reference
```

**FLAGGED — Swing Point Detection:**
```
15m swing point detection parameters need calibration:
- Lookback period: how many 15m bars to identify swing highs/lows?
- Minimum swing height: filter noise swings?
- Which swing point: nearest to current price? Most recent?

For initial implementation, use simple N-bar swing detection:
  Swing high: bar high > N bars before AND N bars after
  Swing low: bar low < N bars before AND N bars after
  N = 3 (15 minutes * 3 = 45 min lookback/forward) — FLAGGED for calibration
```

### Step 2: MSS — Market Structure Shift (15m)

```python
# After the sweep, price must break structure in the trade direction
# For BEARISH (SHORT):
#   After sweeping a high, price breaks below a prior 15m swing LOW
#   This is the Market Structure Shift — bearish confirmation

# For BULLISH (LONG):
#   After sweeping a low, price breaks above a prior 15m swing HIGH

mss_confirmed = (
    sweep_detected AND
    price_broke(prior_15m_swing_in_trade_direction)
)

# The MSS candle typically has displacement quality (strong body)
```

### Step 3: FVG Detection (5m)

```python
# The displacement that caused the MSS creates a FVG on the 5m chart
# Same FVG logic as ARS (3 consecutive 5m candles, gap exists)

# Bearish FVG: candle_A.low > candle_C.high
# Bullish FVG: candle_A.high < candle_C.low
# Untouched area >= 0.5 pip (from ARS v1.3 calibration)

# The FVG zone is where price will retrace for OTE entry
fvg_zone_top = candle_A.low      # bearish
fvg_zone_bottom = candle_C.high  # bearish
```

### Step 4: OTE Entry (0.62 Fib)

```python
# Calculate OTE from the displacement move
# Displacement move: from sweep extreme to MSS break point

# BEARISH (SHORT):
move_high = sweep_extreme        # Top of the move
move_low = mss_break_low         # Bottom — where structure broke
move_size = move_high - move_low

ote_entry = move_low + 0.618 * move_size  # 0.62 fib retracement

# BULLISH (LONG):
move_low = sweep_extreme
move_high = mss_break_high
ote_entry = move_high - 0.618 * (move_high - move_low)

# Wait for price to retrace to OTE level
# Entry is a LIMIT ORDER at the OTE price
```

### Step 5: SL and TP

```python
# SL = sweep extreme + 0.5 pip buffer (same logic as ARS)
# BEARISH (SHORT):
sl = sweep_extreme + 0.00005    # Above sweep high

# BULLISH (LONG):
sl = sweep_extreme - 0.00005    # Below sweep low

# TP = 2R fixed
risk = abs(ote_entry - sl)
# BEARISH: tp = ote_entry - 2 * risk
# BULLISH: tp = ote_entry + 2 * risk
```

---

## 6. COMPLETE EXECUTION FLOW

```python
# ═══ DAILY SETUP (computed once per day, before LOKZ) ═══

# 1. Compute daily direction from daily bars
#    - Find most recent daily MSS (bearish or bullish)
#    - Confirm displacement quality
#    - If no MSS or NEUTRAL → NO TRADE today

# 2. Identify daily FVG (area of interest)
#    - The FVG created by the daily displacement
#    - Must be ACTIVE (not filled)

# 3. Calculate dealing range and equilibrium
#    - Dealing range from MSS origin to displacement extreme
#    - Equilibrium = 50% fib

# 4. Check premium/discount
#    - BEARISH: current price must be in PREMIUM (above 50%)
#    - BULLISH: current price must be in DISCOUNT (below 50%)
#    - Wrong zone → NO TRADE

# 5. Check if price has reached the daily FVG
#    - Price must be inside or have touched the daily FVG
#    - Not yet reached → NO TRADE (wait)

# ═══ EXECUTION SCAN (15m bars within LOKZ only) ═══

# 6. Detect 15m swing points (lookback within recent structure)

# 7. Scan for liquidity sweep of a 15m swing point
#    - BEARISH: sweep above a swing high
#    - BULLISH: sweep below a swing low

# 8. After sweep, detect MSS on 15m
#    - BEARISH: break below prior 15m swing low
#    - BULLISH: break above prior 15m swing high
#    - MSS must occur AFTER the sweep (temporal ordering)

# 9. Detect FVG on 5m created by the displacement
#    - Same rules as ARS: 3-candle gap, ≥0.5 pip untouched

# 10. Calculate OTE (0.62 fib of displacement move)
#     - Move = sweep extreme to MSS break point
#     - Entry = 0.62 fib retracement level

# 11. Validate trade geometry
#     - Entry must be between SL and TP
#     - R:R is always 2.0 (fixed TP)
#     - SL = sweep extreme + 0.5 pip buffer

# 12. Place limit order at OTE
#     - Wait for price to retrace to 0.62 fib
#     - If price never reaches OTE → no fill, no trade

# ═══ TRADE MANAGEMENT ═══

# 13. Set-and-forget: SL and TP orders placed
# 14. Trade resolves when SL or TP is hit (no timeout)
# 15. Max 1 trade per LOKZ session
```

---

## 7. REFERENCE TRADE — Oct 1, 2025 (trade_001)

### Verified on River 1m bars:

```yaml
daily_context:
  daily_mss: BEARISH (Sept 23-24, displacement confirmed)
  daily_fvg: Created by Sept 23-24 displacement
  dealing_range: MSS origin → displacement extreme
  equilibrium: 50% fib of dealing range
  price_zone: PREMIUM (price retraced above 50% by Oct 1)
  daily_fvg_reached: YES (price in FVG zone by Sept 26-29)

execution_chain:
  prior_15m_swing_high: 1.17748 (02:30 NY)
  sweep: 1.17785 at 03:00-03:10 (3.7 pips above swing)
  displacement: 03:15 (22.9 pip bearish body on 15m)
  fvg_5m: 03:25 (6.0 pip bearish gap on 5m)
  mss_15m: 03:30 (bearish break, low 1.17418)
  ote_0.62: 1.17645

trade_parameters:
  direction: SHORT
  entry: 1.17645 (0.62 fib)
  sl: 1.17790 (sweep extreme + 0.5 pip)
  risk: 14.5 pips
  tp: 1.17354 (2R = 29.0 pips)

outcome:
  ote_reached: 04:38 NY (price retraces to 1.17651)
  tp_hit: 05:50 NY (price reaches 1.17336)
  result: WIN +2.00R
```

---

## 8. DIFFERENCES FROM ARS

| Aspect | ARS | DMB |
|--------|-----|-----|
| **HTF gate** | None (self-contained) | Daily MSS + premium/discount + daily FVG |
| **Kill zone** | 00:00-03:00 NY | 02:00-05:00 NY (LOKZ) |
| **Sweep source** | Asia range boundaries | 15m swing points |
| **Entry signal** | FVG on 5m (immediate) | MSS on 15m → FVG on 5m → OTE retrace |
| **Entry method** | Market order at Candle C close | Limit order at 0.62 fib |
| **SL** | Sweep extreme + 0.5 pip | Sweep extreme + 0.5 pip (same) |
| **TP** | Opposite Asia boundary - 0.5 pip | 2R fixed |
| **Trade frequency** | ~2.6/month (ARS v1.3) | FLAGGED — unknown until implemented |
| **Complementary** | Runs independently | Requires daily direction context |

---

## 9. FLAGGED ITEMS FOR CALIBRATION

```yaml
MUST_RESOLVE_BEFORE_IMPLEMENTATION:
  1: Daily MSS detection parameters
     - Swing point lookback on daily bars
     - Displacement body_ratio threshold (0.55 proposed from STATE_DETECTION_LOGIC)
     - Minimum daily range for valid displacement
     - How far back to look for daily MSS (age limit?)

  2: Daily FVG lifecycle
     - When is a daily FVG invalidated? (close through it? opposing MSS?)
     - Multiple daily FVGs — which one is the area of interest?
     - Can price leave and re-enter a daily FVG?

  3: Dealing range boundaries
     - MSS origin candle: body_high or wick?
     - Displacement extreme candle: body_low or wick?
     - STATE_DETECTION_LOGIC says body — confirm with Olya

  4: 15m swing point detection
     - N-bar lookback for swing detection (3 proposed)
     - Minimum swing height filter
     - Lookback period for identifying prior swings to sweep

  5: MSS detection on 15m
     - What constitutes a "break" of a swing point?
     - Must it be a candle CLOSE below/above, or wick sufficient?
     - Displacement quality requirement on 15m?

  6: Daily FVG touch — precision
     - Must price be INSIDE the daily FVG zone?
     - Or is touching the edge sufficient?
     - How recent must the touch be? (Same day? Within N days?)

CAN_DEFER_TO_CALIBRATION_PHASE:
  7: Sweep extension minimum/maximum (like ARS 2-20 pip band)
  8: FVG untouched minimum (start with 0.5 pip from ARS)
  9: Trade frequency expectations
  10: NYOKZ as additional kill zone (Olya said LOKZ only for now)
  11: 5m execution TF as alternative to 15m
  12: Breakeven / risk removal mechanisms
```

---

## 10. IMPLEMENTATION PLAN (Progressive)

```yaml
phase_1_daily_direction:
  goal: "Compute daily MSS + direction from daily bars"
  verify: "Oct 1 shows BEARISH daily direction from Sept 23-24"
  deliverable: "Function that returns daily_direction for any date"

phase_2_dealing_range:
  goal: "Calculate dealing range, equilibrium, premium/discount"
  verify: "Oct 1 shows price in PREMIUM above 50% fib"
  deliverable: "Function that returns zone classification for any date"

phase_3_daily_fvg:
  goal: "Detect daily FVG, track lifecycle, arm execution trigger"
  verify: "Oct 1 shows daily FVG from Sept 23-24 is ACTIVE and price has reached it"
  deliverable: "Function that returns whether execution is armed for a date"

phase_4_15m_execution:
  goal: "Detect sweep → MSS → FVG → OTE on 15m/5m bars"
  verify: "Oct 1 reconstructs exactly: sweep 03:00, MSS 03:30, FVG 03:25, OTE 1.17645"
  deliverable: "Full trade detection for a single session"

phase_5_simulation:
  goal: "Walk-forward simulation with 2R TP, mechanical SL/TP"
  verify: "Oct 1 = WIN +2.00R at 05:50"
  deliverable: "Full backtest across 6+ months"

phase_6_calibration:
  goal: "Olya reviews trades on TradingView, calibrate parameters"
  verify: "Walk-forward validation (train/val split)"
  deliverable: "Locked parameters, canon doc updated to v1.0"
```

---

## DOCUMENT STATUS

**Version:** 0.1 DRAFT
**Status:** Shaping — Olya review required
**Machine executable:** No (flagged items must be resolved)
**Last updated:** March 28, 2026
**Reference implementation:** Not yet started

**Layer 1 (Daily direction):** Defined, needs parameter calibration
**Layer 2 (Premium/discount):** Defined, needs dealing range boundary confirmation
**Layer 3 (Daily FVG trigger):** Defined, needs lifecycle rules from Olya
**Layer 4 (Execution chain):** Defined, needs swing point + MSS detection calibration
**Flagged items:** 12 (6 must-resolve, 6 deferrable)

---

**END OF STRATEGY DOCUMENTATION — DRAFT v0.1**
