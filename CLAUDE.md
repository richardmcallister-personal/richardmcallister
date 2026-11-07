# richardmcallister.app — working notes for Claude

Static showcase of Richard's sites. No build step, no Worker script: `public/` is served as Workers static assets.

Design language is manutd.wiki's (see richardmcallister-personal/site1 `static/manutd/mu.css`): grey ground `--bg`,
white cards `.sheet` radius 18, red masthead band (header + nav), system type, sentence case, 44px tap targets.
**Every colour goes through a token in `site.css` `:root`** and is redefined for dark mode; per-site accents are
`--s-*` tokens set on each card via `--acc`.

Rules: commit as Richard (`-c user.name="Richard McAllister" -c user.email=richardmcallister@gmail.com`);
`node --check` the inline script before pushing; check light + dark at 1280 and 390 wide with no horizontal overflow.
`tesla.richardmcallister.app` is a separate project — don't route it here.
