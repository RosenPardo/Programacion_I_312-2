
# 7) Escribir una función que reciba como parámetros una lista de enteros y MUESTRE la/las posiciones en donde se encuentra el valor máximo hallado.

from funciones_utiles import *

def val_maximo_lista(lista):
    primer_valor = True
    valor_maximo = None
    ubicacion_maximo = None

    for i in range(len(lista)):
        if primer_valor:
            print(i)
            valor_maximo = lista[i]
            ubicacion_maximo = i
            primer_valor = False

        elif lista[i] >= valor_maximo:
            valor_maximo = lista[i]
            ubicacion_maximo = i
            print(ubicacion_maximo)



lista = [22, 1, 65, 3, 88, 8]

val_maximo_lista(lista)