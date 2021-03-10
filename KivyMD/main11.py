# Add more than one list to a screen: using MDList

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList


class DemoApp(MDApp):

    def build(self):
        screen = Screen()

        list_item = MDList()

        item1 = OneLineListItem(text="Item 1")
        item2 = OneLineListItem(text="Item 2")

        list_item.add_widget(item1)
        list_item.add_widget(item2)

        screen.add_widget(list_item)

        return screen


DemoApp().run()
