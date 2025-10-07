#Mostrar todos los datos cargados. 
def mostrar_datos_cargados(calificaciones: list, legajo_estudiante: list, nombre_estudiante: list, genero_estudiante: list, estado_legajo:list) -> None:
    """
    Función que imprime lo que se encuentra cargado en la matriz y arrays compartidos.

    Args:
        calificaciones (list): Matriz con calificaciones.
        legajo_estudiante (list): Array con número de legajo de estudiantes. 
        nombre_estudiante (list): Array con nombres de estudiantes.
        genero_estudiante (list): Array con géneros correspondientes a los estudiantes. 
    """
    for i in range(len(calificaciones)):
        if estado_legajo[i] == 1:
            print(f"\nLegajo: {legajo_estudiante[i]}")
            print(f"Nombre: {nombre_estudiante[i]}")
            print(f"Género estudiante: {genero_estudiante[i]}")

            for j in range(len(calificaciones[i])): 
                print(f"Nota Materia_{j+1}: {calificaciones[i][j]}")
