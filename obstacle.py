import pygame
from random import randint
from random import choice

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'up':
            beam_up_1 = pygame.image.load('img/obstacles/beam-up1.png').convert_alpha()
            beam_up_2 = pygame.image.load('img/obstacles/beam-up2.png').convert_alpha()
            beam_up_3 = pygame.image.load('img/obstacles/beam-up3.png').convert_alpha()
            self.image = choice([beam_up_1, beam_up_2, beam_up_3])
            self.rect = self.image.get_rect(midbottom = (500, randint(661, 861)))
        else:
            beam_down_1 = pygame.image.load('img/obstacles/beam-down1.png').convert_alpha()
            beam_down_2 = pygame.image.load('img/obstacles/beam-down2.png').convert_alpha()
            self.image = choice([beam_down_1, beam_down_2])
            self.rect = self.image.get_rect(midtop = (500, randint(-200, 0)))
        
    def update(self):
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill

        