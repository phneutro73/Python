"""
Ejecicio 2.3
Si una variable está vacía nos pregunta por un valor para rellenarla. El valor lo guarda en minúsculas pero lo muestra en mayúsculas.
"""

variable = ""

if len(variable.strip()) <= 0:
    variable = input("Introduce un valor para la variable: ")
    variable = variable.lower()

print (variable.upper())