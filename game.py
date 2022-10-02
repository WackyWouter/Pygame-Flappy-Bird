import pygame
from bean import Bean
from obstacle import Obstacle
from debug import debug

class Game:
    def __init__(self):
        # Setup
        pygame.init()
        pygame.display.set_caption('Flappy Bean')
        self.font = pygame.font.Font('font/ka1.ttf', 30)
        self.font_small = pygame.font.Font('font/ka1.ttf', 17)
        self.screen = pygame.display.set_mode((500, 772))
        self.clock = pygame.time.Clock()
        self.game_state = 'menu'
        self.start_time = 0
        self.score = 0
        self.top_score = 0

        # Background
        self.sky_surf = pygame.image.load('img/background/background.png').convert()
        self.sky_surf = pygame.transform.scale(self.sky_surf, (500, 772))
        self.floor_surf = pygame.image.load('img/background/floor.png').convert()
        self.floor_surf = pygame.transform.scale(self.floor_surf, (500, 111))
        self.floor_rect = self.floor_surf.get_rect(bottomleft = (0, 772))

        # Menu
        self.play_surf = pygame.image.load('img/menu/play.png').convert_alpha()
        self.play_rect = self.play_surf.get_rect(center = (250, 550))
        self.game_name_surf = pygame.image.load('img/menu/game-name.png').convert_alpha()
        self.game_name_rect = self.game_name_surf.get_rect(center = (250, 150))

        # Game over
        self.game_over_surf = pygame.image.load('img/menu/gameover.png').convert_alpha()
        self.game_over_rect = self.game_over_surf.get_rect(center = (250, 250))
        self.score_screen_surf = pygame.image.load('img/menu/score.png').convert_alpha()
        self.score_screen_rect = self.score_screen_surf.get_rect(center = (250, 350))
        self.gold_medal_surf = pygame.image.load('img/menu/gold.png').convert_alpha()
        self.gold_medal_rect = self.gold_medal_surf.get_rect(center = (197, 350))
        self.silver_medal_surf = pygame.image.load('img/menu/silver.png').convert_alpha()
        self.silver_medal_rect = self.silver_medal_surf.get_rect(center = (197, 350))
        self.reset_game_surf = self.font_small.render('Press space to restart', False, (64,64,64))
        self.reset_game_rect = self.reset_game_surf.get_rect(center = (250, 425))

        # Bean
        self.bean = pygame.sprite.GroupSingle()
        self.bean.add(Bean())

        # Obstacle
        self.obstacle_group = pygame.sprite.Group()

        # Timers
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 750)
        
    def display_score(self):
        current_time = int(pygame.time.get_ticks() / 1000) - self.start_time
        score_surf = self.font.render(str(current_time), False, (64,64,64))
        score_rect = score_surf.get_rect(topright = (475, 25))
        self.screen.blit(score_surf, score_rect)
        
        return current_time

    def collision_sprite(self):
        # If bean touches a beam its game over OR if top or bottom of the screen is touched it's game over
        if pygame.sprite.spritecollide(self.bean.sprite, self.obstacle_group, False, pygame.sprite.collide_mask):
            if pygame.sprite.spritecollide(self.bean.sprite, self.obstacle_group, False, pygame.sprite.collide_mask):
                return 'game over'
        elif (self.bean.sprite.rect.y <= 0 or self.bean.sprite.rect.y >= 661):
            return 'game over'
        return 'playing'

    def run(self):

        while True:

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                # check if the user clicks the play button or presses space to start
                if self.game_state == 'menu': 
                    pos = pygame.mouse.get_pos()
                    if (event.type == pygame.MOUSEBUTTONUP and self.play_rect.collidepoint(event.pos)) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                        self.game_state = 'playing'
                        self.start_time = int(pygame.time.get_ticks() / 1000)

                elif self.game_state == 'playing':
                    if event.type == self.obstacle_timer:
                        self.obstacle_group.add(Obstacle('up')) 
                        self.obstacle_group.add(Obstacle('down')) 
                
                else:
                    # Reset the game when its game over
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        print('reset')
                        self.bean.sprite.rect.y = 250
                        self.start_time = int(pygame.time.get_ticks() / 1000)
                        self.obstacle_group.empty()
                        self.game_state = 'playing'

            self.screen.blit(self.sky_surf, (0, 0))
            self.bean.draw(self.screen)

            # Menu
            if self.game_state == 'menu':
                self.screen.blit(self.play_surf, self.play_rect)
                self.screen.blit(self.game_name_surf, self.game_name_rect)

            elif self.game_state == 'playing':
                # Bean
                self.bean.update()

                # Obstacle
                self.obstacle_group.draw(self.screen)
                self.obstacle_group.update()
                self.screen.blit(self.floor_surf, self.floor_rect)

                # Score
                self.score = self.display_score()
                if self.score > self.top_score:
                    self.top_score = self.score

                # Collision
                self.game_state = self.collision_sprite()

            else: 
                # Score
                score_surf = self.font_small.render(str(self.score), False, (64,64,64))
                score_rect = score_surf.get_rect(center = (335, 327))
                # Top score
                top_score_surf = self.font_small.render(str(self.top_score), False, (64,64,64))
                top_score_rect = top_score_surf.get_rect(center = (335, 367))

                # Show menu on the screen
                self.screen.blit(self.game_over_surf, self.game_over_rect)
                self.screen.blit(self.score_screen_surf, self.score_screen_rect)
                self.screen.blit(top_score_surf, top_score_rect)
                self.screen.blit(score_surf, score_rect)
                self.screen.blit(self.reset_game_surf, self.reset_game_rect)

                # display score 
                if self.score > 100:
                    self.screen.blit(self.gold_medal_surf, self.gold_medal_rect)
                elif self.score > 50:
                    self.screen.blit(self.silver_medal_surf, self.silver_medal_rect)

                self.score = 0
            
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()