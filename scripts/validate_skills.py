#!/usr/bin/env python3
"""Validate the public structure of a Skill release repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PLACEHOLDER_RE = re.compile(r"(?:TODO|FIXME|<skill-name>|<description>)")


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: SKILL.md must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError(f"{path}: frontmatter is not closed") from exc
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or ":" not in line or line.startswith((" ", "\t")):
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"\'')
    for field in ("name", "description"):
        if not fields.get(field):
            raise ValueError(f"{path}: frontmatter needs {field}")
    return fields


def validate_openai_yaml(path: Path, skill_name: str) -> None:
    text = path.read_text(encoding="utf-8")
    if "interface:" not in text:
        raise ValueError(f"{path}: missing interface section")
    for key in ("display_name", "short_description", "default_prompt"):
        match = re.search(rf"^  {key}: (.+)$", text, re.MULTILINE)
        if not match or not (
            match.group(1).startswith('"') and match.group(1).endswith('"')
        ):
            raise ValueError(f"{path}: {key} must be a quoted string")
    prompt = re.search(
        r'^  default_prompt: "([^"\\]*(?:\\.[^"\\]*)*)"$',
        text,
        re.MULTILINE,
    )
    if not prompt or f"${skill_name}" not in prompt.group(1):
        raise ValueError(f"{path}: default_prompt must mention ${skill_name}")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    skills_root = root / "skills"
    errors: list[str] = []
    skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir())

    if not skill_dirs:
        errors.append("skills/: expected at least one Skill directory")

    for skill_dir in skill_dirs:
        skill_path = skill_dir / "SKILL.md"
        try:
            skill_text = skill_path.read_text(encoding="utf-8")
            fields = parse_frontmatter(skill_text, skill_path)
            name = fields["name"]
            if name != skill_dir.name:
                raise ValueError(f"{skill_path}: name {name!r} does not match folder")
            if not NAME_RE.fullmatch(name):
                raise ValueError(f"{skill_path}: invalid skill name")
            if len(fields["description"]) < 20:
                raise ValueError(f"{skill_path}: description is too short")
            if PLACEHOLDER_RE.search(skill_text):
                raise ValueError(f"{skill_path}: unfinished placeholder found")
            for reference in re.findall(r"\]\((references/[^)]+)\)", skill_text):
                if not (skill_dir / reference).exists():
                    raise ValueError(f"{skill_path}: missing linked reference {reference}")
            yaml_path = skill_dir / "agents" / "openai.yaml"
            if yaml_path.exists():
                validate_openai_yaml(yaml_path, name)
        except (OSError, ValueError) as exc:
            errors.append(str(exc))

    plugin_path = root / ".claude-plugin" / "plugin.json"
    if plugin_path.exists():
        try:
            json.loads(plugin_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{plugin_path}: invalid JSON ({exc})")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Validated {len(skill_dirs)} Skill(s) and package metadata.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
