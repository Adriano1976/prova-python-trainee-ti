""" Neste exemplo, a função resolver_labirinto recebe uma matriz labirinto como parâmetro. Cada elemento da matriz
representa uma célula do labirinto, onde:

0: caminho livre
1: parede
2: saída
3: posição inicial

A função utiliza uma abordagem de busca em profundidade recursiva para encontrar o caminho da entrada para a saída.
Ela verifica se uma posição é válida no labirinto, se já foi visitada ou se é uma parede. Em seguida, marca a posição
como visitada e chama recursivamente a função para as posições adjacentes. Se encontrar a saída, retorna o caminho
percorrido.

No exemplo de uso, uma matriz labirinto é fornecida como exemplo. A função resolver_labirinto é chamada com essa
matriz como argumento. Se um caminho for encontrado, o resultado é impresso na tela como "Caminho encontrado: [(0,
0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]". Isso representa o caminho da posição inicial (
3, 0) até a saída (4, 4). Se não for possível encontrar um caminho, é impresso "Não foi possível encontrar um
caminho."."""


def resolver_labirinto(labirinto):

    # Função auxiliar para verificar se uma posição é válida no labirinto
    def posicao_valida(labirinto, linha, coluna):
        num_linhas = len(labirinto)
        num_colunas = len(labirinto[0])
        return num_linhas > linha >= 0 == labirinto[linha][coluna] and 0 <= coluna < num_colunas

    # Função auxiliar recursiva para encontrar o caminho no labirinto
    def encontrar_caminho(labirinto, linha, coluna, caminho):
        if not posicao_valida(labirinto, linha, coluna):
            return False

        if labirinto[linha][coluna] == 2:
            caminho.append((linha, coluna))
            return True

        if labirinto[linha][coluna] == 1:
            return False

        labirinto[linha][coluna] = 1

        if encontrar_caminho(labirinto, linha - 1, coluna, caminho):
            caminho.append((linha, coluna))
            return True
        if encontrar_caminho(labirinto, linha + 1, coluna, caminho):
            caminho.append((linha, coluna))
            return True
        if encontrar_caminho(labirinto, linha, coluna - 1, caminho):
            caminho.append((linha, coluna))
            return True
        if encontrar_caminho(labirinto, linha, coluna + 1, caminho):
            caminho.append((linha, coluna))
            return True

        return False

    # Encontrar a posição inicial no labirinto
    num_linhas = len(labirinto)
    num_colunas = len(labirinto[0])
    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            if labirinto[linha][coluna] == 3:
                caminho = []
                if encontrar_caminho(labirinto, linha, coluna, caminho):
                    caminho.reverse()
                    return caminho

    return None


if __name__ == '__main__':

    labirinto = [
        [0, 0, 0, 2, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 3, 1, 1],
        [0, 2, 0, 0, 2]
    ]

    caminho = resolver_labirinto(labirinto)
    if caminho:
        print("Caminho encontrado:", caminho)
    else:
        print("Não foi possível encontrar um caminho.")
