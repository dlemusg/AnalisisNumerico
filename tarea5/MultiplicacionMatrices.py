
def ppal():
	print (
	"""	
	El siguiente programa se encarga de multiplicar dos matrices A y B.
	Recordar que en la multiplicacion de matrices el orden si altera el producto, es decir, A*B es diferente que B*A
	""")

	#Creacion Matriz A
	filA = int(input("\nIngrese el numero de filas de la matriz A: "))
	colA = int(input("\nIngrese el numero de columnas de la matriz A: "))
	A = []
	for i in range (filA):
		A.append([0] * (colA))
		for j in range(colA):
			print("Ingrese el numero de la fila ", i ," con columna " , j ," de la matriz A: ")
			m = int(input())
			A[i][j] = m	


	#Creacion Matriz B
	filB=colA
	colB = int(input("\nIngrese el numero de columnas de la matriz B: "))
	B = []
	for i in range (filB):
		B.append([0] * (colB))
		for j in range(colB):
			print("Ingrese el numero de la fila ", i ," con columna " , j ," de la matriz B: ")
			m = int(input())
			B[i][j] = m	


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
	print ("La multiplicacion entre A y B es: ")
	print (N)
pass

ppal()