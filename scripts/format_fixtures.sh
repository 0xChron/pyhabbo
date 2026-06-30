#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FIXTURES_DIR="$ROOT/tests/fixtures"

if [[ $# -gt 0 ]]; then
  files=("$@")
else
  shopt -s nullglob
  files=("$FIXTURES_DIR"/*.json)
  shopt -u nullglob
fi

for file in "${files[@]}"; do
  tmp="${file}.tmp"
  python -m json.tool "$file" > "$tmp"
  mv "$tmp" "$file"
  echo "formatted $file"
done