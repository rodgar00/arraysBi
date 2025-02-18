from ayuda import printMatriz

columnas = 5
filas = 5

tabla = []

for nFilas in range(filas):
    tabla.append([])
    for nColumnas in range(columnas):
        valor = int(input(f"Introduce el valor para [{nFilas + 1}][{nColumnas + 1}]: "))
        tabla[nFilas].append(valor)

resultadoC = []
for nColumnas in range(columnas):
    sumaColumnas = sum(tabla[fila][nColumnas] for fila in range(filas))
    resultadoC.append(sumaColumnas)

resultadoF = []
for nFilas in range(filas):
    sumaFilas = sum(tabla[nFilas])
    resultadoF.append(sumaFilas)

print(printMatriz(tabla))
print(f"Resultado de sumar las columnas: {resultadoC}")
print(f"Resultado de sumar las filas: {resultadoF}")
