#!/usr/bin/python3
#
# programa que compara las edades de 2 usuarios y diga quien es mayor al otro, este programa tambien deve pregunrar el nombre de los
# usuarios y decir el nombre de cual de los dos usuarios es mayor menor o la misma edad

def main():
    user = str(input('Ingrese en nombre usuario: '))
    user_2 = str(input('Ingrese el nombre del segundo usuario: '))

    age_user = int(input('Ingrese la edad del usuario: '))
    age_user_2 = int(input('Ingrese la edad del segundo usuario: '))


    if age_user > age_user_2:
        print(f'La edad del usuario: {user} es mayor ala del usuario dos: {user_2}')
    elif age_user < age_user_2:
        print(f'La edad del usuario 2: {user_2} es mayor ala del user: {user}')
    else:
        print(f'La edad de: {user} y user 2: {user_2} son iguales')


if __name__=='__main__':
    main()


