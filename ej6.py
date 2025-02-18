from ayuda import printMatriz

filasAsignaturas = 5
columnasAlumnos = 5

notas = []

for nFilas in range(filasAsignaturas):
    notas.append([])
    for nColumnas in range(columnasAlumnos):
        valor = float(input(f"Introduce la nota de la Asignatura {nFilas + 1} para el Alumno {nColumnas + 1}: "))
        notas[nFilas].append(valor)

media_alumnos = []
for j in range(columnasAlumnos):
    sumaNotas = sum(notas[i][j] for i in range(filasAsignaturas))
    media_alumnos.append(sumaNotas / filasAsignaturas)

media_asignaturas = []
for i in range(filasAsignaturas):
    sumaNotasAsignatura = sum(notas[i])
    media_asignaturas.append(sumaNotasAsignatura / columnasAlumnos)

sumaMediaAsignaturas = sum(media_asignaturas)
media_clase = sumaMediaAsignaturas / filasAsignaturas

print(f"Media de los alumnos: {media_alumnos}")
print(f"Media de las asignaturas: {media_asignaturas}")
print(f"Media de la clase: {media_clase}")

print(printMatriz(notas))