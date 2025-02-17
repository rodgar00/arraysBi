from ayuda import printMatriz

tabla = []

# Captura los valores de la matriz 4x4 por teclado
for i in range(4):
    tabla.append([])
    for j in range(4):
        valor = int(input(f"Ingresa el valor para la posición ({i+1},{j+1}): "))
        tabla[i].append(valor)

# Verifica si la matriz es identidad
es_identidad = True
for i in range(4):
    for j in range(4):
        if i == j:
            if tabla[i][j] != 1:
                es_identidad = False
        else:
            if tabla[i][j] != 0:
                es_identidad = False

# Imprimir la matriz
print("\nLa matriz ingresada es:")
printMatriz(tabla)

# Mostrar si es identidad
if es_identidad == True:
    print("\nLa matriz es identidad.")
else:
    print("\nLa matriz NO es identidad.")
