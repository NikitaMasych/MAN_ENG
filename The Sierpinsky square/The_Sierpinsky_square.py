import turtle 

def Sierpinsky_capret(count, l): 

    if count == 0:  

        turtle.color('black') 
        turtle.begin_fill() 
        for _ in range (4): 
            turtle.forward(l)  
            turtle.left(90) 
        turtle.end_fill() 

    else:

        for _ in range(4): 

            Sierpinsky_capret(count - 1, l / 3)    
            turtle.forward(l / 3) 
            Sierpinsky_capret(count - 1, l / 3)    
            turtle.forward(l / 3)             
            turtle.forward(l / 3)
            turtle.left(90) 


iterations = int(input('Enter the number of iterations: ')) 

length = 500

screen = turtle.Screen()
screen.tracer(0, 0)
screen.title("Sierpinski Capret")

turtle.hideturtle() 
turtle.penup() 
turtle.goto(- length / 2, - length / 2) 
turtle.pendown() 
turtle.speed(0) 

Sierpinsky_capret(iterations, length) 

name = 'Sierpinski_capret_depth_' + str(iterations) + '.eps' 

screen.getcanvas().postscript(file=name)

screen.update()

turtle.done()
