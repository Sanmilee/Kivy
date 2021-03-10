# Text Field

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField


class DemoApp(MDApp):

    def build(self):
        screen = Screen()

        username = MDTextField(text='Enter Username: ', pos_hint={
                               'center_x': 0.5, 'center_y': 0.5}, size_hint_x=None, width=300)

        screen.add_widget(username)

        return screen


DemoApp().run()
