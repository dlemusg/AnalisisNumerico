from numpy import * 
from sympy import *
from tabulate import tabulate

def recolectarDatos():
    n = int(input("Ingrese el numero de ecuaciones: "))#Conociendo el numero de ecuaciones, conoceremos las dimensiones de la matriz
    A = []
    B = []
    L = []
    U = []
    for i in range(n):
        A.append([0] * (n))    #Se le agregan n+1 columnas a la matriz por los terminos independientes
        L.append([0]*n)
        U.append([0]*n)
        fila = str(input("Ingrese los valores de la fila " + str(i+1) + " separados por espacio: "))  #El usuario ingresa los coeficientes de la matriz
        valores = fila.split(" ")
        for j in range(n):       #Es n+1 por la columna de terminos independientes
            A [i][j] = float(valores[j])  #Asignamos a la posición correspondiente de la matriz los coeficientes
    columnas = str(input("Ingrese los valores de B separados por espacio: "))
    val = columnas.split(" ")
    for j in range(n):
        B.append(float(val[j]))
    print("\nMATRIZ ORIGINAL A")
    print(tabulate(A, tablefmt='fancy_grid',floatfmt=".14f"))
    print("\nMATRIZ ORIGINAL B")
    print(B)

    factorizacionLU(A, L, U, B, n)

def factorizacionLU(A,L,U,B,n):
    for k in range (n):
        for i in range(k,n):
            if(i == k):
                sumatoria = 0
                for p in range(k):
                    sumatoria += L[k][p]*U[p][k]
                L[k][k] = (A[k][k] - sumatoria)**(1/2)
            else:
                sumatoria = 0
                for p in range(k):
                    sumatoria += L[i][p]*U[p][k]
                L[i][k]= (A[i][k]-sumatoria)/L[k][k]
        for j in range(k,n):
            if( j == k):
                U[k][k] = L[k][k]
            else:
                sumatoria = 0
                for p in range(k):
                    sumatoria += L[k][p]*U[p][j]
                U[k][j]= (A[k][j]-sumatoria)/L[k][k]
        print("\nETAPA"+str(k+1))
        print("\nMATRIZ L\n")
        print(tabulate(L, tablefmt='fancy_grid',floatfmt=".14f"))
        print("\nMATRIZ U\n")
        print(tabulate(U, tablefmt='fancy_grid',floatfmt=".14f"))
    sustitucionProgresiva(L,B,U,n)     

def sustitucionProgresiva(L,B,U, n):
    print("\nSUSTITUCION PROGRESIVA")   
    print("CALCULANDO Lz=B")
    Z = []
    for i in range(n):
        Z.append(0)
    Z[0]=(B[0]/L[0][0])
    print("Z1""= "+str(Z[0]))
    for i in range(1,n):
        sum = 0
        for j in range(i+1):
            if i==j:
               Z[j] = (B[j]-sum)/L[i][j]
               print("Z"+str(i+1)+"= "+str(Z[j]))
            else:
                sum += L[i][j]*Z[j]
    sustitucionRegresiva(U,Z,n)
        
def sustitucionRegresiva(U,Z, n):
    print("\nSUSTITUCION REGRESIVA")   
    print("CALCULANDO Ux=Z")
    X = []
    for i in range(n):
        X.append(0)
    for i in range(n-1,0-1,-1):
        sum = 0
        for j in range(i,n):
           sum += U[i][j]*X[j]
        X[i] = ((Z[i]-sum)/U[i][i])
    
    for i in range(n):
        print("X"+str(i+1)+": "+str(X[i]))

recolectarDatos()