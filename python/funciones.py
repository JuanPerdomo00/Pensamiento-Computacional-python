#!/usr/bin/python3


def menu():
    print('='*50)
    print('\t[*] Sacar raiz cuadrada [*]')
    print('''
1. aproximacion
2. enumeracion exhausiva
3. busqueda binaria
          ''')
    print('='*50)
   

def aproximacion(n):
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - n) >= epsilon and respuesta <= n:
        print(abs(respuesta ** 2 - n), respuesta)
        respuesta += paso

    if abs(respuesta**2 - n) >= epsilon:
        print(f'No se encontro la raiz cuadrada {n}')

    else:
        print(f'La raiz cuadrada de {n} es {respuesta}')

    return n


def enumeracion_exhaustiva(n):
    resul = 0

    while resul**2 < n:
        resul += 1
 
    if resul**2 == n:
        print(f'La raiz cuagrada de {n} es {resul}')

    else:
        print(f'{n} no tiene raiz cuadrada exacta')
    
    return n


def busqueda_binaria(n):
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, n)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - n) >= epsilon:
        if respuesta**2 < n:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cadrada de {n} es {respuesta}')

    return n


def main():
    menu()
    opcion = int(input('Ingrese una opcion: '))
    if opcion == 1:
        n = int(input('Ingrese un numero: ')) 
        aproximacion(n)
    elif opcion == 2:
        n = int(input('Ingrese un numero: '))
        enumeracion_exhaustiva(n)
    elif opcion == 3:
        n = int(input('Ingrese un numero: '))
        busqueda_binaria(n)
    else:
        print("Ingrese un valor valido")
    


if __name__=='__main__':
    main()

