lista_diccionario = []

diccionario_tecnicatura = {
    "Sede": "Graciela Pane, Avellaneda",
    "plan_2003": {
    "Materias": ["Matemática", "Programación I", "Arquitectura de Sistemas", "Inglés"],
    "lista_estudiantes": [{"estudiante": "Juan", "Nro. Legajo": 123440}]
},
"plan_2024": {
    "Sede": "Graciela Pane, Avellaneda",
    "Materias": ["Matemática", "Programación I", "Arquitectura de Sistemas", "Inglés"],
    "lista_estudiantes": [{"estudiante": "Manuel", "Nro. Legajo": 123441}]
}
}

#print(diccionario_tecnicatura)

lista_diccionario.append(diccionario_tecnicatura)


#print(lista_diccionario)

keys = []

for i in range(len(diccionario_tecnicatura)):
    keys += diccionario_tecnicatura.keys()

keys = set(keys)

print(f"Keys de diccionario es: {keys}")


