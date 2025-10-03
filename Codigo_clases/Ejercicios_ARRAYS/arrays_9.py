
''' 9) Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays. '''
from funciones_utiles import *

def interseccion_arrays(lista_uno, lista_dos):
    interseccion = []
    
    for i in range(len(lista_uno)):
        for j in range(len(lista_dos)):
            if lista_uno[i] == lista_dos[j]:
                print(lista_uno[i])

    return interseccion


lista_uno = ["a", "c", "b"]
lista_dos = ["g", "i", "l", "b"]

interseccion_arrays(lista_uno, lista_dos)


