from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Initialize main game screen
screen = Screen()
screen.title("Pong")  # Set window title
screen.bgcolor("black")  # Set background color to black
screen.setup(width=800, height=600)  # Set the size of the screen
screen.tracer(0)  # Turn off auto screen refresh for smoother animations

# Create paddles and ball
r_paddle = Paddle((350, 0))  # Right paddle at (350, 0)
l_paddle = Paddle((-350, 0))  # Left paddle at (-350, 0)
ball = Ball()  # Ball object for gameplay

# Create scoreboard instance
scoreboard = Scoreboard()

# List of paddles for convenience
paddles = [r_paddle, l_paddle]

# Enable paddle movement controls
screen.listen()
screen.onkey(r_paddle.up, "Up")  # Move right paddle up
screen.onkey(r_paddle.down, "Down")  # Move right paddle down
screen.onkey(l_paddle.up, "w")  # Move left paddle up
screen.onkey(l_paddle.down, "s")  # Move left paddle down

# Main game loop
game_is_on = True
while game_is_on:
    ball.move_ball()  # Update ball's position
    screen.update()  # Refresh the screen

    # Detect collision with top or bottom wall and bounce
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with paddles and bounce
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect when the ball goes off the screen
    if ball.xcor() > 380 or ball.xcor() < -380:
        if ball.xcor() > 380:  # Ball goes past the right paddle
            scoreboard.lscore_up()  # Increment left player's score
        elif ball.xcor() < -380:  # Ball goes past the left paddle
            scoreboard.rscore_up()  # Increment right player's score
        ball.reset_ball()  # Reset ball to the center

# Exit on user click
screen.exitonclick()
