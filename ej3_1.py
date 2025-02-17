matriz = [
    [3, 2, 5, 0, 9],
    [9, 10, 2, 3, 1],
    [-3, 2, 3, 43, 1]
]

matrizGirada = []

for i in range(len(matriz[0])):
    nuevaFila = []
    for j in range(len(matriz)-1, -1, -1):
        nuevaFila.append(matriz[j][i])
    matrizGirada.append(nuevaFila)

for fila in matrizGirada:
    print(fila)
