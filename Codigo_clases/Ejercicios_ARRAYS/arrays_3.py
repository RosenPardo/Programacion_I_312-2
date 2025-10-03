from arrays_1 import *
from funciones_utiles import *

# 3) Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 


def promedio_lista(lista_ingresada):
    suma = 0

    for i in range(len(lista_ingresada)):
        suma += lista_ingresada[i]

    promedio = suma / len(lista_ingresada)

    return promedio
lista_uno = [1,2,3,3]

promedio_de_lista = promedio_lista(lista_uno)

print(promedio_de_lista)


#Ejemplo:

"""
def calcular_promedio_lista(lista:list) -> int:
    suma = 0
    for i in lista:
        suma += i
    promedio = suma / len(lista)
    return promedio
"""