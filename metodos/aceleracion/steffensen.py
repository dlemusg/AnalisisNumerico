from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from tabulate import tabulate

f = Function('fx')
g = Function('gx')

tabla = []

def recolectarDatos():
    global f,g,fil
    fil = open('steffensen.txt', 'w')
    f = parse_expr(input("Ingrese f(x): "))
    g = parse_expr(input("Ingrese g(x): "))
    xi = float(input("Ingrese la aproximacion inicial: "))
    tolerancia = float(input("Ingrese la tolerancia: "))

    while (tolerancia == 0):
        print("ERROR, La tolerancia debe ser diferente de 0")
        tolerancia = float(input("Ingrese la tolerancia: "))

    iteracion = int(input("Ingrese el numero maximo de iteraciones: " ))
    print("\n")

    while (iteracion<0):
        print("El numero de iteraciones debe ser mayor que 0, ingreselo nuevamente")
        iteracion = int(input("Ingrese el numero maximo de iteraciones: "))

    fil.write("---PUNTO FIJO---\n\n")
    print("---VERIFICACION---")
    fil.write("---VARIABLES---\n")
    print("f(x) = ",f)
    fil.write("f(x) = "+str(f)+"\n")
    print("g(x) = ",g)
    fil.write("g(x) = "+str(g)+"\n")
    print("Aproximacion inicial = ",xi)
    fil.write("Aproximacion inicial = "+str(xi)+"\n")
    print("Tolerancia = ",tolerancia)
    fil.write("Tolerancia = "+str(tolerancia)+"\n")
    print("Iteraciones = ",iteracion)
    fil.write("Iteraciones = "+str(iteracion)+"\n")
    input("")
    fil.write("\n")

    metodoPuntoFijo(xi, tolerancia, iteracion)

def metodoSteffense(xi, tolerancia, iteraciones):
    global f,g,tabla,fil
    x = Symbol('x')
    fx = f.subs(x,xi)
    cont = 0
    errorAbs = tolerancia + 1
    tabla.append([str(cont),str(xi),str(fx),str(errorAbs)])
    while (fx != 0 and errorAbs > tolerancia and cont < iteraciones):
        xn1 = g.subs(x,xi)
        xn2 = g.subs(x,xn1)
        if((xn2 - 2*xn1 + xi) == 0):
            print("ERROR, no se puede continuar, division por 0")
            fil.close()
            return 1
        xn = xi-((xn1-xn2)**2)/(xn2 - 2*xn1 + xi)
        fx = f.subs(x,xn)
        print(xn)
        print(xi)
        errorAbs = abs(xn - xi) 
        xi = xn
        cont += 1
        tabla.append([str(cont),str(xi),str(fx),str(errorAbs)])

    if fx == 0:
        fil.write(tabulate(tabla, headers=['i', 'xn','f(xn)','Error Absoluto'],tablefmt='fancy_grid',floatfmt=".15f"))
        print(tabulate(tabla, headers=['i', 'xn','f(xn)','Error Absoluto'],tablefmt='fancy_grid',floatfmt=".15f"))
        print (str(xi) + " es una raiz de f(x)")
    elif errorAbs < tolerancia:
        fil.write(tabulate(tabla, headers=['i', 'xn','f(xn)','Error Absoluto'],tablefmt='fancy_grid',floatfmt=".15f"))
        print(tabulate(tabla, headers=['i', 'xn','f(xn)','Error Absoluto'],tablefmt='fancy_grid',floatfmt=".15f"))
        print(str(xi) + "se aproxima a una raiz de f(x), con una tolerancia de: " + str(tolerancia))
    else:
        print("FALLO, exedio el numero  maximo de iteraciones")
    fil.close()

recolectarDatos()