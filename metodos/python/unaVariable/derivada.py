from tabulate import tabulate
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

f = Function('fx')
df = Function('dfx')
d2f = Function('s2fx')
d3f = Function('s3fx')
d4f = Function('s4fx')
out = open("raicesMultiples.txt", 'w')

tabla = []

def ingresoDatos():
    global f
    f = parse_expr(input("Ingrese f(x): "))
    raicesMutiples(f)   

def raicesMutiples(ff):
    global f,df,d2f,d3f,d4f
    x0 = "2"
    x = Symbol('x')
    df = diff(f,x)
    d2f = diff(df, x)
    d3f = diff(d2f, x)
    d4f = diff(d3f, x)

    fx = f.subs(x, x0)
    dfx = df.subs(x, x0)
    d2fx = d2f.subs(x, x0)
    d3fx = d3f.subs(x, x0)
    d4fx = d4f.subs(x, x0)

    print("fx"+fx)
    print("f'x"+dfx)
    print("f''x"+d2fx)
    print("f'''x"+d3fx)
    print("f'vx"+d4fx)


ingresoDatos()