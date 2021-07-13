"""
Ejercicio 7. Muestra todos los números impares entre dos números introducidos por el usuario
"""

numero1=int(input("Introduce un número: "))
numero2=int(input("Introduce otro número: "))

if numero1 < numero2:
    
    for n in range(numero1, numero2 + 1):
        if n%2 != 0:    
            print(n)
else:
    print("El primer número debe ser inferior al primero")