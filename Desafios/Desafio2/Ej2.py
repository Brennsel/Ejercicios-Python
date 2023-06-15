#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A la derecha vemos un diagrama de flujo de
cómo se hace para calcular un año bisiesto. La
idea es llevar este algoritmo a código Python.

"""

a = int(input("Ingrese el año: "))

if a % 400 == 0 :
    print("ES BISIESTO")
elif a % 4 == 0 and a % 100 != 0 :
    print("ES BISIESTO")
else :
    print("NO ES BISIESTO")