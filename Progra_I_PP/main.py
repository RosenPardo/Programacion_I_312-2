#En el módulo configuraciones se encuentran harcodeadas los valores del punto 1. 

from configuraciones import *
from funciones_menu1 import *
from funciones_menu2 import *
from funciones_menu3 import *
from funciones_menu4 import *
from funciones_menu5 import *
from funciones_menu6 import *
from funciones_menu7 import *

primer_ejecucion = True

while True:
    
    menu = input("\n*MENÚ DE OPCIONES* \n 1) Carga de datos. \n 2) Mostrar datos cargados. \n 3) Ver promedio por estudiante. \n 4) Ordenar y mostrar los datos de los estudiantes por promedio. \n 5) Mostrar la/s materia/s con mayor promedio general. \n 6) Buscar y mostrar todos los datos de un estudiante por legajo. \n 7) Buscar y mostrar cuantas veces se repite cada calificación en una asignatura determinada. \n 8) Salir del programa.\n Seleccione el valor: ")
    menu = validacion_menu(menu) 

    while primer_ejecucion:
        if primer_ejecucion and menu != 1:
            print("Debe cargar datos para poder continuar. \n")
            menu = input("\n*MENÚ DE OPCIONES* \n 1) Carga de datos. \n 2) Mostrar datos cargados. \n 3) Ver promedio por estudiante. \n 4) Ordenar y mostrar los datos de los estudiantes por promedio. \n 5) Mostrar la/s materia/s con mayor promedio general. \n 6) Buscar y mostrar todos los datos de un estudiante por legajo. \n 7) Buscar y mostrar cuantas veces se repite cada calificación en una asignatura determinada. \n 8) Salir del programa.\n Seleccione el valor: ")
            menu = validacion_menu(menu) 
        if menu == 1:
            primer_ejecucion = False

    match menu:
        case 1:
            print("\nCARGA DE DATOS: \n")
            cargar_datos(legajo_estudiante, nombre_estudiante, genero_estudiante, calificaciones, estado_legajo)

        case 2:
            print("\n MOSTRAR DATOS CARGADOS: \n")
            mostrar_datos_cargados(calificaciones, legajo_estudiante, nombre_estudiante, genero_estudiante, estado_legajo)

        case 3:
            print("\n VER PROMEDIO POR ESTUDIANTE: \n")
            mostrar_promedios(calificaciones, estado_legajo, legajo_estudiante, nombre_estudiante, genero_estudiante)

        case 4:
            print("\n ORDENAR Y MOSTRAR ESTUDIANTES POR PROMEDIO: \n")
            ordenar_promedios(calificaciones, estado_legajo, legajo_estudiante, nombre_estudiante, genero_estudiante)

        case 5:
            print("\n MOSTRAR LA/S MATERIA/S CON MAYOR PROMEDIO GENERAL: \n")
            ordenar_mostrar_promedio_materias(calificaciones)

        case 6:
            print("\n BUSQUEDA DATOS ESTUDIANTE POR LEGAJO: \n")
            buscar_estudiante(legajo_estudiante, nombre_estudiante, genero_estudiante, estado_legajo, calificaciones)

        case 7:
            print("\n BUSCAR Y MOSTRAR CUANTAS VECES SE REPITE CADA CALIFICACIÓN: \n")
            mostar_notas_por_materia(calificaciones)

        case 8:
            print("**Se cierra el programa.**")
            break