"""
En este programa definimos una función que nos saca la tabla de multiplicar del númoer introducido
"""

def tabla_multiplicar(numero):
    print(f"La tabla del {numero} es:\n")
    for n in range (10):
        print(f"{numero} * {n+1}\t= {(n+1)*int(numero)}")
        
caracter = ""

while caracter != "0":
    caracter = input("Introduce un numero: ")
    if caracter.isdigit() and caracter != "0":
        tabla_multiplicar(caracter)
    