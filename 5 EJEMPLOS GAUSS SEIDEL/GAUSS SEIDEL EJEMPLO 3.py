import numpy as np

def gauss_seidel(coeficientes, valores_iniciales, tolerancia, iteraciones_maximas):
    n = len(valores_iniciales)
    solucion = np.array(valores_iniciales, dtype=float)
    solucion_anterior = np.zeros_like(solucion)
    iteraciones = 0
    error = tolerancia + 1

    while error > tolerancia and iteraciones < iteraciones_maximas:
        # Copiar la solución anterior
        solucion_anterior[:] = solucion

        # Calcular la nueva solución
        for i in range(n):
            suma = sum(coeficientes[i, j] * solucion[j] for j in range(n) if j != i)
            solucion[i] = (coeficientes[i, n] - suma) / coeficientes[i, i]

        # Calcular el error
        error = np.sum(np.abs(solucion - solucion_anterior))
        iteraciones += 1

    # Verificar la convergencia
    if error <= tolerancia:
        return solucion
    else:
        return None  # No converge

if __name__ == "__main__":
    coeficientes = np.array([
        [2, -1, 0, 3],
        [1, -2, 1, -3],
        [1, 1, -3, -4]
    ])

    # x1 = 4.666628841128849, x2 = 6.333290640897843, x3 = 4.999973160675563
    valores_iniciales = [0, 0, 0]  # Valores iniciales de las incógnitas
    tolerancia = 0.0001  # Tolerancia para el criterio de convergencia
    iteraciones_maximas = 1000  # Número máximo de iteraciones

    solucion = gauss_seidel(coeficientes, valores_iniciales, tolerancia, iteraciones_maximas)

    if solucion is not None:
        print("Solución:")
        for i, valor in enumerate(solucion):
            print(f"x[{i}] = {valor}")
    else:
        print("El método no converge.")