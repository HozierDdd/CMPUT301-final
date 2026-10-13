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
embedded, wiki revision history per member). The wiki is edited directly, exactly as a team
would do it. This repository holds the things a team repo also holds (README, LICENSE,
`doc/team.txt`, `.gitignore`, issue templates) plus the scripts that produced the first version
of the wiki pages and images.

| Deliverable | Where |
|---|---|
| 1. Product backlog | wiki [Product-Backlog](https://github.com/HozierDdd/CMPUT301-final/wiki/Product-Backlog), [Issues](https://github.com/HozierDdd/CMPUT301-final/issues) (#1-#66 stories, #67-#72 tasks), [Project board](https://github.com/users/HozierDdd/projects/1), [backlog/backlog.csv](backlog/backlog.csv), issue templates in [.github/ISSUE_TEMPLATE](.github/ISSUE_TEMPLATE) |
| 2. UI mockups and storyboards | wiki [UI-Mockups](https://github.com/HozierDdd/CMPUT301-final/wiki/UI-Mockups), [Storyboards](https://github.com/HozierDdd/CMPUT301-final/wiki/Storyboards), [US-to-Screen-Traceability](https://github.com/HozierDdd/CMPUT301-final/wiki/US-to-Screen-Traceability) |
| 3. CRC cards | wiki [CRC-Cards](https://github.com/HozierDdd/CMPUT301-final/wiki/CRC-Cards) |
| 4. Tool use | wiki [Tool-Use](https://github.com/HozierDdd/CMPUT301-final/wiki/Tool-Use), `.gitignore`, `LICENSE`, `doc/team.txt`, commit and wiki history |
| Self-check before submitting | [CHECKLIST.md](CHECKLIST.md) |
| TA presenter notes | [PRESENTER-GUIDE.md](PRESENTER-GUIDE.md) |

## How user stories are numbered

The [project description](https://ualberta-cmput301.github.io/projects/project_problem_descr.html)
expresses every requirement as a partial user story, "As a (role), I want (goal)", and gives each
one a number such as **US 01.02.01**. Every page, issue, diagram and CRC card in this demo refers
to requirements by that number, so it is worth reading it once:

| Part | Example | Meaning |
|---|---|---|
| `US` | | User Story |
| first group | **01** | the actor: `01` = Entrant, `02` = Campsite Owner, `03` = Administrator |
| second group | **02** | a feature group within that actor, e.g. entrant `01` = search and browse, `02` = waiting list, `03` = lottery notifications, `04` = reserving after a win |
| third group | **01** | the story's position inside the group |

So `US 01.02.01` is "As an entrant, I want to join the waiting list for a campsite lottery",
and `US 01.02.02` is the next story in the same group, leaving the waiting list.

Keep the numbers exactly as the project description has them. They are not perfectly sequential
(for example `US 02.02.02` appears after `US 02.04.02`, and there is no `US 01.03.03`); do not
renumber, or your backlog no longer matches the specification. A story ending in `-->` was added
to the description later and is treated as optional in this demo (labelled `optional`, not in the
halfway release). The description also says the stories "may change" and that new requirements
will arrive for Part 4, so the backlog has to stay maintained.

## How the wiki was first produced

The wiki is maintained by editing it directly (the Wiki tab, or a clone of
`https://github.com/HozierDdd/CMPUT301-final.wiki.git`). The scripts below produced the
initial version and are kept for reference and for re-drawing images:

```
scripts/backlog_data.py      66 user stories: points, risk, halfway, owner, screens
scripts/gen_docs.py          -> <wiki>/Product-Backlog.md, <wiki>/US-to-Screen-Traceability.md, backlog/backlog.csv, scripts/create_issues.sh
scripts/gen_mockups.py       -> <wiki>/images/M1..M18.png   (Pillow)
scripts/diagrams/*.dot       -> <wiki>/images/S1..S3, crc-collaboration, bad example (Graphviz)
scripts/gen_crc_card.py      -> <wiki>/images/crc-card-*.png
scripts/create_issues.sh     -> labels, milestones and the 72 issues (GitHub CLI)
```

`<wiki>` is a local clone of the wiki repository, by default `../CMPUT301-final.wiki` next to
this checkout (or pass a path as the first argument). Re-running a script overwrites what it
generates, so diff in the wiki clone before committing there.

Requirements: Python 3 with Pillow, Graphviz (`brew install graphviz`), GitHub CLI. Teams do
**not** need any of this; Figma, draw.io or paper plus a phone camera all produce acceptable PNGs.

## Team (fictional, for the demo)

alice, bob, chen, dana, eli, farah. See [doc/team.txt](doc/team.txt).

## AI tool disclosure

This demo was produced with Claude Code (Anthropic) under the TA's direction: roughly 80 % of
the text and all generation scripts were drafted by the model and reviewed by the TA. A team
README must carry a statement like this one if any AI tool was used.

## Licence

Apache-2.0, see [LICENSE](LICENSE).
