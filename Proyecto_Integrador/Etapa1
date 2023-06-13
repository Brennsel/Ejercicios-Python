#!/usr/bin/env python
# -*- coding: utf-8 -*-

alumnos=[]
opc = 0

while opc != 3 :
    print("=========================================================")
    print("Ingrese el numero de la operacion que desea ejecutar: ")
    print("1 - Añadir un alumno a la lista.")
    print("2 - Ver la lista de alumnos.")
    print("3 - Salir.")
    print("=========================================================")

    opc = int(input(">>>> "))

    if opc==1 :
        nombre = input("Ingrese nombre del alumno: ")
        cursos = int(input("Ingrese la cantidad de cursos en la que se encuentra inscripto: "))
        alumnos.append([nombre, cursos])
        print("El alumno fue añadido a la lista correctamente!")

    elif opc==2 :
         for alumno in alumnos :
            print("Nombre: " + alumno[0] + " - Curso: " + str(alumno[1]))

    elif opc == 3 :
        print("¡Gracias por utilizar el programa!")

    else :
         print("La opcion ingresada no es correcta, vuelva a intentarlo.")