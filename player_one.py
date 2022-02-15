from turtle import Turtle
from player import Player

PLAYER_ONE_STARTING_POSITIONS = [(-475, 0), (-475, 20), (-475, 40), (-475, 60)]


class PlayerOne(Player):

    def __init__(self, screen):
        self.screen = screen
        super().__init__(self.screen)
        self.create_players_paddle()

    def create_players_paddle(self):
        for position in PLAYER_ONE_STARTING_POSITIONS:
            self.player_one_paddle(position)

    def player_one_paddle(self, position):
        self.screen.tracer(False)
        player_one = Turtle()
        player_one.clear()
        player_one.hideturtle()
        player_one.color("white")
        player_one.shape("square")
        player_one.penup()
        player_one.goto(position)
        player_one.showturtle()
        self.segments.append(player_one)
        self.screen.update()

    def player_one_position(self):
        return self.segments[0].ycor()
