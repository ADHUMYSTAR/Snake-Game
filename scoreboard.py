from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score}", align="center",font=("Arial",14,"normal"))
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score:{self.score}", align="center",font=("Arial",14,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=("Arial",24,"normal"))


    def incr(self):
        self.score+=1
        self.clear()
        self.update()

