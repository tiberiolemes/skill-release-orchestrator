# Contributing

Contributions should make Skill creation and release more reusable, evidence-based, compatible with Codex and Claude Code, and safe to publish.

## Before opening a pull request

- Read the relevant `SKILL.md` and references.
- Preserve the mandatory intake for visibility, license, destination, scope, platforms, and publication authorization.
- Keep public and private distribution behavior distinct.
- Use fictitious examples; never include tokens, credentials, personal data, private code, or internal URLs.
- Run `python3 scripts/validate_skills.py` and the current Codex Skill Creator validator when available.
- Review `git status`, `git diff`, staged paths, and the final asset before committing.

## Skill design

Keep the entrypoint concise and place long procedures, templates, and policies in focused `references/` files. Preserve automatic invocation unless an explicit-only policy is a deliberate documented choice. Keep Codex UI metadata and Claude-specific agent definitions separate from shared Skill instructions.

## Git and releases

Use small logical commits with prefixes such as `feat:`, `fix:`, `docs:`, `test:`, and `chore:`. Do not rewrite shared history, force-push, or use destructive commands to resolve a conflict. Verify the GitHub owner and remote before publishing.

## English

Contributions should improve reusable, evidence-based, Codex- and Claude-compatible Skill creation and safe publication. Preserve the required intake, keep public and private distribution distinct, use fictitious examples, run validators, review the diff, and avoid secrets, private data, destructive Git operations, and force-pushes.
