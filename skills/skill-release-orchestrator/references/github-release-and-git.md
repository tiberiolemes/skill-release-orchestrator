# Release no GitHub e disciplina de Git

Use esta referência antes de qualquer mutação no GitHub ou no histórico local.

## Checkpoint local

Execute e registre, antes de editar:

~~~bash
git status --short --branch
git remote -v
git branch --show-current
git log -5 --oneline
~~~

Preserve alterações preexistentes. Não faça `git reset --hard`, `git clean -fd`, force push, checkout destrutivo ou sobrescrita silenciosa de arquivos do usuário.

## Conta e destino

Confirme que a conta GitHub ativa corresponde ao owner escolhido:

~~~bash
gh auth status
gh repo view OWNER/REPOSITORY
~~~

Se o owner não corresponder, pare e peça autenticação ou autorização correta. Não tente contornar um `403` usando outra conta.

## Repositório novo

Somente depois do intake e da autorização:

~~~bash
gh repo create OWNER/REPOSITORY --public --description "..."
git remote add origin https://github.com/OWNER/REPOSITORY.git
git push -u origin BRANCH
~~~

Escolha `--public` ou `--private` conforme a resposta registrada; no comando acima, substitua `--public` por `--private` quando necessário. Não use `--public` como padrão silencioso. Crie `LICENSE` com o texto correspondente antes de publicar quando houver licença.

## Repositório existente

Leia o remote e o estado remoto antes de conectar conteúdo local. Se houver um commit inicial no remoto, faça fetch e integre de forma não destrutiva:

~~~bash
git fetch origin BRANCH
git show --stat origin/BRANCH
git merge origin/BRANCH --allow-unrelated-histories
~~~

Resolva conflitos preservando decisões explícitas do usuário. Nunca descarte o commit inicial remoto apenas para facilitar o push.

## Commit e push

Antes do commit:

~~~bash
git add PATHS_INTENDED
git diff --cached --check
git status --short --branch
git diff --cached --stat
~~~

Faça uma varredura por tokens, chaves, secrets, dados privados e arquivos temporários. Use mensagem lógica, por exemplo:

~~~bash
git commit -m "feat: create Skill release orchestrator"
git push -u origin BRANCH
~~~

Se o push falhar, pare no erro exato. `Repository not found`, `403`, branch protegida e histórico divergente exigem diagnóstico e decisão; não exigem force push.

## Verificação pós-publicação

Confirme:

~~~bash
git status --short --branch
git log -1 --oneline --decorate
git ls-tree --name-only origin/BRANCH
gh repo view OWNER/REPOSITORY --json nameWithOwner,isPrivate,url,defaultBranchRef
~~~

Para repositório privado, confirme apenas por uma sessão autorizada e não exponha conteúdo no relatório público.
