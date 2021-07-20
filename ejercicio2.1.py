"""
Ejercicio 2.1 Programa con una lista de 8 números enteros. Primero mostrar la lista completa. Segundo ordenarla y mostrar su longitud.
Tercero buscar un elemento de la lista introducido por teclado.
"""

import random

lista = []
longitud = random.randint(10,20)

for n in range (longitud):
    lista.append(random.randint(1,10))

numero = int(input("Introduce un numero a buscar: "))

# Primero. Mostramos la lista completa
print (lista,"\n")

#Segundo. Ordenamos la lista y mostramos su longitud
print ("La lista tiene",len(lista),"elementos.\n")
lista.sort()
print (lista)

#Tercero. Buscamos un elemento de la lista
if numero in lista:
    print(f"\nEl {numero} está en la lista en la posicion {lista.index(numero)}")
