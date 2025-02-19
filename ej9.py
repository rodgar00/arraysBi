from ayuda import printMatriz

tabla = []

for filas in range(20):
    fila = []
    for columnas in range(2):
        if columnas == 0:
            exponente = int(input(f"Ingrese el exponente {filas + 1}/20: "))
            fila.append(exponente)
        else:
            fila.append(2 ** exponente)
    tabla.append(fila)

print("\nTabla de potencias de 2:")
printMatriz(tabla)
