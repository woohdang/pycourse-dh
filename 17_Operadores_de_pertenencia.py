#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ----------------------------
# 6. OPERADORES DE PERTENENCIA
# ----------------------------

# in

# not in

texto = "En este texto pondremos algunas tecnologias: Python, R, Django y TensorFlow"
texto = texto.lower()

textominusculas = texto.lower()
# Strip quita los espacios ylower deja todo en minusculas antes de hacer la pregunta
aBuscar = "    TENsorFLOw       ".strip().lower()


print(aBuscar in textominusculas)

print("Django" not in texto)

print("TensorFlow" in texto)