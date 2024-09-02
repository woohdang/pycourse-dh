#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ----------------------------------
#  CADENA DE CARACTERES(Parte 3)
# ---------------------------------

# Concatenación de cadenas

a = "Hola"
b= "Mundo!"
c = a + " " + b

print(c)


# concatenación de numeros con cadenas
# la doble llave permite insertar valores numericos en la concatenacion

horas = 10
clases = 60
txt = "El contenido de este curso va durar: {} horas y tendrá {} clases"

print(txt.format(horas, clases)) # "El contenido de este curso va durar: 10 horas y tendra 60 clases"

# Se puede ordenar la salida indicando los indices en las llaves
txt2 = "El contenido de este curso va durar: {1} horas y tendrá {0} clases"

print(txt2.format(clases, horas)) # "El contenido de este curso va durar: 10 horas y tendra 60 clases"


# -----------------------------------
# PONER COMILLAS
# -----------------------------------

# usamos escape de caracteres

# \t Tabulado
# \n Salto de linea

txt4 = "La mejor serie que vi en mi vida es:\t GAME OF THRONES"

txt5 = "La mejor serie que vi en mi vida es:\n GAME OF THRONES"

print(txt4)

print(txt5)












