import turtle

# Persegi panjang
turtle.fillcolor("red")
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.end_fill()

# Segitiga
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.end_fill()

# Trapezium
turtle.penup()
turtle.goto(-200, -100)
turtle.pendown()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(50)
turtle.end_fill()

# Jajar genjang
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.forward(100)
turtle.right(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(100)
turtle.end_fill()

# Segilima
def draw_pentagon(size):
    turtle.fillcolor("purple")
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(size)
        turtle.right(72)
    turtle.end_fill()

def draw_star(size):
    turtle.fillcolor("white")
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(size * 2.63) # 2.63 is the ratio of the star's outer radius to its inner radius
        turtle.right(144)
        turtle.forward(size * 2.63)
        turtle.right(72 - 144) # 72 is the angle of a point of the star
    turtle.end_fill()

def draw_segilima(size):
    draw_pentagon(size)

    # Draw a star inside the pentagon
    turtle.penup()
    turtle.goto(turtle.xcor() + size * 0.5, turtle.ycor() + size * 0.72) # 0.5 and 0.72 are the x and y offsets of the star's center from the pentagon's center
    turtle.pendown()
    draw_star(size * 0.4) # 0.4 is the ratio of the star's size to the pentagon's size

# Draw a segilima with side length of 80 pixels
draw_segilima(80)

# Menutup window saat di-klik
window = turtle.Screen()
window.exitonclick()
