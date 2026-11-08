---
version: 1
slug: "public-index-html"
primary_target: "public/index.html"
related_targets: ["public/404.html"]
---

# Homepage (richardmcallister.app)

Scope: the homepage and the 404 page. Visitor mode: Experience (the sites are the work; the page is the way in).
Audience and job: mainly Richard, often on a phone around match day, getting into one of his sites in one tap. Incidental fans should still find their way.
Constraints: light and dark themes plus the auto/light/dark toggle must survive. Nothing that reads as a generic fan site (crests as decoration, sports-graphics clichés). Real content only; the archive moments and the Dylan show list are real data. Static, no build step, Cloudflare Workers assets.
Success: memorable. Someone who visits once remembers it.
Unresolved: whether the RMC lockup returns on the redesigned page (the user did not keep it as a constraint; favicons and the share image still use it).

## Direction contract

THESIS: The homepage is a teletext service, Richard's own Aertel/Ceefax: every site is a numbered page you can call up. It refuses the category default of a hero over a grid of equal site cards.
OWN-WORLD: Black screen; the seven teletext colours at full saturation (white, yellow, cyan, green, magenta, red, blue as background only); a self-drawn 40-column teletext face with character rounding; double-height titles; blue-band mosaic sixel graphics; coloured title bands per page; dot leaders to page numbers; a coloured Fastext row. Light theme is the same service as a printout: white paper, the colours darkened for ink, bands kept.
STORY: The visitor sees P100, an index of the sites with page numbers, a live Skåne clock in the header. They tap a row to go straight to a site, or call up a page (type a number or use Fastext) to read about one: archive results, the Dylan show of the moment, how the sites are built, who runs them.
FIRST VIEWPORT: Teletext header row at top (P-number entry, RMC 100, date, live clock in yellow). Rows 2-5: blue band with yellow mosaic RMC and the line "Independent fan sites for sport and music". Then double-height SPORT and MUSIC section heads over index entries (title in site colour, dot leaders, white page number, domain line under). Fastext row at the bottom: red United, green Ireland, yellow Dylan, cyan About. Primary action: each index row opens its site.
FORM: Teletext pages (Aertel/Ceefax), grounded candidate 1 of 7 (Impeccable's pick, chosen by the user). seed:e83adcee46273ded
SIGNATURE: typing a page number rolls the header counter through pages until it lands, then the page paints in row by row; the Dylan page rotates real archive shows as numbered subpages (1/8, 2/8 ...). Raised from declined challengers: light only on the active thing (bioluminescent sea): index rows invert to their colour on hover or focus; one fixed scale and baseline across every page (botanical folio): every page is the same 40-column grid; one even line weight with colour saved for what matters (ligne claire).
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
