import pygame
import time

class Button():
    def __init__(self, x : int, y : int, image1, image2, image3, scale : float):
        width = image1.get_width()
        height = image1.get_height()
        self.image1 = pygame.transform.scale(image1, (int(width * scale), int(height * scale)))
        if image2:
            self.image2 = pygame.transform.scale(image2, (int(width * scale), int(height * scale)))
        else:
            self.image2 = pygame.transform.scale(image1, (int(width * scale), int(height * scale)))
        if image3:
            self.image3 = pygame.transform.scale(image3, (int(width * scale), int(height * scale)))
        else:
            self.image3 = pygame.transform.scale(image2, (int(width * scale), int(height * scale)))
        self.rect = self.image1.get_rect()
        self.rect.topleft = (x, y)
        self.clicked_l = False
        self.clicked_r = False

    def draw_l(self, surface, blocker : bool = False): # oddziałowuje na kliknięcia lewy przycisk myszy
        action = False
        pos = pygame.mouse.get_pos() # Pozycja myszki
        
        if self.clicked_l == False:
            surface.blit(self.image1, (self.rect.x, self.rect.y))        
        
        if self.rect.collidepoint(pos) and not blocker:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked_l:
                self.clicked_l = True
        
        if self.clicked_l == True:
            surface.blit(self.image2, (self.rect.x, self.rect.y))
            

        if pygame.mouse.get_pressed()[0] == 0 and self.clicked_l:
            self.clicked_l = False
            action = True
            time.sleep(0.3)

        return action
    
    def draw_l_r(self, surface, blocker :bool = False):
        action = False
        pos = pygame.mouse.get_pos() # Pozycja myszki
        
        if self.clicked_l == False:
            surface.blit(self.image1, (self.rect.x, self.rect.y))   
        
        if self.rect.collidepoint(pos) and not blocker:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked_l and not self.clicked_r:
                self.clicked_l = True
                action = 'left'

            if pygame.mouse.get_pressed()[2] == 1 and not self.clicked_l and not self.clicked_r:
                self.clicked_r = True
                action = 'right'

        if self.clicked_l == True:
            surface.blit(self.image2, (self.rect.x, self.rect.y))
        if self.clicked_r == True:
            surface.blit(self.image3, (self.rect.x, self.rect.y))

        
        return action