""" Neste exemplo, a função contar_palavra recebe um texto e uma palavra como parâmetros. O texto é convertido para
letras minúsculas usando o método lower() para garantir que a comparação seja case-insensitive. A palavra também é
convertida para letras minúsculas.

O texto é dividido em palavras usando o método split(), que retorna uma lista de palavras. Em seguida,
a função percorre cada palavra do texto e verifica se é igual à palavra fornecida. Se for igual, incrementa o contador.

No exemplo de uso, um texto e uma palavra são fornecidos como exemplo. A função contar_palavra é chamada com esses
valores como argumentos, e o resultado é impresso na tela como "Número de ocorrências da palavra: 1". Isso significa
que a palavra "roeu" ocorre uma vez no texto fornecido."""


def contar_palavra(texto, palavra):
    texto = texto.lower()
    palavra = palavra.lower()
    contador = 0

    palavras_texto = texto.split()

    for palavra_texto in palavras_texto:
        if palavra_texto == palavra:
            contador += 1

    return contador


if __name__ == '__main__':

    # Exemplo de uso
    texto = "O rato roeu a roupa do rei de Roma"
    palavra = "roeu"
    ocorrencias = contar_palavra(texto, palavra)

    print(f"Número de ocorrências da palavra '{palavra}':", ocorrencias)
