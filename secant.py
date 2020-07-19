from math import *
import math
from numpy import log as ln
from prettytable import PrettyTable
import main


def function(exp, val):
    x = val
    f = eval(exp)
    return f


def secant(exp, x0, x1):
    p = PrettyTable(["iteration", "Xi"])
    p.title = "SECANT METHOD"
    i = int(input("Enter number of iterations: ")) 
    k = 1
    print("\n")

    for j in range(i):
        f_x0 = function(exp, x0)
        f_x1 = function(exp, x1)
        new_value = x1 - ((f_x1*(x1-x0)) / (f_x1-f_x0))
        p.add_row([k, "{0:.7f}".format(new_value)])
        k += 1 
            
        x0 = x1
        x1 = new_value
    
    print(p,"\n")

