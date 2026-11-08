---
name: richardmcallister.app
description: The back pages of a Sunday broadsheet that covers only Richard's teams and Dylan.
colors:
  newsprint: "#FBFAF7"
  press-ink: "#111110"
  byline-grey: "#4E4D49"
  column-hairline: "#CFCCC4"
  logo-plate: "#FFFFFF"
  dylan-ground: "#171513"
  highlighter: "#FFE27A"
  united-red: "#DA020E"
  limerick-green: "#00693E"
  ireland-football-green: "#0B6E4F"
  ireland-rugby-green: "#0A6B3D"
  dylan-brick: "#B3261E"
  footballclub-ink: "#111110"
  night-newsprint: "#141311"
  night-ink: "#EEEBE4"
  night-byline-grey: "#B9B5AC"
  night-hairline: "#3A3833"
  night-logo-plate: "#F2EFE8"
  night-highlighter: "#6B5A12"
  night-united-red: "#FF3B3B"
  night-limerick-green: "#3FBE74"
  night-ireland-football-green: "#2FB58A"
  night-ireland-rugby-green: "#48B979"
  night-dylan-brick: "#D9675A"
typography:
  display:
    fontFamily: "Libre Franklin, Franklin Gothic Medium, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(40px, 6.2vw, 84px)"
    fontWeight: 900
    lineHeight: 0.92
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "Libre Franklin, Franklin Gothic Medium, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(36px, 4.6vw, 62px)"
    fontWeight: 900
    lineHeight: 0.98
    letterSpacing: "-0.03em"
  page-head:
    fontFamily: "Libre Franklin, Franklin Gothic Medium, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(28px, 3vw, 40px)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Libre Franklin, Franklin Gothic Medium, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(26px, 2.5vw, 34px)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "-0.025em"
  column-head:
    fontFamily: "Libre Franklin, Franklin Gothic Medium, Helvetica Neue, Arial, sans-serif"
    fontSize: "17px"
    fontWeight: 900
    lineHeight: 1.2
  standfirst:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "21px"
    fontWeight: 400
    lineHeight: 1.45
  body:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.55
  link:
    fontFamily: "Libre Franklin, Franklin Gothic Medium, Helvetica Neue, Arial, sans-serif"
    fontSize: "16px"
    fontWeight: 600
    lineHeight: 1.3
  action:
    fontFamily: "Libre Franklin, Franklin Gothic Medium, Helvetica Neue, Arial, sans-serif"
    fontSize: "16px"
    fontWeight: 800
  label:
    fontFamily: "Libre Franklin, Franklin Gothic Medium, Helvetica Neue, Arial, sans-serif"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1.5
    fontFeature: "tnum"
  agate:
    fontFamily: "Libre Franklin, Franklin Gothic Medium, Helvetica Neue, Arial, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.35
    fontFeature: "tnum"
rounded:
  none: "0px"
  logo-xs: "3px"
  logo-sm: "4px"
  logo-md: "6px"
  logo-lg: "8px"
spacing:
  page-edge: "20px"
  column: "22px"
  gutter: "40px"
  tap: "44px"
  xs: "6px"
  sm: "12px"
  md: "16px"
  lg: "22px"
  xl: "44px"
components:
  button-another:
    backgroundColor: "transparent"
    textColor: "{colors.press-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0 14px"
    height: "44px"
  button-another-hover:
    backgroundColor: "{colors.press-ink}"
    textColor: "{colors.newsprint}"
  edition-toggle:
    backgroundColor: "transparent"
    textColor: "{colors.press-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0 12px"
    height: "44px"
  edition-toggle-active:
    backgroundColor: "{colors.press-ink}"
    textColor: "{colors.newsprint}"
  link-open:
    textColor: "{colors.united-red}"
    typography: "{typography.action}"
    height: "44px"
  section-nav-link:
    textColor: "{colors.united-red}"
    typography: "{typography.action}"
    height: "44px"
  site-link-row:
    textColor: "{colors.press-ink}"
    typography: "{typography.link}"
    padding: "9px 0"
    height: "46px"
  site-mark:
    backgroundColor: "{colors.logo-plate}"
    rounded: "{rounded.logo-lg}"
    size: "56px"
---

# Design System: richardmcallister.app

## Overview

**Creative North Star: "The Sunday Back Pages"**

The site is the back pages of a Sunday broadsheet that covers only Richard's teams and Dylan. It reads as a printed page: a heavy grotesque masthead with today's date over a double rule, a section bar, a front of three columns split by hairlines, then one section per site, an agate table and a bylined column. Real archive stories lead, and the sites are the sections. Every story ends in a link into its site.

The page is dense in the way a newspaper is dense. Columns, rules and type weight carry the structure. There are no boxes, cards or shadows. The ground is newsprint white by day and a warm near-black in the Night edition, and the ink is black or bone. The only colour on the page is each site's own colour, and it stays inside that site's section as rules, names and links, next to the site's real logo, which is its section mark. That keeps each site recognisable while the page reads as one paper rather than a fan-site directory.

Confirmed rejections: the generic fan-site look (crests as decoration, sports-graphics clichés), gimmicks and costume (a teletext version was tried and turned down as hard to read and not his world), and the category default of a hero headline over a row of equal site cards.

**Key Characteristics:**
- Libre Franklin at 800 to 900 for everything you scan; Source Serif 4 for everything you read.
- Structure from rules: 5px double under the masthead and page heads, a 1px ink rule under the section bar and front, 1px hairlines between columns and rows, 3 to 6px colour rules on top of each site's section.
- A site's colour appears only inside its own section.
- Two editions, Day and Night, plus Auto, chosen in the colophon.
- Square everywhere except the logos.

## Colors

Black ink on newsprint, with one owned colour per site and nothing else.

### Primary
There is no house accent. Each site's colour is the primary colour inside its own section and appears nowhere else.
- **United Red** (`united-red`; night `night-united-red`): manutd.wiki's section rule, name, links and the lead story, which comes from the United archive.
- **Limerick Green** (`limerick-green`; night `night-limerick-green`): limerickhurling.wiki's section.
- **Ireland Football Green** (`ireland-football-green`; night `night-ireland-football-green`): irelandfootball.wiki's section.
- **Ireland Rugby Green** (`ireland-rugby-green`; night `night-ireland-rugby-green`): irelandrugby.wiki's section.
- **Dylan Brick** (`dylan-brick`; night `night-dylan-brick`): bobdylan.app's section and the Music column.
- **footballclub Ink** (`footballclub-ink`, the same value as ink; night `night-ink`): the early-preview footballclub.wiki gets no colour of its own until it ships one.

### Neutral
- **Newsprint** (`newsprint`; night `night-newsprint`): the page ground.
- **Press Ink** (`press-ink`; night `night-ink`): all text, the masthead and every structural rule (`--rule` matches ink), focus rings, and the pressed state of the edition toggle.
- **Byline Grey** (`byline-grey`; night `night-byline-grey`): secondary text such as fixture descriptions, competition names in the results strip, the colophon, the agate "Why" column and stats.
- **Column Hairline** (`column-hairline`; night `night-hairline`): 1px rules between columns, list rows and table rows.
- **Logo Plate** (`logo-plate`; night `night-logo-plate`): the plate behind logos that need a light ground. Logos with a transparent background drop the plate.
- **Dylan Ground** (`dylan-ground`): the fixed dark ground behind the bobdylan.app logo figure in the Music column. It is the same in both editions.
- **Highlighter** (`highlighter`; night `night-highlighter`): text selection only.

### Named Rules
**The Own Colour Rule.** A site's colour is set on its section through the `--c` custom property and is used only there: the top rule, the site name's subtitle, the dateline, link hovers, the arrows and the "Open" link. Shared furniture (masthead, section rules, toggles, agate, About) is ink. If a colour shows up outside its site's section, it is in the wrong place.

**The Two Editions Rule.** Every colour is a token in the `site.css` `:root` block and is redefined for Night under both `prefers-color-scheme: dark` (unless `data-theme="light"`) and `:root[data-theme="dark"]`. Night site colours are lighter versions of the same hues, not new hues. Never write a literal colour in a component.

## Typography

**Display Font:** Libre Franklin (with Franklin Gothic Medium, Helvetica Neue, Arial), self-hosted at 400, 600, 800 and 900
**Body Font:** Source Serif 4 (with Georgia, Times New Roman), self-hosted at 400, 400 italic and 600

**Character:** A heavy American news grotesque set tight for headlines against a calm, readable text serif. It is the newspaper pairing, used straight and without costume.

### Hierarchy
- **Display** (900, clamp 40 to 84px, 0.92, -0.035em): the masthead name only. The 404 headline uses the same voice at clamp 40 to 76px.
- **Headline** (900, clamp 36 to 62px, 0.98, -0.03em, balanced wrap): the lead story on the front.
- **Page head** (900, clamp 28 to 40px, 1, -0.025em): page-level heads such as "The sites", set over a 5px double rule.
- **Title** (900, clamp 26 to 34px, 1, -0.025em): a site's name in its section, with a 600 15px subtitle in the site colour. The Dylan night head (clamp 24 to 30px) and the smaller site briefs (22px) step down from it.
- **Column head** (900, 17px, 1.2): front-page column heads and secondary section heads, set over a 3px rule in the column's colour or ink.
- **Standfirst** (400 italic, 21px, 1.45): the serif italic under the lead headline.
- **Body** (400, 18px, 1.55; 17px under 720px): reading text, capped between 46ch and 62ch depending on the column. Decks run at 19 to 21px.
- **Link** (600, 16px, 1.3): link rows in a site's section.
- **Action** (800, 15 to 16px): "Open" links, the section bar (15px) and run-in datelines.
- **Label** (600, 14px, 1.5, tabular figures): the masthead dateline, metadata lines, the colophon and the edition toggle.
- **Agate** (400 or 800, 15px, 1.35, tabular figures; heads 800 13px): the "How they're built" table.

### Named Rules
**The Two Faces Rule.** Franklin is for anything you scan (heads, navigation, links, labels, tables, scores). Source Serif is for anything you read through (standfirsts, decks, stories, the About column). Do not mix them within one role.

**The Run-in Dateline Rule.** A story's source and date open its first paragraph as a run-in (Franklin 800 at 0.82em, in the site colour, with a 20px logo). They never sit above the headline.

**The Typographic Apostrophe Rule.** Use curly quotes and apostrophes (’ “ ”) and proper en dashes in ranges (1886–87). Never use straight quotes in copy.

## Layout

The page is a single 1320px measure with a 20px minimum edge (larger where the safe area needs it). Everything snaps to whole column modules, and columns are separated by 1px hairlines rather than gaps. Column padding is 22px (`--col`) and the gutter between paired sections is 40px (`--gut`).

- **Masthead:** the name on the left, a two-line dateline on the right (desk, live date, Skåne), then a 5px double rule and a wrapping section bar closed by a 1px ink rule. The section bar names every site in its colour; "How they're built" and "About" are pushed to the right.
- **Front:** three columns at 2fr / 1fr / 1fr. The lead story is in the wide column and its body runs as two newspaper columns (28px gap).
- **Sections:** one site per section, never crowded. United leads the Sport group, and the three Irish sites share the column beside it as briefs. Dylan gets a two-column section with its links set as a setlist. "How they're built" and About sit as a pair.
- **Rhythm:** 22px between blocks, 44px before page heads, 48px before the colophon, and 12 to 16px within a block.
- **At 1060px or less:** the lead spans the full width and the other two columns pair up under it.
- **At 720px or less:** everything stacks into one column with hairlines between, the lead body goes to one column, the results strip stacks, the section bar drops its right-hand links, and the Dylan figure is capped at 280px.

## Elevation & Depth

The page is flat, like newsprint. There are no shadows, gradients or blur. Hierarchy comes from rule weight and type weight, from heaviest to lightest: the 5px double rule (masthead, page heads, colophon), the 6px colour rule (each site's section and the setlist), the 3px colour or ink rule (column heads, briefs, results strip), the 2px ink rule (agate head), the 1px ink rule (section bar, front, results strip base) and the 1px hairline (columns, rows).

### Named Rules
**The Printed Page Rule.** If something needs separating, use a rule. If it needs emphasis, use weight. Nothing floats above the page.

## Shapes

Square everywhere: buttons, toggles, rules and figures have a radius of 0. The only rounded corners are on the logo plates, scaled to their size (3px at 20px, 4px at 30px, 6px at 40px, 8px at 56px), so a logo reads as a printed mark on its plate. Arrows are drawn by an SVG mask on currentColor (a 16-unit square-capped stroke at 0.8em), so they always take the link's colour.

## Components

### Buttons
Plain and square, in ink, sized for a thumb.
- **Shape:** square (0px).
- **"Another night":** transparent, Franklin 800 14px in ink, a 1px ink border, 44px tall, 14px padding. Hover inverts it to ink with newsprint text.
- **Edition toggle (Auto / Day / Night):** a labelled group in the colophon. The buttons use Franklin 600 at the colophon size with a 1px hairline border, 44px tall and 12px padding. Hover darkens the border to ink. The pressed button (`aria-pressed="true"`) is filled with ink. The choice is stored in `localStorage` as `rm-theme`.
- **Focus:** every focusable element gets a 3px ink outline offset by 3px.

### Links
- **"Open" link:** Franklin 800 16px in the site colour, no underline, at least 44px tall, ending in the masked arrow. Hover adds a 2px underline and moves the arrow 3px right over 0.2s on `cubic-bezier(.2,.7,.2,1)`.
- **Site link row:** a full-width row, at least 46px tall (54px in the lead section), Franklin 600 16px in ink, with a hairline below and an arrow in the site colour. Hover turns the text to the site colour.
- **Fixture row:** a 30px logo spanning two lines, the name in Franklin 800 16px in the site colour, and a Byline Grey 14px description. Hover underlines the name.

### Navigation
- **Section bar:** Franklin 800 15px (14px on mobile), each site in its own colour and the rest in ink, at least 44px tall, wrapping with 26px gaps. Hover adds a 2px underline.

### Section head (signature)
A site's section opens with a 6px rule in its colour, then its real logo (56px, on a plate where needed) beside the site name in Title type and a subtitle in the site colour. A deck, link rows and the "Open" link follow. Briefs use the same structure at a smaller size (3px rule, 40px logo, 22px name).

### Results strip
The final score set as a line of type: home, competition and away on a three-part grid in Franklin 800 20px with tabular figures, between a 3px rule in the site colour and a 1px ink rule. The competition is in Byline Grey 14px.

### Agate table
Franklin 15px with tabular figures. An 800 13px head row over a 2px ink rule, hairlines between rows, the first column in 800 and the last in Byline Grey.

### Byline
The RMC mark at 40px tall (`rmc-mark.svg` by day, `rmc-mark-on-dark.svg` by night), then the name in Franklin 900 20px and the place in Byline Grey 14px.

### Dylan night
The Music column shows a different real night from the archive each time "Another night" is pressed. The text fades out and back in over 0.25s, and the fade is turned off under `prefers-reduced-motion`.

## Do's and Don'ts

### Do:
- **Do** set every colour as a `:root` token in `site.css` and redefine it for Night under both the `prefers-color-scheme` and `data-theme` selectors.
- **Do** pass a site's colour in through `--c` on its section, and keep it within that section's rules, names and links.
- **Do** use the site's real logo as its section mark, on the logo plate unless the logo has a transparent background.
- **Do** separate content with rules (5px double, 6px or 3px colour, 1px ink, 1px hairline), never with boxes.
- **Do** put a story's source and date in a run-in dateline at the start of the first paragraph.
- **Do** keep every tap target at least 44px tall.
- **Do** draw arrows and icons as SVG masks or inline SVG on currentColor.
- **Do** use typographic apostrophes, quotes and en dashes.
- **Do** end every story with a link into its site.

### Don't:
- **Don't** put kickers or eyebrows above headlines.
- **Don't** use hero-metric figures. Numbers belong in running text, the results strip and the agate table.
- **Don't** number lists that aren't sequences.
- **Don't** use font glyphs for arrows or icons.
- **Don't** add shadows, gradients, cards or rounded containers; only logo plates are rounded.
- **Don't** use a site's colour outside its own section, or introduce a house accent colour.
- **Don't** use crests as decoration, sports-graphics clichés or any costume treatment such as teletext.
- **Don't** use straight quotes or apostrophes in copy.
