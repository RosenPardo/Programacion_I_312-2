
"""Escritura usando""" #.write()

#archivo = open("archivo.txt", "w")
#archivo.write("Primera linea de texto\n")
#archivo.write("Segunda linea\n")
#archivo.write("Tercera linea\n")
#archivo.close()


"""Escritura usando""" #.writelines()

# archivo = open("archivo.txt", "w")
# lineas_texto = ["Primera linea de texto con lista\n", 
#                 "Segunda linea con lista\n", 
#                 "Tercera linea con lista\n"]
# archivo.writelines(lineas_texto)
# archivo.close()
# 
# archivo = open("archivo.txt", "r")
# texto = archivo.read()
# print(f"El contenido del archivo es: \n{texto}")
# archivo.close()

# De esta forma podemos crear una lista que guarde la info del archivo y nos permita modificarla.


archivo = open("archivo.txt", "r+")

lista_lineas = archivo.readlines()

for linea in lista_lineas:
    print(linea, end= "")

archivo.close()

for i in range(len(lista_lineas)):
    lista_lineas[i] = "Modifico la lista y la vuelvo a grabar"
    break

archivo = open("archivo.txt", "w")
archivo.writelines(lista_lineas)
archivo.close()