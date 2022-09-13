from turtle import Turtle
import random

COLORS = ['dark slate gray', 'slate blue', 'pale green', 'cyan2', 'purple', 'deep pink', 'brown3', 'firebrick4','plum4']
class Brick(Turtle):
    def __init__(self, x_cor,y_cor,color):
        super().__init__()

        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1.9, stretch_len=6.3)
        self.color(f'{color}')
        self.goto(x_cor, y_cor)


class BrickSetup:
    def __init__(self):
        self.bricks = []
        self.create_brick()


    def create_brick(self):
        self.line = 0
        for y in range (-40, 220,50):
            self.line += 1

            for x in range(-355, 355, 140):
                if self.line == 1:
                    color = random.choice(COLORS)
                    brick = Brick(x, y, color)
                    self.bricks.append(brick)


                elif self.line == 2:
                    color = 'green'
                    brick = Brick(x, y, color)
                    self.bricks.append(brick)

                elif self.line == 3:
                    color = 'yellow'
                    brick = Brick(x, y, color)
                    self.bricks.append(brick)


                elif self.line == 4:
                    color = 'Orange'
                    brick = Brick(x, y, color)
                    self.bricks.append(brick)

                elif self.line == 5:
                    color = 'red'
                    brick = Brick(x, y, color)
                    self.bricks.append(brick)

                elif self.line == 6:
                    color = random.choice(COLORS)
                    brick = Brick(x, y, color)
                    self.bricks.append(brick)









