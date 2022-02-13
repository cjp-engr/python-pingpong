from player_one import PlayerOne
from player_two import PlayerTwo


class PingPongScreen:

    def __init__(self, screen, turtle):
        self.screen = screen
        self.turtle = turtle
        self.setup_screen()

    def setup_screen(self):

        # self.screen.tracer(False)
        self.screen_barrier()
        player_one = PlayerOne()
        player_two = PlayerTwo()
        self.player_one_onkey(player_two)
        # self.screen.update()

    def player_one_onkey(self, player):
        self.screen.onkey(player.up, "Up")
        self.screen.onkey(player.down, "Down")
        self.screen.listen()

    def screen_barrier(self):
        self.turtle.goto(0, self.screen.window_height() / 2)
        self.turtle.color("white")
        self.turtle.pensize(10)
        self.turtle.setheading(270)
        self.turtle.goto(0, -self.screen.window_height() / 2)
