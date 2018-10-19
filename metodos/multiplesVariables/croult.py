from numpy import *
from sympy import *
import math
from tabulate import tabulate

A = [] 
L = []
U = []
B = []
Z = []
X = []
n = 0
def recolectarDatos():
    n = int(input("Ingrese el numero de ecuaciones: "))
    fila = ""
    valores = []
    for i in range(n):
        A.append([0] * n)
        L.append([0] * n)
        U.append([0] * n)    
        fila = str(input("Ingrese los valores de la fila " + str(i+1) + " separados por espacio: "))  #El usuario ingresa los coeficientes de la matriz
        valores = fila.split(" ")
        for j in range(n+1):       #Es n+1 por la columna de terminos independientes
            if j==n:
                B.append(float(valores[j]))
            else:
                A [i][j] = float(valores[j])  #Asignamos a la posicion correspondiente de la matriz los coeficientes"""
    file = open("croult.txt" , "w")
    print("\n    MATRIZ ORIGINAL A")
    file.write("\n    MATRIZ ORIGINAL A \n")
    print(tabulate(A, tablefmt='fancy_grid'))
    file.write(tabulate(A, tablefmt='grid'))
    for i in range(n):
        U[i][i] = 1
    for k in range(n):
        for i in range(k,n):
            sum = 0
            for p in range(k):
                sum += L[i][p]*U[p][k]
            L[i][k] = (A[i][k] - sum)/U[k][k]
        for j in range(k,n):
            sum = 0
            for p in range(k):
                sum += L[k][p]*U[p][j]
            U[k][j] = (A[k][j] - sum)/L[k][k]
    print(" MATRIZ L ")
    file.write("\n    MATRIZ L   \n")
    print(tabulate(L, tablefmt='fancy_grid',floatfmt=".14f"))
    file.write(tabulate(L, tablefmt='grid',floatfmt=".14f"))

    print("  MATRIZ U  ")
    file.write("\n    MATRIZ U   \n")
    print(tabulate(U, tablefmt='fancy_grid',floatfmt=".14f"))
    file.write(tabulate(U, tablefmt='grid',floatfmt=".14f"))

    print("SUSTITUCION PROGRESIVA")
    file.write("\nSUSTITUCION PROGRESIVA\n")
    print("CALCULANDO Lz=B")
    file.write("\nCALCULANDO Lz=B\n")
    for i in range(n):
        Z.append(0)

    Z[0]=(B[0]/L[0][0])
    print("Z1""= "+str(B[0]/L[0][0]))
    file.write("Z1"+"= "+str(B[0]/L[0][0])+"\n")

    for i in range(1,n):
        sum = 0
        for j in range(i+1):
            if i==j:
               temp2 = (B[j]-sum)/L[i][j]
               print("Z"+str(i+1)+"= "+str(temp2))
               file.write("Z"+str(i+1)+"= "+str(temp2)+"\n")
               Z[j]=(temp2)
            else:
                sum += L[i][j]*Z[j]
      
    for i in range(n):
        X.append(0)
    for i in range(n-1,0-1,-1):
        sum = 0
        for j in range(i,n):
           sum += U[i][j]*X[j]
        X[i] = ((Z[i]-sum)/U[i][i])
    
    print("\nSUSTITUCION REGRESIVA\n")
    file.write("\nSUSTITUCION REGRESIVA\n")    
    print("CALCULANDO Ux=Z\n")
    file.write("\nCALCULANDO Ux=Z\n")
    for i in range(n):
        print("X"+str(i+1)+": "+str(X[i]))
        file.write("X"+str(i+1)+": "+str(X[i])+"\n")
    file.close()
            

def printMatriz(matriz):
    for i in matriz:
        print(i)
    
recolectarDatos()
    