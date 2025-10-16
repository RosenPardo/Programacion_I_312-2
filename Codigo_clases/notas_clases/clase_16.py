# TDA: tuplas - sets y diccionarios



mi_tupla = ("Juan", "Perez", 30)

nombre, apellido, edad = mi_tupla

print(f"Hola {apellido}, {nombre}. La edad registrada es {edad}")

set = {3, 5, 9, 5, 3, 4, 3}
print(type(set))
print(set)

print("\n")
print("DICCIONARIO: ")

diccionario = [{
    "Nombre": "Juan",
    "Edad": 21,
    "Ciudad": "Buenos Aires"
},
{
    "Nombre": "Maria",
    "Edad": 23,
    "Ciudad": "Bahía Blanca"
}]
print(diccionario)

diccionario[0]["Ciudad"] = "Marcos Paz"

print(diccionario)

print(f"type: {type(diccionario)}")
print(f"keys: {diccionario.keys()}")
print(f"values: {diccionario.values()}")
print(f"items: {diccionario.items()}")








