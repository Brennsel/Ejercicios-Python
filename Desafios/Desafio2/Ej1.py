#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Se preguntará el tipo de rol que desempeña una
persona en una institución por una entrada del
tipo input. Los valores posibles son “admin” o
“profesor”.
Luego si la persona es “admin” o “profesor”, se
debería pedirla contraseña, siendo la única válida
“1234” (la contraseña se toma como string). Si
la contraseña ingresada es válida, se procederá a
pedir el nombre de la persona, y si no es vacío, se
lo saludará.
Contemplar los casos donde no se cumple como
corresponde y mostrar un mensaje en pantalla.

"""

rol = input("Ingrese su rol en la institucion: ")

if rol == "admin" or rol == "profesor":
    contraseña = input("Ingrese su contraseña: ")
    if contraseña == "1234":
        nombre = input("Ingrese su nombre: ")
        if nombre != "":
            print("Hola " + nombre)
        else:
            print("No se ingresó un nombre")
    else:
        print("Contraseña incorrecta")
else: 
    print("Rol incorrecto")
