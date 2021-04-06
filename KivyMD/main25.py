# Data Table: containing rows and colums

from kivymd.app import MDApp
from kivy.lang import Builder


screen_helper = '''
Screen:
    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            title: 'Demo Application'
            
        MDLabel:
            text: 'Hello World LeeAI'
            halign: 'center'

'''


class LeeAIApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)

        return screen


LeeAIApp().run()
