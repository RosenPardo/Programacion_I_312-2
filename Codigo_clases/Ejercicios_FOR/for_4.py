'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

'''4) Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

	5 x 0 = 0
	5 x 1  = 5
	5 x 2 = 10
	5 x 3  = 15 …
'''
numero_igresado = int(input("Ingrese el número a multiplicar: "))
print(f"{numero_igresado} x 0 = 0")

for i in range(1, 11):
        resultado = numero_igresado * i
        print(f"{numero_igresado} x {i} = {resultado}")

