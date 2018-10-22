from tabulate import tabulate
import sys
from sympy import *
import numpy as np

x = Symbol('x')

def recolectarDatos():
    n = int(input("Ingrese la dimension de la matriz, es decir, el valor de n: "))
    A = []  
    for i in range(n):
        A.append([0] * (n))   
        fila = str(input("Ingrese los valores de la fila " + str(i+1) + " de la matriz A separados por un espacio: "))
        valores = fila.split(" ")
        for j in range(n):       
            A[i][j] = float(valores[j]) 
    #file = open("valoresPropios.txt" , "w")
    valoresPropios(A, n)

def valoresPropios(A, n):
	print("\n'x' es un valor propio de A si y solo si det(xIn - A) = 0. Por tanto: ")
	if n == 2:
		xIn = [['x',0],[0,'x']]
	elif n == 3:
		xIn = [['x',0,0],[0,'x',0],[0,0,'x']]
	elif n > 3:
		for i in range(n):
			for j in range(n):
				if x==j:
					xIn[i][j]='x'

	#print("det ( ", tabulate(xIn, tablefmt='fancy_grid') ," - ", tabulate(A, tablefmt='fancy_grid'), " )")
	nA = []
	for i in range(n):
		nA.append([0] * (n)) 
		for j in range(n):
			nA[i][j] = expand(sympify(xIn[i][j])-A[i][j])
	print("\nHallamos el determinante de:\n",  tabulate(nA, tablefmt='fancy_grid'))

	det = determinante(nA,n)
	print("\nObtenemos la siguiente igualdad: " , str(det), " = 0")

	g = int(input("Ingrese el grado del polinomio: "))
	P = np.zeros([g+1])
	j = g
	for i in range(g+1):
		P[i] = int(input("Ingrese los coeficientes del término de grado "+ str(j)+ " : "))
		j = j - 1
	
	print("Los valores propios de A se cumple cuando x toma el/los siguiente(s) valores: ")
	print(np.roots(P))


def determinante(A, n):
	if n == 2:
		det = expand((A[0][0]*A[1][1])-(A[1][0]*A[0][1]))
		#print("\ndeterminante de A es: " , str(det))
		return det
	elif n == 3:
		for i in range(n):
			for j in range(n-1):
				A[i].append(A[i][j])
		
		#print("\n   MATRIZ PARA DETERMINANTE de 3*3\n")
		#print(tabulate(A, tablefmt='fancy_grid'))

		contador = 0
		sumaC = 0
		while (contador < n):
			j = contador
			i = 0
			mul = 1
			while (i < n):
				mul = expand(mul * A[i][j])
				i = i + 1
				j = j + 1
			sumaC = expand(sumaC + mul)
			contador = contador + 1

		contador = len(A[0]) - 1
		sumaD = 0
		while (contador >= n-1):
			j = contador
			i = 0
			mul = 1
			while (i < n):
				mul = expand(mul * A[i][j])
				i = i + 1
				j = j - 1
			sumaD = expand(sumaD + mul)
			contador = contador - 1

		det = expand(sumaC - sumaD)
		#print("\ndeterminante de A es: " , str(det))
		return det

	else:
		print("\nEl determinante de A es con esta dimension aun no se puede calcular." )

		
recolectarDatos()