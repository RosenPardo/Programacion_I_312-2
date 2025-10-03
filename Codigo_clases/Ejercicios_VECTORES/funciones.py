def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    """Funcion para inicializar una matriz.

    Args:
        cantidad_filas (int): Cantidad de índices en el array principal. 
        cantidad_columnas (int): Cantidad de índices en los arrays internos.
        valor_inicial (any): Valor con el que se rellenan los arrays.

    Returns:
        list: Matriz creada. 
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas  
        matriz += [fila]
    return matriz

def cargar_lista(lista:list, mensaje_dato:str = "Ingrese el str a cargar: ") -> None:
    """
    Carga de valores a una lista inicializada de forma aleatoria, indicando el valor a incorporar y su ubicación en la lista

    Args:
        Lista (list): Lista a cargar
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


    return lista

def cargar_notas(legajo_estudiante, notas_estudiantes, estado_legajo, nombre_estudiantes, cantidad_notas):
    cantidad_notas -= 1

    if notas_estudiantes[legajo_estudiante][cantidad_notas] != 0:
        print("No hay más lugar para cargar. ")
        return None

    
    for i in range(len(notas_estudiantes)):
        for j in range(len(notas_estudiantes[i])):
            
            if i == legajo_estudiante and estado_legajo[i] == 1 and notas_estudiantes[i][j] == 0:
                nota_a_cargar = int(input(f"Ingrese la nota a cargar para el estudiante {nombre_estudiantes[i]}: "))
                
                while nota_a_cargar <= 0 or nota_a_cargar > 10:
                    nota_a_cargar = int(input(f"No es un rango válido (1 - 10) Ingrese la nota a cargar para el estudiante {nombre_estudiantes[i]}: "))

                notas_estudiantes[i][j]= nota_a_cargar
                break
