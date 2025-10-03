#Ejercicio 1)
#Hacer una funcion que reciba como parametros un vector y un dato a buscar (int), y la misma retorne el indice del elemento encontrado.funcion que reciba una lista y que, ademas de la lista, reciba lo que se busca. Que retorne el indice de lo encontrado. En caso de no encontrarse, retornar el valor -1.

def buscador_en_lista(lista: list, elemento: int) -> int:
    """
    Función que busca en la lista un elemento. 

    Args:
        lista (list): Lista donde se buscará el elemento. 
        elemento (int): Elemento a buscar en la lista. 

    Returns:
        int: Indice de la lista donde se encontró el elemento, o indice -1 en caso de no encontrarlo. 
    """
    valor_encontrado = -1

    for i in range(len(lista)):
        if lista[i] == elemento:
            valor_encontrado = i
            break
    
    return valor_encontrado

lista_test = [2, 1, 0, 5, 7]

