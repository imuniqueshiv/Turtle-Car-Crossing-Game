from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1  # Initialize the level to 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)  # Set the position of the scoreboard
        self.update_scoreboard()  # Display the initial scoreboard

    def level_up(self):
        self.level += 1  # Increase the level by 1
        self.update_scoreboard()  # Update the scoreboard display

    def update_scoreboard(self):
        self.clear()  # Clear the previous level display
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Write the current level

    def game_over(self):
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER!", align="center", font=FONT)  # Display the game over message