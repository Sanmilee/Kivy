# Data Table: containing rows and colums


from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class DemoApp(MDApp):

    def build(self):
        screen = Screen()

        table = MDDataTable(column_data=[
            ("Food", dp(20)),
            ("Calories", dp(20))
        ])

        screen.add_widget(table)

        return screen


DemoApp().run()
