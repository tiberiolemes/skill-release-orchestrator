# README, selos e identidade visual

Use esta referência quando o intake pedir um pacote com aparência pronta para distribuição.

## README bilíngue

O README deve conter, nessa ordem ou em ordem equivalente:

1. Nome e banner com texto alternativo.
2. Badges coerentes com versão, licença, plataformas e, se aplicável, build.
3. Resumo do que a Skill faz e do que não faz.
4. Lista de capacidades e estrutura do pacote.
5. Instalação e uso no Codex.
6. Instalação e uso no Claude Code.
7. Prompt completo de exemplo e prompt de retomada quando houver estado persistente.
8. Decisões de visibilidade/licença e limites de segurança.
9. Validação, contribuição e licença.

Para README PT-BR/English, mantenha a mesma promessa, nomes técnicos, comandos e limitações nas duas versões. Não traduza um comando ou nome de Skill de forma diferente.

## Selos

Use imagens de badge somente para fatos reais e verificáveis. Exemplos adequados:

~~~markdown
[![Version](https://img.shields.io/badge/version-1.0.0-7c3aed?style=for-the-badge)](...)
[![License](https://img.shields.io/badge/license-MIT-16a34a?style=for-the-badge)](LICENSE)
![Codex supported](https://img.shields.io/badge/Codex-supported-111827?style=for-the-badge)
![Claude Code supported](https://img.shields.io/badge/Claude%20Code-supported-111827?style=for-the-badge)
~~~

Para repositório privado, não crie badge ou link que sugira instalação pública, download aberto, build público ou disponibilidade para qualquer pessoa.

## Banner

Se aprovado, use um banner panorâmico, legível em miniatura e com espaço negativo para o título do README. Prefira uma ilustração sem texto embutido quando a renderização exata de palavras for importante; mantenha o texto no README e forneça alt text descritivo. Use o gerador de imagem disponível para uma arte nova e salve o asset dentro de `assets/` antes de referenciá-lo.

Checklist visual:

- proporção panorâmica e tamanho adequado para GitHub;
- contraste suficiente e sem dependência de cor para entender o projeto;
- sem logos não autorizados, watermark, secrets ou dados reais;
- paleta compatível com o nome e a finalidade da Skill;
- referência no README com caminho relativo e alt text;
- `file`, preview visual e diff binário conferidos.

## Licença

O README deve apontar para `LICENSE` quando houver licença. Para `MIT`, `Apache-2.0`, `ISC` ou `GPL`, use o texto oficial compatível com a decisão. Para licença proprietária, sem licença ou customizada, explique que a redistribuição depende dos termos definidos; não use badge MIT por conveniência.
