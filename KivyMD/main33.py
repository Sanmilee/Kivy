# Navigation Helper

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

# automatic window size - for mobile testing
Window.size = (300, 500)

navigation_helper = '''
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: 'Demo App'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10   

                    Widget:
                    
        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation: 'vertical'

                MDLabel:
                    text: 'LeeAI'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: 'LeeAI@gmail.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
'''


class LeeAIApp(MDApp):

    def build(self):
        screen = Builder.load_string(navigation_helper)

        return screen


LeeAIApp().run()
