from ayuda import printMatriz

columnas = 5
filas = 5

tabla = []

for nFilas in range(filas):
    tabla.append([])
    for nColumnas in range(columnas):
        valor = int(input(f"Introduce el valor para [{nFilas + 1}][{nColumnas + 1}]: "))
        tabla[nFilas].append(valor)

resultadoC = [sum(fila[columnas] for fila in tabla) for j in range(columnas)]

resultadoF = [sum(fila) for fila in tabla]

print(printMatriz(tabla))
print(f"Resultado de sumar las columnas: {resultadoC}")
print(f"Resultado de sumar las filas: {resultadoF}")
