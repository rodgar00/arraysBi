from ayuda import printMatriz

filasAsignaturas = 3
columnasAlumnos = 15

notas = []

for nFilas in range(filasAsignaturas):
    notas.append([])
    for nColumnas in range(columnasAlumnos):
        valor = float(input(f"Introduce la nota de la Asignatura {nFilas + 1} para el Alumno {nColumnas + 1}: "))
        notas[nFilas].append(valor)

media_alumnos = [sum(notas[i][j] for i in range(filasAsignaturas)) / filasAsignaturas for j in range(columnasAlumnos)]

media_asignaturas = [sum(fila) / columnasAlumnos for fila in notas]

media_clase = sum(media_asignaturas) / filasAsignaturas

print(printMatriz(notas))


print("\nNota media de cada alumno:", media_alumnos)
print("Nota media de cada asignatura:", media_asignaturas)
print(f"Nota media de la clase: {media_clase:.2f}")
