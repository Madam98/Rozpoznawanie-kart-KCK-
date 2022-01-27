import math as mt
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

from sympy.interactive import printing
printing.init_printing(use_latex=True)

def drawplot(clr, lab, data):
    #data = np.genfromtxt(filename, skip_header = 1, delimiter = ',', unpack = True)
    ax = plt.plot(data, lab, label = lab, color = clr)
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

def zad1():
    print("Zad1")
    x = np.arange(-5, 5, 0.1)
    y = []
    for i in range(100):
        y.append(-x[i]**3 + 3*x[i]**2 + 10*x[i] - 24)
    drawplot("blue", y, x)
    plt.show()

    a, b = sym.symbols('a b')
    expr = -a**3 + 3*a**2 + 10*a - 24
    solu = sym.solve(expr.evalf(), a)
    print(solu)

def zad234():
    print("Zad2, 3, 4")
    x, y = sym.symbols('x y')
    expre1 = x**2 + 3*y - 10
    expre2 = 4*x - y**2 + 2
    solu2 = sym.solve((expre1.evalf(), expre2.evalf()), (x, y))
    print(solu2)

    for s in solu2:
        print(s)
        print("\n")

def zad5():
    print("Zad 5")
    x = sym.symbols('x')
    expre3 = sym.sin(sym.log(x, 2)) * sym.cos(x**2)/2
    solu3 = sym.diff(expre3)
    print(solu3)

def zad12n():
    x = np.matrix('1, 3, 1, 2; 1, 2, 5, 8; 3, 1, 2, 9; 5, 4, 2, 1')
    print(x)
    y = np.delete(x, 0, 0)
    y = np.delete(y, 2, 0)
    y = np.delete(y, 3, 1)
    print(y)
    return y

def zad34n():
    x = np.matrix('2, 3, 1; 5, 1, 3')
    print(x)
    y = np.transpose(x)
    print(y)
    return y

def zad6():
    x = np.arange(-mt.pi, mt.pi, mt.pi)
    y = np.arange(-mt.pi, mt.pi, mt.pi/5)
    z = np.arange(-mt.pi, mt.pi, mt.pi/50)
    x=[]
    y=[]
    z=[]
    for i in range(2*mt.pi):
        y.append(-x[i]**3 + 3*x[i]**2 + 10*x[i] - 24)

def main():
    print("Biblioteka sympy")
    zad1()
    zad234()
    zad5()

    print("\nBiblioteka numpy")
    A = zad12n()
    B = zad34n()
    print(A*B)
    zad6

if __name__ == '__main__':
    main()