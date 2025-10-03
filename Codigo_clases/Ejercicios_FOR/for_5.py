'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

#5) Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

suma_numeros = 0
cantidad = 0

for i in range(10):
    valor = int(input("Ingrese un número: "))    

    suma_numeros += valor
    cantidad +=1
    if valor == 0:
        break


promedio = suma_numeros / cantidad
print(f"la suma es: {suma_numeros}")
print(f"el promedio es: {promedio}")

# Ej: 5 https://onlinegdb.com/-zpG0y2AT 
# Ej: 5 https://onlinegdb.com/MnR2wYvwT


