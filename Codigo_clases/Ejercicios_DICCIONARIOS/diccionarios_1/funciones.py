def carga_estudiantes(estudiantes: list) -> list:
    """
    Carga una lista de diccionarios

    Args:
        estudiantes (list): Lista de diccionarios que contiene las siguientes Keys: "Nombre", "Nota materia 1", "Nota materia 2", "Nota materia 3", "Division".

    Returns:
        list: _description_
    """
    for i in range(len(estudiantes)):
        estudiantes[i]["Nombre"] = input("Ingrese el nombre del estudiante: ")
        estudiantes[i]["Nota materia 1"] = input("Ingrese nota de Materia 1: ")
        estudiantes[i]["Nota materia 2"] = input("Ingrese nota de Materia 2: ")
        estudiantes[i]["Nota materia 3"] = input("Ingrese nota de Materia 3: ")
        estudiantes[i]["Division"] = input("Ingrese la división: ")
        print("\n")
    
    return estudiantes

#def mostrar_estudiantes(estudiantes: list) -> None:
#    """
#    Imprime una lista de diccionarios.
#
#    Args:
#        estudiantes (list): Lista de diccionarios que contienen las siguientes Keys: "Nombre", "Nota materia 1", "Nota materia 2", "Nota materia 3", "Division".
#    """
#    print("Nombre: \tNota materia 1: \tNota materia 2: \tNota materia 3: \tDivision: \tPromedio: ")
#    for i in range(len(estudiantes)):
#        print(estudiantes[i]["Nombre"], end="\t\t")
#        print(estudiantes[i]["Nota materia 1"], end="\t\t\t")
#        print(estudiantes[i]["Nota materia 2"], end="\t\t\t")
#        print(estudiantes[i]["Nota materia 3"], end="\t\t\t")
#        print(estudiantes[i]["Division"], end="\t\t")
#        print(estudiantes[i]["Promedio"], end="\t\t")
#        print("\n")

def variable_none(variable):
    if variable == None:
        variable = ""
    return variable

def mostrar_estudiantes(estudiantes: list, key_1: str = "Nombre", key_2: str = "Nota_1", key_3: str = "Nota_2", key_4: str = "Nota_3", key_5: str = "Legajo", key_6: str = "Promedio") -> None:
    """
    Imprime una lista de diccionarios.

    Args:
        estudiantes (list): Lista de diccionarios que contienen las siguientes Keys: "Nombre", "Nota materia 1", "Nota materia 2", "Nota materia 3", "Division".
    """
    key_1 = variable_none(key_1)
    key_2 = variable_none(key_2)
    key_3 = variable_none(key_3)
    key_4 = variable_none(key_4)
    key_5 = variable_none(key_5)
    key_6 = variable_none(key_6)

    print(f"{key_1} \t{key_2} \t{key_3} \t{key_4} \t{key_5} \t{key_6} ")
    for i in range(len(estudiantes)):
        if key_1 != "":
            print(estudiantes[i][key_1], end="\t\t")

        if key_2 != "":
            print(estudiantes[i][key_2], end="\t\t\t")

        if key_3 != "":
            print(estudiantes[i][key_3], end="\t\t\t")

        if key_4 != "":
            print(estudiantes[i][key_4], end="\t\t\t")

        if key_5 != "":
            print(estudiantes[i][key_5], end="\t\t")

        if key_6 != "":
            print(estudiantes[i][key_6], end="\t\t")

        print("\n")


