
#Realizar una función que reciba una cadena de caracteres y pase a minúscula el texto de la misma. 


def texto_a_minuscula(array_texto):

    array_capitalizado = ""

    for caracter in range(len(array_texto)):
        if ord(array_texto[caracter]) >= 65 and ord(array_texto[caracter]) <= 90:
            letra_minuscula = chr(ord(array_texto[caracter]) + 32)
            array_capitalizado += letra_minuscula
        
        else:
            array_capitalizado += array_texto[caracter]
            
        if ord(array_texto[caracter]) == 165:
            letra_minuscula = chr(ord(array_texto[caracter]) - 1)
            array_capitalizado += letra_minuscula
        
    return array_capitalizado


array_test = "MaÑana"

print()
print(array_test)

array_test = texto_a_minuscula(array_test)

print()
print(array_test)
