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
    
puntos = [(-2,12.13533528),(-1,6.367879441),(2,-4.610943901),(3,2.085536923)]
A,b = Vandermonde(puntos)
print(np.linalg.solve(A,b))