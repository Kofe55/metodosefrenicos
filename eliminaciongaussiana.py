# Función para mostrar la matriz
def mostrarMatriz(matriz, orden):
    for i in range(orden):
        linea = "| "
        for j in range(orden + 1):
            linea += str(matriz[i][j]) + " "
        linea += "| "
        print(linea)

# Solicitar al usuario el orden de la matriz
orden = int(input("Ingrese el orden de la matriz: "))

# Crear la matriz vacía
matriz = [[0 for j in range(orden + 1)] for i in range(orden)]

# Solicitar al usuario los valores de la matriz
print("Ingrese los elementos de la matriz:")
for i in range(orden):
    for j in range(orden):
        matriz[i][j] = float(input(f"Elemento [{i+1}][{j+1}]: "))
    matriz[i][orden] = float(input(f"Término independiente de la fila {i+1}: "))

mostrarMatriz(matriz, orden)

# Recorrer la matriz
for j in range(orden + 1):
    for i in range(orden):
        if i > j:
            # Dividir los elementos de la matriz
            division = matriz[i][j] / matriz[j][j]
            for k in range(orden + 1):
                # Obtener el nuevo valor para los elementos en la diagonal inferior
                matriz[i][k] = matriz[i][k] - division * matriz[j][k]

# Recorrer la matriz
x = [0] * orden
for i in range(orden, 0, -1):
    suma = 0
    for j in range(i, orden):
        suma = suma + matriz[i - 1][j] * x[j]
    # Obtener los valores de las variables
    x[i - 1] = (matriz[i - 1][orden] - suma) / matriz[i - 1][i - 1]

# Mostrar los valores de las variables
print("\nSolución:")
for i in range(orden):
    print(f"x{i} = {x[i]}")
