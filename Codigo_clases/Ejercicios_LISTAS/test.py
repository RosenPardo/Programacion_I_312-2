lista_numeros = [2, 4, 56, 23, 2, 3]

for i in range(len(lista_numeros)):
    print(lista_numeros[i], end=f"\t")


lista_numeros.sort()

print()
for i in range(len(lista_numeros)):
    print(lista_numeros[i], end=f"\t")

