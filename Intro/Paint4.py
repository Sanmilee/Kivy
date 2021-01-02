from kivy.app import App
from kivy.uix.button import Button


class Paint4App(App):
    def build(self):
        button = Button(text='SanmiLee AI', size_hint=(
            0.2, 0.2), font_size='20sp', pos_hint={'center_x': 0.5, 'center_y': 0.5}, on_press=self.printPress, on_release=self.printRelease)
        return button

    def printPress(self, obj):
        print("Button has been pressed")

    def printRelease(self, obj):
        print("Button has been released")


Paint4App().run()
