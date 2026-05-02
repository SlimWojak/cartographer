#!/usr/bin/env python3
"""
Build data/cartographer.duckdb from ~/phoenix-river/EURUSD/.

The DuckDB snapshot is gitignored — this script regenerates it from the
upstream phoenix-river parquet tree on M3.

Usage:
    python scripts/seed_data.py                  # default: ~/phoenix-river/EURUSD
    python scripts/seed_data.py --source <path>  # explicit source root
    python scripts/seed_data.py --force          # overwrite existing DB

Requires: duckdb, pyarrow (any recent versions).
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = Path.home() / "phoenix-river" / "EURUSD"
DB_PATH = REPO_ROOT / "data" / "cartographer.duckdb"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help=f"phoenix-river EURUSD root (default: {DEFAULT_SOURCE})",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="overwrite existing data/cartographer.duckdb",
    )
    args = parser.parse_args()

    try:
        import duckdb  # type: ignore
    except ImportError:
        print("ERROR: duckdb not installed. Try: pip install duckdb", file=sys.stderr)
        return 2

    source: Path = args.source
    if not source.is_dir():
        print(f"ERROR: source not found: {source}", file=sys.stderr)
        print(
            "  This script expects M3-local phoenix-river data. On a machine "
            "without it, copy the .duckdb file in directly.",
            file=sys.stderr,
        )
        return 2

    if DB_PATH.exists() and not args.force:
        print(f"ERROR: {DB_PATH} exists. Use --force to overwrite.", file=sys.stderr)
        return 2

    if DB_PATH.exists():
        DB_PATH.unlink()
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    glob = str(source / "*" / "*" / "*.parquet")
    snapshot_date = time.strftime("%Y-%m-%d")

    print(f"Building {DB_PATH}")
    print(f"  source: {source}")
    print(f"  glob:   {glob}")

    t0 = time.time()
    con = duckdb.connect(str(DB_PATH))

    con.execute(
        f"""
        CREATE TABLE bars_1m AS
        SELECT
            timestamp,
            open, high, low, close, volume,
            source,
            knowledge_time,
            bar_hash,
            CAST(timestamp AS DATE) AS bar_date
        FROM read_parquet('{glob}', hive_partitioning=false)
        """
    )
    con.execute("CREATE INDEX idx_bars_1m_date ON bars_1m(bar_date)")
    con.execute("CREATE INDEX idx_bars_1m_ts ON bars_1m(timestamp)")
    con.execute(
        """
        CREATE VIEW bars_daily AS
        SELECT
            bar_date AS date,
            FIRST(open ORDER BY timestamp) AS open,
            MAX(high) AS high,
            MIN(low) AS low,
            LAST(close ORDER BY timestamp) AS close,
            SUM(volume) AS volume,
            COUNT(*) AS minute_bar_count,
            MIN(timestamp) AS session_start,
            MAX(timestamp) AS session_end
        FROM bars_1m
        GROUP BY bar_date
        """
    )
    con.execute(
        """
        CREATE TABLE meta (
            key VARCHAR PRIMARY KEY,
            value VARCHAR
        )
        """
    )

    parquet_count = con.execute(
        f"SELECT COUNT(DISTINCT filename) FROM read_parquet('{glob}', filename=true)"
    ).fetchone()[0]
    row_count = con.execute("SELECT COUNT(*) FROM bars_1m").fetchone()[0]
    daily_count = con.execute("SELECT COUNT(*) FROM bars_daily").fetchone()[0]
    date_min, date_max = con.execute(
        "SELECT MIN(bar_date), MAX(bar_date) FROM bars_1m"
    ).fetchone()

    meta_rows = [
        ("source_root", str(source)),
        ("snapshot_date", snapshot_date),
        ("parquet_file_count", str(parquet_count)),
        ("bars_1m_row_count", str(row_count)),
        ("bars_daily_row_count", str(daily_count)),
        ("date_range_start", str(date_min)),
        ("date_range_end", str(date_max)),
        ("instrument", "EURUSD"),
        ("timeframe_native", "1m"),
        ("source_pipeline", "phoenix-river"),
        ("data_provider_observed", "dukascopy"),
        (
            "note",
            "snapshot is frozen — refresh by re-running scripts/seed_data.py --force",
        ),
    ]
    con.executemany("INSERT INTO meta VALUES (?, ?)", meta_rows)
    con.close()

    elapsed = time.time() - t0
    size_mb = DB_PATH.stat().st_size / 1024 / 1024
    print(f"BUILT: {DB_PATH}")
    print(f"  elapsed:        {elapsed:.1f}s")
    print(f"  size:           {size_mb:.1f} MB")
    print(f"  parquets read:  {parquet_count}")
    print(f"  bars_1m rows:   {row_count:,}")
    print(f"  bars_daily:     {daily_count}")
    print(f"  date range:     {date_min} → {date_max}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
