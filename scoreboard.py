from turtle import Turtle

try:
    score = int(open('score.txt', 'r').read())
except FileNotFoundError:
    score = open('score.txt', 'w').write(str(0))
except ValueError:
    score = 0

FONT = ('arial', 18,'normal')

class ScoreBoard(Turtle):
    def __init__(self, lives):
        super().__init__()
        self.color = 'white'
        self.penup()
        self.hideturtle()
        self.high_score = score
        self.goto(x=-340, y=240)
        self.lives = lives
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Scores: {self.score} | Highest Score:\ {self.high_score} | Lives:{self.lives}', align='left', font=FONT)

