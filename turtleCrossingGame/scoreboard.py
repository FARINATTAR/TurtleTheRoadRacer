from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-248, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.level}", False, "center", ("Courier", 15, "normal"))

    def increment(self):
        self.level += 1
        self.clear()
        self.update_score()
