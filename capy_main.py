import pygame
import sys
import random
import threading
import time

pygame.init()

WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg_img = pygame.image.load('bg.png')
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
clock = pygame.time.Clock()

######################################################
player_image_original = pygame.image.load('capy.png')
player = pygame.transform.scale(player_image_original, (player_image_original.get_width() * 4, player_image_original.get_height() * 4))
player_x = 500
player_y = 300
######################################################

coins = 0
cpclick = 1 
cps = 0
upgrade_cost = int(250)
upgrade_2_cost = 500

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 45)


text_1 = font.render(f'Coins: {coins}', True, (0, 0, 0))
text_1_rect = text_1.get_rect()
text_1_rect.center = (200, 150)
text_2 = font.render(f'CPClick: {cpclick}', True, (0, 0, 0))
text_2_rect = text_2.get_rect()
text_2_rect.center = (200, 75)
text_3 = font.render(f'Upg. CPC [U]: {upgrade_cost}', True, (0, 0, 0))
text_3_rect = text_3.get_rect()
text_3_rect.center = (200, 225)
text_4 = font.render(f'CPS: {cps}', True, (0, 0, 0))
text_4_rect = text_4.get_rect()
text_4_rect.center = (600, 150)
text_5 = font.render(f'Upg. CPS [S]: {upgrade_2_cost}', True, (0, 0, 0))
text_5_rect = text_5.get_rect()
text_5_rect.center = (600, 225)
text_6 = font.render(f'Click!!! [SPACE]', True, (0, 0, 0))
text_6_rect = text_6.get_rect()
text_6_rect.center = (600, 600)

def click_per_second():
    global coins
    while True:
        time.sleep(1)
        coins += cps
        coins = round(coins)  
        text_1 = font.render(f'Coins: {coins}', True, (0, 0, 0))
        text_1_rect = text_1.get_rect()
        text_1_rect.center = (200, 150)
        screen.blit(text_1, text_1_rect)


my_thread = threading.Thread(target=click_per_second)
my_thread.start()

running = True
while running:
    text_6 = font.render(f'Click!!! [SPACE]', True, (0, 0, 0))
    text_6_rect = text_6.get_rect()
    text_6_rect.center = (600, 600)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                coins += cpclick
                text_1 = font.render(f'Coins: {coins}', True, (0, 0, 0))
                text_1_rect = text_1.get_rect()
                text_1_rect.center = (200, 150)
                text_3 = font.render(f'Upg. CPC [U]: {upgrade_cost}', True, (0, 0, 0))
                text_3_rect = text_3.get_rect()    
                text_3_rect.center = (200, 225)
            if event.key == pygame.K_u:
                if coins >= upgrade_cost:
                    coins -= upgrade_cost
                    cpclick += random.randint(0, 5)
                    upgrade_cost *= 1.2
                    upgrade_cost = int(upgrade_cost) 
                    text_1 = font.render(f'Coins: {coins}', True, (0, 0, 0))
                    text_1_rect = text_1.get_rect()
                    text_1_rect.center = (200, 150)
                    text_2 = font.render(f'CPClick: {cpclick}', True, (0, 0, 0))
                    text_2_rect = text_2.get_rect()
                    text_2_rect.center = (200, 75)
                    text_3 = font.render(f'Upg. CPC [U]: {upgrade_cost}', True, (0, 0, 0))
                    text_3_rect = text_3.get_rect()
                    text_3_rect.center = (200, 225)
                else:
                    print("No money")
            if event.key == pygame.K_s:
                if coins >= upgrade_2_cost:
                    coins -= upgrade_2_cost
                    cps += random.randint(0, 3)
                    upgrade_2_cost *= 1.2
                    upgrade_2_cost = int(upgrade_2_cost) 
                    text_1 = font.render(f'Coins: {coins}', True, (0, 0, 0))
                    text_1_rect = text_1.get_rect()
                    text_1_rect.center = (200, 150)
                    text_4_rect = text_4.get_rect()
                    text_4 = font.render(f'CPS: {cps}', True, (0, 0, 0))
                    text_4_rect = text_4.get_rect()
                    text_4_rect.center = (600, 150)
                    text_5 = font.render(f'Upg. CPS [S]: {upgrade_2_cost}', True, (0, 0, 0))
                    text_5_rect = text_5.get_rect()
                    text_5_rect.center = (600, 225)
                else:
                    print("No money")
    text_1 = font.render(f'Coins: {coins}', True, (0, 0, 0))
    text_1_rect = text_1.get_rect()
    text_1_rect.center = (200, 150)
    text_2 = font.render(f'CPClick: {cpclick}', True, (0, 0, 0))
    text_2_rect = text_2.get_rect()
    text_2_rect.center = (200, 75)
    text_3 = font.render(f'Upg. CPC [U]: {upgrade_cost}', True, (0, 0, 0))
    text_3_rect = text_3.get_rect()
    text_3_rect.center = (200, 225)
    text_4 = font.render(f'CPS: {cps}', True, (0, 0, 0))
    text_4_rect = text_4.get_rect()
    text_4_rect.center = (600, 150)
    text_5 = font.render(f'Upg. CPS [S]: {upgrade_2_cost}', True, (0, 0, 0))
    text_5_rect = text_5.get_rect()
    text_5_rect.center = (600, 225)       
    screen.blit(bg_img, (0, 0))
    screen.blit(text_1, text_1_rect)
    screen.blit(text_2, text_2_rect)
    screen.blit(text_3, text_3_rect)
    screen.blit(text_4, text_4_rect)
    screen.blit(text_5, text_5_rect)
    screen.blit(text_6, text_6_rect)
    screen.blit(player, (player_x, player_y))
    
    pygame.display.flip()
    clock.tick(30)
