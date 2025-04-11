import os
from bs4 import BeautifulSoup
from unidecode import unidecode
from datetime import datetime  # <-- para salvar o relatório com data

# Função para carregar os arquivos HTML
def carregar_htmls(pasta='exemplos_cwi'):
    htmls = []
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.html'):
            caminho = os.path.join(pasta, arquivo)
            with open(caminho, 'r', encoding='utf-8') as f:
                htmls.append((arquivo, BeautifulSoup(f.read(), 'html.parser')))
    return htmls

# Função para buscar o item nos arquivos HTML
def buscar_item(nome_item, pasta='exemplos_cwi'):
    resultados = []

    nome_item = unidecode(nome_item.lower())
    htmls = carregar_htmls(pasta)

    for nome_arquivo, soup in htmls:
        componentes = soup.select('#component-parts .assembly, #component-parts .procedure')
        for componente in componentes:
            nome_componente = componente.text.strip()
            nome_componente_processado = unidecode(nome_componente.lower())

            if nome_item in nome_componente_processado:
                resultados.append({
                    'arquivo': nome_arquivo,
                    'nome_encontrado': nome_componente
                })

    return resultados

# NOVO: Função para salvar o relatório
def salvar_relatorio(erros, pasta_relatórios='relatorios'):
    os.makedirs(pasta_relatórios, exist_ok=True)

    agora = datetime.now()
    timestamp = agora.strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"relatorio_erros_{timestamp}.txt"
    caminho_completo = os.path.join(pasta_relatórios, nome_arquivo)

    with open(caminho_completo, 'w', encoding='utf-8') as f:
        if erros:
            f.write("Relatório de Erros Encontrados:\n\n")
            for erro in erros:
                f.write(f"- {erro}\n")
        else:
            f.write("Nenhum erro encontrado!\n")

    print(f"Relatório salvo como '{caminho_completo}'")
    return nome_arquivo
