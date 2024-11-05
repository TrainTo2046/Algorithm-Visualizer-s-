import pygame
from attributes import Screen_Type, Screen_Attributes
from utils import load_readme, load_code

class Right_Screen_Object:
    def __init__(self, name, screen_type, text=[]):
        # Core attributes
        self.name = name
        self.screen_type = screen_type
        self.text = text

        # Right Screen
        self.x_value = Screen_Attributes.x_value.value
        self.y_value = Screen_Attributes.y_value.value
        self.width = Screen_Attributes.width.value
        self.height = Screen_Attributes.height.value
        
        # Text
        self.font_color = Screen_Attributes.font_color.value
        self.font_size_readme_txt = Screen_Attributes.font_size_readme_txt.value
        self.font_size_code_txt = Screen_Attributes.font_size_code_txt.value

        line_content = []
        if (self.screen_type == Screen_Type.ReadMe or 
            self.screen_type == Screen_Type.Home):
            line_content = load_readme(self.name)
        elif (self.screen_type == Screen_Type.Code):
            line_content = load_code(self.name)

        self.txt_file = self.get_line_list(line_content, self.screen_type)

    def get_line_list(self, line_content, screen_type):
        lst = []
        offset = 0
        font_size = self.font_size_code_txt
        if (screen_type == Screen_Type.ReadMe or 
            screen_type == Screen_Type.Home):
            font_size = self.font_size_readme_txt

        gui_font = pygame.font.SysFont("marquee", font_size, bold=False)
        for line in line_content: 
            text_surf = gui_font.render(line, True, self.font_color)
            text_rect = text_surf.get_rect(topleft = (self.x_value + 10, self.y_value + 10 + offset))
            lst.append([text_surf, text_rect])
            offset += 20

        return lst
        
    def draw_text(self, screen):
        for text_surf, text_rect in self.text:
            screen.blit(text_surf, text_rect)