import pygame

class Animation:
    def __init__(self, images, img_dur =40):
        self.images = images
        self.img_duration = img_dur
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.img_duration)
    
    def update(self):
        self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
        if self.frame >= self.img_duration * len(self.images) - 1:
            self.done = True
    
    def reset(self):
        self.frame = 0
        self.done = False

    def img(self):
        return self.images[int(self.frame / self.img_duration)]

    def render_animation(self, screen):
        self.middle_rect = pygame.Rect((0, 0), (453, 705), border_radius = 5)
        img = pygame.transform.scale(self.img(), (453, 705))
        screen.blit(img, (217, 44), area=self.middle_rect)