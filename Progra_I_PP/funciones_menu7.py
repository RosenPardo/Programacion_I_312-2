from validaciones import solo_enteros

def mostar_notas_por_materia(calificaciones:list):
    materia = input("Seleccione qué materia desea ver cuantas veces se repite cada calificación: ")
    validar_int = solo_enteros(materia)
    if validar_int:
        materia = int(materia)

    while validar_int == False or materia < 1 or materia > 5:
        materia = input("Valor erróneo. Seleccione qué materia desea ver cuantas veces se repite cada calificación (Materia 1-5): ")
        validar_int = solo_enteros(materia)
        if validar_int:
            materia = int(materia)

    cantidad_por_nota = [0] * 10 

    for i in range(len(calificaciones)):
        nota = calificaciones[i][materia - 1]

        if nota >= 1 and nota <= 10:
            cantidad_por_nota[nota - 1] += 1
    
    print(f"Calificaciones de Materia_{materia}: ")
    for j in range(len(cantidad_por_nota)):
        print(f"Veces que se repite {j+1}: {cantidad_por_nota[j]}")

