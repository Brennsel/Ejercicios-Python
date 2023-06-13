#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pedir nombre

Crear un programa que solicite el nombre de un alumno a través de la
consola, y luego chequee que no esté vacío.

En caso de estarlo tiene que imprimir un mensaje de error; caso 
contrario deberá imprimir un mensajes indicando que se ingresó correctamente.
"""

nombre = input("Ingrese el nombre del alumno: ")

if nombre == "":
    print("Error: no se ingresó un nombre")
else:
        print("Se ingresó correctamente el nombre")