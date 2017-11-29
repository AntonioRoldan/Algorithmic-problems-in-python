from math import * 

def is_armstrong_number(number):
    armstrong_number = 0
    for digit in str(number):
        armstrong_number += pow(int(digit), 3)
    if(armstrong_number == number):
        return "Yes"
    else:
        return "No"
