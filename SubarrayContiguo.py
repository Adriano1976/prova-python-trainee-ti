""" Esse código Python implementa o algoritmo para encontrar a maior soma de uma sublista contígua em uma lista 'a'.
Ele itera pela lista, atualizando duas variáveis: 'max_so_far', que mantém o valor máximo encontrado até o momento,
e 'max_ending_here', que rastreia a maior soma da sublista que termina no índice atual. O algoritmo retorna
'max_so_far', que é a maior soma de sublista encontrada."""


def maxSubArraySum(a):
    max_so_far = max_ending_here = a[0]

    for i in range(1, len(a)):
        max_ending_here = max(a[i], max_ending_here + a[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


if __name__ == '__main__':
    print(maxSubArraySum([1, -3, 2, 1, -1]) == 3)
    print(maxSubArraySum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7)
    print(maxSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
    print(maxSubArraySum([5, 4, -1, 7, 8]) == 23)
    print(maxSubArraySum([-2, -3, -4, -1, -2, -1, -5, -3]) == -1)
