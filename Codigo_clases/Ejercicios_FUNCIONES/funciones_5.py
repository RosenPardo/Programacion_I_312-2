
#5) Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

def area_circulo(radio: int) -> float:
    """Calcula el área de un círculo.

    Args:
        radio: Valor del radio del círculo.

    Returns:
        int: Área del círculo. 
    """
    
    resultado = 3.14 * (radio ** 2)
    return resultado


print(area_circulo(10))


