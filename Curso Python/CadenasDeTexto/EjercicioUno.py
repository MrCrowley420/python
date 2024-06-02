#Ejercicio 1

#Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

#1 Imprima los dos primeros caracteres.

#2 Imprima los tres últimos caracteres.

#3 Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

#4 Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

#5 Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.#

cadena = 'Te quiero solo como amigo'

print(cadena[0 : 2])   #1   

print(cadena[-3 : ])    #2

print(cadena[: : 2])    #3

print(cadena[: : -1])   #4

print(cadena + cadena[: : -1])   #5