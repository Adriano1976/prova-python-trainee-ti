""" Neste exemplo, a classe `Grafo` representa o grafo ponderado. A função `adicionar_vertice` é usada para
adicionar vértices ao grafo, e a função `adicionar_aresta` é usada para adicionar arestas com
seus respectivos pesos.

A função `a_estrela` implementa o algoritmo A*. Ela recebe o grafo, o vértice de origem e o
vértice de destino como parâmetros. A função utiliza uma fila de prioridade para armazenar os
vértices a serem explorados, ordenados pelo custo atual. O custo atual é atualizado à medida
que o algoritmo avança.

A função `calcular_heuristica` é responsável por calcular a heurística para um determinado vértice.
Você precisa implementar essa função de acordo com o problema específico que está resolvendo.
A heurística é uma estimativa do custo restante para chegar ao destino.

No exemplo de uso, um grafo simples é criado com quatro vértices (A, B, C, D) e suas respectivas
arestas e pesos. O vértice de origem é 'A' e o vértice de destino é 'D'. O algoritmo A* é chamado
para encontrar o caminho mais curto entre a origem e o destino. O resultado é impresso na tela """


import heapq


class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        self.vertices[vertice] = {}

    def adicionar_aresta(self, vertice1, vertice2, peso):
        self.vertices[vertice1][vertice2] = peso
        self.vertices[vertice2][vertice1] = peso

    def obter_vizinhos(self, vertice):
        return self.vertices[vertice]

    def calcular_heuristica(self, vertice, destino):
        # Implemente a função de heurística aqui
        pass


def a_estrela(grafo, origem, destino):
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, origem))  # Adiciona a origem na fila de prioridade
    custo_atual = {origem: 0}  # Dicionário para armazenar o custo atual para cada vértice
    caminho_anterior = {}  # Dicionário para armazenar o caminho anterior para cada vértice

    while fila_prioridade:
        _, vertice_atual = heapq.heappop(fila_prioridade)  # Remove o vértice com menor custo da fila de prioridade

        if vertice_atual == destino:
            # Constrói o caminho a partir do destino até a origem
            caminho = []
            while vertice_atual in caminho_anterior:
                caminho.insert(0, vertice_atual)
                vertice_atual = caminho_anterior[vertice_atual]
            caminho.insert(0, origem)
            return caminho

        vizinhos = grafo.obter_vizinhos(vertice_atual)
        for vizinho in vizinhos:
            custo = custo_atual[vertice_atual] + vizinhos[vizinho]
            if vizinho not in custo_atual or custo < custo_atual[vizinho]:
                custo_atual[vizinho] = custo
                prioridade = custo + (grafo.calcular_heuristica(vizinho, destino) if grafo.calcular_heuristica(vizinho, destino) is not None else 0)

                heapq.heappush(fila_prioridade, (prioridade, vizinho))
                caminho_anterior[vizinho] = vertice_atual

    return None


if __name__ == '__main__':

    # Exemplo de uso
    grafo = Grafo()
    grafo.adicionar_vertice('A')
    grafo.adicionar_vertice('B')
    grafo.adicionar_vertice('C')
    grafo.adicionar_vertice('D')
    grafo.adicionar_aresta('A', 'B', 5)
    grafo.adicionar_aresta('A', 'C', 3)
    grafo.adicionar_aresta('B', 'D', 2)
    grafo.adicionar_aresta('C', 'D', 4)

    origem = 'A'
    destino = 'D'
    caminho = a_estrela(grafo, origem, destino)

    if caminho:
        print("Caminho mais curto:", caminho)
    else:
        print("Não foi possível encontrar um caminho do", origem, "para", destino)
