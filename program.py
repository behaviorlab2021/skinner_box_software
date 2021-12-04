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
        self.feed_time = 3
        self.button_counter = 0
        self.click_ratio = 1
    
    def check_condition(self):
        return self.button_counter >= self.click_ratio
    
    def increase_btn_count(self):

        self.button_counter = self.button_counter + 1
        print(f"Button Counter:{self.button_counter}")

    def clear_counter(self):
        self.counter = 0
        
class Feeder:

    def __init__(self):
        self.counter = 0 
        self.is_active = False

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False
        print("Feeder is reactivated")
        pass

    def create_deactivate_feeder_event(self, feed_time):
        Clock.schedule_once(lambda dt: self.deactivate(), feed_time)
        pass

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
                experiment.increase_btn_count()
                if experiment.check_condition():
                    feeder.activate()
                    feeder.create_deactivate_feeder_event(experiment.feed_time)
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

class MainApp(App):

    def __init__(self, **kwargs):
        self.load_kv("program.kv")
        self.layout = FloatLayout()
        super(MainApp, self).__init__(**kwargs)

    def build(self):
        return self.layout

def distance_from_center (point_x, point_y, center_x, center_y, aspect_ratio):
    return (((point_x - center_x) * aspect_ratio) **2 + (point_y - center_y)**2 ) ** 0.5

if __name__ == "__main__":
  feeder = Feeder()
  experiment = Experiment()
  mainApp = MainApp()
  mainApp.run()


