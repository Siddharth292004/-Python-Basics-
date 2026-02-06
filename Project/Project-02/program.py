from turtle import *

# Setup
speed(0)
bgcolor("black")
colors = ['orange', 'white', 'red', 'yellow']  # more variety
hideturtle()

# Draw pattern
for i in range(180):  # more iterations for fuller design
    goto(0, 0)
    color(colors[i % len(colors)])  # cycle through multiple colors
    forward(150)
    left(2)  # smaller angle for smoother spiral
    circle(50, 90)  # partial circle for elegance
    forward(150)
    right(180)

done()
