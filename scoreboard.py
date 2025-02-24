from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()  # Hide the turtle cursor
        self.penup()  # Do not draw when moving
        self.color("white")  # Set the text color to white
        self.lscore = 0  # Left player's score
        self.rscore = 0  # Right player's score
        self.draw_scoreboard()  # Draw the scoreboard on the screen

    def rscore_up(self):
        """Increment the right player's score and update the scoreboard."""
        self.rscore += 1  # Add 1 to the right player's score
        self.clear()  # Clear the current score display
        self.draw_scoreboard()  # Redraw the updated scoreboard

    def lscore_up(self):
        """Increment the left player's score and update the scoreboard."""
        self.lscore += 1  # Add 1 to the left player's score
        self.clear()  # Clear the current score display
        self.draw_scoreboard()  # Redraw the updated scoreboard

    def draw_scoreboard(self):
        """Display the current scores of both players."""
        self.clear()  # Clear the current score display
        self.goto(-100, 240)  # Move to left score display position
        self.write(self.lscore, align="center", font=("Courier", 40, "normal"))  # Draw left score
        self.goto(100, 240)  # Move to right score display position
        self.write(self.rscore, align="center", font=("Courier", 40, "normal"))  # Draw right score
