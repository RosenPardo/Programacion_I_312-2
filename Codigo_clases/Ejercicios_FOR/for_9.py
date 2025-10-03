'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

#9) Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

valor_ingresado = int(input("Agregue un valor: "))
contador = 0

for i in range(1, valor_ingresado + 1):
    
    if valor_ingresado % i == 0:
        print(f"{i} es divisor de {valor_ingresado}")
        contador += 1

print(f"Existieron {contador} divisores. ")





# Ej: https://onlinegdb.com/NkadN3Zfi
