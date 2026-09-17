# Estrutura e empacotamento

Use esta referência para transformar as decisões do intake em um pacote instalável e fácil de manter.

## Progressive disclosure

Mantenha no `SKILL.md` apenas o que muda a decisão do agente: propósito, gatilhos, limites, fluxo principal, restrições, saída e roteamento. Mova checklists, templates, procedimentos específicos, schemas e exemplos longos para `references/`. Crie `scripts/` somente quando a automação determinística reduzir erro ou trabalho repetido.

## Pacote Codex

Cada Skill deve ter:

~~~text
skills/[skill-name]/
├── SKILL.md
├── agents/openai.yaml
└── references/        # somente as referências que a Skill realmente usa
~~~

O frontmatter precisa ter `name` igual à pasta e uma `description` discriminante. O `openai.yaml` é metadado de interface, não instrução para o agente. O prompt padrão deve ser curto e mencionar `$skill-name`.

## Pacote Claude Code

Quando Claude Code fizer parte do escopo, inclua:

~~~text
.claude-plugin/plugin.json
agents/[skill-name]-agent.md
~~~

O plugin compartilha `skills/*/SKILL.md` e `references/`. O agente Claude deve ter frontmatter com `name`, `description`, `skills`, `tools` e `model`, além de uma instrução curta que preserve o contrato da Skill. Não duplique o workflow inteiro no agente.

## Repositório

Para uma distribuição pública ou privada reutilizável, considere:

~~~text
README.md
LICENSE
CONTRIBUTING.md
.gitignore
scripts/validate_skills.py
assets/[banner]       # somente se aprovado no intake
~~~

Inclua somente arquivos que servem ao uso, à manutenção, à validação ou à identidade do pacote. Um repositório com várias Skills deve validar cada pasta e documentar como instalar uma Skill específica e o conjunto completo.

## Limites e dependências

Declare no entrypoint o que ativa a Skill e o que não ativa. Se houver dependência de MCP, CLI, API ou conta externa, documente a necessidade, o risco de indisponibilidade e o que fazer sem ela. Não coloque credenciais no repositório nem trate autenticação do agente como autorização para publicar.
