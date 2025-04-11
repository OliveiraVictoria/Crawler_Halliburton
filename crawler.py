from validacoes import carregar_html, coletar_componentes, coletar_procedures, coletar_definition_objects, validar_componentes, validar_procedures
from datetime import datetime
import os

def analisar_cwi(caminho_html):
    soup = carregar_html(caminho_html)

    componentes = coletar_componentes(soup)
    procedures = coletar_procedures(soup)
    definition_objects = coletar_definition_objects(soup)

    erros = []
    erros += validar_componentes(componentes, definition_objects)
    erros += validar_procedures(procedures, definition_objects)

    return erros

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
    return nome_arquivo  # <-- Retorna só o nome do arquivo



if __name__ == "__main__":
    caminho = os.path.join('exemplos_html', 'exemplo1.html')  # caminho correto para o arquivo HTML

    erros_encontrados = analisar_cwi(caminho)

    if erros_encontrados:
        print("Erros encontrados:")
        for erro in erros_encontrados:
            print(f"- {erro}")
    else:
        print("Nenhum erro encontrado!")

    salvar_relatorio(erros_encontrados)
    # Aqui você pode adicionar mais chamadas para analisar outros arquivos HTML, se necessário.
    