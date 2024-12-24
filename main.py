import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")  # Bind the "Up" key to the player's move method

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()  # Create a new car at random intervals
    cars.move_cars()  # Move all cars on the screen

    # Detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 27:  # Check if any car is too close to the player
            game_is_on = False
            scoreboard.game_over()  # Display game over message

    # Detect successful crossing
    if player.is_at_finish_line():
        player.reset()  # Reset the player's position
        cars.increase_speed()  # Increase the speed of the cars
        scoreboard.level_up()  # Increase the level on the scoreboard

screen.exitonclick()