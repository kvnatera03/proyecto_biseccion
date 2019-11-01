#!/usr/bin/env python3
"""
Proyecto en Python sobre el Algoritmo de Bisección.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math



def biseccion(f, a, b, ER, N):
    i = 1
    err = 100
    pm_actual = 0
    pm_previa = 0

    if f(a)*f(b) < 0:
     while (i < N) & (err > ER):
      pm_previa = pm_actual
      pm_actual = (a+b)/2
      fr = f(pm_actual)*f(b)

      if fr > 0:
       b = pm_actual
      else:
       a = pm_previa
     
      if i > 1:
       err = abs((pm_actual-pm_previa)/pm_actual)

      print("Iteración:", i, "Punto Medio:", pm_actual, "Error:", err) 
      i=i+1

    else:
     print("#Error: Los limites superior e inferior no son validos")

    return pm_actual


if __name__ == "__main__":
    # Pruebe aquí su función.
    f = lambda x: x**2 - math.cos(x)
    biseccion(f, 0.2, 1, 0.16, 10)
    pass
