"""Single source of truth for the demo backlog.

Every other generated artefact (wiki/Product-Backlog.md, the traceability
table, backlog/backlog.csv, scripts/create_issues.sh) is derived from this
file so that numbers, points, risks and halfway flags can never disagree.

Fields: (us, story, points, risk, halfway, assignee, screens)
  points   -- story points on the 1/2/3/5/8 scale (see SCALE below)
  risk     -- low | medium | high
  halfway  -- True if the story is planned for Part 3 (Halfway, due 2026-11-06)
  assignee -- demo team member who owns the issue
  screens  -- mockup ids (M1..M18) where the story is visible
Stories whose text ends in "-->" are marked optional in the project description.
"""

SCALE = {
    1: "a few hours, no unknowns",
    2: "about half a day",
    3: "one to two days",
    5: "most of a week for one person, some unknowns",
    8: "more than a week or depends on a technology nobody on the team has used",
}

TEAM = {
    "alice": "Backlog owner (entrant search & browse)",
    "bob":   "Backlog owner (entrant lottery & reservations)",
    "chen":  "Mockup owner (campsite owner screens)",
    "dana":  "Mockup owner (lottery & reservation screens)",
    "eli":   "CRC owner (admin stories)",
    "farah": "Wiki & tool-use owner (auth, profile, notifications)",
}

STORIES = [
    # ---- Entrant ---------------------------------------------------------
    ("01.01.01", "As an entrant, I want to search for campsites.", 2, "low", True, "alice", ["M2", "M3"]),
    ("01.01.02", "As an entrant, I want to filter campsites by location, date, and number of guests.", 3, "medium", True, "alice", ["M2"]),
    ("01.01.03", "As an entrant, I want to see a list of campsites based on my filters.", 2, "low", True, "alice", ["M3"]),
    ("01.01.04", "As an entrant, I want to see campsite summary information including name, location, maximum occupancy, and rating.", 1, "low", True, "alice", ["M3"]),
    ("01.01.05", "As an entrant, I want to see details of a campsite.", 2, "low", True, "alice", ["M4"]),
    ("01.01.06", "As an entrant, I want to join an active lottery from the campsite details screen.", 2, "low", True, "bob", ["M4"]),
    ("01.02.01", "As an entrant, I want to join the waiting list for a campsite lottery.", 3, "medium", True, "bob", ["M4"]),
    ("01.02.02", "As an entrant, I want to leave the waiting list for a campsite lottery.", 2, "low", True, "bob", ["M4"]),
    ("01.03.01", "As an entrant, I want to receive a notification when I win the campsite lottery.", 5, "high", True, "farah", ["M6"]),
    ("01.03.02", "As an entrant, I want to receive a notification when I lose the campsite lottery.", 3, "medium", True, "farah", ["M6"]),
    ("01.04.01", "As an entrant, if I win the lottery, I want to see available dates that I can reserve the campsite for.", 3, "medium", True, "bob", ["M7"]),
    ("01.04.02", "As an entrant, if I win a multiple campsite lottery, I want to choose which campsite to reserve and which dates I want.", 5, "high", False, "bob", ["M7"]),
    ("01.04.03", "As an entrant, if I win the lottery, I want to decline a reservation if I changed my mind or if none of the remaining dates work for me.", 2, "low", True, "bob", ["M7"]),
    ("01.05.01", "As an entrant, I want to receive confirmation of my campsite reservation.", 2, "low", True, "bob", ["M7", "M6"]),
    ("01.05.02", "As an entrant, I want to receive reservation by notification or downloadable CSV.", 3, "medium", False, "bob", ["M8"]),
    ("01.06.01", "As an entrant, I want to view a list of my active reservations.", 2, "low", False, "bob", ["M8"]),
    ("01.06.02", "As an entrant, I want to view a list of my past reservations.", 1, "low", False, "bob", ["M8"]),
    ("01.07.01", "As an entrant, I want to cancel my campsite reservation.", 2, "low", False, "bob", ["M8"]),
    ("01.07.02", "As an entrant, I want to receive confirmation of my campsite cancellation by notification or downloadable CSV.", 2, "low", False, "bob", ["M8", "M6"]),
    ("01.07.03", "As an entrant, I want to update my personal information, such as name, email, and phone number, on my profile.", 2, "low", True, "farah", ["M9"]),
    ("01.08.01", "As an entrant, I want to delete my profile.", 2, "low", False, "farah", ["M9"]),
    ("01.08.02", "As an entrant, I want to add, update, or remove my profile image. -->", 3, "medium", False, "farah", ["M9"]),
    ("01.09.01", "As an entrant, I want to be identified by my device, so that I do not have to use a username and password.", 5, "high", True, "farah", ["M1"]),
    ("01.10.01", "As an entrant, I want to opt out of receiving notifications.", 1, "low", False, "farah", ["M9"]),
    ("01.11.01", "As an entrant, I want to see the app policy and guidelines.", 1, "low", False, "farah", ["M9"]),
    ("01.12.01", "As an entrant, I want to view campsite details by scanning the promotional QR code.", 5, "high", True, "alice", ["M5", "M4"]),
    ("01.13.01", "As an entrant, I want to give a rating for a campsite.", 2, "low", False, "alice", ["M4"]),
    ("01.13.02", "As an entrant, I want to post a review for a campsite. -->", 2, "low", False, "alice", ["M4"]),
    ("01.14.01", "As an entrant, I want to message the campsite owner for a reservation that I have. -->", 3, "medium", False, "dana", ["M8", "M16"]),
    # ---- Campsite owner -------------------------------------------------
    ("02.01.01", "As a campsite owner, I want to register my campsite with the app.", 3, "low", True, "chen", ["M10", "M11"]),
    ("02.01.02", "As a campsite owner, I want to provide campsite details including name, location, description (amenities), maximum occupancy, map location, optional image, and tags.", 5, "high", True, "chen", ["M11"]),
    ("02.01.03", "As a campsite owner, I want to update details about my campsite.", 2, "low", True, "chen", ["M11"]),
    ("02.01.04", "As a campsite owner, I want to view details of my campsite.", 1, "low", True, "chen", ["M12"]),
    ("02.02.01", "As a campsite owner, I want the system to generate a unique QR code that links to the campsite details.", 3, "medium", True, "chen", ["M12"]),
    ("02.03.01", "As a campsite owner, I want to view a list of my campsites.", 2, "low", True, "chen", ["M10"]),
    ("02.04.01", "As a campsite owner, I want to list my campsite in a lottery for a certain period.", 3, "medium", True, "dana", ["M13"]),
    ("02.04.02", "As a campsite owner, I want be able to list multiple campsites in a lottery for a certain period.", 5, "high", False, "dana", ["M13"]),
    ("02.02.02", "As a campsite owner, I want be able to list multiple campsites with other campsite owners in a lottery for a certain period. -->", 8, "high", False, "dana", ["M13"]),
    ("02.04.03", "As a campsite owner, I want to set a registration period.", 1, "low", True, "dana", ["M13"]),
    ("02.04.04", "As a campsite owner, I want to set a booking period.", 1, "low", True, "dana", ["M13"]),
    ("02.04.05", "As a campsite owner, I want to set the number of lottery winners.", 1, "low", True, "dana", ["M13"]),
    ("02.04.06", "As a campsite owner, I want to update my campsite lottery listing.", 2, "low", False, "dana", ["M13"]),
    ("02.04.07", "As a campsite owner, I want to optionally set a capacity for my lottery waitlist.", 2, "medium", False, "dana", ["M13"]),
    ("02.05.01", "As a campsite owner, I want the system to automatically draw winners after the registration period ends.", 8, "high", True, "dana", ["M14"]),
    ("02.06.01", "As a campsite owner, I want to view the currently booked dates for my campsite.", 3, "medium", False, "chen", ["M12"]),
    ("02.07.01", "As a campsite owner, I want to view a list of active reservations.", 2, "low", False, "dana", ["M15"]),
    ("02.07.02", "As a campsite owner, I want to view a list of past reservations.", 1, "low", False, "dana", ["M15"]),
    ("02.07.03", "As a campsite owner, I want to view a list of cancelled reservations.", 1, "low", False, "dana", ["M15"]),
    ("02.08.01", "As a campsite owner, I want to reject a reservation.", 2, "low", False, "dana", ["M15"]),
    ("02.09.01", "As a campsite owner, I want to view a list of entrants who have joined the waitlist for my campsite lottery.", 2, "low", True, "dana", ["M14"]),
    ("02.10.01", "As a campsite owner, I want to send notifications to entrants who have joined the waitlist for my campsite lottery.", 3, "medium", True, "farah", ["M14"]),
    ("02.10.02", "As a campsite owner, I want to view a list of all notifications I have sent.", 2, "low", False, "farah", ["M14"]),
    ("02.11.01", "As a campsite owner, I want entrants to confirm that they have read the campsite rules and policies before confirming their reservation.", 2, "low", False, "bob", ["M7"]),
    ("02.12.01", "As a campsite owner, I want to message a user who is reserving my campsite.", 3, "medium", False, "dana", ["M15", "M16"]),
    # ---- Admin -------------------------------------------------------------
    ("03.01.01", "As an admin, I want to remove registered campsites.", 2, "low", True, "eli", ["M17"]),
    ("03.02.01", "As an admin, I want to remove profiles.", 2, "low", False, "eli", ["M17"]),
    ("03.03.01", "As an admin, I want to remove images.", 2, "medium", False, "eli", ["M17"]),
    ("03.04.01", "As an admin, I want to browse campsites.", 2, "low", True, "eli", ["M17"]),
    ("03.05.01", "As an admin, I want to browse profiles.", 2, "low", False, "eli", ["M17"]),
    ("03.06.01", "As an admin, I want to browse uploaded images so I can remove them if necessary.", 3, "medium", False, "eli", ["M17"]),
    ("03.07.01", "As an admin, I want to remove campsite owners that violate app policy.", 2, "low", False, "eli", ["M17"]),
    ("03.08.01", "As an admin, I want to review logs of all notifications.", 3, "medium", False, "eli", ["M18"]),
    ("03.09.01", "As an admin, I want to remove campsite ratings that violate app policy. -->", 1, "low", False, "eli", ["M17"]),
    ("03.10.01", "As an admin, I want to remove campsite reviews that violate app policy. -->", 1, "low", False, "eli", ["M17"]),
    ("03.11.01", "As an admin, I should be able to be a campsite owner and/or entrant with my admin profile.", 2, "medium", True, "farah", ["M1"]),
    ("03.12.01", "As an admin, I want to review logs of all messages from campsite owners to entrants who reserved their campsite.", 3, "medium", False, "eli", ["M18"]),
]

# Preparation tasks: Part 2 work items that are not user stories but still
# belong on the board so that the board has moving cards during Part 2.
TASKS = [
    ("Write product backlog summary page", "alice"),
    ("Create one issue per user story with labels", "bob"),
    ("Draw entrant and shared screens", "chen"),
    ("Draw owner and admin screens, storyboards", "dana"),
    ("Write CRC cards and check collaborators both ways", "eli"),
    ("Set up wiki home, README, .gitignore, project board", "farah"),
]

SCREENS = {
    "M1":  "First launch / role selection",
    "M2":  "Campsite search and filters",
    "M3":  "Campsite results list",
    "M4":  "Campsite details (join / leave waiting list, rate)",
    "M5":  "Scan QR code",
    "M6":  "Notifications",
    "M7":  "You won: choose dates and confirm (or decline)",
    "M8":  "My reservations (active / past) and cancel dialog",
    "M9":  "Profile and settings",
    "M10": "My campsites (owner)",
    "M11": "Register / edit campsite",
    "M12": "Campsite details, QR code and booked dates (owner)",
    "M13": "Create / edit lottery",
    "M14": "Waiting list and send notification",
    "M15": "Reservations (active / past / cancelled) and reject dialog",
    "M16": "Messages",
    "M17": "Admin: browse and remove",
    "M18": "Admin: notification and message logs",
}

STORYBOARDS = {
    "S1": ("Entrant: scan, join, win, reserve or decline", ["M5", "M4", "M6", "M7", "M8", "M1", "M2", "M3"]),
    "S2": ("Owner: register, list lottery, draw, manage reservations", ["M10", "M11", "M12", "M13", "M14", "M15", "M16"]),
    "S3": ("Admin: browse, remove, review logs", ["M1", "M17", "M18"]),
}


def role_of(us):
    return {"01": "entrant", "02": "owner", "03": "admin"}[us[:2]]


def is_optional(story):
    return story.rstrip().endswith("-->")


def issue_number(us):
    """Issue numbers in the demo are simply document order, starting at 1."""
    return [s[0] for s in STORIES].index(us) + 1


def short_title(story):
    """'As an entrant, I want to search for campsites.' -> 'Search for campsites'."""
    text = story.replace(" -->", "").rstrip(".")
    for sep in (", I want to ", ", I want ", ", I should be able to ", ", if I win the lottery, I want to "):
        if sep in text:
            text = text.split(sep, 1)[1]
            break
    for prefix in ("to ", "be able to "):
        if text.startswith(prefix):
            text = text[len(prefix):]
    return text[0].upper() + text[1:]
