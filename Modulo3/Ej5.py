#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribir un programa que almacene los vectores (1, 2, 3) y (-1, 0, 2) en
dos tuplas y muestre por pantalla su producto escalar.
"""

vector1 = (1, 2, 3)
vector2 = (-1, 0, 2)

productoEscalar = 0

for i in range(len(vector1)) :
    productoEscalar += vector1[i] * vector2[i]

print("El producto escalar de los vectores es: ", productoEscalar)