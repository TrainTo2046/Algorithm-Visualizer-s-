import pygame
import button
import rightScreen
import createButtons
import createRightScreen
import screenAttributes

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Algorithm Visualizer')
image =  pygame.image.load('Visualizer/Assets/BackgroundImage.png')
clock = pygame.time.Clock()

def Background(image):
    size = pygame.transform.scale(image, (1024, 768))
    screen.blit(size, (0, 0))

# All Buttons
allButtons = createButtons.ButtonList()
button_list = allButtons.get_button()

# All Right Screens
allScreens = createRightScreen.RightScreenList()
readme_map = allScreens.get_readMe()
code_map = allScreens.get_code()

run = True
while run:
    Background(image)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for button in button_list:
        button.draw(screen)
    
    for button in button_list:
        button.check_click(button_list, readme_map, code_map)

    for name in code_map.keys():
        code_map[name].draw(screen)
        
    for name in readme_map.keys():
        readme_map[name].draw(screen)

    

    pygame.display.update()

pygame.quit()