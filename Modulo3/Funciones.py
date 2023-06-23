#!/usr/bin/env python
# -*- coding: utf-8 -*-

#FUNCIONES
#def nombre(parametros):

"""
#Ejemplo 1
simbolos = ["ALUA", "BBAR", "BMA", "SUPV"]
precios = [337, 999.5, 1288.45, 303]

def imprimir(lista):
    for elemento in lista:
        print(elemento)

print("\nSimbolos:")
imprimir(simbolos)

print("\nPrecios:")
imprimir(precios)
"""

#Ejemplo 2

def suma(num1, num2):
    return num1 + num2


resultado_suma = suma(2, 3)
print(resultado_suma)

#PYTHON ENHANCEMENT PROPOSAL (PEP)

#minimo y maximo

def min_y_max(lista):
    a= min(lista)
    b= max(lista)
    return [a,b]


print(min_y_max(1, 2, 3, 4, 5))