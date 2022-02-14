import turtle 
import math

def alpha_check () : 

  alpha = int(input('Enter the angle of the tree (in degrees, up to 90): '))
  D = alpha
  if alpha >= 90:
    print('Too big angle, please try again: ')
    D = alpha_check() 
  return D 

def Pythagoras_tree(aturt, depth, maxdepth, length, alpha): 

    if depth > maxdepth: 
        return   
    anotherturt = aturt.clone()  
    
    aturt.forward(length)  
    aturt.left(alpha)  
    Pythagoras_tree(aturt, depth+1, maxdepth, math.cos(math.radians(alpha)) * length, alpha) 
    
    anotherturt.right(90)  
    anotherturt.forward(length) 
    anotherturt.left(90)   
    anotherturt.forward(length) 
    
    if depth != maxdepth:   

        turt3 = anotherturt.clone()  
        turt3.left(alpha)   
        turt3.forward(math.sin(math.radians(alpha)) * length) 
        turt3.right(90) 
        Pythagoras_tree(turt3, depth + 1, maxdepth, math.sin(math.radians(alpha)) * length, alpha) 

    anotherturt.left(90)   
    anotherturt.forward(length) 


iterations = int(input('Enter the number of iterations: ')) 
alpha = alpha_check() 

screen = turtle.Screen()

screen.title("Pythagorean tree")
screen.tracer(0, 0)

t = turtle.Turtle() 

t.hideturtle()  
t.penup()  
t.goto(-75, -225)  
t.pendown()  
t.speed(1)  
t.left(90)  

Pythagoras_tree(t, 1, iterations, 150, alpha)  

name = 'Pythagorean_tree_depth_' + str(iterations) + '.eps' 

screen.getcanvas().postscript(file=name)

screen.update()

turtle.done()
