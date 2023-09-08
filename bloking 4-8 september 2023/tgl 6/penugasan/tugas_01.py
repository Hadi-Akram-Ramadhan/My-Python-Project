import turtle

# Persegi panjang
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)

# Segitiga
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)

# Trapezium
turtle.penup()
turtle.goto(-200, -100)
turtle.pendown()
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(50)

# Jajar genjang
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.forward(100)
turtle.right(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(100)

# Belah ketupat
turtle.penup()
turtle.goto(-200, -300)
turtle.pendown()
for i in range(4):
    turtle.forward(50 if i % 2 == 0 else 100)
    turtle.right(90)

# Menutup window saat di-klik
window = turtle.Screen()
window.exitonclick()
