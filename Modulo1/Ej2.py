#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Comparar la entrada del usuario

Que permita ingresar dos cadenas via consola y luego las compare
imprimiendo un mensaje en caso que sean iguales y otro en caso
que sean diferentes
"""

cadena1 = input("Ingrese la primer cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

if cadena1 == cadena2:
    print("Las cadenas son iguales")
else:
    print("Las cadenas son diferentes")