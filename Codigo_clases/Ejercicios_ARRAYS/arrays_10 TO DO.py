
''' 10) Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la unión de los dos arrays.'''

def mostrar_union(lista_uno, lista_dos):
    union_arrays = []

    for i in range(len(lista_uno)):
        for j in range(len(lista_dos)):
            if lista_uno[i] == lista_dos[j]:
                union_arrays += [i]
                print(i)


lista_uno = ["j", "a", "c", "b", "f"]
lista_dos = ["g", "b", "l", "e", "h"]