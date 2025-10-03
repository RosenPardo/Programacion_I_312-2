'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

#11) Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

valor_ingresado = int(input("Agregue un valor: "))
contador_primos = 0

for i in range(2, valor_ingresado + 1):
    bandera = True
    for j in range(2, i):
        if i % j == 0:
            bandera = False
            break

    if bandera:
        print(i, "es primo. ")
        contador_primos += 1
print(f"Se encontraron {contador_primos} primos.")

