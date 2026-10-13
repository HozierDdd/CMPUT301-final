# Part 2 presenter guide (mentor TA)

Use this repository to walk Atomic and Symbol (Tue Oct 13) and Gambit (Wed Oct 14) through
the Part 2 deliverables. About 20 minutes, then go through `CHECKLIST.md` against each team's
own repository.

Due: Tuesday 2026-10-20 17:00. Peer review form: 2026-10-21 17:00, every member individually.
Marks: 0 / 2 / 3 / 4 / 5, no part marks.

## 0. Opening (1 min)

Open the repository's **Wiki tab** (https://github.com/HozierDdd/CMPUT301-final/wiki). This is
the form the course expects. Three sentences:

- Part 2 has no code. Four deliverables: backlog, mockups + storyboards, CRC cards, GitHub use.
- Everything lives in the team repo's wiki; images are embedded, not linked to Figma.
- Marking rewards **consistency**: the same US number on every page, the same name for the same concept.

Point at the role table and the "vocabulary we use everywhere" block on Home; teams can copy the structure.

## 1. Product backlog (5 min)

Open the wiki page **Product Backlog**.

- Top of page: 66 stories, 32 halfway, the story-point scale in one sentence. The scale must be
  written down; the numbers themselves are not marked.
- Table: one row per US with number / text / points / risk / halfway / owner / screens / issue.
  Show the 6 stories marked `-->` labelled optional and kept out of halfway.
- "Why these stories are in the halfway release": Part 3 needs the full lottery path plus
  Firestore, so the halfway set is device login, register campsite, create lottery, search or
  scan, join waiting list, automatic draw, notification, confirm or decline.
- Open `.github/ISSUE_TEMPLATE/user-story.md`: the five things every issue must contain.
  Then the Issues page filtered by label to show the scheme: `role:*`, `risk:*`, `halfway`,
  `optional`, `task`. Then the project board (https://github.com/users/HozierDdd/projects/1):
  stories in Todo, preparation tasks already in Done.
- Common mistakes: only the 30 entrant stories; risk written as a number; several stories merged
  into one issue; an empty board.

Exercise: name a random US (for example 02.04.07) and have the team find it in their own issues.

## 2. Mockups and storyboards (6 min)

Open the wiki page **UI Mockups**, scroll to M4 (campsite details) and M7 (won: choose dates).

- Under every image: what the red numbered markers point at, and the list of US covered.
  Low fidelity is enough; what matters is which controls exist and where.
- M4 markers 5 and 6: both the Join and the Leave state are drawn. A mockup is documentation,
  not a screenshot.

Open the wiki page **Storyboards**:

- S1: boxes are screens with their M id and US numbers; **every arrow carries the action**
  ("taps 'Join waiting list'"). Point at "registration closes; system draws winners": system
  events are transitions too and must be drawn.
- S2, the yellow note: the draw is automatic, not a button the owner presses.
- Scroll to the bad example at the bottom: no ids, no US, no arrow labels. The most common
  reason to lose marks on this deliverable.

Open the wiki page **US to Screen Traceability**: all 66 stories have at least one screen and
one storyboard; the last line says "Stories with no screen: 0". This table is the cheapest way
to earn the "convincingly show all requirements are covered" point.

## 3. CRC cards (5 min)

Open the wiki page **CRC Cards**.

- Start with the Lottery card PNG: responsibilities are actions ("draw N winners at random when
  the registration period ends"), collaborators are domain classes.
- Then the bad example: a field list, with FirebaseFirestore and a ViewModel as collaborators.
  No UI classes, no database classes in Part 2.
- The collaboration graph: every line must be on both cards. Tell teams to check theirs the same way.
- The note under WaitingList: the waiting list is the lottery pool, not a stand-by list for a
  full campsite. All three teams may have this wrong; ask explicitly.
- Mention that these cards become the Part 3 UML class diagram; thinking now saves work later.

## 4. Tool use (2 min)

Open the wiki page **Tool Use**:

- Everyone commits from their own account; the TA checks commits and wiki edits per member.
- No rebase, no force push; `git config --global pull.rebase false`.
- `.gitignore` now, so `google-services.json` never enters the repo in Part 3.
- AI use must be declared in the README (the last section of this repo's README is the example).

## 5. Closing (1 min)

Open `CHECKLIST.md` and say this is what next week's check follows. Run the ten-second test:
name a random US and have one member point to the issue, the button on the screen and the
responsible class within ten seconds.

Also check this week (from the Oct 6 plan): first version of the backlog in issues; mockup tool
chosen; CRC draft exists; every member assigned at least one issue; take attendance.

## Notes

- Issues (#1-#66 stories, #67-#72 preparation tasks) and the board are already set up. When
  talking about the backlog, open the Issues page filtered by label, then the board's Todo and
  Done columns.
- The wiki is edited directly on GitHub (or clone `CMPUT301-final.wiki.git`, edit, push). The
  main repository keeps no copy of the pages.
- If asked "how many screens": the M1-M18 list, the main screens and dialogs for all three
  roles, is about 18; fewer than 10 rarely covers 66 stories.
- If asked how to estimate story points: accuracy is not marked; having a written scale and
  using it consistently is.
