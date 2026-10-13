#!/usr/bin/env python3
"""Draw the 18 low-fidelity phone mockups as PNG files with Pillow.

    python3 scripts/gen_mockups.py [WIKI_DIR]   # writes <wiki clone>/images/M*.png
                                               # default ../CMPUT301-final.wiki

Low fidelity is deliberate: a mockup has to show which controls exist and
where, not what the final colours are.  Red circled numbers are annotation
markers; their meaning is written next to each image on the wiki page UI-Mockups.
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

_ROOT = os.path.join(os.path.dirname(__file__), "..")
WIKI = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("WIKI_DIR", os.path.join(_ROOT, "..", "CMPUT301-final.wiki"))
OUT = os.path.join(WIKI, "images")
W, H = 440, 920          # phone canvas
PAD = 18                 # inner margin
FONT = "/System/Library/Fonts/Helvetica.ttc"


def font(size, bold=False):
    try:
        return ImageFont.truetype(FONT, size, index=1 if bold else 0)
    except Exception:
        return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", size)

F = font(15); FB = font(15, True); FS = font(12); FT = font(19, True); FM = font(13)
INK = (30, 30, 30); GREY = (120, 120, 120); LINE = (190, 190, 190); FILL = (245, 245, 245)
PRIMARY = (33, 110, 80); RED = (200, 40, 40); LIGHT = (225, 238, 232)


class Screen:
    def __init__(self, mid, title, back=True):
        self.mid, self.title = mid, title
        self.im = Image.new("RGB", (W, H), "white")
        self.d = ImageDraw.Draw(self.im)
        d = self.d
        d.rounded_rectangle([2, 2, W - 3, H - 3], radius=36, outline=INK, width=3)
        d.text((PAD + 6, 14), "9:41", font=FS, fill=INK)
        d.text((W - 70, 14), "LTE  100%", font=FS, fill=INK)
        d.rectangle([3, 40, W - 4, 90], fill=PRIMARY)
        x = PAD
        if back:
            d.text((x, 54), "<", font=FT, fill="white"); x += 26
        d.text((x, 55), title, font=FT, fill="white")
        self.y = 104
        self.marks = 0

    # -- helpers -----------------------------------------------------------
    def mark(self, n, y):
        if n:
            cx = W - PAD - 8
            self.d.ellipse([cx - 11, y - 11, cx + 11, y + 11], fill=RED)
            self.d.text((cx - 4 if n < 10 else cx - 8, y - 8), str(n), font=FB, fill="white")

    def text(self, s, size=None, n=0, color=INK, bold=False):
        f = font(size, bold) if size else (FB if bold else F)
        self.d.text((PAD, self.y), s, font=f, fill=color)
        self.mark(n, self.y + 9); self.y += (size or 15) + 10

    def note(self, s, n=0):
        self.text(s, 12, n=n, color=GREY)

    def h(self, s, n=0):
        self.y += 4; self.text(s, 17, n=n, bold=True)

    def spacer(self, px=10):
        self.y += px

    def input(self, label, value="", n=0):
        self.d.text((PAD, self.y), label, font=FS, fill=GREY); self.y += 16
        self.d.rounded_rectangle([PAD, self.y, W - PAD, self.y + 36], radius=6, outline=LINE, fill=FILL)
        self.d.text((PAD + 10, self.y + 10), value, font=F, fill=INK if value and not value.startswith("e.g.") else GREY)
        self.mark(n, self.y + 18); self.y += 46

    def button(self, label, primary=True, n=0, danger=False):
        fill = RED if danger else (PRIMARY if primary else "white")
        self.d.rounded_rectangle([PAD, self.y, W - PAD, self.y + 42], radius=8,
                                 fill=fill, outline=PRIMARY if not danger else RED, width=2)
        tw = self.d.textlength(label, font=FB)
        self.d.text(((W - tw) / 2, self.y + 12), label, font=FB, fill="white" if (primary or danger) else PRIMARY)
        self.mark(n, self.y + 21); self.y += 52

    def row_buttons(self, labels, n=0):
        k = len(labels); gap = 10
        bw = (W - 2 * PAD - gap * (k - 1)) / k
        for i, lab in enumerate(labels):
            x0 = PAD + i * (bw + gap)
            prim = i == 0
            self.d.rounded_rectangle([x0, self.y, x0 + bw, self.y + 40], radius=8,
                                     fill=PRIMARY if prim else "white", outline=PRIMARY, width=2)
            tw = self.d.textlength(lab, font=FB)
            self.d.text((x0 + (bw - tw) / 2, self.y + 11), lab, font=FB, fill="white" if prim else PRIMARY)
        self.mark(n, self.y + 20); self.y += 50

    def tabs(self, labels, active=0, n=0):
        k = len(labels); tw = (W - 2 * PAD) / k
        for i, lab in enumerate(labels):
            x0 = PAD + i * tw
            self.d.text((x0 + 8, self.y + 6), lab, font=FB if i == active else F, fill=PRIMARY if i == active else GREY)
            if i == active:
                self.d.rectangle([x0, self.y + 28, x0 + tw - 6, self.y + 31], fill=PRIMARY)
        self.d.line([PAD, self.y + 32, W - PAD, self.y + 32], fill=LINE)
        self.mark(n, self.y + 14); self.y += 42

    def card(self, title, lines, n=0, badge=None):
        hgt = 34 + 18 * len(lines)
        self.d.rounded_rectangle([PAD, self.y, W - PAD, self.y + hgt], radius=8, outline=LINE, fill="white")
        self.d.text((PAD + 10, self.y + 8), title, font=FB, fill=INK)
        if badge:
            bw = self.d.textlength(badge, font=FS) + 14
            self.d.rounded_rectangle([W - PAD - bw - 36, self.y + 8, W - PAD - 36, self.y + 26], radius=9, fill=LIGHT)
            self.d.text((W - PAD - bw - 29, self.y + 11), badge, font=FS, fill=PRIMARY)
        for i, ln in enumerate(lines):
            self.d.text((PAD + 10, self.y + 30 + 18 * i), ln, font=FM, fill=GREY)
        self.mark(n, self.y + hgt / 2); self.y += hgt + 10

    def listrow(self, title, sub="", right="", n=0):
        self.d.line([PAD, self.y, W - PAD, self.y], fill=LINE)
        self.d.text((PAD + 4, self.y + 8), title, font=FB, fill=INK)
        if sub:
            self.d.text((PAD + 4, self.y + 28), sub, font=FM, fill=GREY)
        if right:
            rw = self.d.textlength(right, font=FB)
            self.d.text((W - PAD - rw - 34, self.y + 12), right, font=FB, fill=PRIMARY)
        self.mark(n, self.y + 24); self.y += 50 if sub else 36

    def toggle(self, label, on=True, n=0):
        self.d.text((PAD, self.y + 6), label, font=F, fill=INK)
        x0 = W - PAD - 70
        self.d.rounded_rectangle([x0, self.y + 4, x0 + 40, self.y + 24], radius=10, fill=PRIMARY if on else LINE)
        cx = x0 + 30 if on else x0 + 10
        self.d.ellipse([cx - 8, self.y + 6, cx + 8, self.y + 22], fill="white")
        self.mark(n, self.y + 14); self.y += 36

    def check(self, label, checked=False, n=0):
        self.d.rectangle([PAD, self.y + 4, PAD + 18, self.y + 22], outline=INK, width=2, fill=LIGHT if checked else "white")
        if checked:
            self.d.line([PAD + 4, self.y + 13, PAD + 8, self.y + 18, PAD + 15, self.y + 7], fill=PRIMARY, width=3)
        self.d.text((PAD + 28, self.y + 5), label, font=F, fill=INK)
        self.mark(n, self.y + 13); self.y += 32

    def chips(self, labels, n=0):
        x = PAD
        for lab in labels:
            w = self.d.textlength(lab, font=FS) + 20
            self.d.rounded_rectangle([x, self.y, x + w, self.y + 24], radius=12, fill=LIGHT)
            self.d.text((x + 10, self.y + 5), lab, font=FS, fill=PRIMARY)
            x += w + 8
        self.mark(n, self.y + 12); self.y += 34

    def box(self, label, hgt=120, n=0, kind="map"):
        self.d.rectangle([PAD, self.y, W - PAD, self.y + hgt], outline=LINE, fill=FILL)
        if kind == "map":
            for i in range(PAD + 30, W - PAD, 45):
                self.d.line([i, self.y, i, self.y + hgt], fill=LINE)
            for j in range(self.y + 30, self.y + hgt, 40):
                self.d.line([PAD, j, W - PAD, j], fill=LINE)
            cx, cy = W / 2, self.y + hgt / 2
            self.d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=RED)
        elif kind == "image":
            self.d.line([PAD, self.y, W - PAD, self.y + hgt], fill=LINE)
            self.d.line([PAD, self.y + hgt, W - PAD, self.y], fill=LINE)
        elif kind == "qr":
            s = 8; x0 = W / 2 - 60; y0 = self.y + (hgt - 120) / 2
            import random; random.seed(7)
            for i in range(15):
                for j in range(15):
                    if random.random() < 0.45 or (i < 4 and j < 4) or (i < 4 and j > 10) or (i > 10 and j < 4):
                        self.d.rectangle([x0 + i * s, y0 + j * s, x0 + i * s + s - 1, y0 + j * s + s - 1], fill=INK)
        elif kind == "camera":
            self.d.rectangle([PAD + 60, self.y + 30, W - PAD - 60, self.y + hgt - 30], outline=PRIMARY, width=3)
        elif kind == "calendar":
            days = "M T W T F S S".split()
            cw = (W - 2 * PAD) / 7
            for i, dname in enumerate(days):
                self.d.text((PAD + i * cw + 20, self.y + 6), dname, font=FS, fill=GREY)
            n_ = 1
            for r in range(4):
                for c in range(7):
                    x0 = PAD + c * cw + 4; y0 = self.y + 26 + r * 22
                    booked = (r, c) in {(0, 5), (0, 6), (1, 5), (1, 6), (2, 2)}
                    avail = c >= 4 and not booked
                    if booked:
                        self.d.rectangle([x0, y0, x0 + cw - 8, y0 + 20], fill=(240, 200, 200))
                    elif avail:
                        self.d.rectangle([x0, y0, x0 + cw - 8, y0 + 20], fill=LIGHT)
                    self.d.text((x0 + 10, y0 + 3), str(n_), font=FS, fill=INK)
                    n_ += 1
        tw = self.d.textlength(label, font=FS)
        self.d.text(((W - tw) / 2, self.y + hgt - 18), label, font=FS, fill=GREY)
        self.mark(n, self.y + hgt / 2); self.y += hgt + 12

    def dialog(self, title, body, buttons, n=0):
        # dim everything drawn so far, then overlay a dialog
        overlay = Image.new("RGBA", self.im.size, (0, 0, 0, 90))
        self.im.paste(Image.alpha_composite(self.im.convert("RGBA"), overlay).convert("RGB"))
        self.d = ImageDraw.Draw(self.im)
        x0, y0, x1 = 40, 330, W - 40
        hgt = 70 + 20 * len(body) + 56
        self.d.rounded_rectangle([x0, y0, x1, y0 + hgt], radius=12, fill="white", outline=INK)
        self.d.text((x0 + 18, y0 + 16), title, font=FT, fill=INK)
        for i, ln in enumerate(body):
            self.d.text((x0 + 18, y0 + 50 + 20 * i), ln, font=F, fill=INK)
        bx = x1 - 18
        for i, lab in enumerate(reversed(buttons)):
            bw = self.d.textlength(lab, font=FB) + 24
            fill = RED if i == 0 and lab.lower().startswith(("cancel res", "reject", "delete", "decline", "remove")) else (PRIMARY if i == 0 else "white")
            self.d.rounded_rectangle([bx - bw, y0 + hgt - 48, bx, y0 + hgt - 14], radius=8, fill=fill, outline=PRIMARY)
            self.d.text((bx - bw + 12, y0 + hgt - 39), lab, font=FB, fill="white" if i == 0 else PRIMARY)
            bx -= bw + 10
        if n:
            cx = x1 - 4; cy = y0 + 4
            self.d.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=RED)
            self.d.text((cx - 4, cy - 8), str(n), font=FB, fill="white")

    def nav(self, labels, active=0):
        y0 = H - 64
        self.d.line([3, y0, W - 4, y0], fill=LINE)
        k = len(labels); tw = (W - 8) / k
        for i, lab in enumerate(labels):
            x0 = 4 + i * tw
            col = PRIMARY if i == active else GREY
            self.d.rounded_rectangle([x0 + tw / 2 - 12, y0 + 10, x0 + tw / 2 + 12, y0 + 30], radius=5, outline=col, width=2)
            w = self.d.textlength(lab, font=FS)
            self.d.text((x0 + (tw - w) / 2, y0 + 36), lab, font=FS, fill=col)

    def save(self):
        self.d.text((PAD, H - 26), self.mid, font=FS, fill=GREY) if False else None
        path = os.path.join(OUT, f"{self.mid}.png")
        self.im.save(path)
        print("wrote", os.path.relpath(path))


ENTRANT_NAV = ["Search", "Scan", "Reservations", "Alerts", "Profile"]
OWNER_NAV = ["Campsites", "Lotteries", "Reservations", "Messages", "Profile"]
ADMIN_NAV = ["Campsites", "Profiles", "Images", "Logs", "Profile"]


def build():
    os.makedirs(OUT, exist_ok=True)

    s = Screen("M1", "Campsite Lottery", back=False)
    s.spacer(30); s.text("Welcome", 26, bold=True)
    s.note("No sign-up. This device is your identity (US 01.09.01).", n=1)
    s.spacer(8); s.input("Display name", "e.g. Sam"); s.input("Email (optional)", "e.g. sam@ualberta.ca")
    s.h("Continue as"); s.note("Admins can switch roles later from Profile (US 03.11.01).", n=2)
    s.button("Entrant  -  find and reserve campsites")
    s.button("Campsite owner  -  list campsites and run lotteries", primary=False)
    s.button("Admin  -  moderate the app", primary=False, n=3)
    s.spacer(6); s.note("Device id: a3f9...e1 (hidden, generated on first launch)")
    s.save()

    s = Screen("M2", "Find a campsite", back=False)
    s.input("Search", "e.g. Banff", n=1)
    s.h("Filters"); s.input("Location / park", "Jasper National Park", n=2)
    s.row_buttons(["From  Jul 10", "To  Jul 12"]); s.input("Guests", "4")
    s.chips(["Has active lottery", "Lake", "Pet friendly"], n=3)
    s.button("Show results", n=4)
    s.nav(ENTRANT_NAV, 0); s.save()

    s = Screen("M3", "Results (12)")
    s.chips(["Jasper", "Jul 10-12", "4 guests"], n=1)
    s.card("Pyramid Lake Site 4", ["Jasper NP  .  max 6 guests  .  4.6 / 5", "Lottery open, closes in 2 days"], badge="LOTTERY", n=2)
    s.card("Whistlers Loop B", ["Jasper NP  .  max 8  .  4.1 / 5", "No lottery - first come first served"], n=3)
    s.card("Wapiti Riverside", ["Jasper NP  .  max 4  .  4.8 / 5", "Lottery open, closes in 6 days"], badge="LOTTERY")
    s.card("Snaring Overflow", ["Jasper NP  .  max 10  .  3.9 / 5", "Fully booked for your dates"])
    s.nav(ENTRANT_NAV, 0); s.save()

    s = Screen("M4", "Pyramid Lake Site 4")
    s.box("promotional image", 90, kind="image", n=1)
    s.text("Jasper NP  .  max 6 guests  .  $65 / night", 13, color=GREY)
    s.text("4.6 / 5  (31 ratings)      Rate this campsite  >", 13, color=PRIMARY, n=2)
    s.note("Lakeside pad, fire pit, bear lockers, 10 min to trailhead.")
    s.box("map (US 02.01.02 geolocation)", 80, kind="map", n=3)
    s.card("Lottery: Jul weekends", ["Registration closes 2026-07-01 23:59", "Booking window Jul 4 - Jul 31  .  5 winners", "18 on waiting list (cap 50)"], badge="OPEN", n=4)
    s.button("Join waiting list", n=5)
    s.button("Leave waiting list", primary=False, n=6)
    s.note("Button swaps to Leave after joining (US 01.02.02). Rules & policy  >")
    s.nav(ENTRANT_NAV, 0); s.save()

    s = Screen("M5", "Scan QR code", back=False)
    s.box("camera preview - point at the poster", 300, kind="camera", n=1)
    s.note("A valid code opens the campsite details (M4) directly.", n=2)
    s.note("Invalid or unknown code: toast 'This code is not a campsite'.")
    s.button("Enter code manually", primary=False, n=3)
    s.nav(ENTRANT_NAV, 1); s.save()

    s = Screen("M6", "Notifications", back=False)
    s.tabs(["All", "Unread"], 0)
    s.listrow("You won! Pyramid Lake Site 4", "Choose your dates before Jul 4  .  tap to open", n=1)
    s.listrow("Reservation confirmed", "Wapiti Riverside, Jul 18-19", n=2)
    s.listrow("Lottery result: not selected", "Snaring Overflow - better luck next time", n=3)
    s.listrow("Message from owner", "Pyramid Lake: 'Fire ban in effect this weekend'")
    s.listrow("Cancellation confirmed", "Whistlers Loop B, Jun 2")
    s.spacer(8); s.note("Opt out in Profile > Settings (US 01.10.01).", n=4)
    s.nav(ENTRANT_NAV, 3); s.save()

    s = Screen("M7", "You won the lottery")
    s.note("Pyramid Lake Site 4  .  respond before Jul 4 23:59", n=1)
    s.input("Campsite (multi-campsite lottery only)", "Pyramid Lake Site 4   v", n=2)
    s.box("available dates (red = already booked)", 130, kind="calendar", n=3)
    s.text("Selected: Jul 10 - Jul 12 (2 nights)  .  $130", 14, color=PRIMARY)
    s.check("I have read the campsite rules and cancellation policy", True, n=4)
    s.row_buttons(["Confirm reservation", "Decline"], n=5)
    s.note("Decline returns the spot to the owner (US 01.04.03).")
    s.save()

    s = Screen("M8", "My reservations", back=False)
    s.tabs(["Active", "Past"], 0, n=1)
    s.card("Pyramid Lake Site 4", ["Jul 10 - Jul 12  .  2 nights  .  confirmed", "Export CSV   .   Message owner   .   Cancel"], badge="ACTIVE", n=2)
    s.card("Wapiti Riverside", ["Jul 18 - Jul 19  .  1 night  .  confirmed", "Export CSV   .   Message owner   .   Cancel"], badge="ACTIVE")
    s.card("Snaring Overflow", ["Aug 2 - Aug 3  .  rejected by owner (refunded)", "Reason: forest fire warning"], badge="REJECTED")
    s.dialog("Cancel this reservation?", ["Pyramid Lake Site 4, Jul 10 - 12.", "You will get a confirmation", "notification and a CSV."], ["Keep", "Cancel reservation"], n=3)
    s.nav(ENTRANT_NAV, 2); s.save()

    s = Screen("M9", "Profile", back=False)
    s.box("profile image  (tap to add / change / remove)", 80, kind="image", n=1)
    s.input("Name", "Sam Lee"); s.input("Email", "sam@ualberta.ca"); s.input("Phone", "780 555 0100")
    s.button("Save changes", n=2)
    s.h("Settings")
    s.toggle("Receive notifications", True, n=3)
    s.listrow("App policy and guidelines", right=">", n=4)
    s.listrow("Switch role (admin only)", right=">")
    s.button("Delete my profile", primary=False, n=5, danger=True)
    s.nav(ENTRANT_NAV, 4); s.save()

    s = Screen("M10", "My campsites", back=False)
    s.card("Pyramid Lake Site 4", ["Jasper NP  .  max 6  .  4.6 / 5", "Lottery OPEN  .  18 on waiting list"], badge="OPEN", n=1)
    s.card("Hinton Cookhouse Site", ["Hinton - Grande Cache  .  max 8", "No lottery  .  5 booked nights in May"], n=2)
    s.card("Athabasca Bend", ["Jasper NP  .  max 4", "Lottery DRAWN  .  3 of 5 winners confirmed"], badge="DRAWN")
    s.spacer(40); s.button("+  Register a new campsite", n=3)
    s.nav(OWNER_NAV, 0); s.save()

    s = Screen("M11", "Register campsite")
    s.input("Name", "Hinton Cookhouse Site", n=1)
    s.input("Description / amenities", "Outdoor cookhouse, tennis court, ...")
    s.row_buttons(["Max guests  8", "Price / night  $65"])
    s.input("Address or park", "Hinton - Grande Cache")
    s.box("drop a pin on the map (geolocation)", 90, kind="map", n=2)
    s.box("promotional image (optional)  +", 60, kind="image", n=3)
    s.chips(["cookhouse", "tennis", "family", "+ tag"], n=4)
    s.input("Rules and cancellation policy", "Quiet hours 11pm; full refund 7 days out")
    s.row_buttons(["Publish", "Save draft"], n=5)
    s.save()

    s = Screen("M12", "Hinton Cookhouse Site")
    s.tabs(["Details", "QR code", "Booked dates"], 1, n=1)
    s.box("QR code - share on posters", 150, kind="qr", n=2)
    s.row_buttons(["Share", "Download PNG"])
    s.box("booked dates (red) / available (green)", 130, kind="calendar", n=3)
    s.row_buttons(["Edit campsite", "Create lottery"], n=4)
    s.nav(OWNER_NAV, 0); s.save()

    s = Screen("M13", "Create lottery")
    s.input("Campsites in this lottery", "Hinton Cookhouse Site  (+ add another)", n=1)
    s.h("Registration period"); s.row_buttons(["Opens  Apr 1", "Closes  Apr 14"], n=2)
    s.h("Booking period"); s.row_buttons(["From  May 1", "To  May 31"], n=3)
    s.input("Number of winners", "5", n=4)
    s.input("Waiting list capacity (optional)", "e.g. 50", n=5)
    s.note("Winners are drawn automatically when registration closes (US 02.05.01).")
    s.row_buttons(["Publish lottery", "Save"], n=6)
    s.save()

    s = Screen("M14", "Waiting list (18)")
    s.card("Lottery: May weekends", ["Registration closes Apr 14 23:59  .  5 winners", "Status: OPEN - draw scheduled Apr 15 00:00"], badge="OPEN", n=1)
    s.listrow("Sam Lee", "joined Apr 2  .  4 guests")
    s.listrow("Priya N.", "joined Apr 2  .  2 guests")
    s.listrow("Jordan K.", "joined Apr 5  .  6 guests")
    s.listrow("+ 15 more", right="see all")
    s.spacer(6); s.button("Send notification to everyone on the list", n=2)
    s.listrow("Sent notifications (3)", right=">", n=3)
    s.button("Draw winners now (testing only)", primary=False, n=4)
    s.nav(OWNER_NAV, 1); s.save()

    s = Screen("M15", "Reservations", back=False)
    s.tabs(["Active", "Past", "Cancelled"], 0, n=1)
    s.card("Sam Lee - Pyramid Lake Site 4", ["Jul 10 - Jul 12  .  4 guests  .  $130", "Message   .   Reject"], badge="CONFIRMED", n=2)
    s.card("Priya N. - Athabasca Bend", ["Jul 11 - Jul 12  .  2 guests", "Message   .   Reject"], badge="CONFIRMED")
    s.dialog("Reject this reservation?", ["Sam Lee, Jul 10 - 12.", "The entrant is notified and refunded.", "Reason (shown to entrant):", "[ forest fire warning            ]"], ["Back", "Reject"], n=3)
    s.nav(OWNER_NAV, 2); s.save()

    s = Screen("M16", "Sam Lee  -  Pyramid Lake")
    s.note("About reservation Jul 10 - 12 (US 02.12.01 / 01.14.01)", n=1)
    s.card("Owner  .  Jun 30 14:02", ["Hi Sam, a fire ban is in effect this weekend;", "please bring a camp stove."])
    s.card("Sam  .  Jun 30 15:40", ["Thanks, will do. Is the lake open for swimming?"])
    s.card("Owner  .  Jun 30 16:05", ["Yes, the beach is open 9am to 8pm."])
    s.spacer(130); s.input("Message", "e.g. type a message...", n=2); s.button("Send", n=3)
    s.save()

    s = Screen("M17", "Admin: campsites", back=False)
    s.tabs(["Campsites", "Profiles", "Images", "Owners"], 0, n=1)
    s.input("Search", "e.g. name, owner, park")
    s.listrow("Pyramid Lake Site 4", "owner: J. Park  .  Jasper", right="Remove", n=2)
    s.listrow("Spam Site 999", "owner: throwaway  .  reported 3x", right="Remove")
    s.listrow("Hinton Cookhouse Site", "owner: M. Chen  .  Hinton", right="Remove")
    s.dialog("Remove campsite?", ["Spam Site 999 will be deleted with its", "lotteries, waiting lists and images.", "This cannot be undone."], ["Back", "Remove"], n=3)
    s.nav(ADMIN_NAV, 0); s.save()

    s = Screen("M18", "Admin: logs", back=False)
    s.tabs(["Notifications", "Messages"], 0, n=1)
    s.input("Filter", "e.g. campsite, user, date")
    s.listrow("Jul 1 00:00  lottery WIN", "to Sam Lee  .  Pyramid Lake Site 4", n=2)
    s.listrow("Jul 1 00:00  lottery LOSE", "to 13 entrants  .  Pyramid Lake Site 4")
    s.listrow("Jun 30 14:02  owner message", "J. Park -> Sam Lee  .  'fire ban in effect'", n=3)
    s.listrow("Jun 28 09:12  owner broadcast", "M. Chen -> 18 on waiting list")
    s.listrow("Jun 27 18:40  reservation REJECTED", "to Priya N.  .  Snaring Overflow")
    s.button("Export log as CSV", primary=False, n=4)
    s.nav(ADMIN_NAV, 3); s.save()


if __name__ == "__main__":
    build()
