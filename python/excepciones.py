#!/usr/bin/python3

def divide_elemento_lista(lista, div):
    try:
        return [i / div for i in lista]

    except ZeroDivisionError as e:
        print(e)
        return lista


lista = list(range(20))
div = 0

print(divide_elemento_lista(lista, div))


