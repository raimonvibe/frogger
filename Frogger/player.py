from turtle import Turtle

STARTING_POSITION = (0, -280)  # Starting position for the player turtle
MOVE_DISTANCE = 10  # Distance to move the turtle each time
FINISH_LINE_Y = 280  # Y-coordinate of the finish line

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)  # Set the turtle to face upwards
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(STARTING_POSITION)  # Position the turtle at the starting position

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE  # Calculate the new y-coordinate
        self.goto(self.xcor(), new_y)  # Move the turtle to the new position

    def reset_position(self):
        self.goto(STARTING_POSITION)  # Reset the turtle's position to the starting position
