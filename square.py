import turtle

def draw_square(side_length, square_color):
    """Function to draw and fill a square with a specific color."""
    turtle.fillcolor(square_color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)
    turtle.end_fill()

screen = turtle.Screen()
screen.bgcolor("light blue")  # You can change this to any color like "pink" or "black"


t = turtle.Turtle()
t.speed(3)
t.pensize(3)

# Draw the beautiful square
draw_square(100, "magenta")


screen.exitonclick()
