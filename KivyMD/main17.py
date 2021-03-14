# helper function: icon list -- with 3 lines list of description

from kivymd.app import MDApp
from kivy.lang import Builder


list_helper = """
Screen:
    ScrollView:
        MDList:
            OneLineListItem:
                text: "Item 1"
            OneLineListItem:
                text: "Item 2"
"""


class LeeAIApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper)

        return screen


LeeAIApp().run()
