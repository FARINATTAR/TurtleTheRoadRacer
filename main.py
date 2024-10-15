import random

from myTurtle import Turtle, Screen
from myTurtle import MyTurtle
from car import Car
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("black")


turtle = MyTurtle()
car = Car()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.turtle_move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    if turtle.ycor() > 280:
        turtle.go_to_starting_position()
        car.level_up()
        score.increment()

    # Detect Collision with Car
    for car_obj in car.cars:
        if turtle.distance(car_obj) < 20:
            car.game_over()
            game_is_on = False

screen.exitonclick()
