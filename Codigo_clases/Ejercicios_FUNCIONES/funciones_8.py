
#8) Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def verificar_mayor(numero_a: int, numero_b: int, numero_c: int, ) -> int:
    """Pide 3 valores numéricos y retorna el número más grande.

    Args:
        numero_a (int): Número a comparar.
        numero_b (int): Número a comparar.
        numero_c (int): Número a comparar.

    Returns:
        int: Número más grande entre los comparados. 
    """

    if numero_a >= numero_b and numero_a >= numero_c:
        resultado = numero_a
    
    elif numero_b >= numero_a and numero_b >= numero_c:
        resultado = numero_b
    
    elif numero_c >= numero_a and numero_c >= numero_b:
        resultado = numero_c

    return resultado


print(verificar_mayor(922, 911, 920))


