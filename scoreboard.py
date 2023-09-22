from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")
screen = Screen()

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()

        self.penup()
        self.level = 1
        self.goto(-260, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def increase_point(self):
        self.level += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)






