'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

# 3) Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

ingreso_nota = int(input("Ingrese la nota: "))

while ingreso_nota < 1 or ingreso_nota > 10:
    ingreso_nota = int(input("Ingrese un valor entre 1 y 10. Ingrese la nota: "))


print("La nota ingresada es", ingreso_nota)

