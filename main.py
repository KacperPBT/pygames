import pygame
import button
import time
pygame.init()

#=============================================================================================#
#                                            Ekran                                            #
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Kółko i krzyżyk')
surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
pygame.draw.rect(surface, (222, 224, 224, 200), (0,0,SCREEN_WIDTH, SCREEN_HEIGHT))
#=============================================================================================#

#=============================================================================================#
#                                           zdjęcia                                           #
start_img = pygame.image.load('image/start_button.png').convert_alpha()
start_act_img = pygame.image.load('image/start_button_active.png').convert_alpha()
exit_img = pygame.image.load('image/exit_button.png').convert_alpha()
exit_act_img = pygame.image.load('image/exit_button_active.png').convert_alpha()
panel_with_circle = pygame.image.load('image/panel_with_circle.png').convert_alpha()
panel_with_cross = pygame.image.load('image/panel_with_cross.png').convert_alpha()
panel = pygame.image.load('image/panel.png').convert_alpha()
#=============================================================================================#

#=============================================================================================#
#                                           Buttony                                           #
start_button = button.Button(30, 200, start_img, start_act_img,None, 1)
exit_button = button.Button(280, 200, exit_img, exit_act_img,None, 1)
panel_button00 = button.Button(96 , 96 , panel,panel_with_circle,panel_with_cross, 1) # 1
panel_button01 = button.Button(96 , 200, panel,panel_with_circle,panel_with_cross, 1) # 2
panel_button02 = button.Button(96 , 304, panel,panel_with_circle,panel_with_cross, 1) # 3
panel_button10 = button.Button(200, 96 , panel,panel_with_circle,panel_with_cross, 1) # 4
panel_button11 = button.Button(200, 200, panel,panel_with_circle,panel_with_cross, 1) # 5
panel_button12 = button.Button(200, 304, panel,panel_with_circle,panel_with_cross, 1) # 6
panel_button20 = button.Button(304, 96 , panel,panel_with_circle,panel_with_cross, 1) # 7
panel_button21 = button.Button(304, 200, panel,panel_with_circle,panel_with_cross, 1) # 8
panel_button22 = button.Button(304, 304, panel,panel_with_circle,panel_with_cross, 1) # 9
#=============================================================================================#
#                                          Game loop                                          #

def starting_settings():
    global game_blocker
    game_blocker = False
    global sleep_blocker
    sleep_blocker = False
    global winner
    winner = None
    global state
    state = 'menu'
    global run
    run = True
    global pb00a # 1
    global pb01a # 2
    global pb02a # 3
    global pb10a # 4
    global pb11a # 5
    global pb12a # 6
    global pb20a # 7
    global pb21a # 8
    global pb22a # 9
    pb00a = 'free' # 1
    pb01a = 'free' # 2
    pb02a = 'free' # 3
    pb10a = 'free' # 4
    pb11a = 'free' # 5
    pb12a = 'free' # 6
    pb20a = 'free' # 7
    pb21a = 'free' # 8
    pb22a = 'free' # 9

starting_settings()


while run:

    screen.fill((202, 228, 241))
    if state == 'menu':
        if start_button.draw_l(screen):
            state = 'gra'

        if exit_button.draw_l(screen):
            run = False
    
    if state == 'game over':
        game_blocker = True
        if not sleep_blocker:
            time.sleep(0.5)
            sleep_blocker = True
        

    if state == 'gra' or state == 'game over':
        
        
        pb00 = panel_button00.draw_l_r(screen, game_blocker) # 1
        pb01 = panel_button01.draw_l_r(screen, game_blocker) # 2
        pb02 = panel_button02.draw_l_r(screen, game_blocker) # 3
        pb10 = panel_button10.draw_l_r(screen, game_blocker) # 4
        pb11 = panel_button11.draw_l_r(screen, game_blocker) # 5
        pb12 = panel_button12.draw_l_r(screen, game_blocker) # 6
        pb20 = panel_button20.draw_l_r(screen, game_blocker) # 7
        pb21 = panel_button21.draw_l_r(screen, game_blocker) # 8
        pb22 = panel_button22.draw_l_r(screen, game_blocker) # 9

        if not winner:
            if pb00a == 'free': # 1
                if pb00 == "left":
                    pb00a = 'left'
                elif pb00 == "right":
                    pb00a = 'right'
            if pb01a == 'free': # 2
                if pb01 == "left":
                    pb01a = 'left'
                elif pb01 == "right":
                    pb01a = 'right'
            if pb02a == 'free': # 3
                if pb02 == "left":
                    pb02a = 'left'
                elif pb02 == "right":
                    pb02a = 'right'
            if pb10a == 'free': # 4
                if pb10 == "left":
                    pb10a = 'left'
                elif pb10 == "right":
                    pb10a = 'right'
            if pb11a == 'free': # 5
                if pb11 == "left":
                    pb11a = 'left'
                elif pb11 == "right":
                    pb11a = 'right'
            if pb12a == 'free': # 6
                if pb12 == "left":
                    pb12a = 'left'
                elif pb12 == "right":
                    pb12a = 'right'
            if pb20a == 'free': # 7
                if pb20 == "left":
                    pb20a = 'left'
                elif pb20 == "right":
                    pb20a = 'right'
            if pb21a == 'free': # 8
                if pb21 == "left":
                    pb21a = 'left'
                elif pb21 == "right":
                    pb21a = 'right'
            if pb22a == 'free': # 9
                if pb22 == "left":
                    pb22a = 'left'
                elif pb22 == "right":
                    pb22a = 'right'

        if not winner:
            if pb00a == pb01a == pb02a:
                if pb00a == "left":
                    state = 'game over'
                    winner = 'Player 1'
                if pb00a == "right":
                    state = 'game over'
                    winner = 'Player 2'
            if pb10a == pb11a == pb12a:
                if pb10a == "left":
                    state = 'game over'
                    winner = 'Player 1'
                if pb10a == "right":
                    state = 'game over'
                    winner = 'Player 2'
            if pb20a == pb21a == pb22a:
                if pb20a == "left":
                    state = 'game over'
                    winner = 'Player 1'
                if pb20a == "right":
                    state = 'game over'
                    winner = 'Player 2'
            if pb00a == pb10a == pb20a:
                if pb00a == "left":
                    state = 'game over'
                    winner = 'Player 1'
                if pb00a == "right":
                    state = 'game over'
                    winner = 'Player 2'
            if pb01a == pb11a == pb21a:
                if pb01a == "left":
                    state = 'game over'
                    winner = 'Player 1'
                if pb01a == "right":
                    state = 'game over'
                    winner = 'Player 2'
            if pb02a == pb12a == pb22a:
                if pb02a == "left":
                    state = 'game over'
                    winner = 'Player 1'
                if pb02a == "right":
                    state = 'game over'
                    winner = 'Player 2'
            if pb00a == pb11a == pb22a:
                if pb00a == "left":
                    state = 'game over'
                    winner = 'Player 1'
                if pb00a == "right":
                    state = 'game over'
                    winner = 'Player 2'
            if pb02a == pb11a == pb20a:
                if pb02a == "left":
                    state = 'game over'
                    winner = 'Player 1'
                if pb02a == "right":
                    state = 'game over'
                    winner = 'Player 2'
    
    if sleep_blocker and state == 'game over':
        screen.blit(surface, (0,0))
        if pygame.mouse.get_pressed()[1] == 1:
            state = "menu"
            panel_button00.clicked_l, panel_button01.clicked_l, panel_button02.clicked_l, panel_button10.clicked_l, panel_button11.clicked_l, panel_button12.clicked_l, panel_button20.clicked_l, panel_button21.clicked_l, panel_button22.clicked_l, panel_button00.clicked_r, panel_button01.clicked_r, panel_button02.clicked_r, panel_button10.clicked_r, panel_button11.clicked_r, panel_button12.clicked_r, panel_button20.clicked_r, panel_button21.clicked_r, panel_button22.clicked_r = False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False
            starting_settings()

    for event in pygame.event.get(): # Event handler

        if event.type == pygame.QUIT: # Quit game
            run = False

    pygame.display.update()

pygame.quit()