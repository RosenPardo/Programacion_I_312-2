#Hacer una lista cuyos indices almacenan productos variados, y deben estructurarse con los siguientes elementos. 

#Nombre del producto, Modelo, Precio, Categoria.

#El programa tiene que tener la capacidad de añadir el producto, verlo en pantalla (como matriz). 

#Debe también modificiar información y eliminarla.


lista_productos = {
    "Nombre de producto": [],
    "Modelo": [],
    "Precio": [],
    "Categoría": [],
}

print(lista_productos)

nuevo_producto = {
    "Nombre de producto": input("Ingrese el nombre del nuevo producto: "),
    "Modelo": input("Ingrese el modelo del producto: "),
    "Precio": input("Ingrese el precio: "),
    "Categoría": input("Ingrese la categoría: ")
}




def recorrer_matriz(mi_matriz):
    for i in range(len(mi_matriz)): 
        for j in range(len(mi_matriz[i])): 
            print(mi_matriz[i][j], end= "\t\t")
        print("")


encabezado = list(lista_productos.keys())

for i in range(len(encabezado)):
    lista_productos[encabezado[i]].append(nuevo_producto[encabezado[i]])


#valores = list(lista_productos.values())

for i in range(len(encabezado)):
    print(encabezado[i], end=" | ")
print("\n")

for i in range(len(lista_productos["Nombre de producto"])):
    print(lista_productos[encabezado[0]][i], end=" | ")
    print(lista_productos[encabezado[1]][i], end=" | ")
    print(lista_productos[encabezado[2]][i], end=" | ")
    print(lista_productos[encabezado[3]][i], end=" | ")
    print("\n")

