lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def cuadrado(lista):
    res = list(map(lambda n: n**2, lista))
    return res


print(cuadrado(lista))
