#!/usr/bin/env python
# -*- coding: utf-8 -*-

lista1 = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista2 = ["Pedro", "Brenda", "Maia"]
lista3 = ["CABA", 3, True, 2.5]

print(lista2)

lista2.append("Juan")
print(lista2)

lista2.insert(1, "Juan")   #insert(<numero de indice, elemento>)
print(lista2)

del lista2[-1] #para eliminar conociendo el indice
print(lista2)

#lista2.remove() #para eliminar conociendo el elemento

print(len(lista1)) #longitud de la lista

print(lista1[len(lista1)-1])


