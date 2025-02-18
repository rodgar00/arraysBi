matriz = [
    [3, 2, 5, 0, 9],
    [9, 10, 2, 3, 1],
    [-3, 2, 3, 43, 1]
]

matrizTranspuesta = []

for i in range(len(matriz[0])):
    nuevaFila = []
    for j in range(len(matriz)):
        nuevaFila.append(matriz[j][i])
    matrizTranspuesta.append(nuevaFila)

for fila in matrizTranspuesta:
    print(fila)
