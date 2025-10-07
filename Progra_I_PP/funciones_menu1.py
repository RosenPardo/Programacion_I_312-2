from validaciones import *


#Corrobora que no se dupliquen los valores de legajo:
def legajo_duplicado(legajo_estudiante:list, num_legajo:int) -> bool:
    """
    Función que recorre la lista de legajos en búsqueda de valores duplicados.

    Args:
        legajo_estudiante (list): Array con números de legajo. 
        num_legajo (int): Número a buscar dentro del array. 

    Returns:
        bool: Devuelve True si encuentra valores duplicados | False si no se encontraron duplicados. 
    """
    for i in range(len(legajo_estudiante)):
        if legajo_estudiante[i] == int(num_legajo):
            print("El número de legajo ya existe. ")
            return True
    
    return False

#Carga de todos los datos de estudiantes: 
def cargar_datos(legajo_estudiante:list, nombre_estudiante:list, genero_estudiante:list, calificaciones:list, estado_legajo:list) -> bool:
    """
    Carga los arrays compartidos, validando que los datos sean correctos. 

    Args:
        legajo_estudiante (list): Espera dato de tipo int, comprendido en un valor de 6 digitos. 
        nombre_estudiante (list): Espera dato de tipo str, únicamente letras y espacios (no permite tildes).
        genero_estudiante (list): Solamente permite el ingreso de los caracteres 'F' 'M' o 'X'.
        estado_legajo (list): Array con el estado del legajo 0 inactivo 1 activo. Se utiliza para buscar espacios libres donde cargar los nuevos datos. 

    Returns:
        bool: Devuelve True si se logró cargar correctamente. 
    """
    for i in range(len(legajo_estudiante)):

        if estado_legajo[i] == 0:
            #Carga legajo:
            num_legajo = input("Ingrese el número de legajo que desea cargar: ")
            validar_int = solo_enteros(num_legajo)
            if validar_int:
                validar_duplicado = legajo_duplicado(legajo_estudiante, num_legajo)

            while validar_int == False or len(num_legajo) != 6 or validar_duplicado == True:
                num_legajo = input("Ingresó un valor erróneo. Ingrese el número de legajo que desea cargar: ")
                validar_int = solo_enteros(num_legajo)
                if validar_int:
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
            
            #Carga de calificaciones: 
            for j in range(len(calificaciones[i])):
                valor_nota = input(f"Ingrese el la nota de Materia_{j+1}: ")
                validar_int = solo_enteros(valor_nota)
                if validar_int:
                    valor_nota = int(valor_nota)

                while validar_int == False or valor_nota < 1 or valor_nota > 10:
                    valor_nota = input(f"Ingresó un valor erróneo (Nota comprendida entre 1 - 10). Ingrese el la nota de Materia_{j+1}: ")
                    validar_int = solo_enteros(valor_nota)
                    if validar_int:
                        valor_nota = int(valor_nota)

                calificaciones[i][j] = int(valor_nota)

            estado_legajo[i] = 1

            print("\n Estudiante cargado correctamente. \n")


    return True
