---
version: 1
slug: "public-index-html"
primary_target: "public/index.html"
related_targets: ["public/404.html"]
---

# Homepage (richardmcallister.app)

Scope: the homepage and the 404 page (the whole of this repo). Visitor mode: Experience (the sites are the work; the page is the way in).
Audience and job: mainly Richard, often on a phone around match day, getting into one of his sites in one tap. Incidental fans should still find their way.
Constraints: light and dark themes plus the auto/light/dark toggle. Nothing that reads as a generic fan site (crests as decoration, sports-graphics clichés), no gimmick or costume, easy reading, and each site keeps its own identity (its logo and colour). Real content only. Static, no build step, Cloudflare Workers assets.
Success: memorable, editorial and confident. Feels like Richard's own.
Rejected: a teletext service (too much of a gimmick, hard to read, not his world, lost the sites' identity).

## Direction contract

THESIS: The site is the back pages of a Sunday broadsheet that covers only Richard's teams and Dylan: real archive stories lead, the sites are the sections. It refuses the category default of a hero headline over a row of equal site cards.
OWN-WORLD: Newsprint-white ground (night edition: warm near-black), black ink. Libre Franklin at heavy weights for masthead, headlines and section heads; Source Serif 4 for reading text. Double rule under the masthead, hairline column rules, thick colour rules under section heads. Each site's own colour is its section colour and its real logo is its section mark; no other colour.
STORY: The visitor reads the front: a masthead with today's date, a lead story from the United archive, a fixtures column into the four sport sites, and a music column with a Dylan night from the archive. Every story ends in a link into its site. Below: one section per site, then how they're built as an agate table, and an About column with a byline.
FIRST VIEWPORT: Masthead (Richard McAllister, live date, Skåne) over a double rule; a section bar naming every site in its colour. Then three columns: lead (2/4 width) with the 1886 headline, results strip and story; Fixtures & results column linking the four sport sites with logos; Music column with the Dylan logo, the archive night and "another night" control. Primary action: every site link and the "Open" link ending each story.
FORM: Sunday back pages (Impeccable's pick in the second hand, chosen by the user from mockups). seed:e83adcee46273ded
SIGNATURE: the Dylan column draws a different real night from the archive on request; the masthead date is today's, in Skåne. Raised from declined challengers: layout snaps to whole column modules (azulejo); one site per section, never crowded (airline ticket wallet).
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
