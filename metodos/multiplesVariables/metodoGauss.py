from numpy import *
from sympy import *
import math

def recolectarDatos():
    n = int(input("Ingrese el numero de ecuaciones: "))
    tolerancia = float(input("Ingrese la tolerancia: "))
    niter = int(input("Ingrese el numero maximo de iteraciones: "))
    A = []   #En primera instacia creamos una lista que posteriormente se convertira en una matriz
    x0 = [] #Lista de los valores inciales de la variables
    b = [] #Vector de terminos independientes
    for i in range(n):
        A.append([0] * n)    #Se le agregan n+1 columnas a la matriz por los terminos independientes
        fila = str(input("Ingrese los valores de la fila " + str(i+1) + " separados por espacio y además el termino independiente: "))  #El usuario ingresa los coeficientes de la matriz
        valores = fila.split(" ")
        for j in range(n+1):       #Es n+1 por la columna de terminos independientes
            if j==n:
                b.append(float(valores[j]))
            else:
                A [i][j] = float(valores[j])  #Asignamos a la posición correspondiente de la matriz los coeficientes

    for i in range(n):
        inicial = float(input("Ingrese el valor inicial de x" + str(i+1) + ": "))
        x0.append(inicial)

    metodoGaussSeidel(A, b, n, x0, niter,tolerancia)


def metodoGaussSeidel(A, b, n, x0, niter, tolerancia):
    contador = 0
    dispersion = tolerancia + 1
    x1 = []
    mayor = 2
    print("\nOrden de los datos: n, x1, x2, x3, ... xn, dispersion " )
    print(str(contador) + "    " + str(x0) + "\n")
    while dispersion >= tolerancia and contador < niter:
        x1 = calcularNuevoGauss(x0, n, b, A)
        dispersion = norma(x1, x0,n)        
        if dispersion >= tolerancia:
            x0 = x1
            contador += 1
            print(str(contador) + "   " + str(x0) + "   " + str(dispersion) + "\n")
            

    if dispersion < tolerancia:
        print(str(x0) + " es una aproximación con una tolerancia: " + str(tolerancia))
    else:
        print("Fracaso en " + str(niter) + " iteraciones")


def calcularNuevoGauss(x0, n, b, A):
    x1 = x0[:]

    for i in range(n):
        suma = 0.0
        for j in range(n):
            if j != i:
                
                valor = x1[j]
                suma += A[i][j] * valor              


        valor = b[i]
        elemento = (valor - suma)/A[i][i]        
        x1.pop(i)
        x1.insert(i,elemento)
        
    return x1 

def norma(x1, x0, n):
    #mayor = -1
    norma = 0
    dividiendo = 0
    divisor = 0
    for i in range(n):
        valor0 = x0[i]
        valor1 = x1[i]
        #if(abs(valor1 - valor0) > mayor):
        #    mayor = abs(valor1 - valor0)
        dividiendo += (valor1-valor0)**2
        divisor += (valor1**2)
    norma = abs(math.sqrt(dividiendo)) / abs(math.sqrt(divisor))
    return norma

recolectarDatos()