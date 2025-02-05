import pygame
from sys import exit

def display_score(pos):
    score_surface = test_font1.render(f'SCORE: {score - start_score}', True, '#198A9C')
    score_rect = score_surface.get_rect(center = pos)
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surface, score_rect)

WIDTH, HEIGHT = 800, 400

game_active = False
score = 0

pygame.init() #initialising pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MY GAME')
clock = pygame.time.Clock()

start_score = 0
# current_time = pygame.time.get_ticks() - start_time

test_font1 = pygame.font.Font('font/Pixeltype.ttf', 50)
test_font2 = pygame.font.Font('font/Pixeltype.ttf', 100)

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

snail_surface = pygame.image.load('graphics/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (725, 300))

player_surface = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100, 300))
player_gravity = 0

play_surface = test_font1.render('Press to Play', True ,'#198A9C')
play_rect = play_surface.get_rect(center = (400, 250))

pixel_runner_surface = test_font2.render('Pixel Runner', True ,'#198A9C')
pixel_runner_rect = pixel_runner_surface.get_rect(center = (400, 100))

player_stand_surface = pygame.image.load('graphics/player_stand.png').convert_alpha()
player_stand_surface = pygame.transform.rotozoom(player_stand_surface, 0, 1.5)
player_stand_rect = player_stand_surface.get_rect(center = (180, 220))
player_stand_rect2 = player_stand_surface.get_rect(center = (620, 220))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #closes any code
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_gravity = -20
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20
    
        
    if game_active:
            
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
            
        snail_rect.left -= 8
        if snail_rect.right <= 0:
            snail_rect.left = 800
            score += 1
        screen.blit(snail_surface, snail_rect)
            
        display_score((400,40))
            # player_rect.left += 3
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300       
        screen.blit(player_surface, player_rect)
        
            
        if snail_rect.colliderect(player_rect):
            game_active = False
            
    
    else:
        screen.fill('#c0e8ec')
        screen.blit(pixel_runner_surface, pixel_runner_rect)
        pygame.draw.rect(screen, '#98CAD3', play_rect)
        pygame.draw.rect(screen, '#98CAD3', play_rect, 10)
        screen.blit(play_surface, play_rect)
        display_score((400, 200))
        screen.blit(player_stand_surface, player_stand_rect)
        screen.blit(player_stand_surface, player_stand_rect2)
    
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                game_active = True
                snail_rect.left = 725
                start_score = score
                # start_time = pygame.time.get_ticks()
        
        
    pygame.display.update()
    clock.tick(60) #setting the maximum framerate for the game