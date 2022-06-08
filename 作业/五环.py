import turtle

turtle.pensize(10)


def circle(pensize: int, color: str, radius: float, x: float, y: float):
    turtle.pensize(pensize)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(radius)


def simple_circle(color: str, x: float, y: float):
    circle(10, color, 110, x, y)


def 五环(x: float, y: float):
    simple_circle("blue", x, y)
    simple_circle("yellow", x + 130, y - 110)
    simple_circle("black", x + 260, y)
    simple_circle("green", x + 390, y - 110)
    simple_circle("red", x + 520, y)


五环(-260, 55)

turtle.pensize(10)
turtle.penup()
turtle.goto(-260, 55)
turtle.pendown()
turtle.color("blue")
turtle.circle(110)
turtle.penup()
turtle.goto(-130, -55)
turtle.pendown()
turtle.color("yellow")
turtle.circle(110)
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.color("black")
turtle.circle(110)
turtle.penup()
turtle.goto(130, -55)
turtle.pendown()
turtle.color("green")
turtle.circle(110)
turtle.penup()
turtle.goto(260, 55)
turtle.pendown()
turtle.color("red")
turtle.circle(110)

input()
