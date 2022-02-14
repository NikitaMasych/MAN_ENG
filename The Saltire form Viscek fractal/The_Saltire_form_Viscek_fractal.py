import turtle

def square(a):

    turtle.begin_fill()
    
    for _ in range(4):
        turtle.forward(a)
        turtle.left(90)

    turtle.end_fill()

def cords(x, y):

    turtle.up()
    turtle.goto(x, y)
    turtle.down()

def draw_cross(x, y, length):

    cords(x + length / 2, y - length / 6)
    square(length / 3)

    cords(x + length / 2, y + length / 2)
    square(length / 3)

    cords(x - length / 6, y + length / 2)
    square(length / 3)

    cords(x - length / 6, y - length / 6)
    square(length / 3)

    cords(x + length / 6, y + length / 6)
    square(length / 3)


def main_rec(x, y, length, count):

    if count > 0:

        main_rec(x, y, length / 3, count - 1)
        main_rec(x + length / 3, y + length / 3, length / 3, count - 1)
        main_rec(x - length / 3, y - length / 3, length / 3, count - 1)
        main_rec(x - length / 3, y + length / 3, length / 3, count - 1)
        main_rec(x + length / 3, y - length / 3, length / 3, count - 1)

    else:

        draw_cross(x, y, length)
        return


iterations = int(input('Enter the number of iterations: '))

screen = turtle.Screen()

screen.tracer(0, 0)
screen.title('Saltire Form Vicsek Fractal')
screen.setup(800, 800)
screen.bgcolor('#FFFFFF')

turtle.speed(0)
turtle.hideturtle()
turtle.color('#000000')
turtle.left(180)

main_rec(0, 0, 600, iterations)

name = 'Saltire_Vicsek_fractal_depth_' + str(iterations) + '.eps' 

screen.getcanvas().postscript(file=name)

screen.update()

turtle.done()
