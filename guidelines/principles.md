# Principles

AnixOps products are tools people work in. We borrow the restraint of
Apple's product pages — and only their principles.

## What we take

| Principle | In practice |
|---|---|
| **Content is the interface** | One topic per screen; a title and one sentence; the most important number and one primary action above the fold |
| **Restrained colour** | White / near-black surfaces, one accent, status colours only where status is shown |
| **Whitespace and a grid** | 4/8 pt spacing; 24 px inside cards; 48–64 px between sections |
| **Type leads the hierarchy** | Seven type steps; titles 600–700, body 400; Chinese line height 1.6 |
| **Materials** | Frosted bars and sidebars (`backdrop-filter`) with an opaque fallback; hairline separators; large, faint shadows |
| **Purposeful motion** | 120–280 ms, standard easing, only for state changes; honour reduced motion |
| **Progressive disclosure** | Simple first; advanced options behind "更多 / More" |
| **Consistent controls** | Pill buttons, segmented controls, switches, a clear focus ring |
| **Settings-style admin** | Light frosted sidebar, grouped lists, details in a side sheet |

## Work first, showcase second

- The user home page can feel like a product page, but must show the
  subscription status and "复制订阅链接" in the first screen.
- Admin screens favour density and speed: comfortable tables by default,
  compact on request; no hero images; no scroll-driven effects.

## Legal limits (must follow)

- **Fonts.** SF Pro, SF Mono and PingFang may not be embedded or distributed
  in web pages. Reference them only through the system stack
  (`-apple-system, BlinkMacSystemFont`). Never bundle any Apple font file.
  Inter (SIL OFL) is self-hosted for non-Apple platforms.
- **Icons.** SF Symbols are licensed only for apps on Apple platforms; never
  use them on the web or in non-Apple apps. Use Lucide (ISC).
- **Images, logos and copy.** Never use Apple product images, logos,
  trademarks, marketing copy, or a pixel-for-pixel copy of an Apple page
  layout. The AnixOps mark and wordmark are our own.
