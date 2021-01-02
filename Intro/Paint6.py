# for more than 1 button, Layout is needed
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


class Paint6App(App):
    def build(self):

        # spacing: for spaces between layouts & padding: spaces bet layout and the app interface walls
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)

        btn1 = Button(text="Button1")
        btn2 = Button(text='Button2')
        btn3 = Button(text='Button3')

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        return layout


Paint6App().run()
