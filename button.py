import pygame
from attributes import Button_Type, Screen_Type
from utils import load_name

class Button:
    def __init__(self, program, text, pos, button_design, button_type): # pos = (x, y)
        self.program = program

        # Core attributes
        self.pressed = False
        self.original_y_pos = pos[1]
        self.button_type = button_type
        
		# button desing
        self.border_raidus = button_design.border_radius.value
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

    def draw(self): # buttons: [List]
        screen = self.program.screen

        # elevation Logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius = self.border_raidus)
        pygame.draw.rect(screen, self.dynamic_top_color, self.top_rect, border_radius = self.border_raidus)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    # checks if any of the buttons are clicked
    def check_click(self):
        buttons = self.program.allButtons.button_list
        rightScreen = self.program.rightScreens

        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.dynamic_top_color = self.clicked_color
                self.pressed = True
            else:
                if self.pressed == True:
                    if self.button_type == Button_Type.PlayButton:
                        return self.play_button(buttons)
                    elif self.button_type == Button_Type.AlgoButton:
                        return self.algo_button(buttons, rightScreen)
                    elif self.button_type == Button_Type.CodeButton:
                        return self.code_button(buttons, rightScreen)
                    elif self.button_type == Button_Type.HomeButton:
                        return self.welcome_button(buttons, rightScreen)
                    elif self.button_type == Button_Type.ReadMeButton:
                        return self.readme_button(buttons, rightScreen)

    def welcome_button(self, buttons, rightScreen):
        
        # set animation to blank rectangle
        # reset all everything
        for button in buttons:
            button.pressed = False
            button.dynamic_elevation = button.elevation
            button.dynamic_top_color = button.top_color
        
        rightScreen.update('', Screen_Type.Home)
        self.program.reset_animation()
        self.program.currentAnimation = self.program.first_page['Home']

    def play_button(self, buttons):
        self.program.reset_animation()
        for button in buttons:
            if (button.button_type == Button_Type.AlgoButton and
                button.pressed == True):
                self.program.currentAnimation = self.program.animation[load_name(button.text)]
        
        self.dynamic_elevation = self.elevation
        self.dynamic_top_color = self.top_color
        self.pressed = False
    
    # when readme button is clicked
    def readme_button(self, buttons, rightScreen):
        val = False
        for button in buttons:
            if (button.button_type == Button_Type.AlgoButton and
                button.pressed == True):
                # have selected an algorithm and clicked readme button
                val = True
                rightScreen.update(button.text, Screen_Type.ReadMe)

            # if code button is currently clicked, it unclicks it
            elif button.button_type == Button_Type.CodeButton:
                button.dynamic_elevation = button.elevation
                button.dynamic_top_color = button.top_color
                button.pressed = False

        # clicked code button without selecting an algorithm   
        if not val:
            self.dynamic_elevation = self.elevation
            self.dynamic_top_color = self.top_color
            self.pressed = False

    # when code button is clicked
    def code_button(self, buttons, rightScreen):
        val = False
        for button in buttons:
            if (button.button_type == Button_Type.AlgoButton and
                button.pressed == True):
                # have selected an algorithm and clicked code button
                val = True
                rightScreen.update(button.text, Screen_Type.Code)
            
            # if read me button is currently clicked, it unclicks it
            elif button.button_type == Button_Type.ReadMeButton:
                button.dynamic_elevation = button.elevation
                button.dynamic_top_color = button.top_color
                button.pressed = False

        # clicked code button without selecting an algorithm
        if not val:
            self.dynamic_elevation = self.elevation
            self.dynamic_top_color = self.top_color
            self.pressed = False

    # when any of the alogrithms buttons are clicked              
    def algo_button(self, buttons, rightScreen):
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
                button.pressed = False

            # Turing on the readme_button
            elif button.button_type == Button_Type.ReadMeButton:
                button.dynamic_elevation = 0
                button.dynamic_top_color = self.clicked_color
                button.pressed = True
        
        # update the right screen
        rightScreen.update(self.text, Screen_Type.ReadMe)
        self.program.reset_animation()
        self.program.currentAnimation = self.program.first_page[load_name(self.text)]

    
            