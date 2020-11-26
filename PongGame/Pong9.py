from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector  # add direction vector to a number
from kivy.clock import Clock
from random import randint


class PongPaddle(Widget):
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            # change from -1 to -1.1 which you want to increase speed upon collision with paddle
            ball.velocity_x *= -1


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    # reference to both velocities at the same time
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # Latest Position = Current Velocity + Current Position

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)

    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self):
        # pixel change at 4 pixels per frame
        # make the Y_axis go any direction
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        # moving the ball by calling the move() function
        self.ball.move()

        # Bounce off top and bottom (change negative y_axis to positive by multiplying with -1)
        if (self.ball.y < 0) or (self.ball.y > self.height - 50):
            self.ball.velocity_y *= -1

        # Bounce off left and right (change negative x_axis to positive by multiplying with -1)
        if (self.ball.x < 0) or (self.ball.x > self.width - 50):
            self.ball.velocity_x *= -1

        # check if collision is done
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

    def on_touch_move(self, touch):
        if touch.x < self.width / 1/4:
            self.player1.center_y = touch.y

        if touch.x > self.width * 3/4:
            self.player2.center_y = touch.y


class Pong9App(App):
    def build(self):
        game = PongGame()

        game.serve_ball()
        # 60 frames per one second as the speed of the game
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


Pong9App().run()
