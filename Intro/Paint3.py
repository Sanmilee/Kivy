from kivy.app import App
from kivy.uix.button import Button


class Paint1App(App):
    def build(self):
        button = Button(text='SanmiLee AI', size_hint=(
            0.2, 0.2), font_size='20sp', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        return button


Paint1App().run()
