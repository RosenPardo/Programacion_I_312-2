'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

# 4) Mostrar la suma de los números pares desde el 1 hasta el 10.

contador = 0
suma_numeros= 0

while contador < 10:
    contador +=1
    print(f"El contador es {contador}")
    if contador % 2 == 0:
        suma_numeros += contador
        print(f"La suma es {suma_numeros}")

print(suma_numeros)