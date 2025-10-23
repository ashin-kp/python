import turtle

t = turtle.Turtle()
t.speed(0)  # Fastest
turtle.bgcolor("black")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(360):
    t.color(colors[i % 6])
    t.forward(i * 0.5)
    t.left(59)

turtle.done()
