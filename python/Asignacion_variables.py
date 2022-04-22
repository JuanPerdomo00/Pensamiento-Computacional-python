#!/usr/bin/python3
##############################################################################################################################################
# Asignacion de variables en python
#
# Las variables son simplemente nombres que se vimvulam con un valor en memoria con el operador de asignacion
#
# Caso 1
a = 2
x = 4
z = (a * x) / 2

# asignando las variables con esos nombres es muy dificil entender que es lo que esto hace
# por lo que los programadores novatos como yo aveces nos tiramos el codigo poniendo nombre de variables sin sentido
# hay es cuando entran los desarrolladores senior a solucionar.
#
# Caso 2
base = 2 # a
altura = 4 # x
area = (base * altura) / 2 # z
#
# Ahora es mas conprensible lo que estamos haciendo. Calcular el area del triangulo, ya somos desarrolladores de software senior
# ok no jsjsjs, pero estamos serca de lograrlo
#
# Pasamos de un programa de no entender lo que significaba como el caso 1, a un programa que podemos leer rapida mente como el caso 2.
# Las variables deben tener nombres expresivos que los humanos entiendan de manera arapida.
##############################################################################################################################################
#
# Podemos reasignar el valor de una variable
#
# simplemente estamos cambiando a donde apunta en memoria
#
mi_var = "Hola Mundo"
# >>> Hola Mundo
#
# Reacignamos el valor a 3
mi_var = 5
# >>> 5
# EL nombre de la variable sigue siendo el mismo, pero esta apuntando a diferentes posiciones de memoria
#                               ==================================================
#                               =   0x0001              =     "Hola Mundo"       =
# mi_var                        ==================================================
#                               =   0x0002              =      5                 =                                                           
#                               ==================================================
#
##############################################################################################################################################
