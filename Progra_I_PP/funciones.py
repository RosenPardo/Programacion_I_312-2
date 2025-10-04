def solo_enteros(cadena:str) -> bool:
    """Verifica si una cadena representa un número entero válido (positivo o negativo)

    Args:
        cadena (str): Cadena a verificar.

    Returns:
        bool: True si es una cadena de Int | False si no es solamente de enteros
    """
    
    if len(cadena) == 1: #Corroborar que si es el largo de la cadena es 1, que no sea un signo menos
        if ord(cadena) == 32:
            son_enteros = False
            return son_enteros

    for i in range(len(cadena)):
        if (ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57) or (ord(cadena[i]) == 45) or (ord(cadena[i]) == 32):
            son_enteros = True
        else:
            son_enteros = False
            break

    return son_enteros

#Imprimir matriz:
def recorrer_matriz(mi_matriz):
    for i in range(len(mi_matriz)): # 0 1
        for j in range(len(mi_matriz[i])): #i = 0 entonces j = 0, 1, 2, 3 cuando i = 1 entonces j = 0, 1, 2, 3
            print(mi_matriz[i][j], end= " ")
        print("")


#Otra forma de imprimir matriz:
def recorrer_matriz_2(mi_matriz):
    for i in range(len(mi_matriz)): # 0 1
        for j in range(len(mi_matriz[i])):
            if len(mi_matriz)-1 == i and len(mi_matriz[i])-1 == j:
                print(mi_matriz[i][j])
            else:
                print(mi_matriz[i][j], end = " | ")

#Carga de valores a una lista:
def cargar_lista(lista:list, mensaje_dato:str = "Ingrese el str a cargar: ") -> None:
    """
    Carga de valores a una lista inicializada de forma aleatoria, indicando el valor a incorporar y su ubicación en la lista

    Args:
        Lista (list): Lista a cargar.
    """
    seguir = "s"
    primer_carga = False
    for i in range(len(lista)):
        
        if primer_carga == True:
            seguir = input("¿Desea seguir cargando? s/n: ")

        if i == len(lista) - 1 or seguir != "s":
            break

        if lista[i] == 0:
            dato= input(mensaje_dato)
            lista[i] = dato
            primer_carga = True

#Cómo crear e inicializar una matriz en Python:
def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas  

        matriz += [fila]

    return matriz


#Cómo hacer una función que tenga CARGA SECUENCIAL:
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


