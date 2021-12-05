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