""" Este código em Python implementa a solução clássica do problema da Torre de Hanoi.
A função `TorreDeHanoi` recebe quatro parâmetros: o número de discos `n`, o pino de
origem `pino_origem`, o pino de destino `pino_destino` e o pino auxiliar `pino_auxiliar`.
A função usa a recursão para mover os discos da pino de origem para o pino de destino,
seguindo as regras do jogo. Quando `n` é igual a 1, ele move o disco do topo diretamente
para o pino de destino. Caso contrário, move `n-1` discos para o pino auxiliar, move o disco
maior para o pino de destino e, em seguida, move os discos do pino auxiliar para o pino
de destino. O código de teste demonstra a resolução do problema com 4 discos, usando os
pinos A, C e B. """


def TorreDeHanoi(n, pino_origem, pino_destino, pino_auxiliar):
    if n == 1:
        print("Mova o disco 1 do pino", pino_origem, "para o pino", pino_destino)
        return

    TorreDeHanoi(n - 1, pino_origem, pino_auxiliar, pino_destino)
    print("Mova o disco", n, "do pino", pino_origem, "para o pino", pino_destino)
    TorreDeHanoi(n - 1, pino_auxiliar, pino_destino, pino_origem)


if __name__ == '__main__':
    # Código de teste
    n = 4
    TorreDeHanoi(n, 'A', 'C', 'B')
    # A, C, B são os nomes dos pinos
