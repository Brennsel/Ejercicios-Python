#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1) Almacenar en una lista los siguientes precios
50, 75, 46, 22, 80, 65, 8
2) Muestre por pantalla el menor y mayor de los precios

"""

precios = [50, 75, 46, 22, 80, 65, 8]

"""
for i in range(len(precios)) :
    for j in range(i+1, len(precios)) :
        if precios[i] > precios[j] :
            aux = precios[i]
            precios[i] = precios[j]
            precios[j] = aux


#print("El menor precio es: " + str(min(precios)))
#print("El mayor precio es: " + str(max(precios)))
"""

precios.sort()
print("El menor precio es: ", precios[0])
print("El mayor precio es: ", precios[-1])
