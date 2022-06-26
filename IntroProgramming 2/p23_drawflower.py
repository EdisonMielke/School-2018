''' 
Draw a Flower
CIS 210 W19 Project 2.3

Author: Edison Mielke

Credits: N/A

Draw a flower using multiple functions
'''
from turtle import *

amount = 25
length = 25

def drawFlower(amount):
    '''
    (int) -> None

    Draws the amount of shapes and makes them evenly apart

    >>>drawFlower(3)
    3 squares touching corners making a triangle near the center

    '''
    rt(360/amount)    
    return None

def drawPolygon(length):
    '''
    (int) -> None

    Draws basic squares variable "length" long

    >>>drawPolygon(20)
    draws a square 20 units long on all sides
    '''
    for i in range(4):
        fd(length)
        rt(90)
    return None

def main():
    '''
    None -> None

    Calls drawFlower and drawPolygon and then draws a flower,
    adds a stem at the bottom
    '''
    for i in range(amount):
        drawFlower(amount)
        drawPolygon(length)
    penup()
    setpos(0,0)
    pendown()
    setpos(0,-100)
    return None

main()
