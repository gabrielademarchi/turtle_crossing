from turtle import Turtle
import random

COLORS = ['#581845', '#900C3F', '#C70039', '#FF5733', '#FFC30F']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.pace = STARTING_MOVE_DISTANCE

    def create_cars(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(2, 1)
        new_car.goto(300, random.randint(-250, 250))
        new_car.tilt(90)
        new_car.setheading(180)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.pace)

    def clear_array(self):
        for car in self.all_cars:
            if car.xcor() < -300:
                self.all_cars.remove(car)
                car.hideturtle()

    def level_up(self):
        self.pace += MOVE_INCREMENT
