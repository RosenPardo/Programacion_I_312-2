from arrays_1 import *
from funciones_utiles import *

# 4) Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.


def promedio_lista_positivos(lista_ingresada):
    suma = 0
    cantidad_positivos = 0
    for i in range(len(lista_ingresada)):
        if lista_ingresada[i] > 0:
            suma += lista_ingresada[i]
            cantidad_positivos += 1

    
    promedio = suma / cantidad_positivos

    return promedio

lista_uno = [3,-2,3,3]

promedio_de_lista = promedio_lista_positivos(lista_uno)

print(promedio_de_lista)

