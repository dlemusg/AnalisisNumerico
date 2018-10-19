from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from tabulate import tabulate
import numpy as np

f = Function('fx')

def recolectarDatos():
    global f
    f = parse_expr(input("Ingrese la función f(x) a ser evaluada: "))
    print("La función es: " + str(f))
    xi = input("Ingrese el extremo inferior: ")
    xs = input("Ingrese el extremo superior: ")
    tolerancia = input("Ingrese la tolerancia: ")
    print("La tolerancia es: " + str(tolerancia))
    while (tolerancia == 0):
        print("La tolerancia debe ser diferente de 0, ingresela nuevamente")
        tolerancia = input("Ingrese la tolerancia: ")

    niteraciones = int(input("Ingrese el numero maximo de iteraciones: " ))
    print("\n")

    while (niteraciones<0):
        print("El numero de iteraciones debe ser mayor que 0, ingreselo nuevamente")
        niteraciones = int(input("Ingrese el numero máximo de iteraciones: "))

    metodoBiseccion(float(xi),float(xs),float(tolerancia),niteraciones)

def metodoBiseccion(xi,xs,tolerancia, niteraciones):
    global f
    v_array_aitken = []
    x = Symbol('x')
    fxi = f.subs(x,xi)
    fxs = f.subs(x,xs)
    if fxi == 0:
        print(str(xi) + " es una raiz")

    elif fxs == 0:
        print(str(xs) + " es una raiz")

    elif fxi * fxs > 0:
        print("El intervalo no posee una raiz")

    else:
        file = open("biseccion.txt", "w")
        v_array_imprimir = []
        xm = (xi + xs) / 2
        fxm = f.subs(x,xm)
        v_array_aitken.append([xm,fxm])
        print( str(1) + "|" + str(xi) + "|" + str(fxi) + "|" + str(xs) + "|" + str(fxs) + "|" + str(xm) + "|" + str(fxm) + "\n")
        cont = 1
        errorAbs = tolerancia + 1
        v_array_imprimir.append([cont, xi, fxi , xs, fxs, xm, fxm, errorAbs, 0])
        while fxm != 0 and errorAbs > tolerancia and cont < niteraciones:
            if fxi * fxm < 0:
                xs = xm
                fxs = f.subs(x,xs)
            else:
                xi = xm
                fxi = f.subs(x,xi)

            xaux = xm
            xm = (xi + xs) / 2
            fxm = f.subs(x,xm)
            v_array_aitken.append([xm,fxm])
            errorAbs = abs(xm - xaux)
            errorRel = errorAbs/xm
            cont += 1
            print(str(cont) + "|" + str(xi) + "|" + str(fxi) + "|" + str(xs) + "|" + str(fxs) + "|" + str(xm) + "|" + str(fxm) + "|" + str(errorAbs) + "|" + str(errorRel) + "\n")
            v_array_imprimir.append([cont, xi, fxi , xs, fxs, xm, fxm, errorAbs, errorRel])

        if fxm == 0:
            print (str(xm) + " es una raiz")
            file.write(tabulate(v_array_imprimir, headers=['Iteraciones', 'xi', 'f(xi)', 'xs', 'f(xs)', 'xm', 'fxm','EA', 'ER'], tablefmt='grid'))
        elif errorAbs < tolerancia:
            print(str(xm) + " se aproxima a una raiz de la función, con una tolerancia de: " + str(tolerancia))
            file.write(tabulate(v_array_imprimir, headers=['Iteraciones', 'xi', 'f(xi)', 'xs', 'f(xs)', 'xm', 'fxm','EA', 'ER'], tablefmt='grid'))
        else:
            print("Excedio el numero de iteraciones posible")

        file.close()
recolectarDatos()
