import numpy as np

def resolver_sistema(matriz):
    """
    Resuelve un sistema de ecuaciones lineales utilizando el método de Gauss-Jordan.
    
    Argumentos:
    matriz -- una matriz numpy de dimensiones (n, n+1) que representa el sistema de ecuaciones
    
    Devuelve:
    solucion -- un vector numpy de longitud n con las soluciones del sistema
    """
    n = len(matriz)
    
    # Convertir la matriz a una forma escalonada reducida por filas (forma escalonada reducida por Gauss-Jordan)
    for i in range(n):
        # Dividir la fila i-ésima para que el elemento diagonal sea igual a 1
        divisor = matriz[i, i]
        matriz[i, :] /= divisor
        
        # Hacer cero los elementos por encima y por debajo del elemento diagonal
        for k in range(n):
            if k != i:
                factor = matriz[k, i]
                matriz[k, :] -= factor * matriz[i, :]
    
    # Extraer la solución del sistema de ecuaciones de la última columna
    solucion = matriz[:, n]
    
    return solucion

# Ejemplo de uso
matriz = np.array([[2, 3, 4, 20],
                   [3, -5, -1, -10],
                   [-1, 2, -3, -6]])

solucion = resolver_sistema(matriz)

print("Solución:")
for i, x in enumerate(solucion):
    print(f"x[{i}] = {x}")