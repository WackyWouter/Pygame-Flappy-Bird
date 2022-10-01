import pygame
from bean import Bean
from debug import debug

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = font.render(str(current_time), False, (64,64,64))
    score_rect = score_surf.get_rect(topright = (475, 25))
    screen.blit(score_surf, score_rect)
    
    return current_time

# Setup
pygame.init()
pygame.display.set_caption('Flappy Bean')
font = pygame.font.Font('font/ka1.ttf', 30)
screen = pygame.display.set_mode((500, 772))
clock = pygame.time.Clock()
game_state = 'menu'
start_time = 0
score = 0


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

# Bean
bean = pygame.sprite.GroupSingle()
bean.add(Bean())

while True:
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

    screen.blit(sky_surf, (0, 0))
    screen.blit(floor_surf, floor_rect)

    # Menu
    if game_state == 'menu':
        screen.blit(play_surf, play_rect)
        screen.blit(game_name_surf, game_name_rect)

    elif game_state == 'playing':
        # Bean
        bean.draw(screen)
        bean.update()

        # Score
        score = display_score()

        # If top or bottom of the screen is touched it's game over
        if bean.sprite.rect.y <= 0 or bean.sprite.rect.y >= 661:
            game_state = 'game over'
    
    pygame.display.update()
    clock.tick(60)