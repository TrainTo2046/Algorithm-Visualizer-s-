import sys
import pygame
from createButtons import ButtonList 
from rightScreen import Right_Screen
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
        allButtons = ButtonList()
        self.button_list = allButtons.get_button()

        # All Right Screens
        self.rightScreens = Right_Screen()

    def run(self):
        while True:
            self.screen.blit(get_background_img(), (0, 0))
            self.rightScreens.drawRightScreen(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for button in self.button_list:
                button.draw(self.screen, self.button_list, self.rightScreens)

            self.rightScreens.draw(self.screen)

            pygame.display.update()
            self.clock.tick(60)

Algorithm_Visualizer().run()