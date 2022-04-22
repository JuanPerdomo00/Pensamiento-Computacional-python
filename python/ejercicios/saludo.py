#!/usr/bin/python3


def main():
    nombre = str(input('Ingresa tu nombre: ')).replace(' ', '')

    saludo = f'Holo Como estas {nombre} :):'

    leng = len(nombre)
    

    print(f'{saludo} tienes {leng} letras en tu nombre')


if __name__=='__main__':
    main()
