'''
Class: Cis 122 Assignment 3 Question 2
Author: Edison N. Mielke
Description: Create a grid that counts up to a number all the way down
'''

def draw_grid(number):
    #Initialize Variable num
    num = ''
    #Create a loop to count to 5
    for i in range(number):
        #use this to count linearly rather than in a row
        num = num + str(i + 1) + ' '
        #this will print as many times as the number used in the arguement
    for i in range(number):
        print(num)
    #to create space for the next set
    print()

draw_grid(3)
draw_grid(5)
draw_grid(10)
