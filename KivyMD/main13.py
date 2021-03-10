# add list with 2 lines of description

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, TwoLineListItem
from kivy.uix.scrollview import ScrollView


class DemoApp(MDApp):

    def build(self):
        screen = Screen()

        scroll = ScrollView()
        list_item = MDList()

        scroll.add_widget(list_item)

        for i in range(10):
            items = TwoLineListItem(
                text="Item " + str(i), secondary_text="Hello World")
            list_item.add_widget(items)

        screen.add_widget(scroll)

        return screen


DemoApp().run()
