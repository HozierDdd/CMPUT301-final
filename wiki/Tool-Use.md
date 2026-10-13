# Tool Use: how we use GitHub

Part 2 is marked on *regular and consistent use of GitHub by all team members*. This page says
what that means for us.

## Where things live

| What | Where |
|---|---|
| Product backlog | one GitHub Issue per user story + [Product-Backlog](Product-Backlog.md) summary |
| Task tracking | the **Project board** (To do / In progress / Done) with every issue on it |
| Mockups, storyboards, CRC cards | the wiki pages, images embedded from `wiki/images/` |
| Who is on the team | `doc/team.txt` and the README |
| Licence | `LICENSE` (Apache-2.0) at the repo root |

## Issues

- One issue per user story, titled `US 01.02.01 Join the waiting list for a campsite lottery`.
  Issues are created with `scripts/create_issues.sh` (needs the GitHub CLI) or by hand from the
  issue template in `.github/ISSUE_TEMPLATE/user-story.md`.
- Body: original text, our interpretation, acceptance criteria, story points, risk, halfway flag.
- Labels: `role: *`, `risk: *`, `halfway`, `optional`, `task`. Milestones: **Part 3 Halfway**, **Part 4 Final**.
- Every member is assigned at least one issue and updates its column on the board.
- Preparation work (writing this wiki) also has issues labelled `task`, so the board moves during Part 2.

## Commits and branches

- Everyone commits from their own GitHub account. Do not commit on behalf of a teammate;
  the marker checks each member's commits and wiki edits.
- Small, frequent commits with messages that say what changed: `Add owner storyboard S2`, not `update`.
- Work on a branch and open a pull request; one teammate reviews. `main` is never force-pushed.
- **No rebase, no force push on shared branches.** The course outline treats rewriting shared
  history as academic misconduct. Everyone runs once:

```bash
git config --global pull.rebase false
```

## Files that never go in the repository

`.gitignore` already excludes them; check before the first Android commit:

- `build/`, `.gradle/`, `.idea/`, `local.properties`, `*.iml`
- `google-services.json` and any Firebase or API key (Part 3)
- large binaries that are not the embedded diagrams

## AI tools

If any deliverable was produced with an AI tool, the README says which tool, for what, and a
rough share of the work. This is required by the course.

## Before the deadline (2026-10-20 17:00)

The checklist in [`CHECKLIST.md`](../CHECKLIST.md) at the repo root is what the mentor TA will
walk through.
