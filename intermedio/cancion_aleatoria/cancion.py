#!/usr/bin/env python
import sys
import random
"""
    lee archivo con n cantidad de caciones
    cada canción esta en una nueva linea
"""


def random_song(file):
    songs = open(file, "r")
    # Usamos una lista
    lista = list(songs)
    # Se obtiene una cación aleatoría
    aleatoria = random.choice(lista)
    return "Debes escuchar ahora: {r}".format(r=aleatoria)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file = sys.argv[1]
        print(random_song(file))
    else:
        print("Se requiere que escriba la ruta y nombre de archivo ")
