from turtle import Screen, Turtle
from ping_pong_screen import PingPongScreen
from ball import Ball

screen = Screen()
turtle = Turtle()
screen.tracer(False)
screen.setup(width=1000, height=700)
screen.bgcolor("black")
ping_pong_screen = PingPongScreen(screen, turtle)
screen.tracer(True)
ball = Ball(screen)
screen.update()
screen.exitonclick()