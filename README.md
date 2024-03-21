### METODO NUMERICOS

Aqui se presentan 5 ejmplos de los 4 metodos de solucion de sistemas de ecuaciones.

- ELIMINACION GAUSSIANA

- GAUSS-JORDAN

- GAUSS-JACOBI

- GAUSS-SEIBEL

El método de eliminación Gauss-Jordan consiste en representar el sistema de ecuaciones por medio de una matriz y obtener a partir de ella lo que se define como la matriz escalonada equivalente, a través de la cual se determina el tipo de solución de la ecuación.

Para resolverlo podemos seguir los siguientes pasos:

Escriba la matriz aumentada del sistema de ecuaciones lineales.
Use operaciones elementales de fila para llevar la matriz aumentada a una forma escalonada.
Mediante sustitución regresiva, resuelva el sistema equivalente correspondiente a la matriz aumentada escalonada.
Ejemplo
- ![image](https://github.com/Kofe55/metodosefrenicos/assets/160757569/ca38388f-eecd-4d0f-8280-4c3c35c5a0dc)

SOLUCION

LA MATRIZ A RESOLVER
![image](https://github.com/Kofe55/metodosefrenicos/assets/160757569/fd3ebc29-660c-47c1-a356-e21e09da1396)
}![image](https://github.com/Kofe55/metodosefrenicos/assets/160757569/8be16af4-7d96-4af9-8656-a94ec90e1b18)

De la tercera fila se obtiene 2z=2, es decir, z=1. De la segunda fila obtenemos y=-1. Finalmente de la primera fila se obtiene x+2y+z=0, es deci, x=1.

Concluimos que la solución del sistema de ecuaciones es:

x=1 y=−1 z=1

El método de Gauss-Jordan utiliza operaciones con matrices para resolver sistemas de ecuaciones de n numero de variables. Para aplicar este método solo hay que recordar que cada operación que se realice se aplicara a toda la fila o a toda la columna en su caso.

Para resolverlo podemos seguir los siguientes pasos:

Divide todo el primer renglón entre la componente a11.
Convierte todos los demás valores de esa columna en ceros:
Al segundo renglón (R2) se le restará el primer renglón multiplicado por la componente a21.
Al tercer renglón (R3) se le restará el primer renglón multiplicado por la componente a31.
Divide todo el segundo renglón entre la componente a22.
Repite todo el proceso para las demás columnas hasta obtener la forma deseada.
Ejemplo
Matriz a resolver:

![image](https://github.com/Kofe55/metodosefrenicos/assets/160757569/3dfab715-bbf8-4c11-8bf8-6f229fea658c)

Solución
Como primer paso dividimos el primer renglón R1 entre la componente a11:

![image](https://github.com/Kofe55/metodosefrenicos/assets/160757569/96b90610-dca8-4ba3-9aa6-b51786da9021)

Como segundo paso se requiere «convertir» las componentes inferiores de la componente a11 en ceros (0):

![image](https://github.com/Kofe55/metodosefrenicos/assets/160757569/15a7cea6-067b-437b-9055-571918cccf60)

Al tercer renglón (R3) se le restará el primer renglón multiplicado por la componente a31.

![image](https://github.com/Kofe55/metodosefrenicos/assets/160757569/1dc098c4-b33e-49c1-82ed-d9957ca516bc)

Se procede a dividir el segundo renglón R2 entre la componente a22 :

![image](https://github.com/Kofe55/metodosefrenicos/assets/160757569/a9bcf537-115c-4088-aa19-88518f0970d8)

Ahora se repite todo el proceso para las demás columnas hasta obtener la forma deseada.

![image](https://github.com/Kofe55/metodosefrenicos/assets/160757569/a55f8db4-b428-4b51-9f0e-d9a711bd2e72)














