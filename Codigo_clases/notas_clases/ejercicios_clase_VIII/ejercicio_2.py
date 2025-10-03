# Hacer una funcion que carge de manera secuencial diez elementos numericos

from Ejercicios_ARRAYS.funciones_utiles import mostrar_lista

def cargar_elemento_secuencial(vector: list = []):
    for i in range(10):
        valor = input(f"Ingrese el valor a cargar en indice {i}: ")
        vector[i] = valor

lista_prueba = [0] * 10

cargar_elemento_secuencial(lista_prueba)

mostrar_lista(lista_prueba)


#Ejercicio 2 https://onlinegdb.com/jeZpdLS4XV