#!/usr/bin/env python3
"""Generate the backlog table, the traceability table, the CSV export and the
issue-creation script from scripts/backlog_data.py.  Run from the repo root:

    python3 scripts/gen_docs.py
"""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import backlog_data as b  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")


def w(path, text):
    with open(os.path.join(ROOT, path), "w") as f:
        f.write(text)
    print("wrote", path)


def flag(x):
    return "yes" if x else "no"


# ---------------------------------------------------------------- backlog page
def backlog_page():
    total = len(b.STORIES)
    half = [s for s in b.STORIES if s[4]]
    pts = sum(s[2] for s in b.STORIES)
    hpts = sum(s[2] for s in half)
    out = []
    out.append("# Product Backlog\n")
    out.append("_Generated from `scripts/backlog_data.py` by `scripts/gen_docs.py`. "
               "Edit the data file, not this page._\n")
    out.append(f"**{total} user stories** from the "
               "[project description](https://ualberta-cmput301.github.io/projects/project_problem_descr.html). "
               f"**{len(half)} stories ({hpts} of {pts} points)** are planned for the "
               "Part 3 Halfway checkpoint (due 2026-11-06). "
               "Each story has one GitHub issue; the issue number is in the last column.\n")
    out.append("## How we estimate\n")
    out.append("Story points compare stories with each other; they are not hours. Our scale:\n")
    out.append("| Points | Meaning |\n|---|---|")
    for k, v in b.SCALE.items():
        out.append(f"| {k} | {v} |")
    out.append("\nRisk is **high** when the story depends on a technology nobody on the team has used "
               "(push notifications, QR scanning, device-based identity, scheduled draws) or when the "
               "requirement is still unclear; **medium** when it touches Firestore structure we have not "
               "designed yet; **low** when it is a plain screen over data we already store.\n")
    out.append("## Labels used on issues\n")
    out.append("| Label | Meaning |\n|---|---|\n"
               "| `role: entrant` / `role: owner` / `role: admin` | which actor the story is for |\n"
               "| `risk: low` / `risk: medium` / `risk: high` | risk level |\n"
               "| `halfway` | planned for Part 3 (also in the **Part 3 Halfway** milestone) |\n"
               "| `optional` | story marked `-->` in the project description; low priority, not before Part 4 |\n"
               "| `task` | preparation work that is not a user story (writing backlog, drawing mockups, ...) |\n")
    out.append("## Why these stories are in the halfway release\n")
    out.append("Part 3 requires about half of the requirements **and** a working Firestore connection, "
               "so the halfway set is the shortest end-to-end path through the lottery: a device-identified "
               "user registers a campsite, lists it in a lottery, entrants find it (search or QR), join the "
               "waiting list, the system draws winners, winners are notified and can confirm or decline. "
               "Reservation history, CSV export, messaging, ratings and most admin moderation come after.\n")
    for role, title in (("01", "Entrant"), ("02", "Campsite owner"), ("03", "Admin")):
        rows = [s for s in b.STORIES if s[0].startswith(role)]
        out.append(f"## {title} ({len(rows)} stories, {sum(1 for s in rows if s[4])} halfway)\n")
        out.append("| US | Story | Points | Risk | Halfway | Owner | Screens | Issue |")
        out.append("|---|---|:-:|---|:-:|---|---|---|")
        for us, story, p, r, h, a, scr in rows:
            opt = " _(optional)_" if b.is_optional(story) else ""
            text = story.replace(" -->", "")
            n = b.issue_number(us)
            out.append(f"| {us} | {text}{opt} | {p} | {r} | {flag(h)} | @{a} | {', '.join(scr)} | #{n} |")
        out.append("")
    out.append("## Preparation tasks (also on the board, label `task`)\n")
    out.append("| Issue | Task | Owner |\n|---|---|---|")
    for i, (t, a) in enumerate(b.TASKS, start=len(b.STORIES) + 1):
        out.append(f"| #{i} | {t} | @{a} |")
    out.append("")
    out.append("## Per-member load\n")
    out.append("| Member | Role in Part 2 | Issues | Points | Halfway points |\n|---|---|:-:|:-:|:-:|")
    for m, role in b.TEAM.items():
        mine = [s for s in b.STORIES if s[5] == m]
        out.append(f"| @{m} | {role} | {len(mine)} | {sum(s[2] for s in mine)} | {sum(s[2] for s in mine if s[4])} |")
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------- traceability page
def trace_page():
    out = []
    out.append("# User Story to Screen Traceability\n")
    out.append("_Generated from `scripts/backlog_data.py`. This table is how we show that "
               "**every** requirement is covered by at least one mockup and one storyboard._\n")
    out.append("Mockup ids (M1...M18) are defined on [UI Mockups](UI-Mockups.md); storyboard ids "
               "(S1...S3) on [Storyboards](Storyboards.md).\n")
    # which storyboard contains which screen
    sb_of = {}
    for sid, (_, screens) in b.STORYBOARDS.items():
        for m in screens:
            sb_of.setdefault(m, []).append(sid)
    out.append("| US | Story (short) | Mockups | Storyboards |\n|---|---|---|---|")
    for us, story, p, r, h, a, scr in b.STORIES:
        short = b.short_title(story)
        sbs = sorted({s for m in scr for s in sb_of.get(m, [])})
        out.append(f"| {us} | {short} | {', '.join(scr)} | {', '.join(sbs) or '-'} |")
    out.append("")
    # reverse table
    out.append("## Reverse view: what each screen covers\n")
    out.append("| Screen | Name | User stories |\n|---|---|---|")
    for mid, name in b.SCREENS.items():
        uss = [s[0] for s in b.STORIES if mid in s[6]]
        out.append(f"| {mid} | {name} | {', '.join(uss)} |")
    out.append("")
    missing = [s[0] for s in b.STORIES if not s[6]]
    out.append(f"**Stories with no screen: {len(missing)}.** "
               "(If this number is not zero, the mockups are incomplete.)\n")
    return "\n".join(out)


# ------------------------------------------------------------------------ csv
def csv_export():
    path = os.path.join(ROOT, "backlog", "backlog.csv")
    with open(path, "w", newline="") as f:
        cw = csv.writer(f)
        cw.writerow(["issue", "us", "role", "story", "points", "risk", "halfway", "optional", "assignee", "screens"])
        for us, story, p, r, h, a, scr in b.STORIES:
            cw.writerow([b.issue_number(us), us, b.role_of(us), story.replace(" -->", ""), p, r,
                         flag(h), flag(b.is_optional(story)), a, " ".join(scr)])
    print("wrote backlog/backlog.csv")


# ------------------------------------------------------------- issue script
def issues_script():
    out = ["#!/usr/bin/env bash",
           "# Create labels, the halfway milestone and one issue per user story with the GitHub CLI.",
           "# Generated by scripts/gen_docs.py from scripts/backlog_data.py.",
           "#",
           "# Usage (inside a clone of the team repo, after `gh auth login`):",
           "#   bash scripts/create_issues.sh OWNER/REPO",
           "# Issues are created in document order so that issue numbers match the wiki table",
           "# ONLY if the repository has no issues yet.",
           "set -euo pipefail",
           'REPO="${1:?usage: create_issues.sh OWNER/REPO}"',
           "",
           "label() { gh label create \"$1\" --repo \"$REPO\" --color \"$2\" --description \"$3\" --force >/dev/null; }",
           'label "role: entrant" 1D76DB "story for the entrant actor"',
           'label "role: owner"   0E8A16 "story for the campsite owner actor"',
           'label "role: admin"   5319E7 "story for the admin actor"',
           'label "risk: low"     C2E0C6 "low risk"',
           'label "risk: medium"  FBCA04 "medium risk"',
           'label "risk: high"    D93F0B "high risk"',
           'label "halfway"       0052CC "planned for Part 3 Halfway (2026-11-06)"',
           'label "optional"      BFD4F2 "marked --> in the project description"',
           'label "task"          EDEDED "preparation work, not a user story"',
           "",
           "gh api -X POST \"repos/$REPO/milestones\" -f title='Part 3 Halfway' -f due_on='2026-11-06T23:59:00Z' >/dev/null 2>&1 || true",
           "gh api -X POST \"repos/$REPO/milestones\" -f title='Part 4 Final'   -f due_on='2026-11-30T23:59:00Z' >/dev/null 2>&1 || true",
           ""]
    for us, story, p, r, h, a, scr in b.STORIES:
        text = story.replace(" -->", "")
        short = b.short_title(story)
        labels = [f"role: {b.role_of(us)}", f"risk: {r}"]
        if h:
            labels.append("halfway")
        if b.is_optional(story):
            labels.append("optional")
        body = (f"**User story (from the project description)**\\n\\n> US {us} {text}\\n\\n"
                f"**Our interpretation**\\n\\n_(write one or two sentences in your own words)_\\n\\n"
                f"**Acceptance criteria**\\n\\n- [ ] ...\\n- [ ] ...\\n\\n"
                f"**Story points:** {p}  \\n**Risk:** {r}  \\n**Halfway:** {'yes' if h else 'no'}  \\n"
                f"**Screens:** {', '.join(scr)}")
        ms = " --milestone 'Part 3 Halfway'" if h else ""
        out.append(f"gh issue create --repo \"$REPO\" --title \"US {us} {short}\" "
                   f"--label \"{','.join(labels)}\"{ms} --body \"$(printf '{body}')\"")
    out.append("")
    for t, a in b.TASKS:
        out.append(f"gh issue create --repo \"$REPO\" --title \"{t}\" --label task --body 'Part 2 preparation task.'")
    out.append("")
    out.append('echo "done: $(gh issue list --repo "$REPO" --limit 200 --state all | wc -l) issues"')
    w("scripts/create_issues.sh", "\n".join(out) + "\n")


if __name__ == "__main__":
    w("wiki/Product-Backlog.md", backlog_page())
    w("wiki/US-to-Screen-Traceability.md", trace_page())
    csv_export()
    issues_script()
