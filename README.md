# richardmcallister.app

Showcase for Richard McAllister's sites: manutd.wiki, celtic.richardmcallister.app, limerickhurling.wiki, irelandfootball.wiki,
irelandrugby.wiki, bobdylan.app, ledzeppelin.app and billy.richardmcallister.app (plus footballclub.wiki under "Also building").

- `public/` — the whole site: `index.html`, `site.css`, `404.html`, `favicon.svg`, `_headers`
- `wrangler.jsonc` — Cloudflare Workers static-assets deploy, custom domains `richardmcallister.app` + `www`

Deploy: Cloudflare → Workers & Pages → Create → Import a repository → this repo.
Build command: none. Deploy command: `npx wrangler deploy`. Pushes to `main` deploy automatically.

Local preview: `npx wrangler dev` (or open `public/index.html`).

## On your birthday

The homepage section "On your birthday" reads `public/data/otd/01.json` to `12.json`, one file per month,
built from the public data of manutd.wiki, Celtic, limerickhurling.wiki, irelandfootball.wiki,
irelandrugby.wiki (from 2020), bobdylan.app, ledzeppelin.app and the Billy Connolly site (2001 to 2017). Refresh it with:

    python3 scripts/build-otd.py   (then commit public/data/otd)

A shared link can carry the date: `https://richardmcallister.app/?d=11-08#birthday`.
