#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribir un programa que reciba un string y que devuelva otra lista con 
cada palabra que contenga como items separados dentro de la lista.

Escribir otra función que reciba la nueva lista generada y 
elimine las palabras repetidas. 

frase = "Como quieres que te quiera si el que quiero que me quiera 
no me quiere como quiero que me quiera"

"""


frase = "como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"



def separar(frase):
    return frase.split(" ")


def eliminar_repetidos(lista):
    set(lista)
    return lista


lista = separar(frase)
print(lista)
print(eliminar_repetidos(lista))
