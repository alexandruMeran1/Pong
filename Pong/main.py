from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong game")
screen.tracer(0)


l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
ball=Ball()
score=Score()


screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")





on=True
x=0.1
while on :
    time.sleep(x)
    screen.update()
    ball.move()

    if ball.ycor() >280 or ball.ycor() < -280 :
        ball.bounce()
    if ball.distance(r_paddle) <50 and ball.xcor() >320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_paddle()
        x-=0.005

    if ball.xcor() >380 :
        ball.reset()
        score.lpoint()
        score.update()
        x=0.1
    if ball.xcor() <-380 :
        ball.reset()
        score.rpoint()
        score.update()
        x=0.1
screen.exitonclick( )
