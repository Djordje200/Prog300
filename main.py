from kivy.uix.textinput import TextInput
from itertools import chain
from kivy.graphics.texture import Texture
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window








class Slope(MDApp):

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))        
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        return screen_manager
       

if __name__ == "__main__":
    LabelBase.register(name="futur", fn_regular="futur.ttf")
    LabelBase.register(name="futur2", fn_regular="Futura Heavy font.ttf")
    LabelBase.register(name="futur3", fn_regular="Futura Book font.ttf")

    Slope().run()

