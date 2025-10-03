

# Array - arreglo - lista simple - vector
mi_vector = [1, 5, 6, 4]
#Para acceder al 5:
mi_vector[1] #5

#array - arreglo - lista compuesta - matriz
mi_matriz = [[2, 4, 5, 8], [6, 3, 1, 9]]
#para acceder al 2:

mi_matriz[0][0] #2
mi_matriz[0][1] #4
mi_matriz[0][2] #5



#Cómo recorrerla?:
def recorrer_matriz(mi_matriz):
    for i in range(len(mi_matriz)): # 0 1
        for j in range(len(mi_matriz[i])): #i = 0 entonces j = 0, 1, 2, 3 cuando i = 1 entonces j = 0, 1, 2, 3
            print(mi_matriz[i][j], end= " ")
        print("")

print("\n")
#otra forma de imprimir:

for i in range(len(mi_matriz)): # 0 1
    for j in range(len(mi_matriz[i])):
        if len(mi_matriz)-1 == i and len(mi_matriz[i])-1 == j:
            print(mi_matriz[i][j])
        else:
            print(mi_matriz[i][j], end = " | ")


#Print con cambio de signos: https://onlinegdb.com/bsSRAnkOm

print("\n")
#Cómo crear e inicializar una matriz en Python:

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas  

        matriz += [fila]

    return matriz

mi_matriz = inicializar_matriz(2, 4, 0)

recorrer_matriz(mi_matriz)

print("\n")
#Cómo hacer una función que tenga CARGA SECUENCIAL:

def cargar_matriz_secuancialmente(matriz:list):
    # Agregar las validaciones / retorno que sean necesarias
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Fila {i} Columna {j}: "))

print("\n")
#Cómo hacer CARGA ALEATORIA:

def cargar_matriz_aleatoriamente(matriz: list):
    """
    Carga de valores a una matriz inicializada de forma aleatoria, indicando el valor a incorporar y su ubicación en la matriz (fila y columna)

    Args:
        matriz (list): Matriz a cargar
    """
    #Agregar las validaciones/retorno que sean necesarias
    seguir = "s"
    cantidad_cargas = 0
    while seguir == "s" and cantidad_cargas <= len(matriz):
        fila= int(input("Indice de la fila: "))
        columna= int(input("Indice de la columna: "))
        dato= int(input("Ingrese el número a cargar: "))
        matriz[fila][columna] = dato
        cantidad_cargas += 1
        seguir = input("Desea seguir cargando? s/n: ")


cargar_matriz_aleatoriamente(mi_matriz)
recorrer_matriz(mi_matriz)


print("\n")
#Cómo hacer una BUSQUEDA EN MATRICES

def buscar_valor_entero(matriz:list, valor:int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f"Se encontró el valor {valor} en la fila {i}, columna {j}.")


