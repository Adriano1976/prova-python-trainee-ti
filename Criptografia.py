""" Neste exemplo, a função criptografar_cesar recebe uma mensagem e uma chave como parâmetros. A mensagem é
percorrida letra por letra. Se a letra for alfabética, a função verifica se é maiúscula ou minúscula e aplica a
fórmula da Cifra de César para obter a letra criptografada correspondente. A letra criptografada é concatenada à
mensagem criptografada final. Se a letra não for alfabética, ela é mantida na mensagem criptografada sem alterações.

No exemplo de uso, a mensagem "Adriano Santos" é criptografada usando uma chave de 3. O resultado é impresso na tela
como "Mensagem criptografada: Dguldqr Vdqwrv". Cada letra foi substituída por outra que está 3 posições à frente no
alfabeto."""


def criptografar_cesar(mensagem, chave):
    mensagem_criptografada = ""
    for letra in mensagem:
        if letra.isalpha():
            if letra.isupper():
                letra_criptografada = chr((ord(letra) - 65 + chave) % 26 + 65)
            else:
                letra_criptografada = chr((ord(letra) - 97 + chave) % 26 + 97)
            mensagem_criptografada += letra_criptografada
        else:
            mensagem_criptografada += letra
    return mensagem_criptografada


if __name__ == '__main__':

    # Exemplo de uso
    mensagem = "Adriano Santos"
    chave = 3
    mensagem_criptografada = criptografar_cesar(mensagem, chave)

    print("Mensagem criptografada:", mensagem_criptografada)
