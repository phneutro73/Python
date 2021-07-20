"""
Obtener la representación inversa de una cadena de caracteres
"""

cadena = input("Introduce una cadena de caracteres: ")

lista = []
textoAlreves = ""

for letra in cadena:
    lista.append(letra)

lista.reverse()

for letra in lista:
    textoAlreves += letra
 
print (textoAlreves)

