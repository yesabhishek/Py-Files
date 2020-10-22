# -*- coding: utf-8 -*-

import kivy
from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout


kivy.require('1.11.1') 
    
class HomeScreen(GridLayout):
    
    def __int__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
    
        self.add_widget(Label(text="Smart Calculator!",halign="center", valign="middle", font_size=30))

    def add():
        pass

    def sub():
        pass
    
    def mul():
        pass
    
    def div():
        pass


class Calculator(App):
    def build(self):
        self.screen_manager = ScreenManager()
        
        self.home_screen = HomeScreen()
        screen = Screen(name="HomeScreen")
        screen.add_widget(self.home_screen)
        self.screen_manager.add_widget(screen)

        return self.screen_manager
     
        
if __name__ == '__main__':
    
    cal_app = Calculator()
    