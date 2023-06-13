#!/usr/bin/env python
# -*- coding: utf-8 -*-

lista1 = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista2 = ["Pedro", "Brenda", "Maia"]
lista3 = ["CABA", 3, True, 2.5]

print(lista2)

lista2.append("Juan")
print(lista2)

print(lista1[1]) #muestra elemnto de pos 1
print(lista1[-1]) #muestra el ultimo elemento de la lista

lista2.insert(1, "Juan")   #insert(numero de indice, elemento)
print(lista2)

del lista2[-1] #para eliminar conociendo el indice
print(lista2)

lista2.remove("Brenda") #para eliminar conociendo el elemento

print(len(lista1)) #longitud de la lista

print(lista1[len(lista1)-1]) #muestra el elemneto que se encuentra en la posicion ngitud de la lista menos uno

lista1[0] = 8 #cambia el valor del elemento que se encuentra en esa posicion

ceros = [0] * 10 #lista con los mismos elementos tal cant de veces
print (ceros)

combinada = ceros + lista1 #combinar listas
print (combinada)

caracteres = "Hola" #String son iterables
#caracteres = list("Hola")
print (type(caracteres)) 

contador = 0

while contador < len(caracteres) :
    print(caracteres[contador])
    contador+=1

print(lista1[2:6]) #muestra de la pos 2 a la 6
print(lista1[::2]) #muestra saltando de dos en dos
print(lista1[::-2]) #muestra la lista de atras para adelante saltando de dos en dos

lista5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista5.clear()
print(lista5)

#list unpacking (desempacar lista)

numerosej = [1, 2, 3, 4, 4, 4, 4, 4, 9]
primeros, segundo, *otros = numerosej

print(primeros, segundo)
print(otros)

primero, *otros, ultimo = numerosej
print(primero)
print(otros)
print(ultimo)

numerosej.sort() #ordena de menor a mayor
numerosej.sort(reverse=True)

