#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""
Escribir un programa que pida al usuario una palabra y muestre por pantalla
el número de veces que contiene cada vocal
"""
vocales = ["a", "e", "i", "o", "u"]
numeroDeVeces = [0]*5

palabra = input("Ingrese una palabra: ")

for letra in palabra :

    cant = 0

    for vocal in vocales :

        if letra == vocal :
           
           numeroDeVeces[cant]+=1

        cant+= 1

print(numeroDeVeces)
cant = 0

for vocal in vocales :

    print("La letra " +vocales[cant]+ " se repite " +str(numeroDeVeces[cant]))
    cant+=1



    





            

