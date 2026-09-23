# FAFNER AERO design record

## Current site — index.html

The repository now maintains one live HTML version. Future changes are made directly in `index.html`; numbered iterations are no longer created or retained.

The current site preserves the established blue palette, original pinned hero scrolling, refined mission and tactical-challenges sections, horizontal product carousel, Share Tech Mono hero title, and consolidated image paths.

Latest change: redesigned the footer as a polished contact section with a large editorial heading, prominent email action, legal address, company register details, and a restrained closing line. The supplied address, CVR number, inquiry guidance, and response statement remain, with copy tightened for clarity.

Refinement: removed the period from the main footer heading, dropped the numbered detail labels, and removed the office and workshop appointment block. The legal address and company register remain as two plain detail columns.

Carousel refinement: enlarged desktop cards to approximately 84% of the viewport with a 1.75:1 ratio, narrow neighboring-card previews, 30px gaps, minimal chrome, left-aligned snapping, and an asymmetric 5.4vw inset matching the supplied reference. Added an internal rule and large product-name typography while retaining the existing imagery and product copy. Mobile uses a 90vw portrait card with swipe and keyboard navigation intact.

Validation: footer content and email destination checked, local image references resolved, inline JavaScript parsed, and reduced-motion behavior preserved. Headless Chromium visual checks were completed at 1440×1000 and 390×844; the Contact anchor includes desktop and mobile offsets for the fixed header.

Carousel validation: an independent visual reviewer compared rendered output with the supplied 1722×956 reference through two critique passes and approved the final desktop and 390×844 mobile layouts with no blockers. Headless Chromium also confirmed selector navigation, ArrowLeft keyboard navigation, and the 5.4vw left snap position. Local references, fragment targets, inline JavaScript syntax, and formatting checks pass.

Carousel correction: restored the clickable technology selector bar and previous/next buttons after user feedback, and removed the horizontal rule from the cards. The oversized card geometry and editorial typography remain.

Typography refinement: standardized the site on Inter, including the hero wordmark and former monospace placeholder. Light-background headings, labels, body copy, carousel selectors, and counters now use black with a more consistent weight and tracking scale. White text remains only where required for contrast over imagery, the fixed header, and the dark footer. Chromium visual inspection at 1440×1000 confirmed the revised mission typography and contrast; formatting and inline JavaScript checks pass.

Footer refinement: moved `contact@fafneraero.com` from the upper contact block to the final footer row, right-aligned on desktop and aligned with the footer content on mobile.

Image update: added the supplied forest operations image as `images/image-12.png` and used it for the Advanced Guidance carousel slide. The previous `images/image-4.jpg` asset remains unchanged and continues to appear in Tactical Challenges.

Placeholder replacement: renamed the supplied `images/image-88` JPEG to `images/image-88.jpg` and used it in place of the Advanced Component Detail placeholder beside Tactical Superiority. The image uses its native landscape composition in a responsive 4:3 frame.

Image 88 sizing: widened the desktop image column, reduced its inner gutter, and removed the 480px width cap. Mobile retains the existing full-column treatment.

Image 88 replacement: replaced the earlier JPEG with the newly supplied 1280×927 PNG as `images/image-88.png`; its placement and responsive sizing remain unchanged.

Image selection: replaced Image 88 in the Tactical Superiority section with the supplied `images/image-ukde.jpg` while preserving the enlarged responsive layout.

Hero image refresh: retained the newly renamed `images/image-1.jpg` as the full-screen title image and added a cache-busting version parameter so browsers load the replacement file immediately. The carousel was left unchanged. The local asset reference and HTML formatting were validated; browser testing was not performed.

Hero positioning: moved the title, supporting text, and primary action down together by 3rem on mobile and 3.5rem on larger screens. The pinned hero behavior and typography remain unchanged. HTML formatting was validated; browser testing was not performed.

Carousel behavior: centered the active card and its image crop at every viewport size, replacing the asymmetric rail inset with equal responsive side previews. Added cloned boundary cards and seamless position normalization for infinite previous/next, keyboard, click, and swipe navigation. Selector state and the position counter continue to reflect the three original slides, cloned cards are hidden from assistive technology, and reduced-motion preferences disable animated transitions.

Tactical Superiority refinement: removed the vertical divider between the copy and image columns while retaining the existing grid and spacing.
