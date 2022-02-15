from turtle import Screen, Turtle


class Player:

    def __init__(self, screen):
        self.segments = []
        self.screen = screen

    def player_up(self):
        if not self.segments[len(self.segments) - 1].ycor() >= 340:
            self.set_movement(90)

    def player_down(self):
        if not self.segments[0].ycor() <= -340:
            self.set_movement(270)

    def set_movement(self, heading):
        for seg_num in range(len(self.segments) - 1, -1, -1):
            self.screen.tracer(False)
            self.segments[seg_num - 1].setheading(heading)
            self.segments[seg_num - 1].forward(20)
            self.screen.update()

