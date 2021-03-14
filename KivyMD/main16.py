# Avatar list -- with 3 lines list of description

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, IconLeftWidget, ImageLeftWidget, ThreeLineAvatarListItem
from kivymd.uix.list import ThreeLineListItem, ThreeLineIconListItem
from kivy.uix.scrollview import ScrollView


class LeeApp(MDApp):

    def build(self):
        screen = Screen()

        scroll = ScrollView()
        list_item = MDList()

        scroll.add_widget(list_item)

        for i in range(7):
            image = ImageLeftWidget(source="uestc.png")

            items = ThreeLineAvatarListItem(
                text="Item " + str(i), secondary_text="Hello World", tertiary_text="Third Text")

            items.add_widget(image)
            list_item.add_widget(items)

        screen.add_widget(scroll)

        return screen


LeeApp().run()
