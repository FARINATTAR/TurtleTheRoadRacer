from turtle import Turtle, Screen


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)
        self.turtle_speed = 0.1

    def turtle_move(self):
        self.forward(10)

    def go_to_starting_position(self):
        if self.ycor() > 280:
            self.goto(0, -280)


