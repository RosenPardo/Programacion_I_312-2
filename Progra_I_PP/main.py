"""
1 – Realizar la carga de los datos en la matriz y en cada una de las listas. (Se pueden hardcodear los datos).
Realizar una función para validar cada dato a ser cargado.

2 – Mostrar todos los datos, esto es la matriz completa de calificaciones conjuntamente con las listas de legajo,
género y nombre del estudiante, siempre y cuando su estado tenga el valor uno. Realizar una función que recorra
todos y otra que muestre uno.

3 – Calcular el promedio de cada estudiante y guardarlo en una nueva lista de promedios. Realizar una función
que calcule el promedio.

4 – Ordenar y mostrar los datos de los estudiantes por promedio de manera DESC. Realizar una función que
ordene, la cual deberá ordenar de manera ASC o DESC de acuerdo a un parámetro de ordenamiento.

5 – Mostrar la/s materia/s con mayor promedio general. Realizar una función para recorrer todas y otra para
mostrar una. Teniendo en cuenta que no hay una lista de materias, sino que cada columna de la matriz representa
una materia, entonces cada materia tomará la siguiente nomenclatura para su nombre MATERIA_ índice más
uno. Por ejemplo: para la materia del índice cero de la columna, será MATERIA_1.

6 – Buscar y mostrar todos los datos de un estudiante por legajo, incluyendo el promedio calculado en el ítem 3.
Realizar una función de búsqueda. Realizar una función que recorra uno y otra que muestre todos.

7 – Buscar y mostrar cuantas veces se repite cada calificación en una asignatura determinada.
Realizar una función que reciba la matriz de calificaciones y el número de materia (índice más uno) como
parámetros, y retorne una lista de 10 elementos, donde en el índice 0 estará la cantidad de veces que se repite la
nota 1, en el índice 1 estará la cantidad de veces que se repite la nota 2, y así sucesivamente hasta el índice 9
donde estará la cantidad de veces que se repite la nota 10.

8 – Salir del programa.

"""
from validaciones import *
from funciones import *

cantidad_estudiantes = 10
calificaciones = inicializar_matriz(cantidad_estudiantes, 5, 0)
nombre_estudiante = [0] * cantidad_estudiantes
genero_estudiante = [0] * cantidad_estudiantes
legajo_estudiante = [0] * cantidad_estudiantes
estado_legajo = [0] * cantidad_estudiantes

while True:

    menu = input("\n*MENÚ DE OPCIONES* \n 1) Carga de datos. \n 2) Mostrar datos cargados. \n 3) Ver promedio por estudiante. \n 4) Ordenar y mostrar los datos de los estudiantes por promedio. \n 5) Mostrar la/s materia/s con mayor promedio general. \n 6) Buscar y mostrar todos los datos de un estudiante por legajo. \n 7) Buscar y mostrar cuantas veces se repite cada calificación en una asignatura determinada. \n 8) Salir del programa.\n Seleccione el valor: ")
    
    menu = validacion_menu(menu) #FALTA VALIDAR QUE SEA EL VALOR 1 la primer opción.

    match menu:
        case 1:
            print("\nCARGA DE DATOS: \n")

            nombre_estudiante = input("Ingrese el nombre del estudiante: ")

            validacion_nombres = solo_letras(nombre_estudiante)

            print(validacion_nombres)

        case 2:
            print("\n ")
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            break