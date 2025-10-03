

# 5) Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

from funciones_utiles import *

def producto_lista(lista: list) -> int:

    for i in range(len(lista)):
        lista[i] = lista[i] ** lista[i]

    return lista


lista = [4, 2, 2, 4, 25]

mostrar_lista(producto_lista(lista))

