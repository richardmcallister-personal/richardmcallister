# richardmcallister.app — working notes for Claude

Static showcase of Richard's sites. No build step, no Worker script: `public/` is served as Workers static assets.

Layout system is manutd.wiki's (see richardmcallister-personal/site1 `static/manutd/mu.css`): white cards `.sheet` radius 18,
masthead band (header + nav), system type, sentence case, 44px tap targets. Colours are Richard's own brand (`public/brand/`):
ink `#16181D` band, off-white `#F6F5F2` ground, orange `#E4572E` accent (logo dot and large marks only; small text uses
`--accent-ink`, which passes contrast). Favicons and the manifest come from the same logo pack.
**Every colour goes through a token in `site.css` `:root`** and is redefined for dark mode; per-site accents are
`--s-*` tokens set on each card via `--acc`.

Rules: commit as Richard (`-c user.name="Richard McAllister" -c user.email=richardmcallister@gmail.com`);
`node --check` the inline script before pushing; check light + dark at 1280 and 390 wide with no horizontal overflow.
`tesla.richardmcallister.app` is a separate project — don't route it here.
