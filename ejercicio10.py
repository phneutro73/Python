'''
Ejercicio 10. Programa que pide la nota de 15 alunmos y devuelve cuantos han aprobado y cuentos han suspendido
'''

alumnos=[]
aprobados=0
suspensos=0
numero_alumnos=int(input("Introduce el número de alumnos: "))

for nota in range (numero_alumnos):
    alumnos.append(float(input(f"Introduce la nota del alumno {nota + 1}: ")))

for alumno in alumnos:
    if alumno >= 5:
        aprobados += 1
    else:
        suspensos += 1

print (f"Los aprobados han sido {aprobados} y los suspensos {suspensos}")
