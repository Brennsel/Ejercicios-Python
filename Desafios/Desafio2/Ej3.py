#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escriba un programa que permita crear una lista
de nombres.
Para ello, el programa tiene que pedir un número
y luego solicitar esa cantidad de nombres para
crear la lista. Por último, el programa tiene que
mostrar la lista creada. 
"""

cant = int(input("Ingrese la cantidad: "))

nombres=[]

while cant > 0 :
    nombres.append(input("Ingrese un nombre: "))
    cant = cant-1

print("\nLista de nombres")

for nombre in nombres :
    print(nombre)