# Setup instructions for Codex

The user who asks you to follow this file authorizes global installation of this website workflow and its named public dependencies. This does not authorize WordPress changes, publishing, costs, or replacing unrelated configuration.

## 1. Prepare

Clone https://github.com/Joshkop/elementor-codex-starter into a user-owned tools directory, outside any client website folder, or use an existing clone. A sibling of the client folders under the user's projects folder is also suitable. The starter clone is an installation source, not a parent workspace in which to design client sites. Read the installer and supplied instructions before running them. Preserve existing user instructions, settings, and skills. Read any applicable local instructions.

Check for Codex, Git, Python 3.9+, Node.js 18.19+, pnpm, and Bash. Use only pnpm for package-manager commands. If prerequisites are missing, explain the exact missing pieces and use a user-approved setup route; do not silently substitute another package manager or system installation. Check the Node requirement reported by upstream packages too.

## 2. Install companion and global instructions

From this repository, run:

```sh
python3 scripts/install.py
```

Use the available Python 3 command on Windows if it differs. The script installs the skill in `~/.agents/skills/website-companion`, creates global preferences if missing, and adds or updates only its marked block in `$CODEX_HOME/AGENTS.md` (default `~/.codex/AGENTS.md`). It backs up changed existing files under `~/.config/website-companion/backups/` and preserves saved preferences.

The default is `preview: browser` and `auto_open: true`. When the setup prompt explicitly requests these settings, update just those keys in the global preference file while preserving other fields. Do not change other saved preferences.

## 3. Install upstream skills

Inspect existing installations first. Reuse working installations and report their versions; do not force replacements. For a clean installation use:

```sh
pnpm dlx impeccable@4.7.0 install --providers=codex --scope=global --yes --no-hooks
pnpm dlx skills@1.7.4 add obra/superpowers --skill '*' --agent codex --global --yes
```

The Impeccable installer version and skills installer version are pinned. Superpowers is fetched from its upstream default branch; record the resolved upstream revision from installation metadata or a public Git lookup. Review upstream instructions before executing helpers. Do not promise fully reproducible dependency content for an unpinned upstream repository.

Do not use `--all`: in the skills installer it selects every agent, which is broader than this Codex setup. Do not install duplicate copies through both the plugin marketplace and the skills installer. If Superpowers is already available as a plugin, reuse it.

The website workflow instructions explicitly opt out of software development ceremonies for planning, mockups, copy, styling, and Elementor edits. Use the visual companion's supporting guide and scripts without imposing a separate mandatory TDD/spec/worktree process. Preserve appropriate testing for custom functional code.

## 4. Verify

Check that website-companion, Impeccable, and the Superpowers brainstorming skill are discoverable, that the global managed rules exist once, and that browser preferences are enabled. If the current skill catalog is stale, distinguish installed files from active discovery and tell the user to start a fresh session.

Locate the installed brainstorming skill and its visual-companion.md. Follow that guide to start its local browser server in a separate scratch project folder using the harness's supported long-running process mechanism. Create a tiny screen with two distinct selectable layout options. Verify that it renders in a browser when browser tools are available; otherwise report only server/file checks as verified and ask the user to confirm the rendered screen. Ask the user to click an option and send “weiter”, then read its recorded event before claiming click feedback works. Keep the full session URL and key intact. Opening local previews is authorized by the selected preference. Do not expose the server on a public address.

Image generation is optional for this HTML/CSS preview. Report available image tools without requesting API keys in chat or activating paid fallbacks.

## 5. Start a website project

Have the user open a dedicated project folder and describe the website in ordinary language. Keep project content out of this starter repository and the global skill directory. Planning and mockups can begin immediately.

For actual site changes, identify the intended site and guide the user through its Elementor MCP connection and authentication. Each site has a separate MCP connection. The user only needs to paste Elementor's site-specific setup guide while working in that client's project folder: activate website-companion automatically and handle project-only configuration and site-identity verification without asking for an additional instruction. Do not install a client's site connection globally or replace another project's connection. If the supplied guide only configures a global connection, adapt it using supported project configuration; if project scope is unsupported, explain the limitation without making a global change. Complete any required project trust or authentication through the supported user interface.

Do not invent an endpoint or assume another client's connection is correct. Never request credentials in chat. During setup verify access with read-only operations only; do not create a test page or change site content.

Finish with a brief verified/pending list and the next useful action. Do not claim installation, browser rendering, click feedback, or WordPress access that was not actually checked.
