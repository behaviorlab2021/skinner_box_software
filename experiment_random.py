import random

from kivy.clock import Clock


class Experiment:

    image_list_random_brown = ["assets/images/buttons_random/brown_face_1.png", "assets/images/buttons_random/brown_face_2.png","assets/images/buttons_random/brown_face_3.png" ]
    image_list_random_white = ["assets/images/buttons_random/white_face_1.png", "assets/images/buttons_random/white_face_2.png","assets/images/buttons_random/white_face_3.png" ]

    image_list_light_temp = [[image_list_random_brown, image_list_random_white], 
                            [image_list_random_white, image_list_random_brown]]

    image_list_dark_temp = [["assets/images/brown_dark.png", "assets/images/white_dark.png"], 
                            ["assets/images/white_dark.png", "assets/images/brown_dark.png"]]
    
    def __init__(self):

        self.time_active = 0
        self.senario = 2
        self.starting_case = 1
        self.case = self.starting_case
        self.feed_time = 3
        self.button_counter = 0
        self.score_counter = 0
        self.click_ratio = 1
        self.case_change_time = 5
        self.feeding_condition = True
        
        self.image_list_light = self.image_list_light_temp[self.senario - 1]
        self.image_list_dark = self.image_list_dark_temp[self.senario - 1]

        self.button_image_light = self.image_list_light[self.case-1][random.randint(0,2)]
        self.button_image_dark = self.image_list_dark[self.case-1]

    def check_condition(self):
        return self.button_counter >= self.click_ratio
    
    def increase_btn_count(self):
        self.button_counter = self.button_counter + 1
    
    def increase_score_count(self):
        self.score_counter = self.score_counter + 1

    def clear_counter(self):
        self.counter = 0

    def change_case(self, dt):
        self.change_case_number()
        self.change_case_feeding_condition()
        self.update_case_image()

    def update_case_image(self):

        self.button_image_light = self.image_list_light[self.case-1][random.randint(0,2)]
        self.button_image_dark = self.image_list_dark[self.case-1]

    def change_case_number(self):

        if self.case == 1:
            self.case = 2
        elif self.case == 2:
            self.case = 1
        else:
            pass

    def change_case_feeding_condition(self):
        if self.case == 1:
            self.feeding_condition = True
        elif self.case == 2:
            self.feeding_condition = False
        else:
            pass