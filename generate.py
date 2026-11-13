"""Generate the complete, dependency-free CORE institutional website.

Edit the content here and run `python generate.py`. Assets live in dist/assets.
All photographs are illustrative. Company copy is an editorial proposal based
on the user-provided service areas and identity material; no dates, customers,
certifications or operating statistics are invented.
"""
from pathlib import Path
from html import escape
import json
import argparse
import os
import re
import shutil
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
ASSETS = ROOT / 'assets'
ORIGIN = os.environ.get('CORE_SITE_URL', 'https://andremartinslicitacao-del.github.io/CORE').rstrip('/')
BASE_PATH = ''
PHONE = '(83) 99193-4988'
EMAIL = 'coregestaoadm@gmail.com'
CNPJ = '48.827.070/0001-44'
FOUNDING_DATE = '2022-12-07'
WA = 'https://wa.me/5583991934988'
MAP = 'https://www.google.com/maps/search/?api=1&query=Avenida+Nossa+Senhora+de+F%C3%A1tima+1646+Torre+Jo%C3%A3o+Pessoa+PB'

ICONS = {
    'arrow':'<path d="M5 12h14m-6-6 6 6-6 6"/>',
    'up-right':'<path d="M7 17 17 7M7 7h10v10"/>',
    'chevron':'<path d="m9 5 7 7-7 7"/>',
    'down':'<path d="m6 9 6 6 6-6"/>',
    'menu':'<path d="M4 6h16M4 12h16M4 18h16"/>',
    'chart':'<path d="M4 3v17h17M8 15v-4m5 4V7m5 8V4"/>',
    'stethoscope':'<path d="M5 3v5a5 5 0 0 0 10 0V3M3 3h4m6 0h4M10 13v3a5 5 0 0 0 10 0v-3"/><circle cx="20" cy="10" r="3"/>',
    'equipment':'<rect x="3" y="3" width="18" height="14" rx="2"/><path d="M7 11h3l2-4 2 7 2-3h2M8 21h8m-4-4v4"/>',
    'shield':'<path d="M12 2 3 6v6c0 5 9 10 9 10s9-5 9-10V6Z"/><path d="m8 12 3 3 5-6"/>',
    'laundry':'<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M4 7h16M7 4.5h.1m3 0h.1"/><circle cx="12" cy="14" r="5"/><path d="M7.5 14c2-3 5 3 9 0"/>',
    'hospital':'<path d="M4 22V5h16v17M2 22h20M9 22v-5h6v5M9 9h6m-3-3v6M7 14h.1m10 0h.1"/>',
    'clinic':'<path d="M3 21h18M5 21V8l7-5 7 5v13M9 10h6m-3-3v6M9 21v-5h6v5"/>',
    'people':'<circle cx="9" cy="7" r="3"/><path d="M3 21v-3a6 6 0 0 1 12 0v3M16 4a3 3 0 0 1 0 6m2 5a5 5 0 0 1 3 4v2"/>',
    'heart':'<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8Z"/>',
    'target':'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    'eye':'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/>',
    'check':'<path d="m5 12 4 4L19 6"/>',
    'check-circle':'<circle cx="12" cy="12" r="9"/><path d="m7 12 3 3 6-6"/>',
    'leaf':'<path d="M20 3C8 2 2 7 5 16s16 4 15-13ZM4 21 15 10"/>',
    'book':'<path d="M12 5v16M3 3c4-1 7 0 9 2 2-2 5-3 9-2v16c-4-1-7 0-9 2-2-2-5-3-9-2Z"/>',
    'refresh':'<path d="M20 8a9 9 0 0 0-15-3L2 8m0-5v5h5M4 16a9 9 0 0 0 15 3l3-3m0 5v-5h-5"/>',
    'clipboard':'<rect x="5" y="4" width="14" height="18" rx="2"/><rect x="8" y="2" width="8" height="4" rx="1"/><path d="M9 11h6m-6 4h6m-6 4h4"/>',
    'tool':'<path d="M14 6a5 5 0 0 0-6 6l-6 6a2.8 2.8 0 0 0 4 4l6-6a5 5 0 0 0 6-6l-3 3-4-4Z"/>',
    'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    'mail':'<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 6 10 7L22 6"/>',
    'phone':'<path d="m8 3 2 5-3 2c2 4 3 5 7 7l2-3 5 2c0 4-1 6-4 5C9 19 5 15 3 7 2 4 4 3 8 3Z"/>',
    'pin':'<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
    'whatsapp':'<path d="M21 11.5a9 9 0 0 1-13.6 7.7L2 21l1.8-5.3A9 9 0 1 1 21 11.5Z"/><path d="m8 7 2 2-1 2c1 2 2 3 4 3l1-1 2 1c0 2-1 3-3 2-4-1-7-5-6-8Z"/>',
    'search':'<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/>',
    'lock':'<rect x="5" y="10" width="14" height="11" rx="2"/><path d="M8 10V6a4 4 0 0 1 8 0v4M12 14v3"/>',
}
def icon(name, extra=''):
    return f'<svg class="icon {extra}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'

SERVICES = [
  dict(slug='gestao-da-saude',name='Gestão da saúde',short='Gestão da saúde',icon='chart',image='hero',alt='Tecnologia e organização apoiando a rotina em saúde',
       description='Pessoas, processos e indicadores conectados para uma operação de saúde mais organizada e eficiente.',
       headline='Mais clareza para gerir. Mais foco para cuidar.',
       intro='A gestão da saúde precisa integrar o que acontece no planejamento ao que acontece na ponta. A CORE propõe uma atuação próxima da rotina da instituição, com organização de processos, definição de responsabilidades e acompanhamento de resultados.',
       tags=['Processos','Indicadores','Gestão operacional'],
       deliverables=[('clipboard','Diagnóstico da operação','Mapeamento de rotinas, recursos, interfaces e pontos de atenção para definir prioridades de melhoria.'),('people','Organização de pessoas e processos','Apoio à definição de fluxos, atribuições e rotinas de comunicação entre as áreas.'),('chart','Acompanhamento por indicadores','Seleção de indicadores relevantes e construção de uma rotina de análise e tomada de decisão.'),('refresh','Melhoria contínua','Planos de ação com responsáveis e acompanhamento da evolução dos processos pactuados.')],
       metrics=[('Operação','Fluxos mais claros','Responsabilidades e etapas definidas para reduzir desencontros na rotina.'),('Decisão','Informação útil','Indicadores selecionados para responder às necessidades reais da gestão.'),('Integração','Áreas conectadas','Uma visão que aproxima assistência, apoio e administração.')],
       faqs=[('A solução pode abranger apenas parte da unidade?','Sim. A conversa inicial permite delimitar um setor, um conjunto de processos ou uma atuação mais abrangente, conforme a necessidade e o escopo contratado.'),('Como são escolhidos os indicadores?','A partir dos objetivos da instituição, da disponibilidade de dados e das prioridades identificadas no diagnóstico. Metas e formas de acompanhamento são pactuadas no projeto.'),('Como começar um projeto?','Compartilhe o perfil da unidade e o desafio que deseja resolver. A CORE avalia a demanda para construir uma proposta de trabalho compatível com essa realidade.')]),
  dict(slug='servicos-medicos',name='Serviços médicos',short='Serviços médicos',icon='stethoscope',image='surgery',alt='Profissionais de saúde durante atividade assistencial',
       description='Planejamento e organização de serviços médicos alinhados às necessidades da instituição e de seus pacientes.',
       headline='Pessoas preparadas. Assistência organizada.',
       intro='Uma boa experiência assistencial depende também de coordenação e organização. A proposta da CORE conecta o planejamento dos serviços médicos às necessidades de cada instituição, respeitando as atribuições profissionais e o modelo de atendimento pactuado.',
       tags=['Coordenação','Organização assistencial','Equipes médicas'],
       deliverables=[('people','Planejamento das equipes','Apoio à estruturação das necessidades de pessoal, perfis profissionais e organização das atividades.'),('clock','Organização de escalas','Planejamento de cobertura e rotinas de acompanhamento, conforme as necessidades definidas no contrato.'),('stethoscope','Coordenação dos serviços','Articulação entre equipes, gestão e fluxos da unidade para favorecer a continuidade do cuidado.'),('chart','Acompanhamento assistencial','Organização de informações e indicadores de produção e desempenho dos serviços contratados.')],
       metrics=[('Planejamento','Cobertura definida','Necessidades assistenciais traduzidas em uma organização de trabalho.'),('Pessoas','Equipes articuladas','Comunicação entre profissionais e gestão da instituição.'),('Cuidado','Continuidade em foco','Rotinas que ajudam a dar consistência à prestação dos serviços.')],
       faqs=[('Quais especialidades podem ser contempladas?','As especialidades, perfis profissionais e modalidades de atuação são avaliados na análise da demanda e definidos na proposta. Consulte a CORE para verificar a aderência ao seu projeto.'),('O site agenda consultas para pacientes?','Não. Este é um canal institucional voltado à contratação e à gestão de serviços para organizações de saúde. Agendamentos devem ser feitos nos canais da unidade assistencial.'),('A contratação inclui coordenação médica?','A coordenação pode compor o projeto quando prevista no escopo, com responsabilidades e requisitos profissionais definidos para a operação.')]),
  dict(slug='engenharia-clinica',name='Engenharia clínica',short='Engenharia clínica',icon='equipment',image='technology',alt='Tecnologia e equipamentos em ambiente de saúde',
       description='Gestão do parque tecnológico, planejamento de manutenção e apoio às decisões sobre equipamentos em saúde.',
       headline='Tecnologia confiável começa com boa gestão.',
       intro='O equipamento faz parte de uma rede de decisões: aquisição, utilização, manutenção e substituição. A engenharia clínica aproxima essa visão técnica da rotina da instituição, com foco em organização, disponibilidade e uso responsável dos recursos.',
       tags=['Parque tecnológico','Manutenção','Ciclo de vida'],
       deliverables=[('clipboard','Inventário e planejamento','Organização do cadastro e das informações do parque tecnológico para apoiar o planejamento técnico.'),('tool','Gestão das manutenções','Planejamento e acompanhamento de intervenções preventivas e corretivas, conforme o escopo e os requisitos aplicáveis.'),('equipment','Histórico dos equipamentos','Estruturação de registros de intervenções, ocorrências e condições de utilização dos equipamentos.'),('chart','Apoio à decisão','Análise de necessidades de renovação, custos e prioridades para orientar a gestão da tecnologia.')],
       metrics=[('Tecnologia','Visão do parque','Informações organizadas para conhecer os equipamentos e suas necessidades.'),('Planejamento','Prioridades técnicas','Rotinas de manutenção e acompanhamento definidas para a operação.'),('Recursos','Ciclo de vida','Decisões que consideram utilização, manutenção e renovação.')],
       faqs=[('É possível contratar a gestão do parque tecnológico?','O projeto pode contemplar a gestão dos equipamentos, o planejamento das manutenções e outras entregas técnicas, conforme as necessidades da instituição e o escopo pactuado.'),('Todos os tipos de equipamentos estão incluídos?','Os grupos de equipamentos, a cobertura técnica e as responsabilidades precisam ser definidos na proposta. A análise inicial identifica o que pode ser atendido.'),('Há atuação integrada com a gestão da unidade?','Essa integração faz parte da proposta de trabalho: aproximar as informações técnicas das decisões operacionais e administrativas da instituição.')]),
  dict(slug='cme',name='Central de Material e Esterilização',short='CME',icon='shield',image='surgery',alt='Instrumentação e equipe em ambiente assistencial',
       description='Organização e gestão dos processos da CME, com atenção aos fluxos, aos registros e à segurança em cada etapa.',
       headline='Cada etapa importa. Cada cuidado também.',
       intro='O processamento de produtos para saúde exige organização, responsabilidade técnica e atenção às interfaces com a assistência. A CORE apresenta soluções de gestão da CME orientadas à padronização das rotinas e ao acompanhamento dos processos.',
       tags=['Processamento','Rastreabilidade','Fluxos e registros'],
       deliverables=[('clipboard','Organização dos fluxos','Mapeamento e estruturação das etapas e das interfaces entre a CME e as áreas atendidas.'),('shield','Rotinas e responsabilidades','Apoio à definição de procedimentos e atribuições, considerando os requisitos técnicos e sanitários aplicáveis.'),('book','Registros e rastreabilidade','Organização das informações necessárias ao acompanhamento do processamento e das entregas.'),('chart','Acompanhamento da produção','Indicadores de demanda, capacidade e ocorrências para apoiar o planejamento da operação.')],
       metrics=[('Processos','Etapas conectadas','Fluxos definidos do recebimento à disponibilização dos materiais.'),('Informação','Registros organizados','Documentação que apoia o acompanhamento do processamento.'),('Assistência','Integração com a unidade','Planejamento das necessidades em diálogo com os setores atendidos.')],
       faqs=[('A gestão pode ocorrer dentro da instituição?','O modelo de execução é definido na análise do projeto. Estrutura, responsabilidades, requisitos e entregas precisam ser compatíveis com a unidade e com a proposta contratada.'),('O serviço contempla esterilização de qualquer produto?','A viabilidade de processamento depende das características e da regularização do produto, das instruções do fabricante e dos requisitos aplicáveis. O escopo deve passar por avaliação técnica.'),('Como a rastreabilidade é tratada?','Por meio da definição dos registros e controles necessários ao processo e às responsabilidades de cada etapa. As ferramentas e as entregas são estabelecidas no projeto.')]),
  dict(slug='lavanderia-hospitalar',name='Lavanderia hospitalar',short='Lavanderia hospitalar',icon='laundry',image='laundry-industrial',alt='Equipamentos e rotinas de lavanderia hospitalar',
       description='Gestão do processamento de roupas e da circulação do enxoval para apoiar a rotina dos serviços de saúde.',
       headline='Cuidado que se sente em cada detalhe.',
       intro='O enxoval participa da experiência de cuidado e do funcionamento diário da instituição. A gestão da lavanderia hospitalar conecta o processamento de roupas à demanda dos setores, com atenção à organização dos fluxos e ao controle da operação.',
       tags=['Processamento de roupas','Gestão de enxoval','Logística interna'],
       deliverables=[('laundry','Organização do processamento','Planejamento das rotinas e das etapas de processamento, considerando os requisitos técnicos e sanitários aplicáveis.'),('refresh','Fluxos de coleta e distribuição','Estruturação das interfaces entre os setores geradores, o processamento e a disponibilização do enxoval.'),('clipboard','Controle do enxoval','Apoio à organização de quantidades, movimentações, reposições e necessidades da unidade.'),('leaf','Uso responsável dos recursos','Acompanhamento de consumo, perdas e oportunidades de melhoria na operação.')],
       metrics=[('Rotina','Fluxos organizados','Coleta, processamento e distribuição considerados de forma integrada.'),('Enxoval','Disponibilidade planejada','Necessidades dos setores traduzidas em rotinas e controles.'),('Recursos','Acompanhamento de consumo','Informações para orientar melhorias e reduzir desperdícios.')],
       faqs=[('A gestão pode utilizar a estrutura da unidade?','O modelo depende das condições existentes, das necessidades do serviço e da avaliação técnica. A proposta define infraestrutura, responsabilidades e limites da operação.'),('O fornecimento de enxoval está sempre incluído?','Não necessariamente. A aquisição, a disponibilização ou a reposição de enxoval precisam ser expressamente avaliadas e previstas no escopo.'),('Como são definidos os volumes e as rotinas de entrega?','A partir do perfil assistencial, da demanda dos setores e da capacidade da operação, com quantidades e frequências pactuadas para o projeto.')]),
]

COMPLEMENTARY = [
    dict(slug='locacao-de-equipamentos',name='Locação de equipamentos e materiais',icon='equipment',description='Converse sobre a disponibilização de equipamentos e materiais médicos e hospitalares, com condições e escopo definidos para o projeto.'),
    dict(slug='software-e-tecnologia',name='Software e tecnologia',icon='chart',description='Avalie demandas de desenvolvimento e licenciamento de software para apoiar os processos e as necessidades da sua instituição.'),
    dict(slug='capacitacao-de-equipes',name='Capacitação de equipes',icon='book',description='Apresente suas necessidades de treinamento profissional e gerencial para estruturar uma proposta de capacitação.'),
    dict(slug='suprimentos-e-equipamentos',name='Suprimentos e equipamentos',icon='clipboard',description='Consulte possibilidades de fornecimento de instrumentos, materiais e equipamentos para uso médico, hospitalar e laboratorial.'),
]

ARTICLES = [
    dict(slug='engenharia-clinica-alem-da-manutencao',category='Engenharia clínica',filter='engenharia',image='technology',
         title='Engenharia clínica: muito além da manutenção',
         desc='Por que olhar para todo o ciclo de vida dos equipamentos melhora a conversa entre tecnologia e gestão.',
         intro='Um equipamento disponível na hora certa depende de decisões que começam antes de sua chegada à instituição. Planejar, conhecer o parque e organizar registros torna essa gestão mais consistente.',
         sections=[('Olhar para o conjunto','A engenharia clínica ajuda a aproximar as necessidades assistenciais das decisões sobre tecnologia. Conhecer o que existe na unidade é um ponto de partida: quais equipamentos são utilizados, onde estão e como suas informações são organizadas. Esse olhar permite discutir prioridades com mais clareza, em vez de tratar cada ocorrência como um evento isolado.'),('Transformar registros em decisões','Históricos de intervenções, condições de uso e custos podem apoiar a análise da operação. Mais do que acumular registros, o desafio é torná-los úteis para o planejamento. Uma rotina de acompanhamento permite que as áreas técnica e administrativa discutam necessidades, recursos e alternativas a partir de informações compartilhadas.'),('Considerar o ciclo de vida','A gestão da tecnologia inclui planejamento, utilização e avaliação de renovação. A RDC nº 509/2021 da Anvisa estabelece critérios para o gerenciamento de tecnologias em saúde. Para a instituição, essa perspectiva reforça a importância de organizar responsabilidades e informações ao longo da trajetória do equipamento.'),('Começar pelo diagnóstico','Um primeiro passo é reunir o cadastro disponível, os registros existentes e as principais dificuldades relatadas pelas equipes. Com esse panorama, a instituição pode definir o que precisa ser organizado, quais prioridades merecem atenção e quais entregas farão parte do projeto de engenharia clínica.')],
         source='Anvisa — RDC nº 509, de 27 de maio de 2021',url='https://bvsms.saude.gov.br/bvs/saudelegis/anvisa/2020/rdc0509_27_05_2021.pdf',service='engenharia-clinica'),
    dict(slug='cme-rastreabilidade-e-gestao',category='CME e qualidade',filter='cme',image='surgery',
         title='CME: a importância dos registros e da rastreabilidade',
         desc='A organização da informação como parte da gestão dos processos de apoio à assistência.',
         intro='A Central de Material e Esterilização se conecta diariamente a diferentes áreas da instituição. Nessa interface, a qualidade da informação importa tanto para a organização da rotina quanto para o acompanhamento dos processos.',
         sections=[('Uma operação feita de conexões','As necessidades dos setores assistenciais precisam encontrar uma operação organizada. Quando responsabilidades, pontos de passagem e rotinas de comunicação estão claros, torna-se mais fácil acompanhar as demandas e tratar ocorrências. A integração entre áreas é uma questão de gestão que merece atenção contínua.'),('Registros que fazem sentido','Registrar não deve ser um fim em si mesmo. A informação precisa permitir o acompanhamento do processo e estar disponível para quem tem responsabilidade sobre ele. A definição do que registrar, em qual etapa e por quem deve considerar a realidade da unidade e os requisitos aplicáveis ao serviço.'),('Rastreabilidade e boas práticas','A RDC nº 15/2012 da Anvisa trata das boas práticas para serviços que processam produtos para saúde. No campo da gestão, a organização dos registros e a clareza das responsabilidades ajudam a dar suporte ao acompanhamento dessas atividades. A execução exige avaliação dos profissionais responsáveis e dos requisitos específicos de cada processo.'),('Gestão próxima da rotina','Um projeto de melhoria pode começar pelo mapeamento das interfaces da CME: de onde chegam as demandas, como circulam as informações e como as entregas são acompanhadas. A partir daí, a instituição pode identificar dificuldades, revisar fluxos e estabelecer uma rotina de análise com as equipes envolvidas.')],
         source='Anvisa — RDC nº 15, de 15 de março de 2012',url='https://bvsms.saude.gov.br/bvs/saudelegis/anvisa/2012/rdc0015_15_03_2012.pdf',service='cme'),
    dict(slug='lavanderia-gestao-do-enxoval',category='Lavanderia hospitalar',filter='lavanderia',image='laundry-industrial',
         title='Enxoval hospitalar: organização que apoia o cuidado',
         desc='Como conectar a demanda dos setores à gestão da lavanderia e à circulação das peças.',
         intro='O enxoval faz parte de uma rotina que envolve diferentes pessoas e setores. Conhecer essa circulação é importante para planejar necessidades e organizar o serviço de processamento de roupas.',
         sections=[('Conhecer a demanda','As necessidades de enxoval variam conforme o perfil da instituição e as atividades de cada setor. Conversar com as equipes e organizar informações sobre movimentações permite construir uma visão mais clara dessa demanda. O planejamento ganha consistência quando considera o caminho completo das peças.'),('Conectar as etapas','Coleta, processamento e distribuição precisam ser vistos como partes de uma mesma operação. A definição de responsabilidades e rotinas de comunicação ajuda a identificar onde ocorrem dificuldades e quais ajustes precisam ser discutidos. A RDC nº 6/2012 da Anvisa é uma referência para as boas práticas de funcionamento das unidades de processamento de roupas de serviços de saúde.'),('Acompanhar o enxoval','Conhecer quantidades, movimentações e necessidades de reposição permite que a gestão discuta disponibilidade e uso dos recursos. O objetivo é organizar informações que ajudem a compreender a rotina e a tomar decisões sobre o serviço, de acordo com as condições de cada unidade.'),('Construir melhorias possíveis','Antes de escolher ferramentas ou rever contratos, vale mapear a operação existente. Um diagnóstico deve considerar a estrutura disponível, as necessidades assistenciais e as responsabilidades das partes. Esse trabalho permite definir um escopo coerente e prioridades de melhoria que possam ser acompanhadas ao longo do tempo.')],
         source='Anvisa — RDC nº 6, de 30 de janeiro de 2012',url='https://bvsms.saude.gov.br/bvs/saudelegis/anvisa/2012/rdc0006_30_01_2012.html',service='lavanderia-hospitalar'),
]

def button(text, href, cls='', ico='arrow'):
    return f'<a class="button {cls}" href="{href}">{text}{icon(ico)}</a>'

def link(text, href):
    return f'<a class="text-link" href="{href}">{text}{icon("arrow")}</a>'

def image(name, alt, cls='', eager=False):
    return f'<img src="/assets/{name}.jpg" alt="{escape(alt)}" class="{cls}" {"fetchpriority=high" if eager else "loading=lazy"} decoding="async">'

def breadcrumb(items):
    parts=['<a href="/">Início</a>']
    for label,href in items:
        parts.append(icon('chevron'))
        parts.append(f'<a href="{href}">{label}</a>' if href else f'<span aria-current="page">{label}</span>')
    return '<nav class="breadcrumb" aria-label="Você está aqui">'+''.join(parts)+'</nav>'

def page_hero(label,title,desc,crumb=None,extra=''):
    return f'<section class="page-hero"><div class="container">{breadcrumb(crumb or [(label,None)])}<div class="eyebrow">{label}</div><h1>{title}</h1><p class="lead">{desc}</p>{extra}</div><img class="hero-symbol" src="/assets/symbol.svg" alt="" aria-hidden="true"></section>'

def header(active):
    def navlink(label,url,key):
        current=' aria-current="page"' if active==key else ''
        return f'<a class="nav-link" href="{url}"{current}>{label}</a>'
    dropdown=''.join(f'<a href="/solucoes/{s["slug"]}/">{icon(s["icon"])}{s["short"]}</a>' for s in SERVICES)
    return f'''<a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
    <div class="topbar"><div class="container"><span>Gestão e tecnologias em saúde</span><div class="topbar-right"><span>João Pessoa · Paraíba</span><a href="tel:+5583991934988">{icon('phone')}{PHONE}</a></div></div></div>
    <header class="site-header"><div class="container header-inner"><a class="brand" href="/" aria-label="CORE Gestão — início"><img src="/assets/logo.svg" alt="CORE — Gestão e Tecnologias em Saúde" width="204" height="65"></a>
    <button class="menu-toggle" aria-label="Abrir menu" aria-controls="main-nav" aria-expanded="false">{icon('menu')}</button>
    <nav class="main-nav" id="main-nav" aria-label="Navegação principal">{navlink('Início','/','home')}{navlink('A CORE','/a-core/','about')}
    <details class="nav-drop {'active' if active=='services' else ''}"><summary>Soluções{icon('down')}</summary><div class="nav-dropdown">{dropdown}<a class="all-solutions" href="/solucoes/">Todas as soluções{icon('arrow')}</a></div></details>
    {navlink('Como atuamos','/como-atuamos/','approach')}{navlink('Conteúdos','/conteudos/','content')}{navlink('Contato','/contato/','contact')}{button('Solicitar proposta','/contato/#solicitar-proposta','header-cta')}</nav></div></header>'''

def cta():
    return f'<section class="cta-band"><div class="container cta-grid"><div><h2>Vamos cuidar da gestão.<br>Para você cuidar de pessoas.</h2><p>Conte à CORE o que sua instituição precisa.</p></div>{button("Vamos conversar","/contato/","button-white")}</div></section>'

def footer():
    service_links=''.join(f'<li><a href="/solucoes/{s["slug"]}/">{s["short"]}</a></li>' for s in SERVICES)
    return f'''<footer class="site-footer"><div class="container"><div class="footer-grid">
    <div class="footer-brand"><a href="/" aria-label="CORE Gestão — início"><img src="/assets/logo-white.svg" alt="CORE — Gestão e Tecnologias em Saúde" width="221" height="70" loading="lazy"></a><p>Conectamos gestão, pessoas e tecnologia para apoiar o que há de mais importante: o cuidado com a vida.</p></div>
    <div class="footer-col"><h3>Institucional</h3><ul><li><a href="/a-core/">A CORE</a></li><li><a href="/a-core/#nossa-historia">Nossa história</a></li><li><a href="/a-core/#missao-visao">Missão, visão e valores</a></li><li><a href="/como-atuamos/">Como atuamos</a></li><li><a href="/qualidade/">Qualidade e responsabilidade</a></li><li><a href="/trabalhe-conosco/">Trabalhe conosco</a></li></ul></div>
    <div class="footer-col"><h3>Nossas soluções</h3><ul>{service_links}<li><a href="/conteudos/">Conteúdos e conhecimento</a></li></ul></div>
    <div class="footer-col contact-col"><h3>Fale com a CORE</h3><div class="footer-contact">{icon('whatsapp')}<a href="{WA}" target="_blank" rel="noopener noreferrer">{PHONE}</a></div><div class="footer-contact">{icon('mail')}<a href="mailto:{EMAIL}">{EMAIL}</a></div><div class="footer-contact">{icon('pin')}<p>Av. Nossa Senhora de Fátima,<br>nº 1646 e 1650, Torre<br>João Pessoa — PB · CEP 58040-380</p></div></div>
    </div><div class="footer-bottom"><span>© 2026 CORE Gestão e Tecnologias em Saúde.<br>CNPJ {CNPJ} · Imagens ilustrativas.</span><div class="footer-bottom-links"><a href="/privacidade/">Privacidade</a><a href="/mapa-do-site/">Mapa do site</a><a href="/contato/">Contato</a></div></div></div></footer>
    <a class="floating-contact" href="{WA}" target="_blank" rel="noopener noreferrer" aria-label="Conversar com a CORE pelo WhatsApp">{icon('whatsapp')}<span>Fale com a CORE</span></a>'''

def write_page(path,title,description,body,active=''):
    target=DIST/path.strip('/')/'index.html' if path!='404.html' else DIST/'404.html'
    target.parent.mkdir(parents=True,exist_ok=True)
    url=ORIGIN+('/'+path.strip('/')+'/' if path.strip('/') else '/')
    if path=='404.html':url=ORIGIN+'/404.html'
    organization={'@context':'https://schema.org','@type':'Organization','name':'CORE Gestão e Tecnologias em Saúde','taxID':CNPJ,'foundingDate':FOUNDING_DATE,'url':ORIGIN,'logo':ORIGIN+'/assets/logo.svg','email':EMAIL,'telephone':'+5583991934988','address':{'@type':'PostalAddress','streetAddress':'Avenida Nossa Senhora de Fátima, 1646 e 1650, Torre','addressLocality':'João Pessoa','addressRegion':'PB','postalCode':'58040-380','addressCountry':'BR'}}
    html=f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} | CORE Gestão</title><meta name="description" content="{escape(description,quote=True)}"><meta name="theme-color" content="#123d56"><link rel="canonical" href="{url}"><link rel="icon" href="/assets/symbol.svg" type="image/svg+xml"><link rel="preload" href="/assets/manrope-vf.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/assets/style.css"><meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="CORE Gestão e Tecnologias em Saúde"><meta property="og:title" content="{escape(title,quote=True)} | CORE Gestão"><meta property="og:description" content="{escape(description,quote=True)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{ORIGIN}/assets/surgery.jpg"><script type="application/ld+json">{json.dumps(organization,ensure_ascii=False)}</script><script src="/assets/site.js" defer></script></head><body>{header(active)}<main id="conteudo">{body}</main>{footer()}</body></html>'''
    if BASE_PATH:
        html=re.sub(r'((?:href|src|action)=")(/(?!/)[^"]*)(")',lambda m:m[1]+BASE_PATH+m[2]+m[3],html)
    if path=='404.html':
        html=html.replace('<meta name="theme-color"', '<meta name="robots" content="noindex"><meta name="theme-color"',1)
    target.write_text(html,encoding='utf-8')

def article_card(a):
    href=f'/conteudos/{a["slug"]}/'
    return f'<article class="article-card" data-category="{a["filter"]}"><a href="{href}" class="article-image" tabindex="-1" aria-hidden="true">{image(a["image"],a["title"])}</a><span class="article-category">{a["category"]}</span><h3><a href="{href}">{a["title"]}</a></h3><p>{a["desc"]}</p>{link("Ler conteúdo",href)}</article>'

def faq(items):
    return '<div class="accordion">'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items)+'</div>'

def service_cards():
    cards=[]
    for i,s in enumerate(SERVICES):
        href=f'/solucoes/{s["slug"]}/'
        if i==0:
            cards.append(f'<a class="solution-card solution-feature" href="{href}">{image("hero","Tecnologia a serviço da gestão em saúde","feature-img")}<span class="number">01</span><div class="feature-body">{icon(s["icon"])}<h3>{s["name"]}</h3><p>{s["description"]}</p><div class="card-bottom"><span>Conheça a solução</span>{icon("up-right")}</div></div></a>')
        else:
            cards.append(f'<a class="solution-card" href="{href}">{icon(s["icon"])}<span class="number">0{i+1}</span><h3>{s["name"]}</h3><p>{s["description"]}</p><div class="card-bottom"><span>Conheça a solução</span>{icon("up-right")}</div></a>')
    return ''.join(cards)

def home():
    strip=''.join(f'<a class="strip-link" href="/solucoes/{s["slug"]}/">{icon(s["icon"])}<span>{s["short"]}</span>{icon("up-right","mini-arrow")}</a>' for s in SERVICES)
    body=f'''<section class="home-hero"><div class="container hero-grid"><div class="hero-copy"><div class="eyebrow">Pessoas, processos e tecnologia</div><h1>A gestão por trás<br>de um cuidado<br><span>melhor.</span></h1><p>Soluções em saúde que conectam a assistência, a tecnologia e os serviços de apoio à sua instituição.</p><div class="button-row">{button('Conheça as soluções','/solucoes/')}{link('Conheça a CORE','/a-core/')}</div></div><div class="hero-photo">{image('surgery','Profissionais de saúde trabalhando em equipe em um ambiente assistencial',eager=True)}<div class="photo-corner"></div><span class="hero-photo-label">GESTÃO + TECNOLOGIA + CUIDADO</span><div class="hero-caption">{icon('heart')}<strong>O cuidado começa muito<br>antes do atendimento.</strong><small>CORE · Gestão e tecnologias em saúde</small></div></div></div></section>
    <nav class="service-strip" aria-label="Explore nossas soluções"><div class="container strip-inner">{strip}</div></nav>
    <section class="section"><div class="container intro-grid"><div><div class="eyebrow">Conexões que fazem a diferença</div><h2>Uma visão integrada.<br>O cuidado em cada ponto.</h2></div><div class="intro-right"><p class="lead">Por trás de cada atendimento, há uma operação que precisa funcionar. A CORE conecta gestão da saúde, serviços médicos, engenharia clínica, CME e lavanderia hospitalar.</p><div class="beliefs"><span>{icon('check-circle')}Pessoas no centro</span><span>{icon('check-circle')}Gestão próxima</span><span>{icon('check-circle')}Visão técnica</span></div>{link('Nossa essência','/a-core/#missao-visao')}</div></div></section>
    <section class="section bg-paper"><div class="container"><div class="section-head"><div><div class="eyebrow">Soluções para a sua instituição</div><h2>Cada especialidade.<br>O mesmo compromisso.</h2></div><p>Da assistência aos serviços de apoio, uma proposta de gestão conectada à realidade de cada operação.</p></div><div class="solutions-grid">{service_cards()}</div></div></section>
    <section class="section"><div class="container care-grid"><div class="care-image">{image('care','Profissional de saúde utilizando tecnologia na rotina de trabalho')}<span class="image-label">Tecnologia com propósito. Gestão com cuidado.</span></div><div class="care-content"><div class="eyebrow">Como atuamos</div><h2>Entender primeiro.<br>Construir juntos.<br>Evoluir sempre.</h2><p>Cada instituição tem um contexto. Nossa proposta começa por ouvir e compreender os desafios para definir um escopo de trabalho coerente com a sua necessidade.</p><ol class="numbered-list"><li><span class="num">01</span><div><strong>Escuta e diagnóstico</strong><p>Conhecer a estrutura, a demanda e as prioridades.</p></div></li><li><span class="num">02</span><div><strong>Planejamento e integração</strong><p>Conectar as entregas às pessoas e aos processos.</p></div></li><li><span class="num">03</span><div><strong>Acompanhamento e melhoria</strong><p>Transformar informações em decisões de gestão.</p></div></li></ol>{link('Conheça nossa abordagem','/como-atuamos/')}</div></div></section>
    <section class="section-sm bg-mint"><div class="container segments"><div class="segment">{icon('hospital')}<div><h3>Hospitais e unidades de saúde</h3><p>Integração entre a operação assistencial e os serviços de apoio.</p></div></div><div class="segment">{icon('clinic')}<div><h3>Clínicas e centros de atendimento</h3><p>Organização alinhada ao perfil e à dimensão de cada serviço.</p></div></div><div class="segment">{icon('people')}<div><h3>Gestores públicos e privados</h3><p>Visão técnica e planejamento para os desafios da instituição.</p></div></div></div></section>
    <section class="section"><div class="container"><div class="section-head"><div><div class="eyebrow">Conhecimento que conecta</div><h2>Um olhar sobre a saúde.<br>E sobre como fazê-la avançar.</h2></div>{link('Explore os conteúdos','/conteudos/')}</div><div class="article-grid">{''.join(article_card(a) for a in ARTICLES)}</div></div></section>{cta()}'''
    write_page('','Gestão e tecnologias em saúde','Conheça a CORE: gestão da saúde, serviços médicos, engenharia clínica, CME e lavanderia hospitalar. João Pessoa, Paraíba.',body,'home')

def about():
    values=[('heart','Cuidado com a vida','Colocar as pessoas e suas necessidades no centro das decisões.'),('shield','Ética e transparência','Conduzir relações com integridade, respeito e clareza.'),('equipment','Responsabilidade técnica','Valorizar conhecimento, critérios técnicos e atribuições profissionais.'),('refresh','Melhoria contínua','Aprender com a rotina e buscar evolução nos processos.'),('people','Colaboração','Conectar equipes, ouvir e construir soluções em conjunto.'),('leaf','Sustentabilidade','Promover o uso responsável dos recursos e uma visão de longo prazo.')]
    body=page_hero('A CORE','Gestão, tecnologia e pessoas.<br>Um propósito em comum.','Conheça a essência da CORE Gestão e Tecnologias em Saúde e a visão que conecta nossas áreas de atuação.')
    body+='''<nav class="page-tabs" aria-label="Nesta página"><div class="container"><a href="#nossa-historia">Nossa história</a><a href="#missao-visao">Missão e visão</a><a href="#valores">Nossos valores</a></div></nav>'''
    body+=f'''<section class="section" id="nossa-historia"><div class="container story-grid"><div class="story-copy"><div class="eyebrow">Nossa história · Desde 2022</div><h2>A conexão entre a gestão e o cuidado.</h2><p>Com atividades iniciadas em <strong>7 de dezembro de 2022</strong> e sede em João Pessoa, na Paraíba, a CORE Gestão e Tecnologias em Saúde reúne organização, conhecimento técnico e cuidado com as pessoas em uma proposta integrada para as instituições de saúde.</p><p>Seus cinco eixos principais conectam gestão da saúde, serviços médicos, engenharia clínica, Central de Material e Esterilização e lavanderia hospitalar. Essa visão também abre espaço para avaliar demandas de locação, software, capacitação e fornecimento de materiais e equipamentos.</p><p>A trajetória da CORE é orientada pela busca de uma gestão próxima da realidade de cada instituição: ouvir as equipes, compreender necessidades e construir soluções com responsabilidade.</p><dl class="company-facts"><div><dt>Início das atividades</dt><dd>7 de dezembro de 2022</dd></div><div><dt>CNPJ</dt><dd>{CNPJ}</dd></div></dl><div class="quote">Cuidar da gestão também é uma forma de cuidar de pessoas.</div></div>{image('hero','Gestão e tecnologia presentes na rotina da saúde','story-image')}</div></section>
    <section class="section bg-paper" id="missao-visao"><div class="container"><div class="eyebrow">Nossa essência</div><h2>O propósito que orienta.<br>A visão que nos move.</h2><div class="principles"><div class="principle">{icon('target')}<h3>Missão</h3><p>Conectar pessoas, gestão e tecnologia para apoiar serviços de saúde mais seguros, eficientes e humanizados.</p></div><div class="principle">{icon('eye')}<h3>Visão</h3><p>Ser reconhecida como parceira estratégica de instituições de saúde pela qualidade da gestão, pela confiabilidade técnica e pelo compromisso com as pessoas.</p></div></div></div></section>
    <section class="section" id="valores"><div class="container"><div class="eyebrow">Nossos valores</div><h2>Princípios que se traduzem<br>em atitudes.</h2><div class="values-grid">{''.join(f'<div class="value">{icon(i)}<div><h3>{t}</h3><p>{d}</p></div></div>' for i,t,d in values)}</div></div></section>{cta()}'''
    write_page('a-core','A CORE — história, missão, visão e valores','Conheça a CORE Gestão e Tecnologias em Saúde: apresentação institucional, história, missão, visão e valores.',body,'about')

def solutions():
    body=page_hero('Nossas soluções','Especialidades que se conectam.<br>Para a saúde funcionar melhor.','Explore as áreas de atuação da CORE e encontre uma proposta de trabalho para a realidade da sua instituição.')
    rows=[]
    for n,s in enumerate(SERVICES,1):
        tags=''.join(f'<span class="tag">{escape(t)}</span>' for t in s['tags'])
        rows.append(f'<article class="service-row"><div class="service-row-image">{image(s["image"],s["alt"])}<span class="row-number">0{n}</span></div><div class="service-row-body">{icon(s["icon"])}<h2>{s["name"]}</h2><p>{s["description"]}</p><div class="tags">{tags}</div>{link("Explore a solução",f"/solucoes/{s['slug']}/")}</div></article>')
    complementary=''.join(f'<article class="complementary-card"><div class="complementary-card-top">{icon(s["icon"])}<span class="tag">Sob consulta</span></div><h3>{s["name"]}</h3><p>{s["description"]}</p>{link("Conversar sobre esta frente",f"/contato/?servico={s['slug']}#solicitar-proposta")}</article>' for s in COMPLEMENTARY)
    body+=f'<section class="section bg-paper"><div class="container service-list">{"".join(rows)}</div></section><section class="section" id="solucoes-complementares"><div class="container"><div class="section-head"><div><div class="eyebrow">Soluções complementares</div><h2>Outras conexões para<br>o seu projeto.</h2></div><p>Além dos cinco eixos principais, sua instituição pode conversar com a CORE sobre demandas complementares. A viabilidade e o escopo são avaliados para cada projeto.</p></div><div class="complementary-grid">{complementary}</div></div></section>{cta()}'
    write_page('solucoes','Soluções em saúde','Gestão da saúde, serviços médicos, engenharia clínica, CME e lavanderia hospitalar. Explore as soluções da CORE.',body,'services')

def service_pages():
    for s in SERVICES:
        related=''.join(f'<li><a href="/solucoes/{other["slug"]}/">{other["short"]}{icon("arrow")}</a></li>' for other in SERVICES if other!=s)
        deliverables=''.join(f'<div class="deliverable">{icon(i)}<h3>{t}</h3><p>{d}</p></div>' for i,t,d in s['deliverables'])
        metrics=''.join(f'<div class="metric"><span class="label">{l}</span><h3>{t}</h3><p>{d}</p></div>' for l,t,d in s['metrics'])
        body=f'''<section class="page-hero"><div class="container">{breadcrumb([('Soluções','/solucoes/'),(s['short'],None)])}<div class="service-hero-grid"><div><div class="eyebrow">{s['name']}</div><h1>{s['headline']}</h1><p class="lead">{s['description']}</p><div class="button-row">{button('Conversar sobre esta solução',f'/contato/?servico={s["slug"]}#solicitar-proposta')}</div></div>{image(s['image'],s['alt'],'service-hero-image',True)}</div></div></section>
        <section class="section"><div class="container detail-grid"><div class="detail-main"><div class="eyebrow">A solução na prática</div><h2>{s['name']}</h2><p>{s['intro']}</p><div class="deliverables">{deliverables}</div><p class="scope-note">O modelo de atuação, as responsabilidades e as entregas são definidos a partir da avaliação da demanda e do escopo contratado.</p></div><aside class="detail-aside"><h3>Como podemos apoiar sua instituição?</h3><p>Conte o perfil da unidade e os desafios que deseja resolver. Vamos avaliar sua necessidade.</p>{button('Solicitar uma proposta',f'/contato/?servico={s["slug"]}#solicitar-proposta')}<ul class="aside-links">{related}</ul></aside></div></section>
        <section class="section bg-mint"><div class="container"><div class="eyebrow">O que orienta a solução</div><h2>Gestão com foco no que importa.</h2><div class="metric-grid">{metrics}</div></div></section>
        <section class="section"><div class="container faq-layout"><div><div class="eyebrow">Dúvidas frequentes</div><h2>Vamos esclarecer?</h2><p>Encontre informações sobre a estruturação desta solução.</p></div>{faq(s['faqs'])}</div></section>{cta()}'''
        write_page('solucoes/'+s['slug'],s['name'],s['description'],body,'services')

def approach():
    steps=[('Escuta e diagnóstico','Compreender o perfil da unidade, suas necessidades e as condições atuais de operação.'),('Desenho da solução','Delimitar o escopo, as responsabilidades, as interfaces e as entregas do projeto.'),('Organização e implantação','Planejar a mobilização, alinhar as equipes e estruturar as rotinas acordadas.'),('Acompanhamento e evolução','Reunir informações, analisar indicadores e construir planos de melhoria.')]
    body=page_hero('Como atuamos','A melhor solução começa<br>por entender a sua realidade.','Uma abordagem que conecta diagnóstico, planejamento e acompanhamento, com diálogo entre a CORE e a instituição.')
    body+=f'''<section class="section"><div class="container"><div class="section-head"><div><div class="eyebrow">Da necessidade à operação</div><h2>Um caminho construído<br>com a sua instituição.</h2></div><p>Cada etapa ajuda a transformar um desafio de gestão em um plano de trabalho claro e acompanhável.</p></div><div class="steps">{''.join(f'<div class="step"><span class="step-num">0{n}</span><h3>{t}</h3><p>{d}</p></div>' for n,(t,d) in enumerate(steps,1))}</div></div></section>
    <section class="section bg-paper"><div class="container quality-feature">{image('hero','Tecnologia utilizada no planejamento da rotina de saúde')}<div><div class="eyebrow">Uma visão integrada</div><h2>Pessoas, rotinas e informação na mesma direção.</h2><p>A gestão ganha força quando as áreas compreendem suas responsabilidades e compartilham informações relevantes. É essa conexão que orienta a proposta da CORE.</p><ul class="quality-points"><li>{icon('check-circle')}Escopo compatível com a necessidade da instituição.</li><li>{icon('check-circle')}Responsabilidades e interfaces definidas.</li><li>{icon('check-circle')}Rotinas de comunicação e acompanhamento.</li><li>{icon('check-circle')}Indicadores voltados às decisões de gestão.</li></ul><div class="button-row">{link('Qualidade e responsabilidade','/qualidade/')}</div></div></div></section>
    <section class="section"><div class="container faq-layout"><div><div class="eyebrow">Antes de começar</div><h2>O que precisamos conhecer?</h2><p>Algumas informações ajudam a qualificar nossa primeira conversa.</p></div>{faq([('O perfil da instituição','Tipo de unidade, localização, serviços existentes e principais características da operação.'),('A necessidade de apoio','Área de interesse, dificuldades identificadas e objetivos que motivam a busca pela solução.'),('A estrutura e o momento do projeto','Recursos e estrutura disponíveis, eventuais condições de transição e expectativas para a implantação.')])}</div></section>{cta()}'''
    write_page('como-atuamos','Como atuamos','Conheça a abordagem da CORE: escuta, diagnóstico, planejamento, organização e acompanhamento dos projetos em saúde.',body,'approach')

def quality():
    body=page_hero('Qualidade e responsabilidade','Cuidado é também<br>a forma de fazer.','Nossa proposta de gestão valoriza processos organizados, atribuições claras e atenção às pessoas em cada etapa da operação.')
    points=[('shield','Segurança como prioridade','Considerar os riscos da operação e as interfaces entre os processos e a assistência.'),('clipboard','Processos e registros','Organizar rotinas e informações que apoiem o acompanhamento do serviço.'),('people','Responsabilidade profissional','Respeitar atribuições técnicas e requisitos profissionais aplicáveis ao escopo.'),('refresh','Aprendizado e melhoria','Analisar ocorrências e oportunidades para aperfeiçoar os processos.'),('leaf','Uso responsável dos recursos','Considerar consumo, conservação e redução de desperdícios nas decisões.'),('lock','Respeito às informações','Tratar as informações com cuidado e orientar o contato pelos canais adequados.')]
    body+=f'''<section class="section"><div class="container"><div class="eyebrow">Compromissos de gestão</div><h2>Uma atenção que atravessa<br>todas as nossas áreas.</h2><div class="values-grid">{''.join(f'<div class="value">{icon(i)}<div><h3>{t}</h3><p>{d}</p></div></div>' for i,t,d in points)}</div></div></section>
    <section class="section bg-paper"><div class="container quality-feature">{image('surgery','Profissionais de saúde em uma operação assistencial')}<div><div class="eyebrow">Técnica e cuidado</div><h2>A qualidade se constrói<br>na rotina.</h2><p>Mais do que uma intenção, a qualidade exige atenção às condições reais de trabalho. Por isso, diagnóstico, organização de processos e acompanhamento precisam caminhar juntos.</p><p>A definição de requisitos técnicos e sanitários integra a avaliação de cada projeto, de acordo com o serviço e o modelo de execução.</p><div class="button-row">{link('Veja como atuamos','/como-atuamos/')}</div></div></div></section>{cta()}'''
    write_page('qualidade','Qualidade e responsabilidade','Conheça os compromissos de gestão da CORE com processos, responsabilidade técnica, pessoas e melhoria contínua.',body,'approach')

def content_pages():
    body=page_hero('Conteúdos','Conhecimento que ajuda<br>a cuidar da gestão.','Reflexões introdutórias sobre tecnologia, processos e serviços de apoio à saúde. Explore por tema ou pesquise um assunto.')
    filters=[('all','Todos'),('engenharia','Engenharia clínica'),('cme','CME'),('lavanderia','Lavanderia hospitalar')]
    body+=f'''<section class="section"><div class="container"><div class="filter-bar"><div class="filter-buttons" aria-label="Filtrar conteúdos por tema">{''.join(f'<button class="filter-btn" data-filter="{key}" aria-pressed="{str(key=="all").lower()}">{label}</button>' for key,label in filters)}</div><label class="search-field">{icon('search')}<span class="sr-only">Pesquisar conteúdos</span><input id="article-search" type="search" placeholder="Pesquisar um assunto..."></label></div><p id="filter-status" class="sr-only" aria-live="polite">3 conteúdos encontrados</p><div class="article-grid">{''.join(article_card(a) for a in ARTICLES)}</div><div class="empty-state" hidden>Nenhum conteúdo encontrado. Experimente outro termo ou selecione “Todos”.</div></div></section>{cta()}'''
    write_page('conteudos','Conteúdos e conhecimento','Conteúdos sobre engenharia clínica, CME e lavanderia hospitalar. Explore temas de gestão e tecnologia em saúde.',body,'content')
    for a in ARTICLES:
        sections=''.join(f'<section id="topico-{i}"><h2>{t}</h2><p>{p}</p></section>' for i,(t,p) in enumerate(a['sections'],1))
        aside=''.join(f'<a href="#topico-{i}">{t}</a>' for i,(t,_) in enumerate(a['sections'],1))
        body=page_hero(a['category'],a['title'],a['intro'],[('Conteúdos','/conteudos/'),(a['category'],None)])
        body+=f'''<section class="section"><div class="container article-layout"><article class="article-body">{image(a['image'],a['title'],'article-cover')}{sections}<div class="source-note"><strong>Leitura complementar</strong><p>Conteúdo introdutório sobre gestão. A definição e a execução de processos técnicos exigem avaliação dos profissionais responsáveis e dos requisitos aplicáveis.</p><a href="{a['url']}" target="_blank" rel="noopener noreferrer">{a['source']} ↗</a></div><div class="button-row">{link('Voltar aos conteúdos','/conteudos/')}</div></article><aside class="article-aside"><h3>Neste conteúdo</h3>{aside}<a href="/solucoes/{a['service']}/">Conheça a solução da CORE →</a></aside></div></section>{cta()}'''
        write_page('conteudos/'+a['slug'],a['title'],a['desc'],body,'content')

def contact():
    options='<option value="">Selecione a área de interesse</option>'+''.join(f'<option value="{s["slug"]}">{s["name"]}</option>' for s in SERVICES)+'<optgroup label="Soluções complementares">'+''.join(f'<option value="{s["slug"]}">{s["name"]}</option>' for s in COMPLEMENTARY)+'</optgroup><option value="integrada">Soluções integradas / outras demandas</option>'
    body=page_hero('Contato','Uma boa conversa pode<br>transformar a sua operação.','Compartilhe sua necessidade. Vamos entender como a CORE pode apoiar a gestão e os serviços da sua instituição.')
    body+=f'''<section class="section"><div class="container contact-layout"><div class="contact-info"><div class="eyebrow">Fale com a CORE</div><h2>Vamos conversar?</h2><p>Escolha o canal mais conveniente ou prepare uma solicitação com as informações da sua instituição.</p><div class="contact-block">{icon('whatsapp')}<div><h3>Telefone e WhatsApp</h3><a href="{WA}" target="_blank" rel="noopener noreferrer">{PHONE} ↗</a><br><a href="tel:+5583991934988">Prefere ligar? Toque aqui.</a></div></div><div class="contact-block">{icon('mail')}<div><h3>E-mail</h3><a href="mailto:{EMAIL}">{EMAIL}</a></div></div><div class="contact-block">{icon('pin')}<div><h3>Endereço</h3><p>Avenida Nossa Senhora de Fátima,<br>nº 1646 e 1650, Torre<br>João Pessoa — PB · CEP 58040-380</p><a class="map-link" href="{MAP}" target="_blank" rel="noopener noreferrer">Ver localização no Google Maps ↗</a></div></div><div class="contact-block">{icon('clipboard')}<div><h3>Identificação da empresa</h3><p>CORE Gestão e Tecnologias em Saúde<br>CNPJ {CNPJ}</p></div></div><div class="contact-note"><strong>Um canal para instituições e parceiros.</strong><p>Para agendar consultas ou obter informações sobre atendimento, procure diretamente os canais da sua unidade de saúde.</p></div></div>
    <form class="contact-form" id="contact-form"><div id="solicitar-proposta"><h2>Conte o que você precisa.</h2><p class="form-intro">Preencha os campos e escolha enviar sua solicitação por WhatsApp ou e-mail.</p></div><div class="form-grid"><div class="field"><label for="nome">Seu nome *</label><input name="nome" id="nome" autocomplete="name" placeholder="Como podemos chamar você?" maxlength="120" required></div><div class="field"><label for="email">E-mail *</label><input name="email" id="email" type="email" autocomplete="email" placeholder="voce@instituicao.com.br" maxlength="180" required></div><div class="field"><label for="instituicao">Instituição / empresa *</label><input name="instituicao" id="instituicao" autocomplete="organization" placeholder="Nome da instituição" maxlength="180" required></div><div class="field"><label for="telefone">Telefone</label><input name="telefone" id="telefone" type="tel" autocomplete="tel" placeholder="(00) 00000-0000" maxlength="30"></div><div class="field full"><label for="servico">Área de interesse *</label><select name="servico" id="servico" required>{options}</select></div><div class="field full"><label for="mensagem">Como podemos ajudar? *</label><textarea name="mensagem" id="mensagem" placeholder="Conte o perfil da sua unidade e a necessidade de apoio. Evite dados de pacientes ou informações clínicas." maxlength="2000" required></textarea></div></div><label class="form-consent"><input type="checkbox" name="privacidade" required><span>Li o <a href="/privacidade/">aviso de privacidade</a> e estou ciente de como os dados desta solicitação serão utilizados.</span></label><button class="button form-submit" type="submit">Preparar solicitação{icon('arrow')}</button><p class="form-hint">Você escolhe o canal e conclui o envio na próxima etapa.</p><div class="form-result" id="form-result" role="status" tabindex="-1" hidden><h3>Sua solicitação está pronta.</h3><p>Escolha um canal para revisar a mensagem e concluir o envio. Nenhuma mensagem foi enviada automaticamente.</p><a class="button button-teal" data-whatsapp target="_blank" rel="noopener noreferrer">Abrir no WhatsApp{icon('whatsapp')}</a><a class="button button-outline" data-email>Abrir por e-mail{icon('mail')}</a></div><noscript><p class="scope-note">Para contato, escreva para {EMAIL} ou ligue para {PHONE}.</p></noscript></form></div></section>'''
    write_page('contato','Contato e solicitação de proposta','Converse com a CORE em João Pessoa. Telefone (83) 99193-4988, e-mail coregestaoadm@gmail.com e solicitação de proposta.',body,'contact')

def careers():
    body=page_hero('Trabalhe conosco','O cuidado também se faz<br>com boas conexões.','Pessoas com responsabilidade, interesse em aprender e disposição para trabalhar em equipe fazem a diferença na saúde.')
    body+=f'''<section class="section"><div class="container career-grid"><div class="career-copy"><div class="eyebrow">Conecte sua trajetória à CORE</div><h2>Quer apresentar<br>seu trabalho?</h2><p>Entre em contato para apresentar seu perfil e conversar sobre oportunidades nas áreas de gestão, assistência e serviços de apoio.</p><p>No e-mail, informe sua área de atuação, cidade e um resumo da sua experiência. Se desejar, anexe o currículo diretamente à mensagem.</p><div class="button-row">{button('Apresentar meu perfil','mailto:coregestaoadm@gmail.com?subject=Apresenta%C3%A7%C3%A3o%20profissional%20%7C%20CORE','', 'mail')}</div><p class="scope-note">Este canal recebe apresentações profissionais. O contato não corresponde à divulgação de uma vaga específica nem garante participação em seleção.</p></div>{image('care','Profissional utilizando tecnologia no ambiente de saúde')}</div></section>{cta()}'''
    write_page('trabalhe-conosco','Trabalhe conosco','Apresente sua experiência à CORE Gestão e Tecnologias em Saúde. Contato para profissionais das áreas de saúde, gestão e apoio.',body)

def privacy():
    body=page_hero('Privacidade','Respeito às suas informações.','Saiba como funciona o contato pelos canais deste site e quais cuidados adotar ao compartilhar dados.')
    body+=f'''<section class="section"><div class="container prose"><h2>Sobre este site</h2><p>Este é o site institucional da CORE Gestão e Tecnologias em Saúde. Ele apresenta as áreas de atuação e oferece canais para contato profissional e comercial.</p><h2>O que acontece com o formulário</h2><p>O formulário prepara uma mensagem no seu navegador a partir dos dados que você preencher: nome, e-mail, instituição, telefone e descrição da necessidade. O site não mantém um cadastro ou banco de solicitações e não envia esses dados automaticamente.</p><p>Ao escolher WhatsApp ou e-mail, você abre o serviço correspondente para revisar e concluir o envio. A partir daí, o tratamento das informações também depende das práticas e condições do provedor utilizado e do atendimento realizado pela CORE.</p><h2>Finalidade do contato</h2><p>As informações encaminhadas aos canais da CORE são destinadas à análise da solicitação, à comunicação com o interessado e ao eventual desenvolvimento de uma proposta. Compartilhe apenas os dados necessários ao contato.</p><h2>Informações de saúde</h2><p>Evite inserir dados de pacientes, prontuários, documentos de saúde ou outras informações sensíveis no formulário. Este canal não é destinado a atendimento clínico, agendamento de consultas ou urgências.</p><h2>Cookies e serviços externos</h2><p>Esta versão do site não utiliza ferramentas próprias de publicidade, análise de audiência ou cookies de marketing. A hospedagem pode tratar informações técnicas de acesso para funcionamento e segurança. Links para WhatsApp, e-mail e Google Maps levam a serviços externos sujeitos às suas próprias políticas.</p><h2>Contato sobre dados pessoais</h2><p>Para dúvidas ou solicitações relacionadas às informações encaminhadas à CORE, entre em contato pelo e-mail <a href="mailto:{EMAIL}">{EMAIL}</a>. Informe a natureza do pedido, evitando incluir dados sensíveis na mensagem inicial.</p><h2>Imagens e conteúdo</h2><p>As fotografias deste site são ilustrativas e não representam necessariamente instalações, profissionais ou operações da CORE. Os conteúdos editoriais são introdutórios e não substituem a avaliação dos profissionais responsáveis por cada serviço.</p></div></section>'''
    write_page('privacidade','Aviso de privacidade','Entenda o funcionamento do formulário e dos canais de contato da CORE, o uso de informações e os serviços externos.',body)

def sitemap():
    groups=[('Institucional',[('Início','/'),('A CORE','/a-core/'),('Como atuamos','/como-atuamos/'),('Qualidade e responsabilidade','/qualidade/'),('Trabalhe conosco','/trabalhe-conosco/')]),('Soluções',[('Todas as soluções','/solucoes/')]+[(s['name'],'/solucoes/'+s['slug']+'/') for s in SERVICES]),('Conteúdos e contato',[('Todos os conteúdos','/conteudos/')]+[(a['title'],'/conteudos/'+a['slug']+'/') for a in ARTICLES]+[('Contato e proposta','/contato/'),('Privacidade','/privacidade/')])]
    body=page_hero('Mapa do site','Encontre o que procura.','Todas as páginas da CORE em um só lugar.')
    body+='<section class="section"><div class="container sitemap-grid">'+''.join(f'<div><h2>{title}</h2>'+''.join(f'<a href="{url}">{label}</a>' for label,url in pages)+'</div>' for title,pages in groups)+'</div></section>'
    write_page('mapa-do-site','Mapa do site','Acesse todas as páginas da CORE Gestão e Tecnologias em Saúde.',body)

def build():
    DIST.mkdir(parents=True,exist_ok=True)
    shutil.copytree(ASSETS,DIST/'assets',dirs_exist_ok=True)
    css=DIST/'assets/style.css'
    css.write_text(css.read_text().replace("url('/assets/",f"url('{BASE_PATH}/assets/"))
    home();about();solutions();service_pages();approach();quality();content_pages();contact();careers();privacy();sitemap()
    write_page('404.html','Página não encontrada','Encontre as soluções da CORE Gestão e Tecnologias em Saúde.',f'<section class="notfound"><div class="container"><div class="error-number">404</div><h1>Vamos encontrar<br>o caminho certo.</h1><p>A página que você procura não está disponível neste endereço.</p>{button("Voltar ao início","/")}</div></section>')
    paths=['/','/a-core/','/solucoes/','/como-atuamos/','/qualidade/','/conteudos/','/contato/','/trabalhe-conosco/','/privacidade/','/mapa-do-site/']+['/solucoes/'+s['slug']+'/' for s in SERVICES]+['/conteudos/'+a['slug']+'/' for a in ARTICLES]
    (DIST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{ORIGIN}{p}</loc></url>' for p in paths)+'</urlset>')
    (DIST/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {ORIGIN}/sitemap.xml\n')
    (DIST/'.nojekyll').write_text('')
    print(f'Generated {len(paths)} pages + 404. Assets are local and navigation is multipage.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Build the complete CORE static website.')
    parser.add_argument('--output',default='dist',help='Output directory, relative to this project or absolute.')
    parser.add_argument('--site-url',default=ORIGIN,help='Full public base URL, including the repository path when applicable.')
    parser.add_argument('--base-path',default=os.environ.get('CORE_BASE_PATH',''),help='Public path prefix, e.g. /CORE; empty for root hosting.')
    args=parser.parse_args()
    public_url=urlsplit(args.site_url)
    if public_url.scheme not in ('http','https') or not public_url.netloc or public_url.query or public_url.fragment:
        parser.error('--site-url must be an absolute HTTP(S) URL without query or fragment.')
    ORIGIN=args.site_url.rstrip('/')
    BASE_PATH=('/'+args.base_path.strip('/')) if args.base_path.strip('/') else ''
    if any(part in ('.','..') for part in BASE_PATH.split('/')) or any(c in BASE_PATH for c in '?#\\'):
        parser.error('--base-path must be a URL path without traversal, query, fragment or backslash.')
    DIST=(ROOT/args.output).resolve()
    if DIST==ROOT or DIST==ASSETS or ASSETS.is_relative_to(DIST):
        parser.error('--output must not be the project root or the source assets directory.')
    build()
