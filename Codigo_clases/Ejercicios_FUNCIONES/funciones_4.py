
#4) Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

def area_rectangulo(base: int, altura: int) -> int:
    """Calcula el área de un rectángulo, multiplicando la base por la altura

    Args:
        base (int): Ancho del rectángulo.
        altura (int): Alto del rectángulo.

    Returns:
        int: Área del rectángulo
    """
    area = base * altura
    return area


print(area_rectangulo(10, 15))

