#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
La lista de alumnos que creamos en el módulo 
anterior ahora debe ser un diccionario, en donde 
las claves serán nombres de alumnos y los 
valores sus respectivas cantidades de cursos. 
Para esto se debe modificar el código de las 
opciones 1 y 2 (agregar un nuevo alumno y ver la 
lista de alumnos).
La tercera opción será “Ver la cantidad de cursos 
de un alumno”. Deberá solicitar el nombre de un 
alumno e imprimir en pantalla el número de 
cursos que tiene asociados como clave. La cuarta 
opción es la de salir, como en la versión anterior. 
Usar todo lo aprendido hasta el momento, el 
programa no debe de frenar de forma imprevista 
a causa de un error. Ya que en el material de 
lectura se vieron todas las posibles soluciones 
frente a los problemas que se puedan presentar. 
"""


alumnos={}
opc = 0

while opc != 4 :
    print("=========================================================")
    print("Ingrese el numero de la operacion que desea ejecutar: ")
    print("1 - Añadir un alumno a la lista.")
    print("2 - Ver la lista de alumnos.")
    print("3 - Ver la cantidad de cursos de un alumno.")
    print("4 - Salir.")
    print("=========================================================")

    opc = int(input(">>>> "))

    if opc==1 :
        nombre = input("Ingrese nombre del alumno: ")
        cursos = int(input("Ingrese la cantidad de cursos en la que se encuentra inscripto: "))
        alumnos[nombre] = cursos
        print("El alumno fue añadido aL diccionario correctamente!")

    elif opc==2 :
        for nombre in alumnos :
            cursos = alumnos[nombre]
            print("Nombre: " + nombre + " - Curso: " + str(cursos))


    elif opc==3 :
        alumnoBuscado = input("Ingrese nombre del alumno: ")

        for nombre in alumnos :
            if alumnoBuscado in nombre :
                print("El alumno " + alumnoBuscado + " se encuentra inscripto en " + str(cursos) + " cursos.")
                break

        else :
                print("El alumno ingresado no se encuentra en la lista.")

    elif opc == 4 :
        print("saliendo...")