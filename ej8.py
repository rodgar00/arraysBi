import random

from ayuda import printMatriz

filas = 10
columnas = 15
matriz = []
sumaMatriz = []

for nFilas in range(filas):
    matriz.append([])
    for nColumnas in range(columnas):
        valor = random.randint(1, 10)
        matriz[nFilas].append(valor)

for nFilas in range(filas):
    sumaElementos = sum(matriz[nFilas])
    sumaMatriz.append(sumaElementos)
print(printMatriz(matriz))
print(sumaMatriz)
