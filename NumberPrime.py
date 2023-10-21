"""
 Esse código em Python verifica se um número é primo ou não. Ele começa tratando os casos
 especiais em que o número é menor ou igual a 1, retornando "não é primo." Em seguida, ele
 verifica se o número é 2 ou 3, considerando-os primos. Caso contrário, ele executa um loop
 para verificar divisibilidade por todos os números a partir de 5 até a raiz quadrada do
 número em questão, pulando de 6 em 6 (otimização). Se encontrar um divisor, retorna "não é
 primo." Se não encontrar nenhum divisor, retorna "é primo." O código é testado com os
 números 7 e 4 no final, retornando True e False, respectivamente.
 """


def is_prime(n):
    if n <= 1:
        print(f'O número {n} não é primo')
        return False
    elif n <= 3:
        print(f'O número {n} é primo')
        return True
    elif n % 2 == 0 or n % 3 == 0:
        print(f'O número {n} não é primo')
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            print(f'O número {n} não é primo')
            return False
        i += 6
    print(f'O número {n} é primo')
    return True


if __name__ == '__main__':
    print(is_prime(7))  # Retorna: True
    print(is_prime(4))  # Retorna: False

