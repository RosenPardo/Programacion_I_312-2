
#Verificación de Cadena Alfabética Ej: https://onlinegdb.com/_p6sScV9P / https://www.onlinegdb.com/CKgcsiKIZ 
"""
📌 Objetivo: Crear una función que determine si una cadena está compuesta únicamente por letras mayúsculas y minúsculas (sin espacios, números ni símbolos).
🔹 Restricciones:
 ✅ Recorrer la cadena carácter por carácter.
 ✅ Comparar los caracteres con los valores ASCII para determinar si son letras.
 ✅ No se pueden usar métodos como .isalpha().
"""

def solo_letras(cadena):
    for i in range(len(cadena)):
        if (ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90) or (ord(cadena[i]) >= 97 and ord(cadena[i]) <= 122) or (ord(cadena[i]) == 32):
            son_letras = True
        else:
            son_letras = False
            break

    return son_letras

cadena_test = input("Ingrese la cadena de caracteres a verificar: ")

prueba_funcion = solo_letras(cadena_test)

print(prueba_funcion)
