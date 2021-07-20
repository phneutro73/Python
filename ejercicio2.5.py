"""
Ejercicio 2.5
Crear un diccionario con el contenido de esta tabla:

ACCION  AVENTURA    DEPORTES
----------------------------
GTA     Assassins   FIFA
COD     CRASH       NBA
PUGB    Prince      MotoGP

Mostrar esta información ordenada por categorías
"""

juegos = {
    "GTA":"ACCION",
    "Assasins":"AVENTURA",
    "FIFA":"DEPORTES",
    "COD":"ACCION",
    "Crash":"AVENTURA",
    "NBA":"DEPORTES",
    "PUGB":"ACCION",
    "Prince":"AVENTURA",
    "MotoGP":"DEPORTES"
}

for elemento in juegos:
    print(elemento)