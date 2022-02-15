class Ball:
    def __init__(self, ball, screen, player_one, player_two):
        self.ball = ball
        self.screen = screen
        self.player_one = player_one
        self.player_two = player_two
        self.setup_ball()
        self.movement_ball()

    def setup_ball(self):
        self.ball.speed("normal")
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.shapesize(1, 1)
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 0.1
        self.ball.dy = -0.1

    def movement_ball(self):
        while True:
            self.screen.update()
            # move the ball
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)
            self.border_checking()
            print(self.ball.position())

    def border_checking(self):
        # 300 < 320 < 360
        y1_player_one = int(self.player_one.player_one_position())
        y2_player_one = int(y1_player_one + 60)
        y1_player_two = int(self.player_two.player_two_position())
        y2_player_two = int(y1_player_two + 60)
        y_ball = int(self.ball.ycor())
        x_ball = int(self.ball.xcor())
        s_height = int(self.screen.window_height())
        s_width = int(self.screen.window_width())
        player_one_ball = y1_player_one <= y_ball <= y2_player_one
        player_two_ball = y1_player_two <= y_ball <= y2_player_two
        print(s_height / 2)
        print(s_width / 2)
        if y_ball >= (s_height / 2) - 30:
            self.ball.sety((s_height / 2) - 30)
            self.ball.dy *= -1
        if y_ball <= -(s_height / 2) + 30:
            self.ball.sety(-(s_height / 2) + 30)
            self.ball.dy *= -1
        if x_ball >= (s_width / 2) - 50:
            if player_one_ball or player_two_ball:
                self.ball.setx((s_width / 2) - 50)
                self.ball.dx *= -1
        if x_ball <= -(s_width / 2) + 50:
            if player_one_ball or player_two_ball:
                self.ball.setx(-(s_width / 2) + 50)
                self.ball.dx *= -1


