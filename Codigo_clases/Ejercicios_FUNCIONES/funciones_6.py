
#6) Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def verificar_par(numero: int) -> bool:
    """Verifica si el número es un número par o impar

    Args:
        numero (int): Número a verificar

    Returns:
        bool: Devuelve True si es un número par.  
    """
    if numero % 2 == 0:
        resultado = True
    else:
        resultado = False

    return resultado


print(verificar_par(12))


