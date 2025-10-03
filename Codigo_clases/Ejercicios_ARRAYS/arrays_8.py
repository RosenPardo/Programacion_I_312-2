
'''8) Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:

Una lista de nombres (lista_nombres).
Un nombre a buscar en la lista (nombre_antiguo).
Un nombre de reemplazo (nombre_nuevo).

La función debe realizar las siguientes acciones:
Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
Retornar la cantidad total de reemplazos realizados.
'''

from funciones_utiles import *

def reemplazar_nombres(lista_nombres, nombre_antiguo, nombre_nuevo):
    contador_cambios = 0

    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
            contador_cambios += 1

    return contador_cambios

lista_de_nombres = ["Rosendo", "Francisco", "Hector", "Luís", "Francisco", "Rodrigo", "Francisco"]
mostrar_lista(lista_de_nombres)

print("Se reemplazaron", reemplazar_nombres(lista_de_nombres, "Francisco", "Rosendo"), "nombres.")

mostrar_lista(lista_de_nombres)