#Validación de Número Entero
"""
📌 Objetivo: Implementar una función que verifique si una cadena representa un número entero válido (positivo o negativo). 
🔹 Restricciones:
 ✅ Recorrer la cadena carácter por carácter.
 ✅ Validar que el primer carácter puede ser un signo + o - (opcional).
 ✅ Los demás caracteres deben ser únicamente dígitos (0-9).
 ✅ No se pueden usar .isdigit().
"""

def solo_enteros(cadena):
    
    if len(cadena) == 1: #Corroborar que si es el largo de la cadena es 1, que no sea un signo menos
        if ord(cadena[i]) == 32:
            son_enteros = False
            return son_enteros

    for i in range(len(cadena)):
        if (ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57) or (ord(cadena[i]) == 45) or (ord(cadena[i]) == 32):
            son_enteros = True
        else:
            son_enteros = False
            break

    return son_enteros

cadena_test = input("Ingrese la cadena de caracteres a verificar: ")

prueba_funcion = solo_enteros(cadena_test)

print(prueba_funcion)


print(cadena_test.isdigit())