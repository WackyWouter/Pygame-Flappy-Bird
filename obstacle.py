import pygame
from random import choice

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type, y):
        super().__init__()

        

        if type == 'up':
            beam_up_1 = pygame.image.load('assets/img/obstacles/beam-up1.png').convert_alpha()
            beam_up_1 = pygame.transform.scale(beam_up_1, (49, 400))
            beam_up_2 = pygame.image.load('assets/img/obstacles/beam-up2.png').convert_alpha()
            beam_up_2 = pygame.transform.scale(beam_up_2, (49, 400))
            beam_up_3 = pygame.image.load('assets/img/obstacles/beam-up3.png').convert_alpha()
            beam_up_3 = pygame.transform.scale(beam_up_3, (49, 400))
            self.image = choice([beam_up_1, beam_up_2, beam_up_3])
        else:
            beam_down_1 = pygame.image.load('assets/img/obstacles/beam-down1.png').convert_alpha()
            beam_down_1 = pygame.transform.scale(beam_down_1, (49, 400))
            beam_down_2 = pygame.image.load('assets/img/obstacles/beam-down2.png').convert_alpha()
            beam_down_2 = pygame.transform.scale(beam_down_2, (49, 400))
            self.image = choice([beam_down_1, beam_down_2])
            
        self.rect = self.image.get_rect(midtop = (500, y))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill

        