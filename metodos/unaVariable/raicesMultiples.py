from tabulate import tabulate
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

f = Function('fx')
df = Function('dfx')
d2f = Function('s2fx')
out = open("raicesMultiples.txt", 'w')

tabla = []

def ingresoDatos():
    global f
    f = parse_expr(input("Ingrese f(x): "))
    x0 = float(input("Ingrese valor inicia: "))
    tolerancia = float(input("Ingrese tolerencia: "))
    while(tolerancia == 0):
        print("ERROR, la tolerancia no debe ser 0")
        tolerancia = float(input("Ingrese la tolerancia: "))
    iteracion = int(input("Ingrese el numero de iteraciones(i): "))
    while(iteracion == 0):
        print("ERROR, Numero de iteraciones debe ser mayor a 0")
        iteracion = int(input("Ingrese el numero de iteraciones(i): "))    

    raicesMutiples(x0, tolerancia, iteracion)

def raicesMutiples(x0, tolerancia, iteracion):
    global f, df, d2f
    x = Symbol('x')
    df = diff(f,x)
    d2f = diff(df, x)

    print("---VERIFICACION---")
    out.write("---VERIFICACION---\n") 
    print("f(x) = "+str(f))
    out.write("f(x) = "+str(f)+"\n")
    print("f'(x) = "+str(df))
    out.write("f'(x) = "+str(df)+"\n")
    print("f''(x) = "+str(d2f))
    out.write("f''(x) = "+str(d2f)+"\n")
    print("tol = "+str(tolerancia))
    out.write("tol = "+str(tolerancia)+"\n")
    print("i = "+str(iteracion))
    out.write("i = "+str(iteracion)+"\n")
    out.write("------------------------------------------------------\n")
    print(" ")


    fx = f.subs(x, x0)
    dfx = df.subs(x, x0)
    d2fx = d2f.subs(x, x0)
    contador = 0
    errorAbs = tolerancia + 1
    denomi = dfx**2-(fx*d2fx)
    

    #print(str(contador) + "|" + str(x0) + "|" + str(fx) + "|" + str(dfx) + "|" + str(d2fx))
    tabla.append([str(contador), str(x0), str(fx), str(dfx), str(d2fx)])

    while fx != 0 and errorAbs > tolerancia and denomi != 0 and contador < iteracion:
        x1 = x0 - fx*dfx/denomi
        fx = f.subs(x, x1)
        dfx = df.subs(x, x1)
        d2fx = d2f.subs(x, x1)
        errorAbs = abs(x1-x0)
        x0 = x1
        contador +=1
        denomi = dfx**2-(fx*d2fx)

        #print(str(contador) + "|" + str(x0) + "|" + str(fx) + "|" + str(dfx) + "|" + str(d2fx) + "|" + str(errorAbs))
        tabla.append([str(contador), str(x0), str(fx), str(dfx), str(d2fx), str(errorAbs)])

    if fx == 0:
        print(str(x0) + " raiz")
        out.write(str(x0) + " raiz")
    elif errorAbs < tolerancia:
        print(str(x0) + " se aproxima a una raiz de la función, con una tolerancia de: " + str(tolerancia))
        out.write(str(x0) + " se aproxima a una raiz de la función, con una tolerancia de: " + str(tolerancia))
    elif dfx == 0:
        print(str(x0) + " Es una raiz multiple simple")
        out.write(str(x0) + " Es una raiz multiple simple")
    elif d2fx == 0:
        print(str(x0) + " Es una raiz multiple de multiplicidad 2")
        out.write(str(x0) + " Es una raiz multiple de multiplicidad 2")
    else:
        print("NO SE PUDO REALIZAR LA SOLICITUD"+"\n")
        out.write("NO SE PUDO REALIZAR LA SOLICITUD"+"\n")

    print(tabulate(tabla, headers= ['n', 'xn', 'f(n)',"f'(n)","f''(n)", 'E']))
    out.write("------------------------------------------------------\n")
    out.write(tabulate(tabla, headers= ['n', 'xn', 'f(n)',"f'(n)","f''(n)", 'E'],floatfmt=".15f"))


    

ingresoDatos()




































































