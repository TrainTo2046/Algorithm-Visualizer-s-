import os
import pygame

BASE_CODE_TXT_PATH = 'CodeReadMe/'  # code path
BASE_README_TXT_PATH = 'AlgoReadMe/'    # readme path
BASE_BACKGROUND_IMG_PATH = 'Assets/BackgroundImage.png' # background image path
BASE_IMG_PATH = 'Assets/'   # animation + first image path

# loads all the read me txt
def load_readme(name):
    # gets the proper name to create the path (no spaces or tabs)
    n = load_name(name)

    path = BASE_README_TXT_PATH + n + ".txt"
    # open the file
    f = open(path)
    # read the file
    content = f.read().splitlines()
    f.close()
    
    # return the content
    return content

# removes any spaces for the name
def load_name(name):
    algo_name = name.split(" ")
    n = ""
    for str in algo_name:
        n += str
    
    return n

# loads all the Code txt
def load_code(name):
    # gets the proper name to create the path (no spaces or tabs)
    n = load_name(name)

    path = BASE_CODE_TXT_PATH + n + "Code.txt"
    f = open(path)
    content = f.read().splitlines()
    f.close()
    return content

# loads background image
def get_background_img():
    load_img =  pygame.image.load(BASE_BACKGROUND_IMG_PATH)
    img = pygame.transform.scale(load_img, (1024, 768))
    return img

# loads single frame from the path provided (FOR ANIMATION)
def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    return img

# loads all the frames for animation
def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))

    return images

