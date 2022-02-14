from turtle import * 

def dragon(level, size, direction = 45): 

    if level:
        right(direction) 
        dragon(level - 1, size / 2**.5, 45) 
        left(direction * 2) 
        dragon(level - 1, size / 2**.5, -45) 
        right(direction) 
    else: 
        forward(size) 
 
iterations = int(input('Enter the number of iterations: ')) 
 
tracer(0, 0)
title("Dragon Curve")

hideturtle() 
speed('fastest') 
penup() 
goto(-90, 20) 
pendown()

thickness = 5 if iterations == 0 else 5 / (iterations  * 0.75)
pensize(thickness) 


dragon(iterations, 200 * iterations ** (1 / 2) ) 

name = 'Dragon_curve_depth_' + str(iterations) + '.eps' 

getcanvas().postscript(file = name) 

update()

done()
