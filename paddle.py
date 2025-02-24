from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, PADDLE_POS):
        super().__init__()
        self.shape("square")  # Paddle shape
        self.color("white")  # Paddle color
        self.shapesize(stretch_wid=5, stretch_len=1)  # Size of the paddle
        self.penup()  # Disable drawing during movements
        self.create_paddle()  # (Unused placeholder method)
        self.goto(PADDLE_POS)  # Move the paddle to its start position

    def create_paddle(self):
        """This method is unused and serves no purpose."""
        pass

    def up(self):
        """Move the paddle up by 20 pixels."""
        new_y = self.ycor() + 20  # Increase the y-coordinate
        self.goto(self.xcor(), new_y)  # Update position

    def down(self):
        """Move the paddle down by 20 pixels."""
        new_y = self.ycor() - 20  # Decrease the y-coordinate
        self.goto(self.xcor(), new_y)  # Update position
