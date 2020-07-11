#!/usr/bin/env python
import collections


def elemento_repetido(lista=[]):
    """
        Genera una diccionario con el elemento y su numero de veces
        repetido, se busca cual se repite mas
        retorna el elemento repetido
    """
    if len(lista) == 0:
        return "No hay elementos"
    elementos = collections.Counter(lista).items()
    mem_val = 0
    elemento_mayor = ()
    for el in elementos:
        if mem_val < el[1]:
            mem_val = el[1]
            elemento_mayor = el
    if elemento_mayor[1] != 1:
        return f"El número que más se repite es: {elemento_mayor[0]} con un total de: {elemento_mayor[1]} veces"
    else:
        return "Todos los elementos son únicos en tu lista"


def genera_lista(longitud):
    """
        Genera una lista de números enteros
        asignados por usuario
        retorna la lista
    """
    lista = []
    try:
        for i in range(0, longitud):
            i += 1
            el = int(input(f"Ingresa el {i}º número: "))
            lista.append(el)

        return lista
    except:
        print("Solo se admiten numeros enteros")


def main():
    """
        Ingresa la longitud de la lista
    """
    try:
        longitud = int(input("Longitud de la lista: "))
    except:
        print("Solo se admiten numeros enteros")
    else:
        lista = genera_lista(longitud)
        result = elemento_repetido(lista)
        print(result)


if __name__ == "__main__":
    main()
