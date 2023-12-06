import turtle
import colorsys 

turtle.bgcolor("black")
turtle.speed(0)
turtle.width(1)

def square(x):
    for i in range(4):
        turtle.forward(x)
        turtle.left(90)
def shape(x):
    turtle.forward(x)
    turtle.left(45)
    turtle.forward(x)
    turtle.right(60)
    turtle.width(3)
    square(x)
    turtle.width(1)
    turtle.right(165)
    turtle.forward(x)
    turtle.left(45)
    turtle.forward(x)
a= 0.0
for i in range(90):
    turtle.color(colorsys.hsv_to_rgb(a,1,1))
    turtle.circle(50,4)
    turtle.right(90)
    shape(70)
    turtle.right(135)
    a+=0.0111
turtle.done()