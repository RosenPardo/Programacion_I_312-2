'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

#2) Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

clave = "pepe95"

ingreso_sistema = input("Ingrese la clave: ")
q_intentos = 1

while q_intentos < 3:
    
    if ingreso_sistema == clave:
        break
    else:
        q_intentos += 1
    
    ingreso_sistema = input("Intente de nuevo. Ingrese la clave: ")

if q_intentos < 3:
    print("Ingresó correctamente. ")
else:
    print("Máximo de claves incorrectas. No es posible ingresar al sistema. ")


