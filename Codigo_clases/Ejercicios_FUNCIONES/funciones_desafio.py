'''
#Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:

def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> None:
    pass

En donde:
MENSAJE: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
MENSAJE_ERROR: mensaje de error en el caso de que el dato ingresado sea invalido.
MINIMO: valor mínimo admitido (inclusive)
MAXIMO: valor máximo admitido (inclusive)
REINTENTOS: cantidad de veces que se volverá a pedir el dato en caso de error.
'''

def get_int(mensaje:str = "Ingrese un número: ", mensaje_error:str = "Ingresó un valor erróneo.", minimo:int = 0, maximo:int = 0, reintentos:int = 0) -> int | None:
    """
    Pide un número por consola.

    Args:
        minimo (int): Valor mínimo admitido (inclusive)
        maximo (int): Valor máximo admitido (inclusive)
        reintentos (int): Cantidad de veces que se volverá a pedir el dato en caso de error.
        mensaje (_type_, optional): Es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola. Defaults to "Ingrese un número: ".
        mensaje_error (str, optional): Mensaje de error en el caso de que el dato ingresado sea invalido. Defaults to "Ingresó un valor erróneo.".
    """
    contador_intentos = 1
    while contador_intentos <= reintentos:
        try:
            numero_entero = input(mensaje)
            numero_entero = int(numero_entero)
        except:
            print(mensaje_error)
            contador_intentos += 1
    
        if numero_entero < minimo or numero_entero > maximo:
            print(mensaje_error)
            contador_intentos += 1
            continue
        else:
            return numero_entero
    return "Superó el máximo de intentos. "
        


print(get_int(minimo=10, maximo=100, reintentos=4)
)


