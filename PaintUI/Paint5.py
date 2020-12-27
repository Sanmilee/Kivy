# erase drawn lines

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.graphics import Ellipse, Color, Line
import random

# Use peach color App
Window.clearcolor = (225/225.0, 155/255.0, 128/225.0, 1)


class PaintWindow(Widget):
    def on_touch_down(self, touch):
        # set colors to random
        colorR = random.randint(0, 255)
        colorG = random.randint(0, 255)
        colorB = random.randint(0, 255)
        self.canvas.add(Color(rgb=(colorR / 255, colorG / 255, colorB / 255)))

        self.canvas.add(
            Ellipse(pos=(touch.x - 30 / 2, touch.y - 30 / 2), size=(30, 30)))

        # cretae touch dictionary to store clicked position - using touch.ud
        touch.ud['line'] = Line(points=(touch.x, touch.y))
        self.canvas.add(touch.ud['line'])

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class Paint5App(App):
    def build(self):
        # create a widget object
        rootWindow = Widget()

        # create a PaintWindow class object
        self.painter = PaintWindow()

        # create a clear button variable and bind it
        clearnBtn = Button(text='Clear', background_color=(
            0/225.0, 225/255.0, 0/225.0, 1), color=(25/225.0, 225/255.0, 225/225.0, 1))
        clearnBtn.bind(on_release=self.clear_canvas)

        rootWindow.add_widget(self.painter)
        rootWindow.add_widget(clearnBtn)

        return rootWindow

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


Paint5App().run()
