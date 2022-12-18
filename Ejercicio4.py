"""""
En algunos países de la antigua Unión Soviética existía la creencia de los boletos de la
suerte. Se creía que un billete de transporte de cualquier tipo traía suerte si la suma de los
dígitos de la mitad izquierda de su número era igual a la suma de los dígitos de la mitad
derecha. Aquí hay ejemplos de tales números:
003111 # 3 = 1 + 1 + 1
813372 # 8 + 1 + 3 = 3 + 7 + 2
17935 # 1 + 7 = 3 + 5 // si la longitud es impar, debes ignorar el número del medio al
sumar las mitades.
56328116 # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6
Dichos boletos se comían después de usarlos o se recolectaban para fanfarronear.
Su tarea es escribir una función luck_check(str), que devuelve true/Truesi el argumento es una
representación decimal de cadena de un número de boleto de la suerte, o false/Falsepara
todos los demás números. Debería arrojar errores para cadenas vacías o cadenas que no
representan un número decimal.
"""
def luck_check(string):
    #Si la longitud de la cadena es par, sumar los dos primeros elementos de la cadena y los dos ultimos elementos de la cadena
    #Si la longitud de la cadena es impar, sumar los dos primeros elementos de la cadena y los dos ultimos elementos de la cadena
    #Si la suma de los dos primeros elementos de la cadena es igual a la suma de los dos ultimos elementos de la cadena, return True
    #Si la suma de los dos primeros elementos de la cadena no es igual a la suma de los dos ultimos elementos de la cadena, return False
    if len(string) % 2 == 0:
        if string[0] + string[1] == string[-2] + string[-1]:
            return True
        else:
            return False
    else:
        if string[0] + string[1] == string[-2] + string[-1]:
            return True
        else:
            return False
print(luck_check("2130"))