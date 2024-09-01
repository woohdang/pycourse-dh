#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TIPOS DE DATOS

# -------------------------------
# Texto
# -------------------------------

# - str (Cadena de caracteres)
texto = "Cadena de Caracteres"


# --------------------------------
# NUMEROS
# --------------------------------

# - int (entero)
numero_entero = 10

# - float(Flotante)
numero_flotante = 3.14

# - complex (complejos)
numero_complejo = 2 + 3j


# -------------------------------
# SECUENCIA
# -------------------------------

# - list(lista) [coleccion ordenada y mutable]
lista = [1,2,3,4]


# - tuple (tupla) [coleccion ordenada y inmutable]
tupla = (1,2,3,4)

# -range(rango) [secuencia inmutable de numeros]
rango = range(0,10)


# -------------------------------
# MAPPING TYPE (MAPEO)
# -------------------------------

# - dict (diccionario) [coleccion no ordenada de pares clave-valor (simil Ojeto JS)]
# Se recomienda usarlo asi con salto de linea
diccionario = { 
    "nombre": "Gaston", 
    "Edad": 41, 
    "Direccion": "Avda. combate de los pozos"
    }

# -------------------------------
# SET TYPES (CONJUNTO)
# -------------------------------

# - set (conjunto) [coleccion no ordenada y mutable de elementos UNICOS(no permite repetir)]
conjunto = {1,2,3,4}

# - frozenset (conjunto inmutable) [conjunto inmutable]
conjunto_inmutable = frozenset({1,2,3,4})

# -------------------------------
# BOOLEAN TYPES (BOOLEANO)
# -------------------------------

# - boolean [puede ser verdadero o falso]
booleano = True
booleano = False

# -------------------------------
# BINARY TYPES (BINARIO)
# -------------------------------

# - bytes [representa una secuencia inmutable de bytes]
bytes_data = b"datos"

# -bytearray (array de bytes) [una secuencia mutable de bytes]
bytearray_data = bytearray(b"datos")

# - memoryview (vista de memoria) [permite acceder a la memoria de objeto de bytes sin hacer copia]
memoria = memoryview(b"datos")


# -------------------------------
# NONE /NULL (NULL)
# -------------------------------

# - none type (nulo) [Representa la ausencia de valor o la no definicion]
nulo = None;


