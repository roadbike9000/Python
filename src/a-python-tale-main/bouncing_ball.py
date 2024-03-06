import turtle

# speed of the ball
ball_speed = -8
gravity = 0.1

# Create a green circle
ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.color("green")

# move the ball
ball.right(90)

# Run forever until application is closed
while True:
    ball_speed += gravity
    ball.forward(ball_speed)
