import pygame
from attributes import Screen_Type, Screen_Attributes
from utils import load_readme, load_code
    
class Right_Screen:
    def __init__(self, name, screen_type):
        # Core attributes
        self.screen_type = screen_type
        self.name = name
        self.font_size_readme = Screen_Attributes.font_size_readme.value

        self.x_value = Screen_Attributes.x_value.value
        self.y_value = Screen_Attributes.y_value.value
        self.width = Screen_Attributes.width.value
        self.height = Screen_Attributes.height.value

        # rectangle for text
        self.top_rect = pygame.Rect((self.x_value, self.y_value), (self.width, self.height))
        self.top_color = Screen_Attributes.top_color.value
        self.elevation = Screen_Attributes.elevation.value
        self.dynamic_elevation = Screen_Attributes.elevation.value

        self.bottom_rect = pygame.Rect((self.x_value, self.y_value), (self.width, self.height))
        self.bottom_color = Screen_Attributes.bottom_color.value
        
        self.font_color = Screen_Attributes.font_color.value

        # text
        self.line_content = []
        if self.screen_type == Screen_Type.ReadMe:
            self.line_content = load_readme(name)
        else:
            self.line_content = load_code(name)

        self.get_line_list(self.line_content)

    def get_line_list(self, line_content):
        lst = []
        offset = 0
        gui_font = pygame.font.SysFont("marquee", self.font_size_readme, bold=False)
        for line in line_content: 
            text_surf = gui_font.render(line, True, self.font_color)
            text_rect = text_surf.get_rect(topleft = (self.x_value + 10, self.y_value + 10 + offset))
            lst.append([text_surf, text_rect])
            offset += 20

        self.line_list = lst
        

    def draw(self, screen):
        self.top_rect.y = self.y_value + self.dynamic_elevation
        #pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius = 5)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 5)
        for text_surf, text_rect in self.line_list:
            screen.blit(text_surf, text_rect)
        
 
            
