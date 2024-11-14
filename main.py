import sys
import pygame
from createButtons import ButtonList 
from rightScreen import Right_Screen
from animation import Animation
from utils import get_background_img, load_images

# First Page consists of the first frame of animation
FIRST_PAGE = 'FirstPage/'
# Animation Page consists of all the frames of animation
ANIMATION_PAGE = 'AlgoAnimation/'

class Algorithm_Visualizer:
    def __init__(self):
        # initalize pygame
        pygame.init()

        # width of the screen
        SCREEN_WIDTH = 1024
        # height of the screen
        SCREEN_HEIGHT = 768
        
        # Caption for the program window
        pygame.display.set_caption('Algorithm Visualizer')
        # creating the program window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # allows the game to run at n frames per sec
        self.clock = pygame.time.Clock()

        # All Buttons
        self.allButtons = ButtonList(self)

        # All Right Screens
        self.rightScreens = Right_Screen(self)

        # Animations
        self.animation = {
            'DFS': Animation(load_images(ANIMATION_PAGE + 'DFS'), img_dur= 70),
            'Bellman-Ford': Animation(load_images(ANIMATION_PAGE + 'Bellman-Ford'), img_dur= 100),
            'BFS': Animation(load_images(ANIMATION_PAGE + 'BFS'), img_dur= 70),
            'BinarySearch': Animation(load_images(ANIMATION_PAGE + 'BinarySearch'), img_dur= 60),
            'BubbleSort': Animation(load_images(ANIMATION_PAGE + 'BubbleSort'), img_dur= 70),
            'BucketSort': Animation(load_images(ANIMATION_PAGE + 'BucketSort'), img_dur= 50),
            'DijkstraAlgorithm': Animation(load_images(ANIMATION_PAGE + 'DijkstraAlgorithm'), img_dur= 70),
            'FloydsAlgorithm': Animation(load_images(ANIMATION_PAGE + 'FloydsAlgorithm'), img_dur= 50),
            'KruskalAlgorithm': Animation(load_images(ANIMATION_PAGE + 'KruskalAlgorithm'), img_dur= 70),
            'PrimsAlgorithm': Animation(load_images(ANIMATION_PAGE + 'PrimsAlgorithm'), img_dur= 70),
            'TopologicalSort': Animation(load_images(ANIMATION_PAGE + 'TopologicalSort'), img_dur= 70),
            'Union-Find': Animation(load_images(ANIMATION_PAGE + 'Union-Find'), img_dur= 50),
        }
        
        # first page
        self.first_page = {
            'Home': Animation(load_images(FIRST_PAGE + 'Home')),
            'DFS': Animation(load_images(FIRST_PAGE + 'DFS')),
            'Bellman-Ford': Animation(load_images(FIRST_PAGE + 'Bellman-Ford')),
            'BFS': Animation(load_images(FIRST_PAGE + 'BFS')),
            'BinarySearch': Animation(load_images(FIRST_PAGE + 'BinarySearch')),
            'BubbleSort': Animation(load_images(FIRST_PAGE + 'BubbleSort')),
            'BucketSort': Animation(load_images(FIRST_PAGE + 'BucketSort')),
            'DFS': Animation(load_images(FIRST_PAGE + 'DFS')),
            'DijkstraAlgorithm': Animation(load_images(FIRST_PAGE + 'DijkstraAlgorithm')),
            'FloydsAlgorithm': Animation(load_images(FIRST_PAGE + 'FloydsAlgorithm')),
            'KruskalAlgorithm': Animation(load_images(FIRST_PAGE + 'KruskalAlgorithm')),
            'PrimsAlgorithm': Animation(load_images(FIRST_PAGE + 'PrimsAlgorithm')),
            'TopologicalSort': Animation(load_images(FIRST_PAGE + 'TopologicalSort')),
            'Union-Find': Animation(load_images(FIRST_PAGE + 'Union-Find')),
        }
        
        # animating either only the first page or the entire animation
        self.currentAnimation = self.first_page['Home']
    
    # sets all the animation back to start
    def reset_animation(self):
        for ani in self.animation:
            self.animation[ani].reset()

    def run(self):
        # game loop
        while True:
            # places the background on the screen
            self.screen.blit(get_background_img(), (0, 0))
            # draws the right screen to put the readme and code descriptions
            self.rightScreens.drawRightScreen()

            # event handler
            for event in pygame.event.get():
                # when clicked exit button, program quits
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # draws all the buttons
            self.allButtons.draw()

            # draws the current right screen
            self.rightScreens.draw()
            
            # runs the current animation
            self.currentAnimation.render_animation(self.screen)
            # updates the current frame of the animation
            self.currentAnimation.update()

            pygame.display.update()
            # running the program 24 frames per second
            self.clock.tick(24)

# runs the visualizer
Algorithm_Visualizer().run()