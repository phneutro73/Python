"""
Solicita un valor del radio y nos devuelve el área
"""
import math

def areaCirculo(radio):
    area = math.pi * radio * radio

    return area

numero = int(input("introduce el radio del cículo: "))

print (f"El area del círculo de rádio {numero} es {areaCirculo(numero)}")
