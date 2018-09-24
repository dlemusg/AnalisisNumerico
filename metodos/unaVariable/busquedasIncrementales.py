from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from tabulate import tabulate

f = Function('fx')

def recolectarDatos():
    global f
    f = parse_expr(input("Ingrese la función f(x) a ser evaluada: "))
    print("La función es: " + str(f))
    x0 = input("Ingrese el valor incial: ")
    delta = input("Ingrese el tamaño del paso: ")
    niteraciones = int(input("Ingrese el numero maximo de iteraciones: " ))
    print("\n")
    while (niteraciones<0):
        print("El numero de iteraciones debe ser mayor que 0, ingreselo nuevamente")
        niteraciones = int(input("Ingrese el numero máximo de iteraciones: "))

    busquedasIncrementales(float(x0),float(delta),niteraciones)

def busquedasIncrementales(x0, delta, niteraciones):
    global f
    file = open("busquedas.txt", "w")
    v_array_imprimir = []
    x = Symbol('x')
    fx0 = f.subs(x,x0)
    if fx0 == 0:
        print(str(x0) + " es una raiz")
        file.write(str(x0) + " es una raiz")
    else:
        x1 = x0 + delta
        cont = 1
        fx1 = f.subs(x,x1)
        v_array_imprimir.append([cont, x1, fx1])
        while fx0*fx1 > 0 and cont < niteraciones:
            x0 = x1
            fx0 = fx1
            x1 = x0 + delta
            fx1 = f.subs(x,x1)
            cont = cont + 1
            v_array_imprimir.append([cont, x1, fx1])

        if fx1 == 0:
            print(tabulate(v_array_imprimir, headers=['i', 'xm', 'f(xm)'],tablefmt='grid',floatfmt=".15f"))
            print (str(x1) + " es una raiz")
            file.write(tabulate(v_array_imprimir, headers=['Iteraciones', 'xm', 'f(xm)'], tablefmt='grid'))
        elif fx0 * fx1 < 0:
            print(tabulate(v_array_imprimir, headers=['Iteraciones', 'xm', 'f(xm)'],tablefmt='grid',floatfmt=".15f"))
            print("Hay una raiz entre: " + str(x0) + " and " + str(x1))
            file.write(tabulate(v_array_imprimir, headers=['Iteraciones', 'xm', 'f(xm)'], tablefmt='grid'))
        else:
            print("Excedio el numero de iteraciones posible")
    file.close()
recolectarDatos()
