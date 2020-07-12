#!usr/bin/env python

def hora_minuto(horas=0):
    if horas < 1 or horas > 100:
        print("Error no puede ingresar numeros menores a 0 o mayores a 100")
    else:
        print("Existen {result} minutos en {hora} hora(s).".format(
            result=horas * 60, hora=horas))


def main():
    try:
        horas = int(input("Ingrese una cantidad de horas: "))
    except:
        print("Solo números enteros")
    else:
        hora_minuto(horas)


if __name__ == "__main__":
    main()
