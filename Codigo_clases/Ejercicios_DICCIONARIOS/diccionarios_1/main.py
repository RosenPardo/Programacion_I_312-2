# Trabajo Práctico 1: Gestión de Estudiantes
# Crea una lista llamada 'estudiantes', donde cada elemento sea un diccionario con las claves:
# 'legajo', 'nombre', 'nota_1', 'nota_2', 'nota_3', 'promedio'.
# Consignas:
# 1. Cargar manualmente (input) al menos 5 estudiantes.
# 2. Mostrar el promedio de notas general y de cada estudiante.
# 3. Listar los nombres de los estudiantes con nota mayor o igual a 6.
# 4. Mostrar el nombre del estudiante con la nota más alta.
# 5. Crear un set de divisiones, con los datos 312 y 313. Recorrer el set y realizar lo siguiente:
#     - Por cada división, listar los estudiantes.
#     - Mostrar el porcentaje de estudiantes por cada división.

from configuraciones import *
from funciones_cargar_mostrar import *


while True:
    menu = int(input("1 - Cargar manualmemte 5 estudiantes, \n2 - Mostrar el promedio de notas por estudiante y general, \n3 - Listar los nombres de los estudiantes cuya nota sea mayor o igual a 6, \n4 - Listar el o los nombre/s del o los estudiante/s con la nota mas alta\n5 - Listar la cantidad de cantidad de estudiantes por división., \n6 - Calcular el porcentaje de estudiantes por división.\nIngrese el valor deseado: "))

    match menu:
        case 1:
            print("***Cargar manualmemte 5 estudiantes**")
            
            carga_estudiantes(estudiantes)
            mostrar_estudiantes(estudiantes, key_7= None)

        case 2:
            print("**Promedio de notas por estudiante y general** \n")

            calcular_promedio(estudiantes)
            mostrar_estudiantes(estudiantes, key_1= None, key_3= None, key_4= None, key_5= None, key_6= None)

        case 3:
            print("**")

        case 4:
            pass

        case 5:
            pass

        case 6:
            pass

        case _:
            break
