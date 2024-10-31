import pygame
from attributes import Button_Type
from attributes import Screen_Type
import rightScreen
import time

class Button:
    def __init__(self, text, pos, button_design, button_type): # pos = (x, y)
        # Core attributes
        self.pressed = False
        self.original_y_pos = pos[1]
        self.button_type = button_type
        
		# button desing
        self.boarder_raidus = button_design.boarder_radius.value
        self.elevation = button_design.elevation.value
        self.dynamic_elevation = button_design.elevation.value
        self.width = button_design.width.value
        self.height = button_design.height.value
        self.font_size = button_design.font_size.value
        
		# top rectangle
        self.top_rect = pygame.Rect(pos, (self.width, self.height))
        
		# click color
        self.top_color = button_design.top_color.value
        self.dynamic_top_color = button_design.top_color.value
        self.clicked_color = button_design.clicked_color.value

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (self.width, self.height))
        self.bottom_color = button_design.bottom_color.value

        # text
        self.text = text
        gui_font = pygame.font.Font(None, self.font_size)
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self, screen): # buttons: [List]
        # elevation Logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius = self.boarder_raidus)
        pygame.draw.rect(screen, self.dynamic_top_color, self.top_rect, border_radius = self.boarder_raidus)
        screen.blit(self.text_surf, self.text_rect)
        #self.check_click(screen, buttons, readme_map, code_map)

    def check_click(self, buttons, readme_map, code_map):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.dynamic_top_color = self.clicked_color
                self.pressed = True
            else:
                if self.pressed == True:
                    if self.button_type == Button_Type.PlayButton:
                        return self.play_button(buttons, readme_map, code_map)
                    elif self.button_type == Button_Type.AlgoButton:
                        return self.algo_button(buttons, readme_map, code_map)
                    elif self.button_type == Button_Type.CodeButton:
                        return self.code_button(buttons, readme_map, code_map)
                    elif self.button_type == Button_Type.WelcomeButton:
                        return self.welcome_button(buttons, readme_map, code_map)
                    else:
                        return self.readme_button(buttons, readme_map, code_map)
        
        return ("", None)

    def play_visualizer(self, text):
        # Place holder for the actual play code
        print("Visualizer is live for ", text)
        time.sleep(5)

    def readme_window(self, text):
        # Place holder for the actual readme code
        print("Presenting Algotith ReadMe for ", text)

    def code_window(self, text):
        # Place holder for the actual Code code
        print("Presenting Algotith Code for ", text)

    def welcome_button(self, buttons, readMe_map, code_map):
        
        for button in buttons:
            button.pressed = False
            button.dynamic_elevation = button.elevation
            button.dynamic_top_color = button.top_color
        
        # reset all everything
        for name in code_map:
            code_map[name].dynamic_elevation = code_map[name].elevation

        for name in readMe_map:
            readMe_map[name].dynamic_elevation = readMe_map[name].elevation

        return ("", None)

    def play_button(self, buttons, readme_map, code_map):

        for button in buttons:
            if (button.button_type == Button_Type.AlgoButton and
                button.pressed == True):
                # plays the visualizer
                self.play_visualizer(button.text)
                break
                
        self.dynamic_elevation = self.elevation
        self.dynamic_top_color = self.top_color
        self.pressed = False
        return ("", None)
        
    def readme_button(self, buttons, readMe_map, code_map):
        
        val = False
        for button in buttons:
            if (button.button_type == Button_Type.AlgoButton and
                button.pressed == True):
                
                self.readme_window(button.text)
                val = True
            elif button.button_type == Button_Type.CodeButton:
                button.dynamic_elevation = button.elevation
                button.dynamic_top_color = button.top_color
                
                button.pressed = False
                
        if not val:
            self.dynamic_elevation = self.elevation
            self.dynamic_top_color = self.top_color
            self.pressed = False
            return ("", None)
        else:
            text = 'Welcome'
            # reset all everything
            for name in code_map:
                code_map[name].dynamic_elevation = code_map[name].elevation

            for name in readMe_map:
                readMe_map[name].dynamic_elevation = readMe_map[name].elevation

            # set the new screen
            readMe_map[text].dynamic_elevation = 0
            return (text, Screen_Type.ReadMe)

    def code_button(self, buttons, readMe_map, code_map):
        val = False
        for button in buttons:
            if (button.button_type == Button_Type.AlgoButton and
                button.pressed == True):

                self.code_window(button.text)
                val = True
            elif button.button_type == Button_Type.ReadMeButton:
                button.dynamic_elevation = button.elevation
                button.dynamic_top_color = button.top_color
                button.pressed = False

        if not val:
            self.dynamic_elevation = self.elevation
            self.dynamic_top_color = self.top_color
            self.pressed = False
            return ("", None)
        else:
            text = 'Welcome'
            # reset all everything
            for name in code_map:
                code_map[name].dynamic_elevation = code_map[name].elevation

            for name in readMe_map:
                readMe_map[name].dynamic_elevation = readMe_map[name].elevation

            # set the new screen
            code_map[text].dynamic_elevation = 0
            
            return (text, Screen_Type.Code)
    
    def algo_button(self, buttons, readMe_map, code_map):
        text = 'Welcome'
        # ReadMe for the currently selected algo
        self.readme_window(self.text)

        for button in buttons:
            # Ending a visualizer if it is currently on
            # Turning off all the other algo buttons
            # Turning off the Code button
            if (button.button_type == Button_Type.PlayButton or 
                button.button_type == Button_Type.CodeButton or
                (button.button_type == Button_Type.AlgoButton and
                  button.text != self.text)):
                
                button.dynamic_elevation = button.elevation
                button.dynamic_top_color = button.top_color
                button.press = False

            # Turing on the readme_button
            elif button.button_type == Button_Type.ReadMeButton:
                button.dynamic_elevation = 0
                button.dynamic_top_color = self.clicked_color
                button.pressed = True

        # reset all everything
        for name in code_map:
            code_map[name].dynamic_elevation = code_map[name].elevation

        for name in readMe_map:
            readMe_map[name].dynamic_elevation = readMe_map[name].elevation

        # set the new screen
        readMe_map[text].dynamic_elevation = 0

        print("Algo selected is ", self.text)
        return (text, Screen_Type.ReadMe)

        