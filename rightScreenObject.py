
class Right_Screen_Object:
    def __init__(self, name, screen_type, text=[]):
        # Core attributes
        self.name = name
        self.screen_type = screen_type
        self.text = text
        
    def draw_text(self, screen):
        for text_surf, text_rect in self.text:
            screen.blit(text_surf, text_rect)