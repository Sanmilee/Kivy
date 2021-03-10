# use "scroll" to move list up

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.scrollview import ScrollView


class DemoApp(MDApp):

    def build(self):
        screen = Screen()

        scroll = ScrollView()
        list_item = MDList()

        scroll.add_widget(list_item)

        for i in range(10):
            items = OneLineListItem(text="Item " + str(i))
            list_item.add_widget(items)

        screen.add_widget(scroll)

        return screen


DemoApp().run()
