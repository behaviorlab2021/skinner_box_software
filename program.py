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

class Experiment:
    def __init__(self):
        self.time_active = 0
        self.phase = 1
        
class Feeder:
     def __init__(self):
        self.is_active = False

class ImageButton(ButtonBehavior, Image):

    def __init__(self, **kwargs):
        self.is_active = True
        self.counter = 0
        super(ImageButton, self).__init__(**kwargs)

    def on_touch_down(self, touch):

        if self.touch_on_button(touch):
            self.change_button_color("green_dark.png")
 
            if feeder.is_active:
                # todo: write "extra" position data...
                pass
            else:

                # check condition ()
                # open feeder if condition is True
                # Schedule feeder deactivation after n seconds
                pass              

        else:
            # todo: write "miss" position data...
            print("miss")

    def on_touch_up(self, touch):
        self.change_button_color("green_light.png")
    
    def change_button_color(self, image_source):
        self.source = image_source
    

    def touch_on_button(self, touch):

        window_x = Window.size[0]
        window_y = Window.size[1]

        button_center_x = self.pos_hint['center_x']
        button_center_y = self.pos_hint['center_y']

        button_radius = float(self.size_hint[0] / 2)       

        aspect_ratio = float(window_x/window_y)

        # touch.sx and touch.sy are the relative coordinates of the touch to the window, between 0 and 1 

        dist_from_center  = distance_from_center(touch.sx, touch.sy, button_center_x, button_center_y, aspect_ratio)

        return  dist_from_center < button_radius
    

class SkinnerBoxApp(App):
    def build(self):
        self.load_kv("program.kv")
        return FloatLayout()


def activate_feeder():
    pass

def deactivate_feeder():
    pass

def create_deactivate_feeder_event():
    pass

def check_condition():
    pass

def distance_from_center (point_x, point_y, center_x, center_y, aspect_ratio):

    return (((point_x - center_x) * aspect_ratio) **2 + (point_y - center_y)**2 ) ** 0.5


if __name__ == "__main__":
  feeder = Feeder()
  SkinnerBoxApp().run()