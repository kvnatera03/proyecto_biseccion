from math import *
    
    # Implementa el Algoritmo de Biseccion y retorna la aproximación.

    # Parámetros:
    # f: función de variable real f(x).
    # a: límite inferior del intervalo.
    # b: límite superior del intervalo.
    # ER: cota mínima del error relativo.
    # N: número máximo de iteraciones.
    

def biseccion (f,a,b,ER,N):

    if (f(a)*f(b))>0 :
        print ("Intervalo no valido")
        return
    error= 100; x_anterior = 0; x_actual=0; n=1;
    while (n<N) and (error>ER):
        m =(a+b)/2.0
        x_actual= m
        error= abs(x_actual-x_anterior)/x_actual
        if (f(a)*f(m)<0):
            b=m
        else:
            a=m
        x_anterior=x_actual
        print ("Iteracion: ",n, " Punto medio: ", x_actual, " Error: ", error)
        n= n + 1
    print (x_actual)
    return x_actual
    
    

if __name__ == "__main__":
    # Pruebe aquí su función.
    f=lambda x: x - cos(x);
    biseccion(f, 0, 1, 0.02, 10)
    pass

