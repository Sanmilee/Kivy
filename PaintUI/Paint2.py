# check on_touch_down function properties

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window


# Use white color App
# Window.clearcolor = (1, 1, 1, 1)

# Use peach color App
Window.clearcolor = (225/225.0, 155/255.0, 128/225.0, 1)


class PaintWindow(Widget):
    def on_touch_down(self, touch):
        print(touch)


class Paint2App(App):
    def build(self):
        return PaintWindow()


Paint2App().run()
