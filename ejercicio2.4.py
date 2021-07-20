"""
Ejercicio 2.4

Creamos 4 variables. Lista, string, entero y booleana.
Imprimimos el tipo de variable qué es cada una.

"""

def traducirTipo(elemento):
    if elemento == list:
        return "lista"
    elif elemento == str:
        return "string"
    elif elemento == int:
        return "entero"
    elif elemento == bool:
        return "booleano"
    elif elemento == float:
        return "decimal"
    else:
        return "desconocido"


catalogo = ["",[],0,True,5.6,{},()]

for elemento in catalogo:
    print("El elemento es: ", traducirTipo(type(elemento)))
