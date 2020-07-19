from math import *
import math
from numpy import log as ln
import numpy 
from sympy import *
from prettytable import PrettyTable
import main


def function(exp, val):
    x = val
    f = eval(exp)
    return f


def newton(exp, x0):
    p = PrettyTable(["iteration", "Xi", "error"])
    p.title = "NEWTON RAPHSON METHOD"
    i = int(input("Enter number of iterations: ")) 
    tol = -1
    opt = input("Tolerance included? (y/n): ")
    if opt == 'y':
        tol = float(input("Enter tolerance: ")) 
    k = 1
    print("\n")

    for j in range(i):
        f_x0 = function(exp, x0)
        x = Symbol('x')
        f_prime = Derivative(exp,x)
        new_value = x0 - (f_x0 / f_prime.doit().subs(x,x0))

        if j == 0:
            p.add_row([k, "{0:.7f}".format(new_value), "-"])
        else:    
            # calculate the ERROR 
            ERROR = math.fabs((new_value - x0) / new_value)
            p.add_row([k, "{0:.7f}".format(new_value), "{0:.7f}".format(ERROR)])
            if round(ERROR,7) == 0 or ERROR < tol:
                print("Tolerance reached on iteration", k, "in the table", "\n")
                break 
                  
        k += 1 
        x0 = new_value

    print(p,"\n")

