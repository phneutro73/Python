"""
Ejercicio 6. Mostramos todas las tablas de multiplicar del 1 al 10
"""

numero=1

for num in range(1,11):
    print(f"### TABLA DEL {num} ###")
    for i in range (1,11):
        print (f"{i} * {num}\t=",i*num)
    print("")