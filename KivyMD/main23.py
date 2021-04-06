# Data Table: containing rows and colums


from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class DemoApp(MDApp):

    def build(self):
        screen = Screen()

        table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            size_hint=(0.9, 0.6),
                            check=True,
                            column_data=[
                                ("No", dp(20)),
                                ("Food", dp(20)),
                                ("Calories", dp(20))
        ],

            row_data=[
                                ("1", "Burger", "300"),
                                ("2", "Oats", "200"),
                                ("3", "Oats", "500")
        ])

        screen.add_widget(table)

        return screen


DemoApp().run()
