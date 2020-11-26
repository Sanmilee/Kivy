from kivy.app import App
from kivy.uix.widget import Widget


# Game Class
class PongGame(Widget):
    pass


# App Class
class PongApp(App):

    def build(self):
        return PongGame()


PongApp().run()
