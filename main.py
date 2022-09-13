import time
from turtle import Screen
from game_paddle import Paddle
from ball import Ball
from bricks import BrickSetup
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor('black')
screen.title("Breakout 2022")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle = Paddle()
ball = Ball()
bricks = BrickSetup()
score = ScoreBoard(5)
screen.listen()
screen.onkey(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')

game_on = True
while game_on:
    time.sleep(0.2)
    screen.update()

    # move the ball continuesly
    ball.move()

    #detect paddle collision with wall
    if paddle.xcor() >= 330:
        paddle.stay_in_window(right=True, left=False)

    if paddle.xcor() <= -340:
        paddle.stay_in_window(right=False, left=True)

    ## collision with walls

    #detection with upper wall collision with the ball
    if ball.ycor() > 270:
        ball.bounce(x_bounce=False, y_bounce=True)



    #detection with side walls collision
    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce(x_bounce=True, y_bounce=False)

    #detect collision with bottom wall

    if ball.ycor() < -280:
        ball.reset()

    #detect ball collision with paddle
    if ball.distance(paddle) < 100 and ball.ycor() < -200:
        if paddle.xcor() > 0:
            if ball.xcor() > paddle.xcor():
                ball.bounce(x_bounce=True, y_bounce=True)
            else:
                ball.bounce(x_bounce=False, y_bounce=True)

        elif paddle.xcor() < 0:
            if ball.xcor() < paddle.xcor():
                ball.bounce(x_bounce=True, y_bounce=True)
            else:
                ball.bounce(x_bounce=False, y_bounce=True)

        else:
            if ball.xcor() > paddle.xcor():
                ball.bounce(x_bounce=True, y_bounce=True)
            elif ball.xcor() < paddle.xcor():
                ball.bounce(x_bounce=True, y_bounce=True)
            else:
                ball.bounce(x_bounce=False, y_bounce=True)

    #ball detection with brick

    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            brick.clear()
            brick.goto(2000, 2000)
            bricks.bricks.remove(brick)

        if ball.xcor() < brick.xcor()-40:
            ball.bounce(x_bounce=True, y_bounce=False)

        elif ball.xcor() < brick.xcor()+40:
            ball.bounce(x_bounce=True, y_bounce=False)

        elif ball.ycor() < brick.ycor() - 25:
            ball.bounce(x_bounce=False, y_bounce=True)




screen.mainloop()