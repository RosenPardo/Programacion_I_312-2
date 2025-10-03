# Hacer una funcion que cargue de manera aleatoria 10 elementos
#from Ejercicios_ARRAYS.funciones_utiles import mostrar_lista

def cargar_elemento_aleatoria(vector):
    
    for i in range(len(vector)):
        indice = input("Indique en qué indice desea cargar datos: ")
        dato = int(input(f"Ingrese el valor a cargar en indice {indice}: "))
        vector[indice] = dato
    

lista_test = [0] * 3
cargar_elemento_aleatoria(lista_test)
print(lista_test)


#Ejercicio 3 de Bruno https://onlinegdb.com/59TQibZKw
