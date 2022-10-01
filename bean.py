import pygame

class Bean (pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('img/player/bean-small1.png').convert_alpha()
        self.rect = self.image.get_rect(center = (250, 386))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity = -10

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity

    def update(self):
        self.player_input()
        self.apply_gravity()
