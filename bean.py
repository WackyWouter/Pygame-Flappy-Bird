import pygame

class Bean (pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        bean_image_1 = pygame.image.load('img/player/bean-small1.png').convert_alpha()
        bean_image_2 = pygame.image.load('img/player/bean-small3.png').convert_alpha()
        self.bean_dead = pygame.image.load('img/player/dead-bean.png').convert_alpha()

        self.bean_fly = [bean_image_1, bean_image_2]
        self.bean_index = 0
        self.player_jump = pygame.image.load('img/player/bean-small2.png').convert_alpha()

        self.image = self.bean_fly[self.bean_index]
        self.rect = self.image.get_rect(center = (250, 386))
        self.gravity = 0
        self.mask = pygame.mask.from_surface(self.image)


    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity = -10

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity

    def animation_state(self):
        self.bean_index += 0.1
        if self.bean_index >= len(self.bean_fly): self.bean_index = 0
        self.image = self.bean_fly[int(self.bean_index)]

    def dead(self):
        self.image = self.bean_dead

    def update(self, game_state):
        if game_state == 'playing':
            self.animation_state()
            self.player_input()
            self.apply_gravity()
        else:
            self.dead()
        
