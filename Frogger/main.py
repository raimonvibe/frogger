import time
from turtle import Screen
from scoreboard import Scoreboard
from car_manager import CarManager
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()  # Create a Scoreboard object
screen.listen()
screen.onkeypress(player.go_up, "Up")

game_loop = 0.1
car_loop = 0.1 / 6

game_is_on = True
while game_is_on:
    time.sleep(game_loop)
    screen.update()

    # Spawn a new car
    car_manager.spawn_car()

    # Move the cars
    car_manager.move_cars()

    # Check for collision with the player
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()  # Display "GAME OVER"
            # Add code here to handle collision (e.g., game over message)

    # Check if player reached the top edge
    if player.ycor() >= 280:
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.increase_level()  # Increase the level and update the scoreboard

screen.exitonclick()
