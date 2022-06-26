'''
CIS 122 Fall 2018 Lab 2
Author: Edison N. Mielke 
Description: Create a function that returns the square of any positive integer
'''

#definte a function that accepts a number
def square(num):
    #verify the number is a positive integer
        #Cannot do yet because I don't have the knowlege to do so
    #multiply the number by itself
        #result = num * num is now unneccesary

    #return the result
        #return num * num; is a little redundant since there exists a square command already
    return num ** 2
#test
print("The square of 2, 10 and 100 is "
      + str(square(2)) + ", "
      + str(square(10)) + ", and "
      + str(square(100)) + " respectively.")


