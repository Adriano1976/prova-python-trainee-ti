"""Palíndromo é uma palavra, frase ou número que permanece igual quando lida de trás para diante. Por extensão,
palíndromo é qualquer série de elementos com simetria linear, ou seja, que apresenta a mesma sequência de unidades
nos dois sentidos

Esse código Python define uma função chamada "is_palindrome" que verifica se uma dada string é um palíndromo.
Para fazer isso, primeiro remove os espaços e caracteres não alfanuméricos da string, transforma a string em letras
minúsculas e, em seguida, compara a string original com sua versão invertida. Se ambas forem iguais, a função retorna
verdadeiro, indicando que a string é um palíndromo; caso contrário, retorna falso, indicando que não é um palíndromo.
Em seguida, no bloco "if __name__ == '__main__':", a função é testada com uma string específica ("A man, a plan,
a canal: Panama"), e uma mensagem é impressa com base no resultado do teste, indicando se a string é ou não um
palíndromo."""


import re


def is_palindrome(string):
    # Remove espaços e caracteres não alfanuméricos da string
    string = re.sub(r'[^a-zA-Z0-9]', '', string)

    # Converte a string para letras minúsculas
    string = string.lower()

    # Verifica se a string é um palíndromo
    return string == string[::-1]


if __name__ == '__main__':

    string = "A man, a plan, a canal: Panama"
    if is_palindrome(string):
        print("A string é um palíndromo")
    else:
        print("A string não é um palíndromo")
