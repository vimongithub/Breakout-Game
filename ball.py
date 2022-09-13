from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.create_ball()
        self.x_move = 20
        self.y_move = 20

    def create_ball(self):
        self.color('white')
        self.shape('circle')
        self.penup()
        self.goto(0, -235)

    def move(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            self.x_move *= -1

        if y_bounce:
            self.y_move *= -1

    def reset(self):
        self.goto(0, -235)
        self.y_move = 10
