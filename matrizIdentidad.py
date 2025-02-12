from ayuda import printMatriz

tabla = []
for i in range(4):
    tabla.append([])
    for j in range(4):
        valor = int(input(f"Introduce los valores ({i+1},{j+1})"))
        tabla[i].append(valor)

identidad = True
for i in range (4):
    for j in range (4):
        if i == j:
            if tabla[i][j] != 1:
                identidad = False
        else:
            if tabla[i][j] != 0:
                identidad = False


print(printMatriz(tabla))

if identidad == True:
    print("Es identidad")
else:
    print("No es")