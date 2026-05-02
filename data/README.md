# Cartographer data

Single-file snapshot of EURUSD market data, frozen for the lab.

## File

`cartographer.duckdb` (≈220 MB) — DuckDB v1.5.1 database.

## Provenance

| Field | Value |
| --- | --- |
| Source | `~/phoenix-river/EURUSD/` (River pipeline) |
| Snapshot date | 2026-05-02 |
| Source parquet count | 1,421 daily files |
| Date range | 2020-11-23 → 2026-04-30 |
| Native timeframe | 1-minute OHLCV |
| Data provider observed | dukascopy |
| Total 1m bars | 2,004,516 |
| Total session days | 1,682 |

The snapshot is **frozen**. River continues to receive live ticks; cartographer
does not. To refresh, re-run the build script (to be authored by the V0 mission)
which re-reads `~/phoenix-river/EURUSD/**/*.parquet` and rebuilds the file from
scratch.

## Schema

### Table `bars_1m`

Native 1-minute OHLCV bars.

| Column | Type | Notes |
| --- | --- | --- |
| `timestamp` | `TIMESTAMP WITH TIME ZONE` | UTC |
| `open` | `DOUBLE` | |
| `high` | `DOUBLE` | |
| `low` | `DOUBLE` | |
| `close` | `DOUBLE` | |
| `volume` | `DOUBLE` | |
| `source` | `VARCHAR` | data provider, e.g. `dukascopy` |
| `knowledge_time` | `TIMESTAMP WITH TIME ZONE` | when the bar was first observed by River |
| `bar_hash` | `VARCHAR` | content hash from upstream |
| `bar_date` | `DATE` | derived; UTC calendar date of `timestamp` |

Indexes: `idx_bars_1m_date(bar_date)`, `idx_bars_1m_ts(timestamp)`.

### View `bars_daily`

Pre-aggregated daily OHLCV (UTC sessions). Cheap convenience for HTF scans;
the source of truth is `bars_1m`.

| Column | Type | Notes |
| --- | --- | --- |
| `date` | `DATE` | UTC calendar date |
| `open` | `DOUBLE` | first 1m open of the day |
| `high` | `DOUBLE` | session high |
| `low` | `DOUBLE` | session low |
| `close` | `DOUBLE` | last 1m close of the day |
| `volume` | `DOUBLE` | session sum |
| `minute_bar_count` | `BIGINT` | sanity check (typical FX session ≈1,440) |
| `session_start` | `TIMESTAMP` | first 1m timestamp |
| `session_end` | `TIMESTAMP` | last 1m timestamp |

> **HTF mission note:** the V0 mission will need to derive H4 / H1 windows
> from `bars_1m`. The Daily view is provided pre-built; do **not** assume the
> cartographer's HTF logic should match en1gma's session boundaries unless the
> methodology docs say so. Verify against `docs/source_methodology/methodology/`.

### Table `meta`

Provenance key/value table — also surfaces source SHA, snapshot date, etc. Read
on startup to confirm the snapshot the agent is working against.

## Access pattern

Open with any DuckDB client:

```bash
duckdb /Users/a8ra_m3/cartographer/data/cartographer.duckdb
```

Or in Python:

```python
import duckdb
con = duckdb.connect("/Users/a8ra_m3/cartographer/data/cartographer.duckdb",
                    read_only=True)
con.execute("SELECT * FROM bars_daily WHERE date >= '2026-01-01' LIMIT 5").fetchall()
```

**Cartographer must open the DB read-only** (`read_only=True`). Writing scenes
goes to `scene_bank/`, not back into the DuckDB.
