'''                          
My Square Root
CIS 210 W19 Project 2-2

Author: Edison Mielke

Credits: N/A

Write a function to determine the square root of a number and then compare
to the built in function
'''
def mysqrt(n,k):
    '''
    (integer, integer) -> float

    Sets result to 0 and compresult to a very high number as to not conflict
    result. Runs through the babalonian equasion and sets result to the answer
    it then compares compresult to result

    >>>mysqrt(100,10)
    10.0
    >>>mysqrt(25,10)
    5.083333
    >>>mysqrt(25,5)
    5.0
    >>>mysqrt(625,5)
    65.0
    >>>mysqrt(10000,8)
    629.9
    >>>mysqrt(10000,10)
    505.0
    >>>mysqrt(10000,11)
    460.045
    >>>mysqrt(10000,96)
    100.083333
    '''
    result = 0
    compresult = 999999999999
    for i in range(k):
        if i > 0:
            compresult = result
        step1 = n/(i+1)
        step2 = step1 + (i+1)
        result = (step2 / 2)
        if result > compresult:
            break
    return result

def sqrt_compare(n, k):
    '''
    (int, int) -> float

    compares between prebuilt square root and mysqrt
    '''
    import math
    
    error = 100 * ((math.sqrt(n))/(mysqrt(n, k)))
    print("For", n, "using", k, "iterations: ")
    print("mysqrt value is:", mysqrt(n, k))
    print("math lib sqrt value is:", math.sqrt(n))
    print("this is a", error, "percent error")
    print()
def main():
    '''Runs square root comparison multiple times'''
    sqrt_compare(25, 5)
    sqrt_compare(25, 10)
    sqrt_compare(625, 5)
    sqrt_compare(625, 10)
    sqrt_compare(10000, 8)
    sqrt_compare(10000, 10)
    sqrt_compare(10000, 11)
    return None

main()
