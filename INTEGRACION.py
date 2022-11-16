import math

def f(x):
    f = 1/math.sqrt(x)
    return f

def simpson38(a,b):    
    h = (b-a)/3
    x1 = a + h
    x2 = x1 + h
    S = (3*h/8)*(f(a)+3*f(x1)+3*f(x2)+f(b))
    return S

def simpson38Comp(a,b,n):    
    h = (b-a)/n  
    S = f(a) + f(b)
    for k in range(1,n):
        if k%3 == 0:
            S += 2*f(a+k*h)
        else:
            S += 3*f(a+k*h)     
    S *= (3*h/8)
    return S

def main():
    a = float(input("Límite inferior de integración (a): \t"))
    b = float(input("Límite superior de integración (b): \t"))
    print("-------------------------------------")
    S = simpson38(a,b)
    print("Integración Simpson 3/8 es: \t %0.14f" % (S) )
    n = int(input("Ingresar número de iteraciones: "))
    Scomp = simpson38Comp(a,b,n)
    print("Integración Simpson 3/8 compuesto es: \t %0.14f" % (Scomp) )
    
main()