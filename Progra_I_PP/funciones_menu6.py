from validaciones import solo_enteros
from funciones_menu3 import calcular_promedio


def buscar_estudiante(legajo_estudiante: list, nombre_estudiante: list, genero_estudiante: list, estado_legajo: list, calificaciones: list) -> None:
    """
    Función que busca los datos de un estudiante, por el número de legajo indicado. 

    Args:
        legajo_estudiante (list): Array donde se buscará el valor indicado. 
        nombre_estudiante (list): Array con nombre de los estudiantes.
        genero_estudiante (list): Array con género de los estudiantes. 
        estado_legajo (list): Indica si el legajo se encuentra activo o inactivo. 
        calificaciones (list): Información con las notas de los estudiantes. 
    """
    promedio_estudiantes = calcular_promedio(calificaciones, estado_legajo)

    legajo_a_buscar = input("Ingrese el legajo que desea buscar: ")
    validar_int = solo_enteros(legajo_a_buscar)

    while validar_int == False or len(legajo_a_buscar) != 6:
        legajo_a_buscar = input("Ingresó un valor erróneo. Ingrese el legajo que desea buscar: ")
        validar_int = solo_enteros(legajo_a_buscar)

    for i in range(len(legajo_estudiante)):
        if int(legajo_a_buscar) == legajo_estudiante[i]:
            print(f"\nLejago: {legajo_estudiante[i]}")
            print(f"Nombre: {nombre_estudiante[i]}")
            print(f"Género estudiante: {genero_estudiante[i]}")
            print(f"Promedio general: {promedio_estudiantes[i]}")
            for j in range(len(calificaciones[i])): 
                print(f"Nota Materia_{j+1}: {calificaciones[i][j]}")
            return None
        
    print("No se encontró el legajo indicado. ")

