from math import *

def factorial_division(number_pairs):
    n = 0
    m = 0
    for pair in number_pairs:
        n = pair[0]
        m = pair[1]
        if(not m % factorial(n)):
            return str(m) + " divides " + str(n) + "!"
        else:
            return str(m) + " doesn't divide " + str(n) + "!"
