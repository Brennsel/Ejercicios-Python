#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Escribir una función que calcule el total de una factura
 tras aplicarle el IVA.
La función debe recibir por parámetro la cantidad SIN iva
 y el porcentaje del impuesto a aplicar.
 Finalmente debe devolver el total del valor de la factura.

Si se invoca la función sin pasarle el porcentaje de IVA,
 deberá aplicar por defecto el 21%
"""

def factura(cantidad, iva = 0.21):
    return cantidad + cantidad * iva

monto = 2000
print("monto: $" , monto)
print("monto con iva: $" ,factura(monto))
