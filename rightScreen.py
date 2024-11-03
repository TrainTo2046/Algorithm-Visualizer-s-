import pygame
from rightScreenObject import Right_Screen_Object
from attributes import Screen_Type, Screen_Attributes
from utils import load_readme, load_code

pygame.init()
class Right_Screen():
    def __init__(self):
        # Right Screen
        self.x_value = Screen_Attributes.x_value.value
        self.y_value = Screen_Attributes.y_value.value
        self.width = Screen_Attributes.width.value
        self.height = Screen_Attributes.height.value

        self.top_rect = pygame.Rect((self.x_value, self.y_value), (self.width, self.height))
        self.top_color = Screen_Attributes.top_color.value
        self.border_radius = Screen_Attributes.border_radius.value

        # Text
        self.font_color = Screen_Attributes.font_color.value
        self.font_size = Screen_Attributes.font_size.value

        # Top Left Button
        readMe1 = Right_Screen_Object('Binary Search', Screen_Type.ReadMe, [])
        code1 = Right_Screen_Object('Binary Search', Screen_Type.Code, [])
        
        self.txt_map = {readMe1.name : [readMe1, code1]}

    def drawRightScreen(self, screen):
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = self.border_radius)

    def draw(self, screen):
        for key in self.txt_map.keys():
            self.txt_map[key][1].draw_text(screen)
            self.txt_map[key][0].draw_text(screen)

    def update(self, name, screen_type):
        for key in self.txt_map.keys():
            if (key == name):
                line_content = []
                # read me txt
                if screen_type == self.txt_map[key][0].screen_type:
                    line_content = load_readme(name)
                    line_list = self.get_line_list(line_content)
                    self.txt_map[key][0].text = line_list
                # code txt
                else:
                    line_content = load_code(name)
                    line_list = self.get_line_list(line_content)
                    self.txt_map[key][1].text = line_list    
            else:
                self.txt_map[key][0].text = []
                self.txt_map[key][1].text = []

    def get_line_list(self, line_content):
        lst = []
        offset = 0
        gui_font = pygame.font.SysFont("marquee", self.font_size, bold=False)
        for line in line_content: 
            text_surf = gui_font.render(line, True, self.font_color)
            text_rect = text_surf.get_rect(topleft = (self.x_value + 10, self.y_value + 10 + offset))
            lst.append([text_surf, text_rect])
            offset += 20

        return lst
