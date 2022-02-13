from turtle import Screen


class Player:

    def __init__(self):
        self.segments = []
        self.create_players_paddle()
        self.head = self.segments[0]

    def create_players_paddle(self):
        pass

    def up(self):
        if not self.segments[len(self.segments) - 1].ycor() >= 340:
            print(self.segments[0].position())
            self.set_movement(90)

    def down(self):
        if not self.segments[0].ycor() <= -340:
            print(self.segments[0].position())
            self.set_movement(270)

    def set_movement(self, heading):
        screen = Screen()
        for seg_num in range(len(self.segments) - 1, -1, -1):
            screen.tracer(False)
            self.segments[seg_num - 1].setheading(heading)
            self.segments[seg_num - 1].forward(20)
            screen.update()

