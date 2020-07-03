def fibonacci(n):
    """
        Metodo recursivo
        # para 34 toma 5 seg
    """
    if n == 1 or n == 2 or n < 1:
        return 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    return result


def fibonacci_2(n):
    """
        Funcion fibonacci usando el metodo
        de menor a mayor
        mejor rendimiento, en 34 el resultado es instantaneo
    """
    if n == 1 or n == 2 or n < 1:
        return 1
    seq = [None] * (n+1)
    seq[1] = 1
    seq[2] = 1
    for i in range(3, n + 1):
        seq[i] = seq[i-1] + seq[i-2]
    return seq[n]


print(fibonacci(34))
