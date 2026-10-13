#!/usr/bin/env python3
"""Draw one CRC card the classic way (index-card look) plus a 'bad' card for contrast."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(__file__), "..", "wiki", "images")
FONT = "/System/Library/Fonts/Helvetica.ttc"
f = lambda s, b=False: ImageFont.truetype(FONT, s, index=1 if b else 0)


def card(name, resp, coll, gen=None, bad=False, fname="crc-card-Lottery.png", note=None):
    W, H = 900, 60 + 30 * max(len(resp), len(coll)) + 150
    im = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(im)
    col = (170, 0, 0) if bad else (33, 110, 80)
    d.rectangle([10, 10, W - 10, H - 10], outline=col, width=3, fill=(255, 250, 240) if bad else (250, 252, 250))
    d.text((30, 24), f"Class: {name}", font=f(24, True), fill=col)
    if gen:
        d.text((W - 330, 28), f"Generalization: {gen}", font=f(16), fill=(80, 80, 80))
    d.line([10, 64, W - 10, 64], fill=col, width=2)
    split = int(W * 0.66)
    d.line([split, 64, split, H - 10], fill=col, width=2)
    d.text((30, 74), "Responsibilities", font=f(17, True), fill=col)
    d.text((split + 20, 74), "Collaborators", font=f(17, True), fill=col)
    for i, r in enumerate(resp):
        d.text((30, 104 + 30 * i), "- " + r, font=f(15), fill=(30, 30, 30))
    for i, c in enumerate(coll):
        d.text((split + 20, 104 + 30 * i), c, font=f(15), fill=(30, 30, 30))
    if note:
        d.text((30, H - 60), note, font=f(14, True), fill=col)
    im.save(os.path.join(OUT, fname)); print("wrote", fname)


card("Lottery",
     ["Hold registration period, booking period, number of winners, optional capacity",
      "Know whether registration is currently open",
      "When the registration period ends, draw N winners at random from the waiting list",
      "Create one pending Reservation per winner",
      "Ask Notification to tell winners and non-winners",
      "Report its state (open / drawn / closed) to the owner"],
     ["Campsite", "CampsiteOwner", "WaitingList", "Entrant", "Reservation", "Notification"],
     note="Good: every line is an action; every collaborator also lists Lottery on its own card.")

card("Lottery",
     ["id: String", "campsiteId: String", "startDate: Date", "endDate: Date", "numWinners: Int",
      "waitlist: List<String>", "status: String"],
     ["FirebaseFirestore", "LotteryViewModel", "LotteryScreen.kt", "RecyclerView"],
     bad=True, fname="crc-card-bad-example.png",
     note="Bad: a field list instead of responsibilities, and Android/Firebase classes as collaborators.")
