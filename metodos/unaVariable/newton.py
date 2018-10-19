from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from tabulate import tabulate

f = Function('fx')
df = Function('dfx')

def recolectarDatos():
    global f
    f = parse_expr(input("Ingrese la función f(x) a ser evaluada: "))
    x0 = input("Ingrese el valor inicial: ")
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

    metodoNewton(float(x0), float(tolerancia), niteraciones)

def metodoNewton(x0, tolerancia, niteraciones):
    global f,df
    file = open("newton.txt", "w")
    v_array_imprimir = []
    x = Symbol('x')
    df = diff(f,x)
    fx = f.subs(x,x0)
    dfx = df.subs(x,x0)
    cont = 0
    errorAbs = tolerancia + 1
    v_array_imprimir.append([str(cont),str(x0),str(fx),str(dfx)])
    while fx != 0 and errorAbs > tolerancia and dfx != 0 and cont < niteraciones:
        x1 = x0 - fx/dfx
        fx = f.subs(x,x1)
        dfx = df.subs(x,x1)
        errorAbs = abs(x1 - x0)
        errorRel = errorAbs/x1
        x0 = x1
        cont += 1
        v_array_imprimir.append([str(cont),str(x0),str(fx),str(dfx),errorAbs, errorRel])

    if fx == 0:
        print (str(x0) + " es una raiz")
        print(tabulate(v_array_imprimir, headers=['Iteraciones' ,'x(m)' , 'f(xm)',' df(xm)','EA','ER'], tablefmt='grid', floatfmt=".17f"))
        file.write(tabulate(v_array_imprimir, headers=['Iteraciones' ,'x(m)' , 'f(xm)',' df(xm)','EA','ER'], tablefmt='grid', floatfmt=".17f"))
    elif errorAbs < tolerancia:
        print(tabulate(v_array_imprimir, headers=['Iteraciones' ,'x(m)' , 'f(xm)',' df(xm)','EA','ER'], tablefmt='grid', floatfmt=".17f"))
        print(str(x0) + " se aproxima a una raiz de la función, con una tolerancia de: " + str(tolerancia))
        file.write(tabulate(v_array_imprimir, headers=['Iteraciones' ,'x(m)' , 'f(xm)',' df(xm)','EA','ER'], tablefmt='grid', floatfmt=".17f"))
    elif dfx == 0:
        print(str(x0) + " Es una posible raiz multiple")
    else:
        print("Excedio el numero de iteraciones posible")
    file.close()
recolectarDatos()
