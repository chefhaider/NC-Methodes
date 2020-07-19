from math import *
import math
from numpy import log as ln
from prettytable import PrettyTable
import main


def function(exp, val):
    x = val
    f = eval(exp)
    return f


def falsePos(exp, a, b):
    p = PrettyTable(["a", "f(a)", "b", "f(b)", "x (new value)", "f(x)", "Error"])
    p.title = "FALSE POSITION METHOD"    
    i = int(input("Enter number of iterations: "))
    tol = -1
    opt = input("Tolerance included? (y/n): ")
    if opt == 'y':
        tol = float(input("Enter tolerance: "))  
    print("\n")
    
    value_before = 0

    for j in range(i):
        f_a = function(exp, a)
        f_b = function(exp, b)
        new_value = ((a * f_b) - (b * f_a)) / (f_b - f_a)
        f_c = function(exp, new_value)

        value = f_a * f_c

        if j == 0:
            p.add_row(["{0:.7f}".format(a), "{0:.7f}".format(f_a), "{0:.7f}".format(b), "{0:.7f}".format(f_b), "{0:.7f}".format(new_value), "{0:.7f}".format(f_c), "-"])
        else:    
            # calculate the ERROR 
            ERROR = math.fabs((new_value - value_before) / new_value)
            p.add_row(["{0:.7f}".format(a), "{0:.7f}".format(f_a), "{0:.7f}".format(b), "{0:.7f}".format(f_b), "{0:.7f}".format(new_value), "{0:.7f}".format(f_c), "{0:.7f}".format(ERROR)])
            if round(ERROR,7) == 0 or ERROR < tol:
                print("Tolerance reached on last value of table: \na =", "{0:.7f}".format(a), "\tb =", "{0:.7f}".format(b), "\n")
                break
            v = new_value         
            
        if value > 0:
            a = new_value
        elif value < 0:
            b = new_value
        value_before = new_value
        i=i+1

    print(p)
    print("\nAnswer is:", "{0:.7f}".format(v),"\n") 
