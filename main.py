from turtle import Screen, Turtle
from ping_pong_screen import PingPongScreen
from player import Player
from player_one import PlayerOne
from player_two import PlayerTwo
from ball import Ball
from players_score import PlayersScore

screen = Screen()
turtle = Turtle()
screen.setup(width=1000, height=700)
screen.bgcolor("black")
player = Player(screen)
player_one = PlayerOne(screen)
player_two = PlayerTwo(screen)
ps = PlayersScore(screen)
pingpong_screen = PingPongScreen(screen, turtle, player_one, player_two)
ball = Turtle()
ball.speed(0)
b = Ball(ball, screen, player_one, player_two, ps)

screen.exitonclick()