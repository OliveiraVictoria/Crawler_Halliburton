
# Função para validar a montagem
# validacoes.py
from bs4 import BeautifulSoup

def carregar_html(caminho_html):
    with open(caminho_html, 'r', encoding='utf-8') as arquivo:
        return BeautifulSoup(arquivo, 'html.parser')

def coletar_componentes(soup):
    componente_tags = soup.select('#component-parts .assembly')
    return [tag.text.strip() for tag in componente_tags]

def coletar_procedures(soup):
    procedure_tags = soup.select('#component-parts .procedure')
    return [tag.text.strip() for tag in procedure_tags]

def coletar_definition_objects(soup):
    definition_tags = soup.select('#definition-objects .engr-drawing, #definition-objects .wiring-diagram')
    return [tag.text.strip() for tag in definition_tags]

def validar_componentes(componentes, definition_objects):
    erros = []
    for componente in componentes:
        if componente not in definition_objects:
            erros.append(f"Componente '{componente}' listado em Component Parts não encontrado em Definition Objects.")
    return erros

def validar_procedures(procedures, definition_objects):
    erros = []
    for procedure in procedures:
        if procedure not in definition_objects:
            erros.append(f"Procedure '{procedure}' listado em Component Parts não encontrado em Definition Objects.")
    return erros

    
    
#Criamos agora o arquivo validacoes.py, com a primeira regra: Validação de Montagem.
#Resumo do que o validar_montagem faz:
#Verifica se existem 4 Assemblies.
#Garante que cada arquivo termine com SIDASM.
#Verifica se existe 1 Engr Drawing na seção Definition Objects.