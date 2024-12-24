from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.all_cars = []  # List to store all car objects
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial speed of the cars

    def create_car(self):
        random_chance = random.randint(1, 5)  # Random chance to create a car
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))  # Assign a random color to the car
            random_car_y = random.randint(-250, 250)  # Random y position for the car
            new_car.goto(300, random_car_y)  # Set the car's starting position
            self.all_cars.append(new_car)  # Add the new car to the list

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move each car backward by the current speed

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT  # Increase the speed of the cars