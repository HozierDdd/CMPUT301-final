# Product Backlog

_Generated from `scripts/backlog_data.py` by `scripts/gen_docs.py`. Edit the data file, not this page._

**66 user stories** from the [project description](https://ualberta-cmput301.github.io/projects/project_problem_descr.html). **32 stories (85 of 166 points)** are planned for the Part 3 Halfway checkpoint (due 2026-11-06). Each story has one GitHub issue; the issue number is in the last column.

## How we estimate

Story points compare stories with each other; they are not hours. Our scale:

| Points | Meaning |
|---|---|
| 1 | a few hours, no unknowns |
| 2 | about half a day |
| 3 | one to two days |
| 5 | most of a week for one person, some unknowns |
| 8 | more than a week or depends on a technology nobody on the team has used |

Risk is **high** when the story depends on a technology nobody on the team has used (push notifications, QR scanning, device-based identity, scheduled draws) or when the requirement is still unclear; **medium** when it touches Firestore structure we have not designed yet; **low** when it is a plain screen over data we already store.

## Labels used on issues

| Label | Meaning |
|---|---|
| `role: entrant` / `role: owner` / `role: admin` | which actor the story is for |
| `risk: low` / `risk: medium` / `risk: high` | risk level |
| `halfway` | planned for Part 3 (also in the **Part 3 Halfway** milestone) |
| `optional` | story marked `-->` in the project description; low priority, not before Part 4 |
| `task` | preparation work that is not a user story (writing backlog, drawing mockups, ...) |

## Why these stories are in the halfway release

Part 3 requires about half of the requirements **and** a working Firestore connection, so the halfway set is the shortest end-to-end path through the lottery: a device-identified user registers a campsite, lists it in a lottery, entrants find it (search or QR), join the waiting list, the system draws winners, winners are notified and can confirm or decline. Reservation history, CSV export, messaging, ratings and most admin moderation come after.

## Entrant (29 stories, 16 halfway)

| US | Story | Points | Risk | Halfway | Owner | Screens | Issue |
|---|---|:-:|---|:-:|---|---|---|
| 01.01.01 | As an entrant, I want to search for campsites. | 2 | low | yes | @alice | M2, M3 | #1 |
| 01.01.02 | As an entrant, I want to filter campsites by location, date, and number of guests. | 3 | medium | yes | @alice | M2 | #2 |
| 01.01.03 | As an entrant, I want to see a list of campsites based on my filters. | 2 | low | yes | @alice | M3 | #3 |
| 01.01.04 | As an entrant, I want to see campsite summary information including name, location, maximum occupancy, and rating. | 1 | low | yes | @alice | M3 | #4 |
| 01.01.05 | As an entrant, I want to see details of a campsite. | 2 | low | yes | @alice | M4 | #5 |
| 01.01.06 | As an entrant, I want to join an active lottery from the campsite details screen. | 2 | low | yes | @bob | M4 | #6 |
| 01.02.01 | As an entrant, I want to join the waiting list for a campsite lottery. | 3 | medium | yes | @bob | M4 | #7 |
| 01.02.02 | As an entrant, I want to leave the waiting list for a campsite lottery. | 2 | low | yes | @bob | M4 | #8 |
| 01.03.01 | As an entrant, I want to receive a notification when I win the campsite lottery. | 5 | high | yes | @farah | M6 | #9 |
| 01.03.02 | As an entrant, I want to receive a notification when I lose the campsite lottery. | 3 | medium | yes | @farah | M6 | #10 |
| 01.04.01 | As an entrant, if I win the lottery, I want to see available dates that I can reserve the campsite for. | 3 | medium | yes | @bob | M7 | #11 |
| 01.04.02 | As an entrant, if I win a multiple campsite lottery, I want to choose which campsite to reserve and which dates I want. | 5 | high | no | @bob | M7 | #12 |
| 01.04.03 | As an entrant, if I win the lottery, I want to decline a reservation if I changed my mind or if none of the remaining dates work for me. | 2 | low | yes | @bob | M7 | #13 |
| 01.05.01 | As an entrant, I want to receive confirmation of my campsite reservation. | 2 | low | yes | @bob | M7, M6 | #14 |
| 01.05.02 | As an entrant, I want to receive reservation by notification or downloadable CSV. | 3 | medium | no | @bob | M8 | #15 |
| 01.06.01 | As an entrant, I want to view a list of my active reservations. | 2 | low | no | @bob | M8 | #16 |
| 01.06.02 | As an entrant, I want to view a list of my past reservations. | 1 | low | no | @bob | M8 | #17 |
| 01.07.01 | As an entrant, I want to cancel my campsite reservation. | 2 | low | no | @bob | M8 | #18 |
| 01.07.02 | As an entrant, I want to receive confirmation of my campsite cancellation by notification or downloadable CSV. | 2 | low | no | @bob | M8, M6 | #19 |
| 01.07.03 | As an entrant, I want to update my personal information, such as name, email, and phone number, on my profile. | 2 | low | yes | @farah | M9 | #20 |
| 01.08.01 | As an entrant, I want to delete my profile. | 2 | low | no | @farah | M9 | #21 |
| 01.08.02 | As an entrant, I want to add, update, or remove my profile image. _(optional)_ | 3 | medium | no | @farah | M9 | #22 |
| 01.09.01 | As an entrant, I want to be identified by my device, so that I do not have to use a username and password. | 5 | high | yes | @farah | M1 | #23 |
| 01.10.01 | As an entrant, I want to opt out of receiving notifications. | 1 | low | no | @farah | M9 | #24 |
| 01.11.01 | As an entrant, I want to see the app policy and guidelines. | 1 | low | no | @farah | M9 | #25 |
| 01.12.01 | As an entrant, I want to view campsite details by scanning the promotional QR code. | 5 | high | yes | @alice | M5, M4 | #26 |
| 01.13.01 | As an entrant, I want to give a rating for a campsite. | 2 | low | no | @alice | M4 | #27 |
| 01.13.02 | As an entrant, I want to post a review for a campsite. _(optional)_ | 2 | low | no | @alice | M4 | #28 |
| 01.14.01 | As an entrant, I want to message the campsite owner for a reservation that I have. _(optional)_ | 3 | medium | no | @dana | M8, M16 | #29 |

## Campsite owner (25 stories, 13 halfway)

| US | Story | Points | Risk | Halfway | Owner | Screens | Issue |
|---|---|:-:|---|:-:|---|---|---|
| 02.01.01 | As a campsite owner, I want to register my campsite with the app. | 3 | low | yes | @chen | M10, M11 | #30 |
| 02.01.02 | As a campsite owner, I want to provide campsite details including name, location, description (amenities), maximum occupancy, map location, optional image, and tags. | 5 | high | yes | @chen | M11 | #31 |
| 02.01.03 | As a campsite owner, I want to update details about my campsite. | 2 | low | yes | @chen | M11 | #32 |
| 02.01.04 | As a campsite owner, I want to view details of my campsite. | 1 | low | yes | @chen | M12 | #33 |
| 02.02.01 | As a campsite owner, I want the system to generate a unique QR code that links to the campsite details. | 3 | medium | yes | @chen | M12 | #34 |
| 02.03.01 | As a campsite owner, I want to view a list of my campsites. | 2 | low | yes | @chen | M10 | #35 |
| 02.04.01 | As a campsite owner, I want to list my campsite in a lottery for a certain period. | 3 | medium | yes | @dana | M13 | #36 |
| 02.04.02 | As a campsite owner, I want be able to list multiple campsites in a lottery for a certain period. | 5 | high | no | @dana | M13 | #37 |
| 02.02.02 | As a campsite owner, I want be able to list multiple campsites with other campsite owners in a lottery for a certain period. _(optional)_ | 8 | high | no | @dana | M13 | #38 |
| 02.04.03 | As a campsite owner, I want to set a registration period. | 1 | low | yes | @dana | M13 | #39 |
| 02.04.04 | As a campsite owner, I want to set a booking period. | 1 | low | yes | @dana | M13 | #40 |
| 02.04.05 | As a campsite owner, I want to set the number of lottery winners. | 1 | low | yes | @dana | M13 | #41 |
| 02.04.06 | As a campsite owner, I want to update my campsite lottery listing. | 2 | low | no | @dana | M13 | #42 |
| 02.04.07 | As a campsite owner, I want to optionally set a capacity for my lottery waitlist. | 2 | medium | no | @dana | M13 | #43 |
| 02.05.01 | As a campsite owner, I want the system to automatically draw winners after the registration period ends. | 8 | high | yes | @dana | M14 | #44 |
| 02.06.01 | As a campsite owner, I want to view the currently booked dates for my campsite. | 3 | medium | no | @chen | M12 | #45 |
| 02.07.01 | As a campsite owner, I want to view a list of active reservations. | 2 | low | no | @dana | M15 | #46 |
| 02.07.02 | As a campsite owner, I want to view a list of past reservations. | 1 | low | no | @dana | M15 | #47 |
| 02.07.03 | As a campsite owner, I want to view a list of cancelled reservations. | 1 | low | no | @dana | M15 | #48 |
| 02.08.01 | As a campsite owner, I want to reject a reservation. | 2 | low | no | @dana | M15 | #49 |
| 02.09.01 | As a campsite owner, I want to view a list of entrants who have joined the waitlist for my campsite lottery. | 2 | low | yes | @dana | M14 | #50 |
| 02.10.01 | As a campsite owner, I want to send notifications to entrants who have joined the waitlist for my campsite lottery. | 3 | medium | yes | @farah | M14 | #51 |
| 02.10.02 | As a campsite owner, I want to view a list of all notifications I have sent. | 2 | low | no | @farah | M14 | #52 |
| 02.11.01 | As a campsite owner, I want entrants to confirm that they have read the campsite rules and policies before confirming their reservation. | 2 | low | no | @bob | M7 | #53 |
| 02.12.01 | As a campsite owner, I want to message a user who is reserving my campsite. | 3 | medium | no | @dana | M15, M16 | #54 |

## Admin (12 stories, 3 halfway)

| US | Story | Points | Risk | Halfway | Owner | Screens | Issue |
|---|---|:-:|---|:-:|---|---|---|
| 03.01.01 | As an admin, I want to remove registered campsites. | 2 | low | yes | @eli | M17 | #55 |
| 03.02.01 | As an admin, I want to remove profiles. | 2 | low | no | @eli | M17 | #56 |
| 03.03.01 | As an admin, I want to remove images. | 2 | medium | no | @eli | M17 | #57 |
| 03.04.01 | As an admin, I want to browse campsites. | 2 | low | yes | @eli | M17 | #58 |
| 03.05.01 | As an admin, I want to browse profiles. | 2 | low | no | @eli | M17 | #59 |
| 03.06.01 | As an admin, I want to browse uploaded images so I can remove them if necessary. | 3 | medium | no | @eli | M17 | #60 |
| 03.07.01 | As an admin, I want to remove campsite owners that violate app policy. | 2 | low | no | @eli | M17 | #61 |
| 03.08.01 | As an admin, I want to review logs of all notifications. | 3 | medium | no | @eli | M18 | #62 |
| 03.09.01 | As an admin, I want to remove campsite ratings that violate app policy. _(optional)_ | 1 | low | no | @eli | M17 | #63 |
| 03.10.01 | As an admin, I want to remove campsite reviews that violate app policy. _(optional)_ | 1 | low | no | @eli | M17 | #64 |
| 03.11.01 | As an admin, I should be able to be a campsite owner and/or entrant with my admin profile. | 2 | medium | yes | @farah | M1 | #65 |
| 03.12.01 | As an admin, I want to review logs of all messages from campsite owners to entrants who reserved their campsite. | 3 | medium | no | @eli | M18 | #66 |

## Preparation tasks (also on the board, label `task`)

| Issue | Task | Owner |
|---|---|---|
| #67 | Write product backlog summary page | @alice |
| #68 | Create one issue per user story with labels | @bob |
| #69 | Draw entrant and shared screens | @chen |
| #70 | Draw owner and admin screens, storyboards | @dana |
| #71 | Write CRC cards and check collaborators both ways | @eli |
| #72 | Set up wiki home, README, .gitignore, project board | @farah |

## Per-member load

| Member | Role in Part 2 | Issues | Points | Halfway points |
|---|---|:-:|:-:|:-:|
| @alice | Backlog owner (entrant search & browse) | 8 | 19 | 15 |
| @bob | Backlog owner (entrant lottery & reservations) | 13 | 31 | 14 |
| @chen | Mockup owner (campsite owner screens) | 7 | 19 | 16 |
| @dana | Mockup owner (lottery & reservation screens) | 16 | 45 | 16 |
| @eli | CRC owner (admin stories) | 11 | 23 | 4 |
| @farah | Wiki & tool-use owner (auth, profile, notifications) | 11 | 29 | 20 |
