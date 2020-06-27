"""
    Programa que calcula el area
    de un triagulo con los valores
    ingresados por el usuario
"""

# Formula a usar (b * a )/ 2


def formating(fn):
    """
        Usamos un decorador para imprimir
        el resultado.
    """
    def new_area_triangulo(b, a):
        print("El área es: {}".format(fn(b, a)))
    return new_area_triangulo

# Decoramos la función


@formating
def area_triangulo(b=0, a=0):
    res = (b * a) / 2
    return res


# Función donde se interactua con el usuario


def calulo():
    try:
        base = float(input("Ingrese base: "))
        altura = float(input("Ingrese altura: "))
        area = area_triangulo
        area(base, altura)
    except:
        print("Solo se aceptan numeros")


if __name__ == "__main__":
    calulo()
