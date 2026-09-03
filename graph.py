
class GrafoListaAdjacencia():

    def __init__(self):
        # dicionario do grafo
        self.grafo = {}
        self.horas_materia = {}

    def adicionar_vertice(self, materia, horas):
        # se ainda nao existe no dicionario do grafo
        if materia not in self.grafo:
            self.grafo[materia] = []
            self.horas_materia[materia] = horas

    def adicionar_aresta(self, origem, destino, horas):
        # garantir que as duas matérias existam no dicionario do grafo
        self.adicionar_vertice(origem, horas)
        self.adicionar_vertice(destino, horas)

        # criando a direção do grafo
        if destino not in self.grafo[origem]:
            self.grafo[origem].append(destino)

    def remover_aresta(self,materia):
        if materia in self.grafo:
            if materia in self.horas_materia:
                del self.horas_materia[materia]
            for vertice in self.grafo:
                self.grafo[vertice] = [
                    req for req in self.grafo[vertice] if req != materia
                ]
            del self.grafo[materia]

    def exibir(self):
        for materia, vizinhos in self.grafo.items():
            print(f"matéria: {materia} libera -> {vizinhos}")

# # # ALGORITMO DE ORDENAÇÃO
    # dicionario pro grau de entrada do grafo
    def ordenacao_topologica(self, limite_horas):
        # cria o dicionario e adiciona todas as matérias como grau zero
        grau_entrada = {materia: 0 for materia in self.grafo}

        for materia, vizinhos in self.grafo.items():
            for destino in vizinhos:
                # pega cada materia da lista de vizinhos e adiciona um grau nele
                grau_entrada[destino] += 1

        # colocar numa fila as matérias com grau de entrada == 0
        disponiveis = [materia for materia in self.grafo if grau_entrada[materia] == 0]
        
        semestre = []

        while disponiveis:
            horas_semestre_atual = 0
            materias_semestre = []
            proximos_disponiveis = []

            # vai pegando as materias disponiveis para serem cursadas e vai calculando as horas
            for materia in disponiveis:
                horas = self.horas_materia[materia]

                if horas_semestre_atual + horas <= limite_horas:
                    materias_semestre.append(materia)
                    horas_semestre_atual += horas
                else:
                    proximos_disponiveis.append(materia)

            for materia_cursada in materias_semestre:
                for vizinhos in self.grafo[materia_cursada]:
                    grau_entrada[vizinhos] -= 1
                    if grau_entrada[vizinhos] == 0:
                        proximos_disponiveis.append(vizinhos)
        
            semestre.append(materias_semestre)
            disponiveis = proximos_disponiveis

        if sum(grau_entrada.values()) > 0:
            return False # Erro: o fluxograma possui um ciclo de dependencia.

        return semestre