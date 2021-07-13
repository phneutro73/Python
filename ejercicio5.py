"""
Ejercicio 5. Muestra todos los números entre dos números
introducidos por el usuario
"""

numero1=int(input("Introduce el primer número: "))
numero2=int(input("Introduce el segundo número: "))

for num in range(numero1 + 1, numero2):
    print (num)