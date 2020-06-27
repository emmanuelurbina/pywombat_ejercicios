from random2 import randint

numeros = []

for i in range(50):
    numeros.append(randint(0, 101))

for numero in numeros:
    if numero % 2 == 0 and numero > 50:
        print(numero)
