---
name: skill-release-orchestrator
description: Orquestre a criação, validação, empacotamento e publicação segura de Skills compatíveis com Codex e Claude Code, com intake obrigatório, README bilíngue, licença, selos, banner, agentes e GitHub.
---

# Skill Release Orchestrator

Use esta Skill quando o usuário quiser transformar um processo, método ou conjunto de instruções em uma Skill distribuível, criar um pacote público ou privado no GitHub, ou atualizar uma Skill já existente mantendo compatibilidade com Codex e Claude Code.

Esta é uma Skill de criação e release de Skills. Ela não substitui o `skill-creator` para decisões específicas de conteúdo, não publica em uma conta diferente da autorizada e não presume que um repositório deve ser público, privado ou usar uma licença determinada.

## Regra de parada mais importante

Antes de criar arquivos, criar um repositório ou executar qualquer mutação externa, faça o intake e registre as decisões. Pergunte explicitamente, mesmo que pareça óbvio:

1. O repositório será **público** ou **privado**?
2. Qual será a **licença**: MIT, Apache-2.0, ISC, GPL, proprietária/sem licença ou texto customizado?
3. Qual é o proprietário e o nome exato do repositório? Ele já existe ou deve ser criado?
4. Qual é o nome técnico, o nome exibido, o objetivo, o público e o limite da Skill?
5. A Skill será distribuída para **Codex**, **Claude Code** ou ambos?
6. Quais idiomas o README, a Skill e os exemplos devem suportar? O README precisa ser bilíngue?
7. Quais recursos a entrega exige: referências, scripts, assets, badges, banner, agentes, plugin, exemplos, changelog ou CI?
8. A invocação deve ser automática, explícita ou ambas? Há dependências de ferramentas, MCPs ou permissões?
9. O usuário autoriza criar/alterar o repositório, fazer commit e fazer push? Qual branch e mensagem de commit devem ser usadas?
10. Existem templates, arquivos de referência, identidade visual, links, política de contribuição, contato ou restrições que precisam ser preservados?

Se alguma resposta mudar o conteúdo, a visibilidade, o acesso ou a publicação, pare e peça a decisão. Nunca escolha público/privado, licença, proprietário, nome de repositório ou autorização de push silenciosamente.

## Resultado esperado

Entregue uma Skill pronta para instalação, com progressive disclosure e um release revisável. Quando solicitado ou quando fizer parte do padrão do repositório, a estrutura é:

~~~text
skill-repository/
├── README.md                         # documentação bilíngue, instalação e uso
├── LICENSE                            # conforme decisão do intake
├── CONTRIBUTING.md
├── .gitignore
├── .claude-plugin/plugin.json         # distribuição Claude Code
├── agents/[skill-name]-agent.md       # agente Claude Code
├── assets/[banner].png                # se banner for aprovado
├── scripts/validate_skills.py
└── skills/
    └── [skill-name]/
        ├── SKILL.md                   # entrypoint enxuto
        ├── agents/openai.yaml         # metadados Codex
        └── references/                # detalhes condicionais
~~~

Não crie arquivos vazios, placeholders ou documentação duplicada sem necessidade. Se a licença escolhida for proprietária, sem licença ou customizada, adapte README, manifestos, badges e instalação para não sugerir reutilização não autorizada.

## Fluxo orquestrado

Siga este ciclo e registre cada decisão relevante:

~~~text
INTAKE → CHECKPOINT → DISCOVERY → DESIGN → BUILD → BRAND → VALIDATE → REVIEW → COMMIT → PUBLISH → VERIFY
~~~

- **INTAKE** — Faça as perguntas obrigatórias, defina escopo, visibilidade, licença, plataformas, identidade e autorização.
- **CHECKPOINT** — Confira `git status`, branch, remote, histórico, conta GitHub ativa e alterações preexistentes. Preserve trabalho do usuário.
- **DISCOVERY** — Leia os artefatos fornecidos, inspecione Skills existentes, identifique padrões de `SKILL.md`, `openai.yaml`, agentes, plugin e validadores.
- **DESIGN** — Defina nome técnico, descrição discriminante, modos de operação, limites, referências, saídas, políticas de invocação e dependências.
- **BUILD** — Escreva `SKILL.md` enxuto, referências focadas, metadados Codex, agente Claude, plugin, README, licença, contribuição e validador.
- **BRAND** — Gere ou integre banner somente se aprovado. Adicione badges coerentes com visibilidade, versão, licença e plataformas; nunca mostre credenciais ou dados privados.
- **VALIDATE** — Execute validador próprio, `quick_validate.py` quando disponível, parse de JSON/YAML, verificação de links/referências, diff check e varredura de secrets.
- **REVIEW** — Revise manualmente clareza, limites, compatibilidade, instalação, perguntas de intake, licença, visibilidade e ausência de promessas não comprovadas.
- **COMMIT** — Faça um commit lógico somente com os caminhos pretendidos. Não misture alterações existentes nem reescreva histórico compartilhado.
- **PUBLISH** — Confirme novamente owner, repositório, visibilidade, branch e autorização antes de criar ou fazer push. Use a conta GitHub correta; se a conta ativa não corresponder, pare.
- **VERIFY** — Confirme branch remoto, arquivos publicados, commit, README, asset, manifestos e status limpo. Relate qualquer parte não verificável.

## Regras para a Skill criada

- O frontmatter deve conter `name` e `description`; o nome deve ser minúsculo, com hífens e igual ao nome da pasta.
- A descrição deve explicar quando usar a Skill e diferenciá-la de Skills próximas, sem virar um catálogo genérico.
- O `SKILL.md` deve conter propósito, limites, fluxo, restrições e roteamento; procedimentos longos ficam em `references/`.
- `agents/openai.yaml` deve ter strings entre aspas, prompt padrão curto e menção explícita a `$skill-name`. Mantenha invocação automática salvo decisão documentada.
- O agente Claude deve ter frontmatter válido, referenciar a Skill correta, declarar ferramentas mínimas e respeitar os mesmos limites.
- README e exemplos devem explicar instalação e uso no Codex e no Claude Code, além de dizer se a distribuição é pública ou privada.
- Não inclua tokens, chaves, URLs internas, PII, dados de cliente, código privado ou valores reais de produção.
- Use `NOT_VERIFIED` quando o comportamento, a permissão, o vínculo GitHub ou o status de publicação não puder ser comprovado.

## Publicação e GitHub

Para um repositório novo, confirme a conta ativa com a CLI do GitHub antes de usar `gh repo create`. Para um repositório existente, leia o remote e faça fetch antes de integrar um commit inicial remoto. Se o repositório for privado, não publique instruções que pressuponham clone público nem use badges que prometam acesso aberto. Se o repositório for público, confirme que todo conteúdo, exemplo, banner e histórico são adequados para exposição pública.

Não use `git reset --hard`, `git clean -fd`, force push ou comandos destrutivos para “resolver” divergências. Se o push falhar por autenticação, owner incorreto, branch protegida, repositório inexistente ou histórico divergente, registre a causa e peça a ação necessária.

## Referências

Leia as referências conforme o momento do fluxo:

- [intake-and-decisions.md](references/intake-and-decisions.md) para perguntas obrigatórias, opções e decisões que bloqueiam publicação.
- [package-layout.md](references/package-layout.md) para o desenho da Skill, progressive disclosure, Codex, Claude Code e estrutura do repositório.
- [github-release-and-git.md](references/github-release-and-git.md) antes de criar, conectar, integrar, commitar ou publicar um repositório.
- [readme-and-branding.md](references/readme-and-branding.md) para README bilíngue, selos, banner, licença e identidade visual.
- [validation-and-report.md](references/validation-and-report.md) para quality gate, relatório e verificação final.

## Critério de conclusão

Considere a entrega concluída somente quando o pacote passar pelas validações, o diff e os secrets forem revisados, o commit for identificado e a publicação for confirmada no owner/repositório corretos. Se a publicação não puder ocorrer, entregue o pacote local completo, o commit e a causa objetiva do bloqueio; não diga que foi publicado.
