#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Texto (str)
variable1 = "Texto"
variable2 = "123456"
variable3 = "Texto123"

# Numericas (int , float, complex)

variable4 = 10
variable5 = 2.5
variable6 = 1j

# casteo de str a int
variablecasteada = int(variable2)

# casteo de int a str
variablecasteada2 = int(variable4)

print(type(variable1)) # <class 'str'>
print(type(variablecasteada)) # <class 'str'>
print(type(variable3)) # <class 'str'>
print(type(variablecasteada2)) # <class 'int'>
print(type(variable5)) # <class 'float'>´
print(type(variable6)) # <class 'complex'> 


# -----------------------------------------------
#  como se castea? (cambiar de tipo de dato)
# tipoDeDato("el dato original")
# Con type podemos saber que tipo de dato es el que estamos manajando
# -----------------------------------------------

tupla = ("manzana", "pera", "naranja")
list = list(tupla)

print(type(list))


