'''                          
FizzBuzz
CIS 210 W19 Project 3-1

Author: Edison Mielke

Credits: N/A

Make a computer play Fizzbuzz!
'''

def fb(x):
    '''
    int -> for loop

    Description:
    counts by one and replaces the number with fizz if it is a multiple of 3,
    buzz if it's a multiple of 5 or fizzbuzz if it's a common multiple of both.

    >>>fb(15)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    '''
    
    for i in range(x):

        if ((i+1) % 3) == 0 and ((i+1) % 5) == 0:
            print("fizzbuzz")
        elif (i+1) % 3 == 0:
            print("fizz")
        elif (i+1) % 5 == 0:
            print("buzz")
        else:
            print(i+1)
        
    return None
