"""""
¡Empiezas a trabajar para una nueva empresa elegante que espera revolucionar las redes
sociales! ¡JADEAR! Tuvieron esta gran idea de que los usuarios deberían poder especificar
palabras clave relevantes para sus publicaciones utilizando una idea ingeniosa al anteponer
esas palabras clave con el signo de libra (#). Su trabajo es extraer esas palabras clave para que
puedan usarse más tarde para cualquier propósito.
Nota:
• Los signos de libra por sí solos no cuentan, por ejemplo: la cadena "#" devolvería una
matriz vacía.
• Si una palabra está precedida por más de un hashtag, solo cuenta el último hashtag
(por ejemplo, "##alot" devolvería ["alot"])
• Los hashtags no pueden estar en medio de una palabra (por ejemplo, "hashtag en
#línea" devuelve una matriz vacía)
• Los hashtags deben preceder a los caracteres alfabéticos (por ejemplo, "#120398" o
"#?" no son válidos)
Entrada: cadena de palabras, donde algunas palabras pueden contener un hashtag.
Salida: matriz de cadenas que tenían el prefijo del hashtag, pero que no contienen el hashtag.
"""
def Matriz_de_Hashtag(string):
    #Si cadena viene precedidda de un # Coger dicha cadena. Si elemento tiene la forma: #String return String, o por ej: tiene la forma 
    #: #Str#ing, return [str, ing] eliminar # y devolver string
    while "#" in string:
        lista = list(string)
        lista.remove("#")        
    return lista
Cadena = "#hello#"
print(Matriz_de_Hashtag(Cadena))

