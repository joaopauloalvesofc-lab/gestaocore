# Publicação do site CORE

O projeto é estático. O Python gera as páginas e copia todos os recursos locais.
Consulte `CONTEXTO_COMPLETO.md` para as decisões de conteúdo e negócio.

## Verificação pelo CLI

Na raiz do repositório:

```bash
python3 generate.py
python3 scripts/check_site.py dist
python3 -m http.server 8000 --directory dist
```

Abra `http://localhost:8000`. O comando do servidor permanece em execução até
ser encerrado com Ctrl+C.

## GitHub Pages

O workflow `.github/workflows/pages.yml` gera e publica o site após um push em
`main`, ou por execução manual. A URL e o caminho são obtidos da configuração
do próprio GitHub Pages.

Antes da primeira execução, um administrador deve habilitar GitHub Pages no
repositório e selecionar **GitHub Actions** como origem. O recurso depende da
disponibilidade do plano e da visibilidade do repositório. Não altere a
visibilidade do repositório apenas para concluir uma publicação.

Com autenticação de administrador no CLI, consulte o estado:

```bash
gh api repos/andremartinslicitacao-del/CORE/pages
```

Se o recurso estiver disponível e ainda não estiver habilitado, a configuração
para publicação por Actions pode ser criada com:

```bash
gh api --method POST repos/andremartinslicitacao-del/CORE/pages -f build_type=workflow
```

Se já houver configuração de Pages, examine-a antes de alterar:

```bash
gh api --method PUT repos/andremartinslicitacao-del/CORE/pages -f build_type=workflow
gh workflow run pages.yml --repo andremartinslicitacao-del/CORE
gh run list --repo andremartinslicitacao-del/CORE --workflow pages.yml
```

Não é necessário criar segredos personalizados para o workflow padrão. Ele usa
o token temporário e a identidade fornecidos pelo GitHub Actions.

## Build reproduzível para o subdiretório CORE

```bash
python3 generate.py --output _site --site-url https://andremartinslicitacao-del.github.io/CORE --base-path /CORE
python3 scripts/check_site.py _site --base-path /CORE
```

A URL acima é a URL padrão esperada. Considere o deploy concluído somente após
o workflow informar sucesso e a hospedagem retornar o site.

## Outra hospedagem ou domínio próprio

Para hospedagem na raiz:

```bash
python3 generate.py --output dist --site-url https://www.exemplo.com.br --base-path ''
python3 scripts/check_site.py dist
```

Publique o conteúdo de `dist/`, incluindo `assets/`, `404.html`, `robots.txt`,
`sitemap.xml` e `.nojekyll`. Não publique o código-fonte ou documentos de
trabalho no lugar do diretório gerado.

Para reverter uma alteração, use o histórico normal do Git e gere novamente o
site. Preserve os commits anteriores; não force a reescrita da branch.
