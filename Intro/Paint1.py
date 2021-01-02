from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window


# set interface color to green
Window.clearcolor = (0, 1, 0, 1)


class Paint1App(App):
    def build(self):
        label = Label(text='SanmiLee AI', font_size='20sp',
                      bold=True, color=(0, 0, 1, 1), italic=True)
        return label


Paint1App().run()
