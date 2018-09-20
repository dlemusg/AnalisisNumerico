from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

f = Function('fx')

def recolectarDatos():
    global f
    f = parse_expr(input("Ingrese la función f(x) a ser evaluada: "))
    x0 = input("Ingrese el valor inicial x0: ")
    x1 = input("Ingrese el segundo valor x1: ")
    tolerancia = 0;
    while (tolerancia <= 0):
    	tolerancia = int(input("Ingrese la tolerancia: "))
    	if tolerancia <= 0:
    		print("La tolerancia debe ser mayor que 0")
    	pass
     
    niteraciones = 0
    while (niteraciones<=0):
    	niteraciones = int(input("Ingrese el numero maximo de iteraciones: " ))
    	if niteraciones <= 0:
    		print("El numero de iteraciones debe ser mayor que 0")
    	pass

    metodoSecante(x0)


def metodoSecante(x0):
	x = Symbol('x')
	fx0 = f.subs(x, x0)
	print(fx0)




	#str_expr = "x**2 + 3*x - 1/2"
	#expr = sympify(str_expr)
	pass

recolectarDatos()