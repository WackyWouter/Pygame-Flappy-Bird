import pygame
from bean import Bean
from obstacle import Obstacle
from debug import debug

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = font.render(str(current_time), False, (64,64,64))
    score_rect = score_surf.get_rect(topright = (475, 25))
    screen.blit(score_surf, score_rect)
    
    return current_time

def collision_sprite():
    # If bean touches a beam its game over OR if top or bottom of the screen is touched it's game over
    if (pygame.sprite.spritecollide(bean.sprite, obstacle_group, False)) or (bean.sprite.rect.y <= 0 or bean.sprite.rect.y >= 661):
        return 'game over'
    else: return 'playing'

# Setup
pygame.init()
pygame.display.set_caption('Flappy Bean')
font = pygame.font.Font('font/ka1.ttf', 30)
font_small = pygame.font.Font('font/ka1.ttf', 17)
screen = pygame.display.set_mode((500, 772))
clock = pygame.time.Clock()
game_state = 'menu'
start_time = 0
score = 0
top_score = 0

# Background
sky_surf = pygame.image.load('img/background/background.png').convert()
sky_surf = pygame.transform.scale(sky_surf, (500, 772))
floor_surf = pygame.image.load('img/background/floor.png').convert()
floor_surf = pygame.transform.scale(floor_surf, (500, 111))
floor_rect = floor_surf.get_rect(bottomleft = (0, 772))

# Menu
play_surf = pygame.image.load('img/menu/play.png').convert_alpha()
play_rect = play_surf.get_rect(center = (250, 550))
game_name_surf = pygame.image.load('img/menu/game-name.png').convert_alpha()
game_name_rect = game_name_surf.get_rect(center = (250, 150))

# Game over
game_over_surf = pygame.image.load('img/menu/gameover.png').convert_alpha()
game_over_rect = game_over_surf.get_rect(center = (250, 250))
score_screen_surf = pygame.image.load('img/menu/score.png').convert_alpha()
score_screen_rect = score_screen_surf.get_rect(center = (250, 350))
gold_medal_surf = pygame.image.load('img/menu/gold.png').convert_alpha()
gold_medal_rect = gold_medal_surf.get_rect(center = (197, 350))
silver_medal_surf = pygame.image.load('img/menu/silver.png').convert_alpha()
silver_medal_rect = silver_medal_surf.get_rect(center = (197, 350))
reset_game_surf = font_small.render('Press space to restart', False, (64,64,64))
reset_game_rect = reset_game_surf.get_rect(center = (250, 425))

# Bean
bean = pygame.sprite.GroupSingle()
bean.add(Bean())

# Obstacle
obstacle_group = pygame.sprite.Group()

# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 750)

while True:
    print(score)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # check if the user clicks the play button or presses space to start
        if game_state == 'menu': 
            post = pygame.mouse.get_pos()
            if (event.type == pygame.MOUSEBUTTONUP and play_rect.collidepoint(event.pos)) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                game_state = 'playing'
                start_time = int(pygame.time.get_ticks() / 1000)

        elif game_state == 'playing':
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle('up')) 
                obstacle_group.add(Obstacle('down')) 
        
        else:
            # Reset the game when its game over
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                print('reset')
                bean.sprite.rect.y = 250
                start_time = int(pygame.time.get_ticks() / 1000)
                obstacle_group.empty()
                game_state = 'playing'

    screen.blit(sky_surf, (0, 0))
    bean.draw(screen)

    # Menu
    if game_state == 'menu':
        screen.blit(play_surf, play_rect)
        screen.blit(game_name_surf, game_name_rect)

    elif game_state == 'playing':
        # Bean
        bean.update()

        # Obstacle
        obstacle_group.draw(screen)
        obstacle_group.update()
        screen.blit(floor_surf, floor_rect)

        # Score
        score = display_score()
        if score > top_score:
            top_score = score

        # Collision
        game_state = collision_sprite()

    else: 
        # Score
        score_surf = font_small.render(str(score), False, (64,64,64))
        score_rect = score_surf.get_rect(center = (335, 327))
        # Top score
        top_score_surf = font_small.render(str(top_score), False, (64,64,64))
        top_score_rect = top_score_surf.get_rect(center = (335, 367))

        # Show menu on the screen
        screen.blit(game_over_surf, game_over_rect)
        screen.blit(score_screen_surf, score_screen_rect)
        screen.blit(top_score_surf, top_score_rect)
        screen.blit(score_surf, score_rect)
        screen.blit(reset_game_surf, reset_game_rect)

        # display score 
        if score > 100:
            screen.blit(gold_medal_surf, gold_medal_rect)
        elif score > 50:
            screen.blit(silver_medal_surf, silver_medal_rect)

        score = 0
    
    pygame.display.update()
    clock.tick(60)