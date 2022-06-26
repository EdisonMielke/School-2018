'''
Class: Cis 122 Fall 2018
Author: Edison N. Mielke
Description: Draw circles and other shapes using turtle
'''

# import turtle graphics module and create a turtle for drawing

import turtle
t = turtle.Turtle()

#______________________________
# draw a circle with radius 50

#radius = 50 
#t.circle(radius)
#radius = 75
#t.circle(radius)
#radius = 100
#t.circle(radius)
#______________________________

#Circle 1
#      radius = 50
#      t.circle(radius)
    
#radius= 50
#t.pu();
#t.rt(90);
#t.fd(radius * 0.25);
#t.lt(90)
#t.pd()
#t.circle(radius)

#circle 2
#radus = 75
#t.pu();
#t.rt(90);
#t.fd(radius * 0.25);
#t.lt(90)
#t.pd()
#t.circle(radius)

#circle 3
#radius = 100
#t.pu();
#t.rt(90);
#t.fd(radius* 0.25);
#t.lt(90)
#t.pd()
#t.circle(radius)

#______________________________
def move(t,x,y):
    #move turtle to x, y position
    t.pu()
    t.goto(x,y)
    t.pd()
    
def draw_circle(t, radius, x, y, ):
    #draw circles using turtle t
    #t.pu();
    #t.rt(90);
    #t.goto(x,y)
    #t.fd(radius * 0.25);
    #t.lt(90)
    #t.pd()

    move(t,x,y - radius)
    t.circle(radius)

def draw_circles(start_size,amount, x, y, growth):
    t.speed(10)
    for i in range(amount):
        draw_circle(t, start_size, x, y)
        start_size = start_size + growth

draw_circles(3, 30, 0, 0, 2)

#draw_circle(t, 50, 0, 0)
#draw_circle(t, 75, 0, 0)
#draw_circle(t, 100, 0, 0)
#______________________________
