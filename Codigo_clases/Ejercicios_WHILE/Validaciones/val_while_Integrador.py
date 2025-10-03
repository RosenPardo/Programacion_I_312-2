'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''
#  _____      _                           _            
# |_   _|    | |                         | |           
#   | | _ __ | |_ ___  __ _ _ __ __ _  __| | ___  _ __ 
#   | || '_ \| __/ _ \/ _` | '__/ _` |/ _` |/ _ \| '__|
#  _| || | | | ||  __/ (_| | | | (_| | (_| | (_) | |   
#  \___/_| |_|\__\___|\__, |_|  \__,_|\__,_|\___/|_|   
#                      __/ |                           
#                      |___/  
'''
1) Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.

Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

Una vez ingresados y validados los datos, mostrarlos por pantalla.
'''


apellido_ingresado = input("ingrese su apellido: ")

while True:
    edad_ingresada  = input("Ingrese su edad: ")
    try:
        edad_ingresada  = int(edad_ingresada )
        if edad_ingresada < 18 or edad_ingresada > 90:
            print("Ingresó una edad inválida. Debe ser entre 18 y 90 años.")
            continue
        break
    except:
        print("Ingresó una edad inválida. Debe ser entre 18 y 90 años.")



estado_civil = int(input(f"Siendo: \n 1) “Soltero/a”,\n 2) ”Casado/a”,\n 3) “Divorciado/a”\n 4) “Viudo/a”. \nIngrese el número correspondiente a su estado civil: "))

match estado_civil:
    case 1: 
        estado_civil = "Soltero/a"
    case 2: 
        estado_civil = "Casado/a"
    case 3: 
        estado_civil = "Divorciado/a"
    case 4: 
        estado_civil = "Viudo/a"

while True:
    numero_legajo = int(input("Ingrese el número de legajo de 4 dígitos, sin ceros: "))

    if len(str(numero_legajo)) != 4:
        print("Debes ingresar un número de 4 digitos. No se tomarán en cuenta los ceros a la izquierda: ")
    else:
        break
    

print(apellido_ingresado)
print(edad_ingresada )
print(estado_civil)
print(numero_legajo)

