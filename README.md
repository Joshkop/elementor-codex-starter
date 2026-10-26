# Elementor Codex Starter

A conversational website companion for planning a project, comparing designs in a small clickable browser preview, and building editable WordPress/Elementor pages.

## One setup prompt

Open Codex on your computer and paste:

> Go to https://github.com/Joshkop/elementor-codex-starter, read SETUP.md, and carry out the global setup on this computer. Preserve my existing instructions and settings. Enable browser previews that open automatically. Verify the installation and tell me what still needs my login or a new Codex session. Do not change a WordPress site during setup.

After setup, open a separate folder for each website and describe what you want:

> Ich möchte eine Website für eine Hundeschule planen. Hilf mir mit Seitenstruktur, Inhalten und ersten Designentwürfen.

> Zeig mir drei unterschiedliche Varianten für die Startseite im Browser.

## What it installs

- The global `website-companion` skill from this repository.
- Public [Impeccable](https://impeccable.style/) design guidance.
- Public [Superpowers](https://github.com/obra/superpowers) skills, including its clickable visual companion.
- A small managed section in your global Codex instructions. Website planning, mockups, copy, styling, and Elementor edits skip TDD, worktrees, test scaffolding, and mandatory software planning ceremonies. Custom functional code may still warrant tests.

The browser companion renders local HTML/CSS mockups; image generation is optional. Mockups guide the later Elementor implementation. They are not an automatic Elementor import.

## Preferences

Global: `~/.config/website-companion/settings.json`. Project overrides: `.website/settings.json` in the current project.

```json
{
  "preview": "browser",
  "auto_open": true
}
```

`preview` accepts `browser`, `chat`, or `ask`. You can also say “Zeig mir Entwürfe immer im Browser” or “Heute nur im Chat”. Project content stays in that project's `PRODUCT.md`, `PROJECT.md`, `DESIGN.md`, and mockup files.

## Practical limits

- Codex, account sign-in, and the local runtime prerequisites must exist or be set up with the user's help.
- The visual companion needs Node.js and Bash. On Windows, use a compatible environment such as Git Bash and verify browser opening from that environment.
- A browser selection is recorded; send “weiter” in Codex to continue. Clicks alone do not necessarily resume the agent.
- Local previews need a running server. Remote/container setups may need port forwarding; setup never exposes them publicly automatically.
- Each WordPress site needs its own compatible Elementor MCP connection. The connection must support the required editable Elementor elements; setup does not install WordPress plugins or configure the server side.
- Skill installation may require a fresh Codex session. No credentials belong in chat or this repository.

## Updating and uninstalling

Rerun the local installer to update this companion; changed existing files are backed up and saved preferences are preserved. Upstream dependency versions below are pinned; review updates before changing them.

To remove the companion, remove `~/.agents/skills/website-companion` and only the marked `website-companion` block from your Codex `AGENTS.md`. Keep or remove its preference file as desired. Impeccable and Superpowers are independent installations and can be removed separately with their installers. Do not remove unrelated skills or instructions.

This project contains original companion instructions. It does not redistribute upstream Impeccable or Superpowers code.
