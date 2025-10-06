from validaciones import solo_letras, solo_enteros

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


###############################################
def calcular_promedio_materias(calificaciones:list) -> list:
    """
    Recibe las calificaciones y calcula el promedio por materia. 

    Args:
        calificaciones (list): Matriz con calificaciones. 

    Returns:
        list: Lista con promedio calculado por materia. 
    """
    suma_nota_materia = [0] * len(calificaciones[0])
    promedio_materia = [0] * len(calificaciones[0])

    for i in range(len(calificaciones)):
        for j in range(len(calificaciones[i])):
            suma_nota_materia[j] += calificaciones[i][j]
        
    for i in range(len(suma_nota_materia)):
        promedio_materia[i] = (suma_nota_materia[i] / len(calificaciones))
    
    return promedio_materia

def ordenar_mostrar_promedio_materias(calificaciones:list):
    
    promedio_materias = calcular_promedio_materias(calificaciones)
    p = len(promedio_materias)
    
    nombre_materias = [0] * p

    for i in range(p):
        nombre_materias[i] = (i + 1)
    
    for i in range(p):
        for j in range(0,p - i -1):
            if promedio_materias[j] < promedio_materias[j + 1]: 
                #Swap de promedio
                aux = promedio_materias[j] 
                promedio_materias[j] = promedio_materias[j+1]
                promedio_materias[j+1] = aux

                #Swap de nombre materia
                aux = nombre_materias[j] 
                nombre_materias[j] = nombre_materias[j+1]
                nombre_materias[j+1] = aux

    cantidad_a_mostrar = input("1) Mostrar todas las materias. \n2) Solo la materia con el promedio más alto. \nSeleccione qué desea mostrar: ")
    validar_respuesta = solo_enteros(cantidad_a_mostrar)

    while validar_respuesta == False or (cantidad_a_mostrar != "1" and cantidad_a_mostrar != "2"):
        cantidad_a_mostrar = input("Seleccione 1 o 2 para continuar. \n1) Mostrar todas las materias. \n2) Solo la materia con el promedio más alto. \nSeleccione qué desea mostrar: ")
        validar_respuesta = solo_enteros(cantidad_a_mostrar)

    if cantidad_a_mostrar == "1":
        for i in range(p):
            print(f"Promedio Materia_{nombre_materias[i]}= {promedio_materias[i]}")
    else:
        for i in range(p):
            print(f"Promedio Materia_{nombre_materias[i]}= {promedio_materias[i]}")
            break







