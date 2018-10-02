from numpy import *
from sympy import *
from tabulate import tabulate

def recolectarDatos():
    n = int(input("Ingrese el numero de ecuaciones: "))  #Conociendo el numero de ecuaciones, conoceremos las dimensiones de la matriz
    A = []   #En primera instacia creamos una lista que posteriormente se convertira en una matriz
    for i in range(n):
        A.append([0] * (n+1))    #Se le agregan n+1 columnas a la matriz por los terminos independientes
        fila = str(input("Ingrese los valores de la fila " + str(i+1) + " separados por espacio: "))  #El usuario ingresa los coeficientes de la matriz
        valores = fila.split(" ")
        for j in range(n+1):       #Es n+1 por la columna de terminos independientes
            A [i][j] = float(valores[j])  #Asignamos a la posición correspondiente de la matriz los coeficientes
    file = open("GaussianaPivoteoParcial.txt" , "w")
    eliminacionGaussianaPivoteoParcial(A, n, file)

def eliminacionGaussianaPivoteoParcial(A,n, file):
    print("\n    MATRIZ ORIGINAL A")
    file.write("\n    MATRIZ ORIGINAL A \n")
    print(tabulate(A, tablefmt='fancy_grid'))
    file.write(tabulate(A, tablefmt='grid'))
    #imprimirMatriz(A,n)
    for k in range(1,n):
        print("\nANTES DEL PIVOTEO PARCIAL\n")
        file.write("\nANTES DEL PIVOTEO PARCIAL\n")
        #imprimirMatriz(A,n)
        print(tabulate(A, tablefmt='fancy_grid'))
        file.write(tabulate(A, tablefmt='grid'))
        A = pivoteoParcial(A,n,k-1)
        print("\nDESPUES DEL PIVOTEO PARCIAL\n")
        file.write("\nDESPUES DEL PIVOTEO PARCIAL\n")
        print(tabulate(A, tablefmt='fancy_grid'))
        file.write(tabulate(A, tablefmt='grid'))
        print("\nETAPA " + str(k) + "\nObjetivo: Poner ceros bajo el elemento A" + str(k) + str(k) + " = " + str(A[k-1][k-1]) + "\n")
        file.write("\nETAPA " + str(k) + "\nObjetivo: Poner ceros bajo el elemento A" + str(k) + str(k) + " = " + str(A[k-1][k-1]) + "\n")
        for i in range(k, n):
            multiplicador = float(A[i][k-1]/A[k-1][k-1])
            print("\nM" + str(i) + str(k) + " = " + str(multiplicador))
            file.write("\nM" + str(i) + str(k) + " = " + str(multiplicador) + '\n')
            for j in range(k,n+2):
                A[i][j-1] = A[i][j-1] - multiplicador*A[k-1][j-1]

            #imprimirMatriz(A,n)
    print("\n   MATRIZ TRIANGULAR SUPERIOR\n")
    file.write("\n   MATRIZ TRIANGULAR SUPERIOR\n")
    print(tabulate(A, tablefmt='fancy_grid'))
    file.write(tabulate(A, tablefmt='grid'))
    sustitucionRegresiva(A,n, file)

def pivoteoParcial(A,n,k):
    mayor = abs(A[k][k])
    filaMayor = k
    for s in range(k+1,n):
        if abs(A[s][k]) > mayor:
            mayor = abs(A[s][k])
            filaMayor = s
    if mayor == 0:
        return ("El sistema no tiene solución única")
    else:
        if filaMayor != k:
            A = intercambieFilas(A,filaMayor,k)
        return A

def intercambieFilas(A,filaMayor,k):
    for i in range(len(A[0])):
        aux = A[k][i]
        A[k][i] = A[filaMayor][i]
        A[filaMayor][i] = aux
    return A

def sustitucionRegresiva(A,n, file):
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
