#!/usr/bin/python3

# enumeracion exhaustuva

def run():
    numero = int(input('Escoje un numero entero: '))
    resul = 0

    while resul**2 < numero:
        print(resul)
        resul += 1

    if resul**2 == numero:
        print(f'La raiz cuagrada de {numero} es {resul}')
    else:
        print(f'{numero} no tiene raiz cuadrada exacta')

if __name__ == '__main__':
    run()

