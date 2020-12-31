from kivy.app import App
from kivy.uix.widget import Widget


class PongGame(Widget):
    pass


class Pong2App(App):
    def build(self):
        return PongGame()


Pong2App().run()
