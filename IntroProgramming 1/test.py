import math

def draw_grid(n):
    x=''
    for i in range(n):
        x=x + str(i+1) + ""
    for i in range(n):
        print(x)

draw_grid(3)
