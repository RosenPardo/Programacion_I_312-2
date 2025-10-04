def solo_enteros(cadena:str) -> bool:
    """Verifica si una cadena representa un número entero válido (positivo o negativo)

    Args:
        cadena (str): Cadena a verificar.

    Returns:
        bool: True si es una cadena de Int | False si no es solamente de enteros
    """
    
    if len(cadena) == 1: #Corroborar que si es el largo de la cadena es 1, que no sea un signo menos
        if ord(cadena) == 32:
            son_enteros = False
            return son_enteros

    for i in range(len(cadena)):
        if (ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57) or (ord(cadena[i]) == 45) or (ord(cadena[i]) == 32):
            son_enteros = True
        else:
            son_enteros = False
            break

    return son_enteros

def validacion_menu(menu:str) -> int:
    """Verifica que sea un númro entero con la función solo_enteros(), castea el valor y verifica que sea entre 1 y 8. Si encuentra un error, muestra en consola que es un valor erróneo.  

    Args:
        menu (str): Cadena de caracteres a verificar.
    
    Returns: 
        int: Número entero entre 1 y 8
    """
    validacion_int= solo_enteros(menu)

    if validacion_int:
        menu = int(menu)
        if menu < 1 or menu > 8:
            print("Ingresó un valor incorrecto. Intente de nuevo")
            menu = None
#            elif menu != 1 and inicializado == False:
#                print("No existen cargas activas. Realice al menos una carga.")
#                menu = None
    else:
        print("Ingresó un valor incorrecto. Intente de nuevo")
        menu = None
    return menu



def solo_letras(cadena:str) -> bool:
    """Determina si una cadena está compuesta únicamente por letras (mayúsculas y minúsculas) o espacios.

    Args:
        cadena (str): Cadena de caracteres a verificar. 

    Returns:
        bool: True si es una cadena de letras. | False si no es solamente de letras.
    """
    #Se toma el código ASCII extendido para "ñ" y "Ñ" (ISO 8859-1 o Latin-1), los códigos son: "ñ" -> 241 "Ñ" -> 209
    
    for i in range(len(cadena)):
        if (ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90) or (ord(cadena[i]) >= 97 and ord(cadena[i]) <= 122) or (ord(cadena[i]) == 32) or (ord(cadena[i]) == 209) or (ord(cadena[i]) == 241):
            son_letras = True
        else:
            son_letras = False
            break

    return son_letras

def capitalizar_texto(array_texto):

    array_capitalizado = ""

    for caracter in range(len(array_texto)):
        if ord(array_texto[caracter]) >= 97 and ord(array_texto[caracter]) <= 122:
            letra_mayus = chr(ord(array_texto[caracter]) - 32)
            array_capitalizado += letra_mayus
        else:
            array_capitalizado += array_texto[caracter]
            
    return array_capitalizado

def validar_genero(cadena: chr) -> bool:
    """Verifica que el valor de la cadena sea 'F' 'M' o 'X'"

    Args:
        cadena (chr): Cadena a verificar

    Returns:
        bool: True si es un caracter de válido | False si no es uno de los caracteres deseados.
    """
    cadena = capitalizar_texto(cadena)

    if cadena == "F" or cadena == "M" or cadena == "X":
        return True
    else:
        return False