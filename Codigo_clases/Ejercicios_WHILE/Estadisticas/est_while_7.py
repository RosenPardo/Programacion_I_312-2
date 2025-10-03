'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

# 7) Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

numero_ingresado = int(input(f"Ingrese un número: "))

bandera = True
suma_numeros= numero_ingresado
suma_positivos = numero_ingresado
producto_negativos = 1

while bandera == True:
    
    numero_ingresado = int(input(f"Ingrese un número: "))
    
    if numero_ingresado >= 0:
        suma_numeros += numero_ingresado
    else:
        producto_negativos *= numero_ingresado

    consulta = input("Desea agregar más números? (s/n): ")
    
    if consulta == "s":
        bandera = True
    else:
        bandera = False

print(f"La suma de los números positivos ingresados es: {suma_numeros}")
print(f"El producto de los números negativos ingresados es: {producto_negativos}")