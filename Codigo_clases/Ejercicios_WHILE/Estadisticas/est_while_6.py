'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

# 6) Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

bandera = True
numero_ingresado = 0
q_numeros_ingresados = 0
promedio_numeros = 0
suma_numeros= 0

while bandera == True:
    numero_ingresado = int(input(f"Ingrese un número: "))
    suma_numeros += numero_ingresado
    q_numeros_ingresados += 1
    consulta = input("Desea agregar más números? (s/n): ")
    
    if consulta == "s":
        bandera = True
    else:
        bandera = False

promedio_numeros = suma_numeros / q_numeros_ingresados
print(f"La suma de los números ingresados es: {suma_numeros}")
print(f"El promedio de los números ingresados es {promedio_numeros}.")
