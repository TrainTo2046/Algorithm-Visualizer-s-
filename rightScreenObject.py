
class Right_Screen_Object:
    def __init__(self, program, name, screen_type, text=[]):
        # Core attributes
        self.program = program
        self.name = name
        self.screen_type = screen_type
        self.text = text
        
    def draw_text(self):
        screen = self.program.screen
        for text_surf, text_rect in self.text:
            screen.blit(text_surf, text_rect)