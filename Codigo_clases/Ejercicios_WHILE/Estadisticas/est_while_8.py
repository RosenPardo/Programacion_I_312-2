'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

#8) Ingresar 10 números enteros. Determinar el máximo y el mínimo.

contador = 0
bandera = True

while contador != 10:
    contador +=1
    numero_ingresado = int(input(f"Ingrese un número: "))
    
    if bandera == True:
        bandera = False
        numero_max = numero_ingresado
        numero_min = numero_ingresado

    if numero_ingresado >= numero_max:
        numero_max = numero_ingresado
    elif numero_ingresado <= numero_min:
        numero_min = numero_ingresado

print("En el ingreso de datos,", numero_max, "fue el número más alto.")
print("En el ingreso de datos,", numero_min, "fue el número más bajo.")