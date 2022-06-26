'''
CIS 122 Fall 2018 Assignment 2 Cement
Author: Edison N. Mielke
Description: Calculate amount cement using functions
Refrences: https://stackoverflow.com/questions/47845478/unsupported-operand-types-for-or-pow-function-and-int
https://www.concretenetwork.com/concrete/howmuch/calculator.htm
https://www.todayshomeowner.com/cubic-yard-calculator/
'''

#calculating yards 

def convert_to_yards(inch):
    return inch / 46656

#given thickness in inches (t), width in inches (w)
#and length (l) in inches find volume of slab 1

def calc_in_cement_1(t=4,w=120,l=240):

    return t*w*l

#given thickness in inches (t), width in inches (w)
#and length (l) in inches find volume of slab 2

def calc_in_cement_2(t=4,w=360,l=360):

    return t*w*l

print("Slab 1 is 4in thick, 120in wide and 240in long so it's " + (str(calc_in_cement_1())) + "in^3")

print("So in yards it is " + (str(round(convert_to_yards(calc_in_cement_1()),2))) + "yd^3")
print()
print("Slab 2 is 4in thick, 360in wide and 360 in long so it's " + (str(calc_in_cement_2())) + "in^3")
print("So in yards it is " + (str(round(convert_to_yards(calc_in_cement_2()),2))) + "yd^3")
