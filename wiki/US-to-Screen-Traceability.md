# User Story to Screen Traceability

_Generated from `scripts/backlog_data.py`. This table is how we show that **every** requirement is covered by at least one mockup and one storyboard._

Mockup ids (M1...M18) are defined on [UI Mockups](UI-Mockups.md); storyboard ids (S1...S3) on [Storyboards](Storyboards.md).

| US | Story (short) | Mockups | Storyboards |
|---|---|---|---|
| 01.01.01 | Search for campsites | M2, M3 | S1 |
| 01.01.02 | Filter campsites by location, date, and number of guests | M2 | S1 |
| 01.01.03 | See a list of campsites based on my filters | M3 | S1 |
| 01.01.04 | See campsite summary information including name, location, maximum occupancy, and rating | M3 | S1 |
| 01.01.05 | See details of a campsite | M4 | S1 |
| 01.01.06 | Join an active lottery from the campsite details screen | M4 | S1 |
| 01.02.01 | Join the waiting list for a campsite lottery | M4 | S1 |
| 01.02.02 | Leave the waiting list for a campsite lottery | M4 | S1 |
| 01.03.01 | Receive a notification when I win the campsite lottery | M6 | S1 |
| 01.03.02 | Receive a notification when I lose the campsite lottery | M6 | S1 |
| 01.04.01 | See available dates that I can reserve the campsite for | M7 | S1 |
| 01.04.02 | Choose which campsite to reserve and which dates I want | M7 | S1 |
| 01.04.03 | Decline a reservation if I changed my mind or if none of the remaining dates work for me | M7 | S1 |
| 01.05.01 | Receive confirmation of my campsite reservation | M7, M6 | S1 |
| 01.05.02 | Receive reservation by notification or downloadable CSV | M8 | S1 |
| 01.06.01 | View a list of my active reservations | M8 | S1 |
| 01.06.02 | View a list of my past reservations | M8 | S1 |
| 01.07.01 | Cancel my campsite reservation | M8 | S1 |
| 01.07.02 | Receive confirmation of my campsite cancellation by notification or downloadable CSV | M8, M6 | S1 |
| 01.07.03 | Update my personal information, such as name, email, and phone number, on my profile | M9 | - |
| 01.08.01 | Delete my profile | M9 | - |
| 01.08.02 | Add, update, or remove my profile image | M9 | - |
| 01.09.01 | Be identified by my device, so that I do not have to use a username and password | M1 | S1, S3 |
| 01.10.01 | Opt out of receiving notifications | M9 | - |
| 01.11.01 | See the app policy and guidelines | M9 | - |
| 01.12.01 | View campsite details by scanning the promotional QR code | M5, M4 | S1 |
| 01.13.01 | Give a rating for a campsite | M4 | S1 |
| 01.13.02 | Post a review for a campsite | M4 | S1 |
| 01.14.01 | Message the campsite owner for a reservation that I have | M8, M16 | S1, S2 |
| 02.01.01 | Register my campsite with the app | M10, M11 | S2 |
| 02.01.02 | Provide campsite details including name, location, description (amenities), maximum occupancy, map location, optional image, and tags | M11 | S2 |
| 02.01.03 | Update details about my campsite | M11 | S2 |
| 02.01.04 | View details of my campsite | M12 | S2 |
| 02.02.01 | The system to generate a unique QR code that links to the campsite details | M12 | S2 |
| 02.03.01 | View a list of my campsites | M10 | S2 |
| 02.04.01 | List my campsite in a lottery for a certain period | M13 | S2 |
| 02.04.02 | List multiple campsites in a lottery for a certain period | M13 | S2 |
| 02.02.02 | List multiple campsites with other campsite owners in a lottery for a certain period | M13 | S2 |
| 02.04.03 | Set a registration period | M13 | S2 |
| 02.04.04 | Set a booking period | M13 | S2 |
| 02.04.05 | Set the number of lottery winners | M13 | S2 |
| 02.04.06 | Update my campsite lottery listing | M13 | S2 |
| 02.04.07 | Optionally set a capacity for my lottery waitlist | M13 | S2 |
| 02.05.01 | The system to automatically draw winners after the registration period ends | M14 | S2 |
| 02.06.01 | View the currently booked dates for my campsite | M12 | S2 |
| 02.07.01 | View a list of active reservations | M15 | S2 |
| 02.07.02 | View a list of past reservations | M15 | S2 |
| 02.07.03 | View a list of cancelled reservations | M15 | S2 |
| 02.08.01 | Reject a reservation | M15 | S2 |
| 02.09.01 | View a list of entrants who have joined the waitlist for my campsite lottery | M14 | S2 |
| 02.10.01 | Send notifications to entrants who have joined the waitlist for my campsite lottery | M14 | S2 |
| 02.10.02 | View a list of all notifications I have sent | M14 | S2 |
| 02.11.01 | Entrants to confirm that they have read the campsite rules and policies before confirming their reservation | M7 | S1 |
| 02.12.01 | Message a user who is reserving my campsite | M15, M16 | S2 |
| 03.01.01 | Remove registered campsites | M17 | S3 |
| 03.02.01 | Remove profiles | M17 | S3 |
| 03.03.01 | Remove images | M17 | S3 |
| 03.04.01 | Browse campsites | M17 | S3 |
| 03.05.01 | Browse profiles | M17 | S3 |
| 03.06.01 | Browse uploaded images so I can remove them if necessary | M17 | S3 |
| 03.07.01 | Remove campsite owners that violate app policy | M17 | S3 |
| 03.08.01 | Review logs of all notifications | M18 | S3 |
| 03.09.01 | Remove campsite ratings that violate app policy | M17 | S3 |
| 03.10.01 | Remove campsite reviews that violate app policy | M17 | S3 |
| 03.11.01 | Be a campsite owner and/or entrant with my admin profile | M1 | S1, S3 |
| 03.12.01 | Review logs of all messages from campsite owners to entrants who reserved their campsite | M18 | S3 |

## Reverse view: what each screen covers

| Screen | Name | User stories |
|---|---|---|
| M1 | First launch / role selection | 01.09.01, 03.11.01 |
| M2 | Campsite search and filters | 01.01.01, 01.01.02 |
| M3 | Campsite results list | 01.01.01, 01.01.03, 01.01.04 |
| M4 | Campsite details (join / leave waiting list, rate) | 01.01.05, 01.01.06, 01.02.01, 01.02.02, 01.12.01, 01.13.01, 01.13.02 |
| M5 | Scan QR code | 01.12.01 |
| M6 | Notifications | 01.03.01, 01.03.02, 01.05.01, 01.07.02 |
| M7 | You won: choose dates and confirm (or decline) | 01.04.01, 01.04.02, 01.04.03, 01.05.01, 02.11.01 |
| M8 | My reservations (active / past) and cancel dialog | 01.05.02, 01.06.01, 01.06.02, 01.07.01, 01.07.02, 01.14.01 |
| M9 | Profile and settings | 01.07.03, 01.08.01, 01.08.02, 01.10.01, 01.11.01 |
| M10 | My campsites (owner) | 02.01.01, 02.03.01 |
| M11 | Register / edit campsite | 02.01.01, 02.01.02, 02.01.03 |
| M12 | Campsite details, QR code and booked dates (owner) | 02.01.04, 02.02.01, 02.06.01 |
| M13 | Create / edit lottery | 02.04.01, 02.04.02, 02.02.02, 02.04.03, 02.04.04, 02.04.05, 02.04.06, 02.04.07 |
| M14 | Waiting list and send notification | 02.05.01, 02.09.01, 02.10.01, 02.10.02 |
| M15 | Reservations (active / past / cancelled) and reject dialog | 02.07.01, 02.07.02, 02.07.03, 02.08.01, 02.12.01 |
| M16 | Messages | 01.14.01, 02.12.01 |
| M17 | Admin: browse and remove | 03.01.01, 03.02.01, 03.03.01, 03.04.01, 03.05.01, 03.06.01, 03.07.01, 03.09.01, 03.10.01 |
| M18 | Admin: notification and message logs | 03.08.01, 03.12.01 |

**Stories with no screen: 0.** (If this number is not zero, the mockups are incomplete.)
