import bisection
import falsePos
import secant
import newtonRaph
import lagrange
import math
from os import system, name

if __name__ == '__main__':
    print("\nWELCOME TO NUMERICAL METHOD SOLVER\n\n")
    flag_set = True
    while(flag_set):
        op = int(input("Methods available:\n1. Bisection\n2. False Position\n3. Secant\n4. Newton Raphson\n5. Lagrange\n\nSelect a method (1,2,3,4,5): "))
        system('clear')

        if op == 1:
            flag = True
            while(flag):
                try:
                    exp = input("BISECTION METHOD\n\nEnter equation: ")
                    flag = False
                except Exception as ex:
                    print(ex)   

            a = float(input("Enter endpoint value 1 (should give negative result): "))
            b = float(input("Enter endpoint value 2 (should give positive result): "))
            ans1 = bisection.function(exp,a) 
            ans2 = bisection.function(exp,b)
            y = ans1 * ans2
            if y > 0:
                print("Invalid values")
            elif ans1 > 0 or ans2 < 0:
                print("Endpoint values need to be interchanged")    
            else:    
                bisection.bisectionMethod(exp, a, b)


        elif op == 2:
            flag = True
            while(flag):
                try:
                    exp = input("FALSE POSITION METHOD\n\nEnter equation: ")
                    flag = False
                except Exception as ex:
                    print(ex)    
            a = float(input("Enter endpoint value 1 (should give negative result): "))
            b = float(input("Enter endpoint value 2 (should give positive result): "))
            ans1 = falsePos.function(exp,a)
            ans2 = falsePos.function(exp,b)
            y = ans1 * ans2
            if y > 0:
                print("Invalid values")   
            else:    
                falsePos.falsePos(exp, a, b)      


        elif op == 3:
            flag = True
            while(flag):
                try:
                    exp = input("SECANT METHOD\n\nEnter equation: ")
                    flag = False
                except Exception as ex:
                    print(ex)    
            x0 = float(input("Enter x0: "))
            x1 = float(input("Enter x1: "))   
            secant.secant(exp, x0, x1)   


        elif op == 4:
            flag = True
            while(flag):
                try:
                    exp = input("NEWTON RAPHSON METHOD\n\nEnter equation: ")
                    flag = False
                except Exception as ex:
                    print(ex)    
            x0 = float(input("Enter initial guess (x0): "))  
            newtonRaph.newton(exp, x0)


        elif op == 5:
            opt = input("LAGRANGE APPROXIMATION METHOD\n\nIs value of y coordinate given? (y/n): ")
            if opt == 'y':
                ord = int(input("Enter order (1,2,3): "))
                if ord == 1:
                    lagrange.order1_y()
                elif ord == 2:
                    lagrange.order2_y()
                elif ord == 3:
                    lagrange.order3_y()
                else:
                    print("Invalid order")
            else:                    
                flag = True
                while(flag):
                    try:
                        exp = input("Enter function: ")
                        flag = False
                    except Exception as ex:
                        print(ex)    
                ord = int(input("Enter order (1,2,3): "))
                if ord == 1:
                    lagrange.order1(exp)
                elif ord == 2:
                    lagrange.order2(exp)
                elif ord == 3:
                    lagrange.order3(exp)
                else:
                    print("Invalid order")  


        else:
            print("INVALID SELECTION")         

        option = input("Do you want to choose other method? (y/n): ")
        if option == 'n' or option == 'N':
            flag_set = False
        else:
            system('clear')