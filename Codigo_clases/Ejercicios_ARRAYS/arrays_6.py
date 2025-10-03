
# 6) Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
# Ejercicio de un compa: https://www.onlinegdb.com/lz92teE-92

from funciones_utiles import *

def val_maximo_lista(lista):
    primer_valor = True
    valor_maximo = None

    for i in range(len(lista)):
        if primer_valor:
            valor_maximo = lista[i]
            primer_valor = False

        elif lista[i] >= valor_maximo:
            valor_maximo = lista[i]



    return valor_maximo


lista = [2, 4, 65, 3, 1, 8]

print(val_maximo_lista(lista))