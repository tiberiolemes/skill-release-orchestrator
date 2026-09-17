# Skill Release Orchestrator

<pre align="center">
+-------------------------------------------------------------+
|  *  SKILL RELEASE ORCHESTRATOR                              |
|     INTAKE -> DESIGN -> BUILD -> VALIDATE -> PUBLISH        |
|     CODEX  -  CLAUDE CODE  -  GITHUB                        |
+-------------------------------------------------------------+
</pre>

<p align="center">
  <a href="https://github.com/tiberiolemes/skill-release-orchestrator"><img src="https://img.shields.io/badge/version-1.0.1-7c3aed?style=for-the-badge" alt="Version 1.0.1"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-16a34a?style=for-the-badge" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/Codex-supported-111827?style=for-the-badge" alt="Codex supported">
  <img src="https://img.shields.io/badge/Claude%20Code-supported-111827?style=for-the-badge" alt="Claude Code supported">
</p>

<p align="center"><a href="#pt-br">🇧🇷 PT-BR</a> · <a href="#english">🇺🇸 English</a></p>

## PT-BR

O `skill-release-orchestrator` transforma um processo ou conjunto de instruções em uma Skill pronta para distribuição, mantendo compatibilidade com Codex e Claude Code.

Ele conduz o intake, o desenho, a escrita, a identidade visual, a validação, o commit e a publicação no GitHub. Antes de qualquer mutação, pergunta se o repositório será público ou privado, qual licença será usada, qual é o destino e quais permissões de publicação foram concedidas.

### O que a Skill entrega

- `SKILL.md` enxuto e com progressive disclosure;
- referências focadas para procedimentos, decisões e templates;
- metadados `agents/openai.yaml` para o Codex;
- plugin e agente Claude Code quando essa plataforma fizer parte do escopo;
- README bilíngue com instalação, uso, badges e limites;
- banner ASCII e identidade visual quando aprovados;
- licença, CONTRIBUTING, `.gitignore` e validador;
- commit lógico, publicação e verificação pós-push quando autorizados.

### Instalação no Codex

```text
$skill-installer

Install the `skill-release-orchestrator` Skill from tiberiolemes/skill-release-orchestrator.
```

Instalação manual em um projeto:

```bash
git clone https://github.com/tiberiolemes/skill-release-orchestrator.git
mkdir -p /caminho/para/seu-projeto/.agents/skills
cp -R skill-release-orchestrator/skills/* /caminho/para/seu-projeto/.agents/skills/
```

### Instalação no Claude Code

```bash
git clone https://github.com/tiberiolemes/skill-release-orchestrator.git
claude --plugin-dir /caminho/para/skill-release-orchestrator
```

O agente especializado fica disponível como `@skill-release-orchestrator-agent`.

### Como usar

No repositório do processo ou produto que dará origem à Skill, envie:

```text
Use $skill-release-orchestrator para transformar estas instruções em uma Skill distribuível.

Antes de editar, faça o intake obrigatório: pergunte se o repositório será público ou privado,
qual licença devo usar, qual owner e nome do repositório, quais plataformas serão suportadas,
quais idiomas e se o banner deve ser ASCII, imagem ou nenhum, quais dependências existem e se você está
autorizado a criar, commitar e publicar. Depois, siga o fluxo completo para Codex e Claude Code,
com README bilíngue, badges, banner ASCII, licença, agentes, plugin, referências e validações.
Preserve alterações existentes, não exponha secrets e não declare o push concluído sem verificar.
```

### Perguntas obrigatórias

A Skill não deve presumir:

- público ou privado;
- licença ou direito de redistribuição;
- owner, nome do repositório ou conta GitHub;
- Codex, Claude Code ou ambas as plataformas;
- idioma, README bilíngue, banner ASCII/imagem, badges ou identidade visual;
- invocação automática, dependências, MCPs ou permissões;
- autorização para criar, commitar, fazer push ou publicar.

### Fluxo

```text
INTAKE → CHECKPOINT → DISCOVERY → DESIGN → BUILD → BRAND → VALIDATE → REVIEW → COMMIT → PUBLISH → VERIFY
```

A Skill para diante de respostas faltantes, owner incorreto, autenticação divergente, branch protegida, secrets, histórico divergente ou qualquer mutação não autorizada. Ela não usa `git reset --hard`, `git clean -fd` ou force push para resolver problemas.

### Estrutura

```text
skill-release-orchestrator/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── .claude-plugin/plugin.json
├── agents/skill-release-orchestrator-agent.md
├── scripts/validate_skills.py
└── skills/skill-release-orchestrator/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── references/
```

### Validação

```bash
python3 scripts/validate_skills.py
python3 /caminho/para/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/skill-release-orchestrator
python3 -m json.tool .claude-plugin/plugin.json
git diff --check
```

## English

The `skill-release-orchestrator` turns a process or instruction set into a distributable Skill compatible with Codex and Claude Code.

It orchestrates intake, design, writing, branding, validation, commits, and GitHub publishing. Before any mutation, it asks whether the repository is public or private, which license applies, the exact destination, and what publishing authorization was granted.

### Install with Codex

```text
$skill-installer

Install the `skill-release-orchestrator` Skill from tiberiolemes/skill-release-orchestrator.
```

Manual project installation:

```bash
git clone https://github.com/tiberiolemes/skill-release-orchestrator.git
mkdir -p /path/to/your-project/.agents/skills
cp -R skill-release-orchestrator/skills/* /path/to/your-project/.agents/skills/
```

### Install with Claude Code

```bash
git clone https://github.com/tiberiolemes/skill-release-orchestrator.git
claude --plugin-dir /path/to/skill-release-orchestrator
```

Invoke it with `$skill-release-orchestrator` in Codex or `@skill-release-orchestrator-agent` in Claude Code.

### Usage

```text
Use $skill-release-orchestrator to turn these instructions into a distributable Skill.
Ask first whether the repository is public or private, which license applies, the owner and
repository name, supported platforms and languages, ASCII/image/no banner, dependencies, and whether
you are authorized to create, commit, and push. Then build, validate, and safely publish the
Codex and Claude Code package. Preserve existing work and never claim a push without proof.
```

### Scope and safety

The orchestrator stops when required decisions, authorization, evidence, or safe GitHub access are missing. It never embeds credentials, uses destructive Git operations, or silently publishes to a different owner.

Released under the [MIT License](LICENSE).
