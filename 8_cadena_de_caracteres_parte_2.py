#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ----------------------------------
#  CADENA DE CARACTERES(Parte 2)
# ---------------------------------

# Slicing ponemos des de un indice hasta un indice de un caracter NO incluido
# imprimiendo palabras de acuerdo a su posicion en la cadena
txt = "Seguimos trabajando con Strings"

print(txt[8:19])
print(txt[23:])
print(txt[-7:])
print(txt[-7:-1])
print(txt[-11:-1])


# TRABAJANDO CON MINUSCULAS (achicamos o agrandamos el texto)
txt2 = "CUANDO ESCROBO EN MAYUSCULAS TODO CREEN QUE GRITO"

minusculas = txt2.lower()
print(minusculas)

minuscolas = minusculas.upper()
print(minusculas)


# CORREGIMOS ESPACIOS EN CADENAS DE TEXTO
# Strip corrige los espacios en las cadenas

txt3 = "              Uy! me dejé espacios antes y despues            "
textoimportante = "clave "


textocorregido = txt3.strip()
textocorregido2 = textoimportante.strip()

print (textocorregido)
print (textocorregido2)
















