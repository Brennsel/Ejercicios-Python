#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1) Buscar multiplos de 3 y 5 en un rango que ingrese el usuario.

Hacer que el valor de fin este incluido dentro del rango

2) Guardar los múltiplos en una lista
"""

inicio = int(input("Ingrese el valor de inicio del rango: "))
fin = int(input("Ingrese el valor final del rango: "))

multiplos = []

for i in range(inicio, fin+1) :
    if i%3 == 0 or i%5 == 0 :
        multiplos.append(i)

print("Los multiplos de 3 y 5 son: " + str(multiplos))

        