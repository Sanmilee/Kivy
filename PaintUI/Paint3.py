# draw circle at the clicked point

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Ellipse, Color


# Use white color App
# Window.clearcolor = (1, 1, 1, 1)

# Use peach color App
Window.clearcolor = (225/225.0, 155/255.0, 128/225.0, 1)


class PaintWindow(Widget):
    def on_touch_down(self, touch):
        # change color of cricle to draw to black
        # self.canvas.add(Color(rgb=(1, 0, 0)))

        # draw circlr of sixe 30, 30 at the clicked position
        self.canvas.add(Ellipse(pos=(touch.x, touch.y), size=(30, 30)))

        # to draw at exact clicked point
        # self.canvas.add(Ellipse(pos=(touch.x - 30 / 2, touch.y - 30 / 2), size=(30, 30)))


class Paint3App(App):
    def build(self):
        return PaintWindow()


Paint3App().run()
