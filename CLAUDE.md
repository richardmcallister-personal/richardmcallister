# richardmcallister.app — working notes for Claude

Static showcase of Richard's sites. No build step, no Worker script: `public/` is served as Workers static assets.

Design: the Sunday back pages of a broadsheet that covers only Richard's teams and his bands, Dylan and Led Zeppelin (see `DESIGN.md` and the direction contract in `.impeccable/surfaces/public-index-html.md`).
Masthead over a double rule; front page with the 1886 archive lead, a Sport column and a Music column; then The sites (United wide, three Irish briefs, Dylan and Led Zeppelin side by side in Music), an agate table and an About column with the RMC mark on the byline.
Libre Franklin for headlines and labels, Source Serif 4 for reading, both self-hosted from `public/fonts/` (no Google Fonts link).
Day edition on newsprint white `#FBFAF7`; Night edition on `#141311`.
**Every colour goes through a token in `site.css` `:root`** and is redefined for dark under both the media query and `[data-theme="dark"]`. Each site's colour (`--mu`, `--lim`, `--irf`, `--irr`, `--bd`, `--lz`) lives only inside its own story or section.
No kickers above headlines (use a run-in dateline), no hero-metric numerals, typographic apostrophes, 44px tap targets.

Rules: commit as Richard (`-c user.name="Richard McAllister" -c user.email=richardmcallister@gmail.com`);
`node --check` the inline script before pushing; check light + dark at 1280 and 390 wide with no horizontal overflow.
`tesla.richardmcallister.app` is a separate project — don't route it here.
When `site.css` changes, bump the `?v=` stamp on its <link> in every HTML file so browsers don't pair new HTML with an old stylesheet.
