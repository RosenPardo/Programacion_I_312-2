
# Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

def sumar_digitos(numero:int)-> int:
    str_numero_dos = ""
    bandera = False
    str_numero = str(numero)

    # Guardo el último valor de la cadena: 
    if len(str_numero) == 1:
        valor = int(str_numero)
    
    # Controlo que la cadena tenga elementos:
    if len(str_numero) > 1:

        # Recorro la cadena:
        for digito in str_numero:
            
            # Utilizo la cadena para quedarme con el primer elemento de la cadena en cada llamada:
            if bandera == False:
                valor = int(digito)
                bandera = True
                continue
            
            # Armo la subcadena, sin el primer elemento de la cadena.
            if bandera == True: 
                str_numero_dos += digito
        
        # Paso a entero la subcadena para pasarla como parámetro en la llamada a la recursividad.
        int_numero = int(str_numero_dos)
    else:
        return valor
    
    return valor + sumar_digitos(int_numero)

total = sumar_digitos(1234)

print(total)

