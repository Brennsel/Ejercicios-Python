#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Volver a pedir
Pedir por teclado el nombre de usuario, si
está vacío, volver a pedirlo hasta que se ingrese
un nombre.
Luego, saludar al usuario

"""
nombre = input("Ingrese su nombre: ")

while nombre == "":
    nombre = input("Ingrese su nombre: ")

print("Hola " +nombre)
