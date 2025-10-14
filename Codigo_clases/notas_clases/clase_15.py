#TDA: listas	Manejo de listas mediante métodos de python. Búsquedas.
lista_1 = [1, 2, 3, 4, 5, 6]
lista_2 = ["a", "b", "c", "d"]

# append Agrega un elemento al final de la lista.
lista_1.append(7) #lista_1 = [1, 2, 3, 4, 5, 6, 7]

# extend Añade una lista en la lista inicial.
lista_1.extend(lista_2) #lista_1 = [1, 2, 3, 4, 5, 6, 7, "a", "b", "c", "d"]

# pop (#) Elimina y devuelve el elemento en la posición dada. Si no se especifica un índice, se elimina y devuelve el último elemento. 
valor_eliminado = lista_1.pop(1) #lista_1 = [1, 3, 4, 5, 6, 7, "a", "b", "c", "d"] ///// #valor_eliminado = 2

# index Devuelve el índice de la primera ocurrencia del elemento especificado 
indice_valor_buscado = lista_1.index(5) #indice_valor_buscado = 3

# insert(i, elemento) Inserta un elemento en la posición (i) especificada.
lista_1.insert(1, 2) #lista_1 = [1, 2, 3, 4, 5, 6, 7, "a", "b", "c", "d"]

# remove(elemento) Elimina la primera ocurrencia del elemento especificado.
lista_1.remove("a") #lista_1 = [1, 2, 3, 4, 5, 6, 7, "b", "c", "d"]
lista_1.remove("b") #lista_1 = [1, 2, 3, 4, 5, 6, 7, "c", "d"]
lista_1.remove("c") #lista_1 = [1, 2, 3, 4, 5, 6, 7, "d"]
lista_1.remove("d") #lista_1 = [1, 2, 3, 4, 5, 6, 7]

# reverse Invierte el orden de los elementos de la lista.
lista_1.reverse() #lista_1 = [7, 6, 5, 4, 3, 2, 1]

# sort Ordena la lista en orden ascendente
lista_1.sort() #lista_1 = [1, 2, 3, 4, 5, 6, 7]

# del lista[i] elimina el elemento de la posición indicada. También puede usarse para eliminar varios elementos con slicing: del lista[1:4]
del lista_1[0] #lista_1 = [2, 3, 4, 5, 6, 7]

# clear Elimina todos los elementos de la lista.
lista_1.clear() #lista_1 = []

####################################################################################
#copy. Importando el módulo "copy", vamos a poder hacer una "shallow copy", que es pasar el valor por referencia, o "Deep copy", que crea una nueva lista independiente.

import copy

print(f"lista_2 = {lista_2}") #lista_2 = ['a', 'b', 'c', 'd']
print(f"lista_2 = {id(lista_2)}") #lista_2 = 2194000056704
print()

copia_lista_2 = copy.deepcopy(lista_2)
print(f"copia_lista_2 = {copia_lista_2}") #copia_lista_2 = ['a', 'b', 'c', 'd']
print(f"copia_lista_2 = {id(copia_lista_2)}") #copia_lista_2 = 2194000345536









