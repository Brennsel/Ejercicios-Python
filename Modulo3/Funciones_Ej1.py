#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribir una función que reciba una lista de números y devuelva
otra lista con sus cuadrados
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cuadrados = []

def cuadrado(lista):
    for numero in lista:
        cuadrados.append(numero ** 2)
    return cuadrados

print(cuadrado(numeros))

