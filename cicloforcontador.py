#programa que imprime los multiplos de 3 en una serie 1 a n
#autor: Juan Camilo Ramirez Urbano
#codigo: 202418301-2725
#fecha: 01/04/2024

n=int(input("Digite un número entero "))
contador=0
for i in range (1,n):
    if (i%3==0):
        contador=contador+1

print ("Entre 1 y", n, " hay ", contador, "multiplos")

        
