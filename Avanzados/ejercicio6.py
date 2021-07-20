"""
Obtener un conjunto aleatorio de numeros y crear una lista
"""

import random

lista = []

for elemento in range(25):
    lista.append(random.randint(1,10))

print (lista)