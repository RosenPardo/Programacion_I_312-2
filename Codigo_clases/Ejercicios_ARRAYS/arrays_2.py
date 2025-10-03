from arrays_1 import *
from funciones_utiles import *

# 2) Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.


def cargar_lista(lista):
    
    for i in range(len(lista)):
        lista[i] += int(input("Ingrese el número que se alojará en la array: "))
    
    return lista

"""TEST de la función:
lista_creada = crear_array_int(5)

lista_cargada = cargar_lista(lista_creada)

mostrar_lista(lista_cargada)
"""