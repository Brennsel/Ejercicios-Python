#!/usr/bin/env python
# -*- coding: utf-8 -*-

letras = ["a", "b", "c", "d"]

for letra in letras :
    if letra == "a":
        pass              #saltear
    else:
        print(letra)

nombres = ["Julian", "alicia", "Jose"]

for nombre in nombres :
    if nombre.capitalize().startswith("A") : #empieza con
        print("Encontre que " +nombre+ " empieza con A")
        break
else :
     print("No encontre ningun nombre con A")