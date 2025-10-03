'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

#Se crea el archivo para poder extrar la función en el ejercicio 11 de FUNCIONES.

#valor_ingresado = int(input("Agregue un valor: "))

def verificar_primo(valor_ingresado):
    contador = 0
    for i in range(1, valor_ingresado + 1):

        if valor_ingresado % i == 0:
            contador += 1
        
    if contador == 2:
        return True
    else:
        return False


# Ej: https://onlinegdb.com/NkadN3Zfi
