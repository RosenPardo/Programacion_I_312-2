numero= 0
suma_numeros = 0

'''
while True:
    numero = input("ingrese el número que desea sumar: ")
    numero = int(numero)
    suma_numeros += numero

    respuesta = input("Desea continuar? (s/n)")
    
    if respuesta == "n":
        break


print(f"La suma de los números ingresados es: {suma_numeros}")

'''
respuesta = True

while respuesta == True:
    print("Hola")

    respuesta = input("desea continuar? (s/n): ")
    
    while respuesta != 'n' and respuesta != 's':
        respuesta = input("Por favor, ingrese una respuesta válida desea continuar? (s/n): ")

    if respuesta == "s":
        respuesta = True
        
    elif respuesta == "n":
        respuesta = False

print("Finalizado")