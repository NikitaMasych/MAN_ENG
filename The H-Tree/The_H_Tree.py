import turtle

def draw_line(buddy, pos1, pos2):
    
    buddy.penup()
    buddy.goto(pos1[0], pos1[1])
    buddy.pendown()
    buddy.goto(pos2[0], pos2[1])

def main_rec(buddy, x, y, width, height, count):
    
    draw_line(buddy, [x + width * 0.25, height // 2 + y], [x + width * 0.75, height // 2 + y])
    draw_line(buddy, [x + width * 0.25, (height * 0.5) // 2 + y], [x + width * 0.25, (height * 1.5) // 2 + y])
    draw_line(buddy, [x + width * 0.75, (height * 0.5) // 2 + y], [x + width * 0.75, (height * 1.5) // 2 + y])

    if count <= 0:  
        return
    else:  
        count -= 1
        main_rec(buddy, x, y, width // 2, height // 2, count)
        main_rec(buddy, x + width // 2, y, width // 2, height // 2, count)
        main_rec(buddy, x, y + width // 2, width // 2, height // 2, count)
        main_rec(buddy, x + width // 2, y + width // 2, width // 2, height // 2, count)

iterations = int(input('Enter the number of iterations: '))

t = turtle.Turtle(visible=False)
t.hideturtle()

thickness = 5 if iterations == 0 else 5 / (iterations  * 0.75)
t.pensize(thickness)

t.color('#000000')
t.speed(0)

screen = turtle.Screen()
screen.tracer(0, 0)
screen.setup(800, 800)
screen.title("H-Tree Fractal")
screen.bgcolor('#FFFFFF')

x = 700
y = 700

main_rec(t, - x / 2, - x / 2, x, y, iterations)

name = 'H-Tree_depth_' + str(iterations) + '.eps' 

screen.getcanvas().postscript(file=name)

screen.update()

turtle.done()
