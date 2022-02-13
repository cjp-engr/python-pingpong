import random
from turtle import Turtle
from random import Random


class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.ball = Turtle()
        self.set_up_ball()
        self.is_ball_alive = True
        self.move_ball()

    def set_up_ball(self):
        self.ball.color("white")
        self.ball.shape("circle")
        self.ball.shapesize(1, 1)

    def move_ball(self):
        # TODO: MAKE THE INITIAL BALL THROW RANDOMLY
        self.ball.goto(Random().randint(-500, 500), 345)
        # WHILE THE VERTICAL WALL IS NOT YET COLLIDED SET TO WHILE TRUE
        self.horizontal_wall_collision_ball()

    def horizontal_wall_collision_ball(self):
        hball = self.ball
        right_x_axis = 0 <= hball.xcor() <= 455
        upper_y_axis = 0 <= hball.ycor() <= 350
        left_x_axis = -455 <= hball.xcor() <= 0
        lower_y_axis = -350 <= hball.ycor() <= 0

        if right_x_axis and upper_y_axis:
            hball.goto(480, Random().randint(0, 350))
        elif right_x_axis and lower_y_axis:
            hball.goto(480, Random().randint(-350, 0))
        elif left_x_axis and upper_y_axis:
            hball.goto(-480, Random().randint(0, 350))
        elif left_x_axis and lower_y_axis:
            hball.goto(-480, Random().randint(-350, 0))
        print(hball.xcor(), hball.ycor())

    def paddle_collision_ball(self):
        # TODO: IF THE BALL COLLIDED WITH THE PADDLE, THE BALL BOUNCES
        pass

    def vertical_wall_collision_ball(self):
        # TODO: IF THE BALL COLLIDED WITH THE WALL, THE PLAYER LOSES
        pass
