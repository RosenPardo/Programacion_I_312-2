
#11) Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

from for_10_funcion import verificar_primo

def mostrar_primos(numero_ingresado:int) -> None:
    """
    Muestra todos los números primos comprendidos entre 1 y el número ingresado como parámetro. 

    Args:
        numero_ingresado (int): Límite para la verificación de números primos

        return (int): None
    """
    
    for i in range(2, numero_ingresado + 1):
        if verificar_primo(i):
            print(i, "es primo. ")
        else:
            continue
            

mostrar_primos(15)


