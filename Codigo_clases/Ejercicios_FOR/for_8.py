'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

'''8) Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:
    1
    12
    123
    1234
    12345
'''

valor_ingresado = int(input("Agregue un valor: "))

for i in range(0, valor_ingresado):
    fila_piramide = ""
    
    for j in range(0, i + 1):
        fila_piramide += str(j + 1)
    
    print(fila_piramide)



# Ej: https://onlinegdb.com/NkadN3Zfi
'''
9) Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.
10) Ingresar un número. Determinar si el número es primo o no.
11) Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.
'''