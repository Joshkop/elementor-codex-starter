#!/usr/bin/env python3
"""Install the companion locally; never installs dependencies or contacts WordPress."""
import argparse
import os
from pathlib import Path
from datetime import datetime, timezone

START = '<!-- website-companion:start -->'
END = '<!-- website-companion:end -->'


def install(home, codex_dir):
    root = Path(__file__).resolve().parents[1]
    backup_dir = home / '.config/website-companion/backups' / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')

    def write(path, content):
        if path.exists():
            previous = path.read_bytes()
            if previous == content:
                return
            backup = backup_dir / path.relative_to(home) if path.is_relative_to(home) else backup_dir / 'custom-codex' / path.name
            backup.parent.mkdir(parents=True, exist_ok=True)
            backup.write_bytes(previous)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        print(f'Installed {path}')

    instructions = codex_dir / 'AGENTS.md'
    current = instructions.read_text() if instructions.exists() else ''
    if current.count(START) != current.count(END) or current.count(START) > 1:
        raise SystemExit('Malformed managed instruction block; repair it before installing.')
    if START in current and current.index(END) < current.index(START):
        raise SystemExit('Reversed managed instruction markers; repair before installing.')
    rules = (root / 'instructions/website-workflow.md').read_text().strip()
    block = START + '\n' + rules + '\n' + END
    if START in current:
        first, remainder = current.split(START, 1)
        _, last = remainder.split(END, 1)
        updated = first + block + last
    else:
        updated = current + ('\n\n' if current and not current.endswith('\n\n') else '') + block + '\n'

    skill = root / 'skills/website-companion'
    for source in sorted(skill.rglob('*')):
        if source.is_file():
            write(home / '.agents/skills/website-companion' / source.relative_to(skill), source.read_bytes())
    settings = home / '.config/website-companion/settings.json'
    if not settings.exists():
        write(settings, (skill / 'assets/settings.json').read_bytes())
    else:
        print(f'Preserved preferences: {settings}')
    write(instructions, updated.encode())
    if (codex_dir / 'AGENTS.override.md').exists():
        print('An AGENTS.override.md exists; check it does not hide the installed workflow instructions.')
    print('Companion installed. Follow SETUP.md for upstream skills and connection verification.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--home', type=Path, help='Alternate home directory for isolated verification')
    args = parser.parse_args()
    target_home = (args.home or Path.home()).expanduser().resolve()
    target_codex = target_home / '.codex' if args.home else Path(os.environ.get('CODEX_HOME', str(target_home / '.codex'))).expanduser().resolve()
    install(target_home, target_codex)
