# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
Primarily Richard himself: richardmcallister.app is his personal launchpad to the sites he builds and uses, on match day or when looking up a Dylan setlist. Other visitors (fans who land here, anyone following a link from GitHub) are incidental. They should still be able to find their way, but the page isn't shaped around winning them over.

## Product Purpose
A single page that lists Richard's independent fan sites and gets you into the right one fast. A visit succeeds when it ends with a click into a site: manutd.wiki, limerickhurling.wiki, irelandfootball.wiki, irelandrugby.wiki, bobdylan.app, or the early footballclub.wiki preview.

## Positioning
One person's own stack of fan sites, built for his own use: United since childhood, Limerick in the blood, Ireland whatever the sport, Dylan on the stereo. It's a personal index, not a portfolio pitch or an agency site.

## Operating Context
- Used to jump to a site, often on a phone and often around match days.
- Each site card links to that site's main tasks: next match and where to watch, fixtures, results and tables, setlists, and archive moments (e.g. the 1886 FA Cup tie, the 1966 "Judas!" show).
- "Also building" covers footballclub.wiki (358 clubs in 19 leagues, early preview) and a planned combined Irish sport calendar feed. "How they're built" and "About" sections give background.

## Capabilities and Constraints
- Static site: everything lives in `public/` (`index.html`, `site.css`, `404.html`, brand assets, per-site logos). No build step, no Worker script.
- Deployed as Cloudflare Workers static assets (`wrangler.jsonc`), custom domains `richardmcallister.app` and `www`. Pushes to `main` deploy automatically.
- Light and dark themes, with the choice stored in `localStorage` (`rm-theme`).
- Working rules in `CLAUDE.md`: every colour goes through a `:root` token in `site.css`, redefined for dark mode; bump the `?v=` stamp on the `site.css` link in every HTML file when the CSS changes; `node --check` the inline script; check light and dark at 1280 and 390 wide with no horizontal overflow; commit as Richard.
- `tesla.richardmcallister.app` is a separate project and must not be routed here.
- Undecided: whether and when the combined Irish sport calendar ships.

## Brand Commitments
- RMC brand kit in `public/brand/` (three-key logo, lockups, mark). Only the C key is ever orange. At 32px and below, use the C key on its own.
- Favicons, app icons, the manifest and the share image (`og-image-1200x630.png`) come from the same logo pack.
- Voice: first person, plain and warm, sentence case.
- Disclaimer stays: "Independent fan sites, built and run by me. Not affiliated with any club, union or artist."

## Evidence on Hand
- Real site logos in `public/logos/` and real copy and archive moments for each site in `public/index.html`.
- The "How they're built" stack table (static HTML and Hugo, Cloudflare Workers, Worker proxy with KV cache, Claude Code as build partner).
- No testimonials, traffic figures or press coverage. Don't invent any.

## Product Principles
1. Get Richard to the site he wants in one tap; everything else is secondary.
2. Each site keeps its own identity inside one shared system.
3. Small, static and cheap to run: no dependencies the page doesn't need.
4. Honest and independent: real content only, no claimed affiliation.
