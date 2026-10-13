#!/usr/bin/env bash
# Render every .dot file in scripts/diagrams to wiki/images/<name>.png (needs graphviz: brew install graphviz)
set -euo pipefail
cd "$(dirname "$0")/.."
for f in scripts/diagrams/*.dot; do
  layout=dot; grep -q "layout=fdp" "$f" && layout=fdp; dot -K$layout -Tpng -Gdpi=110 "$f" -o "wiki/images/$(basename "${f%.dot}").png"
  echo "wrote wiki/images/$(basename "${f%.dot}").png"
done
