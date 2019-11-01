#!/usr/bin/env python3
"""
Proyecto en Python sobre el Algoritmo de Bisección.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""
import math

def biseccion(f, a, b, ER, N):
    """
        Implementa el Algoritmo de Biseccion y retorna la aproximación.

        Parámetros:
        f: función de variable real f(x).
        a: límite inferior del intervalo.
        b: límite superior del intervalo.
        ER: cota mínima del error relativo.
        N: número máximo de iteraciones.
    """
    errAnt = None
    errAct = None
    cont = 1
    while (cont <= N):
        if(cont == 1):
            print("Iteración:", cont, "Punto Medio:", m(a, b))
        else:
            print("Iteración:", cont, "Punto Medio:", m(a, b), "Error:", er(errAct, errAnt))
            if(ER >= er(errAct, errAnt)):
                return m(a, b)
        errAnt = m(a, b)
        a, b = rango(a, m(a, b), b)
        errAct = m(a, b)
        cont = cont + 1

    return m(a, b)



#Determina el rango en el cual se realiza el cambio de signo
rango = lambda a,b,c: [a,b] if (f(a)*f(b)) < 0 else [b,c]

#Función de variable real f(x)
f = lambda x: math.e**x - 3*(x**2)

#Valor medio
m = lambda a,b: (a+b)/2

#Error relativo
er = lambda a,b: math.fabs((a-b)/a)


if __name__ == "__main__":

    m = biseccion(f, 0, 1, 0.03, 100)
    
    print("="*25)
    print("Raiz:", m)
    print("Evaluamos: f(m):", f(m))
