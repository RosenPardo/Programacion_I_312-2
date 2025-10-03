
#10) Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def verificar_num_primo(numero: int, ) -> bool:
    """
    Verifica que el número ingresado sea primo.

    Args:
        numero (int): Numero a verificar.

    Returns:
        bool: True si el número es primo, False en caso contrario. 
    """

    contador = 0
    for i in range(1, numero + 1):
            
        if numero % i == 0:
            contador += 1
    
    if contador == 2:
        resultado = True
    else:
        resultado = False
    
    return resultado


print(verificar_num_primo(6))


