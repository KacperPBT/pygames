#=============================================================================#
#                                   library                                   #
import pygame
#=============================================================================#
class Image_only():
    Surface = pygame.surface.Surface
    def __init__(self,
                 coordinates : tuple,
                 image1: Surface | str,
                 image2: Surface | str = None,
                 image3: Surface | str = None,
                 width : int = None, 
                 height: int = None) -> None:
        self.__state = None
        # \/ photo processing \/
        if not image2:
            image2 = image1
        if not image3:
            if image2:
                image3 = image2
            else:
                image3 = image1
        if type(image1) == str:
            image1 = pygame.image.load(image1)
            image2 = pygame.image.load(image2)
            image3 = pygame.image.load(image3)
        if not width:
            width = image1.get_width()
        if not height:
            height = image1.get_height()
        self.image1 = pygame.transform.scale(image1, (int(width), int(height)))
        self.image2 = pygame.transform.scale(image2, (int(width), int(height)))
        self.image3 = pygame.transform.scale(image3, (int(width), int(height)))
        self.rect = self.image1.get_rect()
        self.rect.topleft = coordinates
    #=========================================================================#
    #                       Draw your button on surface                       #
    def draw(self, surface: Surface):
        if self.__state == None:
            surface.blit(self.image1, (self.rect.x, self.rect.y))
        if self.__state == "left":
            surface.blit(self.image2, (self.rect.x, self.rect.y))
        if self.__state == "right":
            surface.blit(self.image3, (self.rect.x, self.rect.y))
    #=========================================================================#
    #                       Affects on left mouse clicks                      #
    def left(self, act_after_pres : bool = False, blocker : bool = False) -> bool:
        aap = act_after_pres
        pos = pygame.mouse.get_pos() # Mouse position
        if self.rect.collidepoint(pos) and not blocker:
            if pygame.mouse.get_pressed()[0] == 1 and self.__state == None:
                self.__state = "left"
                if aap:
                    return True
        if not aap:
            if pygame.mouse.get_pressed()[0] == 0 and self.__state == "left":
                self.__state = None
                if self.rect.collidepoint(pos):
                    return True
        return False
    #=========================================================================#
    #                      Affects on right mouse clicks                      #
    def right(self, act_after_pres : bool = False, blocker : bool = False) -> bool:
        aap = act_after_pres
        pos = pygame.mouse.get_pos() # Mouse position
        if self.rect.collidepoint(pos) and not blocker:
            if pygame.mouse.get_pressed()[2] == 1 and  self.__state == None:
                self.__state = "right"
                if aap:
                    return True
        if not aap:
            if pygame.mouse.get_pressed()[0] == 0 and self.__state == "right":
                self.__state = None
                if self.rect.collidepoint(pos):
                    return True
        return False
    #=========================================================================#
    #                         Check your button state                         #
    def get_state(self) -> str | None:
        return self.__state

    def set_state(self, state):
        if state == None:
            self.__state = None
        if state == 0:
            self.__state = "left"
        if state == 1:
            self.__state = "right"
#=============================================================================#
