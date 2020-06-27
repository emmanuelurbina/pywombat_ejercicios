"""
    Lista de pares 1 a 100
"""


def pares(min=0, max=0):
    """
        Valida que sea número entero
        si no, a min se le da el valor a 1
    """
    if min <= 0:
        min = 1
   # Bucle para recorrer el rango de numeros
    for i in range(min, max + 1):
        # Si el residuo del numero entre 2 es 0 es par
        if i % 2 == 0:
            print(i)


if __name__ == "__main__":
    min = 0
    max = 10
    pares(min, max)
