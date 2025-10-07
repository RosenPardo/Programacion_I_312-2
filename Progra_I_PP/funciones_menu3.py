#Creación e inicialización una matriz:
def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas  

        matriz += [fila]

    return matriz

# Carga y muestra promedios:
def calcular_promedio(calificaciones: list, estado_legajo:list):
    promedio_estudiantes = [0] * len(estado_legajo)
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

        promedio_estudiantes[i] = suma_notas / 5
    
    return promedio_estudiantes


def mostrar_promedios(calificaciones: list, estado_legajo:list, legajo_estudiante: list, nombre_estudiante: list, genero_estudiante: list) -> None:
    """
    Función que calcula e imprime lo que se encuentra cargado los arrays compartidos, de forma ordenada.

    Args:
        calificaciones (list): Array con notas de los estudiantes.
        estado_legajo (list): Array con el estado del legajo: 0 inactivo | 1 activo. Se utiliza para buscar encontrar datos de estudiantes.  
        legajo_estudiante (list): Array con número de legajo de estudiantes. 
        nombre_estudiante (list): Array con nombres de estudiantes.
        genero_estudiante (list): Array con géneros correspondientes a los estudiantes. 
    """
    promedio_estudiantes = calcular_promedio(calificaciones, estado_legajo)

    for j in range(len(promedio_estudiantes)):
        if estado_legajo[j] == 1:
            print(f"\nLejago: {legajo_estudiante[j]}")
            print(f"Nombre: {nombre_estudiante[j]}")
            print(f"Género estudiante: {genero_estudiante[j]}")
            print(f"Promedio notas: {promedio_estudiantes[j]}")
    
    return promedio_estudiantes
