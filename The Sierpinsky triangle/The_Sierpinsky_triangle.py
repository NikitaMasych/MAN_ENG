from turtle import * 

size = 600 

iterations = int(input('Enter the number of iterations: ')) 

min = 600 / (2 ** iterations) 
 
def Sierpinsky_triangle(l, x, y): 
    
    if l > min: 
    
        l = l / 2 
        
        Sierpinsky_triangle(l, x, y) 
        Sierpinsky_triangle(l, x + l, y)
        Sierpinsky_triangle(l, x + l / 2 , y + l * (3 ** (1 / 2)) / 2 ) 
    
    else:           

        goto(x, y)
        pendown() 

        begin_fill()                    
        forward(l)
        left(120)           
        forward(l)
        left(120)           
        forward(l)                      
        end_fill() 

        setheading(0)                   
        penup()
        goto(x,y)              
 
hideturtle() 
penup() 
speed('fastest')
screen = Screen() 
tracer(0, 0)
title("Sierpinski Triangle")

Sierpinsky_triangle(size, - size / 2, - size * (3 ** (1 / 2)) / 2 / 2.0) 

name = 'Sierpinski_triangle_depth_' + str(iterations) + '.eps' 

screen.getcanvas().postscript(file=name)

update()

done() 
