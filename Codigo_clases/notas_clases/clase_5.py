# Modulos y paquetes

from Ejercicios_FUNCIONES.funciones_10 import * #Trae todas las funciones del documento.py
from Ejercicios_FUNCIONES import saludar, funcion2, funcion3 #Trae las funciones ESPECÍFICAS del documento.py
from Ejercicios_FUNCIONES import saludar #Trae SOLO la función del documento.py

numero_ingresado = int(input("VERIFICADOR DE NUMEROS PRIMO \n Escriba el número a verificar: "))

if verificar_num_primo(numero_ingresado):
    print("Es primo")
else:
    print("No es primo")



