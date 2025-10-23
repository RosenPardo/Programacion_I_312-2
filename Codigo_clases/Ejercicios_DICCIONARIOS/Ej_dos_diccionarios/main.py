# Crear el diccionario de las notas de estudiantes e ingresar las notas cada vez que el usuario lo necesite ingresar.



lista_diccionario = []

diccionario_tecnicatura = {
    'Sede': 'Graciela Pane, Avellaneda',
    'plan_2003':{
        'Materias': [
            {'Matemáticas': 8,
            'Programación I (Python)': 9, 
            'Arquitectura de Sistemas': 7,
            'Inglés': 8

            }],
        'lista_estudiantes': [
            {'estudiante': 'Juan',
            'No. Legajo': 123440
            }
            ]
        },
    
    'plan_2024': {
        'lista_estudiantes': [{'estudiante': 'Juan','No.Legajo': 123440}],
        },
        'lista_notas': [{'Matemáticas': 8,
            'Programación I (Python)': 9, 
            'Arquitectura de Sistemas': 7,
            'Inglés': 8}]  
        
}


estudiante = input('INGRESE EL NOMBRE DE UN ESTUDIANTE: ')
legajo = input('Ingrese el numero de legajo del estudiante: ')

lista_estudiantes = [{"estudiante": estudiante, "No. Legajo": legajo}]

diccionario_tecnicatura['plan_2024']["lista_estudiantes"].append(lista_estudiantes)

print(diccionario_tecnicatura.items(), end="\n")
