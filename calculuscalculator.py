# ! Alert
# ? Question
# TODO 
# * Highlight
# // Strikethrough
# ~ Process/Instructions
# hi

import numpy as np
import math
import mpmath

from numpy import poly1d
from sympy import *

class Calculus:

    start_question = Symbol('x')

    def integration(function, variable):
        return integrate(function, variable)

    def derivation(function, variable):
        return diff(function, variable)
    #print(integrate(1/x, x))

print(Calculus.integration(x**2, start_question))


# ! Aert



# def f(x):
#     return x ** x

# def derivative(function, value):
#     h = 0.00000000001  
#     top = function(value + h) - function(value)
#     bottom = h 
#     slope = top / bottom

#     return float("%.3f" % slope)


# q = input('What is the type of function that you want to derive? 
#                     "Exponential (E), Logarithmic (L), Trignometric (T), Polynomial (P) /n")
#     if q1 == "P":
#         pass

#     elif q1 == "E":
#         pass
    
#     elif q1 == "L":
#         pass
    
#     elif q1 == "T":
#         pass

    
# def integral(function,value):
    
    
   
         




# question2 = input('What is the function itself? /n')

# print(derivative(f,3))



# """if name == '__main__':
#     derivative = derive(f, 2)

#     print(derivative)"""



