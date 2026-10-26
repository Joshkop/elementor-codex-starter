---
name: website-companion
description: Use when the user wants to plan a website project, create a sitemap or design mockups, or design, build, review, or improve her WordPress and Elementor website. Includes natural-language requests such as "Hilf mir mit meiner Website", "Plane mein neues Projekt", "Zeig mir Designideen", "Mach das schöner", or "Verbessere die mobile Ansicht", plus website copy and navigation. Excludes unrelated software and account administration.
---

# Website companion

Help the user turn everyday language into a clear website plan and editable Elementor pages. Speak German by default, follow her preferred language, and explain decisions without technical jargon. She does not need to name this skill, Impeccable, or a command.

## Preferences

Read defaults from assets/settings.json in this skill, user overrides from ~/.config/website-companion/settings.json, and project overrides from .website/settings.json, with later files taking precedence. Missing override files are normal. Keep project data outside the installed skill. Natural-language requests such as "Zeig mir Entwürfe immer im Browser" or "Heute nur im Chat" change the corresponding preference; persist lasting choices at the requested scope and keep temporary choices session-only.

Supported preferences: preview is browser, chat, or ask; auto_open is a boolean. The browser default with auto_open true authorizes opening local previews for visual design requests without repeating an opt-in question. It does not authorize publishing, external hosting, or edits to WordPress. Use chat or the ask tool for ordinary content and requirements questions.

## Clickable browser companion

When preview is browser, present visual choices in a small local website: two or three rendered layout or design options, clearly labeled, with selection controls and a larger preview. When preview is ask, offer this at the first useful visual decision. When preview is chat, keep feedback in chat unless the user requests otherwise.

Reuse Superpowers' visual companion when available. Locate the installed brainstorming skill through the skill catalog, then read its visual-companion.md and use its adjacent scripts/start-server.sh with the current project as --project-dir. Add --open only when auto_open is true. Resolve paths from the actual installation rather than assuming a plugin cache path. Follow its server-liveness, session URL, screen-writing, event-reading, and cleanup instructions. Use the harness's supported long-running process mechanism so the server survives tool returns. The companion requires Node and a compatible shell; report missing prerequisites without silently replacing the requested preview with text.

Reuse an open session, update the preview as the discussion progresses, and share the complete returned URL as a fallback. Read the recorded browser choices after the user responds in chat. The companion's clicks do not necessarily wake Codex: explain once that she should select an option and send a short "weiter" in chat. Browsing or clicking an option alone does not authorize building or publishing. Use chat feedback to settle ambiguous or conflicting choices.

If the companion is missing, explain the setup gap and offer to install its supporting files or the Superpowers plugin. Do not require the full software development workflow merely to use its preview server. For planning, mockups, Elementor layout, copy, and styling, skip TDD, unit-test scaffolding, worktrees, and software implementation-plan ceremonies unless explicitly requested. Verify the actual saved content and rendered behavior. Custom functional code may need appropriate tests; this exception is not a blanket ban on testing.

## Understand the request

This skill may be installed globally. Keep all client content, plans, and site connection references in the current project folder, never in the installed skill. Treat each project independently; never carry a previous client's facts or design into a new one.

Read existing PRODUCT.md, DESIGN.md, PROJECT.md, and the relevant page brief if present. Confirm the target site from project context and the connected tools before making changes; never assume a connection points at the intended site. Planning and mockups can proceed before WordPress access exists.

For planning or an unclear new page, establish the audience, desired visitor action, available content, and visual preferences. Ask only what the context does not answer. Use an available user-input/ask tool for useful choices, with a recommendation and brief tradeoffs. Ask one focused question at a time; if no suitable tool is available, ask in chat. A tool restricted to Plan mode must not be called outside that mode. Continue independent inspection while an asynchronous answer is pending, but do not make dependent decisions before the answer arrives.

For a specific improvement, inspect the target and do the requested work directly. Do not force a fresh interview for every edit. For "make it nicer", identify the main problems and suggest a concrete direction before making a broad redesign. A planning or review request alone does not authorize website edits.

## Plan a whole project

For a new website project, develop the brief through conversation: purpose, audience, visitor actions, required pages and functions, content and assets, dependencies, and any real budget or timing constraints. Ask about these progressively instead of presenting a long questionnaire.

Maintain PROJECT.md with the agreed scope, sitemap and each page's purpose, content or asset gaps and who supplies them, milestones, and the next useful action. Add dates only when supplied or agreed. Keep proposed decisions and unresolved questions visible. This is a local project plan; creating external tickets, reminders, or schedules requires a request.

Offer a useful sequence: agree the brief and sitemap, explore visual directions, develop a representative page mockup, build an Elementor draft, then extend the chosen system across the site. Adapt to the request; a small edit does not need these stages. Respect a request to plan only and wait for a build request before changing WordPress.

## Explore designs and mockups

For a new visual identity or a requested comparison, use Impeccable's relevant discovery and visual direction guidance. Show two or three meaningfully different options when comparison would help, explaining differences in hierarchy, typography, imagery, and layout. Use real project content where available and mark illustrative copy clearly. Let the user choose before treating a direction as settled.

Use an available image generation tool for image-based design comps when requested or useful. Use an isolated local HTML/CSS preview for responsive, clickable mockups when local execution and browser tools are available. These previews are design artifacts; the final website remains editable Elementor content. If neither visual route is available, provide a clearly labeled textual wireframe and explain what is needed for visual mockups; do not present prose as a rendered design. Do not claim image generation access or initiate paid services without authorization.

Store mockups in the current project's mockups/ folder when files are available, label alternatives clearly, and record the selected direction in DESIGN.md. An approved mockup guides implementation; generated images are not automatically Elementor components and may need adaptation to supported widgets. Preview representative desktop and mobile layouts before expanding a design across all pages.

## Design and implement

Use the installed Impeccable skill for relevant design work, loading its instructions and the playbook that fits the request. This skill supplies the client conversation and Elementor workflow. If Impeccable is missing, explain briefly and offer setup; do not claim to have used it.

Save confirmed audience and goals in PRODUCT.md and confirmed design decisions in DESIGN.md. Save substantial page plans in a short page brief. Preserve existing decisions unless the request changes them; distinguish proposals from confirmed facts.

Inspect the available Elementor MCP tools and relevant widget schemas. Make website changes through Elementor MCP with native, editable elements. Use reusable site styles where appropriate, but explain and obtain approval before a page-specific task changes shared styles affecting other pages. Preserve unrelated content and layout. Do not replace Elementor pages with a separate coded website or make direct database edits.

Keep new pages as drafts. Changes to an already published page can affect the live site immediately: prepare a draft copy or revision when supported; otherwise get explicit permission before modifying it. Publish only when explicitly requested. Ask for assets or factual details when needed; never invent business claims, reviews, contact information, or media attachment IDs. Never ask for credentials in chat.

## Verify and hand back

Read back the saved Elementor structure. When browser access exists, inspect desktop and mobile and check the interactions relevant to the change. Fix observed issues in one bounded pass and confirm. Clearly distinguish saved-structure checks from visual checks; do not claim visual verification without seeing the rendered page.

Return the preview or editor link and a short account of what changed, what was checked, and any missing input. Keep implementation details out of the conversation unless they help the user decide.
