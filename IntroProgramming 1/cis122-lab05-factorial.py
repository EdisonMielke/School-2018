'''
Assignment: Cis 123 Lab 05
Author: Edison N. Mielke
Decription: Create factorials using the IDLE editor
'''
final = 6
#Initialize Function Factorial
def factorial(num):
    #Cannot be less than 0
    if num < 0:
        print("Error, number cannot equal 0")
    #0! = 1, only 1 permutation of 0!
    if num == 0:
        print("1")
    #If num > 0 then the program starts
    if num > 0:
        #range is 1 less than num so num isn't multiplied twice
        for i in range(num-1):
            #i + 1 to remove 0
            i = i + 1
            #i*num brings num back to the rest of i
            num = i*num
        return num
print(factorial(final))
import math

def test_factorial(num):
    Errors = 0
    range_num = num + 1
    a = factorial(num)
    b = math.factorial(num)
    Errors = a - b
    print("*",a, b)
    return print("Errors (",num,") :",Errors)
test_factorial(final)
