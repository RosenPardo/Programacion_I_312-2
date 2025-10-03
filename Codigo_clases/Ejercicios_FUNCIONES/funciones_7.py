
#7) Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def verificar_par(numero: int) -> bool:
    """Verifica si el número es un número par o impar

    Args:
        numero (int): Número a verificar

    Returns:
        bool: True si el número es par, False en caso contrario.  
    """
    if numero % 2 == 0:
        resultado = True
    else:
        resultado = False

    return resultado


print(verificar_par(12))


