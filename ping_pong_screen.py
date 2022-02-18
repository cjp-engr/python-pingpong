from player_one import PlayerOne
from player_two import PlayerTwo


class PingPongScreen:

    def __init__(self, screen, turtle, player_one, player_two):
        self.screen = screen
        self.turtle = turtle
        self.player_one = player_one
        self.player_two = player_two
        self.setup_screen()

    def setup_screen(self):

        self.screen_barrier()
        self.player_one_onkey(self.player_one)
        self.player_two_onkey(self.player_two)

    def player_one_onkey(self, player_one):
        self.screen.listen()
        self.screen.onkeypress(player_one.player_up, "w")
        self.screen.onkeypress(player_one.player_down, "s")

    def player_two_onkey(self, player_two):
        self.screen.listen()
        self.screen.onkeypress(player_two.player_up, "Up")
        self.screen.onkeypress(player_two.player_down, "Down")

    def screen_barrier(self):
        self.screen.tracer(False)
        self.turtle.goto(0, self.screen.window_height() / 2)
        self.turtle.color("white")
        self.turtle.pensize(10)
        self.turtle.setheading(270)
        self.turtle.goto(0, -self.screen.window_height() / 2)
        self.screen.update()







