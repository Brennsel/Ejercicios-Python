#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Escribir un programa que almancene las materias de un curso en una lista:

- Matematicas
- Fisica
- Quimica
- Historia

Se debe preguntar al usuario que notas ha sacado en cada materia y después se 
debe mostrar por pantalla el siguiente mensaje:

"En <materia> sacaste <nota>".
"""

materias = ["matematica", "fisica", "quimica", "historia"]
notas = []

contador = 0
aux = 0

while contador < len(materias) :
    
    notas.append(input("Ingrese la nota que saco en " + materias[contador] +":"))
    
    contador+=1

while aux < len(materias) :

    print("En " + materias[aux] + "sacaste " + notas[aux])
    aux+=1


