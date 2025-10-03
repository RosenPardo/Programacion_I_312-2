def lista_cant_establecida (cant_elementos: int):
    mi_lista_numeros = [0] * cant_elementos

    return mi_lista_numeros

def carga_mixta(estados: list, datos: list) -> None:
    """
    Recorre la lista datos, y si encuentra espacio registrado en la lista estados, pide el ingreso de un valor de tipo int.

    Args:
        estados (list): Array que registra 0 si el espacio está vacío y 1 si el espacio está ocupado
        datos (list): Array a cargar, si el indice obtenido de estados se encuentra con valor 0. 
    """

    for i in range(len(datos)):
        if estados[i] == 0:
            estados[i] = 1
            datos[i] = int(input("Ingrese el dato que desea cargar: "))
            break

