# Data Table: containing rows and colums

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

# automatic window size - for mobile testing
Window.size = (300, 500)

screen_helper = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Demo App'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["clock", lambda x: app.navigation_draw()]]
            elevation: 10    # shadow

        MDLabel:
            text: 'Hello World LeeAI'
            halign: 'center'

        MDBottomAppBar
            MDToolbar:
                left_action_items: [["help", lambda x: app.navigation_draw()]]
                mode: 'end'         # 'free-end'
                type: 'bottom'
                icon: 'language-python'
                on_action_button: app.navigation_draw()
'''


class LeeAIApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'

        screen = Builder.load_string(screen_helper)

        return screen

    def navigation_draw(self):
        print("Navigation")


LeeAIApp().run()
