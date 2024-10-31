import sys
import pygame
import button
import rightScreen
import createButtons
import createRightScreen
from utils import get_background_img

class Algorithm_Visualizer:
    def __init__(self):
        pygame.init()

        SCREEN_WIDTH = 1024
        SCREEN_HEIGHT = 768
        
        pygame.display.set_caption('Algorithm Visualizer')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()

        # All Buttons
        allButtons = createButtons.ButtonList()
        self.button_list = allButtons.get_button()

        # All Right Screens
        allScreens = createRightScreen.RightScreenList()
        self.readme_map = allScreens.get_readMe()
        self.code_map = allScreens.get_code()

    def run(self):
        while True:
            self.screen.blit(get_background_img(), (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for button in self.button_list:
                button.draw(self.screen)
            
            for button in self.button_list:
                button.check_click(self.button_list, self.readme_map, self.code_map)

            for name in self.code_map.keys():
                self.code_map[name].draw(self.screen)
                
            for name in self.readme_map.keys():
                self.readme_map[name].draw(self.screen)

            pygame.display.update()
            self.clock.tick(60)

Algorithm_Visualizer().run()