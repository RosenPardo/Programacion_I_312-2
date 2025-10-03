from funciones_utiles import mostrar_lista

# 1) Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.

def crear_array_int(largo: int) -> list:
    array_creada = [0] * largo

    return array_creada

""" TEST de la función:
lista_creada = crear_array_int(5)

mostrar_lista(lista_creada)
"""