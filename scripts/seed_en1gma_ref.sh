#!/usr/bin/env bash
# Seed en1gma-ref/ — a frozen, read-only clone of SlimWojak/en1gma.
#
# en1gma-ref/ is gitignored. This script reclones it at the SHA recorded in
# docs/source_methodology/PROVENANCE.md so anyone working on cartographer
# has an authoritative reference snapshot of the upstream methodology source.
#
# Usage:
#     bash scripts/seed_en1gma_ref.sh
#     bash scripts/seed_en1gma_ref.sh --force   # overwrite existing en1gma-ref/

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="$REPO_ROOT/en1gma-ref"
PROVENANCE="$REPO_ROOT/docs/source_methodology/PROVENANCE.md"
SOURCE_REPO="git@github.com:SlimWojak/en1gma.git"

force=0
for arg in "$@"; do
    case "$arg" in
        --force) force=1 ;;
        *) echo "Unknown argument: $arg" >&2; exit 2 ;;
    esac
done

if [[ ! -f "$PROVENANCE" ]]; then
    echo "ERROR: $PROVENANCE not found" >&2
    exit 2
fi

# Extract the pinned SHA from PROVENANCE.md (looks for `Source SHA` row in the table).
SHA="$(awk -F'`' '/Source SHA/ {print $2; exit}' "$PROVENANCE")"
if [[ -z "$SHA" ]]; then
    echo "ERROR: could not extract Source SHA from $PROVENANCE" >&2
    exit 2
fi

if [[ -d "$TARGET" ]]; then
    if (( force )); then
        echo "Removing existing $TARGET"
        rm -rf "$TARGET"
    else
        echo "ERROR: $TARGET exists. Use --force to overwrite." >&2
        exit 2
    fi
fi

echo "Cloning $SOURCE_REPO at $SHA → $TARGET"
# Full clone first (so we can checkout the specific SHA), then strip .git for
# a frozen snapshot. Shallow clone wouldn't be able to resolve an arbitrary SHA.
git clone "$SOURCE_REPO" "$TARGET"
( cd "$TARGET" && git checkout --quiet "$SHA" )
rm -rf "$TARGET/.git"
touch "$TARGET/.READ_ONLY_SNAPSHOT"

echo "Done. en1gma-ref/ is a frozen snapshot at $SHA (no .git, no remotes)."
