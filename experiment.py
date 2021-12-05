from kivy.clock import Clock


class Experiment:

    image_list_light_temp = [["brown_light.png", "white_light.png"], 
                            ["white_light.png", "brown_light.png"]]

    image_list_dark_temp = [["brown_dark.png", "white_dark.png"], 
                            ["white_dark.png", "brown_dark.png"]]
    
    def __init__(self):

        self.time_active = 0
        self.senario = 1
        self.starting_case = 1
        self.case = self.starting_case
        self.feed_time = 3
        self.button_counter = 0
        self.click_ratio = 1
        self.case_change_time = 15
        self.feeding_condition = True
        
        self.image_list_light = self.image_list_light_temp[self.senario - 1]
        self.image_list_dark = self.image_list_dark_temp[self.senario - 1]

        self.button_image_light = self.image_list_light[self.case-1]
        self.button_image_dark = self.image_list_dark[self.case-1]

    def check_condition(self):
        return self.button_counter >= self.click_ratio
    
    def increase_btn_count(self):
        self.button_counter = self.button_counter + 1
        print(f"Button Counter:{self.button_counter}")

    def clear_counter(self):
        self.counter = 0

    def change_case(self, dt):
        self.change_case_number()
        self.change_case_feeding_condition()
        self.update_case_image()
        

    def update_case_image(self):

        self.button_image_light = self.image_list_light[self.case-1]
        self.button_image_dark = self.image_list_dark[self.case-1]

    def change_case_number(self):

        if self.case == 1:
            self.case = 2
            self.feeding_condition = False
        
        elif self.case == 2:
            self.case = 1
            self.feeding_condition = True
        else:
            pass

    def change_case_feeding_condition(self):
        print(f"here in changing fase the feeding condition is  {self.feeding_condition}")
        if self.case == 2:
            self.feeding_condition = False
        
        elif self.case == 1:
            self.feeding_condition = True
        
        print(f"Changed feeding condition to {self.feeding_condition}")
