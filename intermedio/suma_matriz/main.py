#!usr/bin/env python


def main():
    matriz = [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 200, 300],
    ]

    """
        Salida esperada
        La suma de las columnas es: 150 - 180 - 300 - 420
        La suma de las filas es: 100 - 260 - 690
    """

    fila_s = len(matriz)
    cols_s = len(matriz[0])
    suma_filas = []
    suma_cols = []
    separador = " - "

    for f in range(0, fila_s):
        suma_filas.append(f"{sum(matriz[f])}")

    for c in range(0, cols_s):
        suma_c = 0
        for i in range(0, fila_s):
            suma_c += matriz[i][c]
        suma_cols.append(f"{suma_c}")

    print("La suma de las filas es: {}".format(separador.join(suma_filas)))
    print("La suma de las columnas es: {}".format(separador.join(suma_cols)))


if __name__ == "__main__":
    main()
