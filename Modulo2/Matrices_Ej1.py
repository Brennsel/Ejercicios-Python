#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crea un programa que solicite una fila y una columna e imprima en
pantalla el numero en esa posicion segun la siguiente matriz:

matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
"""

matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

fila = int(input("Ingrese numero de fila: "))
columna = int(input("Ingrese numero de columna: "))

if fila<0 or fila>1 or columna<0 or columna>2:
    print("Ingreso erroneo")
else :
    print("El valor de esa posicion es :" + str(matriz[fila][columna]))

