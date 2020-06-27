#!/usr/bin/env python
from datetime import datetime


months = {1: "Enero",
          2: "Febrero",
          3: "Marzo",
          4: "Abril",
          5: "Mayo",
          6: "Junio",
          7: "Julio",
          8: "Agosto",
          9: "Septiembre",
          10: "Octubre",
          11: "Noviembre",
          12: "Diciembre"}


def formato_fecha(fecha):

    month = months.get(fecha.month)
    year = fecha.year
    day = fecha.day

    hour = fecha.hour
    if hour < 10:
        hour = f"0{fecha.hour}"

    minutes = fecha.minute
    if minutes < 10:
        minutes = f"0{fecha.minute}"

    print(
        f"La fecha es: {day} de {month} del {year}")


if __name__ == "__main__":
    fecha = datetime(2020, 5, 7)
    formato_fecha(fecha)
