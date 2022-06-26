'''
Class: Cis 122 Assignment 3 Question 3
Author: Edison N. Mielke
Description: Create a grid that counts up to a number all the way down
'''
import turtle
t = turtle.Turtle()

def draw_line(t, x, y, angle, length):
    '''Pen starts up, sets angle axes and then puts pen down ending in pen up

    The pen starts in up position and then sets the angle heading to the specified angle
    then it is set to the x axis and y axis positioning to which the pen goes down, after
    that the length is drawn, finally the pen is in up position

Args:

t (Turtle): Drawing Turtle
x (int/float): Starting X location
y (int/float): Starting y location
angle (int/float): Starting angle
length (int/float): Length of line

    Returns:
    
        None
'''
    t.pu()
    t.seth(angle)
    t.setx(x)
    t.sety(y)
    t.pd()
    t.fd(length)
    t.pu()
#draw_line(t,100,100,0,200)
#draw_line(t,-100,-100,270,50)
#draw_line(t,200,-200,45,75)

def draw_radial_lines(t,x,y,length,num_lines):
    t.pu()
    for i in range(num_lines):
        t.setx(x)
        t.sety(y)
        t.pd()
        t.rt(360/num_lines)
        t.fd(length)
        t.pu()
#draw_radial_lines(t,-100,-100,25,8)
#draw_radial_lines(t,-100,100,100,4)
#draw_radial_lines(t,100,-100,200,16)
#draw_radial_lines(t,100,100,50,32)

def draw_radials_in_quadrants(t,length,num_lines):
    disx=2*length
    disy=2*length
    t.pu()
    for i in range(4):
        print(i)
        if i == 0:
            disx=-disx
        if i == 1:
            disx=-disx
        if i == 2:
            disx=-disx
            disy=-disy
        if i == 3:
            disx=-disx
            disy=disy
        for i in range(num_lines):
            t.setpos(disx,disy)
            t.pd()
            t.rt(360/num_lines)
            t.fd(length)
            t.pu()
        t.setpos(0,0)
    
draw_radials_in_quadrants(t,100,8)
draw_radials_in_quadrants(t,50,16)
