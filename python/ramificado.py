#/usr/bin/python3

def escoje(num: int, num_2: int) -> int:
    if num > num_2:
        print('El primer numero {num} es mayor que el segundo {num_2}')
    elif num < num_2:
        print(f'El segundo numero {num_2} es meyor que el primero {num}')

    else:
        print(f'Los dos numero {num} {num_2} son iguales')



def main() -> str:
    num = int(input('Ingrese un numero entero: '))
    num_2 = int(input('Ingrese otro numero entero: '))

    escoje(num, num_2)


if __name__=='__main__':
    main()
