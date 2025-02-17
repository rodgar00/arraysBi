from ayuda import printMatriz

tabla = []

for i in range(5):
    tabla.append([])
    for j in range(5):
        if i == j:
            tabla[i].append(1)
        else:
            tabla[i].append(2)

print(printMatriz(tabla))