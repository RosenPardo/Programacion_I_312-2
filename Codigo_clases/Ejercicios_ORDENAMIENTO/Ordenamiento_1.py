
# Crear una función llamada ordenar_array que reciba como parámetro un array de números enteros y lo ordene de forma ascendente. La función debe implementar como algoritmo de ordenamiento el método de la burbuja. Además, como parámetro opcional debe recibir un booleano (que por default está en False), que en caso de ser True ordena el vector en forma descendente.

def mostrar_lista(lista):
    for i in range(len(lista)):
        print(lista[i], end= " ")



def ordenar_array(lista: list, orden_descendente: bool = False) -> list:
    """
    Ordena de forma ascendente el array.

    Args:
        lista (list): Array de números enteros a ordenar.
        orden_descendente (bool, optional): En caso de ser True, ordena el vector de forma descendente. Defaults to False.

    Returns:
        list: Array ordenado. 
    """

    for i in range(len(lista)):
        for j in range(len(lista)):
            if orden_descendente == False:
                if  lista[i] < lista[j]:
                    lista[i], lista[j] = lista[j], lista[i]
            else:
                if  lista[i] > lista[j]:
                    lista[i], lista[j] = lista[j], lista[i]

    return lista



lista_test = [4, 1, 3, 5, 2]

mostrar_lista(lista_test)
print()

lista_ordenada = ordenar_array(lista_test)

mostrar_lista(lista_ordenada)