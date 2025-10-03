'''
Rosendo Pardo
DNI: 39558016
COM: 312-2 TN
'''

# 4) Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.

ingreso_color = input("Ingrese un color (Rojo | Verde | Azul): ")

while ingreso_color != "Rojo" and ingreso_color != "Verde" and ingreso_color != "Azul" :
    ingreso_color = input("No es un color de la lista, ingrese un color (Rojo | Verde | Azul): ")
    

print("Seleccionó", ingreso_color)

