
#Realizar una función que reciba una cadena de caracteres y capitalice el texto de la misma. 


def capitalizar_texto(array_texto):

    array_capitalizado = ""

    for caracter in range(len(array_texto)):
        if ord(array_texto[caracter]) >= 97 and ord(array_texto[caracter]) <= 122:
            letra_mayus = chr(ord(array_texto[caracter]) - 32)
            array_capitalizado += letra_mayus
        else:
            array_capitalizado += array_texto[caracter]
            
    return array_capitalizado


array_test = "ESDAsdkasdlkjASLDkja"

print()
print(array_test)

array_test = capitalizar_texto(array_test)

print()
print(array_test)
