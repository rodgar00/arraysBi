from ayuda import printMatriz

claseColumna = 3
alumnosClase = 30

notas = []

for nFilas in range(alumnosClase):
    notas.append([])
    for nColumnas in range(claseColumna):
        valor = float(input(f"Introduce la nota para el Alumno {nFilas + 1} de la clase {nColumnas + 1}: "))
        notas[nFilas].append(valor)

notaMaxima = [max(fila) for fila in notas]
notaMinima = [min(fila) for fila in notas]

print(printMatriz(notas))

for i in range(alumnosClase):
    for j in range(claseColumna):
        print(f"La nota máxima del Alumno {i + 1} de la clase {j + 1} es: {notaMaxima[i]}")
        print(f"La nota mínima del Alumno {i + 1} de la clase {j + 1} es: {notaMinima[i]}")
