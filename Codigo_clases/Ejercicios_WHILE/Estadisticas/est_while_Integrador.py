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
# Text to ASCII Art Generator: https://patorjk.com/

'''Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
A) La suma acumulada de los números negativos.
B) La suma acumulada de los números positivos.
C) La cantidad de números negativos ingresados.
D) El promedio de los números positivos.
E) El número positivo más grande.
F) El porcentaje de números negativos ingresados, respecto del total de ingresos.
'''



numero_ingresado = int(input(f"Ingrese un número: "))

continua_carga = True
primer_ingreso = True

while continua_carga == True:
    if primer_ingreso == True:
        primer_ingreso = False
        if numero_ingresado > 0:
                suma_positivos = numero_ingresado
                mayor_positivo = numero_ingresado 
                q_ingresos_positivos = 1
                suma_negativos = 0
                porcentaje_negativos = 0
                q_ingresos_negativos = 0
                continue

        elif numero_ingresado < 0:
                suma_positivos = 0
                mayor_positivo = 0 
                q_ingresos_positivos = 0
                suma_negativos = numero_ingresado
                porcentaje_negativos = numero_ingresado
                q_ingresos_negativos = 1
                continue
        else:
                suma_positivos = 0
                mayor_positivo = 0 
                q_ingresos_positivos = 0
                suma_negativos = 0
                porcentaje_negativos = 0
                q_ingresos_negativos = 0
                continue

    else:
        consulta = input("Desea agregar más números? (s/n): ")
        if consulta == "s":
            continua_carga = True
        else:
            continua_carga = False
            break
    
    numero_ingresado = int(input(f"Ingrese un número: "))
    
    if numero_ingresado > 0:
        suma_positivos += numero_ingresado
        q_ingresos_positivos += 1
        if numero_ingresado > mayor_positivo:
            mayor_positivo = numero_ingresado

    elif numero_ingresado < 0:
        suma_negativos += numero_ingresado
        q_ingresos_negativos += 1
    else:
        continue
    
if q_ingresos_negativos == 0:
    porcentaje_negativos = "0"
else:
    porcentaje_negativos = (q_ingresos_negativos * 100) / (q_ingresos_negativos + q_ingresos_positivos)


if q_ingresos_positivos == 0:
    promedio_positivos = "0"
else:
    promedio_positivos = suma_positivos / q_ingresos_positivos

if q_ingresos_negativos != 0:
    promedio_positivos = suma_positivos / q_ingresos_negativos
else:
    promedio_positivos = 0

print("A) La suma acumulada de los números negativos es", suma_negativos)
print("B) La suma acumulada de los números positivos es", suma_positivos)
print("C) La cantidad de números negativos ingresados es", q_ingresos_negativos)
print(f"D) El promedio de los números positivos es {promedio_positivos}")
print(f"E) El número positivo más grande fue {mayor_positivo}")
print(f"F) El porcentaje de números negativos ingresados, respecto del total de ingresos es del {porcentaje_negativos} %.")