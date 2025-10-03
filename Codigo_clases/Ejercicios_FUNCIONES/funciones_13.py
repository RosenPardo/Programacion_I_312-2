
#13) Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.


#1) Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
def numero_entero(numero_entero = 0):
    
    while True:
        numero_entero = input("Ingrese un número enero: ")
        try:
            numero_entero = int(numero_entero)
            break
        except:
            print("Ingreso incorrecto. Intente nuevamente.")

    return numero_entero

print(numero_entero())


#2) Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def numero_flotante(flotante= 0):
    while True:
        flotante = input("Ingrese un número flotante: ")
        try:
            flotante = float(flotante)
            break
        except:
            print("Ingreso incorrecto. Intente nuevamente.")

    return flotante

print(numero_flotante())


# 3) Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 
def cadena(texto = ""):
    while True:
        texto = input("Ingrese un texto: ")
        try:
            texto = str(texto)
            break
        except:
            print("Ingreso incorrecto. Intente nuevamente.")

    return texto

variable_cadena = cadena()
print(variable_cadena)
print(type(variable_cadena))


