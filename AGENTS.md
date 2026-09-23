# Website design workflow

- This is an existing static HTML site. Keep changes local unless publishing is requested.
- Maintain one live version only: update `index.html` directly. Do not create numbered HTML iterations or duplicate versions.
- Keep CSS and JavaScript inline. Record delivered changes and validation limitations in `DESIGN.md`.
- Do not modify shared images or assets unless the requested change requires it.
- Preserve the existing blue palette: background #f0f4f8, white #ffffff, divider #d9e2ec, foreground #102a43, muted #627d98, primary #003e6b, accent #0f609b. Existing Tailwind names `yellow` and `aqua` refer to the two blue brand colors.
- Preserve the original visual design and pinned/sticky hero scrolling: the user explicitly prefers it. The header issue was its border appearing before its background, not the sticky scrolling. Make narrowly scoped fixes; do not remove effects or redesign typography without a request. Avoid autoplay, new sections, invented claims, or new dependencies unless requested.
- Preserve supplied copy and imagery unless a requested change requires otherwise. Flag missing assets or placeholder destinations instead of inventing company information.
- Validate local image references, fragment links, JavaScript syntax, and relevant interaction logic. Check mobile styles and reduced-motion support. Be explicit about whether browser testing was performed.
