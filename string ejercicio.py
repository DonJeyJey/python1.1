#Ejemplo de uso de libreria math
#autor: Juan Camilo Ramirez Urbano
#codigo: 202418301-2725
#fecha: 08/04/2024

import string
num_1=30
print(str(num_1))

cadena="Cali sucursal del cielo"
print(len(cadena))
#ejemplo string
n1="Alexandra"
n2="PEDRO"
n3="     Pedro    "
n4="      MArTinez     "
n5=n3.strip()+' '+n4.strip().title()
#for i in n1:
 #   print(i)
print(n5)
print(len(n3+n4))
#cuantos caracteres
print(n1,"tiene",len(n1),"caracteres")
print(n2,"tiene",len(n2),"caracteres")
print(n3,"tiene",len(n3),"caracteres")
print(n2,"en minusculas",n2.lower())
print(n1,"en mayusculas",n1.upper())
print(n3,"sin espacios tiene ",len(n3.strip()),"caracteres")

#index()
n1="hola Mundo"
print(n1.index("M"))
#count()
print(n1.count("o"))

n2="alharaca"
print(n2.index("c"))
print(n2.count("a"))