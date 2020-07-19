import math
from math import *
from numpy import log as ln
import main


def function(exp, val):
    x = val
    f = eval(exp)
    return f

def order1(exp):
    x0 = float(input("Enter x0: "))
    x1 = float(input("Enter x1: "))
    x = float(input("Enter x: "))
    f_x0 = function(exp, x0)
    f_x1 = function(exp, x1)
    f_x = ((f_x0*(x-x1)) / (x0-x1)) + ((f_x1*(x-x0)) / (x1-x0))
    print("\nLAGRANGE APPROXIMATION OF F(", x,") = ", round(f_x,6),"\n")

def order1_y():
    x0 = float(input("Enter x0: "))
    y0 = float(input("Enter y0: "))
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x = float(input("Enter x: "))
    f_x = ((y0*(x-x1)) / (x0-x1)) + ((y1*(x-x0)) / (x1-x0))    
    pprint("\nLAGRANGE APPROXIMATION OF F(", x,") = ", round(f_x,6),"\n")

def order2(exp):
    x0 = float(input("Enter x0: "))
    x1 = float(input("Enter x1: "))
    x2 = float(input("Enter x2: "))
    x = float(input("Enter x: "))
    f_x0 = function(exp, x0)
    f_x1 = function(exp, x1)
    f_x2 = function(exp, x2)
    f_x = ((f_x0*(x-x1)*(x-x2)) / ((x0-x2)*(x0-x1))) + ((f_x1*(x-x0)*(x-x2)) / ((x1-x2)*(x1-x0))) + ((f_x2*(x-x0)*(x-x1)) / ((x2-x0)*(x2-x1)))
    print("\nLAGRANGE APPROXIMATION OF F(", x,") = ", round(f_x,6),"\n")

def order2_y():
    x0 = float(input("Enter x0: "))
    y0 = float(input("Enter y0: "))
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    x = float(input("Enter x: "))
    f_x = ((y0*(x-x1)*(x-x2)) / ((x0-x2)*(x0-x1))) + ((y1*(x-x0)*(x-x2)) / ((x1-x2)*(x1-x0))) + ((y2*(x-x0)*(x-x1)) / ((x2-x0)*(x2-x1)))
    print("\nLAGRANGE APPROXIMATION OF F(", x,") = ", round(f_x,6),"\n")


def order3(exp):  
    x0 = float(input("Enter x0: "))
    x1 = float(input("Enter x1: "))
    x2 = float(input("Enter x2: "))
    x3 = float(input("Enter x3: "))
    x = float(input("Enter x: "))
    f_x0 = function(exp, x0)
    f_x1 = function(exp, x1)
    f_x2 = function(exp, x2)
    f_x3 = function(exp, x3)
    f_x = ((f_x0*(x-x1)*(x-x2)*(x-x3)) / ((x0-x2)*(x0-x1)*(x0-x3))) + ((f_x1*(x-x0)*(x-x2)*(x-x3)) / ((x1-x2)*(x1-x0)*(x1-x3))) + ((f_x2*(x-x0)*(x-x1)*(x-x3)) / ((x2-x0)*(x2-x1)*(x2-x3))) + ((f_x3*(x-x0)*(x-x1)*(x-x2)) / ((x3-x0)*(x3-x1)*(x3-x2)))
    print("\nLAGRANGE APPROXIMATION OF F(", x,") = ", round(f_x,6),"\n")


def order3_y():  
    x0 = float(input("Enter x0: "))
    y0 = float(input("Enter y0: "))
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    x3 = float(input("Enter x3: "))
    y3 = float(input("Enter y3: "))    
    x = float(input("Enter x: "))
    f_x = ((y0*(x-x1)*(x-x2)*(x-x3)) / ((x0-x2)*(x0-x1)*(x0-x3))) + ((y1*(x-x0)*(x-x2)*(x-x3)) / ((x1-x2)*(x1-x0)*(x1-x3))) + ((y2*(x-x0)*(x-x1)*(x-x3)) / ((x2-x0)*(x2-x1)*(x2-x3))) + ((y3*(x-x0)*(x-x1)*(x-x2)) / ((x3-x0)*(x3-x1)*(x3-x2)))
    print("\nLAGRANGE APPROXIMATION OF F(", x,") = ", round(f_x,6),"\n")



             