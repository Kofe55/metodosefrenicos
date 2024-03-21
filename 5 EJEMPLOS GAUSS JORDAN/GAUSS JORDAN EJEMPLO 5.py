def resolver_sistema(matriz):
    n = len(matriz)
    solucion = [0] * n

    # Convertir la matriz a una forma escalonada reducida por filas (forma escalonada reducida por Gauss-Jordan)
    for i in range(n):
        # Dividir la fila i-ésima para que el elemento diagonal sea igual a 1
        divisor = matriz[i][i]
        for j in range(i, n + 1):
            matriz[i][j] /= divisor

        # Hacer cero los elementos por encima y por debajo del elemento diagonal
        for k in range(n):
            if k != i:
                factor = matriz[k][i]
                for j in range(i, n + 1):
                    matriz[k][j] -= factor * matriz[i][j]

    # Extraer la solución del sistema de ecuaciones de la última columna
    for i in range(n):
        solucion[i] = matriz[i][n]

    return solucion


if __name__ == "__main__":
    matriz = [
        [1, -2, 3, 11],
        [4, 1, -1, 4],
        [2, -1, 3, 10]
    ]

    # x1 = 2, x2 = -3, x3 = 1
    solucion = resolver_sistema(matriz)

    print("Solución:")
    for i, valor in enumerate(solucion):
        print(f"x[{i}] = {valor}")