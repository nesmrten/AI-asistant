import turtle

# Define colors
colors = {
    'white': '#FFFFFF',
    'skin': '#FFE5B4',
    'hair': '#FFA500',
    'eyes': '#00BFFF',
    'dress': '#FF69B4'
}

# Set up turtle
screen = turtle.Screen()
screen.bgcolor(colors['white'])
screen.title('Medea')

medea = turtle.Turtle()
medea.speed(0)
medea.hideturtle()

# Draw Medea's head
medea.penup()
medea.goto(0, 200)
medea.pendown()
medea.color(colors['skin'])
medea.begin_fill()
medea.circle(100)
medea.end_fill()

# Draw Medea's hair
medea.penup()
medea.goto(0, 200)
medea.pendown()
medea.color(colors['hair'])
medea.begin_fill()
medea.right(90)
medea.circle(100, 180)
medea.goto(0, 200)
medea.end_fill()

# Draw Medea's eyes
medea.penup()
medea.goto(-40, 250)
medea.pendown()
medea.color(colors['eyes'])
medea.begin_fill()
medea.circle(20)
medea.end_fill()

medea.penup()
medea.goto(40, 250)
medea.pendown()
medea.begin_fill()
medea.circle(20)
medea.end_fill()

# Draw Medea's mouth
medea.penup()
medea.goto(0, 180)
medea.pendown()
medea.color(colors['skin'])
medea.width(3)
medea.right(90)
medea.circle(40, 180)

# Draw Medea's dress
medea.penup()
medea.goto(0, 0)
medea.pendown()
medea.color(colors['dress'])
medea.begin_fill()
medea.right(180)
medea.circle(200, 180)
medea.end_fill()

# Draw Medea's arms
medea.penup()
medea.goto(-200, 0)
medea.pendown()
medea.color(colors['skin'])
medea.begin_fill()
medea.right(90)
medea.forward(100)
medea.left(90)
medea.forward(40)
medea.right(90)
medea.circle(40, 180)
medea.right(90)
medea.forward(40)
medea.left(90)
medea.forward(100)
medea.end_fill()

medea.penup()
medea.goto(200, 0)
medea.pendown()
medea.begin_fill()
medea.right(180)
medea.forward(100)
medea.right(90)
medea.forward(40)
medea.left(90)
medea.circle(40, -180)
medea.left(90)
medea.forward(40)
medea.right(90)
medea.forward(100)
medea.end_fill()

# Exit turtle
turtle.done()
