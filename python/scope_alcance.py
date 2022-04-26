#!/usr/bin/python3


def saludar():
   # global mensaje
    mensaje = 'Hoola saludo 1'

    def saludar_2(mensaje):
        mensaje += ' mundo saludo 2'

        return print(mensaje)
    
    saludar_2(mensaje)
    return print(mensaje)

saludar()
