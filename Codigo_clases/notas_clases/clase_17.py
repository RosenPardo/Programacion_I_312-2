def leer_csv(nombre_archivo:str) -> None:
    """
    Función que permite leer e imprimir por consola un archivo csv. 

    Args:
        nombre_archivo (str): Nombre del archivo que se desea abrir.
    """
    try: 
        with open(nombre_archivo, "r") as archivo:
            matriz = []
            nombre_columnas = archivo.readline().strip().split(",")

            for linea in archivo:

                linea = linea.rstrip(",")
                fila = []
                valores = linea.split(",")

                for valor in valores:
                    if valor.isdigit():
                        fila.append(int(valor))
                    else:
                        fila.append(valor)
                matriz.append(fila)

            print(nombre_columnas)

            for fila in matriz:
                print(fila)

    except:
        print("Archivo no encontrado. ")

# PROBAR LA FUNCIÓN: leer_csv()
#
#leer_csv("archivo2.csv")
def escritura_csv(nombres_columnas:list, matriz:list, nombre_archivo:str = "Archivo.csv") -> None:
    """
    Función que crea un archivo .csv (si existe, lo sobreescribe).

    Args:
        nombres_columnas (list): Nombre de las columnas que se generarán en el archivo csv.
        matriz (list): Información de las filas que se crearán en el archivo csv. 
        nombre_archivo (str): Nombre del archivo a crear/sobreescribir.  
    """
    with open(nombre_archivo, "w") as archivo:
        archivo.write(",".join(nombres_columnas) + "\n")

        for fila in matriz:
            linea = ""
            for i in range(len(fila)):

                linea += str(fila[i])

                if i < (len(fila) - 1):
                    linea += ","

            archivo.write(linea + "\n")

# PROBAR LA FUNCION: escritura_csv()
#
#nombres_columnas = ["Nombre", "Edad", "Ciudad"]
#matriz = [["Pedro", 24, "París"], ["José", 25, "Toronto"]]
#
#escritura_csv(nombres_columnas, matriz, "archivo2.csv")


#ESCRITURA DE ARCHIVOS JSON:
import json

def escribir_json(datos:list, nombre_archivo:str) -> None:
    """
    Función que crea un archivo .json (si existe, lo sobreescribe). Se debe importar el módulo "json".

    Args:
        datos (list): Diccionario que se cargará en el archivo json. 
        nombre_archivo (str): Nombre del archivo a crear/sobreescribir. 
    """
    
    with open(nombre_archivo, "w") as archivo_json:
        json.dump(datos, archivo_json, indent=4) #El parámetro indent para que sea más legible

# PROBAR LA FUNCIÓN: escribir_json()
#
#datos = {
#    "nombre": "Juan",
#    "edad": 28,
#    "ciudad": "Madrid"
#}
#
#escribir_json(datos, "Archivo.json")

def leer_json(nombre_archivo:str) -> None:
    """
    Imprime en pantalla la información del archivo json. Se debe importar el módulo "json". 

    Args:
        nombre_archivo (str): Nombre del archivo que se desea printear. 
    """
    try:
        with open(nombre_archivo, "r") as archivo_json:
            datos = json.load(archivo_json) # Cargar el contenido en un diccionario

        print(datos)
    except: 
        print("No se encontró el archivo.")

# PROBAR LA FUNCION: leer_jston():

leer_json("archivo.json")