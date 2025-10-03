'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

#1) Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

clave = "pepe95"

ingreso_sistema = input("Ingrese la clave: ")

while ingreso_sistema != clave:
    ingreso_sistema = input("Intente de nuevo. Ingrese la clave: ")


print("Ingresó correctamente. ")


