# Intake e decisões obrigatórias

Faça o intake antes de qualquer escrita, criação de repositório ou publicação. As perguntas podem ser agrupadas em uma mensagem curta, mas nenhuma decisão abaixo deve ser inferida quando mudar o risco ou a distribuição.

## Perguntas bloqueadoras

| Tema | Pergunta | Por que importa |
|---|---|---|
| Visibilidade | O repositório será público ou privado? | Muda exposição, badges, instalação, conteúdo permitido e revisão de secrets. |
| Licença | Qual licença será usada? | Define cópia, modificação, redistribuição e o arquivo `LICENSE`. |
| Destino | Qual owner e nome exato? O repositório existe? | Evita criar ou publicar na conta errada. |
| Autorização | Posso criar/editar, commitar e fazer push? | Criação e publicação são mutações externas diferentes. |
| Branch | Qual branch padrão e política de proteção? | Determina como integrar e verificar o release. |

Se a resposta for “não sei” para visibilidade, licença, destino ou autorização, mantenha o fluxo em `BLOCKED` até obter a decisão.

## Perguntas de escopo

- Qual problema a Skill resolve e qual resultado deve entregar?
- Quem deve usá-la e quais solicitações estão fora do escopo?
- Qual nome técnico, nome exibido, descrição curta e prompt inicial devem aparecer?
- Será uma Skill única, um conjunto de Skills ou uma Skill orquestradora com especialistas?
- A distribuição inclui Codex, Claude Code ou ambos?
- Deve permitir invocação automática, apenas explícita ou as duas modalidades?
- Quais referências, scripts, templates, MCPs, APIs ou outras dependências são necessárias?
- Há um formato de relatório, changelog, versionamento, contato ou política de contribuição?

## Perguntas de conteúdo e marca

- Quais idiomas serão suportados? O README deve ser PT-BR/English ou outra combinação?
- O banner terá texto exato ou somente uma ilustração? Qual formato, proporção, paleta e mensagem visual?
- Quais badges são obrigatórios: versão, licença, plataforma, estágio, build, cobertura ou outros?
- Existe logo, paleta, tipografia, asset de referência ou restrição de uso?
- O repositório pode conter screenshots, exemplos fictícios, URLs públicas e links para instalação?

## Registro mínimo

Mantenha as decisões em uma seção do relatório ou em issue/arquivo de release:

~~~text
Project: [nome]
Owner/repository: [owner/name]
Visibility: PUBLIC | PRIVATE
License: [escolha ou customizada]
Platforms: Codex | Claude Code | BOTH
Languages: [idiomas]
Auto invocation: ON | OFF
External mutations authorized: [escopo]
Branch: [branch]
Version: [versão]
~~~

Não copie tokens, cookies ou respostas de autenticação para esse registro.
