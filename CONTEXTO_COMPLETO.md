# Contexto completo — CORE Gestão e Tecnologias em Saúde

Atualizado em 13 de novembro de 2026.

## 1. Finalidade e pedido do usuário

André Martins solicitou um site institucional completo para a empresa CORE, de um amigo. O pedido destacou que deveria ser um site com páginas próprias, e não apenas uma página inicial. As áreas principais são gestão da saúde, serviços médicos, engenharia clínica, Central de Material e Esterilização (CME) e lavanderia hospitalar.

Foram solicitadas história, serviços, contatos, missão, visão e valores, além de elementos usuais no mercado. Posteriormente o usuário pediu análise da minuta societária, aproveitamento dos dados institucionais no site, um prompt de regularização ambiental/sanitária/Anvisa e, por fim, envio integral ao repositório:
https://github.com/andremartinslicitacao-del/CORE

Este documento organiza o contexto empresarial e técnico relevante para continuar o projeto. As informações documentais e o estágio dos trabalhos são diferenciados das propostas editoriais e das pendências de validação.

## 2. Identificação e fontes

| Campo | Informação utilizada | Observação |
| --- | --- | --- |
| Marca | CORE Gestão e Tecnologias em Saúde | Preservada a identidade visual fornecida |
| Denominação proposta | CORE Gestão e Tecnologias em Saúde Ltda. | Constante da minuta de alteração; conferir ato registrado |
| Nome anterior documentado | CORE Gestão de Tecnologias em Saúde Ltda. | Identificado nos documentos societários e diagnóstico |
| CNPJ | 48.827.070/0001-44 | Identificador empresarial informado nos documentos |
| Início das atividades | 07/12/2022 | Informação da cláusula de início de atividades da minuta |
| Endereço institucional informado | Av. Nossa Senhora de Fátima, nº 1646 e 1650, Torre, João Pessoa/PB, CEP 58040-380 | Mudança indicada na minuta e na identidade visual; atualização cadastral a conferir |
| Telefone/WhatsApp | (83) 99193-4988 | Material de identidade visual |
| E-mail | coregestaoadm@gmail.com | Material de identidade visual |
| Atividade principal projetada | 8660-7/00 — Atividades de apoio à gestão de saúde | Dependente da alteração cadastral |
| Atividade principal no CNPJ anterior, conforme diagnóstico | 3312-1/03 — Manutenção e reparação de aparelhos eletromédicos | Diagnóstico de trabalho de 13/11/2026 |

Documentos apresentados ou produzidos no trabalho:
- CORE GESTÃO LOGO.pdf: marca em vetor, variantes e dados de contato.
- 3 ACS_MINUTA v3.pdf: minuta da terceira alteração e consolidação contratual.
- 01_Diagnostico_e_Plano_CORE.docx: diagnóstico preliminar e plano de regularização.
- 02_Manual_Institucional_e_Modelos_CORE.docx: manual e modelos operacionais preliminares.
- 03_Minutas_de_Consultas_CORE.docx: consultas propostas aos órgãos competentes.
- 04_Matriz_Cronograma_e_Checklists_CORE.xlsx: planilha do pacote de regularização; não reavaliada nesta migração.
- Pacote_Regularizacao_CORE_v1.zip: pacote de documentos de trabalho.

Os documentos de regularização são minutas sujeitas a validação e não comprovam obtenção de licenças, protocolo, conformidade física ou início de operação. Os documentos originais devem ser consultados no acervo do cliente. Não integram os arquivos públicos do site.

## 3. Modelo operacional informado no trabalho regulatório

O diagnóstico de 13/11/2026 registra modelo misto: CME e lavanderia serão executadas nas instalações dos hospitais contratantes, e não na sede administrativa da Avenida Nossa Senhora de Fátima.

Foram descritos três modelos, a definir por contrato:
- A — Gestão e equipe: gestão operacional, equipe, escalas, treinamento e indicadores.
- B — Operação e insumos: modelo anterior acrescido de aquisição/fornecimento de insumos do processamento.
- C — Operação integral: equipe, insumos, equipamentos ou locação, manutenção, processos e indicadores.

As atribuições da CORE e do hospital precisam ser delimitadas por contrato e por unidade. A planta preliminar da sede mencionada no diagnóstico tem ambientes de estoque, expedição e salas de operações; o uso real desses ambientes continua sujeito a esclarecimento. Não presumir planta industrial de CME ou lavanderia nesse endereço.

Essas informações orientam a continuidade do projeto, mas não constituem certificação ou autorização de funcionamento.

## 4. Estrutura e identidade do site

Site em português brasileiro, responsivo, com HTML estático, CSS e JavaScript, gerado com Python sem bibliotecas externas.

Direção visual:
- Azul institucional: #123d56.
- Verde/azul da marca: #42a4a8.
- Fundos claros, tipografia Manrope local e ícones SVG.
- Marca original extraída em vetor do PDF; variante branca no rodapé.
- Fotografias ilustrativas, com indicação no rodapé e aviso de privacidade.
- Interface institucional voltada a organizações, sem agendamento de consultas.

Referências de arquitetura da informação:
- TECSAÚDE: https://www.tecsaude.com.br/
- Pró-Saúde: https://www.prosaude.org.br/nossos-servicos/
- Esteriliza: https://esteriliza.com.br/quem-somos/
- Elis: https://br.elis.com/pt/hospitais-e-clinicas

As referências orientaram a estrutura. Textos, marcas, clientes, números, certificações e fotografias dessas empresas não foram apresentados como pertencentes à CORE.

## 5. Páginas e conteúdo

Existem 18 páginas públicas e uma página de erro 404:

| Página | Caminho |
| --- | --- |
| Início | / |
| A CORE — história, missão, visão e valores | /a-core/ |
| Todas as soluções | /solucoes/ |
| Gestão da saúde | /solucoes/gestao-da-saude/ |
| Serviços médicos | /solucoes/servicos-medicos/ |
| Engenharia clínica | /solucoes/engenharia-clinica/ |
| CME | /solucoes/cme/ |
| Lavanderia hospitalar | /solucoes/lavanderia-hospitalar/ |
| Como atuamos | /como-atuamos/ |
| Qualidade e responsabilidade | /qualidade/ |
| Conteúdos | /conteudos/ |
| Engenharia clínica: além da manutenção | /conteudos/engenharia-clinica-alem-da-manutencao/ |
| CME: registros e rastreabilidade | /conteudos/cme-rastreabilidade-e-gestao/ |
| Enxoval hospitalar | /conteudos/lavanderia-gestao-do-enxoval/ |
| Contato e proposta | /contato/ |
| Trabalhe conosco | /trabalhe-conosco/ |
| Privacidade | /privacidade/ |
| Mapa do site | /mapa-do-site/ |
| Erro | /404.html |

A denominação solicitada e utilizada é Lavanderia Hospitalar.

Frentes complementares apresentadas sob consulta, a partir do objeto social proposto:
1. Locação de equipamentos e materiais.
2. Software e tecnologia.
3. Capacitação de equipes.
4. Suprimentos e equipamentos.

Cada frente direciona ao formulário com a área de interesse selecionada.

### Redação institucional proposta

Missão: conectar pessoas, gestão e tecnologia para apoiar serviços de saúde mais seguros, eficientes e humanizados.

Visão: ser reconhecida como parceira estratégica de instituições de saúde pela qualidade da gestão, pela confiabilidade técnica e pelo compromisso com as pessoas.

Valores:
- Cuidado com a vida.
- Ética e transparência.
- Responsabilidade técnica.
- Melhoria contínua.
- Colaboração.
- Sustentabilidade.

Missão, visão, valores e a redação comercial foram criados como proposta editorial para validação da empresa. A história usa a data de início de atividades informada na minuta, sem inventar clientes, cronologia de expansão ou resultados.

## 6. Funcionalidades e limites reais

- Navegação entre páginas, breadcrumbs e menu de soluções.
- Menu adaptado a telas estreitas e uso por teclado.
- Perguntas frequentes expansíveis.
- Busca e filtros dos três conteúdos editoriais.
- Links de telefone, e-mail, WhatsApp e Google Maps.
- Solicitação de proposta com validação dos campos.
- Seleção automática da área pelo parâmetro servico da URL.
- Preparação de mensagem para WhatsApp e e-mail: o visitante revisa e conclui o envio no canal escolhido.
- Contato profissional por e-mail em Trabalhe conosco, sem divulgação de vaga fictícia.
- Metadados por página, dados estruturados de organização, sitemap, robots e 404.

Não há backend de leads, banco de dados, painel administrativo, CMS, upload de currículos ou envio automático de e-mail. O site não declara certificações, licenças, equipe, unidades próprias, clientes ou números operacionais que não tenham sido demonstrados.

Os três artigos são introdutórios e incluem leituras oficiais de referência. Não são POPs operacionais nem substituem a avaliação de profissionais responsáveis.

## 7. Contexto da análise societária

A minuta trouxe mudança de nome e endereço, ampliação do objeto e alterações de capital e regras societárias. Os dados institucionais relevantes foram incorporados ao site.

Pontos recomendados para revisão do contrato:
- Corrigir a duplicação “CORE CORE” no preâmbulo da consolidação.
- Harmonizar referências a “outro sócio”, “sócios” e “maioria” com a estrutura unipessoal.
- Descrever expressamente o escopo pretendido de CME e lavanderia hospitalar.
- Confirmar atividades/CNAEs efetivos, atribuições técnicas e licenciamento aplicável.
- Precisar termo inicial e vencimento da integralização de capital ainda prevista.

Essas observações não significam que o contrato foi registrado ou que sua versão jurídica final foi concluída. O arquivo contratual original não foi alterado pelo trabalho de criação do site.

## 8. Contexto ambiental, sanitário e Anvisa

Foi solicitado um prompt para análise do licenciamento e posterior elaboração dos documentos e projetos necessários. Em trabalho posterior, os arquivos de diagnóstico, manual, consultas e matriz foram produzidos como versão preliminar.

Diretriz de continuidade registrada nesses documentos:
- Analisar atividade real, endereço, estabelecimento e contrato individualmente.
- Tratar a sede e cada hospital de forma específica.
- Conferir competência municipal/estadual para vigilância sanitária e meio ambiente.
- Verificar AFE/AE ou outro enquadramento da Anvisa conforme operação efetiva; não presumir uma licença universal.
- Diferenciar manutenção, gestão, processamento, lavanderia, comércio, distribuição, armazenamento e locação.
- Identificar responsabilidades de CORE, hospital e profissionais habilitados.
- Produzir projetos executivos e documentos técnicos a partir de levantamentos e dados reais.

Pendências registradas:
- Contrato social registrado e CNPJ atualizados após alteração.
- Caracterização do uso real de estoque, expedição e salas da sede.
- Identificação dos hospitais, contratos, volumes, plantas e instalações.
- Responsáveis técnicos e coordenadores formalmente designados.
- Licenças, projetos aprovados, laudos e evidências pertinentes a cada unidade.
- Respostas oficiais às consultas propostas.

Órgãos e referências de pesquisa mencionados nos documentos:
- GVS/Secretaria Municipal de Saúde de João Pessoa.
- AGEVISA/PB.
- SEMAM de João Pessoa e órgão ambiental competente de cada hospital.
- Anvisa, inclusive orientações de AFE por atividade e estabelecimento.
- RDC 15/2012, RDC 6/2012, RDC 50/2002, RDC 51/2011, RDC 222/2018 e normas locais, sempre com verificação de vigência na análise específica.

O código do site não é um sistema de gestão de licenças, nem a publicação do site demonstra autorização para executar atividades reguladas.

## 9. Arquitetura e manutenção

| Arquivo/pasta | Finalidade |
| --- | --- |
| generate.py | Dados da empresa, textos, componentes e geração das páginas |
| assets/ | Arquivos fonte: CSS, JavaScript, marca, fotos e fonte |
| dist/ | Versão estática gerada para hospedagem na raiz |
| _site/ | Saída temporária para GitHub Pages, ignorada pelo Git |
| scripts/check_site.py | Verificação de páginas, links, âncoras, recursos e opções de contato |
| .github/workflows/pages.yml | Build e publicação no GitHub Pages |
| README.md | Instruções de uso e manutenção |
| docs/DEPLOY.md | Publicação e verificação via CLI |
| docs/ | Registros visuais de revisão |
| CONTEXTO_COMPLETO.md | Este documento |

A versão atual usa assets locais e não exige instalação de pacotes Python ou Node para gerar o site. Python é utilizado apenas na geração; a hospedagem serve arquivos estáticos.

O gerador aceita:
- --output: diretório de saída.
- --site-url: URL pública completa da aplicação, incluindo /CORE quando aplicável.
- --base-path: prefixo de navegação, como /CORE, ou vazio para hospedagem na raiz.

O workflow usa a URL e o caminho informados pelo GitHub Pages, permitindo futura configuração de domínio próprio sem fixar permanentemente /CORE no código-fonte.

## 10. Publicação e histórico técnico

- Site anterior publicado: https://core-gestao-saude.curlyspice6.chatgpt.site
- Fonte recuperada para esta migração: commit f88056cdc557c5107c9c83925a09c9faf0136121 da versão institucional revisada.
- Repositório de destino solicitado: https://github.com/andremartinslicitacao-del/CORE
- O repositório foi encontrado vazio e privado em 13/11/2026.
- A migração inclui os arquivos completos, conteúdo, imagens locais, gerador, verificações, documentação e workflow.
- GitHub Pages precisa estar habilitado e disponível para o plano/visibilidade do repositório. Não confundir envio de código com publicação concluída.
- URL padrão esperada se o GitHub Pages estiver habilitado: https://andremartinslicitacao-del.github.io/CORE/
- A conclusão da publicação deve ser confirmada no workflow e na URL retornada pela hospedagem.

A configuração do antigo provedor de hospedagem e seu histórico Git não são necessários para executar esta cópia independente.

## 11. Verificações e critérios editoriais

Foram conferidas as 18 páginas e a página 404, os links locais, âncoras, opções de contato, metadados e recursos, tanto na raiz como sob /CORE. O JavaScript passou na verificação sintática. A versão visual anterior foi inspecionada em desktop e em largura de conteúdo de 375 px.

Para continuar:
1. Ler este contexto e o README.
2. Confirmar o estado atual do repositório, da hospedagem e das informações cadastrais.
3. Editar as fontes e gerar novamente os arquivos estáticos.
4. Executar as verificações para a raiz e para o prefixo de publicação.
5. Preservar a identidade visual e o modelo multipágina.
6. Manter claras as diferenças entre fatos demonstrados, propostas editoriais e atividades sob consulta.
7. Não acrescentar alegações de licença, certificação, cliente, resultado ou estrutura própria sem suporte documental.
8. Conferir o sucesso do deploy antes de afirmar que uma nova versão está no ar.

## 12. Imagens e fonte

Fotografias ilustrativas do Unsplash:
- Cirurgia: photo-1551190822-a9333d879b1f.
- Gestão: photo-1576091160550-2173dba999ef.
- Tecnologia/cuidado: photo-1576091160399-112ba8d25d1d.
- Equipamentos: photo-1516549655169-df83a0774514.
- Lavanderia: photo-1545173168-9f1947eebb7f.

A fonte Manrope é fornecida localmente com seu arquivo de licença OFL-Manrope.txt. A marca CORE pertence ao material institucional fornecido. Conferir direitos e autorizações antes de substituir imagens por fotografias reais de pessoas ou instalações.

