"""
Ejercicio 2.2
Programa que añade valores a una lista mientras la longitud sea < 120 y mostrarlo por pantalla
"""

import random

lista = []
resultado = ""

for n in range (120):
    lista.append(random.randint(1,100))

for elemento in lista:
    resultado += str(elemento) + ", "

print (resultado)