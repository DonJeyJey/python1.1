#programa que calcula promedio general
#autor: Juan Camilo Ramirez Urbano
#codigo: 202418301-2725
#fecha: 08/04/2024

continuar= "s"
p1=0
p2=0
lab=0
trafin=0
defint= 0

while (continuar == "s") or (continuar == "S"):
    p1=int(input("Escribe nota de parcial uno "))
    p2=int(input("Escribe nota de parcial dos"))
    lab=int(input("Escribe nota de laboratorio "))
    trafin=int(input("Escribe nota de trabajo final "))
    defint= (p1 *0.30) + (p2 *0.35) + (lab *0.25) + (trafin *0.10)
    