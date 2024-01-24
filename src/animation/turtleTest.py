import turtle
import math
import random

width = 1000
height = 1000

radius = 300
rotation_speed = 0.01

window = turtle.Screen()
window.tracer(0)
window.setup(width, height)
window.bgcolor(0.3, 0.3, 0.3)

n_dots = 800
dots = []
while len(dots) < n_dots:
    x = random.randint(
        -window.window_width() // 2,
        window.window_width() // 2,
    )
    y = random.randint(
        -window.window_height() // 2,
        window.window_height() // 2,
    )
    # Discard points that fall outside the sphere
    if x ** 2 + y ** 2 > radius ** 2:
        continue
    dot = turtle.Turtle()
    dot.penup()
    dot.shape("circle")
    dot.setposition(x, y)
    dot.direction = random.choice([-1, 1])
    dot.color(0.9, 0.9, 0.9)
    dot.turtlesize(0.15)
    dot.radians()

    # Convert 'small_radius' and 'theta' into data attributes
    dot.small_radius = math.sqrt(radius ** 2 - y ** 2)
    # Starting angle
    dot.theta = math.asin(x / dot.small_radius)

    # And don't forget to append the dot to the list
    dots.append(dot)

while True:
    # Move each dot
    for dot in dots:
        x = dot.small_radius * math.sin(dot.theta)
        dot.setx(x)
        # Increase angle by 0.01 radians each iteration, for now
        dot.theta += dot.direction * rotation_speed

    window.update()