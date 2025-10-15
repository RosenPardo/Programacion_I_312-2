# 1- Crea al menos tres listas, cada una representando una línea de colectivo.
# Cada lista debe tener 7 elementos, uno por cada día de la semana.
# 
# 2- Permite ingresar por teclado la cantidad de pasajeros transportados por día para cada línea.
# Los valores deben ser acumulables (es decir, si se vuelve a ingresar datos, se suman a los anteriores).
# 
# 3- El programa debe imprimir por consola:
# -Las listas completas con los pasajeros por día de cada línea.
# -El total de pasajeros por día (sumando las tres líneas).
# -El total semanal de cada línea.
# -El total general de pasajeros de las tres líneas durante toda la semana


colectivo_17 = []
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("Ingrese la cantidad de pasajeros para la línea 17:")

for dia in dias_semana:
    pasajeros = int(input(f"{dia}: "))
    colectivo_17.append(pasajeros)




