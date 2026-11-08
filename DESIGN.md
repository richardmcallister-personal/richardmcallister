---
name: richardmcallister.app
description: Richard McAllister's personal launchpad to his independent fan sites for sport and music.
colors:
  paper: "#F6F5F2"
  card-white: "#FFFFFF"
  keycap-ink: "#16181D"
  keycap-base: "#0E1013"
  slate: "#5A5F6B"
  hairline: "#E4E2DC"
  signal-orange: "#E4572E"
  accent-ink: "#B8431F"
  night-ground: "#0E0F12"
  night-card: "#1B1D22"
  night-slate: "#C9CCD3"
  night-hairline: "#33353C"
  night-tint: "#24262C"
  night-accent-ink: "#FF8A65"
  site-united: "#DA020E"
  site-limerick: "#00693E"
  site-ireland-football: "#0B6E4F"
  site-ireland-rugby: "#0A6B3D"
  site-dylan: "#B3261E"
  site-footballclub: "#1D1D1F"
  site-footballclub-night: "#48484A"
typography:
  display:
    fontFamily: "Space Grotesk, SF Pro Display, system-ui, -apple-system, sans-serif"
    fontSize: "clamp(38px, 6.4vw, 74px)"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.03em"
  headline:
    fontFamily: "Space Grotesk, SF Pro Display, system-ui, -apple-system, sans-serif"
    fontSize: "17px"
    fontWeight: 600
  title:
    fontFamily: "Space Grotesk, SF Pro Display, system-ui, -apple-system, sans-serif"
    fontSize: "19px"
    fontWeight: 600
    lineHeight: 1.1
  score:
    fontFamily: "Space Grotesk, SF Pro Display, system-ui, -apple-system, sans-serif"
    fontSize: "20px"
    fontWeight: 600
    lineHeight: 1.2
    fontFeature: "tnum"
  body:
    fontFamily: "SF Pro Text, system-ui, -apple-system, BlinkMacSystemFont, Inter, Segoe UI, Roboto, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.45
  body-small:
    fontFamily: "SF Pro Text, system-ui, -apple-system, BlinkMacSystemFont, Inter, Segoe UI, Roboto, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: "Space Grotesk, SF Pro Display, system-ui, -apple-system, sans-serif"
    fontSize: "13px"
    fontWeight: 600
  micro-label:
    fontFamily: "Space Grotesk, SF Pro Display, system-ui, -apple-system, sans-serif"
    fontSize: "11px"
    fontWeight: 600
rounded:
  chip: "4px"
  nav: "6px"
  control: "8px"
  tile: "10px"
  key: "12px"
  card: "18px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "20px"
  section: "22px"
components:
  button-keycap:
    backgroundColor: "{colors.keycap-ink}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    rounded: "{rounded.key}"
    padding: "0 16px"
    height: "44px"
  button-keycap-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.keycap-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.key}"
    padding: "0 16px"
    height: "44px"
  button-on-band:
    backgroundColor: "{colors.card-white}"
    textColor: "{colors.site-dylan}"
    typography: "{typography.label}"
    rounded: "{rounded.control}"
    padding: "0 16px"
    height: "44px"
  card-sheet:
    backgroundColor: "{colors.card-white}"
    textColor: "{colors.keycap-ink}"
    rounded: "{rounded.card}"
    padding: "18px 20px"
  site-card:
    backgroundColor: "{colors.card-white}"
    textColor: "{colors.keycap-ink}"
    rounded: "{rounded.card}"
  site-card-band:
    backgroundColor: "{colors.site-united}"
    textColor: "{colors.card-white}"
    padding: "16px 18px 14px"
  nav-link:
    backgroundColor: "transparent"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    rounded: "{rounded.nav}"
    padding: "9px 13px"
  chip:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.keycap-ink}"
    rounded: "{rounded.chip}"
    padding: "3px 7px"
  stat-tile:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.slate}"
    typography: "{typography.body-small}"
    rounded: "{rounded.tile}"
    padding: "8px 12px"
---

# Design System: richardmcallister.app

## Overview

**Creative North Star: "The Keyring"**

Every site Richard runs is a key on one ring, and this page is the ring. Each site card is a key you grab and go: it carries its own club or artist colour in a solid band at the top, while everything around it (the ink masthead, the paper ground, the white cards) stays the same for every site. The RMC three-key logo and the keycap buttons, which press down when you click them, are the signature details. The page should feel plain, warm and tactile: like a well-worn set of keys, not a pitch deck.

The page is quiet so the sites' colours can be loud. Neutrals are slightly warm (paper, not grey), there is one brand accent, and type is set in sentence case with Space Grotesk for anything that labels or announces and the system font for reading. Layout is a single centred column of white cards on paper. It's dense enough to scan on a phone around match day, with 44px tap targets throughout. Depth is minimal: surfaces sit flat, lift slightly when you hover, and the keycaps press.

**Key Characteristics:**
- Ink masthead band across the full width that runs on into a big-type hero; paper ground; white cards with 18px corners.
- Per-site colour bands carry each site's identity; the frame around them never changes.
- One brand accent, signal orange, kept to the logo's C key and large marks.
- Keycap buttons with a solid base that presses down.
- Light and dark themes defined entirely through tokens.

## Colors

Warm neutrals, one signal accent, and a set of borrowed club colours that each live only inside their own card.

### Primary
- **Signal Orange**: the RMC brand accent. Used for the C key in the logo, the logo dot and large marks only. It does not pass contrast as small text, so it is never used there.
- **Accent Ink**: the text-safe partner of signal orange, used for "Open …" links, arrows in link lists, hover colour on footer links, the highlighted word in the hero headline, and focus outlines on site cards. In dark mode it becomes **Night Accent Ink**.

### Secondary
- **Site colours** (United red, Limerick green, Ireland football green, Ireland rugby green, Dylan red, footballclub near-black): each site's own theme colour, set on its card as that card's accent. They fill the card's top band, colour its bullet dots, and colour the text of the button that sits on the band. footballclub's near-black lightens to **Site Footballclub Night** in dark mode so the band doesn't disappear.

### Neutral
- **Keycap Ink**: the masthead band, primary text, h2 underline rules, keycap button fill and the logo tile. In dark mode, text and keycap fill swap to paper while the masthead stays ink.
- **Paper**: the page ground, text on the masthead, chips and stat tiles. It's a warm off-white, not a grey.
- **Card White**: every card and sheet surface. Becomes **Night Card** in dark mode.
- **Slate**: secondary text, intro paragraphs, sub-labels, table headers and footer text. Becomes **Night Slate** in dark mode.
- **Hairline**: list dividers, table row rules, the ghost button border and footer separators. Becomes **Night Hairline** in dark mode.
- **Keycap Base**: the solid 4px base under keycap buttons.
- **Night Ground** and **Night Tint**: the dark-mode page ground and the tile/chip fill.

### Named Rules
**The One Orange Key Rule.** Only the C key is ever orange. Signal orange appears on the logo and large marks; small text and links use accent ink instead.

**The Token-Only Rule.** Every colour goes through a token in the `:root` block of `site.css` and is redefined for dark mode. No colour value is written straight into a rule unless it is a translucent overlay on an already-tokened surface.

**The Borrowed Colours Rule.** A site's colour lives only inside that site's card. It never tints the masthead, the page ground or another card.

## Typography

**Display Font:** Space Grotesk (with SF Pro Display and system-ui fallbacks)
**Body Font:** system UI stack (SF Pro Text, system-ui, Inter, Segoe UI, Roboto)

**Character:** Space Grotesk is slightly mechanical and keyboard-like, which matches the keycap world. It handles everything that labels or announces. The system font does the reading so text loads instantly and feels native on each device.

### Hierarchy
- **Display**: the hero headline only, set in paper on the ink band, capped at 13 characters per line. Its closing phrase ("get going") is the page's one large signal-orange mark.
- **Headline**: section heads ("The sites", "Also building"). Inside sheets, h2s are 15px with a 2px ink underline sized to the text.
- **Title**: the domain name on each site band, with a 12px descriptor below it at regular weight.
- **Score**: archive scorelines and show venues on the bands, with tabular figures. The score itself is set at weight 300.
- **Body**: paragraphs, with intro text capped at 62 characters per line. Card copy runs 15px; lists, stat tiles and footer links run 14px.
- **Label**: navigation, buttons and "Open …" links.
- **Micro label**: band eyebrows ("From the archive"), table headers and footer column heads. Sentence case, never uppercase.

### Named Rules
**The Sentence Case Rule.** Every heading, label, button and nav item is in sentence case. No all-caps eyebrows, no letter-spaced shouting.

**The Two Voices Rule.** Space Grotesk labels and announces; the system font explains. Don't set paragraphs in Space Grotesk or headings in the system font.

## Layout

The page is a single column, centred, at most 1080px wide, with a 16px side gutter that respects safe-area insets. The masthead's ink band runs on, full width, into the hero, so the page opens on one dark block holding the logo, nav and headline. Below it, content is a stack of white sheets with 12px between them. The site cards form a grid: one column on phones, two from 700px (the fourth card spans both columns so the grid stays even), and three from 980px. Cards marked wide (manutd.wiki, bobdylan.app) span the full row; from 700px they split side by side, with a 360px colour band on the left and the body on the right. Spacing steps between 4, 8, 12, 16 and 20px. Cards pad 18–20px, dropping to 16px under 640px, where the masthead tagline also hides and the lockup shrinks from 34px to 28px tall. Wide tables scroll inside their own container, and their "Why" column is hidden on phones. Nothing may scroll horizontally at 390px.

## Elevation & Depth

The system is flat at rest. Sheets and site cards carry only a 1px bottom hairline shadow, which separates white from paper without looking lifted. Depth shows up in only two places: a site card that is a single link lifts 2px with a soft, diffuse shadow on hover, and keycap buttons sit on a solid 4px base that shrinks to 1px as they press down. Logos on the colour bands get a small contact shadow so their white tiles read against saturated colour. Under reduced motion, the lift and the show-picker fade are turned off.

### Shadow Vocabulary
- **Resting hairline** (`box-shadow: 0 1px 0 rgba(0,0,0,.05)`): every sheet, site card and footer card at rest.
- **Hover lift** (`box-shadow: 0 10px 30px rgba(0,0,0,.12)` with `translateY(-2px)`): site cards that are a single link, on hover only.
- **Keycap base** (`box-shadow: 0 4px 0 #0E1013`, pressed `0 1px 0` with `translateY(3px)`): primary buttons.
- **Logo contact** (`box-shadow: 0 1px 3px rgba(0,0,0,.25)`): logo tiles on colour bands.

### Named Rules
**The Flat Until Touched Rule.** Surfaces are flat at rest. Depth appears only when you hover or press: the lift and the keycap press. Never add resting shadows to cards.

**The Many-Links Card Stays Put Rule.** A card that holds several links (an `article`, not one big link) does not lift on hover, because lifting suggests the whole card is a single target.

## Shapes

Corners get rounder as elements get bigger: 4px chips, 6px nav pills, 8px small controls, 10px stat tiles and footer site tiles, 12px keycaps and logo tiles, 18px cards. Borders are rare; separation comes from colour and hairlines. The one heavy line is the 2px ink rule under h2s and table headers, which gives a printed feel. List bullets are 6px dots in the card's own site colour. Logos sit in white rounded tiles with a 2px white border on colour bands, so every crest looks like a key on the ring.

## Components

### Buttons
Tactile and friendly: these are keycaps, meant to be pressed.
- **Shape:** keycap corners, at least 44px tall.
- **Primary (keycap):** keycap ink fill with paper text, Space Grotesk 600 at 13px, 16px side padding, on a solid 4px keycap base. In dark mode the fill swaps to paper and the text to ink.
- **Hover / Active:** hover dims to 92% opacity. Pressing moves the key down 3px and shrinks the base to 1px, over 0.06s.
- **Ghost:** transparent, ink text, 1px hairline border, no base. Used for secondary links (GitHub, "Open early preview").
- **On-band:** white button with the card's site colour as text, 8px corners, used for the "Pick a show" control on a colour band. Hover shows 88% white; focus shows a 3px white outline.

### Chips
- **Style:** paper fill, ink text, 11px, 4px corners, tight 3px × 7px padding. Small metadata only.

### Cards / Containers
- **Corner Style:** card corners (18px).
- **Background:** card white on paper (night card on night ground).
- **Shadow Strategy:** resting hairline only; see Elevation & Depth.
- **Border:** none.
- **Internal Padding:** 18px × 20px, or 16px under 640px.

### Navigation
- **Style:** a row of links on the ink masthead in Space Grotesk 13px paper text, as 6px-cornered pills with 9px × 13px padding. Hover shows 10% white; the current page shows 14% white. The row wraps on narrow screens instead of scrolling.

### Site Card (signature component)
The key on the ring. A white card with a solid band in the site's colour on top: a 52px logo tile, the domain as a title, and a one-line descriptor in the site colour's world. The body below holds a sentence, a link list (rows at least 44px tall, separated by hairlines, each ending in an accent-ink →) or a dot list, an optional stat tile, and an "Open [site] →" link in accent ink. Wide cards add an archive moment to the band: a micro-label eyebrow, a date, a scoreline in the score style and a short note, separated by a translucent white rule. On bobdylan.app the moment is a "Pick a show" picker that fades in a new show.

### Stat Tile
A paper-filled 10px-cornered tile with slate 14px text and one bold ink phrase ("4000+ concerts"). Used for one headline fact per card.

### Theme Toggle
A segmented control with a hairline border and 8px corners holding 11px buttons. The pressed option takes the keycap fill. The choice is saved in `localStorage` (`rm-theme`) and applied before first paint.

## Do's and Don'ts

### Do:
- **Do** put every new colour in the `:root` block of `site.css` and redefine it under both dark-mode selectors.
- **Do** give each new site its own site-colour token and set it on its card as the card accent.
- **Do** keep tap targets at least 44px tall, including link-list rows and buttons.
- **Do** use accent ink, not signal orange, for any accent text or link.
- **Do** use the C key alone (no lockup) when the mark is 32px or smaller.
- **Do** check light and dark at 1280 and 390 wide with no horizontal overflow.
- **Do** bump the `?v=` stamp on the `site.css` link in every HTML file when the stylesheet changes.

### Don't:
- **Don't** make anything but the C key orange.
- **Don't** add resting shadows to cards; depth is for hover and press only.
- **Don't** let a site's colour leak outside its own card.
- **Don't** use uppercase or letter-spaced labels; everything is sentence case.
- **Don't** make cards that hold several links lift on hover.
- **Don't** set paragraphs in Space Grotesk.
