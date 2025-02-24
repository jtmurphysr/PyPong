from turtle import Turtle

# Constants for initial ball position and speed
BALL_POS = (0, 0)
BALL_SPEED = 1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  # Set the shape of the ball
        self.color("white")  # Set the color of the ball
        self.penup()  # Lift pen to prevent drawing while moving
        self.create_ball()  # Initialize ball at starting position
        self.x_move = 1  # Horizontal movement speed
        self.y_move = 1  # Vertical movement speed

    def create_ball(self):
        """This method creates a ball at a fixed starting position."""
        print(f"Creating ball at position: {BALL_POS}")
        new_ball = Turtle()
        new_ball.goto(BALL_POS)

    def move_ball(self):
        """Calculate the new position of the ball and update its position."""
        new_x = self.xcor() + self.x_move  # Update x-coordinate by movement speed
        new_y = self.ycor() + self.y_move  # Update y-coordinate by movement speed
        self.goto(new_x, new_y)  # Move ball to new position

    def bounce_y(self):
        """Reverse the vertical direction of the ball."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse the horizontal direction of the ball and increase speed."""
        self.x_move *= -1
        self.x_move *= 1.1  # Increase horizontal speed slightly
        self.y_move *= 1.1  # Increase vertical speed slightly

    def reset_ball(self):
        """Reset the ball to the starting position and reset the speed."""
        self.x_move = 1  # Reset horizontal speed
        self.y_move = 1  # Reset vertical speed
        self.hideturtle()  # Temporarily hide the ball
        self.goto(BALL_POS)  # Reset position to the starting point
        self.showturtle()  # Show the ball again
        self.bounce_x()  # Reverse direction to give variety after reset
