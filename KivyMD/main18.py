# helper function: icon list -- with 3 lines list of description

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem


list_helper = """
Screen:
    ScrollView:
        MDList:
            id: container
"""


class LeeApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper)

        return screen

    def on_start(self):
        for i in range(10):

            items = OneLineListItem(text="Item " + str(i))

            self.root.ids.container.add_widget(items)


LeeApp().run()
