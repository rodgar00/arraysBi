from ayuda import printMatriz

tabla = []

for i in range(4):
    tabla.append([])
    for j in range(4):
        valor = int(input(f"Ingresa el valor para la posición ({i+1},{j+1}): "))
        tabla[i].append(valor)

es_identidad = True
for i in range(4):
    for j in range(4):
        if i == j:
            if tabla[i][j] != 1:
                es_identidad = False
        else:
            if tabla[i][j] != 0:
                es_identidad = False

print("\nLa matriz ingresada es:")
printMatriz(tabla)

if es_identidad == True:
    print("\nLa matriz es identidad.")
else:
    print("\nLa matriz no es identidad.")
