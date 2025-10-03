'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

# 5) Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.


contador = 0
suma_numeros= 0
promedio_numeros = 0

while contador < 5:
    numero_ingresado = int(input(f"Ingrese el número {contador + 1} a sumar: "))
    suma_numeros += numero_ingresado
    contador +=1

promedio_numeros = suma_numeros / contador
print(f"La suma de los números ingresados es: {suma_numeros}")
print(f"El promedio de los números ingresados es {promedio_numeros}.")
