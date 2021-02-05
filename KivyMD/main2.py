from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles


class LeeAIApp(MDApp):
    def build(self):
        # theme_text_color: "Primary", "Secondary", "Hint", " Error", "Custom"
        # font_style: "Caption", "H1", "H2"

        # label = MDLabel(text="Hello world", halign="center",
        # theme_text_color = "Custom", text_color = (0, 0, 1, 1), font_style = "Caption")

        label = MDIcon(icon="language-python", halign="center")

        return label


LeeAIApp().run()
