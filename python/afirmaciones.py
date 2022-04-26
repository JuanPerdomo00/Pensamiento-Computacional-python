#!/usr/bin/python3

# assert <excepcion booleana>, <manejo errores>

def primera_letra(lista_palabras):
    primera_letras = []

    for palabra in lista_palabras:
        assert type(palabra) == str, f'{palabra} no es de tipo str'
        assert len(palabra) > 0, 'No se permiten str vacios'


        primera_letras.append(palabra[0])


    return primera_letras

lista = ['juan', 'pepe']

print(primera_letra(lista))
