#programa que sume valores ingresador por el usuario
#autor: Juan Camilo Ramirez Urbano
#codigo: 202418301-2725
#fecha: 08/04/2024

continuar="s"
total=0
while continuar=="s":
    cantidad=int(input("Ingrese la cantidad a sumar "))
    print(cantidad)
    total=total+cantidad
    print("total ", total)
    continuar= input("Continuar suma? s/n ")
