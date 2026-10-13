#!/usr/bin/env bash
# Render every .dot file in scripts/diagrams to <wiki clone>/images/<name>.png
# (needs graphviz: brew install graphviz).
#   bash scripts/render_diagrams.sh [WIKI_DIR]     default ../CMPUT301-final.wiki
set -euo pipefail
cd "$(dirname "$0")/.."
WIKI="${1:-${WIKI_DIR:-../CMPUT301-final.wiki}}"
[ -d "$WIKI" ] || { echo "wiki clone not found at $WIKI; git clone https://github.com/HozierDdd/CMPUT301-final.wiki.git there or pass a path" >&2; exit 1; }
mkdir -p "$WIKI/images"
for f in scripts/diagrams/*.dot; do
  layout=dot; grep -q "layout=fdp" "$f" && layout=fdp
  dot -K$layout -Tpng -Gdpi=110 "$f" -o "$WIKI/images/$(basename "${f%.dot}").png"
  echo "wrote $WIKI/images/$(basename "${f%.dot}").png"
done
