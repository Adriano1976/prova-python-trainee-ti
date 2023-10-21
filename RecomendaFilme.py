""" Neste exemplo, a função recomendar_filme recebe um dicionário de avaliações como parâmetro. Cada chave do
dicionário representa o nome de um filme e o valor associado é uma lista de avaliações feitas pelos usuários para
esse filme.

A função percorre todas as avaliações e calcula a média de cada filme. Em seguida, compara a média com a maior
avaliação média encontrada até o momento. Se a média for maior, atualiza a maior avaliação média e o filme recomendado.

No exemplo de uso, um dicionário avaliacoes é fornecido como exemplo, com avaliações para quatro filmes. A função
recomendar_filme é chamada com esse dicionário como argumento, e o resultado é impresso na tela como "Filme
recomendado: Filme 3". Isso significa que o filme "Filme 3" possui a maior avaliação média entre todos os filmes
avaliados."""


def recomendar_filme(avaliacoes):
    maior_avaliacao_media = 0
    filme_recomendado = ""

    for filme, avaliacoes_filme in avaliacoes.items():
        soma_avaliacoes = sum(avaliacoes_filme)
        media_avaliacoes = soma_avaliacoes / len(avaliacoes_filme)

        if media_avaliacoes > maior_avaliacao_media:
            maior_avaliacao_media = media_avaliacoes
            filme_recomendado = filme

    return filme_recomendado


if __name__ == '__main__':
    # Exemplo de uso
    avaliacoes = {
        "Filme 1": [4, 5, 3, 4, 5],
        "Filme 2": [3, 2, 4, 3, 5],
        "Filme 3": [5, 5, 5, 4, 5],
        "Filme 4": [2, 3, 1, 2, 3]
    }

    filme_recomendado = recomendar_filme(avaliacoes)
    print("Filme recomendado:", filme_recomendado)
