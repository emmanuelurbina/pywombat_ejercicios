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

if __name__ == "__main__":
    full_date = datetime.now()
    month = months.get(full_date.month)
    year = full_date.year
    day = full_date.day

    hour = full_date.hour
    if hour < 10:
        hour = f"0{full_date.hour}"

    minutes = full_date.minute
    if minutes < 10:
        minutes = f"0{full_date.minute}"

    print(
        f"La fecha actual es: {hour}:{minutes} del {day} de {month} del {year}")
