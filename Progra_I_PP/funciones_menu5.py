from validaciones import solo_enteros


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

def ordenar_mostrar_promedio_materias(calificaciones:list) -> None:
    """
    La función ordena e imprime la/las materia/s con mayor promedio. 

    Args:
        calificaciones (list): Matriz con calificaciones. 
    """
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
            print(f"Promedio Materia_{nombre_materias[i]}: {promedio_materias[i]}")
    else:
        for i in range(p):
            print(f"Promedio Materia_{nombre_materias[i]}: {promedio_materias[i]}")
            break







