from validaciones import capitalizar_texto, solo_letras
from funciones_menu3 import calcular_promedio


#Pasaje por valor de listas para usar en ordenar_promedios().
def copiar_lista(lista:list) -> list:
    """
    Copia una lista por valor.

    Args:
        lista (list): Lista a copiar.

    Returns:
        list: Lista copiada por valor. 
    """
    lista_nueva = [0] * len(lista)
    for i in range(len(lista)):
        lista_nueva[i] = lista[i]
    
    return lista_nueva

#Para ordenar y mostrar estudiantes por promedio:
def ordenar_promedios(calificaciones: list, estado_legajo: list, legajo_estudiante: list, nombre_estudiante: list, genero_estudiante: list) -> None:
    """
    La función ordena y muestra a los estudiantes por promedio. 

    Args:
        calificaciones (list): Array con notas de los estudiantes.
        estado_legajo (list): Array con el estado del legajo: 0 inactivo | 1 activo. Se utiliza para buscar encontrar datos de estudiantes.  
        legajo_estudiante (list): Array con número de legajo de estudiantes. 
        nombre_estudiante (list): Array con nombres de estudiantes.
        genero_estudiante (list): Array con géneros correspondientes a los estudiantes. 
    """
    promedio_estudiantes = calcular_promedio(calificaciones, estado_legajo)
    
    ordenado_promedio = copiar_lista(promedio_estudiantes)
    ordenado_legajo = copiar_lista(legajo_estudiante)
    ordenado_nombre = copiar_lista(nombre_estudiante)
    ordenado_genero = copiar_lista(genero_estudiante)

    descendente = input("Desea mostrar de forma descendente? s|n: ")
    descendente = capitalizar_texto(descendente)
    validar_respuesta = solo_letras(descendente)

    while validar_respuesta == False or (descendente != "S" and descendente !="N"):
        descendente = input("Desea mostrar de forma descendente? s|n: ")
        descendente = capitalizar_texto(descendente)
        validar_respuesta = solo_letras(descendente)


    n = len(promedio_estudiantes) 
    if descendente == "S":
        for i in range(n):
            for j in range(0,n - i -1):
                if ordenado_promedio[j] < ordenado_promedio[j + 1]: 
                    #Swap de promedio
                    aux = ordenado_promedio[j] 
                    ordenado_promedio[j] = ordenado_promedio[j+1]
                    ordenado_promedio[j+1] = aux

                    #Swap de legajo
                    aux = ordenado_legajo[j] 
                    ordenado_legajo[j] = ordenado_legajo[j+1]
                    ordenado_legajo[j+1] = aux

                    #Swap de nombre
                    aux = ordenado_nombre[j]
                    ordenado_nombre[j] = ordenado_nombre[j+1]
                    ordenado_nombre[j+1] = aux

                    #Swap de género
                    aux = ordenado_genero[j]
                    ordenado_genero[j] = ordenado_genero[j+1]
                    ordenado_genero[j+1] = aux
    else:
        for i in range(n):
            for j in range(0,n - i -1):
                if ordenado_promedio[j] > ordenado_promedio[j + 1]: 
                    #Swap de promedio
                    aux = ordenado_promedio[j] 
                    ordenado_promedio[j] = ordenado_promedio[j+1]
                    ordenado_promedio[j+1] = aux

                    #Swap de legajo
                    aux = ordenado_legajo[j] 
                    ordenado_legajo[j] = ordenado_legajo[j+1]
                    ordenado_legajo[j+1] = aux

                    #Swap de nombre
                    aux = ordenado_nombre[j]
                    ordenado_nombre[j] = ordenado_nombre[j+1]
                    ordenado_nombre[j+1] = aux

                    #Swap de género
                    aux = ordenado_genero[j]
                    ordenado_genero[j] = ordenado_genero[j+1]
                    ordenado_genero[j+1] = aux

    for i in range(len(promedio_estudiantes)):
        if ordenado_legajo[i] != 0:
            print(f"\nLejago: {ordenado_legajo[i]}")
            print(f"Nombre: {ordenado_nombre[i]}")
            print(f"Género estudiante: {ordenado_genero[i]}")
            print(f"Promedio notas: {ordenado_promedio[i]}")
