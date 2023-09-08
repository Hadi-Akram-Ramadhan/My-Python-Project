import turtle

# Membuat layar
screen = turtle.Screen()
screen.bgcolor("white")

# Membuat turtle
t = turtle.Turtle()
t.speed(1)

# Gambar apapun sesuai dengan kreasi Anda
# Misalnya, lingkaran dengan warna biru
t.penup()
t.goto(0, 0)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(100)
t.end_fill()

# Menutup layar jika diklik
screen.exitonclick()