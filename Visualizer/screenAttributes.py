import pygame
from enum import Enum

pygame.init()

class ScreenType(Enum):
    ReadMe: int = 1
    Code: int = 2
    
class ScreenAttributes(Enum):
    width: int = 326
    height: int = 640
    x_value: int = 686
    y_value: int = 102
    
    top_color = '#7C9AD6'
    font_color = '#000000'#"#FFFFFF"
    bottom_color = "#FFFFFF"
    elevation = 700

    boarder_radius: int = 5
    font_size_readme: int = 25
    font_size_code:int = 20
        

    