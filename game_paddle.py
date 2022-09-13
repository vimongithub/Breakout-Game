from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.create_paddle()

    def create_paddle(self):
        self.penup()
        self.shape("square")
        self.color('dodger blue')
        self.shapesize(stretch_wid=1, stretch_len=12)
        self.goto(0, -260)

    def go_left(self):
        self.backward(60)

    def go_right(self):
        self.forward(60)

    def stay_in_window(self,right, left):
        if right:
            self.goto(270, -260)

        if left:
            self.goto(-275, -260)

