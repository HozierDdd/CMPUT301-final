# CMPUT 301 F26 — Project Part 2 demo repository

A complete, worked example of the **Part 2 (Preparation)** deliverables for the Campsite
Reservation System project, built by the mentor TA (hanzhen3) to walk teams through what a
submission should look like. It is not a template to copy; it is a reference for
*shape, level of detail and consistency*.

Official spec: <https://ualberta-cmput301.github.io/projects/project_part2.html>
Project description: <https://ualberta-cmput301.github.io/projects/project_problem_descr.html>

## Start here

Open the **[Wiki tab](https://github.com/HozierDdd/CMPUT301-final/wiki)**: that is what a
team's submission should look like (home page, sidebar, one page per deliverable, images
embedded, wiki revision history per member). The same pages are kept as source under `wiki/`
in this repository and mirrored into the Wiki with `scripts/sync_wiki.sh`, so they can be
regenerated from the data file and still be shown in the form the course expects.

| Deliverable | Where |
|---|---|
| 1. Product backlog | [wiki/Product-Backlog.md](wiki/Product-Backlog.md), [backlog/backlog.csv](backlog/backlog.csv), issue template in [.github/ISSUE_TEMPLATE](.github/ISSUE_TEMPLATE), `scripts/create_issues.sh` |
| 2. UI mockups and storyboards | [wiki/UI-Mockups.md](wiki/UI-Mockups.md), [wiki/Storyboards.md](wiki/Storyboards.md), [wiki/US-to-Screen-Traceability.md](wiki/US-to-Screen-Traceability.md) |
| 3. CRC cards | [wiki/CRC-Cards.md](wiki/CRC-Cards.md) |
| 4. Tool use | [wiki/Tool-Use.md](wiki/Tool-Use.md), `.gitignore`, `LICENSE`, `doc/team.txt` |
| Self-check before submitting | [CHECKLIST.md](CHECKLIST.md) |
| TA presenter notes (中文) | [PRESENTER-GUIDE.md](PRESENTER-GUIDE.md) |

## How the demo is built

Everything derives from one data file so the numbers can never disagree:

```
scripts/backlog_data.py      66 user stories: points, risk, halfway, owner, screens
scripts/gen_docs.py          -> wiki/Product-Backlog.md, US-to-Screen-Traceability.md, backlog.csv, create_issues.sh
scripts/gen_mockups.py       -> wiki/images/M1..M18.png   (Pillow)
scripts/diagrams/*.dot       -> wiki/images/S1..S3, crc-collaboration, bad example (Graphviz)
scripts/gen_crc_card.py      -> wiki/images/crc-card-*.png
scripts/sync_wiki.sh         -> pushes wiki/ into the GitHub Wiki (<repo>.wiki.git) with a _Sidebar
```

Regenerate after editing the data file:

```bash
python3 scripts/gen_docs.py && python3 scripts/gen_mockups.py && python3 scripts/gen_crc_card.py && bash scripts/render_diagrams.sh && bash scripts/sync_wiki.sh
```

Requirements: Python 3 with Pillow, Graphviz (`brew install graphviz`). Teams do **not** need
any of this; Figma, draw.io or paper plus a phone camera all produce acceptable PNGs.

## Team (fictional, for the demo)

alice, bob, chen, dana, eli, farah. See [doc/team.txt](doc/team.txt).

## AI tool disclosure

This demo was produced with Claude Code (Anthropic) under the TA's direction: roughly 80 % of
the text and all generation scripts were drafted by the model and reviewed by the TA. A team
README must carry a statement like this one if any AI tool was used.

## Licence

Apache-2.0, see [LICENSE](LICENSE).
