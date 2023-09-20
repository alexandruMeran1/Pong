from turtle import Turtle

class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.update()

    def lpoint(self):
        self.lscore+=1
    def rpoint(self):
        self.rscore+=1

    def update(self):
        self.clear()
        self.goto(-100,190)
        self.write(self.lscore, align="center",font=("Courier",80))
        self.goto(100,190)
        self.write(self.rscore, align="center",font=("Courier",80))