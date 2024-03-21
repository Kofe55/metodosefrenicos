# metodosefrenicos
Repositorio de Python de Metodos Numericos Cuarto Semestre

# Algoritmo ProcesoGaussJordan
print("Ingrese el número de ecuaciones (n):", end='')
n = int(input())
matriz = [[0 for j in range(n+1)] for i in range(n)]
literales = [0 for i in range(n)]

for i in range(n):
    print(f"Ingrese la literal de la variable {i+1}:", end='')
    literales[i] = input()

for i in range(n):
    for j in range(n):
        print(f"Ingrese el coeficiente de la variable {literales[j]} de la ecuación {i+1}:", end='')
        matriz[i][j] = float(input())
    print(f"Ingrese la constante de la ecuación {i+1}:", end='')
    matriz[i][n] = float(input())

print()

for i in range(n):
    if matriz[i][i] == 0:
        print("Error: división entre cero.")
        print()
    else:
        for k in range(n):
            if k != i:
                termino = matriz[k][i] / matriz[i][i]
                for j in range(n+1):
                    matriz[k][j] -= termino * matriz[i][j]

print("Solución:")
print()

for i in range(n):
    termino = matriz[i][n] / matriz[i][i]
    print(f"{literales[i]} = {termino}")