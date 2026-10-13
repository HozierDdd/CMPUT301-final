# Part 2 self-check (what the mentor TA will look at on 2026-10-20)

Marking is 0 / 2 / 3 / 4 / 5 with no part marks. A **5** means every box below is ticked and the
three deliverables agree with each other. Missing one whole deliverable is a 0 or 2.

## Product backlog
- [ ] One GitHub issue per user story (66 in the current project description), none combined.
- [ ] Each issue: US number, original text, your interpretation, acceptance criteria, story points, risk (low/medium/high).
- [ ] Halfway stories marked (label or milestone); about half, and the full lottery path is inside.
- [ ] Project board exists, every issue is on it, preparation tasks have moved to Done.
- [ ] Every member is assigned at least one issue.
- [ ] Wiki summary table matches the issues exactly (numbers, points, risk).
- [ ] Story-point scale written in one sentence at the top of the page.

## UI mockups and storyboards
- [ ] Every main screen and major dialog for all three roles is drawn.
- [ ] Each image has comments on the important elements and lists the US numbers it covers.
- [ ] At least three storyboards (entrant, owner, admin); **every arrow has an action label**.
- [ ] A US-to-screen table shows every story on at least one screen.
- [ ] Images are PNG embedded in the wiki, readable without zooming, no external links.
- [ ] Names on screens match the backlog and CRC cards (Waiting List, Lottery, Reservation).

## CRC cards
- [ ] One card per important domain class; no Android or Firebase classes.
- [ ] Responsibilities are actions, not field lists.
- [ ] Collaborators match in both directions; every collaborator has its own card.
- [ ] Parent class noted where there is one (User).
- [ ] Every user story is supported by at least one class.

## Tool use
- [ ] Wiki home links to each deliverable page and lists who owns what.
- [ ] Every member has commits or wiki edits from their own account.
- [ ] No rebase / force push on shared branches; `pull.rebase false` set.
- [ ] `.gitignore` excludes build/, .idea/, local.properties, google-services.json.
- [ ] README has team name, members, wiki link, and the AI-use statement.
- [ ] LICENSE and doc/team.txt from Part 1 still in place.

## Ten-second test
Pick any US at random (for example 01.04.03). A team member should be able to point to its
issue, the screen and button that implements it, and the class responsible, within ten seconds.
