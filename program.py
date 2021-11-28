from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.image import Image  
from kivy.lang import Builder    
from kivy.uix.floatlayout import FloatLayout  
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.core.window import Window
from kivy.clock import Clock

# Window.fullscreen = True

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

relay_is_on = False

class ImageButton(ButtonBehavior, Image):
    
    def __init__(self, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
    def on_touch_down(self, touch):
        # print(f"X {touch.sx} Y {touch.sy}")
        if (((touch.sx  - 0.5 ) * float(Window.size[0]/Window.size[1])) **2 + (touch.sy - .8)**2 ) ** 0.5  < 0.10 :
            self.source = "green_dark.png"
            print(relay_is_on) 

    
    def on_touch_up(self, touch):
        self.source = "green_light.png"

class SkinnerBoxApp(App):
    def build(self):
        self.load_kv("program.kv")
        return FloatLayout()

if __name__ == "__main__":
  SkinnerBoxApp().run()
