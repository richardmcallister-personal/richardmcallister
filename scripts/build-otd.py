#!/usr/bin/env python3
"""Build the "On your birthday" data for richardmcallister.app.

Reads the public data files of each of Richard's sites and writes one small
JSON file per month to public/data/otd/MM.json, keyed by "MM-DD":

  {"11-08": [[year, site, headline, detail, path], ...], ...}

site is one of: mu, cel, lim, irf, irr, bd, lz (base URLs live in index.html).
path is appended to that site's base URL. Nothing is fetched by visitors'
browsers from the other sites; the homepage only reads these files.

Run:  python3 scripts/build-otd.py      (re-run whenever you want fresh data)
"""
import json, os, sys, urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

OUT = os.path.join(os.path.dirname(__file__), "..", "public", "data", "otd")
UA = {"User-Agent": "richardmcallister.app on-this-day builder"}

def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

DAYS = defaultdict(list)          # "MM-DD" -> entries
def add(date, site, head, detail, path):
    if not date or len(date) < 10 or date[4] != "-":
        return
    DAYS[date[5:10]].append([int(date[:4]), site, head, detail, path])

def result(gf, ga):
    return "Won" if gf > ga else "Lost" if gf < ga else "Drew"

def season_of(date):            # football seasons start in July
    y, m = int(date[:4]), int(date[5:7])
    return y if m >= 7 else y - 1

# ---------- Manchester United (manutd.wiki) ----------
def united():
    seasons = [s["id"] for s in get("https://manutd.wiki/history/all.json")]
    with ThreadPoolExecutor(8) as ex:
        data = list(ex.map(lambda s: get(f"https://manutd.wiki/history/data/{s}.json"), seasons))
    n = 0
    for d in data:
        league = d.get("div") or "League"
        for r in d.get("results", []):
            if r.get("gf") is None:
                continue
            comp = {"L": league, "FAC": "FA Cup", "LC": "League Cup"}.get(r.get("c"), r.get("c") or "")
            if r.get("r"):
                comp += (" " if comp.endswith("Cup") else ", ") + r["r"].lower() if r["r"] != "Final" else " final"
            if r.get("tie") == "replay":
                comp += " replay"
            venue = "at" if r.get("h") is False and not r.get("n") else "v"
            head = f"{result(r['gf'], r['ga'])} {r['gf']}–{r['ga']} {venue} {r['o']}"
            if r.get("aet"):
                head += " after extra time"
            add(r["d"], "mu", head, comp, f"/history/season/?s={d['id']}")
            n += 1
    return n

# ---------- Celtic (celtic.richardmcallister.app) ----------
def celtic():
    n = 0
    for g in get("https://celtic.richardmcallister.app/history/matches.json"):
        if g.get("gf") is None or not g.get("d"):
            continue
        venue = "at" if g.get("h") == -1 else "v"
        head = f"{result(g['gf'], g['ga'])} {g['gf']}–{g['ga']} {venue} {g['o']}"
        if g.get("aet"):
            head += " after extra time"
        comp = g.get("t") or ""
        rnd = (g.get("r") or "").replace("-round", " round")
        if rnd and comp != "League" and not rnd.startswith("Matchday"):
            comp += ", " + rnd.lower()
        add(g["d"], "cel", head, comp, f"/results/?season={g.get('y') or season_of(g['d'])}")
        n += 1
    return n

# ---------- Limerick hurling (limerickhurling.wiki) ----------
LIM_COMP = {"MSHC": "Munster Championship", "AISHC": "All-Ireland Championship", "NL": "National League"}
def limerick():
    n = 0
    for m in get("https://limerickhurling.wiki/history/matches.json"):
        if not m.get("d") or m.get("gf") is None or not m.get("u") or m["u"][0] is None:
            continue
        us, them = m["u"], m["o"]
        venue = "at" if m.get("h") == "A" else "v"
        head = f"{result(m['gf'], m['ga'])} {us[0]}-{us[1]} to {them[0]}-{them[1]} {venue} {m['opp']}"
        comp = LIM_COMP.get(m.get("cn"), m.get("cn") or "")
        if m.get("rnd"):
            comp += ", " + m["rnd"].lower()
        add(m["d"], "lim", head, comp, f"/match/?id={m['id']}")
        n += 1
    return n

# ---------- Ireland football (irelandfootball.wiki) ----------
def ireland_football():
    n = 0
    for m in get("https://irelandfootball.wiki/history/matches.json"):
        if m.get("gf") is None:
            continue
        venue = "at" if m.get("h") == -1 else "v"
        head = f"{result(m['gf'], m['ga'])} {m['gf']}–{m['ga']} {venue} {m['o']}"
        place = m.get("city") or ""
        detail = m.get("t") or ""
        if place:
            detail += f" · {place}"
        path = f"/match/?id={m['id']}" if m.get("id") else f"/report/?d={m['d']}"
        add(m["d"], "irf", head, detail, path)
        n += 1
    return n

# ---------- Ireland rugby (irelandrugby.wiki): Ireland and the four provinces ----------
def ireland_rugby():
    n = 0
    for m in get("https://irelandrugby.wiki/api/history"):
        if not m.get("score") or m.get("state") not in ("Finished", "Finished after extra time"):
            continue
        hs, as_ = m["score"]
        head = f"{m['h']['n']} {hs}–{as_} {m['a']['n']}"
        add(m["date"][:10], "irr", head, m.get("compName") or "", f"/match/?id={m['id']}")
        n += 1
    return n

# ---------- Concerts: bobdylan.app and ledzeppelin.app ----------
def concerts(base, site):
    idx = get(base + "/data/index.json")
    years = [y["y"] if isinstance(y, dict) else y for y in idx["years"]]
    with ThreadPoolExecutor(8) as ex:
        data = list(ex.map(lambda y: get(f"{base}/data/years/{y}.json"), years))
    n = 0
    for shows in data:
        for c in shows:
            sets = c.get("sets") or []
            opener = next((s["s"][0]["n"] for s in sets if s.get("s")), None)
            head = ", ".join(x for x in (c.get("v"), c.get("c")) if x)
            detail = f"Opened with {opener}" if opener else (c.get("t") or c.get("cn") or "")
            add(c["d"], site, head, detail, f"/concert/?id={c['id']}")
            n += 1
    return n

def main():
    counts = {
        "mu": united(), "cel": celtic(), "lim": limerick(), "irf": ireland_football(),
        "irr": ireland_rugby(), "bd": concerts("https://bobdylan.app", "bd"),
        "lz": concerts("https://ledzeppelin.app", "lz"),
    }
    os.makedirs(OUT, exist_ok=True)
    for month in range(1, 13):
        mm = f"{month:02d}"
        days = {k: sorted(v, key=lambda e: e[0]) for k, v in sorted(DAYS.items()) if k.startswith(mm)}
        with open(os.path.join(OUT, f"{mm}.json"), "w") as f:
            json.dump(days, f, ensure_ascii=False, separators=(",", ":"))
    print("records:", counts, "total:", sum(counts.values()), "dates:", len(DAYS))

if __name__ == "__main__":
    sys.exit(main())
