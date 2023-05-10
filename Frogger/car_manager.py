from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5  # Initial distance for car movement
MOVE_INCREMENT = 10  # Amount to increase the car's movement distance
TOP_POSITION = 250  # Top position limit for car spawning
BOTTOM_POSITION = -250  # Bottom position limit for car spawning

class CarManager:
    def __init__(self):
        self.cars = []  # List to store the car objects

    def spawn_car(self):
        if random.randint(1, 6) == 1:  # Randomly decide if a car should be spawned
            new_car = Turtle("square")  # Create a new car turtle object
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Adjust the size to appear horizontally
            new_car.penup()
            new_car.color(random.choice(COLORS))  # Assign a random color to the car
            y_position = random.randint(BOTTOM_POSITION + 30, TOP_POSITION - 30)  # Adjust the y-position
            new_car.goto(300, y_position)  # Start the car from the right side of the screen
            new_car.setheading(180)  # Set the heading to face left
            self.cars.append(new_car)  # Add the car to the list of cars

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)  # Move each car forward by the current distance

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT  # Increase the car's movement distance

