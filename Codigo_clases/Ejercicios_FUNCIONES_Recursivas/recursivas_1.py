
# Realizar una función recursiva que calcule la suma de los primeros números naturales:

def sumar_naturales(numero: int, valor_inicial) -> int:

    if valor_inicial != numero:
        resultado = numero + sumar_naturales(numero, valor_inicial + 1)
    else:
        resultado = numero

    return resultado

print(sumar_naturales(8,1))