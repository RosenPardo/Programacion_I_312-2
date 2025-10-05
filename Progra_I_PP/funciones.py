from validaciones import *

#Impresión de matriz:
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

#Creación e inicialización una matriz:
def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas  

        matriz += [fila]

    return matriz

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

def legajo_duplicado(legajo_estudiante, num_legajo):
    for i in range(len(legajo_estudiante)):
        if legajo_estudiante[i] == int(num_legajo):
            print("El número de legajo ya existe. ")
            return True
    
    return False

def cargar_datos(legajo_estudiante, nombre_estudiante, genero_estudiante, estado_legajo):
    for i in range(len(legajo_estudiante)):

        if estado_legajo[i] == 0:
            #Carga legajo:
            num_legajo = input("Ingrese el número de legajo que desea cargar: ")
            validar_int = solo_enteros(num_legajo)
            validar_duplicado = legajo_duplicado(legajo_estudiante, num_legajo)

            while validar_int == False or len(num_legajo) != 6 or validar_duplicado == True:
                num_legajo = input("Ingresó un valor erróneo. Ingrese el número de legajo que desea cargar: ")
                validar_int = solo_enteros(num_legajo)
                validar_duplicado = legajo_duplicado(legajo_estudiante, num_legajo)
                
            

            legajo_estudiante[i] = int(num_legajo)

            #Carga de nombre:
            nombre = input("Ingrese el nombre del estudiante que desea cargar: ")
            validar_str = solo_letras(nombre)
            
            while validar_str == False:
                nombre = input("Ingresó un valor erróneo. Ingrese el nombre del estudiante que desea cargar: ")
                validar_str = solo_letras(nombre)
            
            nombre_estudiante[i] = nombre

            #Carga de género:
            genero = input("Ingrese el género del estudiante que desea cargar ('F' | 'M' | 'X'): ")
            validar_gen = validar_genero(genero)
            
            while validar_gen == False:
                genero = input("Ingresó un valor erróneo. Ingrese el género del estudiante que desea cargar ('F' | 'M' | 'X'): ")
                validar_gen = validar_genero(genero)
            
            genero = capitalizar_texto(genero)
            genero_estudiante[i] = genero
            estado_legajo[i] = 1

            print("\n Estudiante cargado correctamente. \n")

    return True

def mostrar_datos_cargados(calificaciones: list, legajo_estudiante: list, nombre_estudiante: list, genero_estudiante: list) -> None:
    """
    Función que imprime lo que se encuentra cargado en la matriz y arrays compartidos.

    Args:
        calificaciones (list): Matriz con calificaciones.
        legajo_estudiante (list): Array con número de legajo de estudiantes. 
        nombre_estudiante (list): Array con nombres de estudiantes.
        genero_estudiante (list): Array con géneros correspondientes a los estudiantes. 
    """
    for i in range(len(calificaciones)):
        print(f"\nLejago: {legajo_estudiante[i]}")
        print(f"Nombre: {nombre_estudiante[i]}")
        print(f"Género estudiante: {genero_estudiante[i]}")

        for j in range(len(calificaciones[i])): 
            print(f"Nota Materia_{j+1}: {calificaciones[i][j]}")

def cargar_promedios(calificaciones, estado_legajo):
    promedio_estudiantes = inicializar_matriz(len(estado_legajo), 5, 0)
    suma_notas = 0
    q_estudiantes = 0
    contador_materias = 0

    for i in range(len(calificaciones)):
        if estado_legajo[i] == 1:
            q_estudiantes += 1

            for j in range(len(calificaciones[i])):
                if contador_materias == 5:
                    suma_notas = 0
                    contador_materias = 0
                contador_materias += 1
                suma_notas += calificaciones[i][j]
                print(f"q_estudiantes: {q_estudiantes}")
                print(f"Suma_notas: {suma_notas}")
        promedio_estudiantes[i] = suma_notas / 5

    return promedio_estudiantes

def mostrar_promedios(calificaciones, estado_legajo):
    notas_estudiantes = cargar_promedios(calificaciones, estado_legajo)
    suma_notas = 0
    q_estudiantes = 0
    for i in range(len(notas_estudiantes)):
        if estado_legajo[i] == 1:
            notas_estudiantes[i] = suma_notas
            q_estudiantes += 1
            for j in range(len(notas_estudiantes[i])):
                suma_notas += notas_estudiantes[i][j]
    print(f"Suma notas: {suma_notas}")
    promedio_final = suma_notas / q_estudiantes

    return promedio_final
