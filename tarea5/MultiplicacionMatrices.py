
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

ppal()