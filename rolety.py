from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import shapebutton

class Rolety(FloatLayout):

    def deactivate_buttons(self):
        self.ids.r_1.selected = False
        self.ids.r_2.selected = False
        self.ids.r_3.selected = False
        self.ids.r_4.selected = False

    def r1_button_click(self):        #przycisk wyboru rolety
        next_state = not self.ids.r_1.selected
        self.deactivate_buttons()
        self.ids.r_1.selected = next_state
        print("r1")
    def r2_button_click(self):
        next_state = not self.ids.r_2.selected
        self.deactivate_buttons()
        self.ids.r_2.selected = next_state
        print("r2")
    def r3_button_click(self):
        next_state = not self.ids.r_3.selected
        self.deactivate_buttons()
        self.ids.r_3.selected = next_state
        print("r3")
    def r4_button_click(self):
        next_state = not self.ids.r_4.selected
        self.deactivate_buttons()
        self.ids.r_4.selected = next_state
        print("r4")

    def up_button_click(slef):
        print("up")
    def down_button_click(slef):
        print("down")

    def up10_button_click(slef):
        print("up 10")
    def down10_button_click(slef):
        print("down 10")


class RoletyApp(App):
    
    def build(self):
        return Rolety()
    
if __name__ == '__main__':
    RoletyApp().run()