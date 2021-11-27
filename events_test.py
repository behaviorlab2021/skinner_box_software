
import kivy
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from kivy.clock import Clock
from kivy.lang import Builder
    
global count

Builder.load_string('''
<MyGrid>:

    name: name
    email: email

    GridLayout:
        cols:1
        size: root.width - 200, root.height -200
        pos: 100, 100

        GridLayout:
            cols:2

            Label:
                text: "Name: "

            TextInput:
                id: name
                multiline:False

            Label:
                text: "Email: "

            TextInput:
                id: email
                multiline:False

        Button:
            text:"Submit"
            on_press: root.btn()
        Button:
            text:"Add"
            on_press: root.add_btn()
''')

count = 0
condition = True

class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)



    def condition_reset(self, dt):
        global condition
        condition = True  

    def my_callback(self):
        global count
        global condition
        count += 1
        if count == 1:
            self.name.text = self.name.text + "-"
            count = 0 
            condition = False
            Clock.schedule_once(self.condition_reset, 1)
            return False
        self.name.text = self.name.text + "."

    def btn(self):
        global condition 
        condition = False
        print("Pausing", condition)
        Clock.unschedule(self.condition_reset)
        Clock.schedule_once(self.condition_reset, 5)

    def add_btn(self):
        global condition
        
        if condition:
            print("hit", condition)

            self.my_callback()
        else:
            print("miss")
            

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()