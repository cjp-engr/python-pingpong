from turtle import Turtle

A = (-30, 320), (-50, 320), (-70, 320)
B = (-30, 320), (-30, 300), (-30, 280)
C = (-30, 280), (-30, 260), (-30, 240)
D = (-30, 240), (-50, 240), (-70, 240)
E = (-70, 280), (-70, 260), (-70, 240)
F = (-70, 320), (-70, 300), (-70, 280)
G = (-30, 280), (-50, 280), (-70, 280)

SCORE_0 = [A, B, C, D, E, F]
SCORE_1 = [B, C]
SCORE_2 = [A, B, G, D, E]
SCORE_3 = [A, B, G, C, D]
SCORE_4 = [F, G, B, C]
SCORE_5 = [A, F, G, C, D]
SCORE_6 = [A, F, E, D, C, G]
SCORE_7 = [A, B, C]
SCORE_8 = [A, B, C, D, E, F, G]
SCORE_9 = [G, F, A, B, C, D]


class PlayersScore:

    def __init__(self, screen):
        self.screen = screen
        self.segments_a = []
        self.create_score_segment(0)

    # def cover(self):
    #     b = Turtle()
    #     b.goto(0, 0)
    #     b.hideturtle()
    #     b.fillcolor("blue")
    #     b.begin_fill()
    #     # b.penup()
    #     b.goto(-100, 340)
    #     for _ in range(4):
    #         b.forward(85)
    #         b.right(90)
    #         b.forward(120)
    #     b.end_fill()

    def segment(self, position):
        # self.cover()
        score = Turtle()
        score.clear()
        score.color("white")
        score.shape("square")
        score.penup()
        score.goto(position)
        self.segments_a.append(score)
        score.clear()
        score.screen.update()

    def create_score_segment(self, sc):
        i = 0
        if sc == 0:
            self.segments_a = []
            sc = SCORE_0
        if sc == 1:
            self.segments_a = []
            sc = SCORE_1
        if sc == 2:
            self.segments_a = []
            sc = SCORE_2
        while i < len(sc):
            for position in sc[i]:
                self.segment(position)
            i += 1

    def get_player_one_score(self, sc):
        self.create_score_segment(sc)

    def get_player_two_score(self, sc):
        print(sc)
        pass
