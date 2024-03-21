import numpy as np

def resolver_sistema(matriz):
    """
    Resuelve un sistema de ecuaciones lineales utilizando eliminación gaussiana.
    
    Argumentos:
    matriz -- una matriz numpy de dimensiones (n, n+1) que representa el sistema de ecuaciones
    
    Devuelve:
    solucion -- un vector numpy de longitud n con las soluciones del sistema
    """
    n = len(matriz)
    
    # Eliminación hacia adelante
    for i in range(n):
        # Hacer los elementos debajo de la diagonal i-ésima igual a cero
        for j in range(i+1, n):
            factor = matriz[j,i] / matriz[i,i]
            matriz[j,:] -= factor * matriz[i,:]
    
    # Sustitución hacia atrás
    solucion = np.zeros(n)
    for i in range(n-1, -1, -1):
        solucion[i] = matriz[i,n] / matriz[i,i]
        for j in range(i):
            matriz[j,n] -= matriz[j,i] * solucion[i]
    
    return solucion

# Ejemplo de uso
matriz = np.array([[4, 1, -2, 1],
                   [3, 1, 3, 10],
                   [6, 2, 1, 10]])

solucion = resolver_sistema(matriz)

print("Solución:")
for i, x in enumerate(solucion):
    print(f"x[{i}] = {x}")