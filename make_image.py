#!/usr/bin/env python3
"""Generate entry.png: a newspaper front-page summary of world news, Tuesday 24 November 2026.
Deterministic: fixed layout, fixed text, no randomness. Output 1024x1024 PNG."""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

NAVY = (15, 42, 74)
RED = (192, 57, 43)
INK = (26, 26, 26)
GRAY = (85, 85, 85)
RULE = (200, 200, 200)
WHITE = (255, 255, 255)
GOLD = (212, 175, 55)
LIGHT_BG = (245, 245, 240)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    """Wrap text to fit max_w pixels, returning list of lines."""
    words = text.split()
    lines, cur = [], ""
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

def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y

img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)

# ---- Masthead ----
d.rectangle([0, 0, W, 118], fill=NAVY)
mast = font(SERIF_B, 62)
d.text((32, 18), "THE WORLD", font=mast, fill=WHITE)
# red breaking pill, top right
pill = "BREAKING"
pf = font(SANS_B, 22)
pw = d.textlength(pill, font=pf) + 28
d.rounded_rectangle([W - 32 - pw, 34, W - 32, 34 + 40], radius=20, fill=RED)
d.text((W - 32 - pw + 14, 42), pill, font=pf, fill=WHITE)
date_f = font(SANS_B, 22)
d.text((32, 88), "TUESDAY, 24 NOVEMBER 2026", font=date_f, fill=GOLD)
d.rectangle([0, 118, W, 122], fill=RED)

# ---- Lead story ----
y = 142
kick = font(SANS_B, 20)
d.text((32, y), "IRAN  •  U.S. NAVAL BLOCKADE", font=kick, fill=RED)
y += 30
head = font(SERIF_B, 46)
lead_head = "Iran vows to use 'all its tools' against U.S. blockade"
y = draw_lines(d, wrap(d, lead_head, head, W - 64), 32, y, head, INK, 54)
y += 6
body = font(SANS, 22)
lead_body = ("Tehran pledges to confront the renewed U.S. naval blockade as Vice President "
             "Vance and Secretary of State Rubio meet Qatar's prime minister at the White House.")
y = draw_lines(d, wrap(d, lead_body, body, W - 64), 32, y, body, GRAY, 30)
y += 14
d.line([(32, y), (W - 32, y)], fill=RULE, width=2)
y += 18

# ---- 2x2 story grid ----
stories = [
    ("GAZA", "Israeli strikes kill Hamas security chief",
     "Naeem Abu Nahel and six others, including two police officers, killed in Gaza, medics say."),
    ("UKRAINE", "Russian strike hits Zaporizhzhia flats",
     "Two killed and 40 wounded, among them four children, in an overnight attack on an apartment block."),
    ("TECH", "Huang back as Nvidia chief",
     "Jensen Huang reinstated as CEO less than two weeks after resigning; Senate Democrats vow an inquiry."),
    ("COURTS", "States sue SpaceX over Grok images",
     "Oregon and Virginia file suit over alleged Grok-generated abuse images."),
]
col_w = (W - 64 - 32) // 2
row_h = 218
for i, (k, h, b) in enumerate(stories):
    cx = 32 + (i % 2) * (col_w + 32)
    cy = y + (i // 2) * row_h
    d.text((cx, cy), k, font=kick, fill=RED)
    hf = font(SERIF_B, 27)
    ny = draw_lines(d, wrap(d, h, hf, col_w), cx, cy + 28, hf, INK, 33)
    bf = font(SANS, 19)
    draw_lines(d, wrap(d, b, bf, col_w), cx, ny + 4, bf, GRAY, 26)
    # vertical divider between columns
    if i % 2 == 0:
        d.line([(cx + col_w + 16, cy), (cx + col_w + 16, cy + row_h - 24)], fill=RULE, width=1)
y = y + 2 * row_h - 6
d.line([(32, y), (W - 32, y)], fill=RULE, width=2)
y += 16

# ---- Bottom strip: three short items ----
strip = font(SANS_B, 19)
items = [
    "UK to host 2035 Women's World Cup",
    "Germany first to access Ukraine's Delta system",
    "NATO vows to defend against space threats",
]
# draw as three lines with red bullets
sy = y
for it in items:
    d.text((32, sy), "■", font=font(SANS, 16), fill=RED)
    d.text((56, sy - 1), it, font=strip, fill=INK)
    sy += 30
y = sy + 8
d.rectangle([0, H - 44, W, H], fill=NAVY)
ff = font(SANS_B, 18)
ft = "24 NOVEMBER 2026  •  THE WORLD IN ONE IMAGE"
fw = d.textlength(ft, font=ff)
d.text(((W - fw) / 2, H - 33), ft, font=ff, fill=WHITE)

img.save(OUT, format="PNG", optimize=True)
print("wrote", OUT)
