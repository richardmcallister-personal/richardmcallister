"""Build public/og-image-1200x630.png: the share image, set as the front page of the paper.

Uses the site's own self-hosted fonts (Libre Franklin, Source Serif 4) and the day-edition tokens from site.css.
All text is outlined, so the render does not depend on installed fonts.

    pip install fonttools brotli        # rsvg-convert must be on PATH
    python3 scripts/build-og.py
"""
import os, subprocess, tempfile
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "public", "fonts")
OUT = os.path.join(ROOT, "public", "og-image-1200x630.png")

PAPER, INK, MUTE, HAIR = "#FBFAF7", "#111110", "#4E4D49", "#CFCCC4"

class Face:
    def __init__(self, name):
        f = TTFont(os.path.join(FONTS, name))
        self.gs, self.cmap, self.upm = f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm
    def width(self, s, size, tr=0.0):
        return sum(self.gs[self.cmap[ord(c)]].width for c in s) * size / self.upm + tr * size * (len(s) - 1)
    def path(self, s, size, x, base, tr=0.0, fill=INK):
        sc = size / self.upm; d = []
        for c in s:
            g = self.gs[self.cmap[ord(c)]]
            pen = SVGPathPen(self.gs)
            g.draw(TransformPen(pen, (sc, 0, 0, -sc, x, base)))
            d.append(pen.getCommands())
            x += g.width * sc + tr * size
        return f'<path d="{" ".join(d)}" fill="{fill}"/>'

F900 = Face("libre-franklin-latin-900-normal.woff2")
F800 = Face("libre-franklin-latin-800-normal.woff2")
F600 = Face("libre-franklin-latin-600-normal.woff2")
SERIF_I = Face("source-serif-4-latin-400-italic.woff2")

SPORT = [("Manchester United", "#DA020E"), ("Celtic", "#007A3D"), ("Limerick hurling", "#00693E"),
         ("Ireland football", "#0B6E4F"), ("Ireland rugby", "#0A6B3D"), ("Club football", INK)]
MUSIC = [("Bob Dylan", "#B3261E"), ("Led Zeppelin", "#8A5A12"), ("Billy Connolly", "#7F5700")]

W, H, M = 1200, 630, 72
b = [f'<rect width="{W}" height="{H}" fill="{PAPER}"/>']
b.append(F900.path("Richard McAllister", 104, M, 160, -0.035))
b.append(f'<rect x="{M}" y="540" width="{W - 2 * M}" height="1" fill="{INK}"/>')
b.append(F800.path("richardmcallister.app", 22, M, 580))
b.append(F600.path("Independent fan sites", 18, W - M - F600.width("Independent fan sites", 18), 579, 0, MUTE))
# double rule under the masthead
b.append(f'<rect x="{M}" y="186" width="{W - 2 * M}" height="2" fill="{INK}"/><rect x="{M}" y="192" width="{W - 2 * M}" height="2" fill="{INK}"/>')
b.append(SERIF_I.path("Nine sites I build about United, Celtic, Irish sport,", 30, M, 250, 0, MUTE))
b.append(SERIF_I.path("Dylan, Led Zeppelin and Billy Connolly.", 30, M, 290, 0, MUTE))

def column(x, w, head, items, y=340):
    out = [F900.path(head, 20, x, y), f'<rect x="{x}" y="{y + 12}" width="{w}" height="4" fill="{INK}"/>']
    yy = y + 16
    for name, col in items:
        yy += 46
        out.append(F800.path(name, 24, x, yy - 14, -0.01, col))
        out.append(f'<rect x="{x}" y="{yy}" width="{w}" height="1" fill="{HAIR}"/>')
    return out

# Sport takes two narrow columns, music and comedy one, like the front page's rail
cw = (W - 2 * M - 2 * 40) / 3
b += column(M, cw, "Sport", SPORT[:3])
b += column(M + cw + 40, cw, " ", SPORT[3:])
b += column(M + 2 * (cw + 40), cw, "Music and comedy", MUSIC)

svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{"".join(b)}</svg>'
with tempfile.NamedTemporaryFile("w", suffix=".svg", delete=False) as t:
    t.write(svg)
subprocess.run(["rsvg-convert", "-w", str(W), "-h", str(H), t.name, "-o", OUT], check=True)
os.unlink(t.name)
print("wrote", OUT)
