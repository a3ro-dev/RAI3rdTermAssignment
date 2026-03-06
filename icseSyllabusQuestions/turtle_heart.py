try:
    import turtle
except ModuleNotFoundError:
    print("Error: turtle module not found. On Fedora, install Tkinter with: sudo dnf install python3-tkinter")
    exit(1)

screen = turtle.Screen()
screen.bgcolor("pink")

pen = turtle.Turtle()
pen.color("red")
pen.speed(1)
pen.begin_fill()
pen.left(140)
pen.forward(113)
pen.circle(57, 200)
pen.right(140)
pen.circle(57, 200)
pen.forward(113)
pen.end_fill()

pen.up()
pen.goto(0, -50)
pen.color("white")
pen.write("Love is in the air!", align="center", font=("Arial", 18, "bold"))

# New code for Cupid's arrow
arrow = turtle.Turtle()
arrow.hideturtle()
arrow.penup()
arrow.goto(-170, 170)
arrow.color("black")
arrow.shape("arrow")
arrow.shapesize(2, 1, 1)
arrow.setheading(-30)
arrow.stamp()

turtle.done()
