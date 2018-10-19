from numpy import *
from sympy import *
from tabulate import tabulate

def recolectarDatos():
    n = int(input("Ingrese el numero de ecuaciones: "))  #Conociendo el numero de ecuaciones, conoceremos las dimensiones de la matriz
    L = []   #En primera instacia creamos una lista que posteriormente se convertira en una matriz
    U = []
    for i in range(n):
        L.append([0] * (n))    #Se le agregan n+1 columnas a la matriz por los terminos independientes
        U.append([0] * (n+1))
        fila = str(input("Ingrese los valores de la fila " + str(i+1) + " separados por espacio, no olvide agregar la igualdad de cada ecuación: "))  #El usuario ingresa los coeficientes de la matriz
        valores = fila.split(" ")
        for j in range(n+1):       #Es n+1 por la columna de terminos independientes
            U [i][j] = float(valores[j])  #Asignamos a la posición correspondiente de la matriz los coeficientes
    file = open("factorizacionLUconGaussianaSimple.txt" , "w")
    factorizacionLUconEliminacionGaussianaSimple(U, n, file, L)

def factorizacionLUconEliminacionGaussianaSimple(U,n,file, L):
   
    print("\n    MATRIZ ORIGINAL A")
    file.write("\n    MATRIZ ORIGINAL A \n")
    print(tabulate(U, tablefmt='fancy_grid'))
    file.write(tabulate(U, tablefmt='grid'))
    for k in range(1,n):
        #print("\nETAPA " + str(k) + "\nObjetivo: Poner ceros bajo el elemento A" + str(k) + str(k) + " = " + str(U[k-1][k-1]) + "\n")
        #file.write("\nETAPA " + str(k) + "\nObjetivo: Poner ceros bajo el elemento A" + str(k) + str(k) + " = " + str(U[k-1][k-1]) + "\n")
        for i in range(k, n):
            multiplicador = float(U[i][k-1]/U[k-1][k-1])
            #print("\nM" + str(i) + str(k) + " = " + str(multiplicador))
            #file.write("\nM" + str(i) + str(k) + " = " + str(multiplicador) + '\n')
            for j in range(k,n+2):
                U[i][j-1] = U[i][j-1] - multiplicador*U[k-1][j-1]
                matrizL(i,j,multiplicador, L)             

            #print(tabulate(U, tablefmt='fancy_grid'))
            #file.write(tabulate(U, tablefmt='grid'))

    for x in range(len(L)):
        for z in range(len(L[x])):
            if x == z:
                L[x][z] = 1

    print("\n   MATRIZ U\n")
    file.write("\n   MATRIZ U\n")
    print(tabulate(U, tablefmt='fancy_grid'))
    file.write(tabulate(U, tablefmt='grid'))
    sustitucionRegresiva(U,n,file)
    print("\n   MATRIZ L\n")
    file.write("\n   MATRIZ L\n")
    print(tabulate(L, tablefmt='fancy_grid'))
    file.write(tabulate(L, tablefmt='grid'))
    sustitucionProgresiva(L,n,file)

def matrizL(i, j, multiplicador, L):
    if i>=j:
        L[i][j-1] = multiplicador


def sustitucionRegresiva(A,n,file):
    print("\n SUSTITUCIÓN REGRESIVA\n")
    file.write("\n SUSTITUCION REGRESIVA\n")
    x = []
    for i in range(n):
        x.append([0])

    for i in range(n,0,-1):
        sumatoria = 0
        for p in range(i+1, n+1, 1):
            sumatoria += A[i-1][p-1]*x[p-1]
        x[i-1] = (A[i-1][n] - sumatoria)/ A[i-1][i-1]
        print("X" + str(i) + " = " + str(x[i-1]))
        file.write("X" + str(i) + " = " + str(x[i-1]))
    

def sustitucionProgresiva(A,n,file):
    print("\n SUSTITUCIÓN PROGRESIVA\n")
    file.write("\n SUSTITUCION PROGRESIVA\n")
    x = []
    a = len(A)
    for i in range(n):
        x.append([0])

    for i in range(0,int(a/2),n):
        sumatoria = 0
        for p in range(i, len(A[i]), n):
            sumatoria += A[i-1][p-1]*x[p-1]
        x[i-1] = (A[i-1][n] - sumatoria)/ A[i-1][i-1]
        print("X" + str(i) + " = " + str(x[i-1]))
        file.write("X" + str(i) + " = " + str(x[i-1]))
    file.close()


def imprimirMatriz(A, n):
    for i in range(n):
        print(str(A[i]).replace("'"," ").replace(","," "))

recolectarDatos()