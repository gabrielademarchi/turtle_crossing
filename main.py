from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time


SECONDS = 0.6
start_time = time.time()

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.listen()
screen.tracer(0)


player = Player()
screen.onkey(player.move_up, "Up")

score = Scoreboard()


car_manager = CarManager()

is_on = True
while is_on:
    time.sleep(0.05)
    screen.update()

    # Generate cars
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time > SECONDS:
        start_time = current_time
        car_manager.create_cars()
    car_manager.move_cars()
    car_manager.clear_array()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) <= 20:
            score.game_over()
            is_on = False

    # Detect successful crossing
    if player.is_at_finish_line():
        player.reset_position()
        score.level_up()
        car_manager.level_up()


screen.exitonclick()
