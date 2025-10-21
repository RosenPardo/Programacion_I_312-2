def cargar_legajo(mensaje:str = "Ingrese el número de legajo de 6 digitos: ") -> int:
    """
    Funcion que se utiliza para cargar un número de legajo, validando que su longitud sea de 6. 

    Args:
        mensaje (_type_, optional): _description_. Defaults to "Ingrese el número de legajo de 6 digitos: ".

    Returns:
        int: _description_
    """
    while True:
        try:
            legajo = input(mensaje)
            if legajo.isdigit() and len(legajo) == 6:
                return int(legajo)
            else:
                print("Ingresó un valor erróneo. Ingrese un valor de 6 digitos.")

        except:
            print("Ingresó un valor erróneo.")

def cargar_nota(mensaje:str = "Ingrese nota de Materia 1: ") -> int:
    """
    Función que se utiliza para cargar un valor númerico de 1 a 10 inclusive.

    Args:
        mensaje (str, optional): Mensaje que se mostrará en el input. Defaults to "Ingrese nota de Materia 1: ".

    Returns:
        int: Entero con valor de 1 a 10 inclusive. 
    """
    while True:
        try:
            nota = input(mensaje)
            nota = int(nota)
            if nota >= 1 and nota <= 10:
                return int(nota)
            else:
                print("Ingresó un valor erróneo.")

        except:
            print("Ingresó un valor erróneo.")

def cargar_division(mensaje:str = "Ingrese la división: ") -> int:
    """
    Función para cargar las comisiones 312 o 313. 

    Args:
        mensaje (str, optional): Mensaje que se mostrará en el input. Defaults to "Ingrese la división:".

    Returns:
        int: Número de comisión. 
    """
    while True:
        try:
            division = input(mensaje)
            division = int(division)

            if division == 312 or division == 313:
                return division
            else:
                print("Ingresó un valor erróneo. La división debe ser 312 o 313.")

        except:
            print("Ingresó un valor erróneo.")

def carga_estudiantes(estudiantes: list) -> list:
    """
    Carga una lista de diccionarios.

    Args:
        estudiantes (list): Lista de diccionarios que contiene las siguientes Keys: "Nombre", "Nota materia 1", "Nota materia 2", "Nota materia 3", "Division".

    Returns:
        list: Lista de diccionarios.
    """
    
    for i in range(len(estudiantes)):
        
        estudiantes[i]["Legajo"] = cargar_legajo()

        while True:
            nombre = input("Ingrese el nombre del estudiante: ")
            if nombre.replace(" ", "").isalpha():
                estudiantes[i]["Nombre"] = nombre
                break
                
            print("Ingresó un valor erróneo. ")
        
        estudiantes[i]["Nota materia 1"] = cargar_nota()
        estudiantes[i]["Nota materia 2"] = cargar_nota(mensaje = "Ingrese nota de Materia 2: ")
        estudiantes[i]["Nota materia 3"] = cargar_nota(mensaje = "Ingrese nota de Materia 3: ")
        estudiantes[i]["Division"] = cargar_division()
    print("Estudiante cargado correctamente. \n")
    return estudiantes

def mostrar_estudiantes(estudiantes: list, key_1: str = "Legajo", key_2: str = "Nombre", key_3: str = "Nota_1", key_4: str = "Nota_2", key_5: str = "Nota_3", key_6: str = "Div.", key_7:str = "Promedio") -> None:
    """
    Imprime una lista de diccionarios. Se debe colocar "None" en el caso de que no se quiera mostrar la key. 

    Args:
        estudiantes (list): Lista de diccionarios que contienen las siguientes Keys: "Legajo", "Nombre", "Nota_1", "Nota_2", "Nota_3", "Div.", "Promedio".
    """
    encabezado = [key_1, key_2, key_3, key_4, key_5, key_6, key_7]

    for i in range(len(encabezado)):
        if encabezado[i] != None:
            print(encabezado[i], end=" \t\t")
    print("\n")

    for i in range(len(estudiantes)):
        for j in range(len(encabezado)):
            if encabezado[j] != None:
                print(estudiantes[i][encabezado[j]], end="\t\t")

        print("\n")

def calcular_promedio(estudiantes: list) -> None:
    """
    Función que calcula y guarda el promedio de los estudiantes. 

    Args:
        estudiantes (list): Lista de diccionarios que contienen las siguientes Keys: "Legajo", "Nombre", "Nota_1", "Nota_2", "Nota_3", "Div.", "Promedio".
    """
    suma_notas_gen = 0
    for i in range(len(estudiantes)):
        suma_notas = 0
        suma_notas += estudiantes[i]["Nota_1"]
        suma_notas += estudiantes[i]["Nota_2"]
        suma_notas += estudiantes[i]["Nota_3"]
        promedio = suma_notas / 3
        estudiantes[i]["Promedio"] = round(promedio, 2)
        
        suma_notas_gen += promedio
    
    promedio_gen = suma_notas_gen / len(estudiantes)
    
    print(f"El promedio general es de {round(promedio_gen, 2)}\n")
