#Puntos = [(x1,y1),(x2,y2)]
import numpy as np
def Vandermonde(puntos):
    A = []
    b = []
    auxA = []
    n = len(puntos)
    for punto in puntos:
        b.append(punto[1])
        for i in range(1,n+1):
            auxA.append(punto[0]**(n-i))
        A.append(auxA)
        auxA = []
    return A,b
    
puntos = [(1,0.5949),
        (2,0.2622),
        (3,0.6028),
        (4,0.7112),
        (5,0.2217),
        (6,0.1174),
        (7,0.2967),
        (8,0.3188),
        (9,0.4242),
        (10,0.5079)]

A,b = Vandermonde(puntos)
print(np.linalg(A,b))
print(Vandermonde(puntos))