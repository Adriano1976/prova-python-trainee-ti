""" Esse código Python verifica se duas strings são anagramas. Ele remove espaços e converte os caracteres para
letras minúsculas em ambas as strings. Em seguida, ele verifica se as versões ordenadas dessas strings são iguais. Se
forem iguais, o código imprime que as strings são anagramas; caso contrário, imprime que elas não são anagramas. No
exemplo fornecido, a primeira chamada retorna verdadeiro, pois "Listen" e "Silent" são anagramas; a segunda chamada
retorna verdadeiro após a remoção dos espaços, e a terceira chamada retorna falso, pois "Hello" e "World" não são
anagramas."""


def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if sorted(str1) == sorted(str2):
        print(f'A String "{str1}" é um anagrama de "{str2}"')
        return True
    else:
        print(f'A String "{str1}" NÃO é um anagrama de "{str2}"')
        return False


if __name__ == '__main__':
    is_anagram("Listen", "Silent")
    is_anagram("Anagram", "Nag a ram")
    is_anagram("Hello", "World")
