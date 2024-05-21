#Primer programa de python con arreglos
#autor: Juan Camilo Ramirez Urbano
#codigo: 202418301-2725
#fecha: 21/05/2024
import math

nota1=[1, 2, 3, 4, 5, 0, 4, 3, 2, 1]
print(nota1)
suma=0
for numero in nota1:
    suma+=numero

    promedio=suma/len(nota1)

print("El promedio es: ",promedio)
print("El mayor valor es ", max(nota1))
print("El menor valor es ", min(nota1))