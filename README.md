# richardmcallister.app

Showcase for Richard McAllister's sites: manutd.wiki, limerickhurling.wiki, irelandfootball.wiki,
irelandrugby.wiki and bobdylan.app.

- `public/` — the whole site: `index.html`, `site.css`, `404.html`, `favicon.svg`, `_headers`
- `wrangler.jsonc` — Cloudflare Workers static-assets deploy, custom domains `richardmcallister.app` + `www`

Deploy: Cloudflare → Workers & Pages → Create → Import a repository → this repo.
Build command: none. Deploy command: `npx wrangler deploy`. Pushes to `main` deploy automatically.

Local preview: `npx wrangler dev` (or open `public/index.html`).
