#!/usr/bin/env python
# -*- coding: utf-8 -*-

#SCOPE ----> Ambito

"""
Dentro del ambito tenemos

1) Variables locales se declaran dentro del ambito de una funcion
2) Variables globales se declaran dentro del ambito de un archivo

(no existe ambito de bloque)
"""

"""
#Ejemplo 1
mensaje = "Hola"  #variable global

def saludo():
    global mensaje
    mensaje = "Chau"  #variable local

saludo()
print(mensaje)

"""

#Ejemplo 2

def funcion_externa():
    x = "Hola" #variable local

    def funcion_interna():
        nonlocal x #nonlocal es para que tome la variable local de la funcion externa
        x = "a todos"
    
    funcion_interna()
    print(x)

funcion_externa()

