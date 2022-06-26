''' 
Binary Encoding/Decoding
CIS 210 W19 Project 4.2

Author: Edison Mielke

Credits: N/A

Description: Encode and Decode into binary
'''
import math
def dtob(n):
    binary = ''
    '''
    (int) ->int

    Converts a decimal integer to binary by taking the remainder and rounding down
    

    >>>dtob(100)
    '1100100'
    >>>dtob(27)
    '11011'
    >>>dtob(31415926)
    '1110111110101111001110110'
    '''
    while n >= 1:
        modulus = int(n%2)
        n = n/2
        binary = binary + str(modulus)
    binary = (binary[::-1])
    if binary == '':
        binary = '0'
    return binary
    '''
    (str) ->int

    converts a binary string to an integer by squaring the ones on reverse order

    >>>btod('1100100')
    100
    >>>btod('11011')
    27
    >>>btod('1110111110101111001110110')
    31415926
    '''
def btod(b):
    decimal = 0
    for i in range (len(str(b))):
        i = i+1
        if (b[-i]) == '1':
            decimal = ((decimal) + (1 * (2**(i-1))))

    return decimal

def main():
    inpint = input("Enter non-negative integer: ")

    print("Binary format is ", dtob(int(inpint)))
    print("Back to decimal", btod(dtob(int(inpint))))
    return None
main()
