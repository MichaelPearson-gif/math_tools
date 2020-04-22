# Import dependencies
import numpy as np 

# Creating Functions for Finding Derivatives

# Power Rule
# The Power Rule (cx^exp), multiplies the c and exp together than the exp is subtracted by 1
def power_rule(c, x, exp):
    
    # c represents the constant number multiplied by our variable
    # x represents our unknown variable
    # exp represents our exponent expression
    
    # multiply the constant and the exponent
    new_c = c * exp
    
    # Subtract the exponent by 1
    new_exp = exp - 1
    
    # Create a condition so that we get 3 types of results dependent on what the new_exp is equivalent to
    # if new_exp = 0, then just print the resulting constant new_c
    if new_exp == 0:
        print(new_c)
    
    # if new_exp = 1, then print new_c*x for a phantom 1 is on the exponent of x
    elif new_exp == 1:
        print(f'{new_c}{x}')
    
    # Otherwise print the statement new_c*x^new_exp
    else:
        print(f'{new_c}{x}^{new_exp}')