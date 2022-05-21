from kivy.app import App
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.popup import Popup
import os
import database

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('kivy', 'show_fps' , True)
Window.size = (800, 600)
Window.minimum_width, Window.minimum_height = Window.size

cwd = os.getcwd()
images = os.path.join(cwd, 'assets','images')
appIcon = os.path.join(images, 'app_icon.png')
rickFace = os.path.join(images, 'rick_face.png')

rickrolls = 0
rickrolls_per_click = 1

def load_data():
    global game_data_save, rickrolls, rickrolls_per_click

    game_data_save = database.load()

    try:
        rickrolls = game_data_save['rickrolls']
        rickrolls_per_click = game_data_save['rickrolls_per_click']

    except KeyError:
        print('Could not find game data!')

load_data()

class MainWidget(TabbedPanel):
    rick_button = ObjectProperty(None)
    rick_rolls_text = ObjectProperty(None)

    def update_text(self, name, var):
        return f'{name}: {globals()[var]}'

    def rick_button_pressed(self):
        global rickrolls
        rickrolls += 1
        self.rick_rolls_text.text = self.update_text('Rick Rolls', 'rickrolls')

        # Temporarily saving here
        database.save(rickrolls = rickrolls, rickrolls_per_click = rickrolls_per_click)
    
    def delete_forever_popup(self):
        database.clear_save()
        load_data()
        self.rick_rolls_text.text = self.update_text('Rick Rolls', 'rickrolls')
        show_popup('Permanently deleted save.')

class P(FloatLayout):
    pass

class RickRollerV2App(App):
    def build(self):
        self.icon = appIcon
        self.title = 'Rick Roller'
        return MainWidget()

def show_popup(t):
    show = P()

    popup_window = Popup(title=t, content = show, size_hint = (None, None), size = (400, 400))

    popup_window.open()

if __name__ == '__main__':
    RickRollerV2App().run()