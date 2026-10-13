#!/usr/bin/env bash
# Mirror wiki/ (the source of truth in this repo) into the GitHub Wiki repository
# (<repo>.wiki.git) so the pages show up in the Wiki tab with the sidebar, page
# list and wiki revision history that student teams will be using.
#
# Usage:  bash scripts/sync_wiki.sh [OWNER/REPO]      (default: HozierDdd/CMPUT301-final)
# The Wiki feature must be enabled and have at least one page before the first run.
set -euo pipefail
REPO="${1:-HozierDdd/CMPUT301-final}"
SRC="$(cd "$(dirname "$0")/.." && pwd)/wiki"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

git clone -q "https://github.com/${REPO}.wiki.git" "$TMP/wiki"
cd "$TMP/wiki"
# Replace page contents; keep the wiki's own history.
find . -maxdepth 1 -name '*.md' -delete
rm -rf images
cp "$SRC"/*.md .
cp -R "$SRC/images" images
# Wiki links: GitHub wiki resolves [Page](Page) by page name, not by .md file.
sed -i '' -E 's/\]\(([A-Za-z0-9-]+)\.md\)/](\1)/g' *.md
# _Sidebar: one entry per deliverable page.
cat > _Sidebar.md <<'SB'
**Part 2 deliverables**
- [Home](Home)
- [Product Backlog](Product-Backlog)
- [UI Mockups](UI-Mockups)
- [Storyboards](Storyboards)
- [US to Screen Traceability](US-to-Screen-Traceability)
- [CRC Cards](CRC-Cards)
- [Tool Use](Tool-Use)

[Self-check](https://github.com/OWNER_REPO/blob/main/CHECKLIST.md)
SB
sed -i '' "s|OWNER_REPO|${REPO}|" _Sidebar.md
# Links from wiki pages back to repo files (../CHECKLIST.md) must be absolute in the wiki.
sed -i '' -E "s|\(\.\./CHECKLIST\.md\)|(https://github.com/${REPO}/blob/main/CHECKLIST.md)|g" *.md
git add -A
if git diff --cached --quiet; then echo "wiki already up to date"; exit 0; fi
git -c user.name="$(git -C "$SRC" config user.name)" -c user.email="$(git -C "$SRC" config user.email)" \
    commit -q -m "Sync wiki pages from main repo ($(git -C "$SRC" rev-parse --short HEAD))"
git push -q origin HEAD
echo "wiki synced: https://github.com/${REPO}/wiki"
