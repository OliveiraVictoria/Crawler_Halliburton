from flask import Flask, render_template, request, send_from_directory
from crawler.crawler_cwi import buscar_item, salvar_relatorio
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultados = []
    termo = ''
    relatorio = None

    if request.method == 'POST':
        termo = request.form.get('termo')
        resultados = buscar_item(termo)

        # Gera o relatório e pega o nome dele
        relatorio = salvar_relatorio([item['nome_encontrado'] for item in resultados])

    return render_template('index.html', resultados=resultados, termo=termo, relatorio=relatorio)

# Nova rota para baixar o relatório
@app.route('/download/<nome_arquivo>')
def download(nome_arquivo):
    return send_from_directory('relatorios', nome_arquivo, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
