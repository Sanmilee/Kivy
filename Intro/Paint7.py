# for more than 1 button, Layout is needed
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)
Window.size = (360, 600)


class Paint6App(App):
    def build(self):

        # spacing: for spaces between layouts & padding: spaces bet layout and the app interface walls
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)

        img = Image(source='boo.jpg')

        btn = Button(text="Button")

        layout.add_widget(img)
        layout.add_widget(btn)

        return layout


Paint6App().run()
