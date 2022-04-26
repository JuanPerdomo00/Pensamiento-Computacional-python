#!/usr/bin/python3

# recursividad

def factorial(n):
    """Ayar el factorial de n
    
    formula: n! = n.(n - 1)!
    
    n int > 0

    return n! 
    """
    print(n)

    if n == 1:
        return 1

    return n * factorial(n - 1)


n = int(input('Escribe un numero entero: '))
print(factorial(n))
