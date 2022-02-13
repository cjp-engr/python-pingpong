from turtle import Turtle
from player import Player

PLAYER_TWO_STARTING_POSITIONS = [(475, 0), (475, 20), (475, 40), (475, 60)]


class PlayerTwo(Player):

    def __init__(self):
        super().__init__()

    def create_players_paddle(self):
        for position in PLAYER_TWO_STARTING_POSITIONS:
            self.player_two_paddle(position)

    def player_two_paddle(self, position):
        # self.players_paddle(position)
        player_two = Turtle()
        player_two.clear()
        player_two.hideturtle()
        player_two.color("white")
        player_two.shape("square")
        player_two.penup()
        player_two.goto(position)
        player_two.showturtle()
        self.segments.append(player_two)

