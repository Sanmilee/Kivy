from kivy.app import App
from kivy.uix.widget import Widget


class PaintWindow(Widget):
    pass


class Paint1App(App):
    def build(self):
        return PaintWindow()


Paint1App().run()
