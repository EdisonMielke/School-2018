'''
CIS 122 Fall 2018 Assignment 2 Pythagorean
Author: Edison N. Mielke
Description: Create functions to calculate a missing side of a triangle
'''
import math

#Calculate missing side c

def calc_side_c(a=10, b=20):
    return round((math.sqrt((a ** 2) + (b ** 2))),2)

print("C is equal to " + str(calc_side_c())+ " if A = 10 and B = 20")

#Calculate missing side a

def calc_side_ab(ab=4, c=5):
    return (math.sqrt((c * c) - (ab * ab)))

print("Sides A or B are equal to " + str(calc_side_ab()) + " If the other A or B = 4 and C = 5")

