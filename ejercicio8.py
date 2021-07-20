'''
Ejercicio 8. Programa que calcula el % de un numero introducido
'''

numero = int(input("Introduce la cantidad total: "))
porcentaje = int(input("Introduce el porcentaje a calcular: "))

if porcentaje <= 0 or porcentaje >=100:
    print("El porcentaje debe estar comprendido entre 1 y 99")
    exit
else:
    print (f"El {porcentaje}% de {numero} es", (numero*porcentaje/100))