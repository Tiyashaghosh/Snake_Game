from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 16, "bold")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",'w') as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def increase(self):
        self.score += 1
        self.update_score()


