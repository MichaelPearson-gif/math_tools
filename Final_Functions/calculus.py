# Import dependencies
import numpy as np 

# SymPy is a nice python library with the ability to do calculus work
# I will be using this to build functions
from sympy import *

# Set x as the symbol
x = symbols('x')

# Creating Functions for Finding Derivatives

# Power Rule
# The Power Rule (cx^exp), multiplies the c and exp together than the exp is subtracted by 1
# c is an optional arguments for constant values that could be multiplied by the variable
# d is an optional arguments for the exponent values
def power(c=1, d=1):
    
    # Take the derivate of x^c
    derivative = diff(c*x**d)
    
    # Return the result
    return derivative

# Addition Rule
# c and e are optional arguments for constant values that could be multiplied by the variable
# d and f are optional arguments for the exponent values 
# Default is set to 1 so if nothing is passed through it then it turns into a phantom 1
def addition(c=1, d=1, e=1, f=1):
    
    # Take the derivative of cx^d + cx^d
    derivative = diff(c*x**d + e*x**f)
    
    # Return the result
    return derivative

# Subtraction Rule
# c and e are optional arguments for constant values that could be multiplied by the variable
# d and f are optional arguments for the exponent values 
# Default is set to 1 so if nothing is passed through it then it turns into a phantom 1
def subtraction(c=1, d=1, e=1, f=1):
    
    # Take the derivative of cx^d - cx^d
    derivative = diff(c*x**d - e*x**f)
    
    # Return the result
    return derivative

print(power(3))