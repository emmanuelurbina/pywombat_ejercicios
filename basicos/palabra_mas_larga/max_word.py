#!/usr/bin/env python


texto = "Esta es una prueba para conocer la palabra mas grande en una cadena de texto"


def max_word(texto=""):
    """
        Función que nos devuelve la primera palabra mas larga
        en un texto dado.
        Si hay 2 palabras del mismo tamaño, la primera es la que se
        toma en cuenta
    """
    # un recolector
    recolector = ""
    # un texto limpio
    texto.strip()
    # para hacerlo mas sencillo lo convertimos en una lista
    texto_lista = texto.split(" ")
    # comparamos cada elemento para ver cual es el mayor
    for palabra in texto_lista:
        if len(palabra) > len(recolector):
            recolector = palabra
    return recolector


result = max_word(texto)
print(f"La palabra mas larga del texto es: {result}")
