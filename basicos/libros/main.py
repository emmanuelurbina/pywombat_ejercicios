#!usr/bin/env python

libros = [
    'Don Quijote de la Mancha',
    'Historia de dos ciudades',
    'El Señor de los Anillos',
    'El principito',
    'El hobbit',
    'Sueño en el pabellón rojo',
    'Las aventuras de Alicia en el país de las maravillas',
    'Triple representatividad,',
    'Y no quedó ninguno (Diez negritos)',
    'El león, la bruja y el armario'
]


def listar(books):
    i = 0
    for book in books:
        i += 1
        print(f"{i} {book}")


def show_book(index):
    libros_len = len(libros)
    if index > libros_len or index <= 0:
        return "El número ingresado no esta en la lista"
    else:
        return libros[index-1]


def menu():
    try:
        listar(libros)
        response = int(input("Selecciona un libro: "))
    except:
        print("Solo se aceptan números")
    else:
        libro = show_book(response)
        print(libro)


if __name__ == "__main__":
    menu()
