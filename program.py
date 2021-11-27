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

Window.fullscreen = True

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class ImageButton(ButtonBehavior, Image):  
    def __init__(self, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
        self.My_Clock = Clock
        self.My_Clock.schedule_interval(self.Update, 1/60.)
    def on_press(self):
    	self.source = "green_dark.png"
    	print ('pressed')
    def on_release(self):
        super().on_touch_down(touch)
        self.source = "green_light.png"
        print ('pressed')
    def on_touch_down(self, touch):

        print(f"X {touch.sx} Y {touch.sy}")
        if (touch.sx - 0.5 )**2 + (touch.sy - .8)**2  < 0.01 :
            self.My_Clock.unschedule(self.Update)
            self.source = "green_dark.png"
    def on_touch_up(self, touch):
        self.source = "green_light.png"


class SkinnerBoxApp(App):
    def build(self):
        return FloatLayout()

if __name__ == "__main__":
  SkinnerBoxApp().run()
