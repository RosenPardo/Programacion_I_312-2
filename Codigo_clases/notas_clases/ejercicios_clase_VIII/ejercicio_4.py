# Ejercicio 4)
# Hacer una app que, utilizando una biblioteca propia de vectores, realice una carga al estilo "agenda de contactos" del celular. Para esto, desarrollar una función que reciba 2 vectores (estados y datos) y que realice la carga en datos, si hay espacio libre. 

from modulo_ejercicio_4 import *



estados = lista_cant_establecida(3)
datos = lista_cant_establecida(3)

contador = 0
bandera = True

while bandera:
    carga_mixta(estados, datos)
    contador += 1
    
    if contador < len(datos):
        continuar = input("Desea continuar la carga? y/n: ")

    if continuar == "n" or contador == len(datos):
        bandera = False
    


print(estados)
print(datos)
