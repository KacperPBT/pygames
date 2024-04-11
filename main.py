import pygame
import os
import sys
import button
from config import *
from modules import *

current_file_path = os.path.abspath(__file__)
current_dir = os.getcwd()
current_file_path = current_file_path.replace("\\main.py", "")
if current_dir != current_file_path:
    os.chdir(current_file_path)

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('Kółko i krzyżyk')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = Running_status()

        self.start_img = pygame.image.load('image/start_button.png').convert_alpha()
        self.start_act_img = pygame.image.load('image/start_button_active.png').convert_alpha()
        self.exit_img = pygame.image.load('image/exit_button.png').convert_alpha()
        self.exit_act_img = pygame.image.load('image/exit_button_active.png').convert_alpha()
        self.panel_with_circle = pygame.image.load('image/panel_with_circle.png').convert_alpha()
        self.panel_with_cross = pygame.image.load('image/panel_with_cross.png').convert_alpha()
        self.panel = pygame.image.load('image/panel.png').convert_alpha()
        self.game_ovre_img = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(self.game_ovre_img, (222, 224, 224, 200), (0,0,SCREEN_WIDTH, SCREEN_HEIGHT))


    def new(self):
        self.winner = None
        self.run.game_over = False
        self.button_list = []
        for i in range(3):
            mini_button_list = []
            for j in range(3):
                mini_button_list.append(button.Image_only((96+i*104, 96+j*104), self.panel, self.panel_with_circle, self.panel_with_cross))
            self.button_list.append(mini_button_list)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run.running = False
                self.run.playing = False
                self.run.menu = False

    def update(self):
        if self.run.game_over:
            self.screen.blit(self.game_ovre_img,(0,0))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.run.menu = True
                self.run.playing = False
        if not self.run.game_over:
            self.button_list_action = []
            for i in range(3):
                mini_list = []
                for j in range(3):
                    self.button_list[i][j].right(True)
                    self.button_list[i][j].left(True)
                    mini_list.append(self.button_list[i][j].get_state())
                self.button_list_action.append(mini_list)

    def draw(self):
        for i in range(3):
            for j in range(3):
                self.button_list[i][j].draw(self.screen)
        pygame.display.update()

    def check_win(self):
        for i in range((len(WINING))):
            if self.button_list_action[WINING[i][0][0]][WINING[i][0][1]] == self.button_list_action[WINING[i][1][0]][WINING[i][1][1]] == self.button_list_action[WINING[i][2][0]][WINING[i][2][1]]:
                if self.button_list_action[WINING[i][0][0]][WINING[i][0][1]] == "left":
                    self.winner = "Player"
                    self.run.game_over = True
                if self.button_list_action[WINING[i][0][0]][WINING[i][0][1]] == "right":
                    self.winner = "AI"
                    self.run.game_over = True

    def main(self):
        if not self.run.playing or not self.run.running:
            return
        self.new()
        while self.run.playing:
            self.screen.fill((202, 228, 241))
            self.events()
            self.update()
            self.draw()
            self.check_win()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_F5]:
                self.new()

    def menu(self):
        if not self.run.menu or not self.run.running:
            return
        start_button = button.Image_only((30, 200), self.start_img, self.start_act_img)
        exit_button = button.Image_only((280, 200), self.exit_img, self.exit_act_img)
        while self.run.menu:
            self.screen.fill((202, 228, 241))
            self.events()
            start_button.draw(self.screen)
            exit_button.draw(self.screen)
            
            if start_button.left():
                self.run.menu = False
                self.run.playing = True

            if exit_button.left():
                self.run.menu = False
                self.run.running = False

            pygame.display.update()



g = Game()
while g.run.running:
    g.menu()
    g.main()
    print(g.button_list_action)
    print(g.winner)
    # g.game_over()
pygame.quit()
sys.exit()
            