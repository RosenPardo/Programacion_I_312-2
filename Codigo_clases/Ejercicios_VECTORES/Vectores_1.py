
'''
vectores:
estados
nombre
legajo
de 100 elementos

matriz de 100 por 3 elementos de números enteros, que van a representar las notas del curso de ingreso
ademas tendremos un vector de 100 elementos donde se cargaran los promedios de las tres notas

1 vector de estados (0/1)
1 vector de nombres
1 vector de legajo (puede ser secuencial, al indice 0 le pongo 0, al indice 1 le pongo legajo 1)
1 vector más del tipo float, para calcular el promedio

Hacer 1 menú de opciones donde:
1= Generar e inicializar los vectores y la matriz
2= Para cargar los datos (nombre, porque el legajo lo puedo sacar del índice)
3= Cargar notas en matiz
4= Calcular y poblar (asignar a cada elemento del vector) los promedios
5= Buscar por promedio >= que el dato a buscar y mostrar el listado de estudiantes que cumplan esa condición
6= Salir

Armar biblioteca "Ejercicio". Que cada opción de menú, sea un función y modularizar. 


son 4 vectores y 1 matriz. cada indice corresponde a 1 estudiante

Tienen que ser todas listas paralelas. 
'''

from funciones import *


programa_activo = True

while programa_activo == True:
    try: 
        print(f"\n \nLista estudiantes: {nombre_estudiantes}")
        print(f"Lista estado legajos: {estado_legajo})")
        print(f"Matriz notas estudiantes: {notas_estudiantes})")
        print(f"Lista promedio notas: {promedio_notas})")

    except:
        print("")

    menu = int(input("\n*MENÚ DE OPCIONES* \n 1) Inicializar. \n 2) Carga de legajos. \n 3) Carga de notas. \n 4) Calcular promedios. \n 5) Buscar promedio. \n 6) Salir. \n Seleccione el valor: "))


    match menu:
            case 1:
                print("\nINICIALIZAR \n")
                cantidad_estudiantes = 5
                cantidad_notas = 3
                
                nombre_estudiantes = [0] * cantidad_estudiantes
                estado_legajo = [0] * cantidad_estudiantes
                promedio_notas = [0] * cantidad_estudiantes
                notas_estudiantes = inicializar_matriz(cantidad_estudiantes, cantidad_notas, 0)

            case 2:
                print("\nCARGA DE LEGAJOS \n")
                
                nombre_estudiantes = cargar_lista(nombre_estudiantes, "Ingrese el nombre del estudiante: ")
                
                for i in range(len(nombre_estudiantes)):
                    if nombre_estudiantes[i] != 0:
                        estado_legajo[i] = 1

            case 3:
                print("\nCARGA DE NOTAS \n")
                
                legajo_estudiante = int(input("Ingrese el legajo que desea cargar: "))
                cargar_notas(legajo_estudiante, notas_estudiantes, estado_legajo, nombre_estudiantes, cantidad_notas)


            case 4:
                print("\nPROMEDIO DE ESTUDIANTES \n")
            case 5:
                print("5")
            case 6:
                programa_activo = False

