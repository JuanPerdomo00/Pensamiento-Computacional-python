#!/usr/bin/python3
# Acá investigue los métodos de listas: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
#
# Los nuevos que encontré además de los de la clase:
#
#    lista.extend(iterable) #extiende la lista con valores dentro de un iterable como un range()
#    lista.insert(i, ‘valor’) #Agrega un valor en la posición i y recorre todos los demás. No borra nada.
#    lista.pop(i) #Elimina valor en la posición i de la lista.
#    lista.remove(‘valor’) #Elimina el primer elemento con ese valor.
#    lista.clear() #Borra elementos en la lista.
#    lista.index(‘valor’) #Retorna posición del primer elemento con el valor.
#    lista.index(‘valor’, start, end) #Retorna posición del elemento con el valor dentro de los elementos desde posición start hasta posición end)
#    lista.count(‘valor’) #Cuenta cuántas veces esta ese valor en la lista.
#    lista.sort() #Ordena los elementos de mayor a menor.
#    lista.sort(reverse = True) #Ordena los elementos de menor a mayor.
#    lista.reverse() #Invierte los elementos
#    lista.copy() #Genera una copia de la lista. También útil para clonar listas.


lista = list(range(101))

# dsacar pares

par = [i for i in lista if i % 2 == 0]
print(par)

