# Add list to a screen: Problem is that you cant add more than one list
# use the MDList to solve this

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem


class DemoApp(MDApp):

    def build(self):

        screen = Screen()

        item1 = OneLineListItem(text="Item 1")

        screen.add_widget(item1)

        return screen


DemoApp().run()
