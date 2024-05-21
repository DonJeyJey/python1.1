#Ejemplo de uso de libreria math
#autor: Juan Camilo Ramirez Urbano
#codigo: 202418301-2725
#fecha: 08/04/2024


import math
a=-5
b=3.4646485118645
base=2
c=math.sqrt (base)
exp=7
print ("valor absoluto de ", a , "es ", abs(a),)
print("ceil de ",b, "es ", math.ceil(b))
print("floor de ",b, "es ", math.floor(b))
print("round de ",b, "es ", round(b,3))
print("la potencia ", exp, "de ", base, "es ", math.pow(base, exp))
print("La raiz cuadrada de ",base, "es ",round(c,2))
print("El entero mayor de los valores absolutos es ", max(abs(a),round(abs(b), round(abs(c)))))
print("El mayor entre A, b, c es",max('A','b','c'))
print("El mayor entre 'Z', 'B', 'C' es",max('Z','B','C'))
n1="Peter"
n2="Pedro"
n3="paola"
print("El mayor entre ",n1, n2, n3, " es",max(n1,n2,n3))
n1="Luis"
n2="Pedro"
n3="Ana"
print("El menor entre ",n1, n2, n3, " es",min(n1,n2,n3))
print(math.pi)
