#Cadena de caracteres

#Una cadena de caracteres la puedo pensar como una lista de caracteres:

cadena_uno = "esto es una cadena"
cadena_dos = "hola mundo"
cadena_tres = "Otra cadena"


#Si quiero escribir una cadena con comillas puedo ponerlo de la siguiente forma:

cadena = "Hello 'World'" #Entre comillas con '

cadena_dos = "Hello \"World\""


#Operaciones básicas que puedo hacer 

print(cadena_dos[1:25]) #Slicing (subcadenas)

print(cadena_dos*3) #Repetición de cadenas)

#Comparación de cadenas Operadores Relacionales (<,>,!=,==,<=,>=):

print(chr(12))
print(ord("a"))
"""
def capitalizar_texto(array_str):
    cadena_capitalizada = []
    for i in range(len(array_str)):
        if ord(array_str[i:i+1]) > 50:
            cadena_capitalizada += array_str[i] + 32

    return cadena_capitalizada
"""

array_test = "Esto es un texto"
print(array_test)

#capitalizar_texto(array_test)

print(array_test)



cadena = "Procesador"

print(cadena <= "Procesador")
print(cadena <= "P")

