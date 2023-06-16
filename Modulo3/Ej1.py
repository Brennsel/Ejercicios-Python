#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribir un programa que guarde en una variable el diccionario
{"Euro": "EUR", "Dolar": "USD", "Pesos": "ARS"}

pregunte al usuario por una divisa y muestre su abreviatura por pantalla.
Si la divisa no existe en el diccionario, dar aviso por pantalla.
"""
#a.title() -> Capitaliza la primera letra de cada palabra

divisas = {"Euro": "EUR", "Dolar": "USD", "Pesos": "ARS"}

divisa = input("Ingrese una divisa: ").title()

if divisa in divisas :  
    print(divisa + " es " + divisas[divisa])
else :
    print("La divisa no existe")

