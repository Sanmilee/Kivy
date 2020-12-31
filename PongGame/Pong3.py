from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector  # add direction vector to a number


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    # reference to both velocities at the same time
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # Latest Position = Current Velocity + Current Position

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    pass


class Pong3App(App):
    def build(self):
        return PongGame()


Pong3App().run()
