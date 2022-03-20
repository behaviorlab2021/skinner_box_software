from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.image import Image  
from kivy.lang import Builder    
from kivy.uix.floatlayout import FloatLayout  
import kivy
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.clock import Clock
from experiment_random import Experiment
from feeder import Feeder
from functions import distance_from_center
from kivy.properties import ObjectProperty

Window.fullscreen = True
# Window.show_cursor = False

Config.set('input', 'mouse', 'mouse, multitouch_on_demand')

phase_time = 15

class ExperimentLayout(FloatLayout):

    phase = 1 

    button_left = ObjectProperty(None)
    button_right = ObjectProperty(None)

    def change_case(self, dt):

        experiment.update_case_image()

        if self.phase == 1:
            
            self.button_right.source = experiment.button_image_light
            self.button_right.source_file = experiment.button_image_light
            self.button_right.source_file_press = experiment.button_image_dark
            
            self.button_left.source = experiment.button_image_light_sec
            self.button_left.source_file = experiment.button_image_light_sec
            self.button_left.source_file_press = experiment.button_image_dark
            self.phase = 2

        else:

            self.button_left.source = experiment.button_image_light
            self.button_left.source_file = experiment.button_image_light
            self.button_left.source_file_press = experiment.button_image_dark
            
            self.button_right.source = experiment.button_image_light_sec
            self.button_right.source_file = experiment.button_image_light_sec
            self.button_right.source_file_press = experiment.button_image_dark
            self.phase = 1

    def prepare_buttons(self, dt):

        self.button_left.source = experiment.button_image_light
        self.button_left.source_file = experiment.button_image_light
        self.button_left.source_file_press = experiment.button_image_dark

        self.button_right.source = experiment.button_image_light_sec
        self.button_right.source_file = experiment.button_image_light_sec
        self.button_right.source_file_press = experiment.button_image_dark
        
        pass

    def __init__(self, **kwargs):

        Clock.schedule_once(self.prepare_buttons, 0.8)
        Clock.schedule_interval(self.change_case, phase_time)

        super(FloatLayout, self).__init__(**kwargs)

    pass

class BasicImageButton(ButtonBehavior, Image):

    button_count = 0

    def on_press(self):
        self.button_count = self.button_count + 1
        # self.parent.ids.label.text ...
        self.source = self.source_file_press
    
    def on_release(self):
        self.source = self.source_file

# ______------______

class MainApp(App):

    def __init__(self, **kwargs):

        self.load_kv("program_faces_switch.kv")
        self.layout = ExperimentLayout()
        super(MainApp, self).__init__(**kwargs)

    def build(self):
        return self.layout

if __name__ == "__main__":
    experiment = Experiment()
    mainApp = MainApp()
    mainApp.run()