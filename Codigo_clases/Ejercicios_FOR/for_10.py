'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

#10) Ingresar un número. Determinar si el número es primo o no.

valor_ingresado = int(input("Agregue un valor: "))
contador = 0
for i in range(1, valor_ingresado + 1):

    if valor_ingresado % i == 0:
        contador += 1
    
if contador == 2:
    print(valor_ingresado, "es primo. ")
else:
    print(valor_ingresado, "no es primo. ")


# Ej: https://onlinegdb.com/NkadN3Zfi
