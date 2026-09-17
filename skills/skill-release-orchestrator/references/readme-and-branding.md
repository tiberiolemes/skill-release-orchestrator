# README, selos e identidade visual

Use esta referência quando o intake pedir um pacote com aparência pronta para distribuição.

## README bilíngue

O README deve conter, nessa ordem ou em ordem equivalente:

1. Nome e banner ASCII ou asset visual explicitamente aprovado, com descrição acessível quando aplicável.
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
[![Version](https://img.shields.io/badge/version-1.0.1-7c3aed?style=for-the-badge)](...)
[![License](https://img.shields.io/badge/license-MIT-16a34a?style=for-the-badge)](LICENSE)
![Codex supported](https://img.shields.io/badge/Codex-supported-111827?style=for-the-badge)
![Claude Code supported](https://img.shields.io/badge/Claude%20Code-supported-111827?style=for-the-badge)
~~~

Para repositório privado, não crie badge ou link que sugira instalação pública, download aberto, build público ou disponibilidade para qualquer pessoa.

## Banner

ASCII é a opção padrão deste pacote: mantenha o banner no próprio README, em um bloco `<pre>` ou de texto monoespaçado. Ele deve comunicar o nome da Skill e, quando couber, seu fluxo ou as plataformas suportadas sem depender de imagem, arquivo binário ou carregamento externo.

Checklist do banner ASCII:

- largura moderada, idealmente entre 60 e 80 colunas, para funcionar em terminal e GitHub;
- contraste e leitura preservados em temas claro e escuro;
- caracteres consistentes e fáceis de copiar; teste setas, acentos e caracteres de caixa no ambiente-alvo;
- sem secrets, PII, URLs internas, logos não autorizados ou texto que fique ilegível em fonte monoespaçada;
- descrição curta antes ou depois do bloco se o desenho não for autoexplicativo.

Só use uma imagem quando o intake aprovar explicitamente esse formato. Nesse caso, salve o asset em `assets/`, forneça alt text, verifique o preview visual e confirme que a imagem não expõe dados privados.

## Licença

O README deve apontar para `LICENSE` quando houver licença. Para `MIT`, `Apache-2.0`, `ISC` ou `GPL`, use o texto oficial compatível com a decisão. Para licença proprietária, sem licença ou customizada, explique que a redistribuição depende dos termos definidos; não use badge MIT por conveniência.
