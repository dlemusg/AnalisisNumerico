from numpy import *
from sympy import *
from tabulate import tabulate

def recolectarDatos():
    n = int(input("Ingrese el numero de ecuaciones: "))  #Conociendo el numero de ecuaciones, conoceremos las dimensiones de la matriz
    A = []   #En primera instacia creamos una lista que posteriormente se convertira en una matriz
    L = []
    for i in range(n):
        A.append([0] * (n+1))    #Se le agregan n+1 columnas a la matriz por los terminos independientes
        L.append([0] * (n+1)) 
        fila = str(input("Ingrese los valores de la fila " + str(i+1) + " separados por espacio: "))  #El usuario ingresa los coeficientes de la matriz
        valores = fila.split(" ")
        for j in range(n+1):       #Es n+1 por la columna de terminos independientes
            A [i][j] = float(valores[j])  #Asignamos a la posición correspondiente de la matriz los coeficientes
            if(j == n):
                L[i][j] = float(valores[j])

    file = open("gaussianaSimple.txt" , "w")
    eliminacionGaussianaSimple(A, n, file,L)

def eliminacionGaussianaSimple(A,n,file,L):
    print("\n    MATRIZ ORIGINAL A")
    file.write("\n    MATRIZ ORIGINAL A \n")
    print(tabulate(A, tablefmt='fancy_grid'))
    file.write(tabulate(A, tablefmt='grid'))
    L[0][0] = 1
    for k in range(1,n):
        print("\nETAPA " + str(k) + "\nObjetivo: Poner ceros bajo el elemento A" + str(k) + str(k) + " = " + str(A[k-1][k-1]) + "\n")
        file.write("\nETAPA " + str(k) + "\nObjetivo: Poner ceros bajo el elemento A" + str(k) + str(k) + " = " + str(A[k-1][k-1]) + "\n")
        for i in range(k, n):
            multiplicador = float(A[i][k-1]/A[k-1][k-1])
            print("\nM" + str(i+1) + str(k) + " = " + str(multiplicador))
            file.write("\nM" + str(i) + str(k) + " = " + str(multiplicador) + '\n')
            L[i][k-1] = multiplicador
            L[i][i] = 1
            for j in range(k,n+2):
                A[i][j-1] = A[i][j-1] - multiplicador*A[k-1][j-1]

            print(tabulate(A, tablefmt='fancy_grid',floatfmt=".14f"))
            file.write(tabulate(A, tablefmt='grid',floatfmt=".14f"))
    print("\n Matriz TRIANGULAR INFERIOR L")
    file.write("\nMatriz TRIANGULAR INFERIOR L\n")
    print(tabulate(L, tablefmt='fancy_grid',floatfmt=".14f"))
    file.write(tabulate(L, tablefmt='fancy_grid',floatfmt=".14f"))
    print("\n   MATRIZ TRIANGULAR SUPERIOR U\n")
    file.write("\n   MATRIZ TRIANGULAR SUPERIOR U\n")
    print(tabulate(A, tablefmt='fancy_grid',floatfmt=".14f"))
    file.write(tabulate(A, tablefmt='grid',floatfmt=".14f"))
    sustitucionRegresiva(A,n,file)
    sustitucionProgresiva(L,n)

def sustitucionProgresiva(L, n):
    print("\n SUSTITUCIÓN PROGRESIVA\n")
    z = []
    for i in range(n):
       z.append(0)
    
    for i in range(n):
        sumatoria = 0
        for j in range(i):
            sumatoria += L[i][j]*z[j]
        z[i] = L[i][n]-sumatoria
        print("Z" + str(i+1) + " = " + str(z[i]))

    

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
    file.close()


def imprimirMatriz(A, n):
    for i in range(n):
        print(str(A[i]).replace("'"," ").replace(","," "))

recolectarDatos()