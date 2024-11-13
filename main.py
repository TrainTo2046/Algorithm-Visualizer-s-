import sys
import pygame
from createButtons import ButtonList 
from rightScreen import Right_Screen
from animation import Animation
from utils import get_background_img, load_images

FIRST_PAGE = 'FirstPage/'
ANIMATION_PAGE = 'AlgoAnimation/'
TEST = 'testAnimation/'

class Algorithm_Visualizer:
    def __init__(self):
        pygame.init()

        SCREEN_WIDTH = 1024
        SCREEN_HEIGHT = 768
        
        pygame.display.set_caption('Algorithm Visualizer')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()

        # All Buttons
        allButtons = ButtonList(self)
        self.button_list = allButtons.get_button()

        # All Right Screens
        self.rightScreens = Right_Screen(self)

        # Animations
        self.animation = {
            'first': Animation(load_images(TEST + 'current'), img_dur = 30),
            'test': Animation(load_images(TEST + 'test'), img_dur = 30),
            'DFS': Animation(load_images(ANIMATION_PAGE + 'DFS'))
        }
        
        self.currentAnimation = self.animation['first']
        """
            'Bellman-Ford': Animation(load_images( 'Bellman-Ford')),
            'BFS': Animation(load_images('BFS')),
            'BinarySearch': Animation(load_images('BinarySearch')),
            'BubbleSort': Animation(load_images('BubbleSort')),
            'BucketSort': Animation(load_images('BucketSort')),
            'DFS': Animation(load_images('DFS')),
            'DijkstraAlgorithm': Animation(load_images('DijkstraAlgorithm')),
            'FloydsAlgorithm': Animation(load_images('FloydsAlgorithm')),
            'KruskalAlgorithm': Animation(load_images('KruskalAlgorithm')),
            'PrimsAlgorithm': Animation(load_images('PrimsAlgorithm')),
            'TopologicalSort': Animation(load_images('TopologicalSort')),
            'Union-Find': Animation(load_images('Union-Find')),
        """
        
    def reset_animation(self):
        for ani in self.animation:
            self.animation[ani].reset()

    def run(self):
        while True:
            self.screen.blit(get_background_img(), (0, 0))
            self.rightScreens.drawRightScreen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for button in self.button_list:
                button.draw()

            self.rightScreens.draw()
            
            self.currentAnimation.render_animation(self.screen)
            self.currentAnimation.update()

            pygame.display.update()
            self.clock.tick(24)

Algorithm_Visualizer().run()