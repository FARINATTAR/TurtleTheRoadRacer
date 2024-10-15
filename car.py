import turtle
from turtle import Turtle, Screen
import random

COLOURS = ["green", "blue", "red", "yellow", "orange", "violet", "purple"]
STARTING_CAR_DISTANCE = 10
MOVE_INCREAMENT = 5

class Car():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_CAR_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREAMENT


    def game_over(self):
        turtle.hideturtle()
        turtle.color("white")
        turtle.write("Game Over", False, "center", ("Courier", 20, "normal"))
