#!/usr/bin/env python
class ErrorRango(Exception):
    pass


def pares(n, m):
    try:
        if n < 0 or n > m:
            raise ErrorRango()
        else:
            for i in range(n, m):
                if i % 2 == 0:
                    print(i)

    except ErrorRango:
        print("No es posible continuar con la operación.")


pares(5, 10)
