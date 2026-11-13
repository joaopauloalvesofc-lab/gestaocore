# CORE — Gestão e Tecnologias em Saúde

Site institucional completo, em português, com **18 páginas e uma página 404**.

- Fontes, imagens, marca, CSS e JavaScript locais.
- Responsivo para computador e celular.
- Gestão da saúde, serviços médicos, engenharia clínica, CME e lavanderia hospitalar.
- História, missão, visão, valores, qualidade, conteúdos e contatos.
- Solicitação de proposta preparada para WhatsApp ou e-mail.

## Comece aqui

- [Contexto completo do projeto](CONTEXTO_COMPLETO.md)
- [Publicação e verificação via CLI](docs/DEPLOY.md)
- [Workflow do GitHub Pages](.github/workflows/pages.yml)

## Gerar e visualizar

Requer Python 3.10 ou superior, sem instalação de bibliotecas.

```bash
python3 generate.py
python3 scripts/check_site.py dist
python3 -m http.server 8000 --directory dist
```

Abra http://localhost:8000.

## GitHub Pages

O workflow publica a branch `main` quando GitHub Pages estiver habilitado com
origem **GitHub Actions**. Ele usa a URL e o caminho informados pelo GitHub,
inclusive o subdiretório `/CORE` ou um domínio próprio.

Build de conferência:

```bash
python3 generate.py --output _site --site-url https://andremartinslicitacao-del.github.io/CORE --base-path /CORE
python3 scripts/check_site.py _site --base-path /CORE
```

A URL esperada só deve ser tratada como publicada após confirmação do workflow.
O repositório é mantido na visibilidade configurada pelo proprietário.

## Manutenção

| Local | Conteúdo |
| --- | --- |
| `generate.py` | Textos, dados da empresa, estrutura e metadados |
| `assets/style.css` | Estilos e responsividade |
| `assets/site.js` | Menu, pesquisa, filtros e formulário |
| `assets/` | Marca, fotos, fonte e outros recursos originais |
| `dist/` | Versão gerada pronta para hospedagem na raiz |
| `scripts/check_site.py` | Verificação de links, recursos, páginas e formulário |

Após alterar textos ou recursos, execute novamente o gerador e a verificação.

## Funcionamento do contato

O formulário prepara uma mensagem localmente. O visitante escolhe WhatsApp ou
e-mail e conclui o envio no serviço escolhido. Esta versão não possui banco de
leads, backend, CMS ou envio automático de mensagens.

## Conteúdo e imagens

Os dados institucionais foram extraídos do material fornecido. Missão, visão,
valores e textos comerciais são propostas editoriais para validação da empresa.
Não se afirmam licenças, certificações, clientes ou resultados não demonstrados.

As fotografias são ilustrativas do Unsplash. A fonte Manrope é fornecida com sua
licença em `assets/OFL-Manrope.txt`. A marca original veio do PDF de identidade
visual. Fontes e decisões estão documentadas no contexto completo.
