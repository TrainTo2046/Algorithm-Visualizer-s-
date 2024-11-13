import os
import pygame

BASE_CODE_TXT_PATH = 'CodeReadMe/'
BASE_README_TXT_PATH = 'AlgoReadMe/'
BASE_BACKGROUND_IMG_PATH = 'Assets/BackgroundImage.png'

BASE_IMG_PATH = 'Assets/'


def load_readme(name):
    algo_name = name.split(" ")
    n = ""
    for str in algo_name:
        n += str

    path = BASE_README_TXT_PATH + n + ".txt"
    f = open(path)
    content = f.read().splitlines()
    f.close()
    
    return content

def load_name(name):
    algo_name = name.split(" ")
    n = ""
    for str in algo_name:
        n += str
    
    return n

def load_code(name):
    algo_name = name.split(" ")
    n = ""
    for str in algo_name:
        n += str

    path = BASE_CODE_TXT_PATH + n + "Code.txt"
    f = open(path)
    content = f.read().splitlines()
    f.close()
    return content

def get_background_img():
    load_img =  pygame.image.load(BASE_BACKGROUND_IMG_PATH)
    img = pygame.transform.scale(load_img, (1024, 768))
    return img

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))

    return images

