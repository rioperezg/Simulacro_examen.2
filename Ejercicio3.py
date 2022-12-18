"""""
La secuencia de Fibonacci se usa tradicionalmente para explicar la recursividad del árbol.
function fibonacci(n) {
 if(n==0 || n == 1)
 return n;
 return fibonacci(n-1) + fibonacci(n-2);
}
Este algoritmo cumple bien su propósito educativo pero es tremendamente ineficiente , no
solo por la recursividad, sino porque invocamos la función de Fibonacci dos veces, y la rama
derecha de la recursividad (ie fibonacci(n-2)) recalcula todos los números de Fibonacci ya
calculados por la rama izquierda (ie fibonacci(n-1)) .
Este algoritmo es tan ineficiente que el tiempo para calcular cualquier número de Fibonacci
por encima de 50 es simplemente demasiado. Puedes ir por una taza de café o ir a dormir una
siesta mientras esperas la respuesta. Pero si lo intenta aquí en Code Wars, lo más probable es
que obtenga un código de tiempo de espera antes de cualquier respuesta.
Para este Kata en particular, queremos implementar la solución de memorización . Esto será
genial porque nos permitirá seguir usando el algoritmo de recursión de árbol mientras lo
mantenemos lo suficientemente optimizado para obtener una respuesta muy rápidamente.
El truco de la versión memorizada es que mantendremos una estructura de datos de caché
(probablemente una matriz asociativa) donde almacenaremos los números de Fibonacci a
medida que los calculamos. Cuando se calcula un número de Fibonacci, primero lo buscamos
en el caché, si no está allí, lo calculamos y lo ponemos en el caché, de lo contrario, devolvemos
el número almacenado en caché.
Refactorice la función en una función de Fibonacci recursiva que, al usar una estructura de
datos memorizada, evita las deficiencias de la recursividad del árbol. ¿Puedes hacer que la
memoria caché sea privada para esta función?
"""
# El truco de la versión memorizada es que mantendremos una estructura de datos de caché
# (probablemente una matriz asociativa) donde almacenaremos los números de Fibonacci a
# medida que los calculamos. Cuando se calcula un número de Fibonacci, primero lo buscamos
# en el caché, si no está allí, lo calculamos y lo ponemos en el caché, de lo contrario, devolvemos
# el número almacenado en caché.
def fibonacci(n):
    # La serie de fibonacci empieza en 1 y es sumando el termino mas el anterior de forma recursiva como es la serie de fibonacci
    # entonces: el primer termino es 1, el segundo es 2, y el tercero es 1 + 2, el cuarto es 3 + 2, el quinto es 5 + 3etc....
    Terms_Suce = []
    for i in range(n):
        if i == 0:
            Terms_Suce.append(1)
        elif i == 1:
            Terms_Suce.append(1)
        else:
            Terms_Suce.append(Terms_Suce[i - 1] + Terms_Suce[i - 2])
    return Terms_Suce
print(fibonacci(10))
 

