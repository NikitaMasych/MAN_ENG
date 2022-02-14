import turtle

def draw_cross(x, y, length):

    turtle.up()
    turtle.goto(x - length / 2, y - length / 6)
    turtle.down()
    turtle.seth(0)
    turtle.begin_fill()

    for _ in range(4):

        turtle.forward(length / 3)
        turtle.right(90)
        turtle.forward(length / 3)
        turtle.left(90)
        turtle.forward(length / 3)
        turtle.left(90)  

    turtle.end_fill()

def main_rec(x, y, length, count):
    
    if count == 0:
        draw_cross(x, y, length)
        return

    main_rec(x, y, length / 3, count - 1)
    main_rec(x + length / 3, y, length / 3, count - 1)
    main_rec(x - length / 3, y, length / 3, count - 1)
    main_rec(x, y + length / 3, length / 3, count - 1)
    main_rec(x, y - length / 3, length / 3, count - 1)

iterations = int(input('Enter the number of iterations: '))

screen = turtle.Screen()
screen.tracer(0, 0)
screen.title('Cross Form Vicsek Fractal')
screen.setup(800, 800)
screen.setworldcoordinates( 1000,  -1000, -1000, 1000)
screen.bgcolor('#FFFFFF')

turtle.speed(0)
turtle.hideturtle()
turtle.color('#000000')

main_rec(0, 0, 1600, iterations)

name = 'Vicsek_fractal_depth_' + str(iterations) + '.eps' 

screen.getcanvas().postscript(file=name)

screen.update()

turtle.done()
