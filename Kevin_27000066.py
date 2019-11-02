#!/usr/bin/env python3
"""
Proyecto en Python sobre el Algoritmo de Bisección.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

import math



def biseccion(f, a, b, ER, N):
    vOri = {
      "cont": 1,
      "eRel": 100,
      "pAct": 0,
      "pPre": 0
    }

    fOri = lambda x1, x2 : f(x1)*f(x2)
    lOri = lambda x1, x2 : (x1+x2)/2
    def messfOri(): print("#Error: limites incorrectos!")

    if fOri(a, b) > 0: 
        messfOri()
        return

    while (vOri["cont"] < N) & (vOri["eRel"] > ER):
        vOri["pPre"] = vOri["pAct"]
        vOri["pAct"] = lOri(a,b)

        if fOri(vOri["pAct"], b) > 0:
            b = vOri["pAct"]
        else:
            a = vOri["pPre"]    
     
        if vOri["cont"] > 1:
            vOri["eRel"] = abs((vOri["pAct"]-vOri["pPre"])/vOri["pAct"])

        i = vOri["cont"]
        pm_act = vOri["pAct"]
        err = vOri["eRel"]
        print("Iteración:", i, "Punto Medio:", pm_act, "Error:", err) 
        vOri["cont"] += 1

    return vOri["pAct"]


if __name__ == "__main__":
    # Pruebe aquí su función.
    f = lambda x: x**2 - math.cos(x)
    biseccion(f, 0.2, 1, 0.16, 10)
    pass
