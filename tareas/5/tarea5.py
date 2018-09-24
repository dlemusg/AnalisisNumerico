from numpy import *
from sympy import *
from tabulate import tabulate
def inicio():
	print("Bienvenido")
	print("ingrese el numero de la acción")
	a = input("ingrese 1. para multiplicación de matrices\n 3.para gaussiana simple")
	if(a == 1):
		ppal()
	if(a == 3):
		recolectarDatos()

def ppal():
	print (
	"""	
	El siguiente programa se encarga de multiplicar dos matrices A y B.
	Recordar que en la multiplicacion de matrices el orden si altera el producto, es decir, A*B es diferente que B*A
	""")

	#Creacion Matriz A
	A = []
	filA = int(input("\nIngrese el numero de filas de la matriz A: "))
	colA = int(input("\nIngrese el numero de columnas de la matriz A: "))
	i=0
	while i<filA:
		f = input("\nIngrese los numeros de la fila "+ str(i)+ " separados por un espacio: ").split()
		if len(f) > colA:
			print("La dimension de los datos es diferente a la establecida")
		elif len(f) == colA:
			for j in range(len(f)):
				f[j] = float(f[j])
			A.append(f)
			i = i+1
		else:
			print("Faltan datos")

	print()
	print ("Matriz A: " , A)


	#Creacion Matriz B
	B = []
	filB=colA
	colB = int(input("\nIngrese el numero de columnas de la matriz B: "))	
	i=0
	while i<filB:
		f = input("\nIngrese los numeros de la fila "+ str(i)+ " separados por un espacio: ").split()
		if len(f) > colB:
			print("La dimension de los datos es diferente a la establecida")
		elif len(f) == colB:
			for j in range(len(f)):
				f[j] = float(f[j])
			B.append(f)
			i = i+1
		else:
			print("Faltan datos")

	print()
	print ("Matriz B: " , B)

	function(A,B)
pass


def function(A, B):
	A = A[:]  
	B = B[:] 

	filN = len(A)
	colN = len(B[0])
	N = []
	for i in range(filN):
		N.append([0] * (colN))
		for j in range(colN):
			N[i][j] = 0
			for k in range(len(A[0])):
				N[i][j] = N[i][j] + (A[i][k] * B[k][j])
			pass

	print ()
	print ("La multiplicacion entre A y B es: ", N)
pass

def recolectarDatos():
    n = int(input("Ingrese el numero de ecuaciones: "))  #Conociendo el numero de ecuaciones, conoceremos las dimensiones de la matriz
    A = []   #En primera instacia creamos una lista que posteriormente se convertira en una matriz
    for i in range(n):
        A.append([0] * (n+1))    #Se le agregan n+1 columnas a la matriz por los terminos independientes
        fila = str(input("Ingrese los valores de la fila " + str(i+1) + " separados por espacio: "))  #El usuario ingresa los coeficientes de la matriz
        valores = fila.split(" ")
        for j in range(n+1):       #Es n+1 por la columna de terminos independientes
            A [i][j] = float(valores[j])  #Asignamos a la posición correspondiente de la matriz los coeficientes
    file = open("gaussianaSimple.txt" , "w")
    eliminacionGaussianaSimple(A, n, file)

def eliminacionGaussianaSimple(A,n,file):
    print("\n    MATRIZ ORIGINAL A")
    file.write("\n    MATRIZ ORIGINAL A \n")
    print(tabulate(A, tablefmt='fancy_grid'))
    file.write(tabulate(A, tablefmt='grid'))
    for k in range(1,n):
        print("\nETAPA " + str(k) + "\nObjetivo: Poner ceros bajo el elemento A" + str(k) + str(k) + " = " + str(A[k-1][k-1]) + "\n")
        file.write("\nETAPA " + str(k) + "\nObjetivo: Poner ceros bajo el elemento A" + str(k) + str(k) + " = " + str(A[k-1][k-1]) + "\n")
        for i in range(k, n):
            multiplicador = float(A[i][k-1]/A[k-1][k-1])
            print("\nM" + str(i) + str(k) + " = " + str(multiplicador))
            file.write("\nM" + str(i) + str(k) + " = " + str(multiplicador) + '\n')
            for j in range(k,n+2):
                A[i][j-1] = A[i][j-1] - multiplicador*A[k-1][j-1]

            print(tabulate(A, tablefmt='fancy_grid'))
            file.write(tabulate(A, tablefmt='grid'))
    print("\n   MATRIZ TRIANGULAR SUPERIOR\n")
    file.write("\n   MATRIZ TRIANGULAR SUPERIOR\n")
    print(tabulate(A, tablefmt='fancy_grid'))
    file.write(tabulate(A, tablefmt='grid'))
    sustitucionRegresiva(A,n,file)

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


inicio()