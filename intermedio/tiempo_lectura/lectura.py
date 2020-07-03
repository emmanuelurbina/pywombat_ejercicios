#!/usr/bin/env python

def reading_time(content):
    # contenido sin espacios en blanco en una lista
    list_content = content.split(' ')
    time_to_read = round(len(list_content) / 265)
    if time_to_read < 1:
        return "< 1 min."
    else:
        return f"{time_to_read} min."


print(reading_time("Hola, mundo!"))
