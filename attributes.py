from enum import Enum
# Button Type
class Button_Type(Enum):
    AlgoButton: int = 1
    ReadMeButton: int = 2
    PlayButton: int = 3
    WelcomeButton: int = 4
    CodeButton: int = 5

# Button Attributes
class TR_Button_Attributes(Enum):
    width: int = 100
    height: int = 30
    elevation: int = 4
    
    top_color ='#117554'
    bottom_color = '#6EC207'
    clicked_color = '#4379F2'
    border_radius: int = 5
    font_size: int = 30
    
class MR_Button_Attributes(Enum):
    width: int = 155
    height: int = 30
    elevation: int = 3
    
    top_color = '#6C48C5'
    bottom_color = '#C68FE6'
    clicked_color = '#D74B4B'
    border_radius: int = 10
    font_size: int = 30
    
class L_Button_Attributes(Enum):
    width: int = 170
    height: int = 40
    elevation: int = 5
    
    top_color ='#4793AF'
    bottom_color = '#074173'
    clicked_color = '#D74B4B'
    border_radius: int = 5
    font_size: int = 25
    
class TL_Button_Attributes(Enum):
    width: int = 150
    height: int = 30
    elevation: int = 4
    
    top_color ='#001F3F'
    bottom_color = '#EAD8B1'
    clicked_color = '#FFEB00'
    border_radius: int = 5
    font_size: int = 25

# Screen Type
class Screen_Type(Enum):
    ReadMe: int = 1
    Code: int = 2

# Screen Attributes
class Screen_Attributes(Enum):
    width: int = 326
    height: int = 640
    x_value: int = 686
    y_value: int = 102
    
    top_color = '#7C9AD6'
    font_color = '#FFFFFF'

    border_radius: int = 5
    font_size: int = 25