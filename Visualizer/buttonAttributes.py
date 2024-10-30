from enum import Enum

class ButtonType(Enum):
    AlgoButton: int = 1
    ReadMeButton: int = 2
    PlayButton: int = 3
    WelcomeButton: int = 4
    CodeButton: int = 5
    
class TopRightButton(Enum):
    width: int = 100
    height: int = 30
    elevation: int = 4
    
    top_color ='#117554'
    bottom_color = '#6EC207'
    clicked_color = '#4379F2'
    boarder_radius: int = 5
    font_size: int = 30
    
class MidRightButton(Enum):
    width: int = 155
    height: int = 30
    elevation: int = 3
    
    top_color = '#6C48C5'
    bottom_color = '#C68FE6'
    clicked_color = '#D74B4B'
    boarder_radius: int = 10
    font_size: int = 30
    
class LeftButton(Enum):
    width: int = 170
    height: int = 40
    elevation: int = 5
    
    top_color ='#4793AF'
    bottom_color = '#074173'
    clicked_color = '#D74B4B'
    boarder_radius: int = 5
    font_size: int = 25
    
class TopLeftButton(Enum):
    width: int = 150
    height: int = 30
    elevation: int = 4
    
    top_color ='#001F3F'
    bottom_color = '#EAD8B1'
    clicked_color = '#FFEB00'
    boarder_radius: int = 5
    font_size: int = 25