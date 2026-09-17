# Validação e relatório

Use esta referência antes de declarar o pacote pronto ou publicado.

## Quality gate

### Intake e escopo

- Público/privado, licença, owner, nome do repositório, branch e autorização de mutação estão registrados.
- Nome, descrição, público, plataformas, idiomas, invocação, dependências e limites foram decididos.
- O pacote não promete compatibilidade ou comportamento que não foi implementado ou verificado.

### Estrutura

- Cada pasta em `skills/` contém `SKILL.md` válido e nome consistente.
- O entrypoint referencia apenas arquivos existentes e mantém progressive disclosure.
- `agents/openai.yaml` tem strings válidas, prompt com `$skill-name` e política coerente.
- `.claude-plugin/plugin.json` e agentes Claude estão presentes e válidos quando Claude Code está no escopo.
- README, CONTRIBUTING, LICENSE e scripts estão presentes; `assets/` só existe quando aprovado no intake.

### Conteúdo e distribuição

- README bilíngue, quando solicitado, tem instruções equivalentes para Codex e Claude Code.
- Badges mostram apenas versão, licença, plataformas e fatos reais.
- O banner ASCII está no README e é legível em tema claro e escuro; se houver asset visual adicional, ele tem alt text e não contém texto ilegível, logos indevidos ou dados privados.
- Exemplos usam placeholders seguros e não expõem credenciais, PII, URLs internas ou código privado.
- Visibilidade privada não é descrita como instalação pública e uma licença ausente/proprietária não é apresentada como permissiva.

### Git e publicação

- `git status`, branch, remote, diff e commit foram revisados.
- O owner da conta autenticada corresponde ao destino.
- O repositório remoto foi preservado; não houve force push ou operação destrutiva.
- O commit é lógico e contém apenas os caminhos pretendidos.
- O push e o conteúdo da branch remota foram verificados, ou o bloqueio foi registrado sem alegar publicação.

## Validações recomendadas

Execute as verificações disponíveis no pacote:

~~~bash
python3 scripts/validate_skills.py
python3 /path/to/quick_validate.py skills/[skill-name]
python3 -m json.tool .claude-plugin/plugin.json
git diff --check
~~~

Adapte o último caminho se não houver plugin Claude no escopo. Acrescente Markdown/link lint, testes de scripts e preview do README quando disponíveis.

## Relatório de release

Use este formato no final da execução:

~~~markdown
# Skill release report

- Skill/repository: [nome e owner/repo]
- Visibility: PUBLIC / PRIVATE
- License: [licença]
- Platforms: Codex / Claude Code / BOTH
- Version: [versão]
- Branch/commit: [branch e hash]
- Publication: PUBLISHED / LOCAL_ONLY / BLOCKED

## Delivered

- [Arquivos e capacidades entregues.]

## Intake decisions

- [Decisões importantes e autorização concedida.]

## Validation

- [Comando]: PASS / FAIL / NOT_VERIFIED — [resultado]

## Follow-up

- [Pendência, bloqueio, link, asset, tradução ou decisão necessária.]
~~~

O relatório final deve dizer claramente se a Skill foi apenas preparada localmente ou realmente publicada e por quê.
