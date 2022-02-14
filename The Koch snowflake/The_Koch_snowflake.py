from turtle import * 

def text_values(p, s):

    penup() 
    pencolor('#ff0000')
    goto(-40, 270) 
    pendown() 

    write("S", move = True, font = ("Verdana",  27, "bold"))

    penup()
    pencolor('#000000')
    goto(-13, 270)
    pendown()

    write(" : ", font = ("Verdana",  20, "bold"))

    penup()
    goto(15, 270)
    pendown()

    write(str(int(s * 100) / 100), font = ("Verdana",  20, "bold", "italic"))

    penup() 
    pencolor('#ff0000')
    goto(-40, 210)
    pendown() 

    write("P", move = True, font = ("Verdana",  27, "bold"))

    penup()
    pencolor('#000000')
    goto(-13, 210)
    pendown()

    write(" : ", font = ("Verdana",  20, "bold"))

    penup()
    goto(15, 210)
    pendown()

    write(str(int(p * 100) / 100), font = ("Verdana",  20, "bold", "italic"))

def movement(iterations=1, actions=None, length=None): 

    if not actions: 
        actions = ['f'] 
    if not length:
        length = 100 / (3 ** (iterations - 1))
    for i in actions: 
        if i == 'f': 
            if iterations != 0: 
                movement(iterations - 1, "flfrflf", length) 
            else:
                forward(length) 
        elif i == 'l': 
            left(60) 
        elif i == 'r':
            right(120) 

iterations = int(input('Enter the number of iterations: ')) 

a = int(input('Enter the relative side length: ')) 

tracer(0, 0)
title("Koch Snowflake")

hideturtle() 
bgcolor('#ffffff') 
penup()
goto(-150,100) 
speed(0) 
down()
pencolor('#000000')

thickness = 2 if iterations in (0, 1) else 4 / (iterations  * 0.75)
pensize(thickness)

movement(iterations) 
right(120) 
movement(iterations)
right(120) 
movement(iterations) 

name = 'Koch_snowflake_depth_' + str(iterations) + '.eps' 

getscreen().getcanvas().postscript(file=name) 

s0 = a * a * (3**(1/2)) / 4 
l = 0 
for i in range (iterations): 
    l = l + (4/9)**(i+1)
s = s0 * (1 + 3/4*l) 

p = 3*a*((4/3)**iterations) 

text_values(p, s)

update()

done() 
