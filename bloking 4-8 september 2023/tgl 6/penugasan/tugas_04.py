import turtle

def fibonacci_tree(t, branch_length, level):
    if level == 0:
        return
    t.forward(branch_length)
    t.left(45)
    fibonacci_tree(t, branch_length * 0.7, level - 1)
    t.right(90)
    fibonacci_tree(t, branch_length * 0.7, level - 1)
    t.left(45)
    t.backward(branch_length)

# Membuat layar
screen = turtle.Screen()
screen.bgcolor("white")

# Membuat turtle
t = turtle.Turtle()
t.speed(1)
t.color("green")

# Menggambar Fibonacci Tree
t.penup()
t.goto(0, -200)
t.pendown()
fibonacci_tree(t, 100, 7)

# Menutup layar jika diklik
screen.exitonclick()