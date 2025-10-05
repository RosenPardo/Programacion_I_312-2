
#Impresión de matriz:
"""def recorrer_matriz(mi_matriz):
    for i in range(len(mi_matriz)): # 0 1
        for j in range(len(mi_matriz[i])): #i = 0 entonces j = 0, 1, 2, 3 cuando i = 1 entonces j = 0, 1, 2, 3
            print(mi_matriz[i][j], end= " ")
        print("")"""

#Otra forma de imprimir matriz:
"""def recorrer_matriz_2(mi_matriz):
    for i in range(len(mi_matriz)): # 0 1
        for j in range(len(mi_matriz[i])):
            if len(mi_matriz)-1 == i and len(mi_matriz[i])-1 == j:
                print(mi_matriz[i][j])
            else:
                print(mi_matriz[i][j], end = " | ")
"""

#Carga de valores a una lista:
def cargar_lista_str(lista:list, mensaje_dato:str = "Ingrese el str a cargar: ") -> None:
    """
    Carga de valores a una lista inicializada de forma aleatoria, indicando el valor a incorporar y su ubicación en la lista

    Args:
        Lista (list): Lista a cargar.
    """
    primer_carga = False
    for i in range(len(lista)):

        if lista[i] == 0 and primer_carga == False:
            dato = input(mensaje_dato)
            validar_dato = solo_letras(dato)

            if validar_dato:
                lista[i] = dato
                primer_carga = True
            else:
                print("El dato ingresado no es válido.")
                return None
        else:
            break

#Carga secuencial de matriz:
def cargar_matriz_secuancialmente(matriz:list):
    # Agregar las validaciones / retorno que sean necesarias
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Fila {i} Columna {j}: "))

#Cómo hacer una BUSQUEDA EN MATRICES
def buscar_valor_entero(matriz:list, valor:int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f"Se encontró el valor {valor} en la fila {i}, columna {j}.")

#Mostrar lista:
def mostrar_lista(lista:list) -> None:
    for i in range(len(lista)):
        print(lista[i], end= " ")
