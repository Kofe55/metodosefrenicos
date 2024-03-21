def jacobi(coeficientes, valores_iniciales, tolerancia, iteraciones_maximas):
    n = len(valores_iniciales)
    solucion = valores_iniciales.copy()
    solucion_anterior = valores_iniciales.copy()
    iteraciones = 0
    error = tolerancia + 1
    
    while error > tolerancia and iteraciones < iteraciones_maximas:
        solucion_anterior = solucion.copy()
        
        for i in range(n):
            suma = 0
            for j in range(n):
                if j != i:
                    suma += coeficientes[i][j] * solucion_anterior[j]
            solucion[i] = (coeficientes[i][-1] - suma) / coeficientes[i][i]
        
        error = sum(abs(solucion[i] - solucion_anterior[i]) for i in range(n))
        iteraciones += 1
    
    if error <= tolerancia:
        return solucion
    else:
        return None

if __name__ == "__main__":
    coeficientes = [
        [4, -3, 2, 6],
        [1, 5, -2, -3],
        [2, -1, 8, -1]
    ]
    valores_iniciales = [0, 0, 0]
    tolerancia = 0.0001
    iteraciones_maximas = 1000
    
    solucion = jacobi(coeficientes, valores_iniciales, tolerancia, iteraciones_maximas)
    
    if solucion is not None:
        print("Solución:")
        for i, x in enumerate(solucion):
            print(f"x[{i}] = {x}")
    else:
        print("El método no converge.")


