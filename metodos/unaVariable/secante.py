from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from tabulate import tabulate

f = Function('fx')
tabla = []

def recolectarDatos():
    global f, fil
    fil = open('secante.txt', 'w')
    f = parse_expr(input("Ingrese la función f(x) a ser evaluada: "))
    x0 = float(input("Ingrese el valor inicial x0: "))
    x1 = float(input("Ingrese el segundo valor x1: "))
    tolerancia = 0
    while (tolerancia <= 0):
    	tolerancia = float(input("Ingrese la tolerancia: "))
    	if tolerancia <= 0:
    		print("La tolerancia debe ser mayor que 0")
    	
     
    niteraciones = 0
    while (niteraciones<=0):
    	niteraciones = int(input("Ingrese el numero maximo de iteraciones: " ))
    	if niteraciones <= 0:
    		print("El numero de iteraciones debe ser mayor que 0")
    

    print("")
    print("")
    fil.write("---SECANTE---\n\n")
    print("---VERIFICACION---")
    fil.write("---VARIABLES---\n")
    print("f(x) = ",f)
    fil.write("f(x) = "+str(f)+"\n")
    print("intervalos [x0, x1] = " , "[ " + str(x0)+ ", ", str(x1),"]")
    fil.write("intervalos [x0, x1] = " + "[" + str(x0)+ ", "+ str(x1)+ "]"+"\n")
    print("Tolerancia = ",tolerancia)
    fil.write("Tolerancia = "+str(tolerancia)+"\n")
    print("Iteraciones = ",niteraciones)
    fil.write("Iteraciones = "+str(niteraciones)+"\n")
    print("")
    fil.write("\n")

    metodoSecante(x0, x1, tolerancia, niteraciones)

def metodoSecante(x0, x1, tolerancia, niteraciones):
	x = Symbol('x')
	fx0 = f.subs(x, x0)
	if fx0==0:
		print (str(x0) + " es una raiz de f(x)")
		pass
	else:
		fx1 = f.subs(x, x1)
		contador = 0
		tabla.append([str(contador),str(x0),str(fx0)])
		contador = 1
		tabla.append([str(contador),str(x1),str(fx1)])
		minus = fx1 - fx0
		errorAbs = tolerancia + 1
		while (errorAbs > tolerancia and fx1 != 0 and minus != 0 and contador < niteraciones):
			x2 = x1 - ((fx1 * (x1 - x0))/minus)
			errorAbs = abs(x2 - x1)
			x0 = x1
			fx0 = fx1
			x1 = x2
			fx1 = f.subs(x, x1)
			minus =  fx1 - fx0
			contador = contador + 1

			tabla.append([str(contador),str(x1),str(fx1),str(errorAbs)])
			

		
		if fx1 == 0:
			fil.write(tabulate(tabla, headers=['i', '(xn)','f(xn)','Error Absoluto'],tablefmt='grid',floatfmt=".17f"))
			print(tabulate(tabla, headers=['i', '(xn)','f(xn)','Error Absoluto'],tablefmt='grid',floatfmt=".17f"))
			print()
			print (str(x1) + " es una raiz de f(x)")
			fil.write(str(x1) + " es una raiz de f(x)")
		elif (errorAbs<tolerancia):
			fil.write(tabulate(tabla, headers=['i', '(xn)','f(xn)','Error Absoluto'],tablefmt='grid',floatfmt=".17f"))
			print(tabulate(tabla, headers=['i', '(xn)','f(xn)','Error Absoluto'],tablefmt='grid',floatfmt=".17f"))
			print()
			print(str(x1) + " se aproxima a una raiz de f(x), con una tolerancia de: " + str(tolerancia))
			fil.write('\n'+str(x1) + " se aproxima a una raiz de f(x), con una tolerancia de: " + str(tolerancia))
		elif minus == 0:
			print("En la funcion f(x) hay una posible raiz multiple")
			fil.write("En la funcion f(x) hay una posible raiz multiple")
		else:
			print("FALLO, exedio el numero  maximo de iteraciones")
			fil.write("FALLO, exedio el numero  maximo de iteraciones")
		fil.close()


recolectarDatos()