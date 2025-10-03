


def carga_de_datos(valores_ingresados):
    valores_ingresados = []
    for i in range(10):
        ingreso_de_datos = input("Ingrese los valores numéricos: ")
        try:
            ingreso_de_datos = int(ingreso_de_datos)
            if ingreso_de_datos >= -1000 and ingreso_de_datos <= 1000:
                valores_ingresados += [ingreso_de_datos]
            else:    
                print("El valor no es correcto. Debe estár en el rango de -1000 a 1000.")

        except:
            print("El valor no es correcto. Debe estár en el rango de -1000 a 1000.")
    return valores_ingresados