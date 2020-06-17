"""
    Promedio
    10 materias
"""


def promedio():
    total_materias = 10
    materias = []
    i = 0
    try:
        while i < total_materias:
            materias.append(float(input("Ingresa una calificación: ")))
            i += 1
        total = sum(materias)
        materias_total = len(materias)
        res = total / materias_total
        print("El promedio es: {}".format(res))
    except:
        print("Error solo números")


if __name__ == "__main__":
    promedio()
