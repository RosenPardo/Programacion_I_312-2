
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
