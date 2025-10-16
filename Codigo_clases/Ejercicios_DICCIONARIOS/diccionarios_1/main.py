# 1 - Cargar manualmemte 5 estudiantes
# 2 - Mostrar el promedio de notas por estudiante y general
# 3 - Listar los nombres de los estudiantes cuya nota sea mayor o igual a 6
# 4 - Listar el o los nombre/s del o los estudiante/s con la nota mas alta
# 5 - Listar la cantidad de cantidad de estudiantes por división. 
# 6 - Calcular el porcentaje de estudiantes por división. 
# Agregar en el diccionario una key "Division" (comisión) de tres dígitos, que sean 2 divisiones distintas 312 y 313. Trabajarla como un set. 


from configuraciones import *
from funciones import *


while True:
    menu = int(input("1 - Cargar manualmemte 5 estudiantes, \n2 - Mostrar el promedio de notas por estudiante y general, \n3 - Listar los nombres de los estudiantes cuya nota sea mayor o igual a 6, \n4 - Listar el o los nombre/s del o los estudiante/s con la nota mas alta\n5 - Listar la cantidad de cantidad de estudiantes por división., \n6 - Calcular el porcentaje de estudiantes por división.\nIngrese el valor deseado: "))

    match menu:
        case 1:
            print("***Cargar manualmemte 5 estudiantes**")
            
#            carga_estudiantes(estudiantes)
            mostrar_estudiantes(estudiantes, key_2 = None, key_3 = None, key_4 = None, key_5 = None)

        case 2:
            print("***Promedio de notas por estudiante y general***")
            
            for i in range(len(estudiantes)):
                suma_notas = 0
                suma_notas += estudiantes[i]["Nota_1"]
                suma_notas += estudiantes[i]["Nota_2"]
                suma_notas += estudiantes[i]["Nota_3"]
                promedio = suma_notas / 3
                estudiantes[i]["Promedio"] = round(promedio, 2)

            mostrar_estudiantes(estudiantes)

        case 3:
            pass

        case 4:
            pass

        case 5:
            pass

        case 6:
            pass

        case _:
            break
