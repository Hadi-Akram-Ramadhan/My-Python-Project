# Mengimpor modul turtle
import turtle

# Membuat objek turtle bernama t
t = turtle.Turtle()

# Mengatur kecepatan dan ukuran t
t.speed(0)
t.pensize(10)

# Mengatur warna latar belakang menjadi putih
turtle.bgcolor("white")

# Mengatur posisi awal t di pojok kiri atas
t.penup()
t.goto(-200, 200)
t.pendown()

# Mengatur warna t menjadi merah
t.color("red")

# Menggambar garis horizontal merah sepanjang 400 piksel
t.forward(400)

# Mengangkat t dan memindahkannya ke bawah sejauh 100 piksel
t.penup()
t.goto(-200, 100)
t.pendown()

# Mengatur warna t menjadi putih
t.color("white")

# Menggambar garis horizontal putih sepanjang 400 piksel
t.forward(400)

# Menampilkan hasil gambar
turtle.done()
