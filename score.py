from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 16, "bold")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over.\n Score : {self.score}", align=ALIGN, font=FONT)

    def increase(self):
        self.clear()
        self.score += 1
        self.update_score()


