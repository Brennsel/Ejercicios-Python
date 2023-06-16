#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Listas
1) Tuplas - Tuples
2) sets
3) Diccionario

#a = set(numeros)
#b = {1, 5}

#tuple
#la tupla es inmutable (no se puede modificar) y se define con parentesis

print(a | b) #union
print(a & b) #interseccion
print(a - b) #diferencia
print(a ^ b) #diferencia simetrica


#Operador ternario

#msj = valor1 if condicion else valor2

"""
"""

print("==========================")

edad = 22

if edad >= 18:
    msj = "Es mayor de edad"
else:
    msj = "Es menor de edad"

print(msj)

print("==========================")
#otra forma de hacerlo

mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"

print(mensaje)

print("==========================")

#Diccionario

#pares de clave-valor

persona ={"nombre" : "brenda", "telefono" : "123456789"}
print(persona["nombre"], persona["telefono"])

otra_persona = dict(nombre = "martin", telefono = "1123674433")
print(otra_persona["nombre"])

otra_persona["nombre"] = "maia"
print(otra_persona["nombre"])

otra_persona[direccion] = "baigorria 123"
print(otra_persona["direccion"])

del otra_persona["direccion"]
print(otra_persona)

for clave in otra_persona:
    print(clave, otra_persona[clave])  
"""
print("==========================")

#range

#range(inicio, fin, salto)

print(range(1, 11))

for i in range(1, 11):
    print(i)






