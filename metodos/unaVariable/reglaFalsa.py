from tabulate import tabulate
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

f = Function('fx')
out = open("reglaFalsa.txt", 'w')

tabla = []


def ingresoDatos():
    global f
    f = parse_expr(input("Ingrese f(x): "))
    xi = float(input("Ingrese extremo inferior(xi): "))
    xs = float(input("Ingreso extremo superior(xs): "))
    tolerancia = float(input("Ingrese la tolerancia: "))
    while(tolerancia == 0):
        print("ERROR, la tolerancia no debe ser 0")
        tolerancia = float(input("Ingrese la tolerancia: "))
    iteracion = int(input("Ingrese el numero de iteraciones(i): "))
    while(iteracion == 0):
        print("ERROR, Numero de iteraciones debe ser mayor a 0")
        iteracion = int(input("Ingrese el numero de iteraciones(i): "))

    
    print("---VERIFICACION---")
    out.write("---VERIFICACION---\n") 
    print("f(x) = "+str(f))
    out.write("f(x) = "+str(f)+"\n")
    print("xi = "+str(xi))
    out.write("xi = "+str(xi)+"\n")
    print("xs = "+str(xs))
    out.write("xs = "+str(xs)+"\n")
    print("tol = "+str(tolerancia))
    out.write("tol = "+str(tolerancia)+"\n")
    print("i = "+str(iteracion))
    out.write("i = "+str(iteracion)+"\n")
    out.write("------------------------------------------------------\n")
    print(" ")

    
    #out.closed()

    reglaFalsa(xi, xs, tolerancia, iteracion)

def reglaFalsa(xi, xs, tolerancia, iteracion):
    global f
    x = Symbol('x')
    fxi = f.subs(x, xi)
    fxs = f.subs(x, xs)
    cont = 1


    if fxi == 0:
        print(str(xi)+" es raiz\n")
        out.write(str(xi)+" es raiz\n")
    
    elif fxs == 0:
        print(str(xs)+" es raiz\n")
        out.write(str(xs)+" es raiz\n")

    elif fxi * fxs > 0:
        print("NO EXISTEN RAICES")
        out.write("NO EXISTEN RAICES")

    elif fxi * fxs < 0: 
        xm = xi - (fxi*(xs-xi))/(fxs-fxi)
        fxm = f.subs(x, xm)
        tabla.append([str(cont),str(xi),str(fxi),str(xs),str(fxs),str(xm),str(fxm)])
        cont += 1
        errorAbs = tolerancia + 1
        while fxm != 0 and errorAbs > tolerancia and cont < iteracion:
            if fxi * fxm < 0:
                xs = xm
                fxs = f.subs(x,xs)
            else:
                xi = xm
                fxi = f.subs(x,xi)

            xaux = xm
            xm = xi - (fxi*(xs-xi))/(fxs-fxi)
            fxm = f.subs(x,xm)
            errorAbs = abs(xm - xaux)
            tabla.append([str(cont), str(xi), str(fxi), str(xs), str(fxs), str(xm), str(fxm), str(errorAbs)])
            cont += 1    

        if fxm == 0:
            print (str(xm) + " es raiz\n")
            out.write(str(xm) + " es raiz\n")
        elif errorAbs < tolerancia:
            print(str(xm) + " se aproxima a una raiz con una tolerancia = " + str(tolerancia)+"\n")
            out.write(str(xm) + " se aproxima a una raiz con una tolerancia = " + str(tolerancia)+"\n")
        else:
            print("Fracasó en "+str(iteracion)+" iteraciones"+"\n")
            out.write("Fracasó en "+str(iteracion)+" iteraciones"+"\n")
    else:
        print("NO SE PUDO REALIZAR LA SOLICITUD"+"\n")
        out.write("NO SE PUDO REALIZAR LA SOLICITUD"+"\n")

    print(tabulate(tabla, headers= ['n', 'xi', 'fxi','xs','fxs','xm','fxm', 'E'],tablefmt='grid',floatfmt=".17f"))
    out.write("------------------------------------------------------\n")
    out.write(tabulate(tabla, headers= ['n', 'xi', 'fxi','xs','fxs','xm','fxm', 'E'],tablefmt='grid',floatfmt=".17f"))
    

ingresoDatos()