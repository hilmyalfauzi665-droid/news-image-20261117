#!/usr/bin/env python3
"""Build the 17 November 2026 front-page poster (1024x1024) with PIL.

Crisp typeset text + one AI-generated flat illustration for the lead story.
All facts from reporting of Tuesday 17 November 2026.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (20, 20, 22)
NAVY = (18, 34, 60)
RED = (178, 34, 34)
GOLD = (201, 162, 39)
GREY = (90, 88, 84)
RULE = (200, 192, 172)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_wrapped(draw, x, y, text, fnt, max_w, fill, leading=None):
    lines = wrap(draw, text, fnt, max_w)
    lh = leading or int(fnt.size * 1.28)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- Masthead ----------
d.rectangle([0, 0, W, 132], fill=NAVY)
d.text((512, 18), "THE WORLD IN ONE DAY", font=font(SANS_B, 26),
       fill=GOLD, anchor="ma")
d.text((512, 50), "TUESDAY, 17 NOVEMBER 2026", font=font(SERIF_B, 52),
       fill=(255, 255, 255), anchor="ma")
d.rectangle([0, 132, W, 138], fill=RED)

# ---------- Lead story ----------
y = 148
d.text((24, y), "UKRAINE  •  WAR IN EUROPE", font=font(SANS_B, 22), fill=RED)
y += 30
d.text((24, y), "UKRAINE STRIKES THE", font=font(SERIF_B, 50), fill=INK)
y += 56
d.text((24, y), "CRIMEA BRIDGE AGAIN", font=font(SERIF_B, 50), fill=INK)
y += 64

hero = Image.open("assets/media-generation-bridge-hero-0-1649e0da-6a35-4999-be7f-66041ecd745e.png")
# Crop a horizontal band around the bridge + smoke (2736x912 source):
# 976x180 band -> crop 2736 x 505, y 170..675 keeps smoke, bridge and sea.
hero = hero.crop((0, 170, 2736, 675)).resize((976, 180), Image.LANCZOS)
img.paste(hero, (24, y))
d.rectangle([24, y, 1000, y + 180], outline=INK, width=2)
y += 180 + 8
cap = ("The Kerch bridge, hit for a second time in under 24 hours; traffic halted. "
       "Russia answered with missile strikes on two bridges in Kyiv.")
draw_wrapped(d, 24, y, cap, font(SERIF, 21), 976, INK, leading=27)
y += 27 * 2 + 8
d.line([24, y, 1000, y], fill=RULE, width=2)

# ---------- Story grid ----------
stories = [
    ("MIDDLE EAST  •  IRAN", RED,
     "IRAN FIRES ON U.S. BASE IN BAHRAIN",
     "Iranian drones target a U.S. radar site in Bahrain; Bahrain says it "
     "intercepted them. Tankers hit mines near the Strait of Hormuz."),
    ("ASIA  •  DIPLOMACY", (26, 92, 140),
     "TRUMP IN MANILA; XI\u2013TRUMP\u2013PUTIN SET",
     "Trump joins Quad talks in Manila. China confirms the first Xi\u2013Trump\u2013"
     "Putin meeting, Thursday in Shenzhen on the APEC sidelines."),
    ("MARKETS  •  U.S. BANKING", (26, 92, 140),
     "JPMORGAN OUTAGE HITS U.S. BANKING",
     "A fault at JPMorgan Chase disrupts online banking at major U.S. banks "
     "and Zelle. The bank says transactions are back to normal."),
    ("WEATHER  •  INDIA", (26, 92, 140),
     "CYCLONE AKVAN BEARS DOWN ON INDIA",
     "The storm strengthens toward Andhra Pradesh; Odisha begins evacuating "
     "coastal areas. Delhi\u2019s air pollution stays at crisis levels."),
]

grid_top = y + 12
row_h = 168
col_w = 488
gap = 24
x0, x1 = 24, 24 + col_w + gap
positions = [(x0, grid_top), (x1, grid_top),
             (x0, grid_top + row_h + 10), (x1, grid_top + row_h + 10)]

for i, (kicker, kc, headline, body) in enumerate(stories):
    px, py = positions[i]
    pw = col_w
    d.rectangle([px, py, px + pw, py + row_h], outline=RULE, width=2)
    d.rectangle([px, py, px + pw, py + 6], fill=kc)
    d.text((px + 14, py + 12), kicker, font=font(SANS_B, 16), fill=kc)
    ty = py + 34
    hl = wrap(d, headline, font(SANS_B, 21), pw - 28)
    for ln in hl:
        d.text((px + 14, ty), ln, font=font(SANS_B, 21), fill=INK)
        ty += 27
    draw_wrapped(d, px + 14, ty + 4, body, font(SANS, 17), pw - 28, (58, 56, 52), leading=22)

# ---------- Also strip ----------
strip_y = grid_top + 2 * row_h + 10 + 10
d.rectangle([24, strip_y, 1000, strip_y + 42], outline=RULE, width=2)
also = "ALSO:  China\u2013Canada agree tariff cuts  \u2022  EU sanctions 101 more Russian entities"
fs = 19
while d.textlength(also, font=font(SANS_B, fs)) > 940 and fs > 12:
    fs -= 1
d.text((38, strip_y + 10), also, font=font(SANS_B, fs), fill=INK)

# ---------- Footer ----------
fy = strip_y + 42 + 12
d.rectangle([0, fy, W, H], fill=NAVY)
d.text((512, fy + 6), "THE DAY IN BRIEF  \u2014  TUESDAY 17 NOVEMBER 2026",
       font=font(SANS_B, 20), fill=(255, 255, 255), anchor="ma")
d.text((512, fy + 32), "All events of that day, as reported. World news in one image.",
       font=font(SANS, 15), fill=(190, 196, 205), anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
