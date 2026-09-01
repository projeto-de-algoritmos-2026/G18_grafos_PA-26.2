import os
import json
from bottle import Bottle, run, template, static_file, TEMPLATE_PATH, request, redirect
from persistencia.persistencia import GerenciadorPersistencia
from graph import GrafoListaAdjacencia

app = Bottle()
base_path = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(base_path, 'views', 'html')
TEMPLATE_PATH.insert(0,html_path)

banco = GerenciadorPersistencia()
''' ARRUMAR PATH DE SALVAMENTO
graph = banco.carregar()
banco.salvar(graph)
'''

Algoritmo = GrafoListaAdjacencia()



# --- ROTAS BOTTLE --- #
@app.route('/css/<filepath:path>')
def server_css(filepath):
    css_path = os.path.join(base_path, 'views','css')
    return static_file(filepath, root=css_path)

@app.route('/')
def fluxo():
    return template('fluxograma.tpl',grafo=Algoritmo.grafo,horas=Algoritmo.horas_materia)

@app.route('/add', method='POST')
def adicionar_materia():
    form_materia = request.forms.get('materia').encode('iso-8859-1').decode('utf8').strip().upper()
    form_horas = int(request.forms.get('horas'))
    form_requisitos = request.forms.getall('requisitos')
    lista_requisitos = [req.encode('iso-8859-1').decode('utf8').strip() for req in form_requisitos if req.strip() != '']

    for mat in lista_requisitos:
        if mat not in Algoritmo.grafo:
            return template('fluxograma.tpl', grafo = Algoritmo.grafo, horas = Algoritmo.horas_materia, erro = 'Esta matéria de pré-requisito não foi adicionada antes. Adicione esta matéria na lista primeiramente')

    Algoritmo.adicionar_vertice(form_materia,form_horas)
    for req in lista_requisitos:
        Algoritmo.adicionar_aresta(req,form_materia, form_horas)
    print(Algoritmo.grafo)

    redirect('/')

@app.route('/exclude', method='POST')
def remover_materia():
    materia = request.forms.getunicode('materia_alvo')
    print(Algoritmo.grafo)
    redirect('/')

@app.route('/fluxograma',method='POST')
def calcular_fluxo():
    form_limite_horas = int(request.forms.get('lim_horas'))
    print(Algoritmo.ordenacao_topologica(360))

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)