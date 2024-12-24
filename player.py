from turtle import Screen, Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)  # Set the starting position of the player
        self.setheading(90)  # Set the direction of the player to face upwards

    def move_up(self):
        self.forward(MOVE_DISTANCE)  # Move the player forward by a set distance

    def reset(self):
        self.goto(STARTING_POSITION)  # Reset the player's position to the starting point

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:  # Check if the player has reached the finish line
            return True
        else:
            return False