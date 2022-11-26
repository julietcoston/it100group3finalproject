# from kivy.lang import Builder
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"


        # defining layout
        layout = GridLayout(cols=1)

        # defining VKeyboard
        keyboard = VKeyboard(on_key_up=self.key_up)


        self.label = Label(text="Type Something", font_size ="20sp")

        layout.add_widget(self.label)
        layout.add_widget(keyboard)

        return layout
    def key_up(self, keyboard, keycode, *args):
        if isinstance(keycode, tuple):
            keycode = keycode[1]


        # Tracking what was already in the label
        thing = self.label.text


        # Running logic

        if thing == "Type Something":
            thing = ''

        # Backspace
        if keycode == 'backspace':
            thing = thing[:-1]
            keycode = ''

        # space bar
        if keycode == 'spacebar':
            keycode = ' '
        # Updating the label
        self.label.text = f'{thing} {keycode}'



MainApp().run()
